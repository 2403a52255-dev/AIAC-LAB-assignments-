"""
Simple Linear Optimization Template
"""

import pulp

def solve_linear_problem():
    """
    Simple template for linear optimization problems
    """
    # Create problem (LpMaximize or LpMinimize)
    prob = pulp.LpProblem("Problem", pulp.LpMaximize)
    
    # Define variables
    x = pulp.LpVariable("x", lowBound=0)
    y = pulp.LpVariable("y", lowBound=0)
    
    # Objective function (example: maximize 3x + 2y)
    prob += 3 * x + 2 * y
    
    # Constraints (example)
    prob += x + y <= 10  # constraint 1
    prob += 2 * x + y <= 15  # constraint 2
    
    # Solve
    prob.solve()
    
    # Results
    print(f"Status: {pulp.LpStatus[prob.status]}")
    print(f"Optimal value: {pulp.value(prob.objective)}")
    print(f"x = {x.varValue}")
    print(f"y = {y.varValue}")

if __name__ == "__main__":
    solve_linear_problem()
    print("\nInstall: pip install pulp")
