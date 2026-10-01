# Conditional threshold-set deletion endgame under simultaneous Turan excess

## Statement

Let ell>=4, put k=floor(2ell/3)+1, and let H be a P_ell-free linear 3-graph which simultaneously satisfies: (i) the threshold-core conclusions of 1e01357bf9c3 for D={v:d_H(v)=k}, and (ii) the sharp Turan excess |E(H)|>(k-1)|V(H)|. For i=1,2,3 let m_i be the number of edges containing exactly i vertices of D. If m_2+2m_3>=|D|, then deleting D is compatible with the sharp Turan induction at coefficient k-1. Hence under these simultaneous hypotheses one must have m_2+2m_3<=|D|-1.

## Body

The counting identity itself is unconditional once D consists of degree-k vertices:
k|D|=m_1+2m_2+3m_3.
The number m_D of edges meeting D is
m_D=m_1+m_2+m_3
   =k|D|-(m_2+2m_3).

Thus if m_2+2m_3>=|D| then
m_D<=(k-1)|D|.

If, in addition, H is being treated inside a vertex-induction proof of the Turan inequality and H-D is known by induction to satisfy
|E(H-D)|<=(k-1)(|V(H)|-|D|),
then
|E(H)|=|E(H-D)|+m_D<=(k-1)|V(H)|,
contradicting Turan excess.

Therefore any H for which both the threshold-core structure and the Turan-excess induction hypotheses hold must satisfy
m_2+2m_3<=|D|-1.

MINIMALITY FENCE.
The threshold-core structure 1e01357bf9c3 was obtained by choosing an edge-minimal counterexample to the dense-core all-special statement, whereas a smallest Turan counterexample is minimal under vertex deletion / edge count for a different property. Passing from a Turan counterexample to an edge-minimal dense-core subgraph can destroy the Turan excess. Hence this lemma is presently a conditional endgame and must not be applied to an arbitrary edge-minimal dense-core counterexample without an additional excess-preservation/equality-layer bridge.