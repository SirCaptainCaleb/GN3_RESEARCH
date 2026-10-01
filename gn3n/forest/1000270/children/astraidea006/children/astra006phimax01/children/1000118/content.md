# Quadratic-maximal three-block states forbid whole-block insertion across a central interval

## Statement

Assume a connected component of the contiguous-block relocation graph on orderings with contiguous-path number at most three contains no ordering with contiguous-path number at most two. Choose, among all reachable orderings and all partitions of them into three nonempty contiguous tight paths, a displayed state X|Y|Z maximizing the quadratic potential, and use whole-block permutation freedom to place X=(x_1,...,x_p) immediately before Y=(y_1,...,y_q). For 1<=i<=p-1, if i>p-q then the concatenation (x_1,...,x_i,y_1,...,y_q) is not tight; if i<q then the concatenation (y_1,...,y_q,x_{i+1},...,x_p) is not tight. Hence every gap satisfying p-q<i<q simultaneously forbids both one-sided concatenations. In particular, if p=q, every internal gap of X has this two-sided failure property for insertion of the whole block Y.

## Body

Let X_i^-=(x_1,...,x_i) and X_i^+=(x_{i+1},...,x_p), where 1<=i<=p-1. Both are nonempty inherited tight paths.

First suppose X_i^- followed by Y is tight. Starting from the ordering X,Y,Z, relocate the entire contiguous block Y into the gap between x_i and x_{i+1}. The new ordering is

X_i^- , Y , X_i^+ , Z.

It has a partition into the three nonempty tight paths
(X_i^- Y) | X_i^+ | Z.
Thus it lies in the same relocation component. The old displayed block orders are p,q,|Z|, while the new ones are i+q,p-i,|Z|. The change in quadratic potential is

(i+q)^2+(p-i)^2-p^2-q^2
=2i(i+q-p).

If i>p-q, this is positive, contradicting the maximal choice of the displayed state. Therefore X_i^-Y is not tight whenever i>p-q.

Now suppose Y followed by X_i^+ is tight. The same relocation of Y yields the displayed partition
X_i^- | (Y X_i^+) | Z
with block orders i,p+q-i,|Z|. The quadratic-potential change is

i^2+(p+q-i)^2-p^2-q^2
=2(p-i)(q-i).

Because i<=p-1, the factor p-i is positive. Hence the change is positive whenever i<q, again contradicting maximality. Therefore YX_i^+ is not tight whenever i<q.

Consequently every integer i with
p-q<i<q
satisfies both conclusions simultaneously. When p=q, this inequality is 0<i<p, so every internal gap of X has both failures.

The argument uses arbitrary-length contiguous relocation of the whole block Y; it does not inspect or bound p or q. The one-vertex interface restrictions of astra006phimax01 are therefore only the boundary shadow of a longer interval of forbidden whole-block insertions.
