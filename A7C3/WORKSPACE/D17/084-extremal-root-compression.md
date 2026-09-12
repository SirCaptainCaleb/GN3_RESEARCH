# Edge-maximal singleton families compress to a universal source crossing or one double star

**Workspace:** D17
**State:** working
**Key:** `extremal-root-compression`

**Summary:** A collective seam-free rebuild accounts for every lost compatibility at once. In an edge-maximal singleton-cover family, the spanning odd-cycle root cannot survive without a universal source-rail crossing; a forest root likewise forces such a crossing unless the entire root is a single double star. The double-star residue is a pair of overlapping deletion-Hamiltonian non-Hamiltonian blocks, so bare hypohamiltonian-block absorption is false and actual path-order exchange remains necessary. Quiet two-pivot swaps are proved and iterate: global absence of universal source crossings forces odd order 2k+1, Hamiltonicity of every k-set, and non-Hamiltonicity of every (k+1)-set.


### 1. Universal-crossing versus collective port saturation

Retain a hypothetical smallest counterexample H and a chosen singleton-deletion cover family. Let x be a physical deletion vertex whose root edge has endpoints P,Q. Write

  Omega_P=A union {x},   Omega_Q=B union {x},

so C_x has literal Hamilton rail supports A|B, A,B are nonempty, and

  Omega_P union Omega_Q=V(H),   Omega_P intersect Omega_Q={x}.

For z in A, call z P-universally crossing relative to C_x if EVERY exact two-nonempty-path cover of H-z contains a selected adjacency with one endpoint in A-{z} and the other in B. If z is not P-universally crossing, choose an exact H-z cover with no such selected A-{z}|B state. The deleted-label substitution argument can then be completed seam-free even in its unique-transition residue. In the only nonclosing no-interior-crossing word

  (A-{z}) - x - B_1   |   B_2

(or its reversal), the contiguous (A-{z})+x subpath is tight and the original C_x rail on all of B is tight. Hence H-z has an exact replacement cover with support partition

  (Omega_P-{z}) | B.

The same statement holds dually for z in B.

If z is already incident with P, the existing compatibility-edge placement theorem already gives exactly (Omega_P-{z})|B. Therefore, if no nonincident z in A is P-universally crossing and no nonincident z in B is Q-universally crossing, choose the compatible existing cover on the incident vertices and the seam-free replacement on every nonincident vertex. Keeping C_x itself, this produces a new complete singleton-cover family with support partitions

  C_z^*: (Omega_P-{z}) | B        for z in A,
  C_x^*: A | B,
  C_z^*: A | (Omega_Q-{z})        for z in B.

Its compatibility graph is EXACTLY the union of two cliques on Omega_P and Omega_Q meeting only in x. Indeed vertices on one side have identical restrictions on pair overlaps. If u in A and v in B, the u-cover places the surviving x with Omega_P-{u,x}, while the v-cover places x with Omega_Q-{v,x}; both opposite side remainders are nonempty, so the restrictions disagree. Thus there are no cross edges.

Call this the collective double-star rebuild about x. If

  s=|Omega_P|,   t=|Omega_Q|=n+1-s,

its exact number of compatibility edges is

  F(s)=binom(s,2)+binom(t,2).

This construction is global: every collateral compatibility lost by changing individual fibers has already been counted in F(s).

### 2. Forest line-graph edge bound

Assume the current rail-incidence root R is a forest with n physical edges. Its compatibility graph is L(R), so

  |E(G)| = sum_{v in V(R)} binom(d(v),2).

Let Delta be the maximum root degree and choose a maximum-degree port P and any incident physical edge x=PQ. Since every incident physical edge lies in Omega_P,

  Delta <= s=|Omega_P|,

and s+t=n+1.

We claim

  |E(G)| <= F(s),

with equality only when R is one connected double star and the chosen maximum-degree side is saturated, |Omega_P|=d(P).

Proof. Let R have c nontrivial components and put a_v=d(v)-1. Since a forest with n edges and c components has n+c vertices,

  sum_v a_v = 2n-(n+c)=n-c <= n-1.

