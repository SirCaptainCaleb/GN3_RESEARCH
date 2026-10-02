# Proof rehearsal II — quadratic potential and minimal three-cover reconfiguration

## Statement

Near-publication rehearsal of the quadratic-potential route. A deletion-generated trapped three-cover is minimized for Phi=sum |P_i|^2; pairwise minimality then converts every failed balancing move into a finite order/support disturbance. Equitable profiles are the absolute Phi floor. In the strongest pending unique-small branch, same-end neutrality reduces to a positioned endpoint reversal, doubled reverse barrier, or a classified common-core six-shell. The first unsupported implication is global consumption of these positioned bounded structures into a spanning two-cover or defect span at most two.

## Body


# Quadratic potential and minimal three-cover reconfiguration

## 1. The proposed proof

Assume that the grand two-cover conjecture is false and let H be a counterexample of minimum order. The certified minimum-counterexample calculus gives pc(H)=3 and, for every vertex x, an exact two-path cover

    H-x = P | Q.

Adjoin x as a singleton. This gives the spanning three-cover

    C_0 = P | Q | {x}.

Consider the graph whose vertices are spanning three-path covers of H and whose edges are legal pairwise repartitions: one replaces two displayed paths by another two-path cover of their union, leaving the third path fixed. Since a reachable two-component state would itself be a spanning two-cover of H, the connected component containing C_0 is trapped.

On a three-cover C=P_1|P_2|P_3 define

    Phi(C) = |P_1|^2 + |P_2|^2 + |P_3|^2.

Choose C in the trapped component of C_0 with minimum Phi. The quadratic route attempts to derive a contradiction from the extremality of C.

The role of Phi is normalization rather than final closure. Its usefulness is that an attempted balancing repartition has only two outcomes: it strictly decreases Phi, contradicting minimality, or its failure forces ordered geometric structure. The existing theory has pushed this dichotomy very far. What remains is to consume the resulting structure globally.

All results below are certified unless explicitly marked **pending**.

## 2. Pairwise extremality at a Phi-minimum

Let C=P_1|P_2|P_3 be Phi-minimal in its trapped component. The certified pairwise-minimality theorem (threecoverquadraticmin01) states that for every pair i != j and every exact two-cover R|S of H[V(P_i) union V(P_j)],

    ||R|-|S|| >= ||P_i|-|P_j||.

Indeed, replacing P_i|P_j by R|S changes only the two corresponding square terms of Phi. Among two positive integers of fixed sum, the sum of squares decreases exactly when their difference decreases. Hence a more balanced two-cover of any displayed pair would give a legal strict Phi-descent inside the same component.

Thus one Phi-minimum simultaneously solves three minimum-imbalance problems. This is the common mechanism behind the many historical size-gap, small-side, endpoint-transfer, four-side, and five-side lemmas: every failed attempt to balance a pair must explain why the pair-union refuses a more equitable two-cover.

The deletion-generated component is not initially at such a minimum. Certified theorem 1000112 supplies explicit strict descent from the singleton lift into a canonical bounded three-side state, and the large-order transport theorems continue the descent. For the present rehearsal we may therefore begin at a componentwise Phi-minimum without losing the deletion ancestry of the route.

## 3. The terminal quadratic theorem

The main certified compression theorem is 1000633. In the present language it says that a trapped Phi-minimum in a minimum counterexample cannot be a structureless balancing obstruction. It exposes at least one member of a finite theorem-facing menu:

- a proper Hamiltonian four- or five-vertex support whose complement has path-cover number two;
- an explicit cross triple or bounded interval connector between displayed supports;
- relative-order disagreement between overlapping Hamiltonian paths;
- an inherited displayed-path edge whose endpoints are separated by a comparison cover;
- a leave-and-return excursion through another displayed core;
- crossing multiplicity at least three;
- a bounded local defect-compression obstruction;
- or a reversed join.

The proof of this theorem is the repeated use of pairwise extremality. One chooses a displayed pair whose sizes or endpoint positions permit a potentially improving repartition. If the repartition exists, Phi falls. If it does not, the missing tight triples, inherited path edges, or forced comparison-cover crossings determine one of the listed configurations. The extensive profile analysis has therefore already been compressed into a single principle:

    quadratic extremality
    => strict descent or positioned order/support structure.

At a Phi-minimum the first alternative is impossible, so the structure must occur.

This theorem is the correct stopping point for generic producer arguments. Re-deriving another crossing, reversal, or small Hamiltonian window is useful only if the argument preserves additional correlations not present in the generic output, such as a common reversed edge, a common endpoint, a shared deletion label, a common core, or same-component reachability.

