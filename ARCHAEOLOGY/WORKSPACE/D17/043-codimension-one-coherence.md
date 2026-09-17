# Codimension-one coherence, deleted-label substitution, and the hidden pair-fiber lift

**Workspace:** D17
**State:** established
**Key:** `codimension-one-coherence`

**Summary:** Singleton-deletion gluing and deleted-label substitution. Zero substitution defect closes H. Any ordered incompatibility either exposes a literal selected crossing between the two source rail supports, or admits a seam-free exact repair of the target fiber by combining a contiguous S+b subpath with the untouched opposite source rail. Hidden neighboring pair-fiber conflicts lift to same-residue endpoint/internal swaps in H-p.

### 1. Coherent singleton-deletion partitions already suffice

Let H be a hypothetical smallest counterexample of order n>=4. For every vertex x choose an actual cover C_x of H-x by two nonempty tight paths. Such a choice exists from the smallest-counterexample property: if H-x is Hamiltonian, split one Hamilton path into two nonempty contiguous subpaths; otherwise use its two-cover. Let sigma_x be the unordered support partition of C_x.

Assume that for every distinct x,y the restrictions of sigma_x and sigma_y to V(H)-{x,y} agree as equivalence relations. Then H has a spanning two-cover.

Indeed, for distinct u,v choose x outside {u,v} and declare u~v when u and v lie in the same sigma_x block. This is independent of x because any two eligible deletion vertices are compared directly on the overlap where u,v survive. For three distinct u,v,w choose x outside all three; transitivity follows inside sigma_x. Thus ~ is an equivalence relation. There are at most two classes, since three inequivalent representatives would remain in some H-x and contradict the fact that sigma_x has only two blocks. There are at least two classes because every sigma_x has two nonempty blocks. For every x, sigma_x is exactly the restriction of the global classes A|B to V-x.

Neither A nor B is a singleton. If A={a}, then sigma_a would restrict to the single class B, contrary to its two nonempty blocks. Hence |A|,|B|>=2. Choose a in A. In C_a the entire class B is one rail support, so B has a Hamilton tight path. Choosing b in B similarly gives a Hamilton tight path on all of A. Those two paths are disjoint and span H. This proves the conditional gluing statement. No endpoint universality, pair-deletion exactness, or R413 is used.

A useful elementary floor accompanies this formulation. In a counterexample no exact two-cover of H-x can have a singleton rail (y): the other rail is then a Hamilton path on V-{x,y}, and that path together with the vacuous dimer (x,y) is already a spanning two-cover of H. Thus every rail used below has at least two vertices.

### 2. Deleted-label substitution turns overlap disagreement into a literal path crossing

Fix distinct a,b and actual covers C_a,C_b. In C_b let Q be the rail containing a and let T be the other rail. Write

  V(Q)={a} union S,   V(T)=T_0,

so S,T_0 are nonempty and partition V-{a,b}. The partition that would make the a- and b-deletion fibers agree is the swapped support partition of H-a

  (S union {b}) | T_0.

Define kappa(a<-b) to be the number of selected adjacencies of the two rails of C_a whose endpoints lie in different classes of this target partition. Thus kappa is path-order data, not merely a support Hamming distance.

If kappa(a<-b)=0, each C_a rail lies wholly in one target class; since both classes and both rails are nonempty, the support partition of C_a is exactly (S union {b})|T_0, so sigma_a and sigma_b agree on H-{a,b}.

Conversely, suppose the overlap partitions agree. Then C_a has support partition either (S union {b})|T_0 or S|(T_0 union {b}). The second possibility closes H immediately: Q is a tight path on {a} union S and the C_a rail on T_0 union {b} is disjoint from Q, so those two paths span H. Hence in a counterexample overlap agreement forces the first placement, and therefore kappa(a<-b)=0.

Consequently, in a counterexample

  sigma_a|_{V-{a,b}} = sigma_b|_{V-{a,b}}  iff  kappa(a<-b)=0.

In particular every disagreement is witnessed in each ordered comparison by an actual selected adjacency of C_a crossing the swapped target support. This is stronger than the abstract same-block disagreement bit.

For a chosen family {C_x}, put

  K = sum_{a != b} kappa(a<-b).

The family is finite, so K has a minimum. K=0 gives coherent singleton-deletion partitions and therefore closes H by the preceding lemma. A hypothetical counterexample forces min K>0. Unlike the pair-deletion Phi, every unit of K is a named selected state in an actual cover.

### 3. Exact normal form when the defect is not an interior source-rail crossing

Continue with Q on {a} union S and opposite source rail T on T_0. A kappa-defect is either a selected S--T_0 adjacency in C_a or an adjacency from b into T_0. Suppose there is no selected S--T_0 adjacency.

If b has no T_0-neighbor then kappa=0, so assume b has a T_0-neighbor. Because no selected S--T_0 adjacency exists, deleting b from C_a leaves only pure S-components and pure T_0-components. A direct two-rail case check now has only one nonclosing possibility.

