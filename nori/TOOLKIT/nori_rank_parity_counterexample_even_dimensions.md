# Rank-parity counterexample to unrestricted antipodal-reversal-odd length-three geodesic conjecture

## Statement

For every even n≥6, the unrestricted NORI conjecture is false.

## Body

Let n be even and n≥6. For each directed length-three geodesic P=(x0,x1,x2,x3) of Q_n define c(P)=|x0| mod 2, where |x| is Hamming weight. Antipodal reversal gives J(P)=(bar x3,bar x2,bar x1,bar x0). Since length three flips exactly three bits, |x3|≡|x0|+3 (mod 2), and |bar x3|≡n−|x3|≡|x0|+1 (mod 2) for even n. Hence c(JP)=1−c(P). On any antipodal geodesic γ=(v0,...,vn), the ith length-three window starts at vi, and |v(i+1)|≡|vi|+1 (mod 2). Thus the consecutive window colors strictly alternate, giving n−3 color changes. For n≥6 this exceeds one. Therefore there is no good antipodal geodesic. This counterexample is in the original NOR Article I development under rank_parity_refutes_unrestricted_n_k and rank_parity_refutes_the_unrestricted_tuple_window_n_k; its exclusion was valid only for NOR's coordinate-only model, not NORI. Status: rigorous counterexample to NORI's current conjecture.

## Metadata

- ID: nori_rank_parity_counterexample_even_dimensions
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
