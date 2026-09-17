# Singleton-cover compatibility is a triangle-free rail-incidence line graph

**Workspace:** D17
**State:** working
**Key:** `singleton-compatibility-graph`

**Summary:** Singleton-cover compatibility has a canonical rail-incidence root. Actual port universes now force that root to be a forest or one spanning odd cycle; any proper induced compatibility cycle of length >=4, or any induced even cycle, therefore closes H. Whole-clique repairs retain fixed Hamilton complements; the forest and spanning alternating odd-cycle cases remain open.

### 1. A sparse compatibility backbone already glues

Choose for every physical vertex x an actual two-nonempty-path cover C_x of H-x, and let sigma_x be its unordered support partition. As proved in `codimension-one-coherence`, in a counterexample both rails of every C_x have at least two vertices. Define the singleton compatibility graph G on V(H) by

  xy in E(G)  iff  sigma_x and sigma_y agree as equivalence relations on V-{x,y}.

Full pairwise compatibility is unnecessary. Suppose merely that for every distinct physical u,v the graph G-{u,v} is connected. Then H has a spanning two-cover.

For distinct u,v choose any deletion vertex x outside {u,v} and declare u~v when u,v lie in the same sigma_x block. If y is another eligible deletion vertex, a path x=x_0,x_1,...,x_k=y in G-{u,v} exists. Along every compatibility edge x_i x_{i+1}, the same-block status of the surviving pair {u,v} agrees, so the status propagates along the path. Hence ~ is well defined. For three distinct u,v,w choose x outside them; transitivity follows inside sigma_x. Three inequivalent representatives would likewise survive some deletion and contradict the two blocks of that sigma_x. There are at least two classes because every sigma_x has two nonempty blocks. Thus there are exactly two global classes A,B.

For each x, sigma_x is the restriction of A|B to H-x. Neither class is singleton: deleting its sole vertex would leave a one-block restriction, contrary to the two nonempty rails of C_x. Choose a in A and b in B. In C_a one whole rail has support B, and in C_b one whole rail has support A. Those two certified tight Hamilton paths are disjoint and span H.

Thus a hypothetical counterexample forces G-{u,v} to be disconnected for some physical pair {u,v}; equivalently, under the usual order assumptions the compatibility graph has vertex connectivity at most two. A repair theorem therefore need not make every singleton pair compatible. It is enough to build a compatibility backbone surviving every two vertex deletions.

### 2. A compatibility edge has a forced deleted-label placement

Fix x and write the two rail supports of C_x as A|B. Let y in A and suppose xy is a compatibility edge. Compatibility determines the restriction of sigma_y on V-{x,y} as (A-{y})|B. There are only two placements for the surviving deleted label x in sigma_y. If x were placed with B, then the C_x rail on all of A and the C_y rail on B union {x} would be two disjoint tight paths spanning H, impossible. Therefore in a counterexample

  sigma_y = (A-{y} union {x}) | B.

The dual statement holds for y in B. In words: along a compatibility edge, the exchanged deleted labels must occupy the corresponding same rail class. The opposite placement is already a closing splice with no new seam.

### 3. Every neighborhood is exactly two anticomplete rail cliques

Continue with C_x having supports A|B. Split the neighbors of x as

  N_A(x)=N_G(x) intersect A,   N_B(x)=N_G(x) intersect B.

If y,z are both in N_A(x), the forced placement above gives

  sigma_y=(A-{y} union {x})|B,
  sigma_z=(A-{z} union {x})|B.

After deleting y,z these partitions agree, so yz is an edge. Thus N_A(x) is a clique; N_B(x) is a clique by the same argument.

If y in N_A(x) and z in N_B(x), then on V-{y,z}, sigma_y places x with A-{y} while sigma_z places x with B-{z}. Both surviving side sets are nonempty because the rails of C_x have order at least two. Hence the restrictions disagree and yz is not an edge. Therefore

  G[N(x)] = G[N_A(x)] disjoint_union G[N_B(x)]

with both pieces cliques and no cross edge. This is stronger than merely saying the neighborhood is coverable by two cliques: the two rail cliques are physically determined by C_x and are anticomplete.

### 4. Canonical rail-incidence root

The preceding local structure canonically reconstructs a graph R whose line graph is G. For each x create two formal ports (x,A_x),(x,B_x), one for each chosen rail support of C_x. Whenever xy is a compatibility edge, identify the port of x corresponding to the rail containing y with the port of y corresponding to the rail containing x. Take the transitive closure of these identifications.