If b is an endpoint adjacent into T_0, or if both neighbors of b lie in T_0, then the b-containing rail is a path on b together with all of T_0 and the other rail is pure S; Q together with that bT_0 rail closes H. If b has one S-neighbor and one T_0-neighbor, its rail has word S-b-T_1 or T_1-b-S. If the other rail is pure S, then b together with all of T_0 is again one contiguous subpath and Q plus that subpath closes H. Therefore the only nonclosing case is

  S-block -- b -- T_1   |   T_2

or its reversal, where T_1,T_2 are both nonempty and partition T_0.

Relative to the accepted R508 packet with deleted set {a}, absorber Q on {a} union S, and complement C=T_0 union {b}, this is exactly the R511 unique-transition word SC|C or CS|C: there is one selected S|C transition, two maximal C-blocks, the mixed C-block contains b and a proper part T_1, and the other rail is the pure C-block T_2. Hence every positive singleton substitution defect has one of two exact species:

1. an actual selected S--T_0 cross-state between the two source rail supports of C_b; or
2. the R511 unique-transition bridge cell above, to which the accepted cut-indexed seam ledger applies.

This gives a literal geometric front door for any future descent in K. It does not yet prove that replacing one or several singleton fibers lowers total K; all collateral ordered comparisons remain to be counted.

### 4. What a hidden neighboring pair-deletion conflict really contains

Return to the pair-deletion objective. Let D={p,a}, E={p,b}, W=V-{p,a,b}, and retain actual exact covers C_D of H-D and C_E of H-E whose restricted support partitions P,Q on W disagree. Delete b from C_D and a from C_E, keeping the resulting literal path forests. Call the conflict hidden in one direction when every component of that trimmed forest lies inside a block of the opposite restricted partition.

If the conflict is hidden in both directions, then the geometry is forced. Neither restricted partition can have only one block, since then a surviving whole path component would visibly cross the other two-block partition. If a were not internal in its C_E rail, trimming a would leave two path components equal to the two Q-blocks; containment in the two P-blocks would force P=Q. Thus a is internal. Its two rail fragments must lie in opposite P-blocks, while the other C_E rail lies in one P-block. Renaming the three nonempty intersections gives

  P=(X union Z)|Y,    Q=(X union Y)|Z,

and the actual covers have the literal support form

  C_D :  X - b - Z   |   Y,
  C_E :  X - a - Y   |   Z,

where each displayed atom denotes the corresponding contiguous tight fragment and the orientation of each whole rail may be either direction. The symmetric argument shows these are exactly the trimmed fragments, not merely support inclusions.

This hidden pair conflict currentizes one level upward. Taking the full a-containing rail from C_E together with the contiguous b-through-Z subpath of the b-containing rail of C_D gives an exact two-cover G_b of H-p. Dually, the full b-containing rail from C_D together with the contiguous a-through-Y subpath of C_E gives an exact two-cover G_a of H-p. Symbolically,

  G_b : (X-a-Y) | (b-Z),
  G_a : (X-b-Z) | (a-Y).

No new seam is introduced: every displayed path is a whole source rail or a contiguous source subpath.

The two H-p covers have different support partitions. More sharply, a is internal in G_b but an endpoint in G_a, while b is an endpoint in G_b but internal in G_a. Thus a doubly-hidden adjacent pair-fiber disagreement is not an anonymous partition mismatch: it lifts to a same-residue endpoint/internal swap on H-p, giving two literal R408 component-drop comparisons after puncturing a and b. The rooted D23 payment can preserve the corresponding puncture if desired, but that payment still does not by itself currentize a repaired pair-deletion representative.

If the original pair conflict is not hidden in both directions, then at least one trimmed common-residue forest contains an actual selected state crossing the opposite support partition. Hence every neighboring pair-fiber disagreement has one of two cover-valued sources: a common-residue selected crossing, or the explicit H-p endpoint/internal-swap lift above.

### 5. Remaining global obstruction and proposed parent repair theorem

The original total-Phi descent remains unproved. The present analysis localizes what a repair theorem must actually consume.

For the pair-deletion formulation, it is enough to consume both source species above while accounting for every changed neighboring fiber: (i) a selected crossing in the common triple-deletion residue, or (ii) a lifted same-residue H-p pair with a/b endpoint-internal roles swapped. Generic payment loses the needed current representative unless its source crossing is explicitly reused.

For a potentially cleaner full-theorem route, minimize the singleton substitution potential K instead. Zero K closes H by the internal gluing proof. Every positive unit already sits in an actual cover, and after excluding direct source-rail crossings the only residue is the accepted R511 unique-transition cell. A useful parent theorem would therefore be a multi-fiber deleted-label exchange theorem: in a K-minimizing family, a source-rail crossing or an R511 bridge cell either closes H or permits simultaneous replacement of finitely many singleton-deletion covers with strictly smaller TOTAL K. This is not proved here.

Status: the gluing, swap-defect equivalence, no-interior-crossing classification, and hidden pair-fiber lift above are complete internal arguments in this DR revision. They have not undergone independent canonical review. The global K- or Phi-repair theorem remains open.
