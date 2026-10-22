# Brevete Perú — Balotario Oficial MTC 2026 & Simulador Open Source

[![Build Status](https://github.com/datevid/brevete-peru-balotario-oficial-mtc/actions/workflows/validate-banks.yml/badge.svg)](https://github.com/datevid/brevete-peru-balotario-oficial-mtc/actions)
[![MTC 2026](https://img.shields.io/badge/MTC_Normativa-2026_Actualizado-blue.svg)](https://www.brevete.net.pe)
[![Plataforma Web](https://img.shields.io/badge/Simulador_Web-Brevete.net.pe-0ea5e9.svg)](https://www.brevete.net.pe)
[![Tarjetas Anki](https://img.shields.io/badge/Tarjetas_Anki-9_Mazos_.apkg-8b5cf6.svg)](https://www.brevete.net.pe/simulacros/a1/tarjetas)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Repositorio oficial y abierto de **datos cívicos, bancos de preguntas, balotarios auditados en formato JSON/Markdown, mazos de tarjetas Anki (.apkg) y guía del Circuito de Manejo de Comas (Lima Norte)** para la obtención de licencias de conducir en el Perú, mantenido por [Brevete.net.pe](https://www.brevete.net.pe).

> ### 🚗 ¿Deseas practicar el examen con cronómetro oficial de 40 minutos, voz y en tu móvil?
> Ingresa gratis al simulador web en vivo sin registros ni publicidad invasiva:  
> 👉 **[https://www.brevete.net.pe](https://www.brevete.net.pe)**

---

## 📑 Tabla de Contenidos

1. [Categorías Incluidas y Estadísticas](#-categorías-incluidas-y-estadísticas)
2. [Estructura del Repositorio](#-estructura-del-repositorio)
3. [Cómo Utilizar los Archivos JSON](#-cómo-utilizar-los-archivos-json)
4. [Tarjetas Anki (.apkg) de Repetición Espaciada](#-tarjetas-anki-apkg-de-repetición-espaciada)
5. [Simulador en Terminal (CLI)](#-simulador-en-terminal-cli)
6. [Circuito de Manejo Comas Lima Norte](#-circuito-de-manejo-comas-lima-norte)
7. [Base Legal y Fuentes Oficiales](#-base-legal-y-fuentes-oficiales)
8. [Contribuciones y Licencia](#-contribuciones-y-licencia)

---

## 📊 Categorías Incluidas y Estadísticas

Todos los bancos corresponden a la versión oficial auditada del MTC para el año **2026**:

| Categoría | Denominación y Vehículos | Preguntas | JSON | Tarjetas Anki (.apkg) | Simulador Web |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **A-I** | Particular (Sedanes, SUVs, Hatchbacks) | **200** | [`Ver JSON`](balotarios-json/balotario-mtc-a1-2026.json) | [`Descargar .apkg`](tarjetas-anki/brevete_mtc_a1_2026.apkg) | [Brevete A-I](https://www.brevete.net.pe/simulacros/a1) |
| **A-IIa** | Profesional (Taxi, Colectivo, Escolar) | **224** | [`Ver JSON`](balotarios-json/balotario-mtc-a2a-2026.json) | [`Descargar .apkg`](tarjetas-anki/brevete_mtc_a2a_2026.apkg) | [Brevete A-IIa](https://www.brevete.net.pe/simulacros/a2a) |
| **A-IIb** | Cúster, Combi y Camiones hasta 12 TN | **270** | [`Ver JSON`](balotarios-json/balotario-mtc-a2b-2026.json) | [`Descargar .apkg`](tarjetas-anki/brevete_mtc_a2b_2026.apkg) | [Brevete A-IIb](https://www.brevete.net.pe/simulacros/a2b) |
| **A-IIIa** | Buses y Ómnibus Interprovinciales | **272** | [`Ver JSON`](balotarios-json/balotario-mtc-a3a-2026.json) | [`Descargar .apkg`](tarjetas-anki/brevete_mtc_a3a_2026.apkg) | [Brevete A-IIIa](https://www.brevete.net.pe/simulacros/a3a) |
| **A-IIIb** | Camiones Pesados y Tráilers (>12 TN) | **271** | [`Ver JSON`](balotarios-json/balotario-mtc-a3b-2026.json) | [`Descargar .apkg`](tarjetas-anki/brevete_mtc_a3b_2026.apkg) | [Brevete A-IIIb](https://www.brevete.net.pe/simulacros/a3b) |
| **A-IIIc** | Máxima Integral Especializada (M3 + N3) | **339** | [`Ver JSON`](balotarios-json/balotario-mtc-a3c-2026.json) | [`Descargar .apkg`](tarjetas-anki/brevete_mtc_a3c_2026.apkg) | [Brevete A-IIIc](https://www.brevete.net.pe/simulacros/a3c) |
| **B-IIa** | Bicimotos y Vehículos Menores Livianos | **204** | [`Ver JSON`](balotarios-json/balotario-mtc-b2a-2026.json) | [`Descargar .apkg`](tarjetas-anki/brevete_mtc_b2a_2026.apkg) | [Brevete B-IIa](https://www.brevete.net.pe/simulacros/b2a) |
| **B-IIb** | Motocicletas Lineales | **204** | [`Ver JSON`](balotarios-json/balotario-mtc-b2b-motos-2026.json) | [`Descargar .apkg`](tarjetas-anki/brevete_mtc_b2b_2026.apkg) | [Brevete B-IIb](https://www.brevete.net.pe/simulacros/b2b) |
| **B-IIc** | Trimóviles, Pasajeros y Mototaxis | **244** | [`Ver JSON`](balotarios-json/balotario-mtc-b2c-mototaxis-2026.json) | [`Descargar .apkg`](tarjetas-anki/brevete_mtc_b2c_2026.apkg) | [Brevete B-IIc](https://www.brevete.net.pe/simulacros/b2c) |

---

## 📁 Estructura del Repositorio

```text
brevete-peru-balotario-oficial-mtc/
├── README.md                              # Documentación general y enlaces canónicos
├── LICENSE                                # Licencia abierta MIT
├── .github/workflows/validate-banks.yml   # CI/CD de validación automática
├── balotarios-json/                       # 9 bancos de preguntas estructurados en JSON
│   ├── balotario-mtc-a1-2026.json
│   ├── balotario-mtc-a2a-2026.json
│   └── ...
├── balotarios-markdown/                   # Balotarios listos para lectura directa en GitHub
│   ├── BALOTARIO_OFICIAL_A1_MTC.md
│   └── ...
├── circuitos-evaluacion/                  # Guía de la sede oficial de manejo en Lima
│   └── CIRCUITO_OFICIAL_COMAS_LIMA_NORTE.md
├── tarjetas-anki/                         # 9 paquetes .apkg legítimos para Anki Desktop y AnkiDroid
│   ├── brevete_mtc_a1_2026.apkg
│   └── ...
├── scripts/                               # Scripts reproducibles de extracción y compilación SQLite
│   ├── export-questions.cjs
│   ├── build_apkg_packages.py
│   └── validate-json.js
└── cli-simulator/                         # Simulador de examen interactivo en consola
    ├── package.json
    └── simular.js
```

---

## 💻 Cómo Utilizar los Archivos JSON

Los archivos en `balotarios-json/` son ideales para desarrolladores, investigadores o educadores viales:

### Esquema de cada pregunta:
```json
{
  "id": 4,
  "materia": "Dispositivos de Control de Tránsito",
  "tema": "Señales Reguladoras",
  "enunciado": "La siguiente señal (R-30A)...",
  "tieneImagen": true,
  "imagenReferencia": "q004_senal_r_3-1.jpg",
  "opciones": [
    { "letra": "A", "texto": "Regula la velocidad máxima permitida en curva." },
    { "letra": "B", "texto": "Indica zona escolar." },
    { "letra": "C", "texto": "Prohíbe adelantar." },
    { "letra": "D", "texto": "Ninguna de las anteriores." }
  ],
  "respuestaCorrecta": {
    "indice": 0,
    "letra": "A",
    "texto": "Regula la velocidad máxima permitida en curva."
  },
  "baseLegal": "Manual de Dispositivos de Control de Tránsito para Calles y Carreteras (R.D. N° 016-2016-MTC/14)",
  "explicacion": "La señal R-30A es de cumplimiento obligatorio..."
}
```

### Ejemplo de consumo en Python:
```python
import json

with open('balotarios-json/balotario-mtc-a1-2026.json', 'r', encoding='utf-8') as f:
    banco = json.load(f)

print(f"Total de preguntas: {banco['metadata']['totalPreguntas']}")
for q in banco['preguntas'][:3]:
    print(f"[{q['id']}] {q['enunciado']} -> Rpta: {q['respuestaCorrecta']['letra']}")
```

---

## 🗂 Tarjetas Anki (.apkg) de Repetición Espaciada

En la carpeta [`tarjetas-anki/`](tarjetas-anki/) encontrarás **9 archivos binarios `.apkg` legítimos**, generados con base de datos SQLite `collection.anki2` estándar y las señales de tránsito embebidas:

1. **En PC (Windows / macOS / Linux):** Abre [Anki Desktop](https://apps.ankiweb.net/), pulsa *Archivo > Importar* y selecciona el archivo `.apkg`.
2. **En Móvil (Android):** Instala [AnkiDroid](https://play.google.com/store/apps/details?id=com.ichi2.anki) y abre directamente el archivo descargado.
3. **En la Web:** También puedes usar el visor nativo sin instalar nada en [https://www.brevete.net.pe/simulacros/a1/tarjetas](https://www.brevete.net.pe/simulacros/a1/tarjetas).

---

## ⌨ Simulador en Terminal (CLI)

Puedes rendir un simulacro de 40 preguntas directamente desde tu terminal:

```bash
cd cli-simulator
node simular.js
```

Al finalizar, te indicará si estás **APROBADO** ($ge 35$ puntos) o **DESAPROBADO** con desglose por pregunta.

---

## 🏁 Circuito de Manejo Comas Lima Norte

Tras la conclusión del convenio histórico con el Touring en Conchán, la Municipalidad Metropolitana de Lima (MML) centralizó las evaluaciones oficiales de manejo en el **Circuito Vial Lima Norte en Comas**.

Consulta la guía completa de Rutas A y B, faltas eliminatorias, cronómetro de 3 segundos en ciclovía roja y estacionamientos en:  
👉 [`circuitos-evaluacion/CIRCUITO_OFICIAL_COMAS_LIMA_NORTE.md`](circuitos-evaluacion/CIRCUITO_OFICIAL_COMAS_LIMA_NORTE.md)  
👉 Simulador interactivo en línea: [https://www.brevete.net.pe/simulacros/a1/circuito](https://www.brevete.net.pe/simulacros/a1/circuito)

---

## ⚖ Base Legal y Fuentes Oficiales

* **D.S. N° 016-2009-MTC** — Texto Único Ordenado del Reglamento Nacional de Tránsito.
* **D.S. N° 007-2016-MTC** — Reglamento Nacional del Sistema de Emisión de Licencias de Conducir.
* **R.D. N° 016-2016-MTC/15** — Balotarios Oficiales de Preguntas para la Evaluación de Conocimientos.
* **D.S. N° 025-2021-MTC** — Modificación de Límites Máximos de Velocidad en Zonas Urbanas y Carreteras.

---

## 🤝 Contribuciones y Atribución

Este proyecto es de código abierto con fines de utilidad cívica y educación vial ciudadana.

* **Proyecto Principal:** [Brevete.net.pe](https://www.brevete.net.pe)
* **Licencia de Código y Datos:** [Licencia MIT](LICENSE)
