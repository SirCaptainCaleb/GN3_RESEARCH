# A closed full-root portal kernel is incoherent-current or a fixed-complement cone shell

**Workspace:** D17
**State:** established
**Key:** `portal-wheel-full-capture-graph-fixed-complement-shell`

**Summary:** Combine SV61245 with the Johnson-triangle coherence quotient SV61535. In a nonclosing reconstruction-closed family, every proper sink SCC of the all-choice P5 capture digraph leaks, so the full five-root capture digraph is strongly connected. Apply the hub Johnson-triangle compiler to every capture arc. Any INTERNAL same-pair currentization, non-endpoint trim, or support disagreement gives a literal current crossing/component-drop. Otherwise the five spoke partitions glue over the connected capture graph to one bipartition P of V(H)-{x}; every capture-edge rim fiber differs only by one hub-side bit, and adjacent rim comparisons force all those bits equal outside current geometry. Thus every spoke and rim partition restricts one global bipartition P*. The cone graph on hub plus five roots contains triangles. If both P* colors contain a cone edge, each opposite global block is Hamiltonian and H closes. Hence a nonclosing coherent kernel has exactly one independent color class Q; the opposite color contains an edge, so Q is a literal Hamiltonian global complement while Omega is non-Hamiltonian. Cross cone edges certify Omega-u and Q-v Hamiltonian, and Omega-monochromatic edges certify Omega-{u,v} Hamiltonian with fixed complement Q. If the hub lies in Q, all five roots lie in Omega and Omega-d is Hamiltonian for every d in the P5. This is a fixed-complement cone shell, not yet full critical-block closure.

### 1. Full all-choice capture kernel
Retain the G23 Hamilton P5 K and common hub x from SV58568/SV58856. Let C_K be the ALL-CHOICE root-capture digraph: its vertices are the five physical roots d in K, and d->e is an arc whenever some lawful nonclosing root-capture choice at d captures e in the sense of SV60333/SV60654.

Work inside a nonclosing reconstruction-closed family. Accepted working unit SV61245 proves that every proper sink strongly connected component of C_K leaks through a root outside it. Since every finite digraph has a sink SCC, the surviving closed kernel cannot have a proper sink SCC. Hence

  C_K is strongly connected on all five roots.             (FC.1)

Let G_K be its underlying simple undirected graph. Then G_K is connected and has at least one edge.

For every root d choose one actual spoke exact cover S_d of H-{x,d} available in the common-center reconstruction family. For every capture arc d->e, retain its same-pair currentization from SV60333. If that currentization is an INTERNAL component-drop packet, retain that CURRENT packet and stop. Otherwise the END branch supplies an actual exact rim cover R_de of H-{d,e}; choose that representative. Opposite directed arcs may therefore give two different exact representatives of the same physical pair deletion.

### 2. Every capture edge is a Johnson triangle with the hub
Apply the Johnson-triangle compiler SV61535 to the three pair fibers

  {x,d}, {x,e}, {d,e}                                    (FC.2)

for every capture arc d->e.

If any triangle exposes a current common-residue crossing/component-drop, retain it and stop. Hence assume every capture triangle is SUPPORT-COMMUTING. Then the spoke support partitions for S_d and S_e agree on their common triple-deletion residue.

Because G_K is connected, the spoke partitions glue exactly as in SV61535: after one initial block naming there is one unordered bipartition

  P=A|B of V(H)-{x}                                      (FC.3)

whose restriction to H-{x,d} is the support partition of every spoke S_d.

### 3. Rim hub-side bits synchronize on the whole capture graph
For a capture edge de, support-commutation of its hub triangle says that the support partition of R_de is obtained from P only by choosing which P-block receives the hub x. Let

  c(de) in {A,B}                                         (FC.4)

be this hub-side bit for the chosen rim representative.

Take two capture edges sharing one root, say ab and bc with a!=c. Compare their actual exact rim covers R_ab and R_bc on the common triple-deletion residue H-{a,b,c}. If c is internal in R_ab or a is internal in R_bc, deleting that internal vertex gives a literal three-cover and hence a current component-drop crossing against an exact two-cover. If both are endpoints, the two trims are exact two-covers. Their nonhub vertices inherit the same P-blocks, so c(ab)!=c(bc) makes their support partitions differ exactly at x; R410 then gives a current common-residue selected crossing.

If instead two retained rim representatives come from opposite arcs on the same unordered pair {a,b}, then differing hub bits already mean two exact covers of H-{a,b} have different support partitions, so R410 again gives a current crossing.

