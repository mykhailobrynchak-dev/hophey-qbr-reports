# HOP HEY — QBR Report (автоматичний)

Автоматизований квартальний бізнес-огляд для партнера HOP HEY × Bolt Food UA.

**Live:** [index.html](index.html)

## Структура

| Файл | Призначення |
|------|-------------|
| `generate_report.py` | Основний скрипт: запити до Databricks → `index.html` |
| `template.html` | HTML-шаблон з Chart.js та JavaScript рендерингом |
| `build_local.py` | Локальна збірка з `report_data.json` (без Databricks) |
| `report_data.json` | Останній знімок даних (генерується MCP або generate_report.py) |
| `index.html` | Готовий звіт |

## Запуск

### Через `generate_report.py` (потрібен `databricks-sql-connector`)

```bash
pip install -r requirements.txt

export DATABRICKS_HOST="bolt-common.cloud.databricks.com"
export DATABRICKS_TOKEN="..."
export DATABRICKS_WAREHOUSE_ID="b39957853740b21d"

python generate_report.py
```

### Локально з кешованими даними

```bash
python build_local.py
```

## Секрети (GitHub Actions)

| Secret | Опис |
|--------|------|
| `DATABRICKS_HOST` | `bolt-common.cloud.databricks.com` |
| `DATABRICKS_TOKEN` | Databricks Personal Access Token |
| `DATABRICKS_WAREHOUSE_ID` | `b39957853740b21d` (Common SQL) |

## Джерела даних

- `ng_delivery_spark.fact_order_delivery` — замовлення (фінанси, операційка)
- `ng_delivery_spark.fact_provider_weekly` — тижневі агреговані метрики провайдерів
- `ng_delivery_spark.dim_provider_v2` — довідник провайдерів
- `ng_delivery_spark.delivery_order_order_resolution` — причини скасувань

## Блоки звіту

1. **KPI Summary** — ключові показники останнього місяця
2. **Зростання та продажі** — Merchant Price, Orders, AOV, Users
3. **Залучення користувачів** — Users Activated, Active Users, Active Merchants
4. **Операційна якість** — Failed/Bad/Honey rates, Duration, Late rates, Adjustment/Replacement, Merchants/Availability, Rating
5. **Failed Orders** — детальний аналіз причин скасувань
6. **Інвестиції** — кампанії Bolt/Merchant
7. **Мережа закладів** — Топ-15 за Merchant Price
8. **Зведена KPI таблиця** — всі місяці
