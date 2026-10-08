# A directed cycle of compatible deletion prefixes defeats fixed-tail completion — preserved pre-item development

## Development

## A common tail can support every residual deletion but no full prefix

Work at coordinate arity r=3, the directed translation-invariant sector of N_4. The following family tests the attempt in §38 to obtain a spanning order from good deletion orders sharing a tail.

### Proposition
For every m>=4 there is a reversal-antisymmetric ternary coloring on
V={a,b,c,t_1,...,t_m}
such that:
1. T=(t_1,...,t_m) has word 0 1^{m-3};
2. each deletion of a,b,c has a one-change order consisting of the other two residual vertices followed by T;
3. no order consisting of all three residual vertices followed by the unchanged tail T is one-change;
4. the full coloring nevertheless has an explicitly prescribed one-change spanning order.

### Construction
Orient the three residual pairs cyclically:
a->b, b->c, c->a.
Prescribe
h(z,t_1,t_2)=0 for z in {a,b,c},
and, for distinct s,t in {a,b,c},
h(s,t,t_1)=0 iff s->t.
On the residual triples prescribe
h(a,b,c)=h(b,c,a)=h(c,a,b)=1,
with the three reversed triples colored 0.
Prescribe the consecutive tail windows by
h(t_1,t_2,t_3)=0,
h(t_i,t_{i+1},t_{i+2})=1 for 2<=i<=m-2.
Also prescribe
h(b,c,t_2)=1, h(c,t_2,t_3)=1.
In every case assign the reverse tuple the complementary color. Complete all remaining reversal-orbits arbitrarily.

These assignments are consistent. Tail windows contain only tail vertices. The one-residual-vertex windows initially use t_1,t_2; the extra window with one residual vertex uses t_2,t_3. The two-residual-vertex windows initially use t_1; the extra such window uses t_2. The residual triples use only a,b,c. Thus different categories do not prescribe conflicting reversal-orbits, and the three residual reversals are explicitly complementary.

### Good residual deletions
The three orders
(a,b,T), (b,c,T), (c,a,T)
have word
0^3 1^{m-3}.
They omit c,a,b respectively. The two added prefix windows are 0 by the cyclic pair rule and the terminal rule h(z,t_1,t_2)=0. The remaining word is the word of T.

### Every full prefix fails
Consider an order (s,t,z,T), where (s,t,z) permutes a,b,c. Because T already has its sole change from 0 to 1, a one-change full order would require every preceding window to be 0.

If (s,t,z) is one of (a,b,c),(b,c,a),(c,a,b), its first color is 1, its second color h(t,z,t_1) is 0, and its third color h(z,t_1,t_2) is 0. Its word is
1,0,0,0,1^{m-3},
which has two changes.

For one of the three reversed residual orders, its first color is 0 and its second color is 1, since its final pair opposes the cyclic orientation. Its word is
0,1,0,0,1^{m-3},
which has three changes.

Thus all six full prefixes fail. The feasible predecessor graph of §38 is precisely the directed cycle a->b->c->a: every residual deletion is supported and every vertex has outdegree one, so its bound is attained.

### A full spanning order succeeds after changing the tail
Take
Pi=(t_1,a,b,c,t_2,t_3,...,t_m).
The first four colors are
h(t_1,a,b)=0,
h(a,b,c)=1,
h(b,c,t_2)=1,
h(c,t_2,t_3)=1.
The first equality follows from h(b,a,t_1)=1 and reversal antisymmetry. All remaining windows begin at t_2 or later in the tail and have color 1. Therefore Pi has word
0 1^m.
This is a spanning one-change order.

### What this rules out
Even a synchronized family of good deletion orders for every residual vertex does not force the paired-prefix collision in §38. A fixed-tail exchange can cycle in a globally soluble instance. This is an arbitrarily long symbolic family, rather than a small-order cutoff.

The family does not refute the grand conjecture and is not a minimum counterexample. Its purpose is to localize the failure of my attempted closure mechanism: the common tail must be allowed to change, or a second construction must resolve a directed cycle of feasible prefixes.

The successful spanning order demonstrates one possible escape from this obstruction: move the first tail vertex to the front. No universal claim is made that this escape works in every coloring.
