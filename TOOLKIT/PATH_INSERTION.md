# Path insertion and endpoint replacement lemmas

## 1. Two-sided endpoint replacement forces reversed order

Let `H` be a boundary tournament. Let

`Q=(q_0,q_1,...,q_r)`, `r>=2`,

be a Hamilton tight path of `H[X]` on a vertex set `X subseteq V(H)`, and let `y in V(H)-X`. Suppose `H[X union {y}]` is non-Hamiltonian. Assume nevertheless that there is

- a Hamilton tight path `L` on `(X-{q_0}) union {y}`, and
- a Hamilton tight path `R` on `(X-{q_r}) union {y}`.

Then at least one of the three pairs

`(Q,L)`, `(Q,R)`, `(L,R)`

has two common vertices occurring in different relative orders.

Consequently `PATH_FORESTS_AND_INTERSECTIONS.md` Section 4 applies to at least one of these pairs and yields a reversed common edge, a tight triple reversing an ordered edge at an intersection, or a vertex-simple tight cycle.

**Proof.** Suppose every pair has its common vertices in the same relative order.

The common vertices of `Q` and `L` are `q_1,...,q_r`, so `L` is obtained by inserting `y` into that displayed order. If `y` were not in one of the first two positions, then `L` would begin with `(q_1,q_2)`, and prepending `q_0` would give a Hamilton tight path on `X union {y}`. Hence

`L=(y,q_1,...,q_r)`

or

`L=(q_1,y,q_2,...,q_r)`.

Similarly, comparison of `Q` with `R` shows that

`R=(q_0,...,q_{r-1},y)`

or

`R=(q_0,...,q_{r-2},y,q_{r-1})`.

Compare these four possible pairs. The first form of `L` and the first form of `R` put `y` and `q_1` in opposite orders. The first form of `L` with the second form of `R` does the same when `r>=3`; when `r=2` it gives the tight Hamilton path

`(q_0,y,q_1,q_2)`.

The second form of `L` with the first form of `R` puts `y` and `q_2` in opposite orders when `r>=3`; when `r=2` it gives

`(q_0,q_1,y,q_2)`.

Finally, the second form of `L` with the second form of `R` puts `y` and `q_2` in opposite orders when `r>=4`; for `r=2`, the common vertices `q_1,y` occur in opposite orders; and for `r=3` the two paths combine to

`(q_0,q_1,y,q_2,q_3)`.

Thus either some pair reverses the order of common vertices or `X union {y}` is Hamiltonian. The latter is excluded. ∎

## 2. Barrier gaps for a noninsertable vertex in an increasing path

Let `G` be an edge-ordered complete graph and let

`Q=(q_0,...,q_m)`, `m>=1`,

be an increasing path. Let `x` be a vertex outside `Q`. For `0<=i<=m-1`, call the gap between `q_i,q_{i+1}`

- **left-feasible** if `i=0` or `q_{i-1}q_i < q_i x`;
- **right-feasible** if `i=m-1` or `xq_{i+1} < q_{i+1}q_{i+2}`.

Assume insertion of `x` between `q_i,q_{i+1}` never gives an increasing path.

Then some gap is both left- and right-feasible, and at every such gap

`xq_{i+1} < xq_i`.

Let `beta(x)` be the least right-feasible gap. Then `beta(x)` is also left-feasible and

`xq_{beta(x)+1} < xq_{beta(x)}`.

Moreover, if `x,y` are two such noninsertable vertices and `beta(x)<beta(y)`, then, with `i=beta(x)`,

`xq_{i+1} < q_{i+1}q_{i+2} < yq_{i+1}`.

Define the boundary tournament `H_G` on `V(G)` by declaring

`(u,v,w)` tight exactly when `uv<vw`.

Then the displayed inequalities imply that

`(x,q_{i+1},y)`

is tight in `H_G`.

**Proof.** Put `e_i=q_iq_{i+1}`. Let `L_0` be true and, for `i>=1`, let `L_i` mean `e_{i-1}<q_i x`. Let `R_{m-1}` be true and, for `i<=m-2`, let `R_i` mean `xq_{i+1}<e_{i+1}`.

