# Two-root protected Radon zeros localize to at most six active coordinates — preserved pre-item development

## Composition

(none yet)

## Development

## Two-root protected Radon zeros localize to the union of two four-coordinate witness packets

Work in ternary arity. Consider one carrier cell indexed by an ordered partition, and suppose a positive two-term zero is supported by opposite actual window-slide roots
rho=e_a-e_d
and
-rho=e_d-e_a
coming from two chamber refinements of that same cell.

A ternary window-slide root e_a-e_d can occur only from two consecutive ternary windows on a four-coordinate packet
(a,b,c,d),
with the certified actual-color descent
h(a,b,c)=1,
h(b,c,d)=0.

Likewise the opposite root is witnessed on a four-coordinate packet
(d,b',c',a)
in the second chamber, again with a 10 descent.

### 1. All irrelevant tied coordinates can be frozen

Because both chamber states refine the same ordered partition and the relative order of a,d reverses, a and d lie in one common tied block B.

In the first witness chamber, a and d are exactly three positions apart. Hence the only coordinates of B lying between them are the two actual middle coordinates b,c of the certificate packet. Every other coordinate of B lies wholly before a or wholly after d.

Adjacent swaps among coordinates outside the interval [a,b,c,d] do not change either certified ternary window. Therefore all other tied coordinates can be reordered to any fixed canonical outside order while preserving the exact 10 certificate and its physical root rho.

The same statement holds for the opposite packet (d,b',c',a).

Thus the large tied block itself is not the base compatibility difficulty. After freezing all irrelevant coordinates, the two certificates live on
S={a,d,b,c,b',c'},
with |S|<=6,
and every ambient coordinate outside S has fixed protected order.

### 2. The base persistence problem has only three support sizes

The union support is:

- four coordinates if {b,c}={b',c'};
- five coordinates if the two middle pairs share exactly one coordinate;
- six coordinates if the middle pairs are disjoint.

Therefore every two-root zero in one ternary carrier cell reduces to a relative Coxeter problem on at most six active coordinates, with the outside order frozen.

This is not a small-order cutoff on the NOR instance: the ambient coordinate set is arbitrary. It is a bounded-support localization of one carrier-cell compatibility event.

### 3. Relation to the existing A3 extraction

In the four-coordinate case both opposite roots lie in one exact A3 block. The already-developed honest-lifted A3/two-term machinery is therefore the correct extraction module, subject to its audited provenance hypotheses.

The genuinely new base cases are only:

- a five-coordinate overlap, where the two four-packets share one middle coordinate;
- an exact six-coordinate overlap, where their middle pairs are disjoint.

### 4. Relation to the all-descent localization

The distance-lifted all-descent carrier independently shows that an essential averaged ternary zero cannot be supported over a Coxeter face all of whose blocks have size at most five.

The present result explains why six coordinates repeatedly appear as the first unresolved scale: even the smallest common-cell opposite-root cancellation that escapes the A3 overlap can be normalized to at most six active coordinates.

One should not identify the two carrier maps without an additional dictionary theorem. The valid conclusion is structural: both routes isolate the six-coordinate scale for the first genuinely new compatibility phenomenon.

### Closure target

To solve the two-root base case it is enough to prove one relative theorem with frozen exterior order:

> Given two chamber refinements on at most six active coordinates carrying opposite ternary 10 slide roots e_a-e_d and e_d-e_a inside one ordered-partition cell, either there is a compatible adjacent-swap/switch repair between them or one of the two witnesses admits a strict protected improvement.

No arbitrary tied-block refinement theorem is needed beyond this bounded packet.
