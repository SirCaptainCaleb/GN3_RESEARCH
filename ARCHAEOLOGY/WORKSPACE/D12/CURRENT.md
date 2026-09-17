# D12 — Fixed-trimer bad graphs: Mantel thresholds, Moore fences, and P6 growth

Connected extremal-graph development around a fixed tight trimer. It derives triangle-free bad-extension graphs, preserves two internal Mantel proofs and sharp finite counterexamples, records the exact K2,2-to-P6 certificate, develops the girth-five Moore bound and spectral degree restriction, and uses them to obtain asymptotically unit P5 density in the P6-free branch and to destroy global Johnson equality.

## Fixed-trimer bad graph and two internal Mantel proofs

Fix a tight trimer support P and a disjoint set X. Define the **bad-extension graph** G_P on X by

    xy in E(G_P)  iff  P union {x,y} does not support a tight P5.

The general pair-extension lemma R146 immediately gives R328: G_P is triangle-free. Indeed, for any three distinct x,y,z outside P, R146 says at least one of Pxy,Pxz,Pyz supports a P5, so not all three graph edges can be bad.

This translation is powerful because path-extension failure is now encoded by an ordinary graph whose extremal structure can be analyzed without carrying ordered-turn notation at every step.



### Two internal Mantel proofs

Triangle-freeness gives

    e(G_P) <= floor(|X|^2/4),

with equality exactly for the balanced complete bipartite graph. The project contains two useful internal derivations rather than relying on an unnamed external theorem.

### Maximum-degree proof P599

Let m=|X|, choose v of maximum degree Delta, put A=N(v) and B=X\A. Triangle-freeness makes A independent, so every edge has an endpoint in B. Therefore

    e(G)<=sum_{b in B}d(b)<=|B|Delta=(m-Delta)Delta<=floor(m^2/4).

If equality holds, comparison of sum_{b in B}d(b)=e(A,B)+2e(B) with e(G)=e(A,B)+e(B) forces e(B)=0. Equality in Delta(m-Delta) then makes the two independent parts balanced, and equality e(G)=|A||B| forces every cross edge. Thus G is K_{floor(m/2),ceil(m/2)}.

### Inductive proof P600

For any edge uv in a triangle-free graph, N(u) and N(v) are disjoint, so d(u)+d(v)<=m. Hence some vertex has degree at most floor(m/2). Remove such a vertex and apply induction:

    e(G)<=floor((m-1)^2/4)+floor(m/2)=floor(m^2/4).

At equality the smaller graph is extremal and the removed vertex must have the maximum allowed degree. Triangle-freeness forces all of its neighbors into one bipartition class, recovering K_{k,k} for m=2k and K_{k,k+1} for m=2k+1.

P600 was later marked abandoned as a route because P599 is shorter, but the induction itself is valid and remains a useful alternative proof method.

Thus R328 gives both the numerical bad-pair ceiling and the exact equality structure. In the equality case every within-part pair is a good P5 extension of P.



## Density alone does not force P6

Several exact finite examples fence what can be concluded from high Hamilton-five density alone.

R321 is a seven-vertex Strong system of maximum tight-path order exactly five in which 18 of the 21 physical five-sets are Hamiltonian. Its complete local turn tables are stored in R230/R321; exhaustive verification checks all ordered six-tuples and exhibits a P5. Thus P6-free systems can already have good-five density 6/7.

R335 is sharper: there is a six-vertex Strong system in which **all six** five-subsets support P5s but the six-set has no P6. The exact six local tournament tables and exhaustive 720-order P6 check are retained in R335/P341. Therefore even density one does not, by itself, force growth from P5 to P6.

R332 supplies the opposite sanity check: define tight(a,b,c) exactly when a<c in one fixed total order of the vertices. Boundary reversal antisymmetry holds, and every subset is Hamiltonian by increasing order. So boundary antisymmetry itself places no upper restriction on Hamilton-five density either.

These examples explain why the later positive results must use the **pattern** of bad pairs, not merely their number.



## Exact Mantel threshold on four outside vertices

For |X|=4, Mantel equality means G_P=K_{2,2}. R348 proves that this exact pattern forces a P6 on P union X.

The proof is a finite exact certificate, retained in P577. After relabeling P={0,1,2}, X={3,4,5,6}, take bad pairs 35,36,45,46 and good pairs 34,56. Boundary antisymmetry has 105 reversal-pair Boolean variables. Absence of a P6 gives 5040 four-literal clauses, one for every ordered six-tuple. Each of the four bad five-supports contributes 120 clauses forbidding a Hamilton order, for 480 clauses. For each of the two good supports, 120 witness variables encode a chosen Hamilton order via three implications plus one existence clause. Together with the unit turn fixing the trimer, the instance has

    345 variables,
    6243 clauses.

P577 specifies a deterministic DPLL rule and records an exhaustive run visiting 18,393 nodes to maximum branch depth 32 with no satisfying leaf. An independent binary MILP translation is infeasible as a separate check. Hence no Strong assignment realizes the K2,2 bad graph while avoiding P6.

