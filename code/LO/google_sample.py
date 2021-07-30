"""
A linear optimization example

One of the oldest and most widely-used areas of optimization is linear optimization
(or linear programming), in which the objective function and the constraints can 
be written as linear expressions. Here's a simple example of this type of problem.

Maximize 3x + y subject to the following constraints:
    0	≤	x	≤	1
    0	≤	y	≤	2
    		x + y	≤	2

The objective function in this example is 3x + y. 
Both the objective function and the constraints are given by linear expressions, 
which makes this a linear problem.

>> source: https://developers.google.com/optimization/introduction/python 
"""

from ortools.linear_solver import pywraplp

def main():
    # Create the linear solver with the GLOP backend.
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Create the variables x and y.
    x = solver.NumVar(0, 1, 'x')
    y = solver.NumVar(0, 2, 'y')

    print('Number of variables =', solver.NumVariables())

    # Create a linear constraint, 0 <= x + y <= 2.
    ct = solver.Constraint(0, 2, 'ct')
    ct.SetCoefficient(x, 1)
    ct.SetCoefficient(y, 1)

    print('Number of constraints =', solver.NumConstraints())

    # Create the objective function, 3 * x + y.
    objective = solver.Objective()
    objective.SetCoefficient(x, 3)
    objective.SetCoefficient(y, 1)
    objective.SetMaximization()

    solver.Solve()

    print('Solution:')
    print('Objective value =', objective.Value())
    print('x =', x.solution_value())
    print('y =', y.solution_value())


if __name__ == '__main__':
    main()