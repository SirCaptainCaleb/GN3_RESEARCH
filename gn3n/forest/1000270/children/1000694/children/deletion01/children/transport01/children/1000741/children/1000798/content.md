# Two Hamiltonian six-deletions do not force a seven-set Hamiltonian

## Statement

There exists a non-Hamiltonian seven-vertex boundary tournament with two distinct vertices whose deletions are Hamiltonian. This remains true in the edge-orderable subclass.

## Body

Use the certified edge-ordered seven-vertex witness on vertices {a,b,c,q_0,q_1,q_2,q_3} from counterfence01, with edge order

q_0q_1 < cq_2 < cq_0 < q_0q_2 < cq_3 < q_1q_3 < bq_2 < bc < cq_1 < bq_0 < aq_3 < bq_3 < bq_1 < aq_2 < q_1q_2 < aq_0 < q_0q_3 < q_2q_3 < ab < aq_1 < ac.

That certified result proves that the full seven-set has no increasing Hamilton path, hence the associated boundary tournament is non-Hamiltonian. Nevertheless deleting q_3 leaves the increasing Hamilton path

(q_0,q_2,b,c,q_1,a),

whose consecutive edge ranks are 4<7<8<9<20. Deleting q_2 leaves the increasing Hamilton path

(q_0,q_1,q_3,b,a,c),

whose consecutive edge ranks are 1<6<12<19<21. Thus q_2 and q_3 are two distinct Hamiltonian-good deletions of a non-Hamiltonian seven-set. Therefore any proposed local principle that a bad seven-set has at most one Hamiltonian six-deletion is false, and two-step trapping in the one-defect route cannot be deduced from seven-set non-Hamiltonicity alone.
