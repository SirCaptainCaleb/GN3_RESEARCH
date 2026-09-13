# D10 — Longest-support intersection geometry: order-ten closure and order-eleven residue

Connected reconstruction of the longest-support program. It now begins with the order-ten longest-path/profile predecessor layer, develops support incidence and overlap normal forms through the accepted R191 order-ten closure, preserves abandoned and spectral alternatives, records the general longest-path one-third bound, and retains the distinct order-eleven 5+5+1 residue geometry. Cross-owner deletion and extension engines remain exact citations.

## Longest-five support family and low-overlap localization

This development reconstructs the historical **support-family** route in the order-ten smallest-counterexample program. Its central objects are the supports of globally longest tight five-paths and their intersection pattern. Generic deletion-cover, P4-plus-trimer, and three-exterior extension lemmas are cited at their exact revisions rather than remigrated here.

The route is historically important because it contains a complete overlap-descent program, several reusable pure set-system arguments, and two distinct Johnson-scheme obstructions. Some intermediate claims were later abandoned because they depended on an abandoned endpoint-amplification theorem. Those claims are retained here as conditional historical branches, while the later accepted R147/R183 repairs are kept separate.

Throughout the order-ten branch, let F be the family of supports of globally longest tight five-paths. R9 supplies the longest-path value five. The support facts R13-R15 are valid historical starting points:

- union F is all ten vertices;
- intersection F is empty;
- any two members of F intersect;
- some two members intersect in at most three vertices;
- more locally, for every prescribed P in F either some support meets P in at most three vertices, or two one-vertex replacement supports around P already meet in exactly three vertices.

The first three assertions in R13 come respectively from the no-universal-exterior fact, prescribed-singleton roots, and the observation that two disjoint five-supports would be complementary tight five-paths and hence a spanning two-cover. R14 excludes the possibility that every pair has intersection at least four via the Johnson-clique star/top dichotomy. R15 gives the stronger radius-one alternative by forming the 5-by-5 replacement incidence graph around a fixed support and finding two disjoint replacement edges if no low-overlap support already exists.

These statements use the standing order-ten smallest-counterexample hypotheses and are not general theorems about arbitrary boundary tournaments.



## Minimum overlap three: butterfly geometry and elimination

Assume A,B in F have globally minimum intersection three. Write

    S=A cap B, |S|=3,
    U=A\B, |U|=2,
    V=B\A, |V|=2,
    R=V(H)\(A union B), |R|=3.

R98 is a pure support-counting dichotomy. For any support C meeting R, minimum overlap three gives

    |C cap (S union U)| >=3,
    |C cap (S union V)| >=3.

If C omits a vertex of S, these two inequalities together with |C|=5 and C cap R nonempty force the exact profile

    (|C cap S|,|C cap U|,|C cap V|,|C cap R|)=(2,1,1,1).

This is the **transversal** alternative. If no such support exists, every R-touching support contains all of S. Empty total intersection then prevents a support of the form S plus two R-vertices, so every R-touching support is S union {w,r} with w in U union V and r in R. For any s in S and any support D omitting s, comparison with A and B forces D to contain exactly S\{s}, to be R-free, and to have three wing vertices meeting both U and V. Comparison with each hub S union {w,r} further forces D to contain every wing w occurring in a hub. This is the **hub** alternative.

The transversal branch has a symmetric Venn normalization R100. A transversal C meets both A and B in exactly three vertices, so A,B,C are pairwise minimum-overlap supports. Their triple intersection T has size two and their union has size eight. After naming the pair-only and private regions,

    A=T union {x,y,alpha},
    B=T union {x,z,beta},
    C=T union {y,z,gamma},

with exactly two vertices delta,epsilon outside A union B union C. Re-expressing any of the three pairwise butterflies shows that the third support is again a (2,1,1,1) transversal. This symmetry is a useful normalization independent of the later cover manipulations.

R108 records an important negative result about the hub branch. The pure five-set incidence constraints alone do **not** contradict it. On blocks S={s1,s2,s3}, U={w,u}, V={v1,v2}, R={r1,r2,r3}, take

    A=S union U,
    B=S union V,
    H_i=S union {w,r_i},
    D_j=(S\{s_j}) union {w,v1,v2}.

