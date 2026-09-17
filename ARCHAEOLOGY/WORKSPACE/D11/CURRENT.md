# D11 — Hamilton-five density and Johnson paired-design geometry

Connected development of the Hamilton-five density program: the four-of-six seed, conditional density hierarchy, dual Johnson-clique inequalities, the sharper local-degree principle with its spectral alternative, exact defect identities, five-exterior sparsity, and the paired-design/routing/Levi geometry forced by equality.

## Four-of-six seed and elementary density hierarchy

Call a physical five-set **good** when it supports a tight P5 and **bad** otherwise. The density theory begins with R195, whose path-specific input is only the three-exterior pair-extension lemma R146.

Let E be any six-set and define

    M={e in E : E\{e} is good}.

Fix any three-set T inside E and put P=E\T. By R8, P supports a tight trimer. Apply R146 to that trimer and the three vertices of T. At least one pair of T extends P to a tight P5. Those three possible five-sets are exactly E\{t}, t in T. Hence every three-set T meets M. If E\M had three vertices, choosing those three as T would contradict this. Therefore |E\M|<=2 and

    |M|>=4.                                      (R195)

Equivalently every six-set contains at most two bad five-subsets. This tiny local occupancy cap is the seed from which the whole Johnson theory grows.

A first double count gives R216. For an r-set W, count incidences (U,F) with F good, |F|=5, |U|=6, and F subset U subset W. Each U contributes at least four incidences by R195, while each good F lies in exactly r-5 six-sets. Thus

    (r-5) h_5(W) >= 4 C(r,6)

and therefore

    h_5(W) >= (2/3) C(r,5).

R228 keeps a fixed s-set S, 0<=s<=3. Among the six five-subsets of U superset S, exactly s omit a vertex of S, so R195 guarantees at least 4-s good ones still containing S. Double counting gives

    h_5(W;S) >= (4-s)/(6-s) C(r-s,5-s).

The resulting guaranteed good fractions are 2/3, 3/5, 1/2, 1/3 for s=0,1,2,3. These older linear bounds remain useful at small orders even after stronger Johnson bounds appear.



## Dual Johnson-clique density inequalities

Let B be a family of k-subsets of an r-set and suppose every (k+1)-set contains at most t members of B. Write b=|B|, M=C(r,k), p=b/M, and regard B as an induced vertex set in the Johnson graph J(r,k).

Every Johnson edge F-G has two unique labels:

- its **union** U=F union G, a (k+1)-set;
- its **intersection** S=F cap G, a (k-1)-set.

These give two edge-disjoint clique decompositions of the same induced graph.

For each union U put y_U=|B cap C(U,k)|. Then

    e(B)=sum_U C(y_U,2) <= C(r,k+1) C(t,2).        (union upper bound)

For each intersection core S put

    x_S=|{F in B:S subset F}|.

Then

    e(B)=sum_S C(x_S,2),
    sum_S x_S=kb.

By Cauchy,

    2e(B)=sum_S x_S^2-kb
          >= k^2 b^2/C(r,k-1)-kb.                (intersection lower bound)

Comparing the two bounds gives R322:

    (r-k+1)p^2-p <= t(t-1)(r-k)/(k(k+1)).

Solving the quadratic yields the stated density ceiling. Equality for t>=2 forces both mechanisms to be exact: all intersection-core occupancies x_S are equal and every union clique reaches its maximum y_U=t.

For k=5,t=2 this is the original dual-clique mechanism R320. Directly, if B is the bad five-set family, R195 gives at most two bad blocks in each six-set, hence at most one bad Johnson edge in each union-indexed K6. The intersection decomposition and Cauchy give

    25b^2/C(r,4)-5b <= 2C(r,6).

With alpha=b/C(r,5), this becomes

    15(r-4)alpha^2-15alpha-(r-5)<=0,

so

    alpha <= [15+sqrt(225+60(r-4)(r-5))]/[30(r-4)].

This improves the elementary bad-density ceiling 1/3 for r>10 and tends to 1/sqrt(15). At r=11 it gives b<=148, so at least 314 of 462 five-sets are good.

