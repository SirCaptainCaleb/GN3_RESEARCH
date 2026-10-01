# Every facing deletion-cover endpoint pair lies in an explicit Hamiltonian four-window

## Statement

Let H be a minimum counterexample and let H-x=P|Q be a deletion two-cover, with displayed paths P=(p_0,...,p_m) and Q=(q_0,...,q_s), where both components have order at least three.

For the facing endpoint pair p_0,q_s, at least one of the following three four-sets is Hamiltonian:
W_L={p_0,q_s,x,p_1},
W_R={p_0,q_s,x,q_{s-1}},
W_O={p_0,q_s,p_1,q_{s-1}}.
In every case the complement is non-Hamiltonian with path-cover number two.

Symmetrically, for the other facing pair q_0,p_m, at least one of
{q_0,p_m,x,q_1},
{q_0,p_m,x,p_{m-1}},
{q_0,p_m,q_1,p_{m-1}}
is Hamiltonian with non-Hamiltonian path-cover-two complement.

Thus a facing endpoint pair never requires a five-vertex support: it always lies in a positioned Hamiltonian four-window.

## Body

Apply reversal_global_frontier01 in its fixed-pair form to the prescribed pair L=p_0, R=q_s and to the three-element set
D={x,p_1,q_{s-1}}.
The hypotheses are valid because both displayed components have order at least three, so p_1 and q_{s-1} exist and all five labels are distinct.

The theorem says that some two labels y,z in D make {p_0,q_s,y,z} Hamiltonian, with non-Hamiltonian path-cover-two complement. The three possible unordered pairs {y,z} are exactly
{x,p_1}, {x,q_{s-1}}, {p_1,q_{s-1}},
which give W_L, W_R, and W_O respectively.

For the other facing pair q_0,p_m, apply the same fixed-pair theorem to L=q_0, R=p_m and
D={x,q_1,p_{m-1}}.
Again the three possible chosen pairs give exactly the three displayed four-sets.

No orientation of the original deletion-cover paths is reversed, and no cyclic invariance is used.