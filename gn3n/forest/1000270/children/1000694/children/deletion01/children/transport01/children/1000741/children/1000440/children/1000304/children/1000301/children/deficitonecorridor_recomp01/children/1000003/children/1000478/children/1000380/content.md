# Corridor order reduces fixed-core five-path synchronization to ten templates

## Statement

In the setting of 958c45ed8d1c, put d_0=floor((r-1)/2). Then either explicit order disagreement already occurs, or there exist x in E, a set W subseteq E-{x} lying entirely on one side of x in the displayed E-order, and one common five-vertex order template such that |W|>=ceil(ceil(d_0/2)/10) and for every w in W that template, with w in its placeholder position, is a Hamilton tight order of D union {x,w}. Consequently either (1) the placeholder is an endpoint, so deleting it leaves one fixed Hamiltonian order R of D union {x} and every w in W extends R at that same endpoint, or (2) the placeholder is internal, so there are fixed distinct a,b in D union {x} with (a,w,b) tight for every w in W. Thus in the no-order-disagreement branch the synchronized family may be chosen one-sided along the corridor and with a ten-template rather than 120-template loss.

## Body

Use the fixed tight core D and Hamiltonicity graph G_D(E) from 958c45ed8d1c. There is x in E with degree d>=d_0=floor((r-1)/2). Split N(x) according to the displayed C-order into vertices preceding x and vertices following x. One side U has order at least ceil(d/2)>=ceil(d_0/2).

For each w in U choose a Hamilton tight order P_w on D union {x,w}. If P_w orders two vertices of D differently from their displayed order in A, then P_w and A have order disagreement. If P_w orders x,w differently from their displayed order in C, then P_w and C have order disagreement. Hence, unless explicit order disagreement already occurs, every chosen P_w preserves the fixed three-term D-order and the fixed two-term x,w order (the latter is common throughout U because U lies on one side of x).

An order of five symbols preserving a fixed three-chain and a fixed two-chain is a shuffle of those two chains, so there are exactly binomial(5,2)=10 possible templates after replacing w by a placeholder. Pigeonhole gives W subseteq U of order at least ceil(|U|/10)>=ceil(ceil(d_0/2)/10) on which one template is constant.

If the placeholder is first or last in this template, deleting it leaves a fixed four-vertex tight path R on D union {x}; every w in W extends R at that same endpoint. If the placeholder is internal, its two neighboring symbols a,b belong to D union {x} and are fixed by the template, while tightness of P_w gives (a,w,b) for every w in W. These are exactly the two stated synchronized forms.
