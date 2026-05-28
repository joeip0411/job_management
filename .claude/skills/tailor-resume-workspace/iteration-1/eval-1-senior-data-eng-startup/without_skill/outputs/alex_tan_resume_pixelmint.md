# Alex Tan

Sydney, Australia · alex.tan@example.com · +61 4xx xxx xxx · linkedin.com/in/alextan · github.com/alextan

## Summary

Data engineer with 6+ years of experience owning data platforms end-to-end at startups and scale-ups — from product event ingestion through Snowflake, dbt, and the dashboards leadership reads on Monday morning. Have been the first data hire, stood up warehouses from scratch, and carried the pager when things broke. Bias to action: ship a scrappy v1, learn from it, iterate. Strong opinions on dbt and dimensional modeling, loosely held. Australian Permanent Resident.

## Experience

### Senior Data Engineer — Lumen Health (Series C HealthTech, ~300 ppl)
*Mar 2022 – Present · Sydney*

- Own the Snowflake + dbt + Fivetran stack end-to-end. Led the migration off Redshift, consolidated 12 ad-hoc ingestion paths into one Fivetran + dbt pipeline, cut nightly batch from 6h to 90m, and dropped infra spend ~35%.
- Run a ~400-model dbt project: CI on every PR (SQLFluff + dbt build), ownership tags, and a deprecation process that retired 80+ stale models in a quarter. Shipped changes weekly, not quarterly.
- Built a column-level lineage + data-quality layer on dbt tests, Elementary, and a custom Slack alerter — cut time-to-detect upstream schema breaks from days to under 30 minutes. On-call rotation; first responder when the Monday dashboards are wrong.
- Partnered directly with PMs and growth-adjacent squads on the metrics that actually drive the business; stood up a Cube semantic layer over revenue and engagement marts so 9 of 11 product squads now self-serve instead of filing tickets (~60% drop in ad-hoc volume).
- Mentored 3 engineers and ran weekly "warehouse office hours" for ~15 PMs and non-DE engineers — informal, no process, just unblocking people.

### Data Engineer — Drift Commerce (Series B B2C e-commerce, ~80 ppl)
*Jul 2019 – Feb 2022 · Melbourne*

- First data hire. Stood up the warehouse (BigQuery), ingestion (Airbyte + custom Python connectors), transformation (dbt), and BI (Looker) solo for 9 months, then with one report. Duct tape where it had to be, real engineering where it counted.
- Built the experimentation data layer used by Product and Growth from scratch — ~200 A/B tests shipped through it in year one, and the SQL templates I wrote became the team standard.
- Shipped new ingestion paths fast: partner integrations, third-party APIs, and a real-time event pipeline (Pub/Sub → Dataflow → BigQuery) that took event-to-warehouse latency from "next-day" to ~30 seconds.
- On-call from day one. Wrote the first runbooks, set up PagerDuty when the team grew to three, and was the person paged at 7am when something broke.
- Sat directly with the founders on the first CAC/LTV model; replaced a brittle spreadsheet with dbt-based marts that fed the Series B fundraise deck.
- Integrated 4 acquired companies' stacks into the warehouse over 18 months; designed the conformed dimension model that made cross-brand revenue reporting possible.

### Analytics Engineer — Northwind Capital (Boutique Australian asset manager, ~60 ppl)
*Feb 2018 – Jun 2019 · Sydney*

- Rebuilt internal reporting (SQL Server → SSAS → Power BI), replacing a decade of hand-maintained Excel.
- Designed the position/exposure mart behind the daily risk report — turned a 3-hour manual workbook into a 5-minute automated run.
- Wrote the team's first SQL style guide and trained 4 analysts in dimensional modeling.

### Data Analyst (Intern → FT) — Bureau of Transport Insights (Government, ~200 ppl)
*Jan 2017 – Jan 2018 · Canberra*

- Built recurring traffic and freight reports for state government clients using SQL and R.

## Projects

- **`dbt-elementary-slack`** — open-source connector routing Elementary test failures to Slack with model-owner mentions. ~120 GitHub stars.
- **Sydney transport delay dashboard** — personal project, scrapes TfNSW open data into DuckDB, surfaced in a Streamlit app.

## Education

- **B.Sc. (Hons.), Statistics** — University of New South Wales, 2017. First-class honours.

## Skills

- **Core stack:** Snowflake (advanced), dbt (advanced), Fivetran, Python (production), SQL (advanced)
- **BI / semantic:** Hex (familiar), Looker, LookML, Cube, Power BI
- **Ingestion / streaming:** Fivetran, Airbyte, custom Python connectors, Kafka, Pub/Sub, Dataflow
- **Orchestration:** Airflow, dbt Cloud, GitHub Actions, Dagster (familiar)
- **Infra:** AWS (S3, IAM, ECS, Lambda), GCP (BigQuery, GCS, Cloud Run), Terraform, Docker
- **Quality / observability:** dbt tests, Elementary, Great Expectations, custom Slack alerting
- **Practices:** First/second data hire experience, on-call ownership, dimensional modeling (Kimball), experimentation data layers, shipping scrappy v1s

## Certifications

- Snowflake SnowPro Core (2023)
- AWS Certified Data Analytics – Specialty (2022)