These eight five-sets cover all ten vertices, have empty total intersection, and every pair meets in at least three vertices. The only R-touching members are the singleton-wing hubs H_i, and the only supports omitting s_j are exactly D_j. Hence any closure of the hub branch needs genuine path-orientation or cover information beyond the abstract support incidence used in R13/R98.

### Eliminating overlap three

R127 is the accepted historical elimination. Delete the common triple S. By small-deletion exactness R5, H-S has an exact two-cover. R105 observes that H-S cannot contain a P5: such a path would be globally longest and, being disjoint from S, would meet A inside U in at most two vertices, contradicting minimum overlap three. Therefore the exact cover has profile 4+3. The local lemma R126 says that a disjoint tight P4 and tight trimer always contain a P5. The 4+3 cover supplies exactly those hypotheses, contradiction.

Thus minimum overlap three is impossible. Combining R13, R14, and R127 gives R128:

    min{|A cap B| : A,B in F, A != B} is either 1 or 2.

The deletion-cover and local amplification proofs are cited at R5 and R126; the specialization above is the complete support-family use of them.



## Overlap two: disjoint-core triangle and repaired exclusions

Assume now that A,B are minimum-overlap supports with |A cap B|=2. Put

    S=A cap B, |S|=2,
    U=A\B, |U|=3,
    V=B\A, |V|=3,
    R=V(H)\(A union B), |R|=2.

R129 deletes S. Exact small-deletion structure gives a 5+3 or 4+4 two-cover of the remaining eight vertices. In the 5+3 case a P5 is already present. In the 4+4 case, orient any three vertices of one P4 as a tight trimer and apply the general R126 P4-plus-trimer lemma to the other P4, again obtaining a P5 in H-S. Let D be its support. Minimum overlap two with both A and B forces D to use at least two vertices of U and two of V, so its block profile is one of

    (2,2,1), (2,3,0), (3,2,0)

across U,V,R. Consequently one of A or B, call it L, has two minimum-overlap partners B,D whose two intersection cores inside L are disjoint two-sets.

R130 turns this into a clean triangle normalization. Let

    X=L cap B,
    Y=L cap D,
    Z=B cap D.

The sets X and Y are disjoint two-subsets of L. Any vertex of Z cap L would lie in X cap Y, so Z lies outside L. Minimum overlap gives |Z|>=2, while B\L and D\L each have size three, so |Z| is 2 or 3. Thus X,Y,Z are pairwise disjoint and inclusion-exclusion gives exactly two types:

- **type (2,2,2):** |L union B union D|=9, with one exterior vertex;
- **type (2,2,3):** |L union B union D|=8, with two exterior vertices.

R131 records the exact-root coordinates. In type (2,2,2), there are unique p,b,d and exterior e with

    L=X union Y union {p},
    B=X union Z union {b},
    D=Y union Z union {d}.

Deleting X,Y,Z gives three cyclic 5+3 roots whose short sides are respectively {p,b,e}, {p,d,e}, {b,d,e}. In type (2,2,3), with exterior e,f,

    L=X union Y union {p},
    B=X union Z,
    D=Y union Z,

and deleting X or Y gives a 5+3 root with the **same** short physical trimer P={p,e,f}.

### Type (2,2,3): the repaired common-trimer argument

R141 is the key support-level shield for the type-(2,2,3) branch. Put U=X union Y union Z, so U is the seven-vertex exterior of P={p,e,f}. No five-set P union {u,v}, u!=v in U, can support a P5. Indeed, such a P5 would be globally longest by R9. Since P cap B=P cap D is empty, minimum overlap two forces u,v both into B and both into D, hence into Z. But P cap L={p}; then P union {u,v} meets L in only p, contradiction.

Now orient P=(a,b,c) tightly. Let E_left be the exterior vertices u with (u,a,b) tight and E_right those with (b,c,u) tight. If distinct x in E_left and y in E_right existed, x,a,b,c,y would be a forbidden P5 on P union {x,y}. Therefore either one extender set is empty or both are the same singleton. Boundary antisymmetry converts every failed direct extension into a reverse terminal turn. Hence every orientation of P has one terminal dimer with seven common outside reverse witnesses, or both terminal dimers with six common reverse witnesses. This is a reusable structural strengthening, even though the canonical route to R141 is flagged not fully reconstructible in the database.

