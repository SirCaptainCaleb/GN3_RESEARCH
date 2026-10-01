# The n<=12 strict two-thirds search reduces to three structural classes

## Statement

Let H be a positive-minimum-degree linear triple system on 6<=n<=12, with maximum path length L and minimum degree delta. If H has a nonspecial edge and 3delta>2L+2, then H belongs to one of three classes: (I) L=3 and delta=3; (II) n=12, L=4 and H is 4-regular with 16 edges; or (III) n=12, L=5 and H is 5-regular, equivalently a one-point puncture of an STS(13).

## Body

Let H be a linear 3-uniform hypergraph on n vertices, with 6<=n<=12 and positive minimum degree delta. Let L be its maximum linear-path length, so ell_0=L+1. Suppose
  delta/ell_0 > 2/3,
equivalently
  3delta > 2L+2.
Assume H has a nonspecial edge. We reduce H to three explicit structural classes.

First, a linear L-edge path uses 2L+1 vertices, so n<=12 gives L<=5.

L<=1.
If delta>=2, some vertex is incident with two distinct edges, which form a two-edge linear path. Hence L>=2, contradiction. Thus no strict-threshold case occurs here.

L=2.
The strict inequality gives delta>=3. Since H is P_3-free, the certified exact P_3 theorem gives |E(H)|<=n, while minimum degree gives 3|E(H)|>=3n. Thus |E(H)|=n and equality in the P_3 theorem forces H to be a disjoint union of Fano planes. Because n<=12 and delta>0, H is a single Fano plane. Every Fano edge is special of rank two: for an edge e and any desired last vertex z in e, choose another vertex x in e\{z} and any other block f through x; then f,e is a two-edge path ending in e with last vertex z. Thus no nonspecial example occurs.

L=3.
The strict inequality gives delta>=3. Since H is P_4-free, the exact P_4 theorem gives |E(H)|<=4n/3. If delta>=4, then 3|E(H)|>=4n, so equality holds throughout: H is 4-regular and equality in the exact P_4 theorem forces a disjoint union of affine planes of order 3. Positive minimum degree and n<=12 leave one 9-vertex affine plane component. Its edges are special (equivalently by block-transitivity, or directly from its spanning three-edge path certificates). Hence any nonspecial strict-threshold example with L=3 must have
  delta=3.
This is Class I.

L=4.
Now delta>=4 and H is P_5-free. The certified exact P_5 theorem gives
  |E(H)| <= 15n/11,
while minimum degree gives
  |E(H)| >= 4n/3.
Linearity also gives n>=2delta+1>=9.

For n=9, the degree bound forces |E(H)|=12 and H is 4-regular. Every vertex is then paired exactly once with every other vertex across its four incident triples, so H is a Steiner triple system on 9 vertices. The STS(9) is unique up to isomorphism and is the affine plane AG(2,3). In that plane two blocks are disjoint exactly when they are parallel. If a four-edge linear path e_1,e_2,e_3,e_4 existed, the nonconsecutive pairs e_1,e_3 and e_2,e_4 would be disjoint, hence parallel in their respective pairs. Since e_1 meets e_2, those two parallel classes are distinct, so e_1 must meet e_4. But e_1 and e_4 are also nonconsecutive in the path and must be disjoint, a contradiction. Thus AG(2,3) is P_4-free, contrary to L=4.

For n=10, minimum degree gives |E(H)|>=14, whereas 15n/11<14, contradiction.

For n=11, both inequalities force |E(H)|=15. Equality in the exact P_5 theorem forces the unique extremal G_0, represented by a one-factorization of K_6 with five color-center vertices. Each color center has degree three, contradicting delta>=4.

For n=12, both inequalities force |E(H)|=16. Since the degree sum is 48 and delta>=4, H is 4-regular.

Thus the only unresolved strict-threshold possibility with L=4 is
  n=12, delta=4, |E(H)|=16, H P_5-free and 4-regular.
This is Class II.

L=5.
The strict inequality gives delta>=5. Linearity implies n>=2delta+1>=11.

If n=11, every degree is exactly five, so the degree sum would be 55, not divisible by three, impossible.

If n=12, the maximum possible degree in a linear triple system is five, so H is 5-regular and has 20 edges. Each vertex is paired inside blocks with exactly ten of the other eleven vertices. Hence the uncovered-pair graph is 1-regular, i.e. a perfect matching of the twelve vertices. Add a new point infinity and, for each uncovered pair {a,b}, add the block {infinity,a,b}. Every pair is then covered exactly once, so the resulting 13-point system is an STS(13), and H is its one-point puncture.

Thus the only unresolved strict-threshold possibility with L=5 is
  a one-point puncture of an STS(13).
This is Class III.

Therefore the finite strict-threshold assertion tested computationally in d9ee4adc37d3 is reduced completely to the following three human subproblems:
(I) P_4-free linear triple systems with delta=3;
(II) 12-vertex 4-regular P_5-free linear triple systems;
(III) one-point punctures of STS(13).
Proving all edges special in these three classes eliminates the finite search entirely.