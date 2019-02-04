# Copyright: copyright.txt

import simple
import inspect
from symbolic.invocation import FunctionInvocation
from symbolic.symbolic_types import SymbolicInteger, SymbolicStr
from symbolic.explore import ExplorationEngine
from symbolic.loader import *

# The built-in definition of len wraps the return value in an int() constructor, destroying any symbolic types.
# By redefining len here we can preserve symbolic integer types.
import builtins
builtins.len = (lambda x : x.__len__())

def createInvocation(fn, symarg, reset=lambda: None):
    inv = FunctionInvocation(fn, reset)
    argspec = inspect.getargspec(fn)
    for a in argspec.args:
        if not a in inv.getNames():
            symarg(inv, a)
            #inv.addArgumentConstructor(a, 0, symarg)
    return inv

def exploreFunction(app, fn, solver='z3', max_iters=0, symarg=lambda n, v: SymbolicInteger(n, v)):
    loader = Loader(filename='',entry=fn, app=app)
    engine = ExplorationEngine(loader.createInvocation(), solver=solver)
    generatedInputs, returnVals, path = engine.explore(max_iters)
    return generatedInputs, returnVals, path

if __name__ == '__main__':
    genInputs, returnVals, path = exploreFunction(simple, simple.simple.__name__, symarg= lambda inv, a: inv.addArgumentConstructor(a, '', SymbolicStr))
    print(returnVals)
