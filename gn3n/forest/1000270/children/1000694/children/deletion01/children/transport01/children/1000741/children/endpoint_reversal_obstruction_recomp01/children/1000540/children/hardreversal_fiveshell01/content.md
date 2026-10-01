# A universal endpoint-reversal family gives Hamiltonian five-sets over every exterior triple

## Statement

Let H be a minimum counterexample and let P=(p_0,...,p_m), m>=2, be a proper tight path. Put K=V(H)-V(P), and suppose that every y in K satisfies the three tight triples
(p_1,p_0,y), (p_m,y,p_0), and (y,p_m,p_{m-1}).
Then |K|>=4, and for every three distinct y,z,w in K the five-set {p_0,p_m,y,z,w} is Hamiltonian. Consequently its complement is non-Hamiltonian with path-cover number two. Hence for every four-set E subseteq K, the six-set {p_0,p_m} union E has at least four Hamiltonian vertex deletions, namely the deletions of the four vertices of E.

## Body

# Proof

By minimum-counterexample calculus, every tight path leaves at least four vertices, so |K|>=4.

Fix distinct y,z,w in K. By hypothesis the three tight triples
(p_m,y,p_0), (p_m,z,p_0), (p_m,w,p_0)
hold. Apply the certified small-set lemma stating that three common-endpoint triples (a,p,c), (a,q,c), (a,r,c) force a Hamiltonian five-path on {a,c,p,q,r}, with a=p_m and c=p_0. Therefore H[{p_0,p_m,y,z,w}] is Hamiltonian.

This five-set is proper because |K|>=4. If its complement were Hamiltonian, Hamilton paths on the five-set and on its complement would form a spanning two-cover of H, contradicting that H is a minimum counterexample. By minimum-counterexample calculus the complement has path-cover number at most two, hence exactly two.

Finally fix four distinct outside vertices y,z,w,t. Deleting any one of them from S={p_0,p_m,y,z,w,t} leaves one of the Hamiltonian five-sets just proved. Thus S has at least four Hamiltonian vertex deletions. ∎
