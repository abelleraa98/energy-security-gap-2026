</> SQL
-- This table will house our cleaned energy security metrics
CREATE TABLE energy_security_master (
  iso_code VARCHAR(3) PRIMARY KEY,
  country_name VARCHAR(100),
  oil_import_reliance_pct FLOAT, -- Percentage of energy from oil
  hormuz_exposure_pct FLOAT, -- % of oil passing through the Strait
  renewable_growth_2026 FLOAT, --YoY growth in TWh
  spr_days_coverage INT, -- Daus of strategic oil reserves
  resilience_score FLOAT -- Calculated metric (Exposure vs. Transition)
);
