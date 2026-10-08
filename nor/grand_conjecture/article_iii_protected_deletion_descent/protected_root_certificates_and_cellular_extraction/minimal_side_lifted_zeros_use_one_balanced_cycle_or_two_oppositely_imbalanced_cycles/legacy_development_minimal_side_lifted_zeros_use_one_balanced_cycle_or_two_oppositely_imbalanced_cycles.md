# Minimal side-lifted zeros use one balanced cycle or two oppositely imbalanced cycles — preserved pre-item development

## Composition

(none yet)

## Development


## Minimal side-lifted zeros use one balanced cycle or two oppositely imbalanced cycles

Consider a positive dependence of side-lifted protected roots
[
sum_{ein E}lambda_e(ho_e,s_e)=0,
qquad lambda_e>0,
]
where each physical root is oriented as a directed coordinate edge so that the physical equation
[
sum_elambda_eho_e=0
]
is a positive circulation.

Allow parallel directed edges when distinct protected states carry the same physical root with different provenance.

### Cycle decomposition with a scalar side imbalance

Every positive circulation on a finite directed multigraph decomposes as
[
lambda=sum_C t_C,chi_C,
qquad t_C>0,
]
over directed simple cycles (C), where (chi_C) assigns one common coefficient to every edge occurrence of (C).

For each constituent cycle define its side imbalance
[
sigma(C)=sum_{ein C}s_e.
]
Its physical root sum is already zero:
[
sum_{ein C}ho_e=0.
]
Hence the lifted contribution of the cycle is simply
[
sum_{ein C}(ho_e,s_e)=(0,sigma(C)).
]

The scalar equation for the whole lifted zero is therefore
[
sum_C t_C,sigma(C)=0.
]

### Minimal-zero dichotomy

Assume the original lifted dependence is support-minimal.

If some constituent cycle has (sigma(C)=0), then that cycle alone is a positive lifted zero. Support minimality forces the whole support to be exactly this one side-balanced cycle.

Otherwise every constituent cycle has nonzero imbalance. Since their positive weighted imbalances sum to zero, there is at least one cycle (C_+) with (sigma(C_+)>0) and one (C_-) with (sigma(C_-)<0). Choose positive scalars
[
u=|sigma(C_-)|,qquad v=sigma(C_+).
]
Then
[
usum_{ein C_+}(ho_e,s_e)
+
vsum_{ein C_-}(ho_e,s_e)
=0.
]
Thus the union of these two cycles already supports a positive lifted zero. Support minimality forces the original support to be exactly the union of two oppositely imbalanced simple cycles.

Therefore:

[
oxed{	ext{Every support-minimal side-lifted zero consists of either one balanced cycle or two oppositely imbalanced cycles.}}
]

### Ternary A3 consequence

Inside one A3 block every simple physical cycle has length 2, 3, or 4.

A balanced constituent cycle must have even length, hence is a 2-cycle or 4-cycle with equal left/right counts.

If a triangle occurs in a support-minimal lifted zero, its side imbalance is necessarily odd and nonzero. It therefore cannot occur alone: it must be paired with a second simple endpoint cycle of opposite side imbalance.

Thus the primitive A3 lifted obstruction is no longer an arbitrary 2/3/4 endpoint circuit. It has one of two forms:

1. a single opposite-side 2-cycle or balanced 4-cycle;
2. a pair of side-unbalanced endpoint cycles whose scalar imbalances have opposite signs.

This converts the decomposition caveat of the preceding subsection into a finite structural alternative. The next extraction theorem may attack the single-cycle cases first; any residual triangle is forced to interact with a second physical cycle and therefore carries additional cut/side coupling unavailable to a raw A3 triangle.
