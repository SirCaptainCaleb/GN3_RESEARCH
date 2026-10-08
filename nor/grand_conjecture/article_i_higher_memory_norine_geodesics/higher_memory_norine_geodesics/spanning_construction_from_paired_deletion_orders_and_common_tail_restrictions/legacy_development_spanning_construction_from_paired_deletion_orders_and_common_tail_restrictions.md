# Spanning construction from paired deletion orders and common-tail restrictions — preserved pre-item development

## Composition

(none yet)

## Development

## Spanning construction from two deletion orders

Work in the directed translation-invariant sector of N_{r+1}, with coordinate arity r>=2 and h(W^rev)=1-h(W). All sequences below have distinct vertices.

### Theorem (paired deletion orders)
Let V be partitioned into an ordered sequence M of length r-2, two vertices b,x, and an ordered tail T. Suppose the deletion orders
P=(M,b,T) on V\{x},
Q=(M^rev,x,T) on V\{b}
have nonempty sliding r-window words, each with at most one change, and with the same initial color sigma.
Then at least one of
(x,M,b,T), (b,M^rev,x,T)
is a spanning one-change order.

Proof. Prepending x to P adds just one window, (x,M,b), and prepending b to Q adds just one window, (b,M^rev,x). These two windows are reverses, so their colors are complementary. One therefore has color sigma. For that candidate the new first color agrees with the old first color; the remaining word is precisely the chosen deletion word and has at most one change. Every vertex is retained. This proves the theorem.

The theorem also covers r=2 with M empty. It uses reversal antisymmetry alone; no edge-order representation is assumed.

### Constant deletion words
If any deletion order has a constant word, any prepending of its omitted vertex gives a spanning word with at most one change. Consequently all good deletion words in a counterexample are nonconstant.

### Corollary (a common nonconstant tail suffices)
Suppose T itself has a nonconstant one-change r-window word. If both P and Q above are one-change deletion orders, then they automatically have the same initial color, and the theorem applies.

Indeed the word of T is a suffix of both words. It already contains the only permissible change. Every preceding window in either deletion order must equal the initial color of T. This removes the need to compare the prefix colors separately.

### Explicit criterion for r=3
Let the common tail T=(t_1,t_2,...,t_m) have word sigma^p(1-sigma)^q, with p,q>=1. Let V\V(T)={a,b,x}. Then
(a,b,T) is one-change if and only if
h(a,b,t_1)=h(b,t_1,t_2)=sigma.
Likewise (a,x,T) is one-change if and only if
h(a,x,t_1)=h(x,t_1,t_2)=sigma.
If all four equalities hold, one of (x,a,b,T) and (b,a,x,T) spans with one change, since
h(x,a,b)=1-h(b,a,x).

Thus two different omitted vertices can be combined without changing the long common tail. This is a spanning construction, rather than a claim that the number of disturbed windows is bounded.

## Restrictions forced by a counterexample

### Corollary (feasible predecessor pairs have outdegree at most one)
For r=3 and a fixed nonconstant one-change tail T with three omitted ground vertices U={a,b,x}, define a directed graph on U by
u -> v iff (u,v,T) is a one-change deletion order.
In a counterexample this graph has outdegree at most one at each vertex.

Proof. Two arcs a->b and a->x meet the paired-deletion criterion and produce a spanning order. Thus they cannot both occur. The argument applies at each vertex.

In terms of local colors, if E_T={v in U:h(v,t_1,t_2)=sigma}, the arcs are precisely
u->v with v in E_T and h(u,v,t_1)=sigma.
This imposes simultaneous restrictions on several middle-vertex tournaments, using full counterexamplehood rather than endpoint blocking for a single fork. For example, if every vertex of U belongs to E_T, at most three of the six colors h(u,v,t_1), u!=v in U, can equal sigma.

More generally, for any r, represent a candidate deletion prefix by (x;M,b), where x is omitted. The transformation
(x;M,b) -> (b;M^rev,x)
is a fixed-point-free involution. For each fixed nonconstant tail, a counterexample permits at most one good deletion prefix in each pair. Hence at most r!/2 of its r! candidate prefixes are good.

## Attempt to force the construction, and the unresolved step

I attempted closure by propagating the omitted vertex through a fixed tail until two paired certificates were obtained. The theorem proves that such a collision closes the instance. However minimum-counterexample minimality only guarantees some good order for each deletion. It does not guarantee a common tail, or that two certificates occupy a paired prefix orbit. Neither the outdegree bound nor the prefix count contradicts that existence statement.

A fixed-tail search can be obstructed even in a globally soluble coloring. Take a strict total order on V and
h(a,b,c)=0 iff a<c.
This is reversal-antisymmetric and has a monochromatic ascending spanning order. Let x be its largest vertex and fix a terminal pair u,v avoiding x. No color-0 tight path ending in u,v can contain x: since x is not among its last two vertices, a window (x,y,z) occurs and has color 1. Thus retaining a particular terminal pair can defeat augmentation despite the existence of a spanning solution.

This example is a guardrail for the attempted mechanism, not a counterexample to NOR. It shows why a completion argument cannot infer success merely from repeated front substitutions while freezing the tail or its terminal pair.

### Remaining closure obligation
Force a pair of compatible deletion certificates, allowing their common tail to change during the search, or supply another spanning construction when every such pair is absent. A strictly improving quantity for that search has not been proved.

### Audit
The new spanning candidates add only their first window to a separately verified deletion word. No crossing windows have been omitted: all other windows are already present in P or Q. The common-tail corollary requires T to have a nonconstant word; a constant tail does not force the deletion orders to have the same initial color. The feasible-pair bound is necessary for a counterexample and is not asserted to be sufficient. The grand conjecture remains open.
