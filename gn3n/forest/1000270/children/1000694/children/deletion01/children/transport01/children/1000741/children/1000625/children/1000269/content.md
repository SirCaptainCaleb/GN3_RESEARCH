# An order-four endpoint triangle forces four persistent noninsertable vertices on three long paths

## Statement

Let H be a minimum counterexample with an endpoint-compatible deletion triangle H-a=(b,c,R)|Q, H-b=(c,a,R)|Q, H-c=(a,b,R)|Q in cyclic precedence, and suppose Q has order four. Then Q plus any one or any two of {a,b,c} is non-Hamiltonian. For every q in Q and every pair of labels u,v, the five-set (Q-{q}) union {u,v} is Hamiltonian. Consequently, for every label w in {a,b,c}, every q in Q is noninsertable into the displayed tight path (w,R).

## Body

Write Q=(q0,q1,q2,q3). The endpoint-compatible triangle has exact deletion covers
H-a=(b,c,R)|Q,
H-b=(c,a,R)|Q,
H-c=(a,b,R)|Q,
with the displayed orders tight.

First, Q union {a} is non-Hamiltonian. Otherwise a Hamilton path on Q union {a}, together with the tight complementary path (b,c,R) from H-a, would two-cover H. The same argument gives non-Hamiltonicity of Q union {b} and Q union {c}.

Next, Q union {a,b} is non-Hamiltonian. Its complement is the support of the tight path (c,R): this path occurs as the suffix beginning at c of the displayed component (b,c,R) in H-a. Hence Hamiltonicity of Q union {a,b} would again two-cover H. Symmetrically, Q union {a,c} and Q union {b,c} are non-Hamiltonian.

Fix distinct labels u,v. The six-set Q union {u,v} is therefore non-Hamiltonian, and its two five-subsets obtained by deleting u or v are Q union {v} and Q union {u}, both non-Hamiltonian. By the certified four-of-six theorem, at least four of the six five-vertex deletions of any six-set are Hamiltonian. The only four remaining deletions are the four sets
(Q-{q}) union {u,v}, q in Q.
Thus all four of them are Hamiltonian.

Finally fix a label w and q in Q, and let {u,v}={a,b,c}-{w}. The path (w,R) is tight: it is a contiguous suffix of one of the three displayed deletion-cover components. Suppose q were insertable into this displayed path. Then there would be a tight Hamilton path on {q,w} union V(R). Its complement in H is exactly
(Q-{q}) union {u,v},
which is Hamiltonian by the preceding paragraph. These two Hamilton paths would form a spanning two-cover of H, contradiction.

Therefore every q in Q is noninsertable into each of (a,R),(b,R),(c,R). The order-four branch is thus not merely a seven-vertex local obstruction: it creates four common persistent insertion obstructions along three long paths sharing the same tail R.