"""
A GENERALIZED linear optimization example

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

    lb = [0,0] # lower boundaries
    ub = [1,2] # upper boundaries
    f = [3,1] # objective function coefficients
    a = [1,1] # constrain coefficients
    b = [2] # constrain boundary

    # Create the linear solver with the GLOP backend.
    solver = pywraplp.Solver('simple_lp_program', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)


    # Create the variables x and y.
    # Format: solver.NumVar(lower boundary, upper boundary, label)
    x = solver.NumVar(lb[0], ub[0], 'x')
    y = solver.NumVar(lb[1], ub[1], 'y')

    # Create a linear constraint, 1+y <= 2
    ct = solver.Constraint(-solver.infinity(), b[0], 'ct')
    ct.SetCoefficient(x, a[0])
    ct.SetCoefficient(y, a[1])

    # Create the objective function, 3 * x + y.
    objective = solver.Objective()
    objective.SetCoefficient(x, f[0])
    objective.SetCoefficient(y, f[1])
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