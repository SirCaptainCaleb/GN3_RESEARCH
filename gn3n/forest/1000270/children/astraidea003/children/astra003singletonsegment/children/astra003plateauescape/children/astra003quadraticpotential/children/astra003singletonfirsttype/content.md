# Quadratic-minimal singleton states force first-type insertion obstructions

## Statement

Let C=B|Q|{x} be a three-component cover in an Astra-003 move component containing no two-cover, and suppose C minimizes the quadratic component-size potential Phi. If B has order m>=3, then the failed-insertion normal form for x into the displayed order of B cannot be of the second type; hence it has a first-type comparison 3-cycle. The same holds for Q whenever |Q|>=3.

## Body

# Singleton components at a quadratic minimum

Let
[
C=B|Q|{x}
]
be a spanning three-component cover in a connected component of the Astra-003 move graph containing no cover with at most two components. Assume (C) minimizes
[
Phi(C)=sum |P_i|^2
]
in that move component.

Write
[
B=(b_1,ldots,b_m),qquad mge3.
]
The vertex (x) cannot be inserted anywhere into the displayed order of (B), since such an insertion would merge (B) with the singleton ({x}) and, together with (Q), give a spanning two-cover.

Apply the certified local failed-insertion normal form from insert01. Suppose its second alternative holds at an index (1le tle m-1). With
[
e_i={b_i,b_{i+1}},qquad f_i={x,b_i},
]
that alternative gives (e_{t-1}	o f_t) when (t>1), so
[
(b_1,ldots,b_t,x)
]
is a tight path; for (t=1) this is just the two-vertex path ((b_1,x)). Likewise (f_{t+1}	o e_{t+1}) when (t<m-1), so
[
(x,b_{t+1},ldots,b_m)
]
is a tight path; for (t=m-1) this is the two-vertex path ((x,b_m)).

Consequently the union (V(B)cup{x}) has each of the exact two-path covers
[
(b_1,ldots,b_t,x)mid(b_{t+1},ldots,b_m)
]
and
[
(b_1,ldots,b_t)mid(x,b_{t+1},ldots,b_m).
]
At least one of these has both component orders at least (2): use the first cover when (t<m-1), and the second when (t=m-1). Since their total order is (m+1), such a cover has size imbalance at most (m-3), strictly smaller than the imbalance (m-1) of the displayed split (Bmid{x}).

Equivalently, replacing (Bmid{x}) by that exact two-cover strictly lowers the quadratic potential, contradicting the assumed minimality of (C).

Therefore the second failed-insertion alternative is impossible. The local obstruction for inserting (x) into (B) must be of the first type:
[
f_t	o e_{t-1}	o e_t	o f_t
]
for some (2le tle m-1).

The argument is symmetric for (Q). Hence a quadratic-minimal trapped three-cover with a singleton component and both other components of order at least three forces first-type insertion obstructions on both large components.

This sharply narrows the possible singleton minima. In the minimum-counterexample setting, transport01 classifies each such first-type window as either a Hamiltonian four-window or the exceptional cyclic four-kernel, so the next step is to couple the two forced first-type windows across the common singleton label.