## 4. Why the equitable profiles are the decisive plateau

The certified arithmetic theorem 1000268 states that if the three path orders differ by at most one, then the multiset of sizes is one of

    {r,r,r},
    {r+1,r,r},
    {r+1,r+1,r},

and Phi is the absolute minimum among all positive three-part size profiles with the same total order.

Consequently no strict Phi-descent is possible from an equitable three-cover while three nonempty components remain. Any proof that reaches this regime must switch from size to order, support, endpoint placement, or deletion provenance.

The three equitable profiles are no longer unclassified.

### 4.1 The all-equal profile

For {r,r,r}, certified theorem 1000292 probes two endpoint deletions of one displayed path. It forces one of the following:

- a deletion cover with several cross-support edges;
- a paired noninsertion obstruction;
- explicit inherited-order disagreement.

Thus the all-equal plateau already reaches the standard disturbance interface. The missing step is not another classification of sparse endpoint covers; it is to convert one of these disturbances into a global two-cover or defect compression.

### 4.2 The unique-large profile

For {r+1,r,r}, certified terminal theory, in particular 1000472 and 1000633, again forces one of the standard transport disturbances. The hard donor-endpoint residue already contains a bounded reverse cross triple. Thus the unique-large profile does not require a separate proof architecture.

### 4.3 The unique-small profile

The profile {r+1,r+1,r} is the one in which the strongest current route retains substantially more information than the generic 1000633 output.

The certified base theorem unique_small_transport_recomp02 gives three disjoint order-r core paths A,B,C and, in the witness-free residue, two exterior labels x,y that extend the same end of every core. For every exact two-cover of H-{x,y}, one obtains one of:

- order disagreement with a core;
- at least three cross-core ordinary edges;
- an inherited core edge split between the two residual paths;
- leave-and-return geometry through another core.

Thus even the neutral unique-small plateau is not order/support neutral.

The strongest continuation is pending audit. It can be organized as one finite argument.

First, same-end extension forces synchronized endpoint reversal. Pending theorems same_end_extenders_initial_reversal01, same_end_extenders_double_reversal01, and same_end_extenders_four_endpoint_reversal01 show that the universal same-end residue produces reverse structure at all four relevant residual endpoints unless an earlier order disagreement has already appeared.

Second, consider an exact residual two-cover R|S of H-{x,y}. Build the 2-by-2 attachment graph between {x,y} and {R,S}. A perfect matching would immediately restore x and y to different residual paths and give a spanning two-cover. Hence Hall's theorem leaves only two possibilities (pending same_end_extenders_hall_completion01):

1. one residual path is unattached by both extenders, so x and y reverse one common endpoint edge; or
2. one extender is blocked from both residual paths while the other attaches to both, giving two exact covers of the same deletion that differ by transferring one label between the two supports.

The first case admits a useful synchronization argument. Suppose two labels reverse the same displayed edge. For each reversing triple, consider the graph of bad two-label extensions. The relevant bad-extension graphs are triangle-free. If no exterior pair Hamiltonized both reversing triples, then on six common exterior vertices the edges of K_6 could be colored according to which bad graph contains them, with neither color containing a triangle. This contradicts R(3,3)=6. Therefore two common-edge reversals force two Hamiltonian five-sets sharing a four-core (pending shared_edge_double_reversal_sixpackage01).

The resulting six-vertex shell is also classified, pending audit (commoncore_fivepair_sixshell_normal01). If K+p and K+q are Hamiltonian five-sets with common four-core K, then their union U has one of three forms:

- U is Hamiltonian, in which case its path-cover-two complement yields a full two-label pc2 square;
- U is non-Hamiltonian but two good deletion labels are adjacent, giving overlapping Hamiltonian four/five-windows;
- U is non-Hamiltonian and the good-deletion graph is a matching, yielding the canonical oriented matching-block six-shell with its fixed 2+2 orientation split and complete cross-hook rectangle.

In the Hall-transfer case, certified singleton_transfer_endpointization01 says that opposite endpoint realizations of the transferred label immediately yield a displayed component-end reversal. If both realizations remain coherently on the same end, pending blocked_extender_coherent_sameend_escape01 reduces the configuration to a proper Hamiltonian five-support with pc2 complement, a doubled reverse-end barrier, or again the common-core six-shell.

Combining these statements gives the pending theorem unique_small_bounded_endgame01:

**Pending unique-small endgame.**  
After exporting the standard Hamiltonian five/six-window outputs, a Phi-minimal state of profile {r+1,r+1,r} reduces to either a positioned component-end reversal or a doubled reverse barrier.

