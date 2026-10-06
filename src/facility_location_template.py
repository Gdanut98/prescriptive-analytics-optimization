"""Portfolio-safe Gurobi template illustrating facility-location structure."""
import gurobipy as gp
from gurobipy import GRB

def build_facility_location(facilities, customers, fixed_cost, eligible):
    model = gp.Model("facility_location")
    open_facility = model.addVars(facilities, vtype=GRB.BINARY, name="open")
    assign = model.addVars(customers, facilities, vtype=GRB.BINARY, name="assign")

    model.setObjective(
        gp.quicksum(fixed_cost[f] * open_facility[f] for f in facilities),
        GRB.MINIMIZE
    )

    for c in customers:
        model.addConstr(gp.quicksum(assign[c,f] for f in facilities) == 1)

    for c in customers:
        for f in facilities:
            model.addConstr(assign[c,f] <= open_facility[f])
            if not eligible[c,f]:
                model.addConstr(assign[c,f] == 0)

    return model, open_facility, assign
