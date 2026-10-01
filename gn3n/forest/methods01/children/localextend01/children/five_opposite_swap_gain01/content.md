# Two opposite five-side swaps force disagreement or a one-vertex longer path

## Statement

Let H be a boundary tournament, let P=(p_1,...,p_m), m>=3, be a tight path, and let x lie outside V(P). Suppose both induced supports (V(P)-{p_1}) union {x} and (V(P)-{p_m}) union {x} are Hamiltonian. Then either some pair among P and chosen Hamilton paths on those two replacement supports has order disagreement on common vertices, or H[V(P) union {x}] is Hamiltonian. Consequently, in the five-side neutral-swap setting of astra003fiveswapobstruct, if the same displaced label x admits successful swaps with both endpoints of one long component P, then either explicit order disagreement occurs or P+x is a Hamiltonian path support of order |P|+1.

## Body

# Proof

Choose a Hamilton tight path L on (V(P)-{p_1}) union {x} and a Hamilton tight path R on (V(P)-{p_m}) union {x}. If H[V(P) union {x}] is Hamiltonian there is nothing to prove. Otherwise all hypotheses of Section 1 of the certified insertion and endpoint-replacement calculus insert01 apply to Q=P, y=x, L, and R. That theorem states that at least one of the pairs (P,L), (P,R), (L,R) has two common vertices in different relative order. Hence order disagreement occurs.

The final sentence is exactly the specialization to the two successful equal-Phi endpoint swaps supplied by astra003fiveswapobstruct. ∎