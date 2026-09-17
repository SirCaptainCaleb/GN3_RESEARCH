# D9 — Minimality and small-deletion structure: exactness, rail floors, and noncircular pair rigidity

Foundational smallest-counterexample development including manuscript vocabulary, minimality, small-deletion exactness and rail floors, the longest-proper-path bound, plus explicitly quarantined historical finite-base and level-nomenclature records.

## Boundary tournaments, tight paths, and path-cover convention

In the 3-uniform fully directed setting, a vertex-simple tight path is a list (v_1,...,v_k) of distinct vertices for which every consecutive ordered triple (v_i,v_{i+1},v_{i+2}) is tight. Lists of one or two vertices contain no three-vertex window, so singleton and dimer paths are vacuously tight. A path cover partitions the vertex set into vertex-disjoint tight paths, and pc(H) denotes the minimum number of parts. Thus an exact two-cover means a spanning two-path cover of a subsystem whose path-cover number is exactly two, not merely a displayed representation using two paths.

The Strong Level-(1) boundary rule is R3. For three distinct vertices u,v,w, the ordered triple (u,v,w) is tight exactly when its complete reversal (w,v,u) is bad. Equivalently, each complete-reversal pair contains exactly one tight orientation. This is the only orientation axiom used in the elementary arguments below.

## Smallest-counterexample minimality: complete proof of R4

Let H be a smallest counterexample to the assertion that every Strong Level-(1) boundary tournament has a spanning cover by at most two tight paths.

First, H itself has no spanning cover by one or two tight paths. If S is any nonempty proper subset of V(H), then the induced subsystem H[S] has smaller order and hence is not a counterexample. Therefore pc(H[S])<=2.

Choose any vertex v. The proper subsystem H-v has a cover by at most two tight paths. Adding the singleton path (v) gives a spanning cover of H by at most three tight paths. Since H has no cover by at most two paths, pc(H)=3.

Now let K be any proper graph-intrinsic tight path in H and put W=V(H)\V(K). The induced subsystem H[W] is proper, so pc(H[W])<=2. It cannot have a Hamilton tight path Q. If it did, K and Q would be two vertex-disjoint tight paths spanning H, contradicting that H is a counterexample. Hence pc(H[W])=2. Any exact two-cover P sqcup Q of H[W], together with K itself, is therefore a spanning three-cover of H. Because pc(H)=3, that three-cover is minimum and contains K literally.

This proves exactly R4. It gives no endpoint prescription for the complement cover and no assertion that every proper induced subsystem has pc exactly two. The older accepted route P2 is the compressed historical form of the same minimality argument; P601 is the fully reconstructed current route.

## Direct pair deletion: exactness and the nontrivial-rail floor

Fix distinct vertices p,t of a smallest counterexample H. By R4, pc(H-{p,t})<=2. We first exclude a Hamilton remainder.

Suppose H-{p,t} has a Hamilton tight path W=(w_0,w_1,...). If W has one vertex w_0, R3 applied to the three vertices p,w_0,t supplies a tight ordering of all three vertices, hence a spanning Hamilton tight path of H, impossible. Otherwise W has at least two vertices. Apply R3 to p,w_0,t. Some ordering K of these three vertices is a tight trimer. The suffix W'=(w_1,w_2,...) is a tight path, possibly a singleton or dimer, disjoint from K. The two paths K and W' span H, contradicting pc(H)>2. Thus H-{p,t} is not Hamiltonian, and since R4 already gives pc<=2, we have pc(H-{p,t})=2.

Now let U sqcup V be any exact two-cover of H-{p,t}. If U were a singleton {u}, R3 on p,u,t would give a tight trimer K on exactly {p,u,t}. Then K sqcup V would be a spanning two-cover of H, again impossible. Therefore |U|>=2, and symmetrically |V|>=2.

This is R429. Historical P438 and the later P608 are two recorded certificates of this same mathematical route, not two distinct proof mechanisms. Keeping the direct theorem separate is important: it proves the pair-deletion floor two without R24 or R5, whereas the sharper R168 pair floor three is downstream of R5.

## Universal exactness through four deleted vertices

