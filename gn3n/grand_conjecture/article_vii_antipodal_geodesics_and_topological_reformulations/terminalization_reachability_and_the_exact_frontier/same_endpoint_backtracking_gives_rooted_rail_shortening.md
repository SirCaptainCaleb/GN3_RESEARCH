# Same-endpoint backtracking gives rooted rail shortening

## Composition

(none yet)

## Development

Correct and sharpen the same-endpoint backtracking analysis. Suppose compatible deletion covers have
F_a=(b,p_1,...,p_m)|Q,
F_b=(a,p_1,...,p_m)|Q,
with Q=(q_1,...,q_t), and a,b inserted in the same initial endpoint gap of the common P-core.

Neither a nor b attaches at either end of Q, so for z in {a,b},
h(q_2,q_1,z)=1 and h(z,q_t,q_{t-1})=1 whenever the displayed edges exist.

The previously stored proof incorrectly used (q_2,q_1,z,q_t,q_{t-1}) as a five-path for t=3; that sequence repeats q_2. The correct case split is:

1. t=1: direct two-cover, as before.
2. t=2: (b,q_2,q_1,a) is Hamiltonian and its complement P is Hamiltonian, so H is directly two-covered. Thus t=2 cannot occur in a counterexample.
3. t=3: if h(q_1,z,q_3)=1 for either z, then (q_2,q_1,z,q_3) is Hamiltonian on Q union {z}; its complement is the Hamiltonian path on the other root followed by P, so H is two-covered. Hence both roots must satisfy h(q_3,z,q_1)=1. They are parallel middle vertices between q_3,q_1, so {q_3,q_1,a,b} is Hamiltonian. Its displayed complement is P | {q_2}: the Q-rail has shortened by two.
4. t=4: if h(q_1,z,q_4)=1 for either z, then (q_2,q_1,z,q_4,q_3) is Hamiltonian on Q union {z}, whose complement is the other-root-plus-P Hamiltonian path, so H is two-covered. Hence again both roots satisfy h(q_4,z,q_1)=1 and {q_4,q_1,a,b} is Hamiltonian, with inherited complement P | (q_2,q_3).
5. t>=5: if h(q_1,z,q_t)=1 for some z, then K=(q_2,q_1,z,q_t,q_{t-1}) is a Hamiltonian five-support. Its complement has the explicit inherited two-cover
(other root,p_1,...,p_m) | (q_3,...,q_{t-2}),
so the Q-rail shortens by four. If neither root has this orientation, then h(q_t,a,q_1)=h(q_t,b,q_1)=1; parallel-middle gives the Hamiltonian four-support
K={q_t,q_1,a,b},
whose complement has inherited two-cover
P | (q_2,...,q_{t-1}),
so the Q-rail shortens by two.

Thus same-endpoint backtracking is not terminal merely because it yields a bounded support; bare bounded support is automatic under minimum-counterexample calculus. Its genuine output is a rooted, inherited rail-shortening state, with a direct two-cover for t<=2 and explicit shortening by two or four thereafter. No cyclic/path reversal or computation is used.
