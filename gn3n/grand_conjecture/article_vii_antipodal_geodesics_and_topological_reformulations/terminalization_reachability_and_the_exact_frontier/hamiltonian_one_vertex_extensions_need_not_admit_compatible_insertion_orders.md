# Hamiltonian one-vertex extensions need not admit compatible insertion orders

The universal ordered-insertion bridge is false, already for four vertices in a genuine boundary 3-tournament. Let V={0,1,2,3}, and declare exactly the following ordered triples tight:
(0,1,3), (0,2,1), (1,0,2), (1,2,3),
(1,3,0), (2,0,3), (2,1,0), (2,3,0),
(2,3,1), (3,0,1), (3,1,2), (3,2,0).
For each reversal pair (a,b,c),(c,b,a), exactly one triple occurs in this list. Thus this is a boundary tournament, with no artificial path truncation.

Put D={0,1,2} and y=3. The Hamilton orders of D are exactly (0,2,1), (1,0,2), (2,1,0). The Hamilton orders of D+y are exactly (1,2,3,0) and (2,3,0,1). Deleting 3 from these two words gives (1,2,0) and (2,0,1), respectively, both non-tight. Therefore no Hamilton order of D+y is obtained by inserting y into any Hamilton order of D.

Here is a direct check of the four-vertex list. Every Hamilton word must start with one of the twelve listed tight triples, and its fourth vertex is then determined. The only initial triples for which the resulting terminal triple is also listed are (1,2,3), completed by 0, and (2,3,0), completed by 1. The three Hamilton orders on D are read directly from the displayed triples.

Consequently support Hamiltonicity and the existential availability of two orders cannot be replaced by a coherent single-insertion witness. The gap-localization and augmentation lemma applies to actual insertion records, and a further theorem must obtain such records under the counterexample hypotheses or allow genuine rearrangement/splitting of the old path.

Scope: this example itself has a Hamiltonian path and hence a two-cover. It refutes only the universal compatibility bridge, not any conditional theorem using minimum-counterexample or odd-uniform hypotheses. It is not edge-order-induced: its triples (1,0,2), (0,2,1), (2,1,0) would require edge ranks 01<02<12<01.
