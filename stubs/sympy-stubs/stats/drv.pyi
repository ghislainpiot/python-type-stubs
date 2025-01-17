from typing import Any, Literal, Self

from sympy import Basic, Contains, Equality, FiniteSet, Intersection, Ne, Piecewise, Sum
from sympy.core.cache import cacheit
from sympy.core.function import Lambda
from sympy.core.logic import And
from sympy.core.relational import Relational
from sympy.logic.boolalg import Boolean
from sympy.series.order import Order
from sympy.sets.sets import Complement, Union
from sympy.stats.rv import (
    ConditionalDomain,
    Distribution,
    NamedArgsMixin,
    ProductDomain,
    PSpace,
    RandomDomain,
    RandomSymbol,
    SingleDomain,
    SinglePSpace,
)
from sympy.stats.symbolic_probability import Probability

class DiscreteDistribution(Distribution):
    def __call__(self, *args): ...

class SingleDiscreteDistribution(DiscreteDistribution, NamedArgsMixin):
    set = ...
    def __new__(cls, *args) -> Self: ...
    @staticmethod
    def check(*args) -> None: ...
    @cacheit
    def compute_cdf(self, **kwargs) -> Lambda: ...
    def cdf(self, x, **kwargs) -> Basic: ...
    @cacheit
    def compute_characteristic_function(self, **kwargs) -> Lambda: ...
    def characteristic_function(self, t, **kwargs) -> Basic: ...
    @cacheit
    def compute_moment_generating_function(self, **kwargs) -> Lambda: ...
    def moment_generating_function(self, t, **kwargs) -> Basic: ...
    @cacheit
    def compute_quantile(self, **kwargs) -> Lambda: ...
    def quantile(self, x, **kwargs) -> Basic: ...
    def expectation(self, expr, var, evaluate=..., **kwargs) -> Any | Equality | Relational | Ne | Sum | Literal[0]: ...
    def __call__(self, *args): ...

class DiscreteDomain(RandomDomain):
    is_Discrete = ...

class SingleDiscreteDomain(DiscreteDomain, SingleDomain):
    def as_boolean(self) -> Contains: ...

class ConditionalDiscreteDomain(DiscreteDomain, ConditionalDomain):
    @property
    def set(self) -> FiniteSet | Intersection | Union | Complement: ...

class DiscretePSpace(PSpace):
    is_real = ...
    is_Discrete = ...
    @property
    def pdf(self): ...
    def where(self, condition) -> SingleDiscreteDomain: ...
    def probability(self, condition) -> Probability | Equality | Relational | Ne | int: ...
    def eval_prob(self, _domain) -> Equality | Relational | Ne | int | None: ...
    def conditional_space(self, condition) -> DiscretePSpace: ...

class ProductDiscreteDomain(ProductDomain, DiscreteDomain):
    def as_boolean(self) -> And: ...

class SingleDiscretePSpace(DiscretePSpace, SinglePSpace):
    is_real = ...
    @property
    def set(self): ...
    @property
    def domain(self) -> SingleDiscreteDomain: ...
    def sample(self, size=..., library=..., seed=...) -> dict[RandomSymbol, Any]: ...
    def compute_expectation(self, expr, rvs=..., evaluate=..., **kwargs) -> Equality | Relational | Ne | Sum: ...
    def compute_cdf(self, expr, **kwargs) -> Lambda: ...
    def compute_density(self, expr, **kwargs) -> Basic: ...
    def compute_characteristic_function(self, expr, **kwargs) -> Lambda: ...
    def compute_moment_generating_function(self, expr, **kwargs) -> Lambda: ...
    def compute_quantile(self, expr, **kwargs) -> Lambda: ...
