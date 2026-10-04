# From topological recurrence to local GN3 structure

**Summary:** Topology supplies recurrence; boundary antisymmetry converts that recurrence into local reversal, carrier, and bounded-support structure.

## Statement

A balanced root face yields directed switch-front recurrence; block separation converts recurrence into exact diagonals, a canonical giant block, cross-intersection, or front motion, where GN3-specific reversal and small-support machinery takes over.

## Body

## From balanced recurrence to local reversal structure


### Directed switch-front cycles

Let
\[
F=B_1|\cdots|B_k
\]
be an ordered-partition face whose extreme-switch roots balance at the origin. By the circulation criterion of the preceding Section, the support contains a directed cycle
\[
x_1\to x_2\to\cdots\to x_t\to x_1.
\]

An arc
\[
x\to y
\]
means that some chamber of \(F\) has first switch coordinate \(x\) and reflected last switch coordinate \(y\).

There are two qualitatively different possibilities.

1. **Exact diagonal:** some chamber has
   \[
   x=y.
   \]
2. **Winding:** every root is nonzero and the support contains a directed cycle of distinct or repeated coordinates.

The diagonal is already a strong positional statement. The winding case is where the face structure becomes useful.

### Block separation

The determining data for a first switch at coordinate \(x\) live in a bounded prefix window; the determining data for a reflected last switch at the same coordinate live in the symmetric suffix window.

Suppose an ordered-partition boundary of \(F\) separates these two determining windows. Because permutations inside different blocks are independent, one may take the block orders realizing the left witness from one chamber and the block orders realizing the right witness from another. The combined chamber then realizes both witnesses simultaneously and produces
\[
q=(x,x),
\]
an exact diagonal.

Therefore, in the no-diagonal branch, no face-block boundary may separate the two mirror determining windows for any coordinate on the directed cycle.

This is the block-separation principle. It uses only the product structure of an ordered-partition face; no hypothesis that the face has only a few blocks is needed.

### The canonical giant block

Let
\[
r=\min\{x_i:1\le i\le t\}.
\]
If the mirror corridor for \(r\) is nonempty, block separation forces that entire corridor into one block \(B\) of the ordered partition.

For every other cycle coordinate \(x_i\ge r\), its mirror corridor is nested inside the corridor for \(r\). Hence the same block \(B\) contains every nonempty mirror corridor occurring on the cycle.

Thus the winding branch has one **canonical giant block**. Different switch coordinates do not require unrelated large blocks.

If the minimum mirror corridor is empty, the switch coordinates are forced into a near-central bounded configuration. The strongest later reductions show that these near-central words fall back into compact switch windows and the existing small-support/repartition machinery. The article therefore treats the giant-block regime as the only genuinely nonlocal winding geometry.

### Cross-intersecting determining families

Inside the canonical block \(B\), let \(\mathcal L_x\) be the family of vertex sets that can occupy the left determining positions for first switch \(x\), and let \(\mathcal R_x\) be the corresponding right determining family.

If
\[
L\in\mathcal L_x,
\qquad
R\in\mathcal R_x
\]
were disjoint, the block permutation could place \(L\) and \(R\) simultaneously in their two determining windows. Together with the frozen outer blocks this would create the exact diagonal \(q=(x,x)\).

Hence
\[
\boxed{
L\cap R\ne\varnothing
\quad
\text{for every }
L\in\mathcal L_x,\ R\in\mathcal R_x.
}
\]

The topology has therefore become a cross-intersection problem inside one ordinary finite set.

From here one may extract small transversals and private witnesses. If a small set \(T\subseteq B\) is an inclusion-minimal transversal of one determining family, then for every
\[
v\in T
\]
there is an opposite witness meeting \(T\) only in \(v\). These private witnesses are useful carriers for the local GN3 arguments, but the transversal formalism is secondary; it is not another topological layer.

### Front motion

There is an even more direct consequence.

Fix a chamber realizing one of the two extreme fronts and vary the permutation of the giant block \(B\). The adjacent-transposition graph of the permutations of \(B\) is connected.

If every adjacent swap in \(B\) preserved that extreme front, then every permutation of \(B\) would preserve it. One could then choose the left and right determining sets independently, and because the two determining windows fit inside \(B\), choose them disjoint. That would create an exact diagonal, contrary to the no-diagonal assumption.

Therefore some adjacent swap in \(B\) **moves the front**.

If the swap lies close to the old front, the disturbance is confined to a bounded local window. If it lies deeper in a monochromatic region, the old and new fronts are separated by a long monochromatic corridor.

This is the strongest useful conclusion of the giant-block analysis:
\[
\boxed{
\text{exact diagonal}
\ \vee\
\text{front displacement}
\ \vee\
\text{bounded local configuration}.
}
\]

### Where GN3-specific structure enters

Up to this point the argument has used mostly antipodal geometry, switch words, and the product structure of permutation faces. The next conversion is specifically GN3.

A moved front or a long monochromatic corridor is not merely a changed bit. Because a failed triple has a forced boundary flip, local front motion produces actual tight reversal triples. Repeated front motion can therefore create:

- an exterior vertex reversing a displayed end edge;
- one carrier reversing two disjoint displayed edges;
- parallel-middle vertices;
- a Hamiltonian four- or five-support;
- a path disturbance suitable for repartition;
- strict decrease of the quadratic potential.

The reusable mechanisms are developed in
[[path_disturbance_endpoint_reversal_descent_or_an_omission_swap]],
[[endpoint_transport_and_small_support_gluing_the_remaining_lemma]],
and
[[defect_lines_and_spanning_order_compression_the_remaining_lemma]].

The conceptual division is now clean:

\[
\boxed{
\text{topology produces recurrence;}
\qquad
\text{boundary antisymmetry converts recurrence into structure.}
}
\]

This is precisely the point where GN3 may be easier than the general memory-two geodesic conjecture.

### The stronger-route alternative remains open

Nothing in this Section says that the GN3-specific conversion is the only possible closure.

A sufficiently strong antipodal memory-geodesic theorem could bypass the giant-block and local-reversal analysis entirely. If such a theorem is proved, Article VII should be rewritten to state it as the main result and the reduction through auxiliary exactification should be used directly.

Conversely, if the general theorem is false, the present Section identifies the extra hypotheses that GN3 contributes and therefore the correct place to exploit them.

The two routes are complementary research programs, not competitors.


## Metadata

- ID: topological_recurrence_to_local_gn3_structure
- Kind: section
- Version: 3
- Math version: 2
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Subsection 1 — crystallized, version 3: From balanced recurrence to local reversal structure
- Subsection 2 — HOT, version 1: Further developments
