"""
A linear optimization example

Dado o problema:
max  3x + y
s.t.
     0 <= x <= 1
     0 <= y <= 2
     x + y <= 2

>> source: Aula 316491 - Tópicos em Sistemas de Computação - Turma PO
"""

from ortools.linear_solver import pywraplp

def main():
    # define variables

    # Create the linear solver with the GLOP backend.
    solver = pywraplp.Solver('simple_lp_program', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)


    # Create the variables x and y.
    # Format: solver.NumVar(lower boundary, upper boundary, label)
    x = solver.NumVar(0, 1, 'x')
    y = solver.NumVar(0, 2, 'y')

    # Create a linear constraint, 1+y <= 2
    ct = solver.Constraint(-solver.infinity(), 2, 'ct')
    ct.SetCoefficient(x, 1)
    ct.SetCoefficient(y, 1)

    # Create the objective function, 3 * x + y.
    objective = solver.Objective()
    objective.SetCoefficient(x, 3)
    objective.SetCoefficient(y, 1)
    # define the problem as maximization
    objective.SetMaximization()

    # run solver
    solver.Solve()

    # print result
    print('Solution:')
    print('Objective value =', objective.Value())
    print('x =', x.solution_value())
    print('y =', y.solution_value())

if __name__ == '__main__':
    main()