If Delta <= (n+1)/2, then a_v+1=d(v)<=Delta gives

  |E(G)| = (1/2) sum_v a_v(a_v+1)
          <= (Delta/2) sum_v a_v
          <= Delta(n-1)/2.

The integer minimum of F(s) over s+t=n+1 is floor(n^2/4). For odd n the last display is at most (n^2-1)/4; for even n, Delta<=n/2 and it is strictly below n^2/4. Hence |E(G)|<=F(s). Equality can occur only for odd n, Delta=(n+1)/2, c=1, and every positive a_v equal Delta-1. Since their sum is n-1=2(Delta-1), exactly two vertices have degree Delta and all others are leaves: R is the balanced double star.

If Delta>(n+1)/2, fix P with d(P)=Delta. After removing a_P=Delta-1 from the excess sum, the remaining excess is at most n-Delta, which is strictly less than Delta-1. Convexity of a(a+1)/2 therefore gives

  |E(G)| <= binom(Delta,2)+binom(n+1-Delta,2)=F(Delta).

Since s>=Delta>(n+1)/2 and F is increasing away from its midpoint on this side,

  F(Delta)<=F(s).

Equality forces c=1, all remaining positive excess to be concentrated at one second root vertex of degree n+1-Delta, and s=Delta. Thus again R is a single double star, now possibly unbalanced. This proves the claim.

### 3. Extremal compression of BOTH forest and odd-cycle roots

Choose the singleton-cover family to maximize |E(G)| over the finite product of all singleton-deletion cover choices.

FOREST. Let P be a maximum-degree root port and x any incident root edge. If neither side of C_x contains a nonincident universally crossing vertex, the collective double-star rebuild exists. By the forest bound it has at least as many compatibility edges as the extremal family. Unless R is already a single double star, the inequality is strict, contradicting maximality. Therefore an edge-maximal forest family has one of two forms:

1. some fixed source cover C_x and some same-side nonincident z have the universal physical source-crossing property; or
2. the entire rail-incidence root is one double star.

ODD CYCLE. If R is the spanning odd cycle of length n=2k+1, every port universe has size k+1. The current compatibility graph has exactly n edges. If no universal source crossing occurs relative to a chosen x, the collective rebuild has

  2 binom(k+1,2)=k(k+1)=(n^2-1)/4

compatibility edges. For every allowed odd cycle n>=5 this is strictly larger than n. Hence an edge-maximal family CANNOT remain in the spanning odd-cycle root unless a universal source crossing occurs. No cyclic Hamilton-order assumption is used.

Thus the forest-or-odd-cycle classification has a sharper extremal form:

  EDGE-MAXIMAL FAMILY => UNIVERSAL SOURCE CROSSING OR DOUBLE-STAR ROOT.

The odd-cycle structural residue is completely absorbed into the crossing branch; among forests only the double star survives without such a crossing.

### 4. Exact meaning of the double-star residue

Suppose the equality residue is a double star with central root edge x=PQ. Put

  U=K_P=Omega_P,   W=K_Q=Omega_Q,

so U intersect W={x} and U union W=V(H). The central x-cover has Hamilton rails U-{x} and W-{x}. For every u in U, compatibility at P supplies a Hamilton path on U-{u}; for every w in W, compatibility at Q supplies a Hamilton path on W-{w}. Hence both induced supports U and W are vertex-deletion-Hamiltonian.

Neither U nor W is Hamiltonian: if U were Hamiltonian, it would be disjoint from the Hamilton path on W-{x} and the two paths would span H; dually for W. Therefore the quiet equality residue is two non-Hamiltonian deletion-Hamiltonian blocks overlapping in the single physical vertex x.

This is NOT itself contradictory. In particular the familiar four-vertex no-P4 cell is already a non-Hamiltonian vertex-deletion-Hamiltonian boundary tournament, because every three-vertex subsystem has a tight Hamilton trimer. Thus a proposed theorem saying merely “deletion-Hamiltonian block plus Hamilton complement implies absorption” is false at the structural level. Any remaining double-star theorem must spend the simultaneous two-block structure, their shared vertex x, or actual path-order/crossing data.

