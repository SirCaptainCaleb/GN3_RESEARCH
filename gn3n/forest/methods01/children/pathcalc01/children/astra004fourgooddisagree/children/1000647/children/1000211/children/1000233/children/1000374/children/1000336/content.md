# Correction: five-core complement coupling applies only to the long sliding-window branches

## Statement

The universal statement of 783367296d15 is not justified. Its five-core complement configurations are valid only in the long sliding-window branches of the proof of 4cf010e3e5b3: namely, when every six-set is Hamiltonian, both components of the chosen deletion cover have order at least six, and the proof reaches either a noninsertable five-window or an adjacent-window side switch. The earlier branches of 4cf010e3e5b3—especially a non-Hamiltonian six-set, or a deletion component of order three through five—need not supply the claimed nested Hamiltonian five/six supports. Therefore 783367296d15 must not be cited as an unconditional theorem about every minimum counterexample.

## Body

Inspection of 4cf010e3e5b3 shows three logically different sources of nonvacuous order disagreement.

First, if some six-set U is non-Hamiltonian, astra004fourgooddisagree supplies two Hamiltonian five-deletions of U with order disagreement. These are two five-sets, not a nested five/six pair of the form asserted in 783367296d15.

Second, if every six-set is Hamiltonian but some deletion-cover component P has order between three and five, 6f72075b0b54 supplies disagreement among Hamiltonian deletions inside V(P) union {x}. Their orders are |P|, which may be three or four, so again no Hamiltonian five-core is forced.

Only in the remaining long-component sliding-window branch do the nested five/six or overlapping-six constructions used in the proof of 783367296d15 occur. Thus the construction is sound conditionally there, but the universal quantifier in 783367296d15 is invalid.
