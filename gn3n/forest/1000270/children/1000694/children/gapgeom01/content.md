# Compatible-triangle common-gap geometry

## Statement

Three pairwise-compatible deletion covers in a counterexample place all three omitted labels at one common gap of one common path. Their precedence tournament controls the forbidden central triple. A fourth cover compatible with two triangle states can occur only at a gap neighbor; transitive triangles are two-deep, compatibility diamonds force pair-order reversal, and two opposite diamonds force a tight 3-cycle.

## Body

# Compatible-triangle common-gap geometry

# Three compatible deletion covers collapse to one common insertion gap

Let H be a boundary tournament with pc(H)>2. Let a,b,c be distinct vertices, and for each x in {a,b,c} let F_x be an exact two-path cover of H-x.

Assume F_a,F_b,F_c are pairwise compatible on their pairwise intersections in the sense of the compatibility-gluing theorem.

Put

W=V(H)-{a,b,c}.

## Theorem

The compatible restrictions to W have exactly two nonempty ordered support classes P,Q.

Each of a,b,c belongs, in both deletion covers in which it occurs, to the same one of these two classes. In fact all three labels belong to the same class, say P.

Relative to the common order on P, all three labels are inserted at one identical gap.

Consequently there is a decomposition of the common order

P=L,R

at one gap such that, for each x in {a,b,c}, the P-component of F_x is obtained by inserting the other two labels consecutively between L and R, in one of their two possible relative orders; the Q-component is exactly the common path Q.

Thus every triple of pairwise-compatible exact deletion two-covers in a counterexample is supported, for whole-block purposes, on the six oriented blocks

L,(a),(b),(c),R,Q,

with empty L or R allowed.

Furthermore, orient each pair of labels according to the order in the unique deletion cover containing that pair: for example a->b if a precedes b in F_c. Let T be this tournament on {a,b,c}. Then every ordering (x,y,z) that is a directed Hamilton path of T has

(x,y,z)

non-tight, and therefore

(z,y,x)

tight.

## Proof

### 1. The restriction to W cannot have one support class

Pairwise compatibility gives one common pair-state on W, so its vertices form either one or two ordered support classes.

Suppose first that W is one ordered class P.

For a label x in {a,b,c}, compare the two covers in which x occurs. Their compatibility on W union {x} shows that either x joins P in both covers or x is separated from P in both. Let J be the set of labels that join P.

Because every F_x is an exact two-cover, in the cover deleting x the two surviving labels cannot both join P: otherwise every vertex of H-x would lie in one component. Hence |J|<=1.

If J is empty, then in every deletion cover the two surviving labels form the second component while P is the first. Since every three-vertex boundary tournament is Hamiltonian, a Hamilton path on {a,b,c} together with P gives a spanning two-cover of H, contradiction.

If J={c}, then F_c has the form

P | (a,b)

with some order of the two-vertex component, while F_a contains a tight component on P union {c}. Those two tight paths are disjoint and together cover H:

(P union {c}) | (a,b).

Again pc(H)<=2, contradiction.

Thus W cannot have one support class. Hence it has exactly two nonempty ordered classes P,Q.

### 2. All three deleted labels join the same common class

Fix x in {a,b,c}. Compatibility of the two covers containing x makes its component relation and relative order with every vertex of W independent of which cover is used.

Since W already has the two nonempty classes P,Q and each deletion cover has exactly two components, x cannot be a third component and cannot merge P with Q. Therefore x joins exactly one of P,Q at a definite insertion slot.

Suppose two labels, say a and b, join different classes. Consider F_a and F_b. Their common intersection contains W and the third label c, and the two covers are compatible there.

Taking from F_b the component containing P and a, and from F_a the component containing Q and b, with c included in whichever common class it belongs to, gives two disjoint tight paths covering all of H. This is exactly the different-common-class gluing of the compatible-pair localization theorem and contradicts pc(H)>2.

Therefore a,b,c all join the same class. Rename it P. The other class Q occurs unchanged as a tight path in all three deletion covers.

### 3. Their base insertion slots are pairwise equal or adjacent

Let s_x be the insertion slot of x in the common order P, defined from either cover containing x.

If two base slots s_x,s_y differed by at least two, then at least one vertex of P would lie strictly between the two gaps. In the common intersection of F_x and F_y the third label may add another vertex but cannot remove that intervening P-vertex. Thus x and y are inserted into separated slots of the common ordered class for the pair F_x,F_y.

Section 3 of the compatible-pair localization theorem would then glue both insertions simultaneously and produce a spanning two-cover of H, contradiction.

Hence

