from typing import Literal, Self

from sympy.core.basic import Basic
from sympy.core.function import Function, UndefinedFunction
from sympy.core.mul import Mul

class DiracDelta(Function):
    is_real = ...
    def fdiff(self, argindex=...) -> Self: ...
    @classmethod
    def eval(cls, arg, k=...) -> Mul | Self | None: ...
    def is_simple(self, x) -> Literal[False]: ...

class Heaviside(Function):
    is_real = ...
    def fdiff(self, argindex=...) -> type[UndefinedFunction]: ...
    def __new__(cls, arg, H0=..., **options): ...
    @property
    def pargs(self) -> tuple[Basic, ...]: ...
    @classmethod
    def eval(cls, arg, H0=...) -> None: ...