The older R320 also has a spectral proof: the least Johnson eigenvalue is -5, so an induced-edge lower bound replaces the Cauchy intersection-clique calculation. The later general spectral proof of R326 below subsumes this method while preserving its distinct linear-algebraic viewpoint.



## Sharper local-degree principle and spectral alternative

R326 strengthens R322 by using the local occupancy cap pointwise rather than only in aggregate. Fix F in B. Every Johnson neighbor G of F lies with F in the unique (k+1)-set U=F union G. There are r-k such U, and each contains at most t-1 selected neighbors of F. Hence

    deg_B(F) <= (t-1)(r-k),

so

    2e(B)<=b(t-1)(r-k).                           (1)

The same intersection-clique decomposition gives

    2e(B)>=k^2b^2/C(r,k-1)-kb.                   (2)

Comparing (1) and (2), using C(r,k-1)=C(r,k)k/(r-k+1), yields

    p <= [k+(t-1)(r-k)]/[k(r-k+1)].              (R326)

For t=2 this becomes

    p <= r/[k(r-k+1)].

For Hamilton-five bad families, k=5 and therefore

    p_bad <= r/[5(r-4)],
    p_good >= 4(r-5)/[5(r-4)],

whose good-density limit is 4/5.

There is a genuinely different spectral proof P337. Let M_inc be the incidence matrix between (k-1)-sets and k-sets. Then

    M_inc^T M_inc = kI + A_J,

so every Johnson eigenvalue is at least -k. If 1_B=(b/M)1+v with v perpendicular to 1, then with Johnson degree d=k(r-k),

    2e(B)=1_B^T A_J 1_B
          >= d b^2/M - k||v||^2
          = k(r-k+1)b^2/M-kb.

Combining this spectral lower bound with the same pointwise upper degree (1) reproduces R326 exactly. Thus the Cauchy proof and incidence-spectrum proof are two reusable routes to the same sharp inequality.

Equality in R326 is also sharper than equality in R322. It forces all x_S equal, and every selected F to attain the maximum possible induced degree. For t=2 this means every (k+1)-set **containing a selected block** contains exactly two selected blocks. It does not require every (k+1)-set to be occupied.



## Conditional density hierarchy

Fix S subset W with |S|=s<=3. Bad five-set supersets of S correspond, after deleting S, to a k=5-s uniform family on N=r-s vertices. Every (k+1)-set in the quotient corresponds to a six-set containing S, and R195 still says at most two quotient blocks are bad.

Applying R326 with t=2 gives the preferred R327 bound

    p_bad(W;S) <= (r-s)/[(5-s)(r-4)].

The guaranteed good fractions tend to 4/5, 3/4, 2/3, and 1/2 for s=0,1,2,3. For every r>10 these strictly improve R228; at r=11 the global case gives at most 145 bad blocks, hence at least 317 good five-sets.

The earlier revision R324 is also mathematically valid and uses the weaker quadratic parent R322 instead. It gives

    p_bad(W;S) <= [1+sqrt(1+8(r-5)(r-4)/((5-s)(6-s)))]/[2(r-4)],

with asymptotic good fractions 1-1/sqrt(15), 1-1/sqrt(10), 1-1/sqrt(6), 1-1/sqrt(3). R327 supersedes it numerically, but R324 is retained because it is the direct quotient form of the symmetric dual-clique argument rather than the pointwise-degree refinement.



## Exact dual-clique defect identity

R325 explains precisely what the weaker R322 inequality throws away. Put

    mu=kb/C(r,k-1),
    V=sum_S (x_S-mu)^2,
    D=sum_U [C(t,2)-C(y_U,2)].

The intersection decomposition gives

    2e(B)=V+k^2b^2/C(r,k-1)-kb,

while the union decomposition gives

    e(B)=C(r,k+1)C(t,2)-D.

Equating them yields the exact identity

    V+2D
      =2C(r,k+1)C(t,2)+kb-k^2b^2/C(r,k-1).

In normalized form,

    V+2D
      = k C(r,k) [ t(t-1)(r-k)/(k(k+1)) + p -(r-k+1)p^2 ].