|s_x-s_y|<=1

for every pair x,y. Thus the three slots lie in either one gap or two adjacent gaps.

### 4. Two adjacent occupied gaps are impossible

Assume both adjacent gaps occur. Let z be the unique vertex of P between them.

By symmetry suppose a,b use the left gap and c uses the right gap.

In F_c the two surviving labels a,b occur consecutively in the left gap. Suppose their order is

... a,b,z ...

(the opposite order is symmetric).

Now compare F_a and F_c. Their common intersection contains b and W, so the relevant common P-class has the order

... b,z ...

The label a, as seen in F_c, is inserted immediately before b, while c, as seen in F_a, is inserted after z.

Thus the insertion slots of a and c in this common ordered class are separated by the two common vertices b,z, hence differ by at least two. By the compatible-pair localization theorem they glue to a spanning two-cover, contradiction.

If F_c orders b,a,z instead, the same argument applied to b and c gives the contradiction.

The case with two labels in the right gap and one in the left gap is identical.

Therefore all three labels use one identical gap of P.

### 5. The remaining obstruction is only the three-label order

Write the common order as

P=L,R

at this gap.

For each deleted label, the other two labels occur consecutively between L and R in that cover; Q is unchanged. Hence the only pairwise data not contained in P,Q are the three relative orders among a,b,c.

Orient those three pairs to form the tournament T.

Let (x,y,z) be any directed Hamilton path of T. Then:

- the pair x,y occurs in F_z in the order x,y;
- the pair y,z occurs in F_x in the order y,z.

Therefore the sequence

L,x,y,z,R

has every consecutive triple by one of the deletion covers except possibly the central triple

(x,y,z).

If (x,y,z) were tight, then

(L,x,y,z,R) | Q

would be a spanning two-cover of H.

Since pc(H)>2, (x,y,z) is non-tight. Boundary antisymmetry therefore gives

(z,y,x)

tight.

This holds for every directed Hamilton path of T. ∎



Three compatible deletion covers do not yet glue automatically, but their failure is completely localized: all three deleted vertices occupy one common insertion gap of one global ordered class, while the second path is fixed.

The obstruction is precisely a mismatch between the precedence tournament supplied by the deletion-cover orders and the boundary orientation on the three deleted labels: every precedence-consistent Hamilton ordering of the labels is forbidden as a tight triple.

Thus the four-cover gluing theorem the compatibility-gluing theorem can be approached through a bounded one-gap kernel rather than arbitrary ambient path lengths. A fourth deletion cover must break compatibility against this same-gap three-label obstruction somewhere. ∎



---

# A fourth compatible deletion cover is confined to the two neighbors of a compatible triangle gap

Assume the setup and conclusions of the common-gap theorem above.

Thus H has pc(H)>2; a,b,c are distinct; F_a,F_b,F_c are pairwise-compatible exact two-covers of H-a,H-b,H-c; and on

W=V(H)-{a,b,c}

their common ordered classes are P,Q, with all three labels inserted at one common gap of P.

Write

P=L,R

at that gap, and write the common one-label restriction as

L,c,R

when only c is retained at the gap.

Orient the label pairs by their relative orders in the corresponding deletion covers, obtaining the precedence tournament T on {a,b,c}.

Let d be a fourth vertex outside {a,b,c}, and let F_d be an exact two-cover of H-d.

## Theorem

Suppose F_d is compatible with two members of the triangle, say F_a and F_b.

Then:

1. d lies in the common class P, not Q;
2. d is one of the at most two P-vertices adjacent to the common insertion gap, namely the last vertex of L or the first vertex of R;
3. if d is the last vertex of L, then both a and b precede c in T;
4. if d is the first vertex of R, then c precedes both a and b in T.

Equivalently, for the pair F_a,F_b whose third triangle label is c, double compatibility of F_d is possible only when c is a sink of T and d is the left gap-neighbor, or c is a source of T and d is the right gap-neighbor.

Consequently, if T is a directed 3-cycle, every outside deletion cover F_d is compatible with at most one of F_a,F_b,F_c.

## Proof

Assume F_d is compatible with F_a and F_b.

Then the three covers

F_a,F_b,F_d

are pairwise compatible. Apply the common-gap theorem above to the deletion labels

a,b,d.

### 1. d must lie in P

The common intersection of F_a and F_b is

V(H)-{a,b},

which contains W and c.

By the original compatible-triangle structure, its two common ordered classes are

P with c inserted at the common gap,

and

Q.

The labels a and b, when present, belong to the first of these classes.

The theorem the common-gap theorem above applied to the compatible triple F_a,F_b,F_d says that the three deletion labels a,b,d must all join the same common class.

