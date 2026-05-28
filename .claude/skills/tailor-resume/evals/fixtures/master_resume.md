# Alex Tan

Sydney, Australia · alex.tan@example.com · +61 4xx xxx xxx · linkedin.com/in/alextan · github.com/alextan

## Summary

Data engineer with 6+ years of experience designing and operating analytical and operational data systems across fintech, e-commerce, and B2B SaaS. Comfortable across the full stack — ingestion, warehousing, transformation, orchestration, BI enablement — and equally happy diving into infra or partnering directly with business stakeholders. Australian Permanent Resident.

## Experience

### Senior Data Engineer — Lumen Health (Series C HealthTech, ~300 ppl)
*Mar 2022 – Present · Sydney*

- Led migration of the analytics warehouse from Redshift to Snowflake; consolidated 12 disjointed ingestion paths into a single Fivetran + dbt pipeline, cutting nightly batch runtime from 6h to 90m and reducing infra spend ~35%.
- Owned the dbt project end-to-end (~400 models): set up CI with SQLFluff and dbt build on PRs, introduced exposure-based ownership tags, and rolled out a model-deprecation process that retired 80+ stale models in the first quarter.
- Designed and implemented a column-level lineage + data-quality framework on top of dbt tests, Elementary, and a custom Slack alerting service; reduced average time-to-detect for upstream schema breaks from days to under 30 minutes.
- Partnered with the Analytics team to build a semantic layer (Cube) over the core revenue and engagement marts; 9 of 11 product squads now self-serve their dashboards instead of routing through analytics, reducing ad-hoc ticket volume ~60%.
- Mentored 3 engineers (one promoted to mid, one onboarded from a non-DE background); ran a weekly internal "warehouse office hours" attended by ~15 non-DE engineers and PMs.
- Represented data eng in the company's PII/PHI handling working group with Security and Legal; co-authored the internal data-classification policy now applied across all new ingestion sources.

### Data Engineer — Drift Commerce (Series B B2C e-commerce, ~80 ppl)
*Jul 2019 – Feb 2022 · Melbourne*

- First data hire. Stood up the company's first warehouse (BigQuery), ingestion (Airbyte + custom Python connectors), transformation (dbt), and BI (Looker) — single-handedly for the first 9 months, then with one direct report.
- Shipped a real-time event pipeline (Pub/Sub → Dataflow → BigQuery) feeding personalization features; reduced event-to-warehouse latency from "next-day" to ~30 seconds.
- Built the experimentation data layer used by Product and Growth; ~200 experiments shipped through it in the first year, with the analysis SQL templates I wrote becoming the team standard.
- On-call for the data platform from day one — wrote the first runbooks, set up PagerDuty rotation when the team grew to three.
- Worked directly with founders on the company's first attempt at LTV modeling; my dbt-based CAC/LTV marts replaced a brittle spreadsheet workflow and became inputs to the Series B fundraise deck.
- Migrated 4 acquired companies' data stacks into Drift's warehouse over 18 months; designed the conformed dimension model that made cross-brand revenue reporting possible.

### Analytics Engineer — Northwind Capital (Boutique Australian asset manager, ~60 ppl)
*Feb 2018 – Jun 2019 · Sydney*

- Built and maintained internal reporting infrastructure for the investment and operations teams (SQL Server → SSAS → Power BI); modernized a stack that had been hand-maintained in Excel for ~10 years.
- Designed a position and exposure data mart consumed by the daily risk report; replaced an analyst's 3-hour manual workbook compilation with a 5-minute automated run.
- Partnered with Compliance on the firm's first automated daily mandate-check report; flagged limit breaches that had previously been caught only at month-end.
- Wrote the team's first SQL style guide and code-review process; trained 4 analysts in dimensional modeling fundamentals.

### Data Analyst (Intern → FT) — Bureau of Transport Insights (Government, ~200 ppl)
*Jan 2017 – Jan 2018 · Canberra*

- Built recurring traffic and freight reports for state government clients using SQL and R.
- Co-authored a published methodology note on imputing missing toll-road volumes.

## Projects

- **`dbt-elementary-slack`** — small open-source connector for routing Elementary test failures to Slack with model-owner mentions. ~120 GitHub stars.
- **Sydney transport delay dashboard** — personal project, scrapes TfNSW open data into DuckDB and surfaces in a Streamlit app. Featured in a local data meetup.

## Education

- **B.Sc. (Hons.), Statistics** — University of New South Wales, 2017. First-class honours. Thesis on time-series imputation methods.

## Skills

- **Warehouses / lakes:** Snowflake, BigQuery, Redshift, Databricks, DuckDB
- **Transformation:** dbt (advanced), SQL (advanced), Python (proficient)
- **Orchestration:** Airflow, Dagster (familiar), dbt Cloud, GitHub Actions
- **Ingestion / streaming:** Fivetran, Airbyte, Kafka, Pub/Sub, Dataflow
- **BI / semantic:** Looker, LookML, Cube, Power BI, Tableau (familiar)
- **Infra:** AWS (S3, IAM, ECS, Lambda), GCP (BigQuery, GCS, Cloud Run), Terraform (proficient), Docker
- **Quality / observability:** dbt tests, Elementary, Great Expectations (familiar), Monte Carlo (evaluated)
- **Practices:** Dimensional modeling (Kimball), data contracts, data product thinking, CI/CD for data, on-call ownership

## Certifications

- Snowflake SnowPro Core (2023)
- AWS Certified Data Analytics – Specialty (2022)
