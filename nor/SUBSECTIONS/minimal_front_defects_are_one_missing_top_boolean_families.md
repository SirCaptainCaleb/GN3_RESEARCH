# Minimal front defects are one-missing-top Boolean families

## Metadata

- ID: minimal_front_defects_are_one_missing_top_boolean_families
- Parent Section: directed_nor_union_closed_bridge
- Position: 15
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Minimal front defects are one-missing-top Boolean families

Work in the directed translation-invariant sector with coordinate arity (r\ge2). Let
[
P=(p_1,\ldots,p_t,S)
]
be an inclusion-maximal (sigma)-tight path in a counterexample, let (F) be its first ordered ((r-1))-tuple, and let
[
X=V\setminus V(P)
]
be the omitted vertices.

By the maximal-front theorem, every singleton ({x}), (x\in X), belongs to the opposite-color support family
[
\mathcal G(P)
=
\{A\subseteq X:A\in\mathcal F_{1-\sigma,F}\},
]
whereas (X\notin\mathcal G(P)).

Choose an inclusion-minimal set
[
D\subseteq X,qquad D\notin\mathcal G(P).
]
Because all singletons in (X) are feasible, (|D|\ge2).

### Proposition 1: the restricted defect is the punctured Boolean cube

For every proper subset (A\subsetneq D),
[
A\in\mathcal G(P).
]
Hence
[
\mathcal G(P)|_D=2^D\setminus\{D\}.
]

#### Proof
This is immediate from the inclusion-minimality of (D): every proper subset of (D) is feasible, while (D) itself is not. (square)

Thus a counterexample does not merely expose an arbitrary non-union-closed accessible family. At the exposed front of a maximal monochromatic path it contains a canonical minimal defect whose support structure is completely determined: the entire Boolean cube boundary is feasible and only the top is missing.

### Proposition 2: every coordinate has the same minimal negative Frankl bias

Put (d=|D|) and
[
\mathcal H_D=2^D\setminus\{D\}.
]
Then
[
|\mathcal H_D|=2^d-1.
]
For each (x\in D),
[
f_x
=
|\{A\in\mathcal H_D:x\in A\}|
=
2^{d-1}-1.
]
Therefore
[
2f_x-|\mathcal H_D|
=
2(2^{d-1}-1)-(2^d-1)
=
-1.
]

So every coordinate lies strictly below one half, and by the smallest possible integral margin. Adding the single missing top (D) changes every bias from (-1) to (0).

Equivalently, under the canonical doubled-cube lift used in Article II, every old-coordinate first harmonic of this minimal defect has the same negative sign and the same minimal unnormalized magnitude. The missing top is simultaneously responsible for all coordinate-frequency deficits.

### Interpretation

This gives a sharp common object for NOR and Frankl.

- On the Frankl side, (2^D\setminus\{D\}) is the maximally balanced local pattern in which every coordinate misses the half-frequency threshold by exactly one incidence.
- On the NOR side, the same pattern arises because every proper collection of omitted blocked singleton branches can be synchronized into an opposite-color tight witness ending at (F), while the whole collection cannot.

Thus the witness-synchronization obstruction can be phrased as follows:

> a directed-NOR counterexample contains a terminal witness language whose support shadow realizes every face of a Boolean (d)-cube except its top, and the entire strict Frankl deficit of that shadow is concentrated in that one missing witness.

This is stronger and more canonical than selecting an arbitrary top-missing square. Every two-dimensional face through the missing top gives a square defect, but the minimal infeasible set (D) records the full arity of the obstruction.

### Splice consequence

For every (x\in D), the set (D\setminus\{x}) is feasible in (\mathcal F_{1-\sigma,F}). Choose a ((1-\sigma))-tight witness
[
Q_x=(\text{an ordering of }D\setminus\{x},F).
]
Writing (P=(F,T)), the concatenation
[
Q_x,T
]
has at most one color change and spans
[
V(P)\cup D\setminus\{x}.
]
Hence the punctured Boolean defect supplies a full family of common-interface near-spanning certificates relative to the induced vertex set (V(P)\cup D).

When (D=X), these are actual deletion orders of the ambient counterexample, all sharing the same suffix (T). In the ternary case, if (|D|=3), this lands directly in the common-tail deletion-triple geometry developed in Article I.

### Closure target

The remaining problem is no longer to locate failure of union closure; it is to exploit the exceptional strength of its minimal form. A closure proof may proceed by showing that a punctured-Boolean witness language cannot coexist with reversal antisymmetry and the maximal path (P), or by proving that the common-interface certificates (Q_x,T) force a paired deletion splice after recentering.

The key point for Article II is that the Frankl deficit and the NOR synchronization defect are literally the same missing top in this canonical local model.


## Frontier

- Development version when composed: None
- Development version now: 1