Thus R322 is exactly the nonnegativity shadow V,D>=0. Near equality in R322 means simultaneously nearly uniform intersection-core occupancy and nearly maximal filling of almost every union clique. This must not be confused with equality in the stronger R326, which can leave many union cliques empty.

R357 quantifies that distinction in the Hamilton-five equality case. Under R326 equality, four-core variance V is zero, but every six-set contains either zero or two bad blocks. Counting occupied six-sets gives

    D = [2(r-10)/(5(r-4))] C(r,6).

The empty-six-set fraction is 2(r-10)/(5(r-4)), tending to 2/5. So R326 equality is far from R322 equality at large order.



## Five-exterior Johnson sparsity

R243 is a separate application of the same intersection-clique technology. In a hypothetical smallest counterexample on the five-exterior equality face, let Ecal be the family of five-sets occurring as exteriors of globally longest paths. R192, developed in D24 as part of the replacement family, implies that each E in Ecal has Johnson degree at most n-5 inside Ecal.

For every four-set S put x_S=|{E in Ecal:S subset E}|. Then

    sum_S x_S=5|Ecal|,
    e_J(Ecal)=sum_S C(x_S,2),

because every Johnson edge has one four-core. The local degree bound gives

    sum_S x_S(x_S-1) <= (n-5)|Ecal|,

hence

    sum_S x_S^2 <= n|Ecal|.

Cauchy then yields

    25|Ecal|^2/C(n,4) <= n|Ecal|,

so

    |Ecal| <= [n/(5(n-4))] C(n,5).

The earlier revision R231 obtained the same ceiling spectrally from the least Johnson eigenvalue -5. R243 is preferred because its clique decomposition exposes the exact incidence mechanism; the spectral revision remains a useful alternate proof.



## Paired-design equality normal form

R375 gives the universal equality normal form for R326 when t=2. Suppose

    |B|/C(r,k)=r/[k(r-k+1)].

Equality forces constant (k-1)-core occupancy. Its value is

    mu = k|B|/C(r,k-1)=r/k.

Therefore k divides r; write r=kq. Every (k-1)-core lies in exactly q selected blocks, so B is a (k-1)-(r,k,q) design at the incidence level.

Equality in the pointwise degree bound has an equally strong local meaning. For every selected block F and every x outside F, the union U=F union {x} must contain exactly one selected neighbor of F. Since the local cap is two, that neighbor is unique and has the form

    F-f+x

for a unique f in F. Thus every occupied (k+1)-union clique contains exactly two selected blocks and every selected block has Johnson degree r-k.

The Hamilton-five specialization k=5 is R331. If equality holds in the bad-five ceiling, r=5q, every physical four-set lies in exactly q bad five-sets, and every six-set containing any bad block contains exactly two. The older Hamilton-specific proof and the universal R375 proof are mathematically the same equality mechanism, so R331 is retained as the application interface while R375 is the parent theorem.



## Arithmetic and hierarchy fences

The design normal form immediately produces divisibility constraints.

R377 gives the full lower-incidence tower. For every s<=k-1, count pairs (F,T) with S subset T subset F, |T|=k-1. If lambda_s is the number of selected blocks through a fixed s-set S, then

    lambda_s(k-s) = (r/k) C(r-s,k-1-s),

so

    lambda_s = (r/k) C(r-s,k-1-s)/(k-s),

and every displayed number must be integral.

For k=5, R346 extracts the congruence r=5q with q not congruent to 2 modulo 3, hence r congruent to 0 or 5 modulo 15. R355 adds a parity fence. For any five-set F, sum modulo two the occupancies y_U of six-sets U containing F and the occupancies x_S of four-sets S inside F. A bad block sharing four vertices with F appears once in each sum and cancels; F itself contributes r times. Under equality every y_U is 0 or 2 and every x_S=q, so

    q = q 1_B(F) mod 2.

If q were odd, every five-set would be bad, contradicting R195. Hence q is even. Combining the two arithmetic conditions gives

    q congruent 0 or 4 mod 6,
    r congruent 0 or 20 mod 30.

