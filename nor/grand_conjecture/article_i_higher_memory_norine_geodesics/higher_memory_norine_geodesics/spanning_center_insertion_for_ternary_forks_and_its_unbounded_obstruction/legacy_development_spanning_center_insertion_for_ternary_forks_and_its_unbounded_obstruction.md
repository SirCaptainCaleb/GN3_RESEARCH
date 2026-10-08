# Spanning center insertion for ternary forks and its unbounded obstruction — preserved pre-item development

## A spanning center-insertion exchange, and why it does not close the conjecture

Work in coordinate arity r=3, the directed translation-invariant sector of N_4, with h(c,b,a)=1-h(a,b,c).

Let a color-0 converging fork cover V\{x}, with branches P=A,u,v and Q=B,v,u. The sequences A,B are disjoint and avoid {u,v,x}. Assume |A|,|B|>=3. Write a',a for the last two vertices of A, and b',b for the last two vertices of B. The deletion order A,u,v,B^rev has word 0^{|A|}1^{|B|}.

### A full-support exchange criterion
For any permutation (t_1,t_2,t_3) of {u,v,x}, form pi=A,t_1,t_2,t_3,B^rev.
Its status word is
0^{|A|-2},
h(a',a,t_1), h(a,t_1,t_2), h(t_1,t_2,t_3), h(t_2,t_3,b), h(t_3,b,b'),
1^{|B|-2}.
Thus this spanning candidate gives a one-change order if and only if its five displayed bits are nondecreasing. The positive untouched outer runs force its switch to have direction 0 to 1.

This is an actual spanning exchange whenever the inequalities hold: it retains every vertex and the internal order of both outer branches. The formula follows by listing all windows touching the new three-vertex center. There are FIVE affected windows, including the two joins involving a' and b'; omitting those two is invalid.

### Failed universal augmentation attempt
Reversal antisymmetry and endpoint blocking do not guarantee a successful candidate among the six center permutations. The following family makes all six fail.

Prescribe the outer joins by
h(a',a,t)=0 and h(t,b,b')=1 for every t in {u,v,x}.
Prescribe
h(a,t_1,t_2)=1 for all distinct central t_1,t_2, except h(a,u,v)=0.
Prescribe
h(t_2,t_3,b)=0 for all distinct central t_2,t_3, except h(u,v,b)=1.

On the central triples prescribe
h(u,v,x)=1, h(x,u,v)=0, h(u,x,v)=0,
and set their reverses by antisymmetry:
h(x,v,u)=0, h(v,u,x)=1, h(v,x,u)=1.

The middle three bits and the full five affected bits are:

| Central order | Middle three bits | Five affected bits |
|---|---|---|
| (u,v,x) | 010 | 00101 |
| (u,x,v) | 100 | 01001 |
| (v,u,x) | 110 | 01101 |
| (v,x,u) | 110 | 01101 |
| (x,u,v) | 101 | 01011 |
| (x,v,u) | 100 | 01001 |

Every row has at least two changes. Thus all six full-support center-insertion candidates fail.

### Arbitrarily long blocked branches
Choose any disjoint A,B of lengths at least three as above. Set every consecutive triple of P=A,u,v and Q=B,v,u to color 0. This agrees with the prescribed joins and bridges:
h(a',a,u)=0, h(a,u,v)=0,
h(b',b,v)=0, h(b,v,u)=0.
The latter two equalities are the reversals of the assigned suffix bits h(v,b,b')=1 and h(u,v,b)=1.

Let F_P,F_Q be the first ordered pairs of P,Q. Set
h(x,F_P)=h(x,F_Q)=1.
The missing vertex is therefore blocked at both outer fronts.

These prescriptions are consistent with reversal antisymmetry. The original branch windows avoid x. The additional outer-join windows are either original branch windows/reverses or contain x or the opposite central endpoint in a new reversal-orbit. The middle bridges contain a or b and two central vertices; central triples use precisely {u,v,x}. The two blocking windows contain x and their respective outer front pairs. For branch lengths at least three, their reversal-orbits are distinct from the prescribed join and bridge orbits. Set all remaining reversal-orbits arbitrarily.

Consequently the construction works at arbitrarily large orders. It is a symbolic family, not a bounded-order search.

### Scope and outcome of this closure attempt
The five-bit criterion is a valid spanning construction when satisfied. The family refutes only the assertion that endpoint blocking guarantees a repair obtained by permuting the center and missing vertex while both outer branch orders remain fixed.

It does not refute the grand conjecture, does not establish a minimum counterexample, and does not exclude other spanning orders in these colorings. Additional consequences of global minimality might still force a successful candidate for a genuine minimum counterexample.

My attempted closure therefore remains incomplete. Endpoint blocking alone cannot justify this center-insertion step. Any continuation must exploit global minimality or change an outer branch, with a proved termination mechanism.
