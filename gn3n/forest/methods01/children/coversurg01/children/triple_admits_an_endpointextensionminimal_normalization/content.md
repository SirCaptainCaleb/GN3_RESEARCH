# A mandatory two-cover triple admits an endpoint-extension-minimal normalization

## Statement

Let H be a boundary tournament with at least one spanning two-cover, and let T=(a,b,c) be a tight ordered triple that occurs consecutively, in that order, in one component of every spanning two-cover of H. Choose a spanning two-cover A|B and a displayed tight order on A containing (a,b,c) consecutively so that |A| is minimum among all spanning two-covers. Then for each endpoint v of the displayed path A, the induced subtournament H[V(B) union {v}] is non-Hamiltonian. Consequently v is noninsertable into every position of every displayed Hamilton order on B.

## Body

Choose A|B with A containing the mandatory ordered triple T=(a,b,c) consecutively and with |A| minimum. Let v be an endpoint of the displayed tight order on A. Suppose for contradiction that H[V(B) union {v}] is Hamiltonian; choose a Hamilton path B_v on that support. Deleting the endpoint v from the displayed order of A leaves an inherited tight path A-v. Hence (A-v)|B_v is a spanning two-cover of H.

If v is not one of a,b,c, then A-v still contains (a,b,c) consecutively. Its T-containing component has order |A|-1, contradicting the minimal choice of |A|.

If v belongs to {a,b,c}, then because T occurs consecutively in A and v is an endpoint of A, necessarily v=a with T at the beginning of A, or v=c with T at the end of A. In either case A-v does not contain all three vertices of T, while B_v contains only v from T because B was disjoint from A. Thus the spanning two-cover (A-v)|B_v contains no component with the mandatory consecutive triple (a,b,c), contradicting the hypothesis that every spanning two-cover contains T.

Therefore H[V(B) union {v}] is non-Hamiltonian for both endpoints v of A. Any successful insertion of v into a Hamilton order of B would itself Hamiltonize V(B) union {v}, so v is noninsertable into every such displayed order. ∎