The doubled barrier is genuine residue. Certified theorem 1000753 shows that it propagates along a displayed path unless a four-vertex connector opens, but does not by itself imply absorption.

## 5. Non-equitable states and the global-minimum variant

For the ordinary componentwise route, non-equitable profiles are already subsumed by the terminal theorem 1000633. A pair with a size gap at least two cannot simply be repartitioned more evenly, so the failed balancing move produces one of the canonical disturbances.

There is a stronger optional variant in which C is globally Phi-minimal among all spanning three-covers. The certified theorem global_sizegap_maximin_bypass01 then shows, outside the endpoint-square branch, that a largest-second size gap at least two collapses to one of the exact profiles

    (c+2,c,c) or (c+3,c,c),

with maximin parameter c, together with a tight path whose complement is non-Hamiltonian of order at most 2c. This arithmetic is useful only if a later consumer exploits it; otherwise the generic terminal theorem is the cleaner interface.

Small sides are likewise no longer a separate frontier. Certified theorem 1000921 says that for n>=18 a globally Phi-minimal three-cover has minimum side at least six unless order disagreement is already present, and certified theorem 1000323 says that a trapped local 4|5|a minimum with a>=7 already forces order disagreement. The old four-side and five-side trees are therefore supporting lemmas, not independent proof branches.

## 6. The closure interface

The certified defect-span theorem 1000694 provides the clean final language. H has a spanning two-cover if and only if some spanning ordering has defect span at most two. A deletion cover gives the canonical width-three state.

The quadratic route has now produced one of the following, with substantial positional information:

- relative-order disagreement;
- a cross-support edge or bounded connector;
- an inherited-edge split or leave-and-return configuration;
- a Hamiltonian 4/5/6 support with pc2 complement;
- a positioned component-end reversal;
- a doubled reverse barrier;
- a full pc2 square, overlap shell, or oriented matching-block six-shell.

What is not proved is that every such output can be inserted into the canonical deletion join so as to eliminate one global defect.

The desired theorem is therefore:

**Canonical disturbance compression lemma (open).**  
Let C be a Phi-minimal three-cover in a deletion-generated trapped component of a minimum counterexample. If C exposes any canonical terminal disturbance from 1000633, or any of the stronger synchronized unique-small outputs above, then H has a spanning two-cover; equivalently, H has a spanning ordering of defect span at most two.

This is the first unsupported implication of the route.

A weaker theorem consuming only one synchronized subfamily would still be real progress: for example, a common-edge double reversal, a same-deletion transfer fork, an endpoint-aligned common-core six-shell, or a doubled barrier with its deletion provenance retained.

## 7. Mathematical obstructions that delimit the route

Three facts prevent the most obvious shortcuts.

First, pure pair-union balancing is too strong. The conjectural statement that every imbalanced two-coverable pair-union admits a more balanced two-cover is, by certified theorem 1000079, equivalent to the global balanced-refinement problem for every already two-coverable boundary tournament. A successful quadratic argument must exploit the third component or deletion/reachability data; it cannot be purely internal to one pair-union.

Second, Phi itself cannot close an equitable plateau. The arithmetic minimum in 1000268 makes strict size descent impossible there. Any secondary descent must involve order, support, endpoint phase, or provenance.

Third, local reversal and Hamiltonicity are not absorption. Existing certified counterexamples show that same-end extenders need not concatenate and that endpoint hooks need not Hamiltonize the enlarged support. The pending unique-small theory is useful precisely because it adds common-edge, common-core, Hall, and same-deletion synchronization before asking for a global splice.

## 8. Exact stopping point

The proof through quadratic normalization and disturbance production is complete in the certified core, with the strongest unique-small reduction pending audit.

The live proof stops at

    synchronized bounded disturbance
    => spanning ordering of defect span at most two.

In the narrow unique-small barrier branch it stops at

    doubled reverse barrier + deletion/plateau provenance
    => defect compression or legal merge.

No general theorem presently justifies either arrow.

## 9. Research handoff

The strongest viable next target is not another quadratic profile lemma. It is a context-sensitive consumer for a **positioned bounded disturbance**. The most information-rich test cases are the common-core six-shell, the same-deletion transfer fork, and the doubled reverse barrier, because each remembers enough provenance to plausibly interact with the canonical width-three join.

The principal route not to retry without a new ingredient is generic descent or witness production. Pairwise imbalance has already been normalized, small-side profiles have already been compressed, and the equitable regimes already expose disturbance. The remaining mathematics lies in the second half of the route:

    size extremality -> synchronized order/support rigidity -> global absorption.

The first arrow is mature. The second is the frontier.
