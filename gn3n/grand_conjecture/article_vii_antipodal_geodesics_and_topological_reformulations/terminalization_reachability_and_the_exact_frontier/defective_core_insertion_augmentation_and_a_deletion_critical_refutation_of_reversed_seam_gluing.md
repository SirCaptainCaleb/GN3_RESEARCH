# Defective-core insertion augmentation and a deletion-critical refutation of reversed-seam gluing

## Composition

(none yet)

## Development

## Adjacent insertion augmentation does not require a Hamiltonian root-deleted core

Let sigma=(d_1,...,d_k) be ANY ordering of distinct vertices, not assumed tight. For a root z outside sigma, call a gap feasible when inserting z there gives an actual Hamiltonian word on its k+1 vertices.

Suppose distinct roots x,y have feasible gaps i,j.

If |i-j|>=2, simultaneous insertion produces a tight (k+2)-path. Every resulting consecutive triple is inherited from one of the two actual single-root words; no triple contains both roots.

If j=i+1, write b=d_{i+1}. The simultaneous word (...,x,b,y,...) is tight exactly when (x,b,y) is tight. Every other triple is inherited from a single-root witness. If both roots are feasible at both adjacent gaps, boundary reversal makes one of (...,x,b,y,...) and (...,y,b,x,...) tight, producing a (k+2)-path.

Thus the actual augmentation tests in 281 extend to root-deleted orders with defects. They require agreement of the root-deleted ORDER, but not Hamiltonicity of that order. This preserves the positive mechanism when a root deletion exposes a seam.

## Defects locate compatible root placements

Index the core triples by 1,...,k-2, with triple i equal to (d_i,d_{i+1},d_{i+2}). Insertion in an interior gap g, between d_g and d_{g+1}, replaces just the old triples g-1 and g whenever those indices exist. Endpoint insertion replaces no old triple.

Therefore every non-tight core triple must be among {g-1,g} for any feasible root gap g. A single defect j permits only gaps j and j+1. Two adjacent defects j,j+1 permit only gap j+1. Separated defects permit no single-root Hamiltonian insertion.

In particular, for a core with two adjacent defects, ALL compatible actual root extensions must use the same gap. This identifies where the separated/adjacent augmentation mechanism cannot operate; it does not assert that compatible extensions exist.

## Explicit refutation of the reversed-four-seam closure shortcut

Even full deletion-criticality plus two actual extensions using opposite orders of the same four-core does not force Hamiltonicity of their union.

Use vertices 0,...,5. Index the 60 independent variables lexicographically by (m,u,w), u<w and u,w distinct from m. Read the bits most-significant first. Bit 1 means (u,m,w) is tight and bit 0 means (w,m,u) is tight.

The 60-bit word is
110100010101101010010000011010100000010001101110001100000001,
or hexadecimal d15a906a046e301.

The following two words are tight:
W_4=(0,1,4,2,3),
W_5=(3,2,5,1,0).

Deleting 4 from W_4 gives the core order (0,1,2,3), whose two triples are BOTH non-tight. Deleting 5 from W_5 gives the reversed core order (3,2,1,0), whose two triples are both tight by boundary reversal. Thus the two roots have actual central-gap extension witnesses over mutually reversed four-core orders, and the first deletion exposes precisely the reversed four-vertex seam described in 285.

Nevertheless the six-set has NO Hamiltonian path.

Moreover every five-vertex deletion is Hamiltonian. For omitted vertices 0,...,5, respectively, the complete Hamiltonian-order counts are
1,6,6,6,5,4.
Explicit witnesses are:
H-0: (5,4,2,3,1);
H-1: (3,5,4,0,2);
H-2: (1,4,5,0,3);
H-3: (0,1,4,5,2);
H-4: (2,5,1,0,3);
H-5: (0,1,4,2,3).

Verification. The word specifies one orientation of each reversal pair, so it defines a genuine boundary tournament. All 720 six-vertex orders were checked directly and none has its four consecutive triples tight. For each deletion all 120 orders were checked, giving the counts above. Each displayed witness and the two non-tight core triples were also checked separately. The model was obtained by a fixed six-label feasibility test of this particular local gluing claim; this is not a moving small-order cutoff argument.

Scope. This example has a two-cover and is not a grand-conjecture counterexample. It also lacks the full ambient order 2r+1 of the odd residue (here r=5 and n=6). It proves that local reversed-seam information, even accompanied by Hamiltonicity of every r-subset and non-Hamiltonicity of the (r+1)-set itself, does not suffice for augmentation. Any valid ambient theorem must actually use the exterior balanced supports or other global counterexample hypotheses.

The common-core-order augmentation above remains valid. Reversal of a four-core cannot be silently treated as preserving that required order agreement.
