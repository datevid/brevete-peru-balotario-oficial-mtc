# Brevete Perú — Balotarios Oficiales MTC 2026 en PDF & Recursos de Estudio Open Source

[![Build Status](https://github.com/datevid/brevete-peru-balotario-oficial-mtc/actions/workflows/validate-banks.yml/badge.svg)](https://github.com/datevid/brevete-peru-balotario-oficial-mtc/actions)
[![MTC 2026](https://img.shields.io/badge/MTC_Normativa-2026_Actualizado-blue.svg)](https://www.brevete.net.pe)
[![Plataforma Web](https://img.shields.io/badge/Simulador_Web-Brevete.net.pe-0ea5e9.svg)](https://www.brevete.net.pe)
[![Balotarios PDF](https://img.shields.io/badge/Balotarios_PDF-9_Categorías-red.svg)](balotarios-pdf/)
[![Tarjetas Anki](https://img.shields.io/badge/Tarjetas_Anki-9_Mazos_.apkg-8b5cf6.svg)](https://www.brevete.net.pe/simulacros/a1/tarjetas)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Repositorio oficial y abierto de **balotarios oficiales en PDF del MTC con archivo histórico, mazos de tarjetas Anki (.apkg), balotarios en Markdown y guía del Circuito de Manejo de Comas (Lima Norte)** para la obtención de licencias de conducir en el Perú, mantenido con fines cívicos por [Brevete.net.pe](https://www.brevete.net.pe).

> ### 🚗 ¿Deseas practicar el examen con cronómetro oficial de 40 minutos, voz y en tu móvil?
> Ingresa gratis al simulador web en vivo sin registros ni publicidad invasiva:  
> 👉 **[https://www.brevete.net.pe](https://www.brevete.net.pe)**

---

## 📑 Tabla de Contenidos

1. [Balotarios Oficiales en PDF (Vigentes e Históricos)](#-balotarios-oficiales-en-pdf-vigentes-e-históricos)
2. [Estructura del Repositorio](#-estructura-del-repositorio)
3. [Tarjetas Anki (.apkg) de Repetición Espaciada](#-tarjetas-anki-apkg-de-repetición-espaciada)
4. [Balotarios en Formato Markdown](#-balotarios-en-formato-markdown)
5. [Circuito de Manejo Oficial Comas Lima Norte](#-circuito-de-manejo-oficial-comas-lima-norte)
6. [Base Legal y Fuentes Oficiales](#-base-legal-y-fuentes-oficiales)
7. [Contribuciones y Licencia](#-contribuciones-y-licencia)

---

## 📄 Balotarios Oficiales en PDF (Vigentes e Históricos)

Todos los balotarios corresponden a los documentos oficiales expedidos por el Ministerio de Transportes y Comunicaciones (MTC) para el año **2026**, organizados en [`balotarios-pdf/2026-vigente/`](balotarios-pdf/2026-vigente/):

| Categoría | Denominación y Vehículos | Preguntas | Balotario Oficial PDF | Tarjetas Anki (.apkg) | Simulador Web Interactivo |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **A-I** | Particular (Sedanes, SUVs, Hatchbacks) | **200** | [`Descargar PDF`](balotarios-pdf/2026-vigente/balotario-oficial-mtc-a1-2026.pdf) | [`Descargar .apkg`](tarjetas-anki/brevete_mtc_a1_2026.apkg) | [Simulador A-I](https://www.brevete.net.pe/simulacros/a1) |
| **A-IIa** | Profesional (Taxi, Colectivo, Escolar) | **224** | [`Descargar PDF`](balotarios-pdf/2026-vigente/balotario-oficial-mtc-a2a-2026.pdf) | [`Descargar .apkg`](tarjetas-anki/brevete_mtc_a2a_2026.apkg) | [Simulador A-IIa](https://www.brevete.net.pe/simulacros/a2a) |
| **A-IIb** | Cúster, Combi y Camiones hasta 12 TN | **270** | [`Descargar PDF`](balotarios-pdf/2026-vigente/balotario-oficial-mtc-a2b-2026.pdf) | [`Descargar .apkg`](tarjetas-anki/brevete_mtc_a2b_2026.apkg) | [Simulador A-IIb](https://www.brevete.net.pe/simulacros/a2b) |
| **A-IIIa** | Buses y Ómnibus Interprovinciales | **272** | [`Descargar PDF`](balotarios-pdf/2026-vigente/balotario-oficial-mtc-a3a-2026.pdf) | [`Descargar .apkg`](tarjetas-anki/brevete_mtc_a3a_2026.apkg) | [Simulador A-IIIa](https://www.brevete.net.pe/simulacros/a3a) |
| **A-IIIb** | Camiones Pesados y Tráilers (>12 TN) | **271** | [`Descargar PDF`](balotarios-pdf/2026-vigente/balotario-oficial-mtc-a3b-2026.pdf) | [`Descargar .apkg`](tarjetas-anki/brevete_mtc_a3b_2026.apkg) | [Simulador A-IIIb](https://www.brevete.net.pe/simulacros/a3b) |
| **A-IIIc** | Máxima Integral Especializada (M3 + N3) | **339** | [`Descargar PDF`](balotarios-pdf/2026-vigente/balotario-oficial-mtc-a3c-2026.pdf) | [`Descargar .apkg`](tarjetas-anki/brevete_mtc_a3c_2026.apkg) | [Simulador A-IIIc](https://www.brevete.net.pe/simulacros/a3c) |
| **B-IIa** | Bicimotos y Vehículos Menores Livianos | **204** | [`Descargar PDF`](balotarios-pdf/2026-vigente/balotario-oficial-mtc-b2a-2026.pdf) | [`Descargar .apkg`](tarjetas-anki/brevete_mtc_b2a_2026.apkg) | [Simulador B-IIa](https://www.brevete.net.pe/simulacros/b2a) |
| **B-IIb** | Motocicletas Lineales | **204** | [`Descargar PDF`](balotarios-pdf/2026-vigente/balotario-oficial-mtc-b2b-motos-2026.pdf) | [`Descargar .apkg`](tarjetas-anki/brevete_mtc_b2b_2026.apkg) | [Simulador B-IIb](https://www.brevete.net.pe/simulacros/b2b) |
| **B-IIc** | Trimóviles, Pasajeros y Mototaxis | **244** | [`Descargar PDF`](balotarios-pdf/2026-vigente/balotario-oficial-mtc-b2c-mototaxis-2026.pdf) | [`Descargar .apkg`](tarjetas-anki/brevete_mtc_b2c_2026.apkg) | [Simulador B-IIc](https://www.brevete.net.pe/simulacros/b2c) |

### Política de Archivo Histórico
Cuando el MTC publica reformas normativas (ej. cambios en reglamentos o límites de velocidad), los PDFs anteriores no se eliminan: se preservan en [`balotarios-pdf/historico/`](balotarios-pdf/historico/) organizados por año y fecha, garantizando la trazabilidad cívica del marco regulatorio peruano.

---

## 📁 Estructura del Repositorio

```text
brevete-peru-balotario-oficial-mtc/
├── README.md                              # Documentación general y enlaces canónicos
├── LICENSE                                # Licencia abierta MIT
├── .github/workflows/validate-banks.yml   # CI/CD de validación automática en GitHub Actions
├── balotarios-pdf/                        # Balotarios oficiales en PDF organizados por fecha
│   ├── README.md                          # Guía de descarga y trazabilidad
│   ├── 2026-vigente/                      # 9 PDFs oficiales MTC vigentes
│   │   ├── balotario-oficial-mtc-a1-2026.pdf
│   │   ├── balotario-oficial-mtc-a2a-2026.pdf
│   │   └── ...
│   └── historico/                         # Preservación de versiones previas del MTC
│       └── README.md
├── balotarios-markdown/                   # Balotarios para lectura directa en GitHub
│   ├── BALOTARIO_OFICIAL_A1_MTC.md
│   └── ...
├── circuitos-evaluacion/                  # Guía de la sede oficial de manejo en Lima Norte
│   └── CIRCUITO_OFICIAL_COMAS_LIMA_NORTE.md
├── tarjetas-anki/                         # 9 paquetes .apkg legítimos para Anki Desktop y AnkiDroid
│   ├── brevete_mtc_a1_2026.apkg
│   └── ...
└── scripts/                               # Scripts reproducibles de compilación y verificación
    ├── build_apkg_packages.py
    ├── export-questions.cjs
    └── validate-repo.js
```

---

## 🗂 Tarjetas Anki (.apkg) de Repetición Espaciada

En la carpeta [`tarjetas-anki/`](tarjetas-anki/) encontrarás **9 archivos binarios `.apkg` legítimos**, generados con base de datos SQLite `collection.anki2` estándar y las señales de tránsito embebidas:

1. **En PC (Windows / macOS / Linux):** Abre [Anki Desktop](https://apps.ankiweb.net/), pulsa *Archivo > Importar* y selecciona el archivo `.apkg`.
2. **En Móvil (Android):** Instala [AnkiDroid](https://play.google.com/store/apps/details?id=com.ichi2.anki) y abre directamente el archivo descargado.
3. **En la Web:** También puedes usar el visor interactivo sin instalar nada en [https://www.brevete.net.pe/simulacros/a1/tarjetas](https://www.brevete.net.pe/simulacros/a1/tarjetas).

---

## 📖 Balotarios en Formato Markdown

Para una lectura ágil sin necesidad de lector de PDF ni descargas, consulta los balotarios directamente en la web de GitHub en [`balotarios-markdown/`](balotarios-markdown/):

* [Balotario Oficial A-I (Particular)](balotarios-markdown/BALOTARIO_OFICIAL_A1_MTC.md)
* [Balotario Oficial A-IIa (Taxi y Escolar)](balotarios-markdown/BALOTARIO_OFICIAL_A2A_MTC.md)
* [Balotario Oficial A-IIb (Cúster y Carga)](balotarios-markdown/BALOTARIO_OFICIAL_A2B_MTC.md)
* [Balotario Oficial B-IIb (Motos)](balotarios-markdown/BALOTARIO_OFICIAL_MOTOS_B2B.md)
* [Balotario Oficial B-IIc (Mototaxis)](balotarios-markdown/BALOTARIO_OFICIAL_MOTOTAXIS_B2C.md)

---

## 🏁 Circuito de Manejo Oficial Comas Lima Norte

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
