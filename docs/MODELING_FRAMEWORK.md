# Optimization Modeling Framework

## 1. Define decisions
Use business-readable variable names. Examples:
- `open_hub[city] ∈ {0,1}`
- `ship[origin,destination] ≥ 0`
- `full_time_staff[shift] ∈ Z+`
- `production[product] ≥ 0`

## 2. Define objective
Typical objectives:
- minimize total cost,
- minimize distance,
- maximize contribution/profit,
- maximize coverage,
- minimize staffing expense.

## 3. Translate business rules into constraints
Examples:
- capacity,
- demand satisfaction,
- coverage,
- assignment,
- balance/conservation,
- workforce availability,
- logical open/close links,
- resource limits.

## 4. Select domains
Continuous vs integer vs binary decisions are part of the business meaning, not an implementation detail.

## 5. Validate
Check feasibility, constraint binding/slack, objective calculation, units, and whether the mathematical solution makes operational sense.

## 6. Sensitivity
Evaluate how recommendations change when costs, capacity, demand, coverage radius, prices, or other assumptions move.
