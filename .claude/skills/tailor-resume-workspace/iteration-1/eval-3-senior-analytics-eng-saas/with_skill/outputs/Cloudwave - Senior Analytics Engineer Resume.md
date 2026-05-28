# Alex Tan

Sydney, Australia · alex.tan@example.com · +61 4xx xxx xxx · linkedin.com/in/alextan · github.com/alextan

## Summary

Senior analytics engineer with 6+ years building trusted data products on Snowflake, dbt, and Looker. Comfortable owning a large dbt project end-to-end — modeling, testing strategy, semantic layer, deprecation — and partnering directly with Finance, GTM, and Product stakeholders. Happy pushing back on modeling tradeoffs and equally happy mentoring juniors through them.

## Experience

### Senior Data Engineer — Lumen Health (Series C HealthTech, ~300 ppl)
*Mar 2022 – Present · Sydney*

- Own the dbt project end-to-end (~400 models on Snowflake): set CI standards with SQLFluff and dbt build on PRs, introduced exposure-based ownership tags, and rolled out a model-deprecation process that retired 80+ stale models in the first quarter.
- Led the semantic-layer initiative on Cube over the core revenue and engagement marts; 9 of 11 product squads now self-serve dashboards against consolidated metric definitions instead of routing through analytics, cutting ad-hoc ticket volume ~60%.
- Designed a column-level lineage and data-quality framework on top of dbt tests, Elementary, and a custom Slack alerting service; reduced average time-to-detect for upstream schema breaks from days to under 30 minutes.
- Led migration of the analytics warehouse from Redshift to Snowflake; consolidated 12 disjointed ingestion paths into a single Fivetran + dbt pipeline, cutting nightly batch runtime from 6h to 90m and reducing infra spend ~35%.
- Mentor 3 engineers (one promoted to mid, one onboarded from a non-DE background); review PRs, pair on harder modeling problems, and run a weekly "warehouse office hours" attended by ~15 non-DE engineers and PMs.
- Partner with Security and Legal on PII/PHI handling; co-authored the internal data-classification policy applied across all new ingestion sources — including the contracts between raw/staging and downstream marts.

### Data Engineer — Drift Commerce (Series B B2C e-commerce, ~80 ppl)
*Jul 2019 – Feb 2022 · Melbourne*

- First data hire. Stood up the company's warehouse (BigQuery), ingestion (Airbyte + Fivetran), transformation (dbt), and BI (Looker / LookML) — single-handedly for the first 9 months, then with one direct report.
- Worked directly with founders on the company's first LTV and CAC modeling; dbt-based marts replaced a brittle spreadsheet workflow and became inputs to the Series B fundraise deck.
- Built the experimentation data layer used by Product and Growth; ~200 experiments shipped through it in the first year, with the analysis SQL templates I wrote becoming the team standard.
- Migrated 4 acquired companies' data stacks into the warehouse over 18 months; designed the conformed dimension model that made cross-brand revenue reporting possible.

### Analytics Engineer — Northwind Capital (Boutique Australian asset manager, ~60 ppl)
*Feb 2018 – Jun 2019 · Sydney*

- Built and maintained internal reporting on SQL Server → SSAS → Power BI; modernized a stack that had been hand-maintained in Excel for ~10 years.
- Designed a position and exposure data mart consumed by the daily risk report; replaced an analyst's 3-hour manual workbook compilation with a 5-minute automated run, and partnered with Compliance on the firm's first automated daily mandate-check report.
- Wrote the team's first SQL style guide and code-review process; trained 4 analysts in dimensional modeling fundamentals.

### Data Analyst (Intern → FT) — Bureau of Transport Insights (Government, ~200 ppl)
*Jan 2017 – Jan 2018 · Canberra*

- Built recurring SQL/R reports for state government clients; co-authored a published methodology note on imputing missing toll-road volumes.

## Projects

- **`dbt-elementary-slack`** — small open-source connector for routing Elementary test failures to Slack with model-owner mentions. ~120 GitHub stars.

## Education

- **B.Sc. (Hons.), Statistics** — University of New South Wales, 2017. First-class honours. Thesis on time-series imputation methods.

## Skills

- **Warehouse & transformation:** Snowflake, dbt (advanced, ~400-model project), SQL (advanced), BigQuery, Redshift
- **Semantic / BI:** Cube, Looker / LookML, Power BI
- **Project hygiene & testing:** dbt tests, Elementary, SQLFluff, dbt-checkpoint, CI on PRs, exposures, model deprecation
- **Modeling:** Kimball-style dimensional modeling, conformed dimensions, data contracts, data product thinking
- **Ingestion & orchestration:** Fivetran, Airbyte, dbt Cloud, Airflow, GitHub Actions
- **Python & infra:** Python, AWS (S3, IAM, Lambda), GCP (BigQuery, GCS), Terraform, Docker

## Certifications

- Snowflake SnowPro Core (2023)
- AWS Certified Data Analytics – Specialty (2022)
