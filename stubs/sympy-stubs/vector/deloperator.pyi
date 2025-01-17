from typing import Self

from sympy.core import Basic
from sympy.core.add import Add
from sympy.vector.operators import Curl, Divergence, Gradient
from sympy.vector.vector import VectorAdd, VectorZero

class Del(Basic):
    def __new__(cls) -> Self: ...
    def gradient(self, scalar_field, doit=...) -> VectorZero | VectorAdd | Gradient: ...

    __call__ = ...
    def dot(self, vect, doit=...) -> Divergence | Add: ...

    __and__ = ...
    def cross(self, vect, doit=...) -> VectorZero | VectorAdd | Curl: ...

    __xor__ = ...
