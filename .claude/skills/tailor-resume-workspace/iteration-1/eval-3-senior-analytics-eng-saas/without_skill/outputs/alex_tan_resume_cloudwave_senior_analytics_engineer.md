# Alex Tan

Sydney, Australia · alex.tan@example.com · +61 4xx xxx xxx · linkedin.com/in/alextan · github.com/alextan

## Summary

Senior analytics engineer with 6+ years building trusted, well-modeled data products on Snowflake, dbt, and Looker across B2B SaaS, fintech, and e-commerce. Deep dbt expertise at scale (400+ models in current project), hands-on with semantic-layer rollouts (Cube), and a strong partner to Finance, GTM, and Product stakeholders. Comfortable as the senior IC who sets project standards, mentors junior engineers, and translates ambiguous business questions into reliable marts. Australian Permanent Resident.

## Experience

### Senior Data Engineer — Lumen Health (Series C HealthTech, ~300 ppl)
*Mar 2022 – Present · Sydney*

- Own the dbt project end-to-end (~400 models on Snowflake): set the model conventions, CI standards (SQLFluff + dbt build on PRs), exposure-based ownership tags, and a model-deprecation process that retired 80+ stale models in the first quarter — the same kind of project hygiene Cloudwave is hiring this role to raise.
- Designed and rolled out a semantic layer (Cube) over the core revenue and engagement marts so metric definitions are defined once and consumed everywhere; 9 of 11 product squads now self-serve their dashboards instead of routing through analytics, cutting ad-hoc ticket volume ~60%.
- Partner directly with Finance, Product, and GTM-adjacent stakeholders to translate ambiguous questions into well-modeled, well-documented, well-tested data products — including the revenue and engagement marts the exec team relies on.
- Led the migration of the analytics warehouse from Redshift to Snowflake; consolidated 12 disjointed ingestion paths into a single Fivetran + dbt pipeline, cutting nightly batch runtime from 6h to 90m and reducing infra spend ~35%.
- Built a column-level lineage + data-quality framework on top of dbt tests, Elementary, and a custom Slack alerting service; reduced time-to-detect for upstream schema breaks from days to under 30 minutes.
- Mentor 3 engineers (one promoted to mid, one onboarded from a non-DE background), review their PRs, and pair with them on harder modeling problems; run a weekly "warehouse office hours" attended by ~15 non-DE engineers and PMs.
- Partner with the data engineering function on contracts between raw/staging layers and downstream marts, including co-authoring the internal data-classification policy now applied across all new ingestion sources.

### Data Engineer — Drift Commerce (Series B B2C e-commerce, ~80 ppl)
*Jul 2019 – Feb 2022 · Melbourne*

- First data hire. Stood up the company's first warehouse (BigQuery), ingestion (Airbyte + custom Python connectors), transformation (dbt), and BI (Looker / LookML) — including the LookML conventions and explore structure the analytics team still uses.
- Built the experimentation data layer used by Product and Growth; ~200 experiments shipped through it in the first year, with the analysis SQL templates I wrote becoming the team standard.
- Worked directly with founders on the company's first attempt at LTV modeling; my dbt-based CAC/LTV marts replaced a brittle spreadsheet workflow and became inputs to the Series B fundraise deck — an early example of building data products business stakeholders actually trusted and used.
- Migrated 4 acquired companies' data stacks into Drift's warehouse over 18 months; designed the conformed (Kimball-style) dimension model that made cross-brand revenue reporting possible.
- Shipped a real-time event pipeline (Pub/Sub → Dataflow → BigQuery) feeding personalization features; reduced event-to-warehouse latency from "next-day" to ~30 seconds.

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
- **Sydney transport delay dashboard** — personal project, scrapes TfNSW open data into DuckDB and surfaces in a Streamlit app.

## Education

- **B.Sc. (Hons.), Statistics** — University of New South Wales, 2017. First-class honours.

## Skills

- **Transformation / modeling:** dbt (advanced, 400+ model project), SQL (advanced), dimensional modeling (Kimball), data contracts
- **Semantic / metrics layers:** Cube (production rollout), LookML, dbt Semantic Layer (familiar)
- **Warehouses:** Snowflake, BigQuery, Redshift, Databricks, DuckDB
- **BI:** Looker / LookML, Power BI, Tableau (familiar)
- **Ingestion:** Fivetran, Airbyte, custom Python ingestion services, Kafka, Pub/Sub, Dataflow
- **Quality / observability:** dbt tests, Elementary, SQLFluff, dbt-checkpoint, Great Expectations (familiar), Monte Carlo (evaluated)
- **Delivery:** dbt Cloud, GitHub Actions, dbt CI, Airflow, Dagster (familiar)
- **Infra:** AWS (S3, IAM, ECS, Lambda), GCP (BigQuery, GCS, Cloud Run), Terraform, Docker
- **Python:** proficient (ingestion services, internal tooling)

## Certifications

- Snowflake SnowPro Core (2023)
- AWS Certified Data Analytics – Specialty (2022)
