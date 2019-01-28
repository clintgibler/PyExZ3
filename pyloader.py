# Copyright: copyright.txt

import inspect
from symbolic.invocation import FunctionInvocation
from symbolic.symbolic_types import SymbolicInteger

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

from symbolic.explore import ExplorationEngine

def exploreFunction(fn):
    engine = ExplorationEngine(createInvocation(fn), solver='z3')
    generatedinputs, returnvals, path = engine.explore(0)
    return generatedInputs, returnVals, path

if __name__ == '__main__':
    import simple
    return explore(simple.simple)
    print(returnVals)