Therefore d also belongs to the P-class. In particular d is a vertex of P, not Q.

### 2. d must neighbor the original gap

Remove a,b,d. In the common P-class of F_a and F_b, the surviving triangle label c remains at the original common gap. Thus the common order for the triple {a,b,d} is

(P-d) with c inserted at the original gap.

By the common-gap theorem above, the three labels a,b,d must all be inserted at one identical gap of this common order.

Consider a as seen in F_b. In F_b, the only two triangle labels present are a and c, and both occupy the original gap of P. Therefore relative to the one-label common order

L,c,R,

the insertion slot of a is either immediately before c or immediately after c.

But d must have exactly the same insertion slot after d is deleted from P.

A vertex of P can be reinserted immediately before c only if it is the last vertex of L. Likewise it can be reinserted immediately after c only if it is the first vertex of R.

Hence d is one of the two P-vertices adjacent to the original common gap, with the obvious omission when L or R is empty.

### 3. The side of d determines the precedence orientation at c

Suppose d is the last vertex of L.

Then the common insertion gap for the compatible triple F_a,F_b,F_d is immediately before c.

Therefore a, as seen in F_b, is inserted immediately before c, so a precedes c in the original precedence tournament T.

Likewise b, as seen in F_a, is inserted immediately before c, so b precedes c in T.

Thus c is a sink relative to a,b.

If instead d is the first vertex of R, the common insertion gap is immediately after c. Hence c precedes a in F_b and c precedes b in F_a. Thus c is a source relative to a,b.

This proves all four assertions.

Finally suppose T is a directed 3-cycle. No vertex of a directed 3-cycle is a source or a sink. Therefore for no choice of two triangle covers can the third label satisfy the necessary source/sink condition above. Hence an outside cover F_d cannot be compatible with two members of the triangle.

So every outside deletion cover is compatible with at most one of F_a,F_b,F_c. ∎



A compatible triangle is not merely a one-gap obstruction. Its interaction with the rest of the deletion-cover family is strongly localized.

Only the two vertices of the common path immediately neighboring the gap can support a fourth cover compatible with two triangle states, and even those possibilities are controlled by the source/sink structure of the triangle precedence tournament.

In the cyclic-precedence case, the triangle is compatibility-isolated: every other deletion cover disagrees with at least two of its three states.

This converts the local one-gap kernel into a global sparsity constraint on the compatibility graph of deletion covers, independent of ambient order. ∎

---

# A transitive compatible-triangle gap must be two-deep on both sides

Assume the one-gap compatible-triangle setup of `the common-gap theorem above` in a boundary tournament `H` with `pc(H)>2`.

Thus three pairwise-compatible exact deletion covers have common classes `P,Q`, all three deleted labels use one gap of `P`, and
`P=L,R`.

Assume the precedence tournament on the deleted labels is transitive. Relabel them so
`a<b<c`.
Then the three deletion-cover components on the exceptional class are

`F_a: (L,b,c,R)`,
`F_b: (L,a,c,R)`,
`F_c: (L,a,b,R)`,

while `Q` is the unchanged second component.

By `the common-gap theorem above`, the precedence-consistent triple `(a,b,c)` is non-tight, hence
`(c,b,a)`
is tight.

## Theorem

In this transitive one-gap obstruction,
`|L|>=2`
and
`|R|>=2`.

## Proof

### 1. The left side cannot be empty

Assume `L` is empty.

Exactly one of
`(b,a,c)`
and
`(c,a,b)`
is tight, by boundary antisymmetry.

If `(b,a,c)` is tight, then
`(b,a,c,R)`
is a tight Hamilton path on the exceptional support: after the first triple, every remaining consecutive triple is inherited from
`F_b=(a,c,R)`.

If `(c,a,b)` is tight, then
`(c,a,b,R)`
is a tight Hamilton path on the exceptional support, with all remaining consecutive triples inherited from
`F_c=(a,b,R)`.

This argument also covers empty or singleton `R`. In either case the exceptional support is Hamiltonian, and adjoining `Q` gives a spanning two-cover of `H`, contradiction.

Hence `L` is nonempty.

### 2. The left side cannot be a singleton

Assume
`L=(ell)`.

Exactly one of
`(a,ell,b)`
and
`(b,ell,a)`
is tight.

If `(a,ell,b)` is tight, then the path
`(a,ell,b,c,R)`
is tight: after the first triple, every remaining consecutive triple is inherited from
`F_a=(ell,b,c,R)`.

