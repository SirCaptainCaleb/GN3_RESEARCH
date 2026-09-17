# Path-cover surgery lemmas

**Status: GN3 AUDIT PASS.**

These statements are GN3 rewrites of selected reusable A7C3 spare parts. The exact current text has passed independent GN3 audit; legacy acceptance is provenance only.

## 1. Crossing forced by an absorbable deletion

Let `H` be a boundary tournament with `pc(H)>2`. Let `D` be a nonempty proper subset of `V(H)`, put `W=V(H)-D`, and let `S` be a nonempty proper subset of `W`. Suppose `H[D union S]` has a Hamilton tight path.

Then every exact two-path cover of `H-D` contains an ordinary path edge with one endpoint in `S` and the other in `W-S`.

**Proof.** Let `T_1|T_2` be an exact two-path cover of `H-D` and suppose no ordinary edge of either path crosses the cut `S | (W-S)`. Then each connected path component lies wholly in one side of the cut. Since both sides are nonempty and the two paths cover `W`, after exchanging their names we have

`V(T_1)=S`, `V(T_2)=W-S`.

A Hamilton tight path on `D union S`, together with `T_2`, is then a spanning two-path cover of `H`, contradicting `pc(H)>2`. ∎

## 2. Cyclic rotations of a tight path

Let `P=(p_0,p_1,...,p_r)` be a tight path in a boundary tournament, with `r>=2`. Put

`alpha=(p_r,p_0,p_1)`, `beta=(p_{r-1},p_r,p_0)`.

Then the cyclic rotation

`(p_r,p_0,p_1,...,p_{r-1})`

is tight exactly when `alpha` is tight, and

`(p_1,...,p_r,p_0)`

is tight exactly when `beta` is tight. Consequently exactly one of the following four possibilities occurs:

1. both rotations are tight, in which case `(p_0,p_1,...,p_r,p_0)` is a tight cycle;
2. only the first rotation is tight, and `(p_0,p_r,p_{r-1})` is tight;
3. only the second rotation is tight, and `(p_1,p_0,p_r)` is tight;
4. neither rotation is tight, and both `(p_1,p_0,p_r)` and `(p_0,p_r,p_{r-1})` are tight. If `r>=3`, then `(p_1,p_0,p_r,p_{r-1})` is a tight four-vertex path.

**Proof.** Each rotation preserves every old consecutive triple of `P` except its one displayed wrap triple. Thus the two equivalences are immediate. Boundary antisymmetry gives the reverse of each failed wrap triple, and when both fail and `r>=3` the two reversed triples concatenate. ∎

## 3. Opposite orientations of one end edge absorb every exterior vertex

Let `X` be a vertex set in a boundary tournament, and let `u,v` be distinct vertices of `X`. Suppose `H[X]` has a Hamilton tight path beginning with `(u,v)` and also a Hamilton tight path ending with `(v,u)`.

Then for every `d outside X`, the induced tournament `H[X union {d}]` is Hamiltonian.

**Proof.** Exactly one of `(d,u,v)` and `(v,u,d)` is tight. In the first case prepend `d` to the Hamilton path beginning with `(u,v)`; in the second append `d` to the Hamilton path ending with `(v,u)`. ∎

## 4. Component count after a path-cover edge exchange

Let a spanning tight-path cover on `n` vertices have `q` components, so its ordinary path forest has `n-q` edges. Delete `a` ordinary edges and insert `b` ordinary edges. Suppose the resulting spanning ordinary graph has only path components and cycle components, and that every component carries the corresponding tight path or tight cycle order. Let `c` be the number of cycle components.

Opening each cycle by deleting one of its ordinary cycle edges gives a spanning tight-path cover with

`q' = q-(b-a)+c`

components.

**Proof.** After the exchange there are `n-q-a+b` ordinary edges. Opening the `c` cycles leaves `n-q-a+b-c` edges. A spanning path forest with `q'` components has `n-q'` edges, so

`n-q'=n-q-a+b-c`,

which rearranges to the formula. ∎

## 5. Two-ended Hamilton splice

Let `X,Y` partition `V(H)`, and suppose `Y` has an exact two-path cover

`U=(x,u_1,...,u_r)`, `V=(v_0,...,v_{s-1},y)`

with `r,s>=0`. Suppose `X` is nonempty and `H[X union {x,y}]` has a Hamilton tight path

`Q=(y,q_1,...,q_t,x)`.

Form the spanning vertex order

`K=(v_0,...,v_{s-1},y,q_1,...,q_t,x,u_1,...,u_r)`,

omitting an empty residual prefix or suffix. Every consecutive triple of `K` is tight except possibly

`alpha=(v_{s-1},y,q_1)` when `s>=1`,

and

`beta=(q_t,x,u_1)` when `r>=1`.