The local two-clique lemma makes every identification class coherent. If ports of x-y and x-z lie in the same x-rail class, then yz is a compatibility edge; repeating this observation along an identification chain shows that all physical deletion vertices represented in one port class are pairwise compatible through that same rail class. No identification class can contain both ports of one physical x, since that would put two neighbors from opposite x-rails into one compatibility clique, contradicting the anticompleteness just proved.

Let the vertices of R be the resulting port classes and let each physical x be an edge e_x joining its two port classes. Then two physical vertices x,y are adjacent in G exactly when e_x,e_y share a port class. Hence

  G = L(R).

Moreover R is triangle-free. If root edges e_x,e_y,e_z formed a triangle on three distinct root ports, then x,y,z would be pairwise adjacent in G. At x, however, y and z would meet the two different ports of e_x, hence lie on opposite rails of C_x; the local two-clique lemma would force yz to be a nonedge, contradiction.

Thus every chosen singleton-cover family in a counterexample carries a canonical triangle-free rail-incidence graph R: physical deletion vertices are its edges, and the two endpoints of e_x are precisely the two compatibility ports of the two rails of C_x. This representation uses only the actual chosen support partitions and the no-two-cover obstruction.

### 5. The seam-free repair is a whole-clique port move

Let ab be a nonedge of G. In C_b write the rail containing a as A={a} union S and the opposite rail as B=T_0. The sharpened deleted-label substitution lemma in `codimension-one-coherence` says: either C_a contains a literal selected S--T_0 adjacency, or there is an exact replacement cover C_a^* with support partition

  (A-{a} union {b}) | B.

Assume the repair branch. It does more than add the single compatibility edge ab. Let c be any current neighbor of b. If c lies on the same C_b rail A as a, then the forced edge-placement formula gives sigma_c=(A-{c} union {b})|B. Restricting sigma_c and sigma_a^* to V-{a,c} gives the same partition, so ac becomes compatible. If c lies on the opposite rail B, the two restrictions place b on opposite sides, so ac is not compatible.

Therefore the repaired a inherits the entire b-side rail clique

  K_b(a) = {b} union { c in N_G(b) : c lies on the same C_b rail as a }.

No assertion is made about vertices that were not neighbors of b; extra compatibility may appear, but the whole displayed clique is guaranteed. In the root R, this operation moves one port of the deletion edge e_a onto the root endpoint of e_b corresponding to the rail of C_b that contains a.

This gives an exact extremal consequence. Choose the singleton-cover family to maximize |E(G)|. For a nonedge ab, if

  |K_b(a)| > deg_G(a),

then the seam-free repair would produce a new a-cover of degree at least |K_b(a)| while changing no graph edge not incident with a. Hence the total number of compatibility edges would strictly increase, contradicting maximality. Consequently in an edge-maximal family every such degree-pressure nonedge must be in the other branch: the actual chosen C_a contains a selected adjacency crossing the two source rail supports of C_b.

This is a genuine multi-fiber repair statement, though not yet closure. A free repair clones an entire compatibility clique at once; failure of the move under a strict degree advantage forces a named source-rail crossing. The unresolved cases are the degree-balanced/sparse rail-incidence configurations where every available target port is too small to force an improving move, together with the consumption of the resulting source crossings.

Status: all statements in this section are complete internal arguments in this DR revision and have not undergone independent canonical review. No accepted standalone theorem is asserted. The remaining full-theorem target is to combine the low-connectivity triangle-free rail-incidence structure with the forced crossing branch, or to find a stronger extremal potential whose permitted port moves always improve unless H closes.

### 6. A rail clique carries one fixed Hamilton complement

Let K be one nontrivial port clique of the rail-incidence representation and choose x in K. Let A be the C_x rail containing K-{x}, let B be the opposite C_x rail, and put Omega=A union {x}. For every y in K, compatibility xy and the forced deleted-label placement give

  sigma_y = (Omega-{y}) | B.

Thus B is a fixed physical support carrying a tight Hamilton path in every y-fiber, while Omega-{y} carries a tight Hamilton path for every y in K. The definition is independent of the anchor x: changing x within K gives the same fixed opposite support B and the same universe Omega.

Now take z in Omega-K. Then z lies on the K-side rail A of C_x but xz is not a compatibility edge. Apply the ordered deleted-label substitution test z<-x. If the chosen C_z has no selected adjacency crossing the two source rail supports A and B of C_x away from the exchanged labels, the seam-free repair constructs an exact C_z^* with support partition

  (Omega-{z}) | B.