This certificate is deliberately not duplicated verbatim here; P577 is the exact retrievable certificate and verifier specification.

The threshold is sharp. R347 gives a seven-vertex explicit Strong system in which G_P on four outside vertices is the three-edge star K_{1,3}, only one edge below Mantel extremality, yet the whole seven-set has maximum path order five. Its full turn table, good/bad pair list, sample P5s, and exhaustive no-P6 verification are retained in R347/P576.

Therefore the statement is genuinely an equality phenomenon at m=4, not a vague near-density principle.

R349 extends exact Mantel equality to every m>=4. A balanced complete bipartite extremal bad graph has both parts of size at least two. Choosing two vertices from each part induces K2,2, so R348 yields a P6 on those four vertices together with P.



## Johnson equality gives regular five-way bad-edge routing

Assume the global Hamilton-five bad family attains the R326/R331 density ceiling on an r-set W. Write r=5q. Fix any tight trimer P and X=W\P.

R341 shows that G_P is q-regular and triangle-free on

    |X|=5q-3

vertices. For x in X, its bad neighbors correspond exactly to bad five-blocks containing the four-core P union {x}; R331 gives q such blocks. Triangle-freeness is R328.

There is also exact routing around every bad edge xy. For z outside Pxy, the occupied six-set P union {x,y,z} contains exactly one additional bad five-set. If xz or yz is bad, triangle-freeness allows at most one and it is the unique partner. If neither is bad, the unique partner is obtained by deleting exactly one of the three trimer vertices from P and adding x,y,z.

R342 balances these five routing channels. For a fixed bad edge xy, the remaining outside vertices split into

    N(x)\{y},
    N(y)\{x},
    A_1,A_2,A_3,

where A_i routes through deletion of trimer vertex p_i. Each class has exactly q-1 vertices. The two neighbor classes have this size by q-regularity and triangle-freeness. For A_i, the four-core (P\{p_i}) union {x,y} lies in exactly q bad blocks; one is Pxy, leaving q-1 partners. The five disjoint classes have total size 5(q-1)=|X|-2, so they partition the remainder.

This five-way routing is a concrete local shadow of the paired-design geometry in D11.



## No-P6 girth-five reduction and Moore edge bound

If G_P contains a 4-cycle, triangle-freeness makes its four vertices induce exactly K2,2. R348 then produces a P6. Therefore R366 gives the clean dichotomy:

- either P union X contains a tight P6;
- or G_P has no triangles and no 4-cycles, hence girth at least five.

The no-P6 branch can therefore use ordinary girth-five extremal graph theory.



### Moore edge bound and equality geometry

R363 is a self-contained bound for any simple m-vertex graph G with no triangles or 4-cycles:

    e(G) <= m sqrt(m-1)/2.

For a fixed vertex v, triangle-freeness makes N(v) independent. C4-freeness makes the sets

    N(u)\{v},   u in N(v),

pairwise disjoint and disjoint from N(v). Hence

    1 + sum_{u in N(v)} d(u) <= m.

Sum over v. The double sum becomes sum_u d(u)^2, giving

    sum_u d(u)^2 <= m(m-1).

Cauchy now yields

    (2e)^2=(sum d)^2 <= m sum d^2 <= m^2(m-1),

which proves the bound.

Equality is rigid. Cauchy forces regularity d=sqrt(m-1), so m-1=d^2. Equality in every radius-two count means that for each v, the vertex v, its neighbors, and all second-neighborhood sets N(u)\{v} partition the whole graph. Equivalently adjacent vertices have no common neighbor and every nonadjacent pair has exactly one. This is exact diameter-two girth-five Moore geometry.

Applying R363 to the no-P6 branch of R366 gives

    e(G_P) <= m sqrt(m-1)/2,

so bad-pair density is at most 1/sqrt(m-1) and at least

    [1-1/sqrt(m-1)] C(m,2)

earlier pairs extend the trimer to a P5.



## P6 or asymptotically unit P5 density

R367 double-counts the previous bound over all physical triples. If an r-set W has no P6, every three-set supports some tight trimer by R8. For each triple P, R366 bounds the number of bad pairs outside P by

    (r-3)sqrt(r-4)/2.

Summing over all C(r,3) triples counts each bad five-set exactly C(5,3)=10 times. Hence

    10|B| <= C(r,3)(r-3)sqrt(r-4)/2.

After division by C(r,5),

    |B|/C(r,5) <= 1/sqrt(r-4).

Thus every r-set satisfies the dichotomy:

    either a tight P6 exists,
    or Hamilton-five density >= 1-1/sqrt(r-4).

This tends to one. In the no-P6 branch it improves the unconditional Johnson bound r/[5(r-4)] exactly beyond r=20, with equality of the two numerical ceilings at r=20.

This does not contradict R335: the six-vertex unit-density example lies at the tiny-order end where the square-root bound is weak.



## Spectral restriction on exact Moore graphs

R369 classifies the possible degrees of exact diameter-two girth-five Moore graphs arising from equality in R363.

