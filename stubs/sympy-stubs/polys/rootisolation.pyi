from typing import Any, Literal, LiteralString, Self

def dup_sturm(f, K) -> list[Any | list[Any]]: ...
def dup_root_upper_bound(f, K) -> None: ...
def dup_root_lower_bound(f, K) -> None: ...
def dup_cauchy_upper_bound(f, K): ...
def dup_cauchy_lower_bound(f, K): ...
def dup_mignotte_sep_bound_squared(f, K): ...
def dup_step_refine_real_root(
    f, M, K, fast=...
) -> (
    tuple[Any, tuple[Any, Any, Any, Any]]
    | tuple[list[Any], tuple[Any, Any, Any, Any]]
    | tuple[list[Any] | Any, tuple[Any, Any, Any, Any]]
): ...
def dup_inner_refine_real_root(
    f, M, K, eps=..., steps=..., disjoint=..., fast=..., mobius=...
) -> tuple[Any, Any] | tuple[Any | list[Any], tuple[Any, Any, Any, Any]]: ...
def dup_outer_refine_real_root(
    f, s, t, K, eps=..., steps=..., disjoint=..., fast=...
) -> tuple[Any, Any] | tuple[Any | list[Any], tuple[Any, Any, Any, Any]]: ...
def dup_refine_real_root(
    f, s, t, K, eps=..., steps=..., disjoint=..., fast=...
) -> tuple[Any, Any] | tuple[Any | list[Any], Any | tuple[Any, Any, Any, Any]]: ...
def dup_inner_isolate_real_roots(
    f, K, eps=..., fast=...
) -> list[Any] | list[tuple[Any, Any] | tuple[Any | list[Any], tuple[Any, Any, Any, Any]]]: ...
def dup_inner_isolate_positive_roots(
    f, K, eps=..., inf=..., sup=..., fast=..., mobius=...
) -> list[Any] | list[tuple[Any, Any] | tuple[Any | list[Any], tuple[Any, Any, Any, Any]]]: ...
def dup_inner_isolate_negative_roots(
    f, K, inf=..., sup=..., eps=..., fast=..., mobius=...
) -> list[Any] | list[tuple[Any, Any] | tuple[Any | list[Any], tuple[Any, Any, Any, Any]]]: ...
def dup_isolate_real_roots_sqf(
    f, K, eps=..., inf=..., sup=..., fast=..., blackbox=...
) -> list[Any] | list[tuple[Any, Any] | tuple[Any | list[Any], tuple[Any, Any, Any, Any]]] | list[RealInterval]: ...
def dup_isolate_real_roots(
    f, K, eps=..., inf=..., sup=..., basis=..., fast=...
) -> list[Any] | list[tuple[tuple[Any, Any], Any, Any] | tuple[Any, Any]]: ...
def dup_isolate_real_roots_list(
    polys, K, eps=..., inf=..., sup=..., strict=..., basis=..., fast=...
) -> list[tuple[tuple[Any, Any], Any, Any] | tuple[tuple[Any, Any], dict[Any, Any]]]: ...
def dup_count_real_roots(f, K, inf=..., sup=...) -> int: ...

OO = ...
Q1 = ...
Q2 = ...
Q3 = ...
Q4 = ...
A1 = ...
A2 = ...
A3 = ...
A4 = ...
_rules_simple = ...
_rules_ambiguous = ...
_values = ...

def dup_count_complex_roots(f, K, inf=..., sup=..., exclude=...) -> int: ...
def dup_isolate_complex_roots_sqf(f, K, eps=..., inf=..., sup=..., blackbox=...): ...
def dup_isolate_all_roots_sqf(
    f, K, eps=..., inf=..., sup=..., fast=..., blackbox=...
) -> tuple[list[Any] | list[tuple[Any, Any] | tuple[Any | list[Any], tuple[Any, Any, Any, Any]]] | list[RealInterval], Any]: ...
def dup_isolate_all_roots(
    f, K, eps=..., inf=..., sup=..., fast=...
) -> tuple[list[tuple[tuple[Any | list[Any], Any | tuple[Any, Any, Any, Any]], Any]], list[tuple[tuple[Any, Any], Any]]]: ...

class RealInterval:
    def __init__(self, data, f, dom) -> None: ...
    @property
    def func(self) -> type[RealInterval]: ...
    @property
    def args(self) -> tuple[tuple[Any, ...] | Any, list[Any] | Any, Any]: ...
    def __eq__(self, other) -> bool: ...
    @property
    def a(self): ...
    @property
    def b(self): ...
    @property
    def dx(self): ...
    @property
    def center(self): ...
    @property
    def max_denom(self): ...
    def as_tuple(self) -> tuple[Any, Any]: ...
    def __repr__(self) -> LiteralString: ...
    def __contains__(self, item) -> Literal[False]: ...
    def is_disjoint(self, other): ...
    def refine_disjoint(self, other) -> tuple[Self | RealInterval, Any]: ...
    def refine_size(self, dx) -> Self | RealInterval: ...
    def refine_step(self, steps=...) -> Self | RealInterval: ...
    def refine(self) -> Self | RealInterval: ...

class ComplexInterval:
    def __init__(self, a, b, I, Q, F1, F2, f1, f2, dom, conj=...) -> None: ...
    @property
    def func(self) -> type[ComplexInterval]: ...
    @property
    def args(self) -> tuple[Any, Any, Any, Any, Any, Any, Any, Any, Any, bool]: ...
    def __eq__(self, other) -> bool: ...
    @property
    def ax(self): ...
    @property
    def ay(self): ...
    @property
    def bx(self): ...
    @property
    def by(self): ...
    @property
    def dx(self): ...
    @property
    def dy(self): ...
    @property
    def center(self) -> tuple[Any, Any]: ...
    @property
    def max_denom(self): ...
    def as_tuple(self) -> tuple[tuple[Any, Any], tuple[Any, Any]]: ...
    def __repr__(self) -> LiteralString: ...
    def conjugate(self) -> ComplexInterval: ...
    def __contains__(self, item): ...
    def is_disjoint(self, other) -> Literal[True]: ...
    def refine_disjoint(self, other) -> tuple[Self | ComplexInterval, Any]: ...
    def refine_size(self, dx, dy=...) -> Self | ComplexInterval: ...
    def refine_step(self, steps=...) -> Self | ComplexInterval: ...
    def refine(self) -> ComplexInterval: ...
