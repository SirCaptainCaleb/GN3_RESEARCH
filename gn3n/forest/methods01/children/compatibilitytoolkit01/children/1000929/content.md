# Arbitrary selected deletion supports form a forest or a spanning odd cycle

## Statement

Let H be a finite boundary 3-tournament with pc(H)>2. Choose one two-cover A_d|B_d of H-d for each distinct label d in D. In the simple graph J of distinct component supports, join A_d to B_d by the edge labeled d. Then J is a forest, or D=V(H), n=|V(H)| is odd, and J is a single n-cycle whose supports all have size (n-1)/2. Two chosen covers are support-compatible exactly when their selected edges share a support vertex; consequently the support-compatibility graph is L(J). Tree components have the support and symmetric-difference formulas proved below and a constant unordered deletion-cover size profile. If J is connected and D=V(H), a tree J must branch. In the odd-cycle case n=2k+1, with edge S_i S_{i+1} labeled d_i, S_i={d_{i+1},d_{i+3},...,d_{i+2k-1}} (indices modulo n).

## Body


Retain H with pc(H)>2, a set D of distinct deletion labels, and one chosen two-cover F_d=A_d|B_d of H-d for each d in D. Each cover has exactly two nonempty paths. Neither path is a singleton: otherwise adding the omitted vertex d to the singleton makes a two-vertex tight path, which together with the other component would two-cover H.

Form a simple graph J whose vertices are the distinct component supports appearing in these covers, and whose edge e_d joins A_d to B_d. The label of e_d is d. The graph is simple, because a pair of supports determines its union and therefore determines the unique omitted vertex. It has no isolated vertices by construction.

**Theorem.** Exactly one of the following holds:

1. J is a forest.
2. D=V(H), n=|V(H)| is odd, and J is a single cycle of length n. Every component support in the cycle has size (n-1)/2.

In particular, a proper subset of the deletion labels always yields a forest.

**Proof.** Fix a ground vertex x. On every selected edge other than e_x, exactly one endpoint support contains x. Thus membership of x gives a bipartition of J-e_x; if x is not a selected deletion label, it gives a bipartition of all of J. The endpoints of e_x both omit x.

Suppose J contains a cycle C of length ell, and let e_x be one of its edges. The remaining path C-e_x connects two supports omitting x, and membership of x alternates at each edge of this path. Consequently ell-1 is even, and ell is odd.

If a ground vertex y is not among the labels of C, membership of y alternates around all of C, impossible on an odd cycle. Hence the labels of C are all the ground vertices. Because selected edge labels are distinct, no selected edge lies outside C. There are no isolated support vertices, so J=C and D=V(H).

On every cycle edge the endpoint support sizes sum to n-1. Alternating this identity around the odd cycle forces every support size to be (n-1)/2. This proves the dichotomy.

This proof is the elementary membership argument behind the loaded sharp-shell statement. Its hypotheses show that the sharp-shell restriction is unnecessary. The conclusion does NOT say that these balanced paths are globally longest.

### Support compatibility is exactly a shared component support

**Lemma.** Two chosen deletion covers F_a and F_b are support-compatible if and only if they share a component support.

**Proof.** A shared support immediately gives agreement of the two restricted support partitions. Conversely suppose the restricted partitions agree. Write F_a=A|B with b in A. Since neither component is a singleton, the common partition on H-{a,b} consists of the two nonempty classes A-{b} and B. In F_b the restored vertex a belongs to one of these classes. If it joins B, then A and B+{a} are disjoint Hamiltonian supports covering H, a contradiction. Therefore it joins A-{b}, and B is a component support of both covers.

It follows that the graph of support compatibility of the chosen covers is exactly the line graph L(J). The full compatibility graph G is a subgraph of L(J); agreement of the path orders is its additional requirement. This assertion concerns support compatibility, not the ordinary graph-theoretic supports of components of G.

### Exact support sets in a tree component

Let T be a tree component of J, let L be its set of ground-vertex edge labels, and fix its bipartition X,Y. Put Z=V(H)-L. There is a partition Z=Z_X disjoint-union Z_Y such that every support vertex in X contains precisely Z_X from Z, and every support vertex in Y contains precisely Z_Y from Z. Indeed, for a ground vertex outside L, membership alternates on every edge of T.

For a support vertex u in X,

    S_u = Z_X union { label of the first edge on the path from x to u : x in X-{u} }.

For a support vertex v in Y,

    S_v = Z_Y union { label of the first edge on the path from y to v : y in Y-{v} }.

Here a vertex of J is itself a support set; S_u is used merely to distinguish the support from the graph vertex in the formulas.

**Proof.** Root T at u in X. An edge label e is absent from both endpoint supports of its edge. Along the path from an endpoint to u, membership in the label alternates at every other edge. If the endpoint of its edge nearer u has depth h, then e belongs to S_u exactly when h is odd, equivalently when the farther endpoint has even depth. These are precisely the parent edges of the vertices x in X-{u}. Their labels are distinct. This gives the formula. The Y formula is identical.

In particular all X-supports have size |Z_X|+|X|-1, and all Y-supports have size |Z_Y|+|Y|-1. The two sizes sum to n-1, and every selected deletion cover belonging to this tree component has this same unordered size profile.

There are also exact distance formulas. If u,v lie in the same bipartition class and P_T(u,v) is their tree path, then

    S_u symmetric-difference S_v = labels(P_T(u,v)).

If they lie in opposite classes, then

    S_u symmetric-difference S_v = V(H)-labels(P_T(u,v)).

To verify these, remove an edge with label e. Along any path not crossing that edge, membership of e alternates with bipartition class; the two endpoints of the removed edge both omit e. If u,v are on the same side of the edge, their memberships agree precisely when their classes agree. If the edge separates u,v, that condition is reversed. Ground vertices outside L belong to exactly one bipartition class throughout T. These observations give the displayed identities.

### Explicit cycle supports

In the exceptional case n=2k+1, write the cycle support vertices as S_0,...,S_{n-1} and let d_i label S_i S_{i+1}, with indices modulo n. Then

    S_i = {d_{i+1}, d_{i+3}, ..., d_{i+2k-1}}.

This follows by starting at the edge bearing a specified label, where membership is zero at both ends, and alternating around the rest of the cycle. Equivalently, S_i is the set of labels of the unique perfect matching of the support-cycle with vertex S_i removed.

Again, this is a description of the chosen balanced covers. It does not assert that their order k is the maximum tight-path order in H.

### A connected support graph cannot be a spanning tree path

Suppose J is connected and a tree, and D=V(H). If J were a path of odd length, its endpoints would lie in opposite classes. Their tree path contains all ground labels, so the opposite-class symmetric-difference formula would make their support sets equal. They would be the same vertex of J, a contradiction.

If J were a path of even length, its endpoints would lie in the same class. Their support symmetric difference would be all of V(H); thus they would be disjoint Hamiltonian supports whose union is V(H), giving a two-cover. This is also impossible.

Therefore a connected selected support graph must either branch as a tree or be the exceptional odd cycle. This is a structural statement for arbitrary orders, not a fixed-small-order analysis.


Scope: this removes the sharp-half-order and minimum-counterexample assumptions of 1000829. It does not say the balanced paths in the cycle are globally longest. The proof is self-contained; 1000829 is provenance, not a logical premise.