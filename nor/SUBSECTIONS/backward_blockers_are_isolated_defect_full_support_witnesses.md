# Backward blockers are isolated-defect full-support witnesses

## Metadata

- ID: backward_blockers_are_isolated_defect_full_support_witnesses
- Parent Section: directed_nor_union_closed_bridge
- Position: 27
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Backward blockers are isolated-defect full-support witnesses

Work in the ternary setting of the insertion-sliding lemma. Let (U) be a front circuit in (mathcal F_{	au,F}), fix (xin U), and let
[
W_x=(y_1,ldots,y_k,F)
]
be a (	au)-tight witness for (Usetminus{x}).

At a scan transition choose
[
p=y_{i-1},quad a=y_i,quad b=y_{i+1},quad c=y_{i+2}
]
with
[
h(x,a,b)=1-	au,qquad h(x,b,c)=	au,qquad h(a,b,c)=	au.
]

If the shifted two-circuit alternative fails, the insertion-sliding lemma gives
[
h(a,x,b)=	au,qquad h(p,a,x)=1-	au.
]

Insert (x) between (a) and (b) in (W_x). Every old window of (W_x) has color (	au). The new windows after the insertion are
[
(p,a,x),qquad (a,x,b),qquad (x,b,c),
]
with colors
[
1-	au,qquad 	au,qquad 	au.
]
Therefore the resulting ordering of all of (U) followed by the original terminal pair (F) has status word
[
	au^*, (1-	au), 	au^*,
]
where the opposite-color run has length exactly one.

Thus every insertion transition yields one of two sharply reduced obstructions:

1. a genuine two-element front circuit at a shifted terminal pair; or
2. a full-support fixed-tail ordering with a unique isolated wrong-color window.

This converts the general punctured-Boolean synchronization problem into a local defect-removal problem. In the second case the missing top of the support family is already realized by an ordering; only one ternary window prevents that ordering from being monochromatic.

The natural next move is to transport or cancel the isolated defect by a full-support interval reversal or by comparing the isolated-defect orders obtained from different deleted vertices. Any operation that removes the single defect fills the missing top and closes the circuit immediately.

## Frontier

- Development version when composed: None
- Development version now: 1
