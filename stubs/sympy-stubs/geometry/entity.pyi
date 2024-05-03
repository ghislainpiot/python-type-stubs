from typing import Any, Self

from sympy.core.basic import Basic
from sympy.core.evalf import EvalfMixin
from sympy.multipledispatch import dispatch
from sympy.sets import Set
from sympy.sets.sets import FiniteSet, Union

ordering_of_classes = ...
T = ...

class GeometryEntity(Basic, EvalfMixin):
    __slots__: tuple[str, ...] = ...
    def __cmp__(self, other) -> int: ...
    def __contains__(self, other): ...
    def __getnewargs__(self) -> tuple[Basic, ...]: ...
    def __ne__(self, o) -> bool: ...
    def __new__(cls, *args, **kwargs) -> Self: ...
    def __radd__(self, a): ...
    def __rtruediv__(self, a): ...
    def __repr__(self) -> str: ...
    def __rmul__(self, a): ...
    def __rsub__(self, a): ...
    def __str__(self) -> str: ...
    @property
    def ambient_dimension(self): ...
    @property
    def bounds(self): ...
    def encloses(self, o) -> bool: ...
    def equals(self, o): ...
    def intersection(self, o): ...
    def is_similar(self, other): ...
    def reflect(self, line) -> Self: ...
    def rotate(self, angle, pt=...) -> Self: ...
    def scale(self, x=..., y=..., pt=...) -> Self: ...
    def translate(self, x=..., y=...) -> Self: ...
    def parameter_value(self, other, t) -> dict[Any, Any]: ...

class GeometrySet(GeometryEntity, Set):
    __slots__ = ...

@dispatch(GeometrySet, Set)
def union_sets(self, o) -> FiniteSet | Union | None: ...
@dispatch(GeometrySet, Set)
def intersection_sets(self, o) -> FiniteSet | Union | None: ...
def translate(x, y): ...
def scale(x, y, pt=...): ...
def rotate(th): ...