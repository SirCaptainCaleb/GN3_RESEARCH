# Rigidity of a common-tail deletion 3-cycle — preserved pre-item development

## Development

## Rigidity of a common-tail deletion 3-cycle

Work in the directed ternary sector, so
h(c,b,a)=1-h(a,b,c).

Assume a minimum counterexample on V. Let
T=(t_1,...,t_m)
have a nonconstant one-change word with initial color sigma, and let
V\V(T)={a,b,c}.

Suppose the three deletion orders
(a,b,T), (b,c,T), (c,a,T)
are one-change. Thus their feasible-prefix graph is the directed cycle
a->b->c->a.

Then the local colors are forced as follows.

### 1. Uniform head colors
Because each displayed deletion order has the same nonconstant tail, every prefix window before the unique tail change must have color sigma. Hence
h(a,b,t_1)=h(b,c,t_1)=h(c,a,t_1)=sigma
and
h(a,t_1,t_2)=h(b,t_1,t_2)=h(c,t_1,t_2)=sigma.

### 2. The reverse residual pairs have the opposite prefix color
For example, if h(b,a,t_1)=sigma, then (b,a,T) would also be a one-change deletion order. Together with (b,c,T), the paired-deletion theorem would give a spanning one-change order, impossible in a counterexample. Therefore
h(b,a,t_1)=1-sigma.
Cyclically,
h(c,b,t_1)=h(a,c,t_1)=1-sigma.

Thus the six ordered residual pairs are completely polarized by the directed 3-cycle.

### 3. Every cyclic residual triple has color 1-sigma
Consider the full order
(a,b,c,T).
After its first window, the next windows are
h(b,c,t_1)=sigma,
h(c,t_1,t_2)=sigma,
followed by the one-change tail beginning in sigma.
If h(a,b,c)=sigma, the full order would be one-change. Hence
h(a,b,c)=1-sigma.
The same argument with the two cyclic rotations gives
h(b,c,a)=h(c,a,b)=1-sigma.
By reversal antisymmetry, the three reversed residual triples all have color sigma.

### 4. Uniform terminal extension colors
Apply minimum-counterexample endpoint blocking to each deletion order. Since its word starts in sigma and ends in 1-sigma, appending the omitted residual vertex must create a final sigma-window. Thus
h(t_{m-1},t_m,a)
=
h(t_{m-1},t_m,b)
=
h(t_{m-1},t_m,c)
=
sigma.

Similarly, prepending the omitted vertex gives exactly the cyclic residual triple constraints in part 3.

### Consequence
A common-tail directed deletion cycle in a minimum counterexample is not an arbitrary obstruction. It is a rigid three-vertex gadget attached uniformly to both ends of T:

- forward cycle pair-prefixes have color sigma;
- backward pair-prefixes have color 1-sigma;
- cyclic residual triples have color 1-sigma;
- reversed residual triples have color sigma;
- every residual vertex has the same color sigma against the first two and last two tail coordinates.

The remaining freedom is therefore concentrated at interfaces involving deeper tail coordinates, especially near the unique switch of T. Any exchange that resolves this gadget may focus on the switch neighborhood rather than the whole tail.

### Audit
The reverse-pair conclusion uses the paired-deletion theorem: two outgoing feasible arcs from one residual vertex already close the instance. No assumption is made that the common-tail cycle itself is impossible; Section 39 gives globally soluble examples realizing it.