If `(b,ell,a)` is tight, then
`(b,ell,a,c,R)`
is tight, with all remaining consecutive triples inherited from
`F_b=(ell,a,c,R)`.

Thus the exceptional support is Hamiltonian in either case, again contradicting `pc(H)>2` after adjoining `Q`.

Therefore `|L|>=2`.

### 3. The right side cannot be empty

Assume `R` is empty.

Exactly one of
`(a,c,b)`
and
`(b,c,a)`
is tight.

If `(a,c,b)` is tight, then
`(L,a,c,b)`
is tight because every preceding consecutive triple is inherited from
`F_b=(L,a,c)`.

If `(b,c,a)` is tight, then
`(L,b,c,a)`
is tight because every preceding consecutive triple is inherited from
`F_a=(L,b,c)`.

Thus the exceptional support is Hamiltonian, contradiction after adjoining `Q`.

Hence `R` is nonempty.

### 4. The right side cannot be a singleton

Assume
`R=(r)`.

Exactly one of
`(b,r,c)`
and
`(c,r,b)`
is tight.

If `(b,r,c)` is tight, then
`(L,a,b,r,c)`
is tight: the prefix through `(a,b,r)` is inherited from `F_c`.

If `(c,r,b)` is tight, then
`(L,a,c,r,b)`
is tight: the prefix through `(a,c,r)` is inherited from `F_b`.

Thus the exceptional support is Hamiltonian in either case, contradiction.

Therefore `|R|>=2`. ∎

## Consequence

A transitive compatible triangle is necessarily genuinely internal: the common gap lies at distance at least two from both ends of its common support class. Combined with `the fourth-cover localization theorem above`, the only vertices whose deletion covers can be compatible with two triangle states are the two immediate gap-neighbors, and both of those neighbors are themselves internal path vertices.

---

# Compatibility diamonds force an explicit pair-order reversal

Assume the compatible-triangle setup of the common-gap theorem above and the fourth-cover localization of the fourth-cover localization theorem above.

Let the triangle labels be a,b,c, with common path gap between the last vertex ell of L and the first vertex r of R when those vertices exist.

Assume the precedence tournament of the triangle is transitive:

a -> b,
b -> c,
a -> c.

Thus the three original deletion covers have local gap orders

F_c: ... ell,a,b,r ...,
F_b: ... ell,a,c,r ...,
F_a: ... ell,b,c,r ...,

with the obvious endpoint modifications if ell or r is absent.

## Theorem

1. Suppose ell exists and a fourth deletion cover F_ell is compatible with F_a and F_b. Then F_ell orders b before a, opposite to the a-before-b order in F_c. Moreover

(a,b,ell)

is tight.

2. Suppose r exists and a fourth deletion cover F_r is compatible with F_b and F_c. Then F_r orders c before b, opposite to the b-before-c order in F_a. Moreover

(r,b,c)

is tight.

Consequently every compatibility diamond consisting of one transitive compatible triangle plus its only possible double-compatible gap-neighbor has a forced pair-order disagreement across its two nonadjacent tips.

## Proof

### Left gap-neighbor

Assume F_ell is compatible with F_a and F_b.

By the fourth-cover localization theorem above this is exactly the only possible left-side double compatibility: the third triangle label c is the sink of the original precedence tournament.

Consider the compatible triangle

F_a,F_b,F_ell

with deletion labels a,b,ell.

In F_b the vertices ell and a lie in the common path class with ell preceding a, because F_b contains the local order

... ell,a,c ...

Likewise F_a has ell preceding b.

Hence in the precedence tournament T_left of the compatible triangle {a,b,ell},

ell -> a,
ell -> b.

The only undetermined edge of T_left is the order of a,b in F_ell.

Suppose for contradiction that F_ell also orders a before b.

Then T_left is transitive with directed Hamilton order

ell,a,b.

By the common-gap theorem above, every directed Hamilton path of the precedence tournament of a compatible triangle in a counterexample must be a non-tight triple. Therefore

(ell,a,b)

would be non-tight.

But the original cover F_c literally has the local path order

... ell,a,b,r ...

so (ell,a,b) is a consecutive tight triple of F_c.

Contradiction.

Therefore F_ell must order

b before a.

Now T_left is transitive with directed Hamilton order

ell,b,a.

Again the common-gap theorem above forces

(ell,b,a)

non-tight.

Boundary antisymmetry therefore gives

(a,b,ell)

tight.

This proves the first assertion.

### Right gap-neighbor

Assume F_r is compatible with F_b and F_c.

By the fourth-cover localization theorem above this is the only possible right-side double compatibility: the third triangle label a is the source of the original precedence tournament.

