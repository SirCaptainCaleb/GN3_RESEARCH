# The synchronized order-disagreement branch is a fixed-complement Hamiltonian-deletion family

## Statement

In branch (B) of astra002odduniform05, after passing to the synchronized same-side subfamily S', there is a set X of order k+1 and a fixed Hamiltonian k-set Q such that H[X] is non-Hamiltonian, H[X-{x}] is Hamiltonian for every x in D={d} union S', and for each x in D the chosen balanced deletion cover F_x has support partition (X-{x}) | Q. Moreover |D|>=1+ceil(ceil(k/2)/2). Thus a hypothetical odd minimum balanced-cover failure either has a linear family of support-incompatible deletion states against one anchor, or contains a non-Hamiltonian half-plus-one support with linearly many Hamiltonian deletions synchronized against one fixed complementary Hamilton path.

## Body

Assume branch (B) of astra002odduniform05. Write the anchor balanced deletion cover as

F_d=P|Q,

with |P|=|Q|=k.

That theorem gives a subfamily S' of labels all lying on one anchor side; after interchanging P,Q if necessary, assume S' subseteq V(P). For every t in S',

F_t has support partition
((P-{t}) union {d}) | Q.

Put

X=P union {d}.

Then |X|=k+1 and, for every t in S',

X-{t}=(P-{t}) union {d}

is Hamiltonian because it is a component support of F_t. Also

X-{d}=P

is Hamiltonian because it is the anchor component of F_d. Hence every deletion label in

D={d} union S'

is a Hamiltonian deletion of H[X].

The opposite support Q is the same Hamiltonian k-set in every chosen cover F_x, x in D.

Finally H[X] itself cannot be Hamiltonian. If it were, a Hamilton path on X together with the fixed Hamilton path on Q would give a balanced spanning cover of H with component orders k+1 and k, contradicting that H is a counterexample to Astra-002.

The size lower bound is exactly the two pigeonhole bounds from astra002odduniform05:

|S'| >= ceil(|S|/2)
      >= ceil(ceil(k/2)/2),

so

|D| >= 1+ceil(ceil(k/2)/2).

No fixed-order analysis is used.