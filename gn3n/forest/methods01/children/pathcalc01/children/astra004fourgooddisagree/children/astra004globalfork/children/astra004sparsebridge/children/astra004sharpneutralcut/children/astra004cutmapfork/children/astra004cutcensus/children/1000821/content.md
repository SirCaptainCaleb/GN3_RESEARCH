# A longest support maximizing good complement deletions has at least two good deletions in the neutral sparse shell

## Statement

Let H be a minimum counterexample in the sharp half-order shell |V(H)|=2lambda+1. Among all globally longest Hamiltonian lambda-supports A choose one maximizing d(A)=|{u in V(H)-A : H[(V(H)-A)-{u}] is Hamiltonian}|. Suppose d(A)<=2 and that the deletion-sparse equality-two-crossing analysis around A is completely neutral: every bad complement deletion admits the neutral cut normalization, and no same-cut pair or triple produces explicit crossing/order disturbance or odd degree at least three. Then d(A)=2. Equivalently, the cases d(A)=0 and d(A)=1 are impossible under this normalization.

## Body

Put U=V(H)-V(A) and D(A)={u in U:U-{u} is Hamiltonian}, with d=|D(A)|. Assume for contradiction d<=1. By astra004cutcensus, in the completely neutral sparse cut-map branch there is at least one repeated cut: two distinct bad labels u,v in U-D(A) have the same neutral cut.

Apply astra004samecutfork to this pair. By the present hypothesis the explicit-disturbance outcome is excluded, so the pair lies in the fixed-support odd-walk outcome. Thus, after possibly exchanging the two cut sides, there is one Hamiltonian lambda-support Q common to both deletion covers, and distinct Hamiltonian lambda-supports P_u,P_v such that P_u--Q--P_v is a length-two walk in the Hamiltonian-support odd graph with edge labels u and v.

Let W=V(H)-V(Q). Since P_u and Q are disjoint lambda-supports whose union is V(H)-{u}, one has P_u=W-{u}. Hence W-{u} is Hamiltonian. Likewise the second odd edge gives P_v=W-{v}, so W-{v} is Hamiltonian. Therefore u,v are two distinct good deletion labels for the complement W of Q, and d(Q)>=2.

The support Q has order lambda, so it is globally longest. By the defining choice of A, d(Q)<=d(A)=d<=1, contradicting d(Q)>=2. Thus d cannot be zero or one. Under the standing sparse hypothesis d<=2, necessarily d=2. ∎