A further exact consequence is useful. If the universal-crossing obstruction is absent not only at the central source but also after changing the bridge source to another r in U, then for each b in W-{x} one can obtain an exact H-b cover with support partition

  (U-{r}) | ((W-{x,b}) union {r}).

Thus a fully quiet double-star regime generates complete one-vertex replacement Hamiltonicity across the two sides. This is a stronger exchange reservoir than bare deletion-Hamiltonicity, but no path-order theorem consuming it is proved here.

### 5. Remaining full-theorem obstruction

The missing theorem is now cover-valued and narrow.

UNIVERSAL-CROSSING branch: for a fixed literal singleton source C_x=A|B and z in A, every exact H-z cover contains a selected A-{z}|B adjacency. One must use those actual covers together with the fixed Hamilton orders of A and B to construct a spanning two-cover. Generic R176/R428 payment does not consume this obstruction.

DOUBLE-STAR branch: two deletion-Hamiltonian non-Hamiltonian supports U,W overlap in one physical vertex x, and bridge changes can create many exact one-vertex replacement covers. One must exploit their literal Hamilton orders to absorb x or force a universal source crossing.

These are the only quiet extremal residues after the forest-or-odd-cycle support-label theorem. The arguments in this section are complete internal mathematics in this development revision, not canonically accepted standalone claims.

### 6. Quiet pivot composition and the uniform middle-layer alternative

The following argument is internal working mathematics. Its quietness hypothesis is quantified over the source covers encountered during the construction, not merely the initial double star.

Write a double-star family as D(x;A,B), where V(H)=A disjoint-union B disjoint-union {x}, |A|=k, |B|=l. Thus C_x has supports A|B, the a-cover for a in A has supports (A-a+x)|B, and the b-cover for b in B has supports A|(B-b+x). These are actual Hamilton rails.

Choose a in A and b in B. If the source C_a permits the collective rebuild of section 1 (no universal source crossing on either side), rebuilding around a gives D(a;A-a+x,B). Its b-cover is the literal exact cover with supports (A-a+x)|(B-b+a). If this source also permits collective rebuilding, rebuilding around b gives D(b;A-a+x,B-b+a). Since x belongs to the first rail, the x-cover in this family has supports

  (A-a+b) | (B-b+a).

Thus the proposed two-pivot composition really does produce a one-for-one swapped exact cover of the SAME H-x residue. No restriction of a Hamilton path across a deleted internal vertex is used: each step uses the seam-free collective rebuild. A further quiet rebuild around x restores double-star form with these new sides. All these double stars have the same compatibility edge count C(k+1,2)+C(l+1,2), so if the initial family was edge-maximal, these rebuilds remain edge-maximal.

For fixed x, the graph of k-subsets of V(H)-{x}, joined by one-for-one exchanges, is connected: whenever S differs from the current A, exchange an element of A-S with an element of S-A. Therefore, unless a universal source crossing is encountered during the pivot/rebuild sequence, EVERY partition of H-x into supports of sizes k and l is realized by an actual exact two-cover.

There is a useful global consequence. Assume NO universal source crossing exists for ANY singleton-deletion source cover and ANY vertex on either source rail. Start from any C_x=A|B and rebuild to D(x;A,B). The preceding construction saturates all k|l partitions at x. A quiet pivot to any other deletion label y, followed by the same exchanges, saturates all k|l partitions at y as well. Given any k-subset or l-subset S of V(H), choose y outside S. Saturation at y proves that S is Hamiltonian.

Suppose k<l. A Hamilton l-rail contains a contiguous tight subpath on k+1 vertices. Its complement has l vertices and is Hamiltonian by saturation, so these two paths span H: contradiction. The case l<k is dual. Hence k=l and n=2k+1. Every k-subset of H is Hamiltonian. No (k+1)-subset can be Hamiltonian, because its k-vertex complement is Hamiltonian and would close H.

We have therefore proved the sharper conditional full-theorem reduction:

  hypothetical smallest counterexample
    => a universal physical source crossing exists
       OR n=2k+1, every k-subset is Hamiltonian,
          and every (k+1)-subset is non-Hamiltonian.

