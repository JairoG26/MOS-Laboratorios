
from __future__ import division
from pyomo.environ import *

from pyomo.opt import SolverFactory

Model = ConcreteModel()

numHistorias = 11

p=RangeSet(1, numHistorias)

tareas = {1:(5,7),2:(3,5),3:(13,6),4:(1,3),5:(21,1),6:(2,4),7:(2,6),8:(5,4),9:(8,2),10:(13,7),11:(21,6)}

Model.x = Var(p, domain=Binary)

# Función objetivo
Model.obj = Objective(expr = sum(Model.x[i]*tareas[i][1] for i in p), sense=maximize)

# Restricciones
Model.res1 = Constraint(expr = sum(Model.x[i]*tareas[i][0] for i in p) <= 96)

# Especificación del solver
SolverFactory('glpk').solve(Model)

Model.display()