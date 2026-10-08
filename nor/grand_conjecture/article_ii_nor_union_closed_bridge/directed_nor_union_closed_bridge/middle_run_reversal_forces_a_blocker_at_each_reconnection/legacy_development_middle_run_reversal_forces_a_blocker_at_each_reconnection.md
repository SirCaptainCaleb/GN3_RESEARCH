# Middle run reversal forces a blocker at each reconnection — preserved pre-item development

## Development

## Middle-run reversal forces a blocker at each reconnection

Work in directed ternary NOR. Let
[
S=(v_0,ldots,v_{n-1})
]
be a spanning coordinate order whose linear status word has exactly two changes,
[
sigma^{a}	au^{b}sigma^{c},
qquad 	au=1-sigma,
]
with
[
age2,qquad bge1,qquad cge2.
]

Let the middle (	au)-run consist of statuses
[
c_L,ldots,c_R,
qquad c_i=h(v_i,v_{i+1},v_{i+2}),
]
so (R-L+1=b). Reverse the full vertex interval
[
I=(v_L,v_{L+1},ldots,v_{R+2}).
]

Every status wholly internal to (I) is the reverse of an old (	au)-status and therefore has color (sigma). Every status whose window lies wholly outside (I) is unchanged and also has color (sigma). Thus after reversal the only statuses that may differ from (sigma) are the four reconnection statuses.

Write the local order before reversal as
[
ldots,p,a,x_1,ldots,x_m,b,q,ldots
]
with (I=(x_1,ldots,x_m)). The four new boundary statuses are
[
alpha=h(p,a,x_m),qquad
eta=h(a,x_m,x_{m-1}),
]
[
gamma=h(x_2,x_1,b),qquad
delta=h(x_1,b,q).
]

Because (a,cge2), the status immediately before (alpha), the internal status immediately after (eta), the internal status immediately before (gamma), and the status immediately after (delta) all have color (sigma).

Hence the cyclic variation of the reversed full-support order is the sum of the contributions of two disjoint local strings
[
sigma,alpha,eta,sigma
qquad	ext{and}qquad
sigma,gamma,delta,sigma.
]
Each local contribution is even and is either (0) or (2). It is (0) exactly when both middle entries equal (sigma).

In a counterexample every cyclic coordinate order has variation at least four, since a cyclic order of variation at most two can be cut to a spanning linear order with at most one change. Therefore both reconnection zones must contribute exactly two. Equivalently,
[
(alpha,eta)
e(sigma,sigma),
qquad
(gamma,delta)
e(sigma,sigma).
]

### Consequence

Reversing the middle run of any spanning two-change order cannot fail globally for a diffuse reason. Counterexamplehood forces a local blocker at **each** end of the reversed run: among the two new windows at each reconnection, at least one has the opposite color (	au).

Thus a depth-two alternating peeling, or any other spanning (sigma-	au-sigma) certificate, canonically produces two separated local blockers. The next closure target is to vary the endpoint realization of the middle tight run. If one can choose its first or last two vertices so that both new windows at one reconnection are (sigma), the middle reversal immediately gives cyclic variation at most two and closes NOR. Otherwise the persistent blocker conditions should impose rigid tournament inequalities analogous to the front-circuit insertion blockers.
