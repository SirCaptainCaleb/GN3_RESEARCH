# Every eight-vertex boundary tournament has a balanced 4|4 two-cover

## Statement

Every boundary tournament on eight vertices has a partition into two Hamiltonian four-vertex induced subtournaments. Equivalently, every eight-vertex boundary tournament has an exact tight-path cover of component orders 4 and 4.

## Body


# Exact eight-vertex balanced two-cover theorem

Let (H) be a boundary tournament on vertex set ([8]).

For each ordered triple ((a,b,c)) of distinct vertices, exactly one of
[
(a,b,c),qquad(c,b,a)
]
is tight. There are therefore
[
3inom83=168
]
independent reversal-pair orientation variables.

For a fixed four-set (A), a Hamilton tight path on (A) is an ordering
[
(a_1,a_2,a_3,a_4)
]
for which both consecutive triples
[
(a_1,a_2,a_3),qquad(a_2,a_3,a_4)
]
are tight. Up to reversing the whole path there are (4!/2=12) candidate Hamilton orders on (A).

Suppose, for contradiction, that (H) has no complementary Hamiltonian (4|4) partition. For each of the
[
rac12inom84=35
]
unordered complementary pairs (A,ar A), and for each pair of candidate Hamilton orders (p) on (A) and (q) on (ar A), at least one of the four consecutive triples required by (p,q) must fail to be tight.

This gives an exact finite (0)-(1) feasibility system:
- (168) binary variables, one for each ordered-triple reversal pair;
- for every complementary (4+4) partition and every pair of the (12) candidate Hamilton orders on the two sides, one linear clause excluding simultaneous truth of the four required triple orientations.

Thus there are
[
35cdot12^2=5040
]
constraints. Each clause is exactly the linear inequality saying that the four relevant Boolean literals have sum at most three.

The resulting mixed-integer feasibility problem was solved exactly with HiGHS. It was declared infeasible. No relaxation, sampling, symmetry assumption, or edge-orderability hypothesis was used.

Therefore the hypothesized orientation does not exist. Every eight-vertex boundary tournament has complementary four-sets (A,ar A) such that both induced subtournaments are Hamiltonian. Choosing Hamilton paths on the two supports gives an exact (4|4) tight-path cover.

## Astra-003 consequence

Let
[
C=X|P|Q
]
be a quadratic-potential minimum in a trapped Astra-003 component with
[
|X|=3,qquad |P|=5.
]
The induced boundary tournament on
[
V(X)cup V(P)
]
has order eight, so by the theorem it has an exact (4|4) cover (R|S). Replacing (X|P) by (R|S) is one legal Astra-003 move. The quadratic contribution changes from
[
3^2+5^2=34
]
to
[
4^2+4^2=32,
]
a strict decrease of (2), contradicting minimality.

Hence no quadratic-minimal trapped Astra-003 state can contain a (3|5) pair.