Let D be any vertex set with 1<=|D|<=4. R4 gives pc(H-D)<=2. To prove R5 we must exclude the possibility that H-D is Hamiltonian.

If |D|=1, let D={x} and let K be a Hamilton path of H-x. Then the singleton (x) together with K is a spanning two-cover of H, contradiction.

If |D|=2, the two vertices of D form a vacuously tight dimer. That dimer together with a Hamilton path of H-D would again span H with two paths, contradiction.

If |D|=3, R3 guarantees a tight ordering of the three vertices in D. That tight trimer together with a Hamilton path of H-D gives a spanning two-cover, contradiction.

It remains to treat |D|=4. Suppose H-D has a Hamilton tight path K. Choose z in D and put T=D-{z}. By R3, the three vertices of T admit a tight ordering, so K sqcup T is a two-path cover of H-z. This cover is exact: if H-z were Hamiltonian, adding the singleton z would give a spanning two-cover of H. Thus H-z has an exact singleton-deletion two-cover one of whose rails is the trimer T, of order three. R24 forbids every singleton-deletion rail of order at most three. This contradiction excludes the Hamilton remainder.

Therefore pc(H-D)=2 for every D with 1<=|D|<=4. This is the current full proof P609 of R5. Its logical status must be read accurately: the steps for |D|<=3 are fully reconstructible from R3 and R4 alone, while the |D|=4 step depends genuinely on R24. Since the selected legacy route P22 for R24 is not fully reconstructible, the selected R5 route is accepted and usable but not yet fully reconstructible end to end. The older accepted P3 is the compressed historical form of this same repaired four-vertex argument.

## The small-deletion staircase rail floor

Let D have size d in {1,2,3}, and let H-D=P sqcup Q be any exact two-cover. We show |P|,|Q|>=5-d.

Suppose |P|<=4-d. Set E=D union V(P). Then E is nonempty and |E|=d+|P|<=4. The complement H-E is exactly the other rail Q, which is Hamiltonian. Hence pc(H-E)=1. But R5 applies to the deletion set E and asserts pc(H-E)=2, contradiction. Therefore |P|>=5-d. Interchanging P and Q gives the same bound for Q.

Consequently singleton-deletion exact covers have both rails of order at least four, pair-deletion exact covers have both rails of order at least three, and triple-deletion exact covers have both rails of order at least two. This is the complete proof P167 of retired but valid R168.

The implication must not be reversed in the foundational dependency graph. Although the d=1 conclusion numerically reproduces the bare R24 rail floor, R168 depends on R5, and R5's four-deletion case depends on R24. Thus R168 is a useful downstream strengthening, not a noncircular reconstruction of R24.

## Exact legacy R24 interface and what its certificate does not reconstruct

R24 states that every exact one-vertex deletion two-cover has both rails of order at least four. Equivalently for the small cases relevant here, no proper tight path of order at most three can occur as one rail in an exact singleton-deletion two-cover. Its recorded scope also preserves more than the bare numeric floor: in the same representative one may use the standard four caps, boundary-collision implications, and the disjoint companion-collision package; after two genuine two-sided enlargements the transplanted singleton packet and its witnesses lie outside the surviving ancestor core, with a core/internal vertex still available. Those historical scope clauses are part of the R24 interface and are not erased merely because the current proof effort reorganizes them into later gate geometry.

The selected proof P22 does not contain a locally reconstructible derivation of those facts. It records prior A7C2 acceptance and explicitly notes that the full historical handoff transcript was not migrated into the compact ledger. Therefore this development treats R24 as a historically accepted theorem with an incomplete proof artifact, not as newly proved here.

The modern noncircular reconstruction is O6 and is developed in D3. Its first reduction R594 shows that any failure of the rail floor must be an order-three deletion rail coupled to the synchronized transitive four-cell frame. That route, rather than R168, is the current proof-reconstruction corridor.

## Circularity ledger: which deletion facts are genuinely independent

The foundational dependency graph is deliberately asymmetric.

