# A complete 2n root-rotation orbit and its antipodal reversals can all have maximal switch defect

# A full cyclic root-rotation orbit can be maximally alternating under active NORI

**Theorem (sharp no-go for rotation-only global descent).** For every \(n\ge5\), every chosen root \(x\in Q_n\), and every chosen permutation \(p=(p_1,\ldots,p_n)\) of the coordinate directions, there exists a globally valid ACTIVE NORI ordered-physical-three-face coloring \(c\) for which ALL \(2n\) cyclic root-rotations of the full geodesic \((x,p)\), and their physical antipodal reversals, have exactly \(n-3\) window-color changes (the maximum possible). Consequently no proof that compares only cyclic rotations of one full direction order and their antipodal reversals can force a grand one-switch witness.

**Definition of the actual cyclic root orbit.** Let
\[
R(x,(p_1,\ldots,p_n))=
(x\oplus e_{p_1},(p_2,\ldots,p_n,p_1)).
\]
The starting root really moves along the first edge. After \(n\) rotations, \(R^n(x,p)=(\bar x,p)\); after \(2n\), \(R^{2n}(x,p)=(x,p)\). Extend the direction list periodically \(p_{j+n}=p_j\), and let \(y_0=x\), \(y_j=y_{j-1}\oplus e_{p_j}\) for \(j=1,\ldots,2n\), so \(y_{j+n}=\bar y_j\) and \(y_{2n}=x\). Define the \(2n\) ACTUAL ordered physical face windows
\[
U_j=\big(F(y_{j-1};\{p_j,p_{j+1},p_{j+2}\}),(p_j,p_{j+1},p_{j+2})\big),
\qquad j=1,\ldots,2n
\]
with cyclic indices modulo \(2n\) for the walking vertices and modulo \(n\) for the directions. These are the windows along the closed \(2n\)-edge coordinate walk that runs through \(p\) twice. The \(n-2\) physical windows of \(R^k(x,p)\) are precisely \(U_{k+1},\ldots,U_{k+n-2}\), cyclic indices modulo \(2n\).

**Crucial independence lemma.** All \(U_1,\ldots,U_{2n}\) are distinct actual ORDERED physical faces. Moreover, NONE is the active NORI antipodal-reversal mate
\[
\tau(U_j)=\big(\bar F_j,\operatorname{reverse}(p_j,p_{j+1},p_{j+2})\big)
\]
of another \(U_k\).

*Proof.* An ordered direction triple determines \(j\) modulo \(n\), because every \(p_i\) is distinct. Thus possible repetitions among \(U_j\) occur only between \(U_j\) and \(U_{j+n}\); these are antipodal PHYSICAL faces carrying the same ordered triple, with their \(n-3\ge2\) fixed exterior coordinates complemented, so are distinct. If a cyclic forward triple at \(j\) equaled a reversed cyclic forward triple at \(k\), their middle directions would coincide: \(p_{j+1}=p_{k+1}\), giving \(j\equiv k\pmod n\). The first directions would then require \(p_j=p_{j+2}\), impossible for \(n\ge5\). Hence the cyclic collection avoids its tau-images entirely. QED.

**Construction and proof.** Prescribe \(c(U_j)=j\bmod2\) for \(j=1,\ldots,2n\), so these actual cyclic window colors alternate around a cycle of even length \(2n\). By the independence lemma the assignments are consistent, and the active NORI coloring axiom uniquely specifies the opposite colors on the disjoint mate set \(\tau\{U_j\}\). Complete all remaining face-reversal orbits arbitrarily. Every full rooted path \(R^k(x,p)\) takes a length-\((n-2)\) consecutive arc of this alternating \(2n\)-color cyclic word, and therefore has exactly \(n-3\) changes. Under physical antipodal path reversal \(\Theta\), the full root stays unchanged, the direction order is reversed, and the path's window color word becomes its reverse complemented word, which is equally alternating. QED.

**Geometry of the method limit.** Moving along \(R\) is maximally coherent: the new full path reuses \(n-3\) ACTUAL ordered face windows and replaces exactly one at the endpoint. Even this strongest possible single-window overlap on each transition can leave EVERY path in an entire rotation orbit bad. The rotation path has even period \(2n\), so binary alternation has no pentagon-style parity obstruction. The active NORI reversal involution interchanges this orbit with a different reversed-order orbit rather than identifying two windows within it. Any grand-closure mechanism based on root rotation must incorporate NONCYCLIC changes of direction order, other physical hub incidence, or a stronger cross-orbit topological invariant. This is an exact obstruction to a restricted proof method, not a counterexample to the grand conjecture.
