from typing import Self

from sympy.matrices.expressions import MatrixExpr

class DFT(MatrixExpr):
    def __new__(cls, n) -> Self: ...

    n = ...
    shape = ...

class IDFT(DFT): ...