By the clique-cloning calculation, z then becomes compatible not only with x but with every member of K. Thus a missing same-side port vertex has an exact dichotomy: it can be adjoined to the entire common-Hamilton rail clique by one cover replacement, or its chosen deletion cover contains a literal crossing between the fixed source supports Omega-{x} and B.

In an edge-maximal compatibility family, if |K|>deg_G(z), the first alternative would raise the degree of z to at least |K| and strictly increase |E(G)|. Hence every such low-degree z in Omega-K must carry the crossing alternative against the same fixed two-support frame. This concentrates many potential global obstructions onto one common Hamilton complement B.

The saturated case Omega=K has a different exact meaning: B is Hamilton and Omega-{y} is Hamilton for every y in Omega. Closure would follow if Omega itself were Hamilton, but that last implication is not proved; a non-Hamiltonian deletion-Hamiltonian Omega is therefore a precise residual species rather than something to call solved.


### 7. The support labels force a forest or one spanning odd cycle

The triangle-free root R above is much more restricted once its actual rail supports are retained. For each root vertex P (a port class), let K_P be the set of physical vertices whose root edges are incident with P. Choose x in K_P, let A_x be the rail support of C_x corresponding to P, and define Omega_P=A_x union {x}. This is well defined: for two incident physical edges x,y in the same port class, the forced placement formula gives A_y=(A_x-{y}) union {x}. It also defines Omega_P for a singleton port class.

If the physical edge x of R has endpoints P,Q, its two rail supports in C_x partition V(H)-{x}. Therefore
  Omega_P union Omega_Q = V(H),
  Omega_P intersect Omega_Q = {x}.
In particular x belongs to both Omega_P and Omega_Q.

The root has no parallel edges: if distinct physical edges x,y had the same endpoints P,Q, the same intersection would have to equal both {x} and {y}. It has no loops by the earlier port argument, and every root vertex is incident with an edge by construction.

Fix any physical vertex y, regarded as an edge of R. Color each root vertex P by
  epsilon_y(P)=1 if y in Omega_P, and 0 otherwise.
For every root edge x other than y, the two endpoint colors differ, since the union/intersection identities imply y belongs to exactly one of its endpoint universes. At the edge y itself both endpoint colors equal 1. Thus R-y is bipartite, with the two endpoints of y given the same color.

Now suppose R contains a simple cycle C. Choose y in E(C). Along C-y the colors alternate, while its endpoints have the same color. Hence |E(C)|-1 is even, so C has odd length. If there were any edge z outside E(C), epsilon_z would be a proper two-coloring of all edges of C, impossible for an odd cycle. Consequently E(R)=E(C). There are no isolated root vertices, so R is exactly that one odd cycle. It is of length at least five because the root is triangle-free.

We have proved: in a hypothetical counterexample, for EVERY chosen singleton-cover family its canonical rail-incidence root is either a forest (possibly disconnected), or a single odd cycle containing every physical edge. No extremal choice, payment theorem, R24, or computation is used.

Equivalently the compatibility graph G is either the line graph of a forest, or one odd cycle spanning all physical vertices of H. In the forest case every induced cycle of length at least four is absent: a chordless cycle in a line graph of a tree would require an underlying root cycle; alternatively leaf-edge removal successively removes vertices whose remaining neighbors form a clique. The same argument applies componentwise.

Useful conditional closure certificate: if some chosen singleton-cover family has an induced compatibility cycle of length k>=4 which is even OR omits a physical vertex of H, then H has a spanning two-cover. For otherwise the classification just proved forbids that cycle. This implication does not assert that such a compatible family can be constructed, and a compatibility cycle is a cycle of deletion labels, not a tight path cycle in H.

In the sole odd-cycle case, let the root edges in cyclic order be x_0,...,x_{n-1}, with n=2k+1. The partitions themselves are forced:
  sigma_{x_i} =
    {x_{i+1},x_{i+3},...,x_{i+2k-1}} |
    {x_{i+2},x_{i+4},...,x_{i+2k}},
with indices modulo n and the two blocks unordered. To see this, fix y=x_j. The epsilon_y colors are 1 at both endpoints of x_j and alternate along the remaining even path of the cycle. Evaluating membership at the two endpoints of x_i gives exactly the displayed alternating blocks. Each block has a certified Hamilton path supplied by C_{x_i}; no cyclic order of those Hamilton paths is asserted.

Scope and status: this is a complete internal extension of the port and forced-placement arguments in this section, not a canonically accepted standalone theorem. It narrows the remaining full-theorem exchange problem to forest compatibility and the fully spanning odd alternating family. It does not prove an improving port move, odd-cycle absorption, or compatibility of path orders under reassembly.

