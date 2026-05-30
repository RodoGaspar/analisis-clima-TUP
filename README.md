# Análisis de Temperatura Global 🌡️

## Integrantes
| Rol | Nombre | Tarea |
|-----|--------|-------|
| P1 - Líder | Rodolfo Gaspar Paredes | Inicialización del repositorio (SCRUM-1) |
| P2 - Desarrollador | Rodolfo Gaspar Paredes | Script de análisis climático (SCRUM-2) |
| P3 - Revisor QA | Rodolfo Gaspar Paredes | Revisión, documentación y merge (SCRUM-3) |

## Escenario
Escenario A – Análisis de Datos Climáticos

## Dataset
- **Fuente:** GCAG (Global Climate Analysis Group) vía datahub.io
- **URL:** https://datahub.io/core/global-temp
- **Formato:** CSV
- **Período:** 1850–2024
- **Licencia:** Dominio público

## Estructura del Repositorio

analisis-clima-TUP/
├── datos/
│   └── global_temp.csv
├── scripts/
│   └── analisis_climatico.py
├── resultados/
│   └── grafico_temperatura.png
├── README.md
└── .gitignore

## Indicadores Calculados
- Anomalía de temperatura promedio histórica
- Anomalía máxima y año correspondiente
- Anomalía mínima y año correspondiente
- Media móvil de 20 años

## Cómo ejecutar el script
1. Abrir Google Colab
2. Clonar el repositorio:
git clone https://github.com/RodoGaspar/analisis-clima-TUP.git
3. Ejecutar el script:
python scripts/analisis_climatico.py

## Gestión del Proyecto
Tablero Jira: Analisis-Clima-TUP
