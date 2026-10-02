# Incidence-rank path conjecture

## Statement

For every ell>=4, if H is a linear 3-uniform P_ell-free hypergraph with m edges and incidence matrix N, then ell*rank_R N >= 3m.

## Body

Unproved conjecture proposed as the sharp-form target for the rank route. It would imply m <= (ell/3)|V(H)| because rank N <= |V(H)|, reaching the conjectural leading coefficient 1/3 with no additive term. Calibration: at ell=4 this is exactly Ramani's sharp cograph incidence-rank theorem 4 rank N >= 3m. For the Tang-Wu-Zhang P5 extremal G0 (15 edges on 11 vertices), direct exact row-reduction of the displayed 15x11 incidence matrix gives rank 10, so 5 rank N=50>45=3m. The realizability hypothesis is essential: graph-only PSD information is insufficient. The complete q-partite graph K_{3,...,3} has 3I+A positive semidefinite, rank(3I+A)=2q+1 and is induced-P4-free; for q>4 it violates 4 rank >=3|V|. Ramani's parallel-class argument explains why q>4 cannot arise from a linear triple-system incidence representation: realizability caps the number of size-3 balanced parallel classes at 4. This suggests extending the balanced-component/orthogonality mechanism beyond cographs, rather than proving a statement for arbitrary graphs with lambda_min>=-3. Immediate proof obligation: identify a decomposition or local reduction for induced-P_ell-free realizable line graphs under which rank deficit can be charged at rate at most (ell-3)/ell per edge. Falsification test: search for a P_ell-free linear triple system with rank N < 3m/ell.