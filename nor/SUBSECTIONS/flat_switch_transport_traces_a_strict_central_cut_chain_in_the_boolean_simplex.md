# Flat switch transport traces a strict central-cut chain in the Boolean simplex

## Metadata

- ID: flat_switch_transport_traces_a_strict_central_cut_chain_in_the_boolean_simplex
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 82
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

Every rightward flat endpoint transport moves the canonical central cut strictly upward by two or three coordinates; leftward transport is the reverse. Hence a one-sided transport orbit is an honest strict Boolean-subset flag, i.e. a simplex in the barycentric subdivision. Each flag vertex carries both a legitimate inside Sperner label and a same-rank terminal-root chord. This supplies provenance-valid simplicial traces for a future fixed-point carrier, but not labels on every Boolean face.

## Development

## Flat switch transport traces a strict central-cut chain in the Boolean simplex

Work in the alternating ternary sector with the corrected endpoint-repair law. Let a transition occur at consecutive window indices i,i+1 in a coordinate order

(...,a,b,c,d,q,r,s,...),

where a,b,c,d occupy positions i,i+1,i+2,i+3.

Associate to this transition its canonical central cut

C_i={coordinates in positions 1,...,i+1},

i.e. the prefix cut between b and c. The transition root is e_a-e_d and crosses this cut.

Suppose a rightward flat endpoint repair swaps c,d. The repaired order is

(...,a,b,d,c,q,r,s,...).

By the corrected transport theorem, if the repair does not reduce variation, the surviving transported transition occurs at index

j in {i+2,i+3}.

### Central-cut evolution

If j=i+2, the new central cut is the prefix through position i+3 of the repaired order. Hence

C_j=C_i union {c,d}.

If j=i+3, the new central cut is the prefix through position i+4, hence

C_j=C_i union {c,d,q}.

Therefore in either transport case

C_i proper-subset C_j,

and the rank increases by exactly two or three.

The leftward repair is the reversed statement: its central cut strictly decreases by deleting two or three coordinates.

### Corollary: a one-sided combing trajectory is a simplex flag

Repeated rightward flat transport gives a strict chain

C_0 proper-subset C_1 proper-subset ... proper-subset C_t

of physical coordinate subsets. Repeated leftward transport gives the reverse kind of chain.

Such chains are precisely simplices in the barycentric subdivision of the coordinate simplex / nonempty-subset Boolean complex. Thus the audited switch-transport dynamics already carries a natural Sperner-ready simplicial trace; no auxiliary discretization of the transport history is required.

At each chain vertex C_j, the current transition root e_{a_j}-e_{d_j} crosses C_j and therefore supplies:
- an inside endpoint a_j in C_j;
- an outside endpoint d_j outside C_j;
- an adjacent same-rank cut C_j'=(C_j-{a_j}) union {d_j}.

So the transport flag carries simultaneously a legal ordinary Sperner label a_j in C_j and a Johnson edge based at C_j.

### Scope

This theorem does not define such labels on every subset of V and therefore is not by itself a Sperner proof. Its role is narrower: any refined fixed-point/Sperner carrier built from actual transport states may regard each one-sided repair orbit as an honest barycentric simplex, with the central-cut labels and root chords retaining exact physical provenance.
