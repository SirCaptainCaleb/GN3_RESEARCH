# One-change NOR is reachability in a two-layer flag prism

**Summary:** Keep the last r-1 coordinates as a flag state and add one bit recording whether the unique color switch has already happened. Then NOR is exactly source-to-sink reachability in a two-layer prism over the barycentric simplex.

## Statement

For any coordinate arity r, the NOR one-change problem is exactly a directed reachability problem on the memory-state flag complex with two color phases. The underlying memory states are ordered consecutive-rank flags in sd(Delta^{n-1}); adjoining the pre-switch/post-switch phase embeds the automaton in a refinement of Delta^{n-1} x [0,1]. A spanning one-change order is precisely a directed source-to-sink path in one of the two initial-color copies.

## Body


## One-switch automaton

Fix coordinate arity r and a reversal-odd label h on ordered r-tuples.

A partial coordinate order is represented by:
- its used support S;
- its ordered tail T=(v_{k-r+2},...,v_k) of the last r-1 coordinates when k>=r-1.

This is exactly an ordered consecutive-rank flag in the barycentric simplex: the successive prefix sets remembering the last r-1 added coordinates.

Fix an initial color q in {0,1}. Add a phase bit p in {0,1}:
- p=0 means the switch has not yet occurred and the currently required color is q;
- p=1 means the switch has occurred and the required color is 1-q.

When a new unused coordinate x is appended, let c=h(T,x).

The directed automaton has:
- a horizontal transition in phase 0 when c=q;
- a switch transition from phase 0 to phase 1 when c=1-q;
- a horizontal transition in phase 1 when c=1-q;
- no transition from phase 1 on a color-q window.

Before the first complete r-window exists, initialization edges are unconstrained and simply build the memory tail.

### Exactness theorem

A permutation pi has h-word with at most one change and initial run color q if and only if its successive prefix-memory states form a directed path from the empty/source state to a full-support sink in the q-automaton.

Proof: before the unique switch every consumed r-window has color q; the first opposite window uses the unique layer-changing edge; afterward every window has color 1-q. Conversely any automaton path has exactly this form.

Taking the union of the q=0 and q=1 automata gives exact equivalence with NOR.

### Geometric realization

Ignoring phase, memory states are barycenters of ordered consecutive-rank flags in sd(Delta^{n-1}), and transitions join overlapping flags inside one higher flag.

Adjoin the phase coordinate p. After a standard prism triangulation, the two horizontal copies p=0 and p=1 and the allowed layer-changing edges form a directed subcomplex of a refinement of

Delta^{n-1} x [0,1].

Thus NOR is not merely analogous to a threshold problem: the unique switch is literally the vertical coordinate of a simplex prism.

### Reversal symmetry

Reversing a full coordinate order reverses the chamber and complements every window color. On the automaton this exchanges the two initial-color copies and reverses source/sink orientation, while the used-support flag is sent by subset complementation.

Hence a counterexample produces an antipodally related pair of source-sink nonreachability problems in the flag prism.

### Connector target

If no spanning one-change order exists, let R_q be the set of states reachable from the q-source. Its directed frontier separates source from all full-support sinks in the q-prism.

This is the correct object for a Connector/Hex theorem:
- the ambient space is an honest simplex prism;
- the separator retains the r-1 memory;
- the vertical coordinate retains the one allowed switch;
- face restrictions correspond to deleting coordinates and hence to lower-dimensional NOR instances.

A minimum-counterexample proof would therefore aim to show that every proper side face has source-sink reachability while the whole prism does not. A connector theorem should force a connected separating carrier meeting side faces in a prescribed way. The remaining closure obligation is to exploit reversal symmetry and the compatibility of these facewise reachable sets to rule out such an interior separator.

### Relation to affine-threshold certificates

Choosing a switch time in a completed permutation is the discrete counterpart of choosing an affine threshold separating the signed points epsilon_i(1,t_i). The two-layer automaton retains the same threshold parameter before the permutation is completed, so unlike a chamberwise Radon certificate it is compatible with prefixes and with the simplex face structure.


## Metadata

- ID: one_change_nor_is_reachability_in_a_two_layer_flag_prism
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
