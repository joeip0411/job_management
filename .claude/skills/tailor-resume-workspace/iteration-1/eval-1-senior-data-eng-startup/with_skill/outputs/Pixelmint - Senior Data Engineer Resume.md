# Alex Tan

Sydney, Australia · alex.tan@example.com · +61 4xx xxx xxx · linkedin.com/in/alextan · github.com/alextan

## Summary

Data engineer with 6+ years owning analytics and operational data end-to-end across startups and scale-ups — including two stints as the first or second data hire. Deep dbt + Snowflake, comfortable shipping Python in production, and equally happy wiring up a new ingestion path on a Tuesday as I am sitting in a growth review on Wednesday. Bias to ship a scrappy v1 and iterate. Australian Permanent Resident.

## Experience

### Senior Data Engineer — Lumen Health (Series C HealthTech, ~300 ppl)
*Mar 2022 – Present · Sydney*

- Migrated the analytics warehouse to Snowflake and consolidated 12 messy ingestion paths into a single Fivetran + dbt pipeline — cut nightly runtime from 6h to 90m and trimmed infra spend ~35%.
- Owned the dbt project end-to-end (~400 models): CI on every PR, ownership tags by exposure, and a model-deprecation process that killed 80+ stale models in a quarter.
- Shipped a column-level lineage + data-quality layer on top of dbt tests, Elementary, and a custom Slack alerter — time-to-detect upstream schema breaks went from days to under 30 minutes.
- Built a Cube semantic layer over the revenue and engagement marts so 9 of 11 product squads now self-serve their dashboards; ad-hoc ticket volume dropped ~60%.
- Mentored 3 engineers (one promoted, one onboarded from outside data eng) and ran weekly "warehouse office hours" for ~15 PMs and engineers.

### Data Engineer — Drift Commerce (Series B e-commerce, ~80 ppl)
*Jul 2019 – Feb 2022 · Melbourne*

- First data hire. Stood up the warehouse (BigQuery), ingestion (Airbyte + custom Python connectors), dbt, and BI (Looker) solo for 9 months, then with one hire. No handoffs — if it broke at 7am, it was mine.
- Built the experimentation data layer from zero for Product and Growth; ~200 A/B tests shipped through it in the first year and my analysis SQL templates became the team default.
- Shipped a real-time event pipeline (Pub/Sub → Dataflow → BigQuery) feeding personalization — event-to-warehouse latency went from next-day to ~30 seconds.
- On-call from day one. Wrote the first runbooks and set up PagerDuty rotation once the team hit three.
- Paired directly with the founders on the first CAC/LTV model; my dbt marts replaced a brittle spreadsheet and went into the Series B fundraise deck.
- Folded 4 acquired companies' stacks into the Drift warehouse over 18 months — designed the conformed dimension model that made cross-brand revenue reporting actually work.

### Analytics Engineer — Northwind Capital (Asset manager, ~60 ppl)
*Feb 2018 – Jun 2019 · Sydney*

- Built internal reporting infra (SQL Server → SSAS → Power BI) for investment and ops teams; replaced a 10-year-old Excel stack.
- Designed the position/exposure mart behind the daily risk report — 3-hour manual workbook compressed to a 5-minute automated run.

### Data Analyst — Bureau of Transport Insights
*Jan 2017 – Jan 2018 · Canberra*

- Built recurring traffic and freight reports in SQL and R; co-authored a published methodology note on imputing missing toll-road volumes.

## Projects

- **`dbt-elementary-slack`** — open-source connector routing Elementary test failures to Slack with model-owner mentions. ~120 GitHub stars.
- **Sydney transport delay dashboard** — scrapes TfNSW open data into DuckDB, surfaces it in Streamlit. Featured at a local data meetup.

## Education

- **B.Sc. (Hons.), Statistics** — University of New South Wales, 2017. First-class honours.

## Skills

- **Warehouse / transformation:** Snowflake, BigQuery, dbt (advanced), SQL (advanced)
- **Ingestion / streaming:** Fivetran, Airbyte, custom Python connectors, Pub/Sub, Dataflow, Kafka
- **Languages:** Python (proficient), SQL
- **BI / semantic:** Hex (familiar), Looker, LookML, Cube
- **Infra:** AWS (S3, IAM, ECS, Lambda), GCP (BigQuery, GCS, Cloud Run), Terraform, Docker, GitHub Actions
- **Quality / observability:** dbt tests, Elementary, on-call ownership, runbooks
- **Practices:** Dimensional modeling, experimentation data layers, data contracts, CI/CD for data, shipping scrappy v1s

## Certifications

- Snowflake SnowPro Core (2023)
- AWS Certified Data Analytics – Specialty (2022)