Consider the compatible triangle

F_b,F_c,F_r

with deletion labels b,c,r.

The original covers give

b -> r

from F_c and

c -> r

from F_b.

Thus r is a sink of the precedence tournament T_right.

If F_r ordered b before c, then T_right would have transitive Hamilton order

b,c,r.

The triangle theorem the common-gap theorem above would make

(b,c,r)

non-tight.

But F_a contains the consecutive local path

... ell,b,c,r ...,

so (b,c,r) is tight.

Contradiction.

Hence F_r orders

c before b.

Then T_right has transitive Hamilton order

c,b,r,

so the common-gap theorem above makes

(c,b,r)

non-tight.

Boundary antisymmetry gives

(r,b,c)

tight.

This proves the second assertion. ∎



Fix one exact two-cover for each deletion label and form the compatibility graph.

A compatible triangle with cyclic precedence has no outside vertex adjacent to two of its vertices, by the fourth-cover localization theorem above.

A compatible triangle with transitive precedence can participate in a compatibility diamond only through the two physical vertices neighboring its common insertion gap:

- the left neighbor may complete the edge joining the source and middle triangle states;
- the right neighbor may complete the edge joining the middle and sink states.

Whenever such a diamond exists, its two nonadjacent deletion covers disagree by reversing the corresponding label pair, and boundary antisymmetry exports the explicit tight triple displayed above.

Thus diamonds in the compatibility graph are not support-only phenomena: they carry forced orientation data in H. ∎

---

# Compatibility diamonds rotate the triangle; two diamonds force a tight cycle

Let `H` be a boundary tournament with `pc(H)>2`. Let `F_a,F_b,F_c` be a pairwise-compatible exact deletion-two-cover triangle with the one-gap structure of `the common-gap theorem above`. Assume its precedence tournament is transitive, relabelled

`a -> b -> c`, `a -> c`.

Write the common exceptional path as `P=L,R` at the common insertion gap, so locally

`F_a: (L,b,c,R)|Q`,
`F_b: (L,a,c,R)|Q`,
`F_c: (L,a,b,R)|Q`.

By `the two-deep-gap theorem above`, both `L,R` are nonempty; let `ell` be the last vertex of `L` and `r` the first vertex of `R`.

## Theorem

1. If an exact cover `F_ell` of `H-ell` is compatible with both `F_a` and `F_b`, then `(b,a,c)` is tight.
2. If an exact cover `F_r` of `H-r` is compatible with both `F_b` and `F_c`, then `(a,c,b)` is tight.
3. Consequently, if both compatibility diamonds exist, then the three triangle labels carry the tight cyclic ordering `(c,b,a,c)`; equivalently `(c,b,a)`, `(b,a,c)`, `(a,c,b)` are all tight.

## Proof

The original precedence tournament has directed Hamilton path `(a,b,c)`. By `the common-gap theorem above`, that precedence-consistent triple is non-tight, so boundary antisymmetry gives `(c,b,a)` tight.

Assume first that `F_ell` is compatible with `F_a,F_b`. By `the diamond-reversal theorem above`, `F_ell` orders `b` before `a`.

Apply the one-gap theorem `the common-gap theorem above` to the compatible triangle with deletion labels `{a,b,ell}`. After deleting those three labels, the common exceptional order is obtained from the original one by deleting `ell`; the surviving label `c` is the first vertex immediately to the right of the new common insertion gap. Since `F_ell` inserts `b,a` in that order at this gap, its exceptional component has local order `...,b,a,c,...`. Therefore `(b,a,c)` is a consecutive tight triple of `F_ell`.

The right-hand statement is symmetric. If `F_r` is compatible with `F_b,F_c`, `the diamond-reversal theorem above` says that `F_r` orders `c` before `b`. Applying `the common-gap theorem above` to the compatible triangle `{b,c,r}`, the surviving label `a` is immediately to the left of the common insertion gap. Hence the exceptional component of `F_r` has local order `...,a,c,b,...`, so `(a,c,b)` is tight.

When both diamonds exist we therefore have all three triples `(c,b,a)`, `(b,a,c)`, `(a,c,b)` tight. These are exactly the cyclically consecutive triples of `(c,b,a,c)`, so `{a,b,c}` is a tight three-cycle. ∎



A compatibility diamond does more than reverse one pair order across its nonadjacent tips. It rotates the actual boundary orientation on the original compatible-triangle labels. Two-sided diamond compatibility forces the entire deleted-label triple to become cyclically tight.

This is an arbitrary-order statement: the ambient common paths may be arbitrarily long, and only the one-gap compatibility structure is used.