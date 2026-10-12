# Three-connectivity does not force a prescribed pair into one cocircuit of a cocycle

- Stable ID: note_nori_xi_three_connected_matroid_two_port_cocycle_separation
- Author: unspecified; session provenance retained
- Primary home: section:nori_matroid_generalizations_conjectures
- Labels: obstruction, binary-matroid, two-port, connectivity
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6430_3
- Updated session: session_nori_r6430_3
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Take the graphic matroid M(K_{3,3}), which is 3-connected. Write the bipartition as {a,c,d} and {x,y,z}. Let p=ax and q=cx, and let Z=delta({a,c}) be the six-edge cocycle incident to a or c. The graph obtained by deleting Z has three components: isolated a, isolated c, and the connected remainder {d,x,y,z}. Any bond contained in Z corresponds to a bond of the three-vertex quotient star with parallel edge bundles from a and c to the central component. The only cocircuits contained in Z are the three-edge stars delta(a) and delta(c), so NONE contains both p and q. Therefore even global 3-connectivity of M does not imply the cocycle-support port-cohesion condition required for two-port repair. The correct condition is that p and q lie in a common connected component of the restricted dual M*|Z, as proved in Article XI's independent-contraction subsection.
