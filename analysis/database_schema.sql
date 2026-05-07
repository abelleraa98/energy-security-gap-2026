</> SQL

-- Purpose: Analyze country-level energy response during the 2026 crisis period (2024 data proxy)
-- This query compares oil exposure with renewable growth, oil demand changes, and reserve capacity.
-- Results are sorted by exposure to identify the most vulnerable countries first.

SELECT
	country,
	CAST (oil_exposure_pct as REAL) AS oil_exposure_pct,
	CAST (renewable_growth_pct as REAL) AS renewable_growth_pct,
	CAST(oil_consumption_change_pct as REAL) as oil_consumption_change_pct,
	CAST(spr_days_2026 as REAL) as spr_days_2026
FROM energy_security_master
WHERE year =2024
ORDER by oil_exposure_pct DESC;

---Purpose: Identify patterns in energy response based on exposure levels.
-- Countries are grouped into High, Medium, and Low exposure categories.
-- This query calculates average renewable growth, oil demand change, and reserve capacity for each group.
-- Helps determine whether higher exposure leads to stronger policy or energy transitions.

SELECT
	CASE
		WHEN CAST (oil_exposure_pct as REAL) >= 60 THEN 'High Exposure'
		WHEN CAST (oil_exposure_pct as REAL) >= 30 THEN 'Medium Exposure'
		ELSE 'Low Exposure'
	END as exposure_group,
	
	round(avg(cast(renewable_growth_pct as real)), 2) as avg_renewable_growth_pct,
	round(avg(cast(oil_consumption_change_pct as real)), 2) as avg_oil_consumption_change_pct,
	round(avg(cast(spr_days_2026 as real)), 2) as avg_spr_days_2026
	
FROM energy_security_master
WHERE year = 2024
GROUP by exposure_group
ORDER by avg_renewable_growth_pct DESC;

-- Purpose: Identify which countries reduced or increased oil consumption during the crisis period (2024).
-- Results are sorted by oil consumption change (largest reductions first),
-- and then by exposure level (high exposure first)
-- This allows analysis of whether highly exposed countries were more likely to reduce oil demand.

SELECT
	country,
	CAST (oil_consumption_change_pct as REAL) as oil_consumption_change_pct,
	CAST (oil_exposure_pct as REAL) as oil_exposure_pct
FROM energy_security_master
WHERE year = 2024
ORDER by oil_consumption_change_pct ASC, oil_exposure_pct DESC;
