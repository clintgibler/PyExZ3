# Copyright: copyright.txt

import inspect
from symbolic.invocation import FunctionInvocation
from symbolic.symbolic_types import SymbolicInteger
from symbolic.explore import ExplorationEngine

# The built-in definition of len wraps the return value in an int() constructor, destroying any symbolic types.
# By redefining len here we can preserve symbolic integer types.
import builtins
builtins.len = (lambda x : x.__len__())

def createInvocation(fn, reset=lambda: None):
    inv = FunctionInvocation(fn, reset)
    argspec = inspect.getargspec(fn)
    for a in argspec.args:
        if not a in inv.getNames():
            inv.addArgumentConstructor(a, 0, lambda n,v: SymbolicInteger(n,v))
    return inv

def exploreFunction(fn, solver='z3', max_iters=0):
    engine = ExplorationEngine(createInvocation(fn), solver=solver)
    generatedInputs, returnVals, path = engine.explore(max_iters)
    return generatedInputs, returnVals, path

if __name__ == '__main__':
    import simple
    genInputs, returnVals, path = exploreFunction(simple.simple)
    print(returnVals)
