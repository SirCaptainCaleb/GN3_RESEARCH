# Inner facing four-windows have local two-move potential formulas

**Summary:** Inner facing four-windows have local two-move potential formulas.

## Statement

Let H be a boundary tournament, let P=(p_0,...,p_{p-1}) and Q=(q_0,...,q_{q-1}) be vertex-disjoint tight paths with p,q>=3, and let x lie outside both. Regard P|Q|{x} as a three-path cover of its union. If W_L={p_0,q_{q-1},x,p_1} is Hamiltonian, then two pairwise repartitions of this local cover produce W_L | (p_2,...,p_{p-1}) | (q_0,...,q_{q-2}), with quadratic-potential change 20-4p-2q. If W_R={p_0,q_{q-1},x,q_{q-2}} is Hamiltonian, two pairwise repartitions produce the symmetric local cover of component orders 4,p-1,q-2, with change 20-2p-4q.

## Body

For W_L, first repartition Q|{x} into the inherited path (q_0,...,q_{q-2}) and the two-vertex path (q_{q-1},x). Then repartition P together with that two-vertex path into the Hamiltonian four-set W_L and the inherited tail (p_2,...,p_{p-1}). Every vertex of V(P) union V(Q) union {x} appears exactly once, so both moves are legal pairwise repartitions of the local three-path cover. The component orders change from p,q,1 to 4,p-2,q-1, and the potential change is 16+(p-2)^2+(q-1)^2-(p^2+q^2+1)=20-4p-2q. The W_R case is symmetric: first split P|{x} as (p_1,...,p_{p-1}) | (p_0,x), then combine (p_0,x) with Q using W_R, leaving (q_0,...,q_{q-3}); the component orders are 4,p-1,q-2 and the change is 20-2p-4q. No ambient spanning hypothesis is used.

## Metadata

- ID: facing_k4_local_twomove_formula01
- Kind: toolkit
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
