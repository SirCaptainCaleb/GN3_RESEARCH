# The universal hard-reversal cross family is a complete endpoint pair-extension grid

## Statement

Continue the maximal unresolved endpoint-reversal setting of adecd58bef3d in the branch where the bounded four-vertex frontier and the direct middle-tight Hamiltonian window are absent. Thus P=(p_0,...,p_m) is a proper tight path and every y outside P satisfies
(p_1,p_0,y), (p_m,y,p_0), and (y,p_m,p_{m-1}) tight.

Then for every two distinct outside vertices y,z, the four-set
{p_0,p_m,y,z}
is Hamiltonian. More precisely, exactly one of (y,p_m,z) and (z,p_m,y) is tight, and accordingly one of
(y,p_m,z,p_0), (z,p_m,y,p_0)
is a tight Hamilton path.

Consequently, if K=H-V(P) and G=H-{p_0,p_m}, then:
(1) K has order at least four;
(2) for every pair y,z in K, H[{p_0,p_m,y,z}] is Hamiltonian and G-{y,z} is non-Hamiltonian with path-cover number two;
(3) G itself and G-y for every y in K are also non-Hamiltonian with path-cover number two.

Thus the unresolved endpoint reversal produces a complete pair-extension graph over the endpoint core {p_0,p_m}, together with radius-two path-cover-two stability on the corresponding labels in G.

## Body

Fix distinct y,z outside V(P). The hard-residue hypothesis gives
(p_m,y,p_0) and (p_m,z,p_0)
tight.

Apply boundary antisymmetry to the three-set {y,p_m,z}. Exactly one of the reversal mates
(y,p_m,z) and (z,p_m,y)
is tight.

If (y,p_m,z) is tight, then
(y,p_m,z,p_0)
is a tight four-vertex path: its two consecutive triples are (y,p_m,z) and (p_m,z,p_0). If instead (z,p_m,y) is tight, then
(z,p_m,y,p_0)
is a tight four-vertex path, using (p_m,y,p_0). Hence {p_0,p_m,y,z} is Hamiltonian for every pair y,z.

Put K=H-V(P). Minimum-counterexample calculus gives |K|>=4. For each pair y,z in K, the displayed Hamiltonian four-set is proper, so its complement
H-{p_0,p_m,y,z}=G-{y,z}
is non-Hamiltonian with path-cover number two.

The two-vertex deletion G=H-{p_0,p_m} is non-Hamiltonian with path-cover number two by minimum-counterexample calculus. For every y in K, the three-set {p_0,p_m,y} is Hamiltonian because every boundary tournament of order three is Hamiltonian. If G-y were Hamiltonian, Hamilton paths on G-y and {p_0,p_m,y} would two-cover H. Thus G-y is non-Hamiltonian; being proper, it has path-cover number two.

No cyclic rotation and no reversal of a displayed path is used.