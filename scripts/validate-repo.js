/**
 * Script de validación de integridad para GitHub Actions
 * Verifica la estructura de balotarios, paquetes .apkg y Markdown del repositorio.
 */
const fs = require('fs');
const path = require('path');
const assert = require('assert/strict');

const root = path.resolve(__dirname, '..');
const pdfDir = path.join(root, 'balotarios-pdf');
const ankiDir = path.join(root, 'tarjetas-anki');
const mdDir = path.join(root, 'balotarios-markdown');
const circuitDir = path.join(root, 'circuitos-evaluacion');

console.log('🔍 1. Validando directorio y guía de Balotarios PDF...');
const pdfReadme = path.join(pdfDir, 'README.md');
assert.ok(fs.existsSync(pdfReadme), 'Falta el archivo balotarios-pdf/README.md');
const pdfReadmeContent = fs.readFileSync(pdfReadme, 'utf8');
assert.ok(pdfReadmeContent.includes('brevete.net.pe/licencias'), 'README de balotarios-pdf debe incluir enlaces a Brevete.net.pe');
console.log('  ✔ balotarios-pdf/README.md con enlaces canónicos de descarga verificado.');

console.log('\n🔍 2. Validando paquetes Anki (.apkg)...');
const ankiFiles = fs.readdirSync(ankiDir).filter(f => f.endsWith('.apkg'));
assert.ok(ankiFiles.length >= 9, 'Deben existir al menos 9 archivos .apkg');

for (const f of ankiFiles) {
  const stat = fs.statSync(path.join(ankiDir, f));
  assert.ok(stat.size > 10000, `Archivo Anki ${f} sospechosamente pequeño (${stat.size} bytes)`);
  console.log(`  ✔ ${f}: ${(stat.size / 1024).toFixed(1)} KB (OK)`);
}

console.log('\n🔍 3. Validando balotarios en Markdown...');
const mdFiles = fs.readdirSync(mdDir).filter(f => f.endsWith('.md'));
assert.ok(mdFiles.length >= 5, 'Deben existir al menos 5 balotarios en Markdown');
for (const f of mdFiles) {
  const stat = fs.statSync(path.join(mdDir, f));
  assert.ok(stat.size > 5000, `Archivo Markdown ${f} muy pequeño (${stat.size} bytes)`);
  console.log(`  ✔ ${f}: ${(stat.size / 1024).toFixed(1)} KB (OK)`);
}

console.log('\n🔍 4. Validando documentación de Circuito Oficial de Comas...');
const circuitDoc = path.join(circuitDir, 'CIRCUITO_OFICIAL_COMAS_LIMA_NORTE.md');
assert.ok(fs.existsSync(circuitDoc), 'Falta la guía del Circuito de Comas');
console.log('  ✔ CIRCUITO_OFICIAL_COMAS_LIMA_NORTE.md (OK)');

console.log('\n✅ TODAS LAS VALIDACIONES PASARON EXITOSAMENTE.');