The accepted revision R147 then uses the general local pair-extension lemma R146. Choose any three distinct vertices x,y,z in U. R146 says one of P union {x,y}, P union {x,z}, P union {y,z} contains a P5, contradicting the universal shield just proved. Hence type (2,2,3) is impossible.

The earlier R133/P132 attempted to exclude this type through an endpoint-preserving amplification R132. That proof and R133 revision 1 were abandoned because R132 itself was abandoned. Their conditional mathematics is retained historically, but it is not the accepted route. R147/P146 is the repaired accepted route and does not use R132.

### Type (2,2,2): direct pair-extension contradiction

R183 eliminates the remaining type. Use the coordinates above and write X={x1,x2}. The short side P={p,b,e} of the root obtained by deleting X is a tight trimer and is disjoint from D=Y union Z union {d}. Choose any r in D. Apply R146 to P and the three exterior vertices x1,x2,r. One of

    P union {x1,x2},
    P union {x1,r},
    P union {x2,r}

supports a P5 and is therefore globally longest by R9. But P cap D is empty, x1,x2 are outside D, and only r belongs to D, so each candidate meets D in at most one vertex. This contradicts minimum overlap two.

Thus R147 and R183 eliminate both disjoint-core types, and minimum overlap two is impossible.

The abandoned R134/P133 had tried to amplify type (2,2,2) into type (2,2,3) using the same abandoned R132 endpoint theorem; R135/P134 then concluded minimum overlap one. These remain useful records of an earlier strategy but are not part of the accepted proof. The later R183 argument is both shorter and avoids the abandoned dependency.



## Overlap one: replacement lower bound versus Johnson cut ceiling

After the accepted elimination of overlap two, the only value left by R128 would be one. The eventual contradiction has two ingredients: a replacement lower bound supplied by the separate pair-extension machinery, and a pure Johnson-graph upper bound.

R184, developed in D24 as part of the five/six-exterior replacement machinery, says the following. Fix A in F, let E be its five-vertex complement, choose a tight trimer P inside E, and write E\P={x,y}. For each a in A, at least one of

    (E\{x}) union {a},
    (E\{y}) union {a}

is a global-longest support. Rotating over all two-hole choices yields R189: for each fixed a, at most one of the five replacement columns (E\{z}) union {a} can fail. Hence each A has at least twenty distinct longest-five supports meeting A in exactly one vertex.

The clean combinatorial obstruction is R186. Let Omega be a 10-set and F any family of 5-subsets containing no complementary pair. Write barF={Omega\A:A in F}. In J(10,5), each four-set C indexes a clique

    K_C={C union {v}:v outside C},

which is K_6, and every Johnson edge belongs to exactly one such clique, namely the clique indexed by the four-set intersection of its endpoints. Put r_C=|F cap K_C| and s_C=|barF cap K_C|. Since F and barF are disjoint, r_C+s_C<=6. Therefore

    r_C s_C <= (r_C+s_C)^2/4 <= (3/2)(r_C+s_C).

Summing over four-cores C,

    e_J(F,barF) <= (3/2) sum_C(r_C+s_C).

Every five-set contains five four-subsets, so sum r_C=5|F| and sum s_C=5|barF|=5|F|. Hence

    e_J(F,barF) <= 15|F|.                         (Johnson cut ceiling)

On the other hand, in the longest-support family complementary members cannot both occur, because two complementary tight five-paths would be a spanning two-cover. Every successful replacement B(a,z)=(E\{z}) union {a} has complement

    (A\{a}) union {z}

in barF and this complement meets A in four vertices, so it is a Johnson neighbor of A. The twenty-replacement lower bound therefore gives at least twenty F-to-barF Johnson edges incident with every A:

    e_J(F,barF) >= 20|F|.

This contradicts the ceiling 15|F|. R190 is the preferred accepted version of this proof; R187 is an earlier accepted version with the same mathematical route and slightly more expanded bookkeeping. The two are not distinct conceptual proofs, so they are consolidated here while both exact proof objects remain retrievable.

Thus minimum overlap one is impossible. Together with R128 and R183, the historical accepted support-family chain excludes every possible minimum overlap in the order-ten smallest-counterexample setting.



## Independent spectral Johnson-scheme alternative

C181 had an earlier accepted revision R185 with genuinely different mathematics, so it must not disappear merely because R186 is cleaner for the later contradiction.

