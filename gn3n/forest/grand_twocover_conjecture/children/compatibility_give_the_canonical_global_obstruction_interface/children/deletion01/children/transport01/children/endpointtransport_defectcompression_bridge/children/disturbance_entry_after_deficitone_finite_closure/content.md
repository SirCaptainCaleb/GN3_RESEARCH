# Disturbance entry after deficit-one finite closure

## Statement


Let H be a minimum counterexample. Suppose the current deletion-cover or trapped-three-cover machinery produces one of the certified standard disturbance witnesses: support crossing, order disagreement, a reversed inherited edge or reversing tight triple, a bounded Hamiltonian four- or five-support with non-Hamiltonian two-coverable complement, a leave-and-return excursion, crossing multiplicity, or one of the bounded local defect-compression configurations. Prove that at least one of the following follows:

(1) H has a spanning two-cover, equivalently a spanning ordering of defect span at most two;

(2) the disturbance can be transported to a displayed component-end reversal to which the certified endpoint-reversal calculus applies; or

(3) for some globally longest tight path A there is an A-order-preserving tight comparison path C of order |A|-1 to which the certified deficit-one corridor closure applies.

This is an entry theorem, not a termination theorem: once outcome (3) is reached, the binary-balance machinery gives finite descent to bounded closure inputs.


## Body


The theorem-scale gap has narrowed after certification of the deficit-one corridor closure. Earlier formulations of endpoint transport had to prove both (a) entry into a controlled transport regime and (b) well-founded termination inside that regime. The second obligation is now available whenever one reaches an A-order-preserving comparison path of deficit one against a globally longest path.

Several certified partial consumers delimit the remaining entry problem.

- 883bd2af7e73 transports a complementary path greedily whenever an endpoint label can be placed at the matching end of a Hamilton order, and produces a literal reversed component-end edge at the first failure.
- ac7bd525291b consumes such a displayed endpoint reversal into a two-cover, strict quadratic descent, or a neutral singleton transfer.
- ed2d3ae845f3 compresses a direct mixed-support crossing to reciprocal support crossing, bounded reversal data, a Hamiltonian five-support, direct closure/descent, or a neutral singleton transfer.
- b18d4f6c729a shows that reciprocal unique support crossing has only a singleton-transfer residue.
- 86502fe2225c independently reconstructs finite closure of every unbounded A-order-preserving deficit-one corridor.

What remains unsupported is the conversion from the generic disturbance menu to one of these controlled entry states. Ordinary order disagreement alone does not suffice: pathcalc01 produces a reversed edge, reversing triple, or tight cycle, but does not straighten an arbitrary alternative Hamilton order into a one-vertex-deficit order-preserving comparison. Likewise, a Hamiltonian four/five-support with a two-coverable complement does not by itself place a complementary endpoint at the required end of a Hamilton order.

Thus future disturbance-consumption work can focus on endpointization or deficit-one entry; recurrence/termination inside the deficit-one corridor is no longer part of the missing theorem.
