# A unique intersection of two equal-potential entrance rails is an aligned joint

## Statement

Let
   Q=(e_1,...,e_q),   Q'=(f_1,...,f_q)
be q-edge linear paths ending physically at vertices y,y' with
   phi(y)=phi(y')=q.
Assume
   V(Q)∩V(Q')={w}.

Then w is a path joint on both rails, and at the same index: there exists
   1<=t<=q-1
such that
   w=e_t∩e_{t+1}=f_t∩f_{t+1}.

Apply this to two canonical high entrance rails Q_i,Q_j in a q,(q+1)^3 configuration. If their only common vertex is w, then their mandatory crossings of the opposite high edges are reciprocal terminal crossings:
   z_j∈V(Q_i),   z_i∈V(Q_j).
Indeed Q_i cannot meet h_j at y_j, and Q_j cannot meet h_i at y_i, because y_j∈Q_j and y_i∈Q_i would give additional common vertices.

## Body

For a q-edge path Q and a vertex w on it, split Q at w as follows.

If w is private to e_t, let
   alpha=t,  beta=q-t+1.
Then e_1,...,e_t is an alpha-edge path ending at w, while e_t,...,e_q is a beta-edge path starting at w and ending at y.

If w=e_t∩e_{t+1} is a joint, let
   alpha=t,  beta=q-t.
Then e_1,...,e_t ends at w and e_{t+1},...,e_q starts at w and ends at y.

Thus always
   alpha+beta = q+epsilon,
where epsilon=1 in the private case and epsilon=0 in the joint case.

Define alpha',beta',epsilon' similarly for Q'.

Because Q and Q' have no common vertex except w, concatenate the w-ending prefix of Q with the w-starting suffix of Q'. This is a linear path ending at y' of length
   alpha+beta'.
Hence
   alpha+beta'<=phi(y')=q.
Similarly,
   alpha'+beta<=q.

Adding gives
   (alpha+beta)+(alpha'+beta')<=2q.
The left side equals
   2q+epsilon+epsilon'.
Therefore epsilon=epsilon'=0: w is a joint on both paths.

Now beta=q-alpha and beta'=q-alpha'. The two inequalities give alpha<=alpha' and alpha'<=alpha. Hence
   alpha=alpha'=t,
so w is the joint at the same index t on both rails.

For the final assertion, let Q_i,Q_j be canonical entrance rails for high edges
   h_i={y_i,v,z_i}, h_j={y_j,v,z_j}.
Each rail avoids v and its own opposite terminal. By 21dfd53c201f, Q_i meets h_j and Q_j meets h_i. If V(Q_i)∩V(Q_j)={w}, then Q_i cannot contain y_j, since y_j is the endpoint of Q_j and y_j!=w; likewise Q_j cannot contain y_i. Therefore the forced contacts are z_j on Q_i and z_i on Q_j.