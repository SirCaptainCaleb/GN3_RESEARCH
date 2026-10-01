# The order-four fixed-path endpoint-triangle constraints are locally consistent

## Statement

There exists a seven-vertex boundary tournament on Q={q0,q1,q2,q3} and labels {a,b,c} such that Q=(q0,q1,q2,q3) is tight, (c,b,a),(a,c,b),(b,a,c) are tight, and each of Q∪{a}, Q∪{b}, Q∪{c}, Q∪{a,b}, Q∪{a,c}, Q∪{b,c} is non-Hamiltonian. Hence the order-four fixed-path branch of an endpoint-compatible deletion triangle cannot be eliminated from the induced seven-vertex data alone; any contradiction must use attachment to the ambient common path or other global minimum-counterexample structure.

## Body

An exact bounded MILP feasibility check produces the following explicit boundary tournament certificate.

Order the vertices as
q0,q1,q2,q3,a,b,c.
For each middle vertex m in this order, and then each unordered endpoint pair u<w in lexicographic order among the other six vertices, use one reversal-pair bit. Bit 1 means the ordered triple (u,m,w) is tight, while bit 0 means its reverse (w,m,u) is tight. This gives 105 bits. Left-pad by three zero bits to a multiple of four. The hexadecimal word is

1f003ffc03f8000180070006001.

Direct exact verification of this orientation gives:
- (q0,q1,q2) and (q1,q2,q3) tight, so Q is a tight four-path;
- (c,b,a), (a,c,b), and (b,a,c) tight;
- zero Hamilton tight-path orders on each of the three five-sets Q∪{a}, Q∪{b}, Q∪{c};
- zero Hamilton tight-path orders on each of the three six-sets Q∪{a,b}, Q∪{a,c}, Q∪{b,c}.

The verification is finite: each five-set has 5!=120 orders and each six-set has 6!=720 orders. The feasibility model used one binary variable for every reversal pair and, for every candidate Hamilton ordering of the six constrained induced sets, imposed the clause that at least one consecutive triple is non-tight. There were 105 binary variables and 2525 linear constraints including the five prescribed tight triples.

Thus the natural seven-vertex local consequences of an endpoint-compatible triangle with a four-vertex fixed path are mutually consistent. In particular, the facts that Q plus every one or two labels is non-Hamiltonian, together with the cyclic label orientation, do not themselves force a contradiction. Any proof excluding this branch must use the ambient common path R, deletion-cover compatibility outside these seven vertices, or another genuinely global condition.
