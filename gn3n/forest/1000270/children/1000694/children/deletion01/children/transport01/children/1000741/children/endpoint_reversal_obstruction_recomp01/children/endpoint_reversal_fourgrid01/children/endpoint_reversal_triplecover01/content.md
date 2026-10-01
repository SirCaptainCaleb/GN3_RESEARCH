# The fixed-endpoint four-grid captures every outside triple

## Statement

In the complete fixed-endpoint four-grid branch of endpoint_reversal_fourgrid01, let a=p_0 and b=p_m, let x be the distinguished exterior witness from that branch, and let Y=V(H)-(V(P) union {x}). For every three distinct y,z,w in Y, either H[{a,b,y,z,w}] is Hamiltonian, or at least one of H[{a,y,z,w}] and H[{b,y,z,w}] is Hamiltonian. Every Hamiltonian support arising here is proper and has non-Hamiltonian complement of path-cover number two.

## Body

# Proof

Let x be the distinguished exterior witness from endpoint_reversal_fourgrid01 and put Y=V(H)-(V(P) union {x}). Fix distinct y,z,w in Y. By endpoint_reversal_fourgrid01 the three four-sets

W_yz={a,b,y,z},  W_yw={a,b,y,w},  W_zw={a,b,z,w}

are Hamiltonian, and each has non-Hamiltonian path-cover-two complement. Apply the certified overlap-amplification theorem d9a4b66724d2 to W_yz and W_yw. They meet in the three-set {a,b,y}, and their union is

S={a,b,y,z,w}.

If H[S] is Hamiltonian, the first alternative holds. Otherwise d9a4b66724d2 says that at least four of the five four-subsets of S are Hamiltonian. Three of them are already W_yz,W_yw,W_zw, namely the subsets obtained by deleting w,z,y. Therefore at least one of the remaining two four-subsets, S-{a}={b,y,z,w} or S-{b}={a,y,z,w}, is Hamiltonian.

All these supports have order four or five and H has order greater than ten, so they are proper. If the complement of any such support were Hamiltonian, the two Hamilton paths would give a spanning two-cover of H. Minimum-counterexample calculus therefore gives path-cover number exactly two for every complement. ∎
