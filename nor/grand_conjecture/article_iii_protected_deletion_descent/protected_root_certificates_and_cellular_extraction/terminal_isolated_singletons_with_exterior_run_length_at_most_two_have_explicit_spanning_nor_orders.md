# Terminal isolated singletons with exterior run length at most two have explicit spanning NOR orders

## Composition

Every flat alternating full order with word 0^A 1 0^B and min(A,B)<=2 admits an explicit spanning NOR order. For B=1 an endpoint pair swap suffices. For B=2 a complete six-coordinate flat/full and holonomy classification gives a word in 0^*1^*, retaining the original ordered first pair and the entire preceding zero prefix. Full reversal gives the other endpoint. Arbitrary longer prefixes are covered.

## Development

## Every flat alternating global singleton with a short terminal run has a spanning NOR order

Let alpha be a coboundary-flat alternating ternary label. Suppose a full coordinate order has global word
0^A 1 0^B, A,B>=1.
If B<=2, an explicit surgery gives a spanning NOR-good order. By full reversal and one global color convention, the same holds if A<=2.

The ambient coordinate set and A are arbitrary. Every replacement below retains the full support and the ordered first pair of its terminal packet, so every preceding ternary window is unchanged.

### Terminal run B=1

The final five coordinates (a,b,c,d,e) have word 010. Swap the last pair, obtaining
(a,b,c,e,d).
The internal word is 0,z,1, with z=alpha(b,c,e).
Both choices of z give 0^*1^*. Every earlier window is zero and fixed.

This case uses alternation alone; the transposition c,e,d complements c,d,e. General reversal-odd ternary labels require their own transposition law.

### Terminal run B=2

The final six coordinates (a,b,c,d,e,f) have word 0100:
abc=0, bcd=1, cde=0, def=0.
All earlier windows are zero. We give a complete symbolic classification.

#### Case 1: left boundary flat

Flatness of (a,b,c,d) gives abd=0. Put u=alpha(c,e,f).

If u=1, the order
(a,b,d,c,e,f)
has word 0011:
abd=0, bdc=0, dce=1, cef=1.

If u=0, the order
(a,b,d,c,f,e)
has word 00z1:
abd=0, bdc=0, dcf=z, cfe=1.
For either z this is one-change.

#### Case 2: right boundary fully curved

For the 1->0 transition (b,c,d,e), full curvature gives bce=0.
The order
(a,b,c,e,d,f)
has word 0011:
abc=0, bce=0, ced=1, edf=1-def=1.

This covers the full/full branch and any remaining flat/full branch.

#### Case 3: left full, right flat, holonomy t=0

The residual type has
abd=1, acd=0, bce=1, bde=0.
Put t=alpha(a,b,e).

If t=0, the order
(a,b,e,c,d,f)
has word 000z:
abe=0, bec=0, ecd=0, cdf=z.
It is one-change for either z.

#### Case 4: left full, right flat, holonomy t=1

Now abe=1, bce=1, bde=0. Put
gamma=alpha(c,d,f), eta=alpha(b,e,f).

If gamma=0, use
(a,b,e,d,c,f).
Its word is 1111:
abe=1, bed=1, edc=1, dcf=1.

If gamma=1, tetrahedral parity on {c,d,e,f}, using cde=def=0, forces
alpha(c,e,f)=1.

If additionally eta=1, use
(a,b,e,f,c,d).
Its word is 1111:
abe=1, bef=1, efc=1, fcd=1.

If eta=0, use
(a,b,f,e,d,c).
Its word is z111:
abf=z, bfe=1, fed=1, edc=1.
For either z this is one-change.

### Boundary verification and conclusion

Every displayed six-coordinate order starts with the same ordered pair (a,b). The packet reaches the global right endpoint. Therefore there are zero changed reconnection windows on either exterior side: the preceding windows are literally fixed, and the right exterior is empty.

All displayed words belong to 0^*1^*. Concatenating them after the unchanged all-zero prefix yields a full spanning NOR-good order.

The four cases exhaust the flat/full choices and both mixed holonomy values. Thus every global isolated singleton with terminal run length one or two closes NOR in the flat alternating sector.

### Consequences

1. Every global isolated-singleton order in a flat alternating counterexample has both exterior runs of length at least three.
2. Every five-position carrier-zero witness of §§241-242 whose singleton is within two status ranks of either endpoint is extractable into a spanning NOR order.
3. The terminal holonomy-one full/flat residue is discharged by the exact six-coordinate orders above.
4. For the prefix-extremal singleton normalization of §250, the surviving residue has full-left/flat-right type, holonomy one, and two exterior runs each of length at least three.

The internal holonomy-one residue with longer exterior runs remains a boundary-reconnection problem; the terminal proof retains its endpoint hypothesis.