R353 gives the analogous conditional equality divisibility after quotienting a fixed s-set: equality in R327 forces (5-s)|(r-s). Simultaneous equality at s=0,1,2,3 would require r congruent 5 mod 60.

R356 makes a subtler point. Global R331 equality is a 4-design, so the bad fraction among five-sets through any fixed s-set, s<=4, is exactly the same global fraction r/[5(r-4)]. For s>0 this is strictly below the R327 conditional ceiling by

    s(r-5)/[5(5-s)(r-4)].

Thus global equality is conditionally uniform but never conditionally extremal at a positive level.



## Balanced swaps and girth-eight Levi geometry

R378 refines the equality design into a canonical routing. For F in B and f in F let

    A_f(F)={x outside F : F-f+x in B}.

Unique union-clique pairing says these k classes partition V\F. The core F\{f} lies in exactly q selected blocks, one of them F, so

    |A_f(F)|=q-1.

The routing is reversible: if G=F-f+x, then F and G are the two selected blocks in their common union clique, so from G the reverse swap replaces x by f. Hence f belongs to A_x(G).

R379 translates this to a partial linear geometry. Every physical (k-1)-core S supports a clique L_S of q selected blocks in J(r,k). Each selected block lies on exactly k such core-cliques and every Johnson edge belongs to exactly one. The neighborhood of any selected block is therefore the disjoint union of k copies of K_{q-1}, and the selected Johnson graph is k(q-1)-regular.

R380 gives the clean incidence representation. Form the bipartite Levi graph Lambda with selected blocks on the left and physical (k-1)-cores on the right, incidence by containment. It is (k,q)-biregular. A 4-cycle would make two selected k-sets share two distinct (k-1)-cores and hence coincide. A 6-cycle would give three selected blocks pairwise Johnson-adjacent through distinct cores. Such a Johnson triangle not lying in one core-clique is a top triangle inside one (k+1)-set, contradicting the local occupancy cap two. Therefore

    girth(Lambda) >= 8.

The left point graph is exactly the selected Johnson graph of R379. On the right, the line-intersection neighborhood of a core splits into q cliques K_{k-1}, so that graph is q(k-1)-regular.

This paired-design/Levi structure is a genuine reusable equality theory for arbitrary k, not merely bookkeeping for Hamilton-five supports.



## Interface to fixed-trimer bad graphs

The density theory alone does not force longer paths. Explicit systems even achieve unit Hamilton-five density without a P6. What equality does provide is highly rigid local bad-pair geometry. In the Hamilton-five case R341 turns each fixed trimer into a regular triangle-free bad-extension graph, and the separate Moore development shows that the remaining global equality regime must contain a P6.

That final path-growth mechanism is developed separately because its central mathematics is extremal graph theory and finite certificates, not Johnson incidence counting. The present development therefore ends at the paired-design/equality interface rather than mixing two proof languages into one oversized document.



## Exact proof-route disposition

The density development retains the original route identities as follows. R195/P195, R216/P216, and R228/P228 are the preferred elementary seed and double-count routes. R231/P231 is the accepted spectral five-exterior proof; R243/P243 is the preferred four-core clique/Cauchy proof. R320 has two accepted routes: P323 is the preferred dual-clique/Cauchy proof, while P325 is the spectral Johnson-eigenvalue alternative. R322/P327 and R325/P331 are preferred. R324/P330 is the accepted older conditional quadratic route; R327/P333 is its stronger preferred local-degree successor. R326 has two accepted methods: preferred P332 uses intersection-core Cauchy, and P337 uses the incidence-matrix identity M^T M=kI+A_J. R331 has accepted P338 as the direct Hamilton-specific equality specialization and preferred P384 through the universal paired-design parent R375/P383; these share the same equality mechanism rather than constituting different mathematics. The arithmetic and geometry chain is R346/P352, R353/P357, R355/P359, R356/P360, R357/P361, R377/P386, R378/P387, R379/P388, R380/P389.

Thus no accepted spectral route is silently replaced by a combinatorial one, and no older valid quantitative bound disappears merely because a stronger revision exists.