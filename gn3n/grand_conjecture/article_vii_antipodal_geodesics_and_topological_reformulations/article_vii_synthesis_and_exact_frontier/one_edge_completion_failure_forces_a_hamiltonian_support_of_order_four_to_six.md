# One-edge completion failure forces a Hamiltonian support of order four to six

## Composition

(none yet)

## Development

Retain the canonical matching-block six-set U=C union {a,b}, with C=C_+ sqcup C_- and |C_+|=|C_-|=2. By the preceding theorem Gamma(U)-{ab} is acyclic. For y in C_+ and z in C_-, the cross four-set {a,b,y,z} is non-Hamiltonian with hooks ay->yb, bz->za, ay->az, bz->by. Its matching-block edge order is therefore {ay,bz} < {ab,yz} < {az,by}. Consequently every y in C_+ and z in C_- satisfy ay->ab->az and bz->ab->by. Thus the direct predecessors of ab are L={ay:y in C_+} union {bz:z in C_-}, while its direct successors are R={az:z in C_-} union {by:y in C_+}. Every comparison between an incident L-edge and R-edge is oriented from L to R: cross-class same-side comparisons are ay->az and bz->by, while same-label mixed comparisons are ay->by for C_+ and bz->az for C_-. Hence adding ab creates no directed comparison triangle. If Gamma(U) is cyclic, choose a shortest directed cycle. It contains ab because Gamma(U)-{ab} is acyclic. By the general shortest-cycle classification it cannot be a star triangle or ordinary triangle, so its ordinary edges form a vertex-simple cycle of length m in {4,5,6}. Removing the shadow edge ab from the directed cycle leaves a directed chain of m-1 consecutive ordinary edges, hence a tight Hamilton path on the m underlying vertices. Therefore failure to complete the one-edge order forces a Hamiltonian support of order 4, 5, or 6 containing a and b. If no such completion failure occurs, the entire six-set is edge-orderable. Thus the matching-block exception has the sharp dichotomy: full edge-orderability, or an explicit Hamiltonian 4/5/6-support exposed by the first obstruction to inserting ab.
