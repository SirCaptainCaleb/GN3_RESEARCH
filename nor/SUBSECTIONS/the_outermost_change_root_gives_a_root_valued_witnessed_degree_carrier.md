# The outermost-change root gives a root-valued witnessed-degree carrier

## Metadata

- ID: the_outermost_change_root_gives_a_root_valued_witnessed_degree_carrier
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 243
- Row version: 1
- Development version: 1
- Composition version: 2
- Composition stale: False

## Composition

Outermost-change roots give a root-valued degree carrier with proper-face witness concatenation and zero-free boundary in the stated reversal-odd construction. The topological obstruction forces a root cancellation in the carrier, but does not by itself extract a provenance-preserving physical path.

## Development

## The outermost-change root gives a simpler witnessed-degree carrier

For a full ternary order pi=(v_1,...,v_n), let p be its first change position and q its last change position whenever pi has at least two changes. Define
D(pi)=e_{v_p}-e_{v_{q+3}}.
For an order with at most one change, define D(pi)=0.

### Exact zero set

If pi has at least two changes then p<q, so v_p and v_{q+3} are distinct coordinates. Hence D(pi) is a nonzero type-A root. Therefore
D(pi)=0 iff pi is NOR-good.

### Reversal oddness

Let pi^rev=(v_n,...,v_1). Reversal complements every ternary window color and reverses the window order, so changes are preserved as a reflected set. The first change of pi^rev is the reflection of q and the last is the reflection of p. The corresponding two physical endpoints are v_{q+3} and v_p. Thus
D(pi^rev)=-D(pi).

Global color complementation leaves the change set unchanged, so it leaves D unchanged.

### Proper-face crossing

Fix a proper ordered-partition face
F=B_1|...|B_s
and choose one NOR-good order g(B_i) in each block. Let
pi_F=g(B_1)...g(B_s).

Assume the ambient instance is a counterexample, so pi_F is bad and has first and last changes p<q. The two endpoints v_p and v_{q+3} cannot lie in the same face block. If they did, the whole positional interval from p through q+3 would lie inside that contiguous block. In particular both changes p and q would be internal changes of the block order g(B_i), contradicting that g(B_i) has at most one change.

Therefore v_p lies in a strictly earlier face block than v_{q+3}.

If h_F is any block-rank functional constant on each B_i and strictly increasing from left to right, then
<h_F,D(pi_F)><0.

### Nested-face carrier property

For a flag of proper faces F_0<...<F_t, use the block-rank functional of the coarsest face in the flag. Every finer-face outermost root is weakly forward for this functional, while the root attached to the coarsest face is strictly forward. Hence every positive convex combination of the flag labels has strictly negative pairing.

Thus the piecewise-linear boundary carrier obtained by sending each face barycenter to D(pi_F) is zero-free on every boundary simplex and has the same face-normal orientation class as the existing consecutive-change carrier.

In particular the ordinary boundary-degree argument used for the consecutive-change carrier applies verbatim to D: proper-face witnesses define a zero-free nonzero-degree boundary map whose labels are single physical roots.

### Why this is useful

A forced interior zero for this carrier is a positive dependence of actual type-A roots rather than sums of macro-roots. Any support-minimal zero is therefore a directed physical root cycle.

This removes the Abel-summation layer from the topological side of Article III. The remaining obligation is realization: show that a directed cycle of outermost-change roots arising from compatible witness faces yields a legal block splice, a spanning NOR-good order, or a strict admissible witness improvement.

The outermost root also retains explicit defect provenance: its source sits at the first change and its target three positions after the last change. Thus every root spans the entire multichange region of its witness.