1. R3 and R4 alone give the direct pair-deletion theorem R429, including pc(H-{p,t})=2 and rail floor two.
2. R3 and R4 alone also prove the R5 exactness assertion for deletion sets of sizes one, two, and three.
3. The four-vertex case of R5 additionally uses the singleton-deletion rail floor R24.
4. R168 is then a short consequence of the completed R5 and gives the stronger staircase floor 5-|D| for d=1,2,3.
5. Therefore R168 cannot be fed backward as a proof of R24 without circularity.

This separation is mathematically useful. Arguments that need only pair-deletion exactness or nontrivial pair-deletion rails can cite R429 and remain independent of O6. Arguments that need the pair floor three, triple floor two, or universal exactness through four vertices necessarily enter the R24-dependent branch unless they supply a new independent proof.

## Historical proof-route disposition

The source records in this family have different historical roles.

R3 is intrinsic and requires no proof route. R4 has legacy accepted P2 and fully reconstructed accepted P601; they encode the same minimality argument, so the exposition presents that argument once while preserving both route identities in the source ledger. R5 similarly has compressed accepted P3 and full accepted P609; the latter makes the repaired four-vertex dependence on R24 explicit. R24's accepted P22 is historically canonical but not fully reconstructible, which is precisely why O6 exists. R168 has the complete accepted staircase proof P167. R429 has historical accepted P438 and later accepted P608; both implement the same direct R3+R4 pair-deletion proof, so they are preserved as provenance rather than inflated into two mathematical methods.

No accepted route is retired by this exposition. No new theorem is being self-accepted. The sections above are a connected presentation of exact source mathematics with its original review and reconstructibility distinctions intact.

## Foundational manuscript vocabulary and its revision history

R893 is the current source-grounded vocabulary interface. A fully directed hypergraph has ordered-list edges; an r-graph is r-uniform undirected and an r-digraph r-uniform fully directed. A k-orientation chooses exactly k orderings of each underlying r-edge, and an (r,k)-tournament is such an orientation of the complete r-graph. A directed tight path is a vertex ordering whose consecutive r-intervals are directed edges; tight cycles use cyclic order.

A boundary tournament is characterized locally: for every ordered (r-2)-tuple and two outside vertices u,w, exactly one of (u,v_1,...,v_{r-2},w) and its endpoint reversal (w,v_1,...,v_{r-2},u) is present. Hence it is an (r,r!/2)-tournament. R893 additionally records the manuscript vocabulary of an edge-ordered hypergraph, monotone path, and altitude alt(H), the maximum monotone-path order. In the live 3-uniform project the local boundary rule specializes to R3.

R889 is not false. It is the earlier, narrower revision containing the fully directed / boundary-tournament definitions but not the later edge-order, monotone-path, and altitude clauses. It was abandoned only because R893 subsumed that source-grounded vocabulary.

## Minimality bounds the order by the longest proper tight path

Let H be a smallest counterexample of order n and let L be the maximum order of a proper tight path in H. Fix any vertex v. By R4, H-v has a spanning cover by at most two tight paths P,Q. Both are proper tight paths of H because they omit v, hence |P|,|Q|<=L. Their supports partition H-v, so n-1=|P|+|Q|<=2L. Therefore n<=2L+1.

This is R314/P317. It is independent of R24 and is useful whenever a separate argument bounds all proper tight paths. The recorded corollary L<=5 => n<=11 is immediate.

## The legacy small-deletion profile R47 is only partially recoverable in A7C3

R47 is a retired historically accepted theorem called "Small-deletion profile staircase." The current A7C3 claim record preserves only the lead sentence "Every exact deletion cover has the following unordered rail sizes:"; the actual size table is absent. Its selected proof P45 is explicitly a legacy compressed certificate pointing back to the A7C2 theorem ledger and does not reconstruct the table.

Accordingly this migration preserves R47 as an exact historical interface but does not invent its missing numerical profile. The later R168 staircase is fully reconstructible at the mathematical level now needed here: under R5, for |D|=1,2,3 every rail of an exact two-cover of H-D has order at least 5-|D|. That later statement may overlap the lost R47 table, but the surviving sources do not justify claiming identity. R47 therefore remains a documented historical gap rather than being silently collapsed into R168.

## The exact-2+2 finite SAT detour is preserved but not promoted