If no gap satisfied both `L_i` and `R_i`, then `L_0` would force `R_0` to fail. Whenever `L_i` holds and `R_i` fails, we have

`e_i<e_{i+1}<xq_{i+1}`,

so `L_{i+1}` holds. Induction gives `L_{m-1}`, contradicting the automatic truth of `R_{m-1}`. Hence some gap is left- and right-feasible.

At such a gap all comparisons needed for insertion are correct except possibly the comparison of the two edges `q_i x` and `xq_{i+1}`. Since insertion fails, totality of the edge order gives

`xq_{i+1}<q_i x`.

For `beta(x)`, every earlier `R_j` fails. The same propagation from `L_0` gives `L_{beta(x)}`, so the displayed inequality follows.

Finally let `beta(x)=i<beta(y)`. Right-feasibility of `x` gives

`xq_{i+1}<e_{i+1}`,

while minimality of `beta(y)` makes `R_i(y)` false, hence

`e_{i+1}<yq_{i+1}`.

By the definition of `H_G`, the comparison `xq_{i+1}<q_{i+1}y` is exactly the tightness of `(x,q_{i+1},y)`. ∎

## 3. Local obstruction when every insertion position fails

Let `H` be a boundary tournament. Let

`B=(b_1,...,b_m)`, `m>=2`,

be a tight path in `H`, and let `x in V(H)-V(B)`. In the comparison digraph `Gamma(H)` put

`e_i={b_i,b_{i+1}}` for `1<=i<=m-1`,

`f_i={x,b_i}` for `1<=i<=m`.

Assume that inserting `x` in every one of the `m+1` positions of the displayed order of `B` fails to give a tight path. Then for some `1<=t<=m-1`, one of the following occurs.

1. `2<=t<=m-1` and

   `f_t -> e_{t-1} -> e_t -> f_t`.

2. The following arcs hold:

   `e_t -> f_t`,

   `f_{t+1} -> f_t`,

   together with `e_{t-1}->f_t` when `t>1`, and `f_{t+1}->e_{t+1}` when `t<m-1`. When `t=m-1`, the failed final insertion additionally gives

   `f_m -> e_{m-1}`.

Every displayed arc in either alternative involves only `x` together with at most four consecutive vertices of `B`.

**Proof.** Failure of the insertion at the left end gives `e_1->f_1`, while failure at the right end gives `f_m->e_{m-1}`.

If some `t<=m-2` satisfies `f_{t+1}->e_{t+1}`, choose the least such `t`; otherwise put `t=m-1`. For `t=1`, the left-end failure gives `e_t->f_t`. For `t>1`, minimality says `f_t->e_t` does not hold, so boundary antisymmetry gives `e_t->f_t`.

If `t>1` and `f_t->e_{t-1}`, then tightness of `B` gives `e_{t-1}->e_t`, producing alternative 1. Otherwise `e_{t-1}->f_t` whenever `t>1`.

Suppose first that `t<m-1`. By construction `f_{t+1}->e_{t+1}`. If `f_t->f_{t+1}`, then all comparisons needed to insert `x` between `b_t,b_{t+1}` would point forward:

`e_{t-1}->f_t->f_{t+1}->e_{t+1}`,

with the first comparison omitted when `t=1`. This contradicts failed insertion, so `f_{t+1}->f_t`.

If `t=m-1`, the same argument uses the arc `f_m->e_{m-1}` supplied by failure of the right-end insertion. When the predecessor comparison exists and does not form alternative 1, failed middle insertion forces `f_m->f_{m-1}`. The case `m=2` is the same with no predecessor edge. Thus alternative 2 holds. ∎

## 4. Opposite extensions of one ordered pair concatenate

Let `a,b,x,y` be distinct vertices of a boundary tournament.

If

`(x,a,b)` and `(a,b,y)`

are tight, then

`(x,a,b,y)`

is a tight path. Likewise, if

`(y,a,b)` and `(a,b,x)`

are tight, then

`(y,a,b,x)`

is a tight path.

Two left extensions of `(a,b)`, or two right extensions of `(a,b)`, do not by themselves imply a four-vertex path; the useful automatic conclusion is the opposite-end concatenation above.
