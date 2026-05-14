# Партнерські QBR звіти — Bolt Food UA

Автоматизовані квартальні бізнес-огляди для партнерів Bolt Food UA.

**Live:** https://mykhailobrynchak-dev.github.io/hophey-qbr-report/

## Структура

```
├── index.html                  ← головна сторінка з посиланнями на бренди
├── requirements.txt            ← спільні залежності
├── .github/workflows/
│   └── update-report.yml       ← один workflow оновлює всі звіти
├── hophey/                     ← HOP HEY
│   ├── generate_report.py
│   ├── template.html
│   ├── build_local.py
│   ├── report_data.json
│   └── index.html
├── loko/                       ← (приклад наступного бренду)
│   └── ...
```

## Як додати новий бренд

1. Створити папку: `назва_бренду/`
2. Скопіювати `hophey/generate_report.py` та `hophey/template.html`
3. Змінити `PARTNER_NAME` у `generate_report.py`
4. У `.github/workflows/update-report.yml` додати крок:
   ```yaml
   - name: Generate НАЗВА report
     env:
       DATABRICKS_HOST: ${{ secrets.DATABRICKS_HOST }}
       DATABRICKS_TOKEN: ${{ secrets.DATABRICKS_TOKEN }}
       DATABRICKS_WAREHOUSE_ID: ${{ secrets.DATABRICKS_WAREHOUSE_ID }}
     run: python назва_бренду/generate_report.py
   ```
5. У `index.html` (кореневий) додати запис у масив `brands`

## Секрети (GitHub Actions)

Додаються один раз на весь репозиторій:

| Секрет | Значення |
|--------|----------|
| `DATABRICKS_HOST` | `bolt-common.cloud.databricks.com` |
| `DATABRICKS_TOKEN` | Databricks Personal Access Token |
| `DATABRICKS_WAREHOUSE_ID` | `b39957853740b21d` |

## Джерела даних

- `ng_delivery_spark.fact_order_delivery` — замовлення
- `ng_delivery_spark.fact_provider_weekly` — тижневі метрики
- `ng_delivery_spark.dim_provider_v2` — довідник провайдерів
- `ng_delivery_spark.delivery_order_order_resolution` — причини скасувань
