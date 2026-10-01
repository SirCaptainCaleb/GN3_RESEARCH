# An order-four endpoint triangle has a common-exchange Hamiltonian four-kernel and, in the cyclic subbranch, a universal five-shell

## Statement

In an endpoint-compatible cyclic deletion triangle H-a=(b,c,R)|Q, H-b=(c,a,R)|Q, H-c=(a,b,R)|Q with |Q|=4, there is a common q in Q such that (Q-{q}) union {z} is Hamiltonian for each z in {a,b,c}. The four-set X_q={a,b,c,q} is Hamiltonian, H-X_q has path-cover number two with explicit exact cover R|(Q-{q}), and if R begins at r_0 then (r_0,q,a),(r_0,q,b),(r_0,q,c) are tight. If the original endpoint kernel X_0={a,b,c,r_0} is the exceptional cyclic non-Hamiltonian K4, then X_q union {d} is Hamiltonian for every d outside X_q, while K=H-X_q and every K-d are non-Hamiltonian of path-cover number exactly two. Thus the explicit complement cover lies in a deletion-stable pc2 residue.

## Body

# An order-four endpoint triangle has a common-exchange Hamiltonian four-kernel and, in the cyclic subbranch, a universal five-shell

Suppose H is a minimum counterexample with an endpoint-compatible cyclic deletion triangle
H-a=(b,c,R)|Q,
H-b=(c,a,R)|Q,
H-c=(a,b,R)|Q,
where the displayed orders are tight and |Q|=4.

## A common exchange label

For z in {a,b,c}, put
C_z=Q union {z}.
This five-set is non-Hamiltonian: otherwise a Hamilton path on C_z together with the opposite component of H-z would two-cover H.

Apply the synchronized-omission theorem to the order-four component Q in the deletion cover H-z. At least four of the five vertices of C_z are Hamiltonian deletion labels. The label z itself is one, so for each z at least three of the four vertices q in Q satisfy
(Q-{q}) union {z}
Hamiltonian. Thus each z has at most one bad q. Three bad singleton sets cannot cover the four-set Q, so choose
q in Q
that is simultaneously good for z=a,b,c.

For this q, the three exchanges give exact covers of H-q
A_a | (b,c,R),
A_b | (c,a,R),
A_c | (a,b,R),
where A_z is a Hamilton path on (Q-{q}) union {z}.

Endpoint-hook forcing at the left ends of the displayed long components yields
(c,b,q), (a,c,q), (b,a,q)
tight. After cyclic relabelling the original triangle has (c,b,a) tight, so
(c,b,a,q)
is a tight Hamilton path on
X_q={a,b,c,q}.
Thus X_q is Hamiltonian.

The complement H-X_q has vertex set V(R) union (Q-{q}). Let T be any Hamilton path on the three-set Q-{q}. Then
R|T
is a two-path cover of H-X_q. The complement cannot be Hamiltonian, because together with the Hamilton path on X_q it would two-cover H. By minimality,
pc(H-X_q)=2,
and R|T is exact.

The second synchronized hook gives, when R begins at r_0,
(r_0,q,a), (r_0,q,b), (r_0,q,c)
tight. Hence the common exchange q produces a structured Hamiltonian four-kernel, an explicit exact complement split, and three synchronized first-tail barriers.

## Cyclic original kernel: universal five-shell

Assume now that
X_0={a,b,c,r_0}
is the exceptional cyclic non-Hamiltonian K4 from the endpoint-triangle theorem. Put
K=H-X_q.

Fix d in K. If d=r_0, then
X_q union {d}=X_0 union {q}
is Hamiltonian by the cyclic-K4 fifth-vertex extension theorem.

If d!=r_0, then q and d are distinct vertices exterior to X_0. Cyclic-kernel exterior forcing says that every three vertices of X_0 together with any two exterior vertices induce a Hamiltonian five-set. Taking a,b,c and q,d gives
X_q union {d}
Hamiltonian.

Thus every one-vertex exterior extension of X_q is Hamiltonian.

Since X_q is Hamiltonian, K itself cannot be Hamiltonian or H would have a spanning two-cover. Minimality gives
pc(K)=2.
Now fix d in K. If K-d were Hamiltonian, a Hamilton path on K-d together with one on X_q union {d} would two-cover H. Therefore K-d is non-Hamiltonian; again by minimality,
pc(K-d)=2.

So in the cyclic subbranch the common-exchange four-kernel has a universal Hamiltonian five-shell, while its explicit complement
K=R disjoint-union (Q-{q})
is a deletion-stable pc2 residue.