Therefore, outside current geometry, the hub-side bit is constant on adjacent edges of the underlying capture multigraph. The line graph of a connected graph with at least one edge is connected after parallel representatives are identified, so

  all retained capture-edge rim covers have one common hub-side bit.    (FC.5)

Extend P by placing x in that common side. Call the resulting global bipartition

  P*=Omega | Q of V(H).                                  (FC.6)

Then every chosen spoke cover and every END-currentized capture-edge rim cover has support partition exactly equal to the restriction of P* to its deleted-pair residue.

Thus the full all-choice kernel has the dichotomy

  CURRENT-INCOHERENT:
    some capture arc / hub Johnson triangle / adjacent-rim comparison exposes a literal current crossing or component drop;

  SUPPORT-COHERENT:
    the entire spoke star and all chosen capture-edge rim fibers are restrictions of one global P*.       (FC.7)

### 4. The coherent cone has one Hamiltonian color class
Assume the SUPPORT-COHERENT branch. Form the finite physical graph W whose vertices are {x} union V(K), whose edges are all five spokes x-d and all underlying capture edges de of G_K. This is the cone over the connected graph G_K. In particular every capture edge de forms the triangle x-d-e-x, so W is not bipartite.

Color W by the two global support classes Omega,Q of P*. If W contains a monochromatic Omega-edge uv, then the coherent exact cover of H-{u,v} has support partition

  (Omega-{u,v}) | Q,

so the Q-block itself carries a literal Hamilton path. Thus

  monochromatic Omega edge => Q Hamiltonian.             (FC.8)

Dually,

  monochromatic Q edge => Omega Hamiltonian.             (FC.9)

If both colors contain a monochromatic W-edge, FC.8-FC.9 give disjoint Hamilton paths on Omega and Q, a spanning two-cover of H. Therefore in a nonclosing coherent kernel exactly one color class is independent in W. Since W is non-bipartite, at least one monochromatic edge exists, so this is exhaustive.

Rename the independent color Q. Then

  Q is an independent set on W,
  Q is Hamiltonian as a global block,
  Omega is non-Hamiltonian.                               (FC.10)

Hence every nonclosing coherent full-root kernel is already a FIXED-COMPLEMENT CONE SHELL: one global Hamiltonian complement Q and one non-Hamiltonian block Omega, with the six wheel vertices colored so that Q intersects W in an independent set.

There are two elementary geometric subforms:

- if x in Q, then no root of K lies in Q because every spoke x-d is an edge; hence Q intersects W exactly in {x};
- if x in Omega, then Q intersects K in an independent set of the connected capture graph G_K (possibly empty).

### 5. Hamilton puncture data forced by cross and monochromatic edges
The coherent support partitions retain additional literal Hamiltonicity.

For every cross edge uv of W with u in Omega and v in Q, the exact pair-deletion cover has rails

  (Omega-u) | (Q-v),                                     (FC.11)

so BOTH punctured blocks are Hamiltonian.

For every monochromatic Omega edge uv, the same cover gives

  (Omega-{u,v}) | Q,                                     (FC.12)

so Omega-{u,v} is Hamiltonian while the fixed complement Q remains literally Hamiltonian.

In the particularly rigid subcase x in Q, all five spokes are cross edges. Therefore

  Omega-d is Hamiltonian for every d in K,                (FC.13)

with the same global Hamilton complement Q already available. Thus the coherent kernel has become a partial fixed-complement deletion-Hamiltonian shell on all five P5 roots.

### 6. Scope fence
FC.10-FC.13 do not yet prove Omega deletion-Hamiltonian at vertices outside the six-vertex kernel, and therefore do not by themselves satisfy the full fixed-complement critical-block hypothesis. Nor is a current crossing/component-drop in the first branch counted as strict Phi or epsilon_* descent. The gain is a branch-scale compression: after proper capture sinks are eliminated by SV61245, the full G23 wheel has no quietly incoherent support state. Its only quiet nonclosing form is one Hamiltonian global complement plus a connected finite cone of certified puncture/pair-puncture Hamiltonian supports in the opposite non-Hamiltonian block.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R4"
    },
    {
        "relation": "dependency",
        "revision_id": "R159"
    },
    {
        "relation": "dependency",
        "revision_id": "R410"
    },
    {
        "relation": "dependency",
        "revision_id": "R429"
    }
]
```