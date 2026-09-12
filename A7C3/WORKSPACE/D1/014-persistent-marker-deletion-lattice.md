# Persistent markers force graded deletion exactness and common-source constraints

**Workspace:** D1
**State:** established
**Key:** `persistent-marker-deletion-lattice`

**Summary:** Universal internality implies exact two-covers after every deletion of at most three vertices meeting a marker, with rail floors 3,2,1. Two markers thus share a nontrivial double-deletion source; simultaneous endpoint insertions have no matching. With selected marker separation, Hamilton complements force marker-capacity constraints and non-Hamiltonian four-sets.

Let H be a hypothetical smallest counterexample, let D be a pair, and put W=V(H)-D. Let B be a nonempty set of vertices that are internal in EVERY exact two-cover of H[W]. The PERSISTENT alternative of extremal-recompletion supplies B=X, but the first assertion below needs no selected B-B separation and no four-set hypothesis.

Graded deletion exactness. For any S subset W with 1<=|S|<=3 and S intersect B nonempty, provided W-S is nonempty,
  pc(H[W-S])=2.
Moreover, in every exact two-cover of H[W-S], each rail has order at least 4-|S|.

Proof. Choose b in S intersect B. Every set of at most three vertices containing b has a Hamilton path with b as an endpoint: singletons and dimers are immediate; for {b,y,z}, one of (b,y,z) and (z,y,b) is tight by R3. If H[W-S] were Hamiltonian, its Hamilton path together with this path on S would be an exact two-cover of H[W] exposing b, a contradiction. Minimality supplies the upper bound two. Now suppose a source rail A has |A|<=3-|S|. The set A union S has at most three vertices and contains b, so it has a Hamilton path exposing b. Replace A by that path and keep the other source rail literally. This again two-covers W with an exposed b, a contradiction. This proves the rail floor. No R24, R5, R168, pair payment, or trimer-return theorem is used.

In particular, for distinct x,y in B, H[W-{x,y}] has an exact two-cover with both rails nontrivial. This is one common source residue for the two markers, not an identification of independently chosen covers of W-x and W-y. Singleton deletion at a persistent marker has both rails of order at least three, recovering the direct source-rail floor in extremal-recompletion. Triple deletion meeting B is still exact, even though singleton source rails are then allowed.

A simultaneous insertion constraint on the common source is immediate. Fix a two-cover A disjoint-union C of W-{x,y}. Form the bipartite graph with left vertices x,y and right vertices A,C, putting an edge when that marker can be attached at either end of the indicated source rail while leaving its order unchanged. This graph has no matching of size two: the two matched attachments would yield a W two-cover exposing the markers. If both markers have an available rail, all their available rails must consequently be the same single rail. Even on that rail, attachments at opposite ends cannot be jointly available: the rail has order at least two, so the two new endpoint turns are separate certified turns, and placing x and y at opposite ends would again yield a forbidden W cover. Same-end attachments are not asserted composable. This is a common-residue compatibility constraint, not a closure argument.

There is also a complementary Hamilton-support constraint using the full PERSISTENT hypothesis. Assume every W two-cover keeps B internal and selects no B-B edge. Let Z be a nonempty proper subset of W whose complement is Hamiltonian. Every Hamilton path on Z, if any, must have both endpoints outside B and no adjacent B vertices. Hence
  |Z-B| >= |Z intersect B|+1
is necessary for Z to be Hamiltonian. Indeed j internal separated markers on one path require at least j+1 other vertices. If this inequality fails, H[Z] is non-Hamiltonian, and minimality makes its path-cover number exactly two. In particular, a four-set Z containing at least two persistent markers and having Hamiltonian complement must itself be non-Hamiltonian. This gives an exact point at which non-Hamiltonian four-cell structure can enter the persistent branch.

Scope. These are consequences of universal internality over the entire fixed W-cover fiber, not of a single selected MAX5 representative. Exactness after deletion here is conditional on persistence and is not the unrestricted small-deletion theorem R168. The simultaneous insertion condition is necessary; absence of a matching does not rule out insertions requiring cuts or rearrangement. No identification of historical paid-floor ancestry with the present source cover is made. Full internal proof supplied; pending independent mathematical review.
