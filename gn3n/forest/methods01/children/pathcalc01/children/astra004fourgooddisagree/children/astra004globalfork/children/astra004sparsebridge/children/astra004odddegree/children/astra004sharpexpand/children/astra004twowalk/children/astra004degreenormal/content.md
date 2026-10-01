# Every sharp-shell odd degree has a concrete ordered normal form

## Statement

Let H be a minimum counterexample in the sharp half-order shell |V(H)|=2lambda+1, and let G be its Hamiltonian-support odd graph. Then at least one of the following ordered structural regimes occurs. (1) Delta(G)=1: every odd edge P-Q with omitted label x is double-frozen, meaning x is the unique Hamiltonian deletion of both P union {x} and Q union {x}; hence every deletion of any vertex other than x from either enlarged side forces support crossing or relative-order disagreement. (2) Delta(G)=2: at some degree-two support S with incident edge labels x,y, the associated canonical covers (R-{x})|S of H-x and (R-{y})|S of H-y either expose the two-walk crossing/order-disagreement alternatives, or form a clean same-end omission swap on the common Hamiltonian support R-{x,y}. (3) Delta(G)=3: at some degree-three support S with incident labels x,y,z, either one incident pair exposes the two-walk crossing/order-disagreement alternatives, or the three canonical deletion covers (R-{x})|S,(R-{y})|S,(R-{z})|S are pairwise compatible and therefore collapse by gapgeom01 to one common insertion gap on the R-side with fixed second path S. (4) Delta(G)>=4: some support has at least four Hamiltonian complement deletions, so astra004manygoodmixed yields a direct mixed-support edge in an endpoint deletion cover or explicit relative-order disagreement. Thus the sharp shell has no featureless low-degree support regime: degrees one through three respectively force double-freezing, a clean one-swap, or a common-gap triangle unless explicit disturbance is already present.

## Body

# Proof

The odd graph is nonempty because bcfa72bc175f shows every ambient label occurs on some odd edge. Let Delta=Delta(G).

If Delta=1, G is a matching. Take an edge P-Q with omitted label x. By astra004odddegree applied to support Q, the Hamiltonian deletions of P union {x} are counted by deg_G(Q)=1; since deleting x leaves the Hamiltonian set P, x is its unique Hamiltonian deletion. Symmetrically Q union {x} is frozen at x. The double-frozen conclusion is then exactly c4cd6c0f9141.

If Delta=2, choose a degree-two support S. Write R=V(H)-S and let its two incident labels be x,y, so the two neighbors are R-{x},R-{y}. Apply astra004twowalk to the length-two walk (R-{x})-S-(R-{y}). Its alternatives are exactly the asserted explicit disturbance or clean same-end omission swap.

If Delta=3, choose a degree-three support S with incident labels x,y,z in R. For each pair among x,y,z apply astra004twowalk to the corresponding length-two walk through S. If any pair takes a crossing or order-disagreement branch we are done. Otherwise every pair is in the clean branch: after deleting its two labels, the two canonical covers coincide as ordered covers and the restorations use the same component end. In particular the three canonical deletion covers F_x=(R-{x})|S, F_y=(R-{y})|S, F_z=(R-{z})|S are pairwise compatible on pairwise intersections. Apply gapgeom01. It places x,y,z at one common insertion gap of the common R-{x,y,z} order, while the second component S is fixed.

If Delta>=4, choose a support S of degree at least four and put R=V(H)-S. By astra004odddegree, R has at least four Hamiltonian vertex deletions. Choose a Hamilton order on S; it is globally longest. The certified astra004manygoodmixed theorem gives the direct mixed-edge / order-disagreement conclusion.

These four cases exhaust Delta(G). ∎
