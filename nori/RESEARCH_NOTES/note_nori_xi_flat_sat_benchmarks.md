# Flat-graded antipodal reachability SAT checks

- Stable ID: note_nori_xi_flat_sat_benchmarks
- Author: unspecified; session provenance retained
- Primary home: section:nori_matroid_generalizations_conjectures
- Labels: 
- Lifecycle: active
- Epistemic status: computational
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6430_3
- Updated session: session_nori_r6430_3
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Reproduced the flat-automaton SAT obstruction formulation via native Z3 (libz3.so.4). Dimensions 3,4,5,6 returned UNSAT; dimension 6 required about two seconds. Dimension 7 has 224 antipodal coloring variables, 16384 rooted subset variables, and 65664 clauses; a 15-second run timed out without result. Antipodal-root reduction gives 8192 rooted variables and 32832 clauses at dimension 7; symmetry-restricted trials also timed out. These are consistency checks and not independent proof certificates. No conclusion about Q7 is established.
