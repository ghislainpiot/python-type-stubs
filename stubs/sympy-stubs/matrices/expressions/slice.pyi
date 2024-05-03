from typing import Any, Literal, Self

from sympy.core.function import UndefinedFunction
from sympy.matrices.expressions.matexpr import MatrixExpr

def normalize(i, parentsize) -> tuple[Any | Literal[0], Any, Any | Literal[1]]: ...

class MatrixSlice(MatrixExpr):
    parent = ...
    rowslice = ...
    colslice = ...
    def __new__(cls, parent, rowslice, colslice) -> MatrixSlice | Self: ...
    @property
    def shape(self) -> tuple[Any | type[UndefinedFunction], Any | type[UndefinedFunction]]: ...
    @property
    def on_diag(self) -> Any: ...

def slice_of_slice(s, t) -> tuple[Any, Any, Any]: ...
def mat_slice_of_slice(parent, rowslice, colslice) -> MatrixSlice: ...