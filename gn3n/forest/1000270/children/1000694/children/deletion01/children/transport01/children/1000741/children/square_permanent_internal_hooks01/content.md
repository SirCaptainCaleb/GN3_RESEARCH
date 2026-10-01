# A vertex internal in every two-cover forbids extensions of complementary paths

## Statement

Let G be a boundary tournament admitting a two-cover, and let d be a vertex that is internal in every two-cover of G. Suppose G-d=P|Q is a two-cover. Then |P|,|Q|>=3. For every S subseteq V(P), if G[(V(P)-S) union {d}] has a Hamilton path with endpoint d, then G[V(Q) union S] is non-Hamiltonian; the symmetric assertion also holds. In particular, if |P|=3, then G[V(Q) union {p}] is non-Hamiltonian for every p in V(P).

Write P=(p_0,...,p_m) and Q=(q_0,...,q_s). The four triples (p_1,p_0,d), (d,p_m,p_{m-1}), (q_1,q_0,d), and (d,q_s,q_{s-1}) are tight. Moreover either (q_1,q_0,d,p_m,p_{m-1}) is a tight path or (p_m,d,q_0) is tight; and either (p_1,p_0,d,q_s,q_{s-1}) is a tight path or (q_s,d,p_0) is tight.

## Body

First, every set {d,a,b} of three distinct vertices has a Hamilton path with endpoint d: exactly one of (d,a,b) and (b,a,d) is tight. Sets of order one or two also have a path with the prescribed endpoint. If a path in the two-cover P|Q had order at most two, adjoining d to its support and using this observation would give a two-cover of G with endpoint d. Thus both path orders are at least three.

Let S be as in the statement. A Hamilton path with endpoint d on (V(P)-S) union {d}, together with a hypothetical Hamilton path on V(Q) union S, would be a two-cover of G with endpoint d. These supports are disjoint and partition V(G), so this is forbidden. When |P|=3 and S={p}, the first support has order three and the rooted path exists by the first paragraph. This proves all three non-Hamiltonian extensions of Q. Notice that the conclusion forbids every Hamilton order on Q+p, not merely insertion into the displayed Q.

Since d cannot prepend to P, (d,p_0,p_1) is a non-edge, and its reversal (p_1,p_0,d) is tight. Since d cannot append to P, (p_{m-1},p_m,d) is a non-edge, and (d,p_m,p_{m-1}) is tight. The same reasoning applies to Q. Exactly one of (q_0,d,p_m) and (p_m,d,q_0) is tight. In the first case the three consecutive triples of (q_1,q_0,d,p_m,p_{m-1}) are the initial hook, this triple, and the terminal hook. In the second case the stated cross triple holds. The other pair is identical, using (p_1,p_0,d,q_s,q_{s-1}). All five labels are distinct because the two paths are disjoint and each has at least three vertices.

No minimum-counterexample hypothesis, Hamiltonian four-set, or additional deletion label is needed. The former square statement follows by taking G=K+d+e. The result constrains the whole family of two-covers of G-d; it does not assert that a vertex internal in every two-cover is impossible.
