# The mutual bad-extension core generates six mixed 5|3 repartitions with exact excluded bad deletions

## Statement

In the eight-label residue of 851be99bfc11, write P={u,a,b,c}, Q=(q0,q1,q2,q3)={v,d,e,f} in any Hamilton order of Q, and X={t,s,w}. For each pair of distinct r1,r2 in {a,b,c}, localextend01 forces both {q0,q1,q2,r1,r2} and {q1,q2,q3,r1,r2} Hamiltonian. Hence P union Q admits six legal 5|3 repartitions. For each such repartition, pairing the resulting 3-side with X gives a six-set whose deletions at t and u are non-Hamiltonian; therefore by four-of-six these are exactly its two bad deletions.

## Body

Work in the eight-label residue of 851be99bfc11. Write
[
X={t,s,w},qquad P={u,a,b,c},
]
where (t,u) are excluded singleton labels, and choose a Hamilton order
[
Q=(q_0,q_1,q_2,q_3).
]
The three labels (a,b,c) are all bad one-vertex extensions of (Q):
[
Qcup{a},quad Qcup{b},quad Qcup{c}
]
are non-Hamiltonian.

Fix distinct (r_1,r_2in{a,b,c}). Applying the certified repeated-bad-extension lemma of localextend01 to the Hamilton four-path (Q) and exterior vertices (r_1,r_2) gives both
[
H_0(r_1,r_2)={q_0,q_1,q_2,r_1,r_2},
]
and
[
H_3(r_1,r_2)={q_1,q_2,q_3,r_1,r_2}
]
Hamiltonian.

Let (r_3) be the third member of ({a,b,c}). Then the complements of these five-sets inside (Pcup Q) are respectively
[
{u,r_3,q_3},
qquad
{u,r_3,q_0},
]
and every three-vertex boundary tournament is Hamiltonian. Therefore each (H_i(r_1,r_2)) gives a legal Astra repartition of the pair (P|Q) into sizes (5|3).

Keeping (X) unchanged, we obtain a reachable (5|3|3) state. In the first case, the union of the two three-sides is
[
R_3(r_3)={u,r_3,q_3,t,s,w}.
]
In the second case it is
[
R_0(r_3)={u,r_3,q_0,t,s,w}.
]

We claim that in each such six-set both (t) and (u) are bad deletion labels.

If (R_i(r_3)-{t}) were Hamiltonian, then together with the untouched Hamiltonian five-set (H_i(r_1,r_2)) it would give a reachable (5|5|1) state with singleton (t), contradicting (t
otin S).

Likewise, if (R_i(r_3)-{u}) were Hamiltonian, the same untouched five-side would give a reachable (5|5|1) state with singleton (u), contradicting (u
otin S).

Thus (t,u) are both bad deletions. By four-of-six, a six-set has at most two bad deletion labels. Hence they are exactly the bad deletion set of every
[
R_i(r_3),qquad iin{0,3}, r_3in{a,b,c}.
]

Consequently the mutual bad-extension core produces six mixed (5|3) repartitions of (Pcup Q), and the corresponding six-sets
[
{u,r,q_i,t,s,w}
]
for (rin{a,b,c}) and (q_iin{q_0,q_3}) all have exact bad deletion set
[
{t,u}.
]