Let G be the graph on the 252 five-subsets of a ten-set Omega, joining S,T when |S cap T|=1. Let J=A_1 be ordinary Johnson adjacency, joining intersection-four pairs. For a j-subset T define f_T(S)=1_{T subset S}, let W_j span these functions, and U_j=W_j cap W_{j-1}^perp. A one-swap count gives

    J f_T=((5-j)^2-j)f_T+(6-j) sum_{T' subset T, |T'|=j-1} f_{T'}.

Thus J acts on U_j with eigenvalue theta_j=(5-j)^2-j, namely

    25,15,7,1,-3,-5.

Let A_i be the Johnson distance-i matrix. The standard one-swap recurrence gives A_i=p_i(J); iterating to distance four yields

    p_4(t)=(t^4-32t^3+166t^2+864t-1575)/576.

Evaluating on the six theta_j gives

    25,-15,7,-1,-3,5.

Since A_4 is exactly adjacency in G, G is 25-regular and every nonconstant eigenvalue is at most 7. If H is a complement-free family of m five-sets and chi is its characteristic vector, decompose

    chi=(m/252)1+v,   v perpendicular to 1.

Then ||v||^2=m-m^2/252 and the Rayleigh bound gives

    2e(H)=chi^T A_4 chi
          <=25m^2/252 + 7(m-m^2/252).

Hence average degree in G[H] is at most

    7+18m/252.

Complement-freeness gives m<=126, so the average degree is at most 16. This spectral result is independent of the later K_6 Johnson cut estimate and remains a useful standalone finite-set theorem.



## Abandoned amplification branches

Three abandoned claims record mathematically coherent implications under abandoned premises:

1. **R133/P132, type-(2,2,3) via endpoint amplification.** Conditional on the abandoned R132 endpoint-preserving P4-plus-trimer amplification, the shared-trimer motif was claimed impossible. This route was superseded by accepted R147/P146.
2. **R134/P133, type-(2,2,2) amplifies to type-(2,2,3).** This also uses abandoned R132 and abandoned R133. It is not an accepted exclusion. Accepted R183 replaces it directly.
3. **R135/P134, minimum overlap one.** This deduction used the two abandoned exclusions above, so it was itself abandoned. The later accepted chain obtains a stronger end result without it.

R137/P136 gives another abandoned branch: assuming minimum overlap one and the abandoned universal endpoint three-set completion R136, a singleton-deletion 5+4 root would force a ten-member cone of longest-five supports over one fixed endpoint pair. The cone is a useful structural picture, but it is conditional on the abandoned completion theorem and is not consumed in the accepted Johnson route.

Keeping these branches matters because they explain which amplification ideas were tried and why the successful repair changed mechanism rather than merely changing notation.



## General no-one-vertex-extension fence

R585 is a simple general statement independent of order ten. If K is globally longest with support X and r lies outside X, then H[X union {r}] cannot be Hamiltonian, because such a Hamilton path would have |X|+1 vertices. Consequently any local theorem, such as R561, that would Hamilton-extend X by every exterior vertex is automatically incompatible with global-longestness whenever the exterior is nonempty.

This observation is elementary but useful as an interface check: proposed absorber or replacement arguments around a globally longest carrier must not secretly manufacture a one-vertex Hamilton extension.



## Recovered support normalizations

Three accepted historical support lemmas belong to this development even though their titles did not trigger the initial metadata routing.

**R104: core-singleton eight-support classification.** In the transversal coordinates A=T∪{x,y,alpha}, B=T∪{x,z,beta}, C=T∪{y,z,gamma}, delete one core vertex t∈T. The singleton-root theorem R46 supplies a longest five-rail D. Minimum overlap three with A,B,C forces the other core vertex tprime into D. Writing E=D−{tprime}, the three inequalities

    |E∩{x,y,alpha}|≥2,
    |E∩{x,z,beta}|≥2,
    |E∩{y,z,gamma}|≥2

leave exactly eight possibilities: {x,y,z,w} with w∈{alpha,beta,gamma,delta,epsilon}, or {x,y,beta,gamma}, {x,z,alpha,gamma}, {y,z,alpha,beta}. This is a finite support-incidence classification; the singleton-root existence is a cited foundational dependency rather than remigrated here.

**R107: hub radius-one-or-singleton-star compression.** In the hub alternative of R98, let W be the wing vertices that occur in an R-touching hub. R98 forces every S-omitting support to contain W. If a hub wing and the opposite replacement support complete the same side of A or B, one obtains an actual radius-one replacement pair. If that never happens, W must be a singleton {w}; after exchanging U and V if necessary, every S-omitting support is B−{s}+{w} and every R-touching support is A−{u}+{r}. Thus the apparently diffuse hub branch compresses to two explicit stars unless it already contains the radius-one configuration.

**R142: private-endpoint motif rotation.** In a type-(2,2,3) motif, the endpoint-replacement rule R140 says that if a private endpoint t of D lies in Y, then (D−{t})∪{p} is again a longest support. Renaming Yprime=(Y−{t})∪{p} and pprime=t gives a new type-(2,2,3) motif with the same X,Z and exterior pair, while the shared short trimer rotates from {p,e,f} to {t,e,f}. The symmetric statement holds on the B/X side. R140 is cited as the endpoint-replacement theorem; the support-family consequence R142 is developed here.

These lemmas are not needed by the final short R147/R183 repair, but they are distinct valid mathematics from the historical branch and explain the internal geometry that the repair bypassed.



## Support-incidence does not force complementary swaps

R204 records a negative result that is easy to lose when pruning the replacement era. The support-membership conclusion “every carrier vertex has four successful five-exterior replacements” does not by itself force any complementary carrier swap.

For disjoint K,E with |K|=m≥6 and |E|=5, choose for each k∈K one failed hole h(k)∈E. Declare exactly the four supports (E−{z})∪{k}, z≠h(k), successful, and declare every complementary candidate (K−{k})∪{z} non-Hamiltonian. The marked supports satisfy the relevant exterior-size floor, but there is no complementary carrier replacement. This is an abstract contract model, not a realizable boundary tournament. Its mathematical content is logical independence: any synchronization theorem needs more than support incidence.



## No order-ten smallest counterexample

R191 is the preferred capstone. R128 leaves minimum support overlap one or two. R147/R183 eliminate overlap two, so overlap one would remain. The complete twenty-versus-fifteen Johnson contradiction is derived once in the section “Overlap one: replacement lower bound versus Johnson cut ceiling”; applying that result eliminates overlap one and therefore rules out an order-ten smallest counterexample. R188/P188 is the earlier accepted revision of the same route and remains exact historical provenance. No second copy of the Johnson cut calculation is needed here.

## Exact proof-route disposition

The connected exposition above is the mathematical home; the original proof objects remain the exact provenance and retrieval layer. Exact historical routes are:

- R13/P11 and R14/P12: accepted preferred legacy-compressed certificates; their deductions are expanded in Sections 1-2.
- R15/P13; R98/P97; R100/P99; R104/P103; R105/P104; R107/P106; R108/P107: accepted preferred routes for the low-overlap and overlap-three normalizations.
- R127/P126; R128/P127; R129/P128; R130/P129; R131/P130: accepted preferred route chain into the overlap-two triangle.
- R133/P132, R134/P133, R135/P134, R137/P136: valid but abandoned proof routes, retained only as the conditional endpoint-amplification branch described above.
- R141/P140; R142/P141; R147/P146; R183/P183: accepted preferred repaired overlap-two routes.
- R185/P185 and R186/P186: two accepted, genuinely different Johnson proofs, spectral intersection-one versus four-core K6 cut.
- R187/P187 and R190/P190: accepted versions of the same twenty-versus-fifteen overlap-one route; P190 is preferred.
- R188/P188 and R191/P191: accepted versions of the same order-ten capstone; P191 is preferred.
- R204/P204 and R585/P663: accepted preferred logical-independence and longest-support fences.

R99/P98, R184/P184, and R189/P189 are separate mechanism routes and are cited rather than rederived here; their specializations are shown where consumed.



Newly incorporated exact source routes are R9/P7 with accepted legacy alternative P175; R10/P8 and its stronger successor R46/P44; R11/P9; R12/P10; R219/P219; R316/P319; R317/P320; and R318/P321. The R9 and R11 arguments above are later complete reconstructions in the exposition, not newly accepted P-objects. R12 is deliberately left at its exact legacy-certificate status.

## Order-ten predecessor layer

The historical order-ten program did not begin at R13. Four earlier claims are mathematical inputs to the support-family language and are retained here with their exact reconstructibility distinctions.

**R9, longest-path order five, has a short modern reconstruction.** Assume the standing hypothetical order-ten smallest counterexample. The small-deletion corollary R169 says every proper tight path leaves at least five exterior vertices, hence every proper tight path has order at most five. The finite-base theorem R193 says every six-set contains a tight P5, hence H contains a tight path of order at least five. Therefore the global longest proper-path order is exactly five. This is a complete later reconstruction of the statement of R9; it does not erase the original accepted legacy routes P7 and P175, and it is not being self-promoted as a new canonical proof object. P175 remains historically useful because it records the old Type-13 Mate-Fork closure, but its upstream dependency package is incomplete.

**R10/R46, prescribed singleton roots.** For any prescribed z, R4 gives a cover of H-z by at most two paths, and it cannot be Hamiltonian because adding singleton z would two-cover H. Thus it is exact. The two rail orders sum to nine and each is at most five by R9, so they are 5 and 4. This reconstructs the profile part of R10/R46. The stronger R46 reverse-star/witness package remains attached to its accepted legacy proof P44 and is not silently claimed from this counting argument.

**R11, three-deletion staircase profile.** Delete any three vertices. R5 gives exact pc=2 and R168 gives rail floor two. The two rail orders sum to seven; R9 bounds each by five. Hence the unordered profile is exactly 5+2 or 4+3. This reconstructs the numerical statement of R11 from the later clean deletion interfaces.

**R12, no universal exterior vertex.** For every vertex z there is a global-longest P5 containing z. The retained P10 is an accepted legacy audit certificate with a corrected one-hole shell and explicitly forbids implicit cyclic rotation/reversal. The compact A7C3 source does not contain the entire expanded implication ledger. Therefore R12 remains mathematically accepted and source-accounted, but this development does not pretend to have reconstructed a new full proof from the later support lemmas.

These four claims explain why the R13 family has union V(H), empty total intersection, and all supports of common order five.



## Arbitrary-order longest-path scale

R219/P219 is a clean orthogonal consequence of smallest-counterexample minimality. Let K be a global-longest proper tight path of order L and let E be its exterior. R4 gives an exact two-cover E=P sqcup Q. Global maximality gives |P|,|Q|<=L, so |E|<=2L and n=L+|E|<=3L. R169 gives the independent lower bound |E|>=5. Hence L>=ceil(n/3). Equality n=3L holds exactly when |P|=|Q|=L, in which case H is literally partitioned into three global-longest paths of order L. This is useful beyond the order-ten branch and is not a gate-specific statement.



## Order-eleven longest-five residue

The historical order-eleven branch is a separate support geometry and is retained even though it did not close the global problem. Assume |H|=11 and every proper tight path has order at most five.

**R316/P319.** For any v, minimality covers H-v by at most two tight paths. Ten vertices must be partitioned between two paths of order at most five, so every such cover is exactly P5 sqcup P5. Both rails are global-longest. Thus every vertex is the unique omission of a pair of disjoint global-longest five-supports.

**R317/P320.** Fix a root H=K sqcup Q sqcup {e} with K,Q both P5. The equal-order reverse-four theorem R44 supplies disjoint cross-rail reverse P4s on the first two and last two vertices of K,Q. The three vertices left over, k_3,q_3,e, admit a tight trimer by R8. Hence every such singleton root has a literal companion 4+4+3 spanning cover. R44 is the generic equal-order reverse-four path-interaction theorem and is cited rather than redeveloped.

**R318/P321.** Take one reverse P4 A from R317 and the disjoint leftover trimer T. The generic P4-plus-trimer extension theorem R138 forces a P5 on one of its six candidate supports. Because five is globally longest, this P5 is another global-longest support. Its overlap signature with (K,Q,{e}) is one of (3,2,0),(2,3,0),(2,2,1),(3,1,1),(1,3,1). Thus every singleton root forces a third mixed longest support bridging its two disjoint P5 rails. R138 is the generic P4-plus-trimer extension theorem and is cited rather than redeveloped.

This order-eleven residue is mathematically distinct from the order-ten minimum-overlap contradiction and remains searchable as such.

