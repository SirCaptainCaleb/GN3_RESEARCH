# A Phi-neutral singleton swap at a six-set yields local order or insertion structure

## Statement

Let H be a boundary tournament and let C=X|P|Q be a spanning three-cover minimizing Phi in its pairwise-repartition component. Assume |X|=6, P=(p_1,...,p_m) has m>=8, and y is a displayed endpoint of P. Suppose x in V(X) and there is a Phi-neutral repartition of X|P whose new supports X'=(V(X)-{x}) union {y} and P'=(V(P)-{y}) union {x} are both Hamiltonian. Choose Hamilton paths A on X and A' on X'. Then at least one of the following occurs: (1) A and A' have order disagreement on V(X)-{x}; (2) there is a tight triple (x,k,y) or (y,k,x) for some k in V(X)-{x}; (3) x,y together with one displayed edge of the common five-vertex order form a Hamiltonian four-set; (4) the common five-vertex order is a tight path and both x and y extend the same endpoint of it.

## Body

Put K=V(X)-{x}. If A and A' order K differently, outcome (1) holds. Hence suppose they induce the same relative order C_K on K.

Because y is a displayed endpoint of P and m>=8, the seven-set V(X) union {y} is non-Hamiltonian. Indeed, if it were Hamiltonian, then together with the inherited endpoint truncation P-y it would repartition X|P with size pair
6,m -> 7,m-1.
The Phi change is
7^2+(m-1)^2-[6^2+m^2]=14-2m<0,
contradicting local Phi-minimality.

Apply d495c62905f0 to the Hamilton paths A on K union {x} and A' on K union {y}. If the insertion gaps of x and y in the common K-order are separated by at least two positions, d495c62905f0 Hamiltonizes K union {x,y}=V(X) union {y}, contradiction. If the gaps are adjacent, the same lemma gives either Hamiltonicity of that seven-set, again impossible, or a reverse cross triple, yielding (2). If the gaps coincide at an internal edge of the common order, d495c62905f0 gives a Hamiltonian four-set on x,y and that edge, yielding (3).

The only remaining case is that the two insertion gaps coincide at one endpoint of the common K-order. In this case d495c62905f0 also shows that the common K-order itself is a tight path and both x and y extend the same endpoint of it. This is (4).
