# Two-port cocircuit sector fails under independent port-preserving contraction

- Stable ID: note_nori_xi_two_port_contraction_separates_ports
- Author: unspecified; session provenance retained
- Primary home: section:nori_matroid_generalizations_conjectures
- Labels: obstruction, binary-matroid, two-port, counterexample
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

Let G be the diamond graph with vertex set {u,v,a,b} and five edges t=uv, p=ua, p'=av, q=ub, q'=bv. Let M=M(G) be its binary graphic matroid, with designated ports p and q, and contract T={t}. The set {t,p,q} is independent (a spanning tree), and Y=delta_G(u)={t,p,q} is a cocircuit containing both ports. After contracting t=uv, the graph has two parallel pairs (p,p') and (q,q') meeting at a common vertex, and M/T is the direct sum U_{1,2} plus U_{1,2}. Every cocircuit of M/T is either {p,p'} or {q,q'}, so NO cocircuit contains both ports. Thus independent contraction with faithful cycle-space projection preserving nonloop independent ports does not necessarily transport the BOTH-PORT cocircuit sector. In the repaired cocycle Y triangle K_t^*, the two ports split across different cocircuit constituents. A two-port selector theorem needs a port-cohesion or prescribed-sector irreducibility hypothesis in addition to the independent-contraction and short-certificate axioms. Note the separate single-port transfer theorem remains valid.