If `pc(H)>1`, at least one existing one of `alpha,beta` is not tight. If `pc(H)>2`, then `r,s>=1` and neither `alpha` nor `beta` is tight. Hence in the latter case both

`(q_1,y,v_{s-1})`, `(u_1,x,q_t)`

are tight.

**Proof.** All triples wholly inside the residual part of `V`, inside `Q`, or inside the residual part of `U` are already tight, so the displayed triples are the only possible failures.

If all existing attachment triples were tight, `K` would be a Hamilton tight path, contradicting `pc(H)>1`.

Now suppose `pc(H)>2`. If `K` had at most one non-tight consecutive triple, then cutting `K` at one of the two ordinary edges inside that triple would split `K` into two nonempty tight paths covering all vertices. Thus `H` would have a spanning two-path cover. Therefore `K` has at least two non-tight consecutive triples. Since only `alpha,beta` can fail, both must exist and both must fail. Boundary antisymmetry gives their reverses. ∎

## 6. Transitions across a vertex partition

Let `Pi={X_1,...,X_m}` be a partition of `V(H)` into nonempty sets, and let `T` be a spanning exact `q`-path cover. Let `t_Pi(T)` be the number of ordinary edges of the paths of `T` whose endpoints lie in different classes of `Pi`.

For each `i`, delete all such cross-class edges and let `b_i(T)` be the number of resulting nonempty path blocks contained in `X_i`. Then

`t_Pi(T)=sum_i b_i(T)-q`

and hence

`t_Pi(T) >= sum_i pc(H[X_i])-q`.

Equality holds exactly when the blocks inside every `X_i` form a minimum path cover of `H[X_i]`.

**Proof.** Deleting one cross-class edge from a path forest increases the number of components by one. Thus all deletions produce exactly `q+t_Pi(T)` blocks, which is `sum_i b_i(T)`. Since the blocks in `X_i` form a path cover of `H[X_i]`, we have `b_i(T)>=pc(H[X_i])`. The inequality and equality condition follow. ∎

## 7. Deletion block count and a unique crossing

Let

`V(H)=D disjoint-union S disjoint-union C`,

where `S,C` are nonempty. Suppose `H[D union S]` has a path cover with `a` components. Let `T` be a `k`-path cover of `H-D`. For each component of `T`, cut every ordinary edge with one endpoint in `S` and the other in `C`, and let `b_C(T)` be the total number of nonempty resulting blocks contained in `C`.

Then

`pc(H) <= a+b_C(T)`.

In particular, if `H[D union S]` is Hamiltonian and `pc(H)>k`, then `b_C(T)>=k`.

Under these latter hypotheses, if `T` has exactly one ordinary edge joining `S` to `C`, then exactly one component of `T` meets both sets. That component consists of one nonempty `S`-block followed by one nonempty `C`-block, or vice versa; every other component of `T` lies wholly in `C`.

Assume now that `H` is a boundary tournament and keep these latter hypotheses. If the unique crossing edge occurs in the order `x,y` with `x in S` and `y in C`, then for every Hamilton tight path of `H[D union S]` ending with the ordered pair `(p,x)`, the triple

`(y,x,p)`

is tight. Dually, if the unique crossing occurs in the order `y,x`, then for every Hamilton tight path of `H[D union S]` beginning with `(x,p)`, the triple

`(p,x,y)`

is tight.

**Proof.** After cutting all `S-C` edges of `T`, the `C`-blocks are disjoint tight paths covering `C`. Together with the given `a`-path cover of `D union S`, they form a spanning path cover of `H`, proving `pc(H)<=a+b_C(T)`.

If `a=1` and `pc(H)>k`, then `pc(H)>=k+1`, so `b_C(T)>=k`. If there is exactly one `S-C` edge in `T`, cutting it produces exactly `k+1` monochromatic blocks. There is at least one `S`-block and at least `k` `C`-blocks, so there is exactly one `S`-block and exactly `k` `C`-blocks. The asserted form of `T` follows.

Suppose the unique crossing is `x,y` with `x in S`, `y in C`, and let `Q` be a Hamilton path of `H[D union S]` ending with `(p,x)`. Replace the unique `S`-block of the mixed component of `T` by `Q`, leaving the adjacent `C`-block and every other component unchanged. If `(p,x,y)` were tight, these `k` paths would cover `H`, contradicting `pc(H)>k`. Hence `(p,x,y)` is not tight, so boundary antisymmetry gives `(y,x,p)`. The other orientation is identical after reversing the role of the splice. ∎

## Legacy provenance

Sections 1–7 rewrite, respectively, A7C3 spare parts `S9003`, `S9004`, `S9005`, `S9006`, `S9009`, `S9013`, and the reusable content of `S9033`.