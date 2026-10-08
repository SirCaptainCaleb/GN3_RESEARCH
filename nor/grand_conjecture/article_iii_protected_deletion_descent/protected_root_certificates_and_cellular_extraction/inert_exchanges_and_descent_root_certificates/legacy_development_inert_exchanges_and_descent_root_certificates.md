# Inert exchanges and descent root certificates — preserved pre-item development

## Development

Sources: Article II §§195,197, under the admissibility conditions of the protected replacement lemma.

At a minimum-first-phase deletion witness with p>=r, the replacement packet B is inert (0^r) or contains 10. For each adjacent 10 in B, let a_i be the coordinate dropped as that window slides and c_i the coordinate entering. Define
R(B)=sum over such descents of (e_{a_i}-e_{c_i}).
The dropped coordinates lie to the left of the replacement coordinate and the entering coordinates lie to its right. These sets are disjoint, so positive coefficients cannot cancel negative ones. Hence R(B) is nonzero exactly when B contains a descent. At an admissible extremal witness its zero locus is the inert packet.

If replacement is inert, write y=v_p. Both orders O_y (containing y and omitting x) and O_x (containing x and omitting y) have word 0^p1^q on a common codimension-two core. In a full counterexample, x blocks every insertion into O_y and y blocks every insertion into O_x; no particular scan is inferred.

Insert both coordinates consecutively, in either order, at that common gap. The first outer crossing window is inherited from O_x or O_y and has color zero. The r-1 windows containing BOTH coordinates form the pair packet. The next window containing only the second inserted coordinate is also inherited zero, after which the old one-colored suffix begins. If all pair windows were zero, the full order would be good. Thus each pair orientation has a nonempty set of one-colored pair windows, followed by a forced zero. It supplies a 10 descent.

For this pair packet the dropped coordinates (left core coordinates and the first inserted coordinate) are disjoint from the entering right-core coordinates. Its descent root sum is therefore nonzero as well. An inert first-level exchange supplies a second-level local obstruction, rather than closure.

Under reversal together with color complementation, a bridge becomes complement(reverse B); each descent swaps dropped and entering coordinates, so its root changes sign. This is an algebraic equivariance identity. It does NOT prove that the family selected by minimum first phase is a free antipodal cell complex, or that level-two certificates continuously fill the zero locus. Those remain topological obligations.
