# Alex Tan

Sydney, Australia · alex.tan@example.com · +61 4xx xxx xxx · linkedin.com/in/alextan · github.com/alextan

Australian Permanent Resident · Willing to undergo National Police and credit checks

## Summary

Senior data engineer with 6+ years designing, developing, and operating enterprise-grade data pipelines on Snowflake and dbt, including in regulated environments handling sensitive customer data (PII/PHI). Strong background in dimensional modeling (Kimball), data quality and observability frameworks, lineage and metadata management, and CI/CD for data. Experienced partnering with Security, Legal, Governance, and non-technical stakeholders to deliver certified, well-modeled data products. Comfortable contributing to design review forums, change processes, and platform-level capabilities.

## Experience

### Senior Data Engineer — Lumen Health (Series C HealthTech, ~300 ppl)
*Mar 2022 – Present · Sydney*

- Designed, developed, and operated production-grade ingestion and transformation pipelines on Snowflake (AWS) with dbt as the primary transformation framework; led migration from Redshift to Snowflake and consolidated 12 ingestion paths into a single Fivetran + dbt pipeline, reducing nightly batch runtime from 6h to 90m and infra spend ~35%.
- Owned the dbt project end-to-end (~400 models) with disciplined engineering standards: CI/CD via SQLFluff and `dbt build` on PRs, exposure-based ownership tags, structured model-deprecation process that retired 80+ stale models, and documentation conventions suitable for architecture and design review.
- Implemented a column-level lineage and data quality / observability framework on top of dbt tests, Elementary, and a custom Slack alerting service; reduced average time-to-detect for upstream schema breaks from days to under 30 minutes, and established reconciliation controls for critical revenue marts.
- Partnered with Data Governance, Security, and Legal in the company's PII/PHI handling working group; co-authored the internal data-classification policy now applied across all new ingestion sources, including controls for sensitive customer data and retention requirements.
- Built a semantic layer (Cube) over core revenue and engagement marts, partnering with non-technical analytics, product, and finance stakeholders to translate business requirements into well-modeled, certified data products; 9 of 11 product squads now self-serve.
- Provided subject matter expertise to downstream teams during onboarding to the platform; ran a weekly "warehouse office hours" attended by ~15 engineers, PMs, and analysts.
- Supported incident management for production pipelines, including root cause analysis, remediation, and post-incident review write-ups.
- Mentored 3 mid-level and junior engineers; contributed to team engineering standards and code review forums.

### Data Engineer — Drift Commerce (Series B B2C e-commerce, ~80 ppl)
*Jul 2019 – Feb 2022 · Melbourne*

- Designed and operated the company's first enterprise data platform: warehouse (BigQuery), ingestion (Airbyte + custom Python connectors), transformation (dbt), and BI (Looker), establishing engineering standards, CI/CD, and documentation practices from the ground up.
- Built and operated a real-time event ingestion pipeline (Pub/Sub → Dataflow → BigQuery) feeding personalization features; reduced event-to-warehouse latency from next-day to ~30 seconds.
- Designed the conformed dimensional model (Kimball) underpinning cross-brand revenue reporting after migrating 4 acquired companies' data stacks into Drift's warehouse over 18 months.
- Built the experimentation data layer used by Product and Growth (~200 experiments shipped in the first year); analysis SQL templates became the team standard.
- Partnered directly with founders and finance stakeholders to deliver CAC/LTV data products that replaced brittle spreadsheet workflows and fed external reporting.
- On-call from day one; authored the first runbooks and established PagerDuty rotation and incident response process as the team grew.

### Analytics Engineer — Northwind Capital (Boutique Australian asset manager, ~60 ppl)
*Feb 2018 – Jun 2019 · Sydney*

- Designed and maintained internal reporting infrastructure for investment and operations teams (SQL Server → SSAS → Power BI) in a regulated financial services environment; modernized a decade-old Excel-based stack.
- Designed a position and exposure data mart consumed by the daily risk report; replaced a 3-hour manual workbook process with a 5-minute automated run.
- Partnered with Compliance to deliver the firm's first automated daily mandate-check report, surfacing limit breaches that had previously only been caught at month-end — directly supporting regulatory and internal risk controls.
- Authored the team's first SQL style guide and code-review process; trained 4 analysts in dimensional modeling fundamentals.

### Data Analyst (Intern → FT) — Bureau of Transport Insights (Government, ~200 ppl)
*Jan 2017 – Jan 2018 · Canberra*

- Built recurring reporting for state government clients using SQL and R within a regulated public-sector data environment.
- Co-authored a published methodology note on imputing missing toll-road volumes.

## Projects

- **`dbt-elementary-slack`** — open-source connector routing Elementary test failures to Slack with model-owner mentions. ~120 GitHub stars.
- **Sydney transport delay dashboard** — personal project: TfNSW open data into DuckDB, surfaced via Streamlit.

## Education

- **B.Sc. (Hons.), Statistics** — University of New South Wales, 2017. First-class honours. Thesis on time-series imputation methods.

## Skills

- **Cloud data platforms:** Snowflake (primary), BigQuery, Redshift, Databricks, DuckDB; AWS (S3, IAM, ECS, Lambda)
- **Transformation:** dbt (advanced — project structure, testing, documentation, CI/CD), SQL (advanced), Python (proficient)
- **Data modeling:** Dimensional modeling (Kimball), conformed dimensions, data product / data mesh patterns, data contracts
- **Data quality, observability, lineage:** dbt tests, Elementary, column-level lineage, Great Expectations (familiar), Monte Carlo (evaluated), reconciliation controls
- **Governance:** PII/PHI classification, data retention, metadata management, partnering with Security, Legal, Compliance
- **Orchestration & CI/CD:** Airflow, Dagster (familiar), dbt Cloud, GitHub Actions
- **Ingestion / streaming:** Fivetran, Airbyte, Kafka, Pub/Sub, Dataflow
- **Infrastructure-as-code:** Terraform (proficient), Docker
- **BI / semantic:** Looker, LookML, Cube, Power BI, Tableau (familiar)
- **Delivery practices:** Design documentation for architecture review, change/CAB processes, on-call ownership, incident management, mentoring

## Certifications

- Snowflake SnowPro Core (2023)
- AWS Certified Data Analytics – Specialty (2022)
