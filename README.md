# HOP HEY — Бізнес-огляд

Автоматизований бізнес-огляд для партнера HOP HEY × Bolt Food UA.

**Live:** https://mykhailobrynchak-dev.github.io/hophey-qbr-reports/

## Структура

| Файл | Призначення |
|------|-------------|
| `generate_report.py` | Databricks SQL → `index.html` |
| `template.html` | HTML-шаблон із Chart.js (2 вкладки: Місяці / Тижні) |
| `build_local.py` | Локальна збірка з `report_data.json` |
| `report_data.json` | Кешовані дані |
| `index.html` | Готовий звіт |

## Автоматичне оновлення

Щопонеділка о 08:00 за Києвом через GitHub Actions.

## Секрети (GitHub Actions)

| Секрет | Значення |
|--------|----------|
| `DATABRICKS_HOST` | `bolt-common.cloud.databricks.com` |
| `DATABRICKS_TOKEN` | Databricks Personal Access Token |
| `DATABRICKS_WAREHOUSE_ID` | `b39957853740b21d` |
