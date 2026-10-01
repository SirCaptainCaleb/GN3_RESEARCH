# A clean three-step repeated label is automatically the reciprocal singleton rectangle

## Statement

Let H be a minimum counterexample in the sharp half-order shell and let S_0-S_1-S_2-S_3-S_4 be a simple four-edge path in the Hamiltonian-support odd graph with consecutive edge labels a,b,c,a. Choose Hamilton orders on the supports and assume the three length-two subwalks S_0-S_1-S_2, S_1-S_2-S_3, and S_2-S_3-S_4 are clean in the sense of astra004twowalk. Then the two distinct covers S_0|S_1 and S_3|S_4 of H-a satisfy the reciprocal two-crossing equality case of astra004recrect with no intersection-order disagreement. More precisely, after naming the clean inherited orders, their four intersections are S_0∩S_3={b}, S_0∩S_4=S_0-{b}, S_1∩S_3=S_1-{c}, S_1∩S_4={c}; each large intersection has order lambda-1 and occurs with exactly the same inherited order in both covers, while b and c occur as endpoint singleton blocks. Therefore astra004rectsingleton applies unconditionally: the repeated-label corridor either has the fully alternating singleton rectangle form or exposes the two reversed tight triples through b and c.

## Body

# Proof

The first clean subwalk gives
S_2=(S_0-{b}) union {a},
with b an endpoint of the chosen order on S_0, a occupying the same endpoint in S_2, and the entire order on S_0-{b} unchanged. Since edge S_0S_1 is labelled a, S_0 and S_1 partition V(H)-{a}. In particular b lies in S_0 and c lies in S_1, because the next clean subwalk removes c from S_1.

The clean subwalk S_1-S_2-S_3 gives
S_3=(S_1-{c}) union {b},
with c an endpoint of the chosen order on S_1, b replacing it at the same endpoint, and the order on S_1-{c} unchanged.

The clean subwalk S_2-S_3-S_4 has consecutive labels c,a, so
S_4=(S_2-{a}) union {c}=(S_0-{b}) union {c}.
Moreover a is the endpoint of S_2 introduced by the first clean swap; replacing it by c at the same end preserves the inherited order on S_0-{b}. Thus S_4 has the same large ordered block S_0-{b} as S_0, with c occupying the endpoint formerly occupied by b. Similarly S_3 has the same large ordered block S_1-{c} as S_1, with b occupying the endpoint formerly occupied by c.

Therefore
S_0∩S_3={b},
S_0∩S_4=S_0-{b},
S_1∩S_3=S_1-{c},
S_1∩S_4={c}.
All four intersections are nonempty. In the S_3 path the singleton b and the large block S_1-{c} are its two contiguous monochromatic blocks relative to S_0|S_1, so S_3 contributes exactly one crossing edge. Likewise S_4 contributes exactly one. Hence S_3|S_4 has crossing number exactly two across S_0|S_1. Conversely S_0 consists of endpoint singleton b plus the large block S_0-{b}=S_0∩S_4, and S_1 consists of endpoint singleton c plus S_1-{c}=S_1∩S_3, so S_0|S_1 has crossing number exactly two across S_3|S_4.

The two large intersection blocks inherit exactly the same orders in the two covers by the clean-swap construction, while singleton intersections have no order issue. Thus there is no intersection-order disagreement, and all hypotheses of astra004recrect hold with the singleton-cell case. Apply the certified astra004rectsingleton conclusion. ∎