#!/usr/bin/env node

/**
 * Simulador de Examen de Reglas MTC Clase A-I en Terminal
 * Desarrollado por Brevete.net.pe (https://www.brevete.net.pe)
 */

const fs = require('fs');
const path = require('path');
const readline = require('readline');

const jsonPath = path.join(__dirname, '..', 'balotarios-json', 'balotario-mtc-a1-2026.json');

if (!fs.existsSync(jsonPath)) {
  console.error('Error: No se encontró el archivo balotario-mtc-a1-2026.json');
  process.exit(1);
}

const data = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
const allQuestions = data.preguntas;

// Barajar y tomar 40 preguntas como en el examen oficial
function shuffle(array) {
  const arr = [...array];
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

const examQuestions = shuffle(allQuestions).slice(0, 40);

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

console.clear();
console.log('================================================================');
console.log('      SIMULADOR DE EXAMEN DE REGLAS MTC A-I 2026 EN CONSOLA     ');
console.log('                 Desarrollado por Brevete.net.pe                ');
console.log('================================================================');
console.log('Reglas del Examen:');
console.log('• Total de preguntas: 40 preguntas aleatorias del balotario oficial.');
console.log('• Nota mínima para aprobar: 35 aciertos (87.5%).');
console.log('• Para practicar con interfaz web, audio y tiempo real:');
console.log('  👉 https://www.brevete.net.pe/simulacros/a1\n');

let currentIndex = 0;
let correctCount = 0;
const results = [];

function askQuestion() {
  if (currentIndex >= examQuestions.length) {
    showResults();
    return;
  }

  const q = examQuestions[currentIndex];
  console.log(`\n--- Pregunta ${currentIndex + 1} de 40 [N° ${q.id} - ${q.materia}] ---`);
  console.log(q.enunciado);
  console.log('');
  q.opciones.forEach(opt => {
    console.log(`  [${opt.letra}] ${opt.texto}`);
  });

  rl.question('\nTu respuesta (A, B, C, D) o [Q] para salir: ', (answer) => {
    const cleaned = answer.trim().toUpperCase();
    if (cleaned === 'Q') {
      console.log('\nSimulacro cancelado por el usuario.');
      rl.close();
      return;
    }

    const validLetters = q.opciones.map(o => o.letra);
    if (!validLetters.includes(cleaned)) {
      console.log('⚠️ Opción inválida. Ingresa A, B, C o D.');
      askQuestion();
      return;
    }

    const isCorrect = cleaned === q.respuestaCorrecta.letra;
    if (isCorrect) {
      correctCount++;
      console.log('✔ ¡CORRECTO!');
    } else {
      console.log(`❌ INCORRECTO. La respuesta oficial es [ ${q.respuestaCorrecta.letra} ]: ${q.respuestaCorrecta.texto}`);
    }
    if (q.baseLegal) {
      console.log(`  ⚖ Base legal: ${q.baseLegal}`);
    }

    results.push({
      num: currentIndex + 1,
      id: q.id,
      userAnswer: cleaned,
      correctAnswer: q.respuestaCorrecta.letra,
      isCorrect
    });

    currentIndex++;
    askQuestion();
  });
}

function showResults() {
  rl.close();
  console.log('\n================================================================');
  console.log('                    RESULTADOS DEL SIMULACRO                    ');
  console.log('================================================================');
  const scorePercent = ((correctCount / 40) * 100).toFixed(1);
  console.log(`Respuestas correctas: ${correctCount} / 40 (${scorePercent}%)`);

  if (correctCount >= 35) {
    console.log('\n🎉 ¡APROBADO! Cumples con el estándar oficial del MTC (mínimo 35/40).');
  } else {
    console.log(`\n❌ DESAPROBADO. Necesitas mínimo 35 aciertos (te faltaron ${35 - correctCount}).`);
  }

  console.log('\nContinúa practicando con simuladores cronometrados y tarjetas Anki en:');
  console.log('👉 https://www.brevete.net.pe/simulacros/a1');
  console.log('👉 https://www.brevete.net.pe/simulacros/a1/tarjetas\n');
}

askQuestion();
