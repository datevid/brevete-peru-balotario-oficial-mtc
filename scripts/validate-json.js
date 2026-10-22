/**
 * Script de validación de integridad para GitHub Actions
 * Verifica que todos los JSONs sean válidos y que los paquetes .apkg existan.
 */
const fs = require('fs');
const path = require('path');
const assert = require('assert/strict');

const root = path.resolve(__dirname, '..');
const jsonDir = path.join(root, 'balotarios-json');
const ankiDir = path.join(root, 'tarjetas-anki');

console.log('🔍 Validando archivos JSON de balotarios...');
const jsonFiles = fs.readdirSync(jsonDir).filter(f => f.endsWith('.json'));
assert.ok(jsonFiles.length >= 9, 'Deben existir al menos 9 archivos JSON');

let totalQuestionsCount = 0;

for (const file of jsonFiles) {
  const filePath = path.join(jsonDir, file);
  const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
  
  assert.ok(data.metadata, `Falta metadata en ${file}`);
  assert.ok(Array.isArray(data.preguntas), `Faltan preguntas en ${file}`);
  assert.equal(data.metadata.totalPreguntas, data.preguntas.length, `Total anunciado no coincide en ${file}`);
  
  const ids = new Set();
  for (const q of data.preguntas) {
    assert.ok(typeof q.id === 'number', `ID no numérico en ${file}`);
    assert.ok(!ids.has(q.id), `ID duplicado ${q.id} en ${file}`);
    ids.add(q.id);
    assert.ok(q.enunciado && q.enunciado.length > 5, `Enunciado vacío en ${file} ID ${q.id}`);
    assert.ok(Array.isArray(q.opciones) && q.opciones.length >= 2, `Opciones insuficientes en ${file} ID ${q.id}`);
    assert.ok(q.respuestaCorrecta && typeof q.respuestaCorrecta.indice === 'number', `Falta respuesta en ${file} ID ${q.id}`);
    assert.ok(q.respuestaCorrecta.indice >= 0 && q.respuestaCorrecta.indice < q.opciones.length, `Índice fuera de rango en ${file} ID ${q.id}`);
  }
  
  totalQuestionsCount += data.preguntas.length;
  console.log(`  ✔ ${file}: ${data.preguntas.length} preguntas validadas correctamente.`);
}

console.log(`🔍 Validando paquetes Anki (.apkg)... Total de preguntas auditadas: ${totalQuestionsCount}`);
const ankiFiles = fs.readdirSync(ankiDir).filter(f => f.endsWith('.apkg'));
assert.ok(ankiFiles.length >= 9, 'Deben existir al menos 9 archivos .apkg');

for (const f of ankiFiles) {
  const stat = fs.statSync(path.join(ankiDir, f));
  assert.ok(stat.size > 10000, `Archivo Anki ${f} sospechosamente pequeño (${stat.size} bytes)`);
  console.log(`  ✔ ${f}: ${(stat.size / 1024).toFixed(1)} KB (OK)`);
}

console.log('✅ TODAS LAS VALIDACIONES PASARON EXITOSAMENTE.');
