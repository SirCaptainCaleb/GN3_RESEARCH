# Brainstorm: use a switch-parameter prism and Tucker labels on full permutation chambers — preserved pre-item development


## Brainstorm: switch-parameter prism and Tucker labels on full permutation chambers

This note records two compatible topology ideas; neither is yet a proof.

### 1. Build the switch position into the domain

A NOR-good order is not merely a permutation. It is naturally a pair

(permutation pi, switch cut q)

together with a polarity s, where the target window word is

s...s,-s...-s

with the cut after q.

Therefore ordinary Sperner on the permutation complex discards one essential degree of freedom. A more natural domain is a prism/suspension over the full-support permutation complex with an interval coordinate q recording the switch threshold.

In the memory-lift formulation, for each polarity s and rank q define P_q^s as states reachable by an s-monochromatic prefix and Q_q^s as states from which a (-s)-monochromatic suffix reaches the sink. Then cut q succeeds exactly when P_q^s intersects Q_q^s. Reversal exchanges P_q^s with Q_{m-q}^s.

Thus a counterexample gives two antipodally related disjoint carriers over the switch interval. A Connector/Hex/Poincare-Miranda style theorem on this prism may be more appropriate than ordinary Sperner: the desired conclusion is literally a forced intersection of the two carriers.

Any triangulation used here should retain the full memory state, not just the support subset, to avoid the dropped-coordinate failures seen in hand-splicing arguments.

### 2. Canonical antipodal bad-chamber labels from tightest alternating triples

For a bad ternary order pi, let epsilon_i be its window signs and let T(pi) be its transition positions. Choose two consecutive transitions p<q minimizing q-p. The windows p+1,...,q form the shortest middle run between two changes.

Every middle-run window j gives a three-window obstruction epsilon_p=epsilon_{q+1}=-epsilon_j. Use the physical center coordinate of that ternary window as a label magnitude. Among all shortest packets and their middle windows, choose the least physical center coordinate in a fixed ground-set ordering.

Sign that coordinate by epsilon_j.

Reversal preserves transition gaps and the set of candidate physical center coordinates, while reversal-oddness flips the window sign. Hence this construction is designed to satisfy

lambda(pi^rev)=-lambda(pi).

This is a natural Tucker/Ky-Fan style label because it is attached to an actual full-support bad permutation and an actual local Radon certificate of at-least-two-change failure.

The next obligation is not the antipodal law but adjacency compatibility: determine what opposite labels or alternating simplices mean for adjacent full-support permutation chambers. A successful interpretation should yield either a direct local repair, a lower-complexity obstruction, or a good chamber.

### Strategic point

These modifications deliberately move away from support-only simplex labels. The topology should preserve:

- the full coordinate order;
- the memory state;
- the candidate switch position;
- and the actual three-window obstruction certificate.

Those are exactly the pieces lost in earlier failed Sperner and propagation attempts.
