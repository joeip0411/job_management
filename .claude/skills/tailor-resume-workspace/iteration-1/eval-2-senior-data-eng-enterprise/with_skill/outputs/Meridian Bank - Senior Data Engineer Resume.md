# Alex Tan

Sydney, Australia · alex.tan@example.com · +61 4xx xxx xxx · linkedin.com/in/alextan · github.com/alextan

## Summary

Senior data engineer with 6+ years designing and operating production-grade data pipelines on Snowflake and BigQuery, with a focus on data quality, lineage, and governance. Experienced partnering with Security, Legal, and analytics consumers to deliver well-modelled, certified data products. Australian Permanent Resident.

## Experience

### Senior Data Engineer — Lumen Health (Series C HealthTech, ~300 staff)
*Mar 2022 – Present · Sydney*

- Designed and led migration of the enterprise analytics warehouse from Redshift to Snowflake; consolidated 12 ingestion paths into a single Fivetran + dbt framework, reducing nightly batch runtime from 6 hours to 90 minutes and lowering infrastructure spend by approximately 35%.
- Owned the dbt project end-to-end (~400 models), establishing engineering standards including CI with SQLFluff and `dbt build` on PRs, exposure-based ownership tags, and a formal model-deprecation process that retired 80+ stale models in the first quarter.
- Designed and implemented a column-level data lineage and data quality framework on dbt tests, Elementary, and a custom alerting service; reduced mean time-to-detect for upstream schema breaks from days to under 30 minutes, improving observability across downstream consuming teams.
- Represented data engineering on the company's PII/PHI handling working group with Security and Legal; co-authored the internal data classification policy now applied across all new ingestion sources — directly comparable to a Data Management Policy environment.
- Partnered with the Analytics function to build a governed semantic layer (Cube) over the core revenue and engagement marts, enabling 9 of 11 product squads to self-serve from certified data products and reducing ad-hoc request volume by approximately 60%.
- Mentored 3 mid-level engineers (one promoted to mid-level, one transitioned from a non-DE background) and ran a recurring "warehouse office hours" forum attended by ~15 engineers and product managers.

### Data Engineer — Drift Commerce (Series B B2C e-commerce, ~80 staff)
*Jul 2019 – Feb 2022 · Melbourne*

- Established the company's first enterprise data platform from the ground up: warehouse (BigQuery), ingestion (Airbyte and custom Python connectors), transformation (dbt), and BI (Looker).
- Designed and delivered a conformed dimensional model (Kimball) consolidating four acquired companies' data stacks into a single warehouse over 18 months, enabling cross-brand revenue reporting and reconciliation.
- Built the experimentation data layer used by Product and Growth, including standardised analysis SQL templates adopted as the team standard across ~200 experiments in the first year.
- Operated the data platform on-call from day one; authored the team's first runbooks and stood up the PagerDuty rotation and incident management process as the team scaled.
- Delivered a real-time event pipeline (Pub/Sub → Dataflow → BigQuery), reducing event-to-warehouse latency from next-day to ~30 seconds for downstream personalisation use cases.

### Analytics Engineer — Northwind Capital (Boutique Australian asset manager, ~60 staff)
*Feb 2018 – Jun 2019 · Sydney*

- Designed and maintained internal reporting infrastructure for investment and operations functions (SQL Server → SSAS → Power BI), modernising a stack previously hand-maintained in Excel for ~10 years.
- Designed a position and exposure data mart consumed by the daily risk report, replacing a 3-hour manual workbook process with a 5-minute automated, reconciled run.
- Partnered with Compliance to deliver the firm's first automated daily mandate-check report, surfacing limit breaches that had previously been detected only at month-end.
- Authored the team's first SQL style guide and code review process; trained 4 analysts in dimensional modelling fundamentals.

### Data Analyst (Intern → Full-time) — Bureau of Transport Insights (Government, ~200 staff)
*Jan 2017 – Jan 2018 · Canberra*

- Delivered recurring traffic and freight reports for state government clients using SQL and R.
- Co-authored a published methodology note on imputing missing toll-road volumes.

## Education

- **B.Sc. (Hons.), Statistics** — University of New South Wales, 2017. First-class honours. Thesis on time-series imputation methods.

## Skills

- **Cloud data warehouses:** Snowflake, BigQuery, Redshift, Databricks
- **Transformation & modelling:** dbt (advanced), SQL (advanced), dimensional modelling (Kimball), data contracts
- **Data quality & observability:** dbt tests, Elementary, Great Expectations, column-level lineage frameworks
- **Ingestion & orchestration:** Fivetran, Airbyte, Airflow, dbt Cloud, GitHub Actions
- **Infrastructure-as-code & cloud:** Terraform (proficient), AWS (S3, IAM, ECS, Lambda), Docker
- **Governance & practices:** PII/PHI classification, data product thinking, CI/CD for data, on-call and incident management

## Certifications

- Snowflake SnowPro Core (2023)
- AWS Certified Data Analytics – Specialty (2022)