Let G be d-regular on d^2+1 vertices with exact Moore geometry. Its adjacency matrix satisfies

    A^2=(d-1)I-A+J.

On the all-ones vector the eigenvalue is d. On its orthogonal complement, every eigenvalue t satisfies

    t^2+t-(d-1)=0.

Write Delta=sqrt(4d-3). The two roots are (-1+-Delta)/2 and their multiplicities are

    m_+- = d^2/2 +- d(d-2)/(2Delta).

For d=2 the cycle case is allowed. For d>=3, integral multiplicities force Delta to be rational, hence an odd integer q. Then

    q^2=4d-3,
    d=(q^2+3)/4.

Integrality further gives q | d(d-2). Modulo q, 4d=3 and 4(d-2)=-5, so gcd(q,d) divides 3 and gcd(q,d-2) divides 5. Thus q divides 15. The positive odd possibilities giving d>=3 are q=3,5,15, hence

    d in {3,7,57}.

Together with d=2,

    d in {2,3,7,57}.                              (R369)

R368, the older statement that no 4-regular Moore graph exists on 17 vertices, follows immediately. It also has a direct historical eigenvalue proof using the irrational roots of t^2+t-3 and their impossible multiplicities; this is retained as P372 even though R369 subsumes it.



## Global Johnson equality forces P6

R362 combines the Johnson equality theory of D11 with the Moore branch here.

Assume global R331 equality and write r=5q. The congruence and parity fences R346/R355 force q even and q congruent 0 or 1 modulo 3, so q>=4. Fix a tight trimer P. R341 gives a q-regular triangle-free bad graph G_P on

    m=5q-3

vertices.

If G_P has a C4, R348 gives a P6 and we are done. Otherwise G_P has girth at least five. R363 gives

    q <= sqrt(m-1)=sqrt(5q-4),

or

    (q-1)(q-4)<=0.

Since q>=4, this forces q=4. Then m=17=q^2+1 and equality holds in the Moore bound, so G_P has exact Moore geometry of degree four. R369 forbids degree four. Contradiction.

Therefore G_P must contain a 4-cycle, and R348 converts it to a tight P6. This proves R362.

The historical direct route P366 performed the special 17-vertex strongly-regular eigenvalue contradiction inside the equality proof. The preferred modular route P376 factors that calculation through the general R363/R369 theorems. Both are valid; the latter is the reusable parent structure.

R354 records an important comparison of equality regimes. Under global Johnson equality, G_P is q-regular on 5q-3 vertices, so it has q(5q-3)/2 edges. For q>1 this is strictly below the Mantel extremal count, and for arithmetically admissible q>=3 the ratio to n^2/4 is at most 1/2. Thus Johnson equality is locally regular but nowhere near fixed-trimer Mantel equality. The Moore argument, not Mantel equality itself, is what bridges this gap.



## What the bad-graph representation contributes

This development leaves a crisp hierarchy of facts:

- R328: every fixed-trimer bad graph is triangle-free.
- R347/R335/R321: high or even unit P5 density alone does not force P6.
- R348: an induced K2,2 bad pattern on four outside vertices does force P6, by exact finite certificate.
- R366: absent P6, every bad graph has girth at least five.
- R363: girth five imposes the square-root Moore edge bound.
- R367: globally, P6-free Strong systems have asymptotically unit P5 density.
- R369: exact Moore equality allows only degrees 2,3,7,57.
- R362: the regular bad graphs forced by global Johnson equality cannot survive without creating P6.

The core mathematical mechanism is ordinary extremal/spectral graph theory fed by one local path-extension dictionary. This is why it belongs beside, but not inside, the Johnson incidence development.



## Exact proof-route disposition

The fixed-trimer/extremal branch keeps exact historical routes visible. R230/P230 is the original seven-vertex no-P6 certificate and R321/P326 adds the 18/21 density count. R328 has three recorded routes: P334 is the preferred concise triangle-free-plus-Mantel route; P599 is an accepted self-contained maximum-degree proof of Mantel equality; P600 is valid but abandoned as a route because its full induction is longer, and is preserved as a genuinely different proof method. R347/P576 is the sharp K1,3 near-equality counterexample; R348/P577 is the exact 345-variable, 6243-clause K2,2-to-P6 certificate; R349/P353 is the larger-m equality corollary. R341/P347 and R342/P348 give the equality regularity and five-way routing. R363/P367 is the Moore edge bound. R364/P368 is the earlier accepted no-P6 fixed-trimer formulation and R366/P370 its preferred sharper dichotomy. Likewise R365/P369 is the earlier global density revision and R367/P371 the preferred dichotomy. R368 has two accepted proofs, P372 is the direct 17-vertex irrational-multiplicity argument and P375 derives it from R369/P374. R362 has accepted P366 (direct special-degree argument), P373 (factored Moore-parent route), and preferred P376 (generic Moore edge plus degree restriction); P373 and P376 are closely related factorizations, while P366 preserves the historical direct calculation.

The finite certificate payloads remain in their P-objects rather than being duplicated in the development body.