# Antimatroid saturation and the two-obstruction dichotomy

## Composition

Finite union-closed feasible families saturate their entire feasible support; accessible families that fail union closure expose a missing-square obstruction. This distinguishes support-level saturation from the unresolved compatibility of tight witness orders. Antimatroid support structure alone is not an ordered-witness merging theorem.

## Development

## Antimatroid saturation and the two-obstruction dichotomy

Fix coordinate arity (r\ge2), a color (sigma), and an ordered terminal ((r-1))-tuple (S). Let
[
\mathcal F_{\sigma,S}
=
\{A\subseteq V\setminus S:
\text{some ordering of }A,S\text{ is }\sigma\text{-tight}\}.
]
This family is finite, contains (arnothing), and is accessible.

### Proposition 1: union closure gives a saturated tight witness

Assume (mathcal F_{\sigma,S}) is union-closed, and put
[
U_{\sigma,S}=\bigcup_{A\in\mathcal F_{\sigma,S}}A.
]
Then (U_{\sigma,S}\in\mathcal F_{\sigma,S}). Consequently there is one (sigma)-tight sequence
[
P_{\sigma,S}=u_1,\ldots,u_t,S
]
whose support before the terminal state is exactly (U_{\sigma,S}). Thus every coordinate that occurs in any (sigma)-tight witness ending at (S) occurs simultaneously in a single saturated witness.

#### Proof
Because the ground set is finite, (mathcal F_{\sigma,S}) is finite. Repeated union closure shows that the union of all its members is itself a member. The definition of feasibility then supplies the required tight ordering. (square)

This is stronger than the ordinary Frankl conclusion on this family: union closure does not merely force an abundant coordinate; it merges all terminally compatible supports into one monochromatic path.

### Proposition 2: the Frankl coordinate is immediate in the antimatroid case

If (mathcal F_{\sigma,S}
e\{\varnothing\}) is union-closed, accessibility gives some singleton ({x}\inmathcal F_{\sigma,S}). Then
[
A\longmapsto A\cup\{x\}
]
injects the feasible supports avoiding (x) into the feasible supports containing (x). Hence (x) belongs to at least half the members of (mathcal F_{\sigma,S}).

So Frankl's occupancy conclusion holds for every nontrivial union-closed NOR support family for the elementary reason that accessibility supplies a feasible singleton.

### Proposition 3: a NOR counterexample forces two globally excluded coordinates

Suppose the directed NOR instance is a counterexample. If (mathcal F_{\sigma,S}) is union-closed, then
[
|U_{\sigma,S}|\le n-r-1.
]
Equivalently, among the (n-r+1) coordinates outside (S), at least two occur in no (sigma)-tight witness ending at (S).

#### Proof
By Proposition 1 there is a (sigma)-tight path on (U_{\sigma,S}\cup S). If (|U_{\sigma,S}|=n-r+1), this path is spanning and already gives a constant status word. If (|U_{\sigma,S}|=n-r), it is a monochromatic tight path on (n-1) vertices, which closes NOR by the near-spanning tight-path lemma: the omitted vertex either prepends monochromatically or forms the opposite-color short branch of a spanning converging fork. Therefore a counterexample requires (|U_{\sigma,S}|\le n-r-1). (square)

Call the vertices of
[
E_{\sigma,S}=(V\setminus S)\setminus U_{\sigma,S}
]
the terminal exclusion set. Under union closure, counterexamplehood forces (|E_{\sigma,S}|\ge2). For every (x\in E_{\sigma,S}), even the singleton support is infeasible, so
[
h(x,S)=1-\sigma,
]
and reversal antisymmetry gives
[
h(S^{\rm rev},x)=\sigma.
]
Thus every excluded coordinate is simultaneously a blocked left extension of (S) and a legal right extension of (S^{\rm rev}).

### Corollary: every terminal support system has one of two concrete obstruction types

For any fixed ((\sigma,S)), exactly one of the following structural regimes applies.

1. **Antimatroid saturation.** The family (mathcal F_{\sigma,S}) is union-closed. Then all (sigma)-reachable support is represented by one saturated tight witness. In a counterexample this witness leaves at least two coordinates globally excluded.

2. **Square defect.** The family is not union-closed. Choosing a top-missing square with minimal base gives
[
C, C\cup\{a\}, C\cup\{b\}\in\mathcal F_{\sigma,S},
qquad
C\cup\{a,b\}\notin\mathcal F_{\sigma,S},
]
and the restrictions to (C), (C\cup\{a}), and (C\cup\{b}) are antimatroids. The remaining obstruction is witness-order incompatibility across one missing top.

Hence the NOR--Frankl bridge yields a useful local dichotomy rather than merely an analogy: terminal reachability is either completely mergeable into one saturated monochromatic witness, or its first failure is concentrated on a single Boolean square whose two sides already have antimatroid structure.

### Closure target

A directed-NOR counterexample must therefore sustain these obstructions at every terminal state. A promising next step is to exploit reversal to couple them: show that a terminal exclusion set on one side forces saturation on a reversed or shifted terminal state, or that a minimal square defect propagates to a smaller defect after recentering. Either mechanism would eliminate one branch of the dichotomy and could force a spanning fork.
