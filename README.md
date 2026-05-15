# Stores QBR Reports

Автоматизовані квартальні бізнес-огляди для партнерів Bolt Food UA.

## Звіти

| Партнер | Папка | Live | Оновлення |
|---------|-------|------|-----------|
| HOP HEY | `/` (root) | [Відкрити](https://mykhailobrynchak-dev.github.io/stores-qbr-reports/) | Пн 08:00 Київ |
| CAFE RYNOK | `/cafe-rynok/` | [Відкрити](https://mykhailobrynchak-dev.github.io/stores-qbr-reports/cafe-rynok/) | Пн 07:00 Київ |

## Структура

```
├── generate_report.py      # HOP HEY: Databricks → index.html
├── template.html           # HOP HEY: HTML-шаблон
├── index.html              # HOP HEY: готовий звіт
├── report_data.json        # HOP HEY: кешовані дані
├── cafe-rynok/
│   ├── generate_report.py  # CAFE RYNOK: Databricks → index.html
│   ├── template.html       # CAFE RYNOK: HTML-шаблон (3 вкладки: Місяці / Тижні / Локації)
│   ├── index.html          # CAFE RYNOK: готовий звіт
│   └── report_data.json    # CAFE RYNOK: кешовані дані
└── .github/workflows/
    ├── update-report.yml       # HOP HEY workflow
    └── update-cafe-rynok.yml   # CAFE RYNOK workflow
```

## Автоматичне оновлення

Обидва звіти оновлюються щопонеділка через GitHub Actions.

## Секрети (GitHub Actions)

| Секрет | Значення |
|--------|----------|
| `DATABRICKS_HOST` | `bolt-common.cloud.databricks.com` |
| `DATABRICKS_TOKEN` | Databricks Personal Access Token |
| `DATABRICKS_WAREHOUSE_ID` | `b39957853740b21d` |
