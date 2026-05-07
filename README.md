# The 2026 Energy Security Gap: Oil Chokepoint Exposure, Strategic Reserves, and Renewable Transition Speed. 

## Project Overview
In February 2026, a major conflict in the Middle East led to the near-total closure of the Strait of Hormuz, disrupting approximately 20% of the global oil supply.

This project evaluates the **"Energy Security Gap"** - the vulnerability of nations based on their reliance on Middle Eastern oil and their ability to respond through strategic reserves and short-term demand adjustments.

Using 2023-2024 national energy data as a proxy for pre-crisis conditions, this analysis explores whether countries with higher exposure to oil supply disruptions demonstrate stronger resilience behaviors, including reduce oil consumption, increased renewable adoption, or reliance on strategic reserves.

---

## Research Question
> **How does exposure to Middle Eastern oil transit chokepoints relate to a country's emergency energy resilience, strategic reserve coverage, and renewable energy transition speed during the 2026 supply shock?**

### Secondary Questions
* **Buffer Analysis:** Which countries' Strategic Petroleum Reserves (SPR) are most capable of sustaining their economies during the current 18-million-barrel-per-day global deficit?
* **Policy Impact:** Does a higher "Policy Response Score" (per IEA's 2026 Tracker) lead to a measurable decrease in national fuel demand within the first 60 days of the conflict?
* **Transition Velocity:** Are high-exposure nations (e.g., India, China, Japan) outperforming lower-exposure nations in new renewable grid connections since March 2026?

---

## Variable Analyzed
* **Oil Exposure (%):** Estimated share of national oil consumption dependent on imports vulnerable to Middle Eastern supply disruptions.
* **Strategic Reserve Coverage (SPR Days):** Number of days a country can sustain oil demand using stored reserves.
* **Renewable Growth (%):** Year-over-year change in renewable electricity generation.
* **Oil Consumption Change (%):** Short-term change in national oil demand.

---

## Data Sources
* **IEA (2026):** _Middle East Maritime Chokepoints Shipping Monitor_ and _2026 Energy Crisis Policy Response Tracker_.
* **Our World in Data (OWID):** _Electricity Generation from Renewables (Ember 2026 Update)_.
* **World Bank:** National GDP and Energy Intensity datasets.

---

## Tools Used
* **SQL:** Data modeling, filtering, and grouping for exposure and behavior analysis.
* **Python (Pandas, Matplotlib):** Data cleaning and visualization (scatter plots, bar charts).
* **GitHub:** Documentation and version control.

--- 

## Analysis Plan
1. **Ingestion:** Pull 2026 shipping and policy data from the IEA and renewable TWh from OWID.
2. **SQL Integration:** Create a unified table linking country import sources to their renewable growth.
3. **Vulnerability Mapping:** Categorize countries into "High Risk/Slow Pivot," "High Risk/Fast Pivot," and "Resilient."
4. **Trend Analysis:** Use Python to visualize the correlation between the $150/bbl price peak and the uptick in EV sales/heat pump installations.

---

## Key Visualizations
* **Oil Exposure by Country (Bar Chart):** Highlights which countries are most vulnerable to supply disruptions.
* **Oil Consumption Change by Country (Bar Chart):** Shows how countries adjusted demand in response to energy pressures.
* **Oil Exposure vs Oil Consumption Change (Scatter Plot):** Examines whether higher exposure leads to stronger demand reduction.

---

## Key Findings

1. **Oil Exposure is Highly Concentrated**
   - Countries such as Japan and South Korea show extremely high exposure (~90%), while the United States, Canada, and Brazil exhibit near-zero exposure due to domestic production.

2. **High Exposure Does Not Guarantee Demand Reduction**
   - Japan significantly reduced oil consumption (~-5%), but other highly exposed countries like India and South Korea increased consumption.
   - This suggests that exposure alone does not drive immediate behavioral change.

3. **Weak Relationship Between Exposure and Behavior**
   - Scatter plot analysis shows no consistent correlation between oil exposure and short-term changes in oil demand.
   - Countries respond differently based on internal economic structure, not just external risk.

4. **Strategic Reserves Play a Critical Role**
   - Highly exposed countries (Japan, South Korea) maintain large strategic reserves, indicating reliance on stored capacity rather than rapid demand reduction.

5. **Short-Term Response Favors Stability Over Transition**
   - Countries primarily rely on existing infrastructure (reserves and supply chains) rather than accelerating renewable energy adoption in the immediate term.

---

## Recommendations

1. **Increase Strategic Reserve Capacity in High-Exposure Countries**
   - Countries with high import dependence but low reserve coverage (e.g., India) remain highly vulnerable.

2. **Diversify Energy Supply Chains**
   - Reducing reliance on single-region imports can significantly improve resilience.

3. **Invest in Long-Term Renewable Infrastructure**
   - While renewables do not provide immediate crisis response, they reduce structural vulnerability over time.

4. **Develop Rapid Demand-Response Policies**
   - Behavioral and policy tools (e.g., fuel restrictions, efficiency measures) are necessary to complement physical reserves.

5. **Align Crisis Planning with Energy Transition Goals**
   - Current responses prioritize stability, but future strategies should integrate both resilience and decarbonization.

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
