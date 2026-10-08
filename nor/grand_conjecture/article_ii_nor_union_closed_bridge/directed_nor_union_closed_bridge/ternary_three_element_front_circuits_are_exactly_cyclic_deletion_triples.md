# Ternary three-element front circuits are exactly cyclic deletion triples

## Composition

For ternary NOR, a three-element minimal front circuit is completely classified. If (U={a,b,c}) is minimally infeasible for the fixed-tail family at (F=(f_1,f_2)) in color (	au), define (x	o y) by (h(x,y,f_1)=	au). Pair feasibility gives at least one arrow on each pair. Triple infeasibility plus reversal implies that any arrow forces the other two arrows of a directed 3-cycle, and forbids all reverse arrows. Hence, after relabeling,
[
a	o b	o c	o a.
]
The cyclic residual triples have color (1-	au), while their reverses have color (	au).

When this circuit is the entire omitted set of a maximal opposite-color tight path, its three facet witnesses splice to three one-change deletion orders with a common tail. Thus the size-three punctured-Boolean obstruction of Article II is exactly the cyclic common-tail deletion-triple geometry studied in Article I. Together with the size-two/two-hole correspondence, this identifies the two smallest front circuits with existing rigid NOR configurations.

## Development

## Ternary three-element front circuits are exactly cyclic deletion triples

Work at ternary coordinate arity. Let (F=(f_1,f_2)) be a terminal pair and let (	auin{0,1}). Suppose
[
U={a,b,c}
]
is a minimal infeasible support for (mathcal F_{	au,F}): every proper subset of (U) has a (	au)-tight witness ending at (F), while (U) has none.

In particular,
[
h(a,f_1,f_2)=h(b,f_1,f_2)=h(c,f_1,f_2)=	au.
]

Define a directed relation on (U) by
[
x	o y quadLongleftrightarrowquad h(x,y,f_1)=	au.
]

### Theorem 1: the pair relation is a directed 3-cycle

For every unordered pair ({x,y}subset U), at least one of (x	o y) or (y	o x) holds, because the pair support is feasible.

Moreover, if (y	o z) and (x) is the third vertex, then
[
h(x,y,z)=1-	au.
]
Indeed otherwise
[
(x,y,z,f_1,f_2)
]
would be a (	au)-tight witness for all of (U).

By reversal antisymmetry,
[
h(z,y,x)=	au.
]
Since (U) is nevertheless infeasible, the order
[
(z,y,x,f_1,f_2)
]
must fail at its second window, so
[
h(y,x,f_1)=1-	au.
]
Thus (y
ot	o x). Pair feasibility for ({x,y}) then forces
[
x	o y.
]

Applying the same implication once more gives
[
z	o x.
]
Hence any arrow (y	o z) forces the directed cycle
[
x	o y	o z	o x.
]

No reverse arrow can also occur. For example, if (z	o y), then triple infeasibility would force
[
h(x,z,y)=1-	au.
]
But (x	o y) already forces
[
h(z,x,y)=1-	au,
]
and (z	o x) forces
[
h(y,z,x)=1-	au.
]
In particular reversal of the latter gives
[
h(x,z,y)=	au,
]
a contradiction.

Therefore, after cyclic relabeling,
[
a	o b,qquad b	o c,qquad c	o a
]
are the only arrows.

### Corollary 2: the residual triples are completely polarized

The three cyclic pair-witness identities are
[
h(a,b,f_1)=h(b,c,f_1)=h(c,a,f_1)=	au.
]
Triple infeasibility then gives
[
h(c,a,b)=h(a,b,c)=h(b,c,a)=1-	au.
]
By reversal,
[
h(b,a,c)=h(c,b,a)=h(a,c,b)=	au.
]

Thus a three-element front circuit has no remaining local coloring freedom: its pair witnesses form one directed 3-cycle, the cyclic residual triples have color (1-	au), and the reversed residual triples have color (	au).

### Corollary 3: when the circuit is the whole omitted set, it is exactly a common-tail deletion triple

Let (P=(F,T)) be a maximal ((1-	au))-tight path whose omitted set is precisely
[
X=U={a,b,c}.
]
The three feasible deletion supports have the uniquely oriented witnesses
[
(a,b,F),qquad (b,c,F),qquad (c,a,F)
]
up to cyclic relabeling. Splicing with (T) gives three one-change deletion orders
[
(a,b,P),qquad (b,c,P),qquad (c,a,P)
]
with a common tail (P).

The missing vertices are blocked at the exposed front:
[
h(c,a,b)=h(a,b,c)=h(b,c,a)=1-	au,
]
exactly the cyclic residual-triple polarization appearing in the common-tail deletion geometry of Article I.

Hence the Article-II punctured-Boolean obstruction of circuit size three and the Article-I common-tail deletion-triple obstruction are the same local configuration.

### Significance

Circuit sizes two and three now both meet previously developed Article-I geometry:
- size two is the two-hole cage around a near-spanning tight path;
- size three is the cyclic common-tail deletion triple.

This suggests a concrete induction target: prove that every larger front circuit contains, after recentering one deletion witness at its blocked front, a front circuit of smaller size. Such a circuit-contraction principle would reduce the general punctured-Boolean obstruction to the already rigid sizes two and three.
