# Every complement-deletion Hamilton path in the uniform layer carries two forced endpoint-edge shields

**Workspace:** D17
**State:** established
**Key:** `uniform-middle-layer-endpoint-jet-shields`

**Summary:** In the R927 uniform residue, fix any Hamilton k-path Q=(q0,...,q{k-1}) and its (k+1)-vertex complement W. For every z in W and every Hamilton order K=(x1,...,xk) of W-z, the failed reversed-boundary splices force (x2,x1,q0) and (q{k-1},xk,x{k-1}) tight. Thus q0 and q{k-1} cap the reversed source and terminal boundary dimers of every Hamilton deletion path of W. The natural retained coordinate is an endpoint 1-jet, meaning an endpoint together with its selected neighbor/boundary dimer. No closure of the uniform branch is claimed.

### 1. Setup and universal outer reversals

Work in the uniform middle-layer residue of accepted R927: `|V(H)|=2k+1`, every `k`-set is Hamiltonian, and no `(k+1)`-set is Hamiltonian. The case `k=2` is already impossible by R3 on a three-set, so assume `k>=3`.

Fix any `k`-set `X` and retain any actual Hamilton order

`Q=(q_0,q_1,...,q_{k-1})`.

Put `W=V(H)-X`, so `|W|=k+1`. For each `y in W`, non-Hamiltonicity of `X+{y}` forbids both one-vertex extensions of this literal Q order. Hence

`(y,q_0,q_1)` and `(q_{k-2},q_{k-1},y)` are bad.

By R3 their exact reversals are tight:

`(q_1,q_0,y)`,
`(y,q_{k-1},q_{k-2})`.                              (UJ.1)

These are universal in `y`.

### 2. Every Hamilton deletion path of W is source-shielded

Fix arbitrary `z in W`. By uniform k-set Hamiltonicity, `W-{z}` has an actual Hamilton order. Retain an arbitrary one,

`K=(x_1,x_2,...,x_k)`.

Equation (UJ.1) with `y=x_1` gives `(q_1,q_0,x_1)` tight. Consider the only remaining junction turn needed to prepend the reversed Q-boundary dimer to K:

`(q_0,x_1,x_2)`.

If this turn were tight, then

`(q_1,q_0,x_1,x_2,...,x_k)`

would be a vertex-simple tight path on `k+2` vertices. Any contiguous `k+1` vertices of it would be a Hamilton tight path on a `(k+1)`-set, contradicting the uniform residue. Therefore `(q_0,x_1,x_2)` is bad. R3 on the same three physical vertices forces the exact reverse

`(x_2,x_1,q_0)` tight.                                  (UJ.2)

Thus the reversed source boundary dimer `(x_2,x_1)` of EVERY actual Hamilton deletion path K on W continues to the fixed physical vertex `q_0`.

### 3. The terminal dual is simultaneous

At the other end, (UJ.1) with `y=x_k` gives `(x_k,q_{k-1},q_{k-2})` tight. The only additional turn needed to append the reversed terminal Q-boundary dimer after K is

`(x_{k-1},x_k,q_{k-1})`.

If it were tight, then

`(x_1,...,x_k,q_{k-1},q_{k-2})`

would again be a tight `(k+2)`-path and contain a forbidden tight `(k+1)`-subpath. Hence that seam is bad, and R3 yields

`(q_{k-1},x_k,x_{k-1})` tight.                           (UJ.3)

So EVERY Hamilton deletion path K on W is simultaneously shielded at both ends by the two fixed boundary vertices `q_0,q_{k-1}` of the retained Q order.

### 4. Endpoint 1-jets are the correct retained coordinate

The output depends essentially on the immediate endpoint neighbors `x_2` and `x_{k-1}`. Endpoint identity alone does not determine the obstruction. For this purpose call

`(x_1;x_2)` the source endpoint 1-jet of K, and `(x_k;x_{k-1})` its terminal endpoint 1-jet.

Then (UJ.2)-(UJ.3) say that all source 1-jets of all Hamilton deletion paths of W are capped by `q_0` after reversing their selected boundary dimer, and all terminal 1-jets are capped by `q_{k-1}` in the dual orientation. This is a support-wide family statement, not a property of one chosen Hamilton representative.

The all-endpoint Hall representation records endpoint-deletion cores and opposite endpoint ports; it does not by itself retain these immediate endpoint neighbors. Any consumer of this section should therefore preserve the 1-jet data while using Hall circuits, port switches, pair switches, or rigid common-core bicycles. In particular, two Hamilton representatives that share an endpoint but expose different first neighbors produce two distinct same-dimer witness certificates against the same fixed q-boundary and should be compared before projecting down to endpoint-only Hall data.

### 5. Output and limitation

The uniform R927 branch remains open. The exact new output is the TWO-SIDED ENDPOINT-JET SHIELD SYSTEM (UJ.2)-(UJ.3), simultaneously for every Hamilton k-path Q, every complement deletion z, and every actual Hamilton order on W-z.

A natural next consumer is a lifted endpoint-Hall argument on flagged endpoint 1-jets: either the jet varies and creates repeated-witness/order geometry on a fixed boundary dimer, or jet-rigidity sharply strengthens the existing rigid-bicycle alternative. No such global consumer is claimed here.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "conditional_dependency",
        "revision_id": "R927"
    }
]
```