In particular, every even-order smallest counterexample has a universal physical source crossing. The argument does not require an extremal cover family for this final alternative; global absence of the crossing is sufficient to construct all the needed double-star families.

Scope fences:
* Quietness of one initial source is insufficient for iteration. Every intermediate source must permit the rebuild; a failure produces the universal-crossing branch.
* The swapped supports come with actual Hamilton paths, but no relation between their path orders is asserted.
* The uniform middle-layer alternative is not presently contradictory. It asks for an orientation-level theorem: on 2k+1 vertices, Hamiltonicity of every k-set should force a tight path on k+1 vertices. Such a path would have a Hamilton k-complement and close H.
* Do not infer Hamiltonicity of arbitrary smaller subsets by restricting a k-path. Only contiguous subpaths preserve tightness automatically.


### 7. Maximum-path intersection template from the uploaded tight-path paper

Source: user-supplied main-appendix.tex, lemma labelled lem:noDisjointMaxPaths in the subsection Paths in (3,4)-tournaments. Its exact hypothesis is a TRIANGLE-FREE (3,4)-tournament, not an arbitrary (3,4)-tournament. Here triangle means a tight directed cycle on three vertices. Four orientations and absence of such triangles imply that each of the two cyclic classes of three permutations contains exactly two edges. Thus a missing orientation forces BOTH of its cyclic rotations tight. This is the precise rule used by the paper.

The extremal ordering argument itself transfers to any directed triple system. Let A=(a_1,...,a_t) and B=(b_1,...,b_t) be vertex-disjoint globally maximum tight paths, t>=2. Define out edges as in the paper: a_j a_{j+1} b_r and b_j b_{j+1} a_r for 1<=j<t and r in {j,j+1}.

If an out edge exists, choose one maximizing (j,r) lexicographically, and interchange the path names if necessary to write it as (a_j,a_{j+1},b_r). If r=t, A[1,j+1] followed by b_t already has t+1 vertices and is tight, a contradiction. Thus r<t. The only possibly bad new turn in A[1,j+1] followed by B[r,t], beyond the chosen tight out edge, is

  (a_{j+1},b_r,b_{r+1}).

It must be bad by maximum-path length. The cyclic rotation

  (b_r,b_{r+1},a_{j+1})

is also bad by the extremal choice: if r=j+1 it has a greater first index, and if r=j it has equal first index and greater second index. Hence this exact mixed triple has two absent cyclic rotations. In a boundary tournament their reversals

  (b_{r+1},b_r,a_{j+1}), (a_{j+1},b_{r+1},b_r)

are tight. The desired forward seam is not one of these reversals.

If there are no out edges, consider the vertex-simple word
  a_t,b_t,a_{t-1},b_{t-1},...,a_1,b_1.
It has 2t vertices and cannot be a tight path. Every consecutive turn has one of the forms
  (a_j,b_j,a_{j-1}) or (b_j,a_{j-1},b_{j-1}), 2<=j<=t.
Choose a bad turn. In the first form the cyclic rotation (a_{j-1},a_j,b_j) is an absent A-out edge. In the second form the cyclic rotation (b_{j-1},b_j,a_{j-1}) is an absent B-out edge. Again two specified cyclic rotations are bad on a mixed triple.

This reconstructs the paper's contradiction: its triangle-free (3,4) rule forbids either pair of bad cyclic rotations. For boundary tournaments the pairs are allowed; complete reversal gives tight turns in the opposite cyclic class and does not complete the attempted splice.

This exact transfer lemma is established internally here. It retains physical selected-path coordinates and the last-out-edge order (or the no-out alternating word). It does NOT prove maximum-path intersection in boundary tournaments.

Connection to section 6: in the uniform middle-layer residue, for every spare x and every k|k partition of H-x, both supports have Hamilton paths of globally maximum size k. Thus the transfer lemma applies to every such pair and every chosen Hamilton order. The unresolved augmentation target is to use this simultaneous availability to overcome the coordinate-labelled cyclic gaps; no theorem relating the new Hamilton orders after a support exchange is asserted.

