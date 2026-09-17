# Positive pair-partition disagreement amplifies to a fixed-witness star fan

**Workspace:** D17
**State:** working
**Key:** `pair-disagreement-star`

**Summary:** A complete combinatorial amplification of the pair-deletion Phi objective: if one physical pair {u,v} has nonconstant same-block status across deletion pairs, then some fixed deleted vertex p supports a complete bipartite fan of at least n-4 adjacent conflicting fibers {p,a},{p,b}, all witnessed by the same {u,v}. This identifies a canonical multi-fiber repair region.


Let a family of pair-deletion partitions pi_D be chosen as in the partition-rigidity section, and fix a physical pair {u,v}. Put U=V-{u,v}, N=|U|=n-2. For every deletion pair D in binom(U,2), define

  f(D)=1 if u,v are in the same pi_D block, and f(D)=0 otherwise.

The {u,v}-contribution to Phi is exactly the number of adjacent pairs D,E in the Johnson graph J(U,2) for which f(D) != f(E). Thus this physical pair contributes positively iff f is nonconstant.

If f is nonconstant, there is a vertex p in U for which the values f({p,a}), a in U-{p}, are not all equal. Indeed, if every p-star were constant, write c_p for its value. For any distinct p,q we would have c_p=f({p,q})=c_q, so all c_p and hence all values of f would be equal, contradiction.

Fix such a mixed p and split U-{p}=A sqcup B by

  A={a: f({p,a})=0},   B={b: f({p,b})=1}

(after exchanging labels if desired). Both A and B are nonempty. For every a in A and b in B, the deletion pairs

  D={p,a},   E={p,b}

are adjacent, have common surviving pair {u,v}, and disagree on its same-block status. Hence every cross pair A x B is an actual Phi-conflict edge, all sharing the same deleted vertex p and the same physical witness pair {u,v}. The number of such conflicts is

  |A||B| >= N-2 = n-4,

with equality only when one star color has size one.

Therefore a positive Phi minimum cannot be treated as an isolated bad edge. For at least one fixed witness pair {u,v}, it contains a complete bipartite conflict fan in the p-star of the pair-deletion graph. This is the natural unit for any simultaneous repair: changing the minority family {p,a}, a in A, to the opposite {u,v}-status would remove |A||B| witness disagreements at once, though collateral disagreements for other physical pairs and neighboring stars must still be counted.

Combining this with `codimension-one-coherence` gives a sharper source classification for the fan. For each cross edge {p,a}--{p,b}, either the exchanged-vertex trims expose an actual selected crossing on the common triple-deletion residue, or the edge is doubly hidden and lifts to two explicit exact covers of H-p with a/b endpoint-internal roles swapped. If all cross edges in a large fan are hidden, then one fixed singleton residue H-p carries a large family of such swapped-exposure currentizations, all arising from the same physical witness pair {u,v}; if many are visible, one obtains a large source-labelled crossing fan instead. Either alternative is considerably more synchronized than an arbitrary collection of pair births.

Status: the star-amplification statement and its count are complete elementary arguments. No theorem is claimed that the minority star can actually be flipped without collateral cost; that is the remaining multi-fiber repair problem.


## References

```json
[
    {
        "relation": "related",
        "revision_id": "R408"
    }
]
```
