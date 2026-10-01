# Insertion-slot interval structure

## Statement

Fix a longest tight path P=(p_1,...,p_m). For each outside vertex x, record the indices i at which x can replace or be inserted adjacent to the local window around p_i while preserving all newly created consecutive triples. Conjecture that after choosing the appropriate left/right insertion type, the feasible indices for x form an interval, or at worst the union of two intervals with forced alternating boundary signs. If true, the family of outside-vertex slot sets has a Helly-type overlap forcing either two simultaneous absorptions or a bounded endpoint obstruction that can be compressed.

## Body

Why it might matter globally:
This would turn endpoint transport into one-dimensional interval combinatorics. Overlapping slots could absorb complement vertices into P, while disjoint slot intervals would impose a rigid global ordering on the complement that may itself yield the second path. The mechanism is uniform in the order of H.

Plausible first attack:
For one outside vertex x, write the tight/non-tight signs of triples (p_i,p_{i+1},x) and (x,p_i,p_{i+1}) along P. Use only the boundary-tournament local axioms and maximality of P to forbid repeated alternation of these signs. Aim first for a no-ABAB lemma for feasible insertion types along P; then deduce interval structure and test how two outside vertices with overlapping feasible intervals can be absorbed without unchecked path reversal.