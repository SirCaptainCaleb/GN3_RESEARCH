# Audit: unrestricted realized-root circuit minimization is vacuous under reversal — preserved pre-item development

## Composition

(none yet)

## Development

## Audit: unrestricted realized-root minimization collapses to antipodal 2-cycles

This corrects the strategic interpretation of the preceding shortest-Hamiltonian realized-transition-circuit subsection.

Let (mathcal R) be the unrestricted graph of all genuine ternary transition roots realized by full coordinate orders. Then (mathcal R) is automatically reversal-closed.

Indeed, if
[
(a,b,c,d)
]
has transition word (x,1-x) and root
[
a	o d,
]
then the reversed order
[
(d,c,b,a)
]
has transition word
[
x,1-x
]
again (the two ternary statuses reverse order and each complements), and its physical root is
[
d	o a.
]

Hence every edge of (mathcal R) belongs to a directed 2-cycle
[
a	o d	o a.
]

Therefore minimizing positive circuits in the unrestricted realized-transition graph is useless for the Article III extraction problem. The shortest circuits are the antipodal reversal pairs already known to cancel formally, and they need not lie in one compatible carrier/hemisphere.

### What remains valid

The local algebra in the preceding subsections is unaffected:

- a fully-curved transition realizes the complete (K_{2,2}) family
  [
  a	o c, a	o d, b	o c, b	o d
  ]
  at one central Johnson cut;
- the disjoint companion root of a transition carrier is genuine;
- these rank-two cells are exact local structure.

What must **not** be inferred is that one may minimize cycles after freely adjoining every realized root. Doing so forgets the compatibility/provenance condition that distinguishes a meaningful positive carrier relation from the vacuous root-plus-antipode pair.

### Correct circuit target

Circuit minimization must remain inside a class carrying enough common data to exclude the reversal mate automatically—for example:

- one compatible protected carrier/hemisphere;
- a coherent side-lifted root complex;
- or a cellular selection in which all roots are simultaneously realized with the same target/provenance constraints.

Within such a compatible class, the (K_{2,2}) square can still provide genuine chord or square surgery. But closure under a side root must be proved **inside that class**, not obtained by passing to all full orders.

Thus the useful content of the new (K_{2,2}) theorem is local rank-two coherence, not unrestricted graph-theoretic circuit shortening. The remaining global problem is exactly to glue those canonical local squares while retaining the compatibility data that prevents antipodal 2-cycle collapse.
