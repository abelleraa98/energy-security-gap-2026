# The 2026 Energy Security Gap: Oil Chokepoint Exposure, Strategic Reserves, and Renewable Transition Speed. 

## Project Overview
In February 2026, a major conflict in the Middle East led to the near-total closure of the Strait of Hormuz, disrupting 20% of the global energy supply. This project evaluates the **"Energy Security Gap"** – the vulnerability of nations based on their reliance on Middle Eastern oil and their speed of transition to renewable alternatives. It monitors how countries are examining whether high-exposure countries are accelerating clean energy adoption and emergency demand-reduction policies in response to the 2026 supply shock.  

---

## Research Question
> **How does exposure to Middle Eastern oil transit chokepoints relate to a country's emergency energy resilience, strategic reserve coverage, and renewable energy transition speed during the 2026 supply shock?**

### Secondary Questions
* **Buffer Analysis:** Which countries' Strategic Petroleum Reserves (SPR) are most capable of sustaining their economies during the current 18-million-barrel-per-day global deficit?
* **Policy Impact:** Does a higher "Policy Response Score" (per IEA's 2026 Tracker) lead to a measurable decrease in national fuel demand within the first 60 days of the conflict?
* **Transition Velocity:** Are high-exposure nations (e.g., India, China, Japan) outperforming lower-exposure nations in new renewable grid connections since March 2026?

---

## Variable Analyzed
* **Oil Chokepoint Exposure:** % of national oil imports that pass through the Strait of Hormuz.
* **Strategic Reserve Coverage:** Days of net-import coverage provided by the national Strategic Petroleum Reserves.
* **Renewable Transition Speed:** YoY growth rate in TWh (Terawatt-hours) of solar and wind generation.
* **Emergency Demand Response:** % change in national oil consumption post-February 2026.
* **Energy Policy Response Score**

---

## Data Sources
* **IEA (2026):** _Middle East Maritime Chokepoints Shipping Monitor_ and _2026 Energy Crisis Policy Response Tracker_.
* **Our World in Data (OWID):** _Electricity Generation from Renewables (Ember 2026 Update)_.
* **World Bank:** National GDP and Energy Intensity datasets.

---

## Tools Used
* **SQL:** For data modeling, joining trade flow datasets, and calculating the Resilience Index.
* **Python (Pandas/Matplotlib):** For time-series analysis of oil price spikes ($150/bbl) vs. renewable investment.
* **GitHub:** For documentation and version control.

--- 

## Analysis Plan
1. **Ingestion:** Pull 2026 shipping and policy data from the IEA and renewable TWh from OWID.
2. **SQL Integration:** Create a unified table linking country import sources to their renewable growth.
3. **Vulnerability Mapping:** Categorize countries into "High Risk/Slow Pivot," "High Risk/Fast Pivot," and "Resilient."
4. **Trend Analysis:** Use Python to visualize the correlation between the $150/bbl price peak and the uptick in EV sales/heat pump installations.

---

## Key Visualizations
_(Coming Soon)_
* Global Map of Oil Chokepoint Exposure vs SPR Levels.
* The "Resilience Gap" Scatter Plot: Import Reliance vs. Renewable Growth.

---

## Key Findings
_(Coming Soon)_

---

## Recommendations
_(Coming Soon)_

---

## Repository Structure
```text
├── data/               # Raw datasets from IEA, OWID, and World Bank
├── cleaned/            # Data that has been processed via SQL/Python
├── analysis/           # SQL scripts and Jupyter Notebooks (.ipynb)
├── visualizations/     # Exported charts, maps, and PNGs
├── report/             # Final summary of findings and policy insights
└── README.md           # Project documentation
```

---

## Purpose of the Project
This project is part of my transition from Psychology to Data Analytics. It applies behavioral insights and data system analysis to development economics, specifically focusing on how global crises catalyze structural shifts in energy consumption.

---

## Author
Arshalisha Abellera

_Junior Data Analyst_
