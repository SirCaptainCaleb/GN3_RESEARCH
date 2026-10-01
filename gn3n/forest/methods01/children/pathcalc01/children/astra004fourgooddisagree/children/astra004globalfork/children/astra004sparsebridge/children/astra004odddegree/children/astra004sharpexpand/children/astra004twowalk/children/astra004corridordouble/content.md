# Two consecutive clean odd-walk swaps make the middle deletion cover double-clean

## Statement

Let H be a minimum counterexample in the sharp half-order shell and let S_0-S_1-S_2-S_3 be a simple four-vertex path in the Hamiltonian-support odd graph, with consecutive omitted labels a,b,c. Assume the two length-two walks S_0-S_1-S_2 and S_1-S_2-S_3 both take the clean alternative of astra004twowalk. Then the middle exact deletion cover H-b=S_1|S_2 admits simultaneous clean endpoint replacements by b on both components: in a Hamilton order P on S_1 the label c is an endpoint and replacing c by b at that same end gives a Hamilton order on S_3=(S_1-{c}) union {b}; in a Hamilton order Q on S_2 the label a is an endpoint and replacing a by b at that same end gives a Hamilton order on S_0=(S_2-{a}) union {b}. If these two replaced endpoints are opposite ends of P,Q, then the unique central join that would concatenate the two shortened components through b must be non-tight, so its reverse is tight. Explicitly, if P=(...,u,c) and Q=(a,v,...), then (v,b,u) is tight; if P=(c,u,...) and Q=(...,v,a), then (u,b,v) is tight. Thus a clean degree-two corridor either synchronizes both replacements to the same side type or already exports an explicit reverse cross-bridge through the middle omitted label.

## Body

# Proof

For the walk S_0-S_1-S_2 with labels a,b, the clean conclusion of astra004twowalk says that after deleting a,b the outer supports share one Hamilton order K and a,b restore at the same end. Viewed from the middle edge cover H-b=S_1|S_2, this says precisely that a is an endpoint of the S_2 Hamilton order Q and that deleting a and restoring b at the same end gives the outer neighbor S_0. Likewise, cleanliness of S_1-S_2-S_3 says c is an endpoint of the S_1 Hamilton order P and deleting c and restoring b at the same end gives S_3. This proves simultaneous double cleanliness.

Assume first P=(p_0,...,u,c) and Q=(a,v,...,q_s). The two clean replacements give tight paths (p_0,...,u,b) and (b,v,...,q_s). If (u,b,v) were tight, their union through the common b would form the tight path (p_0,...,u,b,v,...,q_s), spanning (S_1-{c}) union {b} union (S_2-{a}). The two omitted endpoint labels a,c form a two-vertex tight path. These two paths would span H, contradicting pc(H)>2. Hence (u,b,v) is non-tight, and boundary antisymmetry gives (v,b,u) tight.

The case P=(c,u,...,p_m), Q=(q_0,...,v,a) is symmetric: if (v,b,u) were tight, (q_0,...,v,b,u,...,p_m)|(a,c) would two-cover H, so (u,b,v) is tight. ∎