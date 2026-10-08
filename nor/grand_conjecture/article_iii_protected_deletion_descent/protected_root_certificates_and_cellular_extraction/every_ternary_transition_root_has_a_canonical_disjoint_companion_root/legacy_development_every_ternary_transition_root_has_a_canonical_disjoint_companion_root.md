# Every ternary transition carrier has a realized disjoint companion root — preserved pre-item development

## Composition

(none yet)

## Development

## Audit correction: every ternary transition root has a realized disjoint companion relation

Work in the coboundary-flat alternating ternary sector.

Let four consecutive coordinates
(a,b,c,d)
carry a genuine transition
alpha(a,b,c)=x,qquad alpha(b,c,d)=1-x.
Its physical transition root is
rho=e_a-e_d,
oriented a->d.

Coboundary flatness gives exactly two possibilities for the off-faces.

- Flat packet:
  alpha(a,b,d)=x,
  alpha(a,c,d)=1-x.

- Fully-curved packet:
  alpha(a,b,d)=1-x,
  alpha(a,c,d)=x.

Apply both disjoint endpoint swaps and consider the actual order with local block
(b,a,d,c).
Its two local statuses are
alpha(b,a,d)=1-alpha(a,b,d),
alpha(a,d,c)=1-alpha(a,c,d).

In the flat case this word is (1-x,x); in the fully-curved case it is (x,1-x). In either case it is a genuine transition whose physical root is
e_b-e_c,
oriented b->c.

Thus every CARRIER of a transition root a->d supplies a realized disjoint companion root b->c on the same four physical coordinates.

The relation is symmetric at the carrier level: the opposite local order (b,a,d,c) has (a,b,c,d) as its double-swap mate.

### Consequence for a minimum Hamiltonian physical-root circuit

Let C be a directed physical root cycle of minimum length among a class containing all genuine transition roots under discussion, and suppose C is Hamiltonian on the ambient coordinates.

For an edge a->d of C and any realized transition carrier (a,b,c,d), the companion b->c is genuine and b,c lie on C.

If b->c is not already an edge of C, it is a directed chord. The chord plus the directed segment of C from c back to b gives a strictly shorter positive root cycle, contradiction.

Hence every realized transition carrier of every edge of a minimum Hamiltonian circuit has its companion root already among the cycle edges.

Equivalently, define the COMPANION GRAPH whose vertices are the directed edges of C, joining two cycle edges when some four-coordinate transition carrier realizes them as the two disjoint companion diagonals. Then:
- the companion graph is undirected/symmetric;
- it has no loops;
- it has no edge between adjacent physical-cycle edges, because companion roots use four distinct coordinates;
- every cycle edge that has a transition carrier has companion-graph degree at least one.

### Important audit qualification

A physical root may admit more than one transition carrier, with different middle-coordinate pairs. Therefore the companion of a root is NOT canonically unique at the root level.

Consequently the preceding theorem does NOT by itself produce:
- a fixed-point-free involution on cycle edges;
- a perfect matching;
- even cycle length.

Those stronger conclusions from the first development version are withdrawn.

### Additional orientation datum

For each individual companion incidence:
- a flat carrier reverses the 0->1 / 1->0 transition orientation between its two companion roots;
- a fully-curved carrier preserves that orientation.

This gives a signed companion graph. The safe next target is to exploit the minimum-degree/nonadjacency constraint together with these carrier signs, rather than assuming a pairing.

### Scope

No Johnson corner attainment is used. Both endpoints of every companion incidence are literal full coordinate orders obtained by the two commuting endpoint swaps of one four-coordinate packet.
