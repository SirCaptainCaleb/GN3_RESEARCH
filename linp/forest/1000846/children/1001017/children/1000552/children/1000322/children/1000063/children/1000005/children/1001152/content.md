# Minimal-counterexample minimum-degree reduction

## Statement

Let d>=0 and let P be any hereditary property of finite hypergraphs. To prove |E(H)|<=d|V(H)| for all H with property P, it is enough to prove it for H with minimum degree δ(H)>d. Equivalently, every smallest counterexample to the inequality has δ(H)>d.

## Body

Suppose H is a counterexample with the fewest vertices. If some vertex v has degree at most d, then H-v still has property P and by minimality satisfies |E(H-v)|<=d(|V(H)|-1). Therefore |E(H)|=|E(H-v)|+d_H(v)<=d(|V(H)|-1)+d=d|V(H)|, contradiction. Hence δ(H)>d. In particular, for the target |E(H)|<=floor(2ell/3)|V(H)| in the P_ell^(3)-free linear 3-graph problem, a smallest counterexample may be assumed to satisfy δ(H)>=floor(2ell/3)+1.