R551 and its revision R559 explored a finite problem outside the live Level-(1) boundary-tournament hypothesis: exact 2+2 systems on at most eight vertices, asking for a spanning tight path. The mathematical proposal was supported by a claimed SAT enumeration, and R559 even names the historical artifact path `artifacts/exact22_span_sat.py`, but that artifact is not present in the authoritative A7C3 proof record. The deposited proof objects therefore do not permit independent reconstruction of the exhaustive computation.

Both revisions remain `needs_more_work` and retired. They are not evidence for a theorem used by R24, R4, or the small-deletion staircase, and this migration does not import their conclusion into the Level-(1) spine. Their value is historical: they document a broader finite-base experiment and the exact reason it could not be certified. If the original SAT certificate is ever recovered, it can be reviewed on its own terms without changing the foundational boundary-tournament argument.

## Deprecated Level-(1)/(2)/(3) nomenclature remains a historical vocabulary record

R890 and R891 are two near-duplicate historical vocabulary revisions supplied from a human clarification. They call Level-(1) the unrestricted boundary-tournament condition, Level-(2) the subclass represented by a transitive tournament at each middle vertex, and Level-(3) the subclass induced by a linear order on unordered pairs. R891 additionally warns that the phrase “Strong Level-(1)” should not be read as a hidden extra axiom when no exact source says so.

These records are valid as preserved historical terminology, but their review status is still pending and their lifecycle is retired. They therefore do not override the source-grounded manuscript vocabulary R893 or the exact boundary reversal axiom R3. In particular, this development continues to state every mathematical hypothesis by its exact revision when the distinction matters. The purpose of retaining R890/R891 here is retrieval and provenance, not promotion of an unreviewed naming hierarchy.

## Global two-cover target and its terminology-clean restatement

The project target has two exact historical formulations under the same claim identity C2. R2 states that every finite Strong Level-(1) boundary tournament has a spanning cover by at most two tight paths. R892 is the current terminology-clean restatement: every finite 3-uniform boundary tournament has a spanning cover by at most two directed tight paths. The later formulation removes obsolete Level terminology; it does not add a theorem or a proof.

Both revisions are accepted as statements of the research target, but neither has a canonically usable proof route. Their correct mathematical status is therefore: open conjecture, not a proved premise. Smallest-counterexample arguments begin only after assuming a counterexample to this target and applying the separately proved minimality reduction R4. No section of this development upgrades either conjectural formulation.

## Every three-set has a tight trimer orientation

For any three distinct vertices {a,b,c}, choose any ordering, say (a,b,c). Boundary antisymmetry R3 says exactly one of (a,b,c) and its complete reversal (c,b,a) is tight. Whichever one is tight is a directed tight path on all three vertices. Thus every three-set admits a tight trimer orientation, which is R8.

R8 is historically superseded as a standalone interface because R3 is the stronger foundational statement, but the existence fact remains useful throughout the migration whenever a proof says “orient the remaining three vertices as a trimer.” It is recorded here explicitly so that such uses do not depend on rediscovering a historical lemma.

## Every proper tight path leaves at least five exterior vertices

Let H be a smallest counterexample and let K be a proper graph-intrinsic tight path. Put D=V(H)-V(K). Since K is proper, |D|>=1. Suppose |D|<=4. Then H-D is exactly the induced subsystem on V(K), and K itself is a Hamilton tight path of that subsystem, so pc(H-D)=1. But the accepted small-deletion theorem R5 says that deleting any set of one, two, three, or four vertices from a smallest counterexample leaves path-cover number exactly two. This contradiction proves |D|>=5.

Equivalently, if L(H) denotes the maximum order of a proper tight path, then L(H)<=|H|-5. This is the mathematical content of R169. Its selected archival proof P168 is canonically usable but not fully reconstructible from its historical record; the short derivation above recovers the theorem inside the current foundational development from accepted R5 without changing the status or identity of R169.

The dependency matters. This five-exterior floor is available in arguments allowed to use R5, and it explains many five-/six-exterior longest-path normalizations. It is not a permitted substitute inside the deliberately noncircular R24 reconstruction when that reconstruction is avoiding R5/R24.