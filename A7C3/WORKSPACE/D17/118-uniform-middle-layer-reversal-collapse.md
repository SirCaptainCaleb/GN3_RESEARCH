# Failed one-seam reversal splice in the uniform middle layer

**Workspace:** D17
**State:** working
**Key:** `uniform-middle-layer-reversal-collapse`

**Summary:** CORRECTION: the proposed elimination of the R927 uniform middle-layer alternative was invalid. Prepending x to Q and reversing its failed seam does certify (q1,q0,x), but concatenating the reversed dimer (q1,q0) with a Hamilton complement path K=(x,k2,...) requires a second boundary turn (q0,x,k2), which was omitted. Under the no-(k+1)-path hypothesis that second turn is actually forced bad by the failed prepend (q0,x,k2,...). Thus no P_{k+2} is obtained and the R927 uniform branch remains live.

### Correction: the proposed uniform-layer collapse is invalid

A previous version of this section claimed that the R927 uniform residue was impossible by a short exact-reversal splice. That proof omitted one boundary turn and is invalid.

Retain the attempted setup. Let `Q=(q_0,q_1,...,q_{k-1})` be a Hamilton `k`-path on `X`, let `W` be disjoint, and let

`K=(x,k_2,...,k_k)`

be a Hamilton `k`-path on a support in `W`. If `X+{x}` is non-Hamiltonian, the prepend proposal

`(x,q_0,q_1,...,q_{k-1})`

fails at its only new turn, so R3 correctly gives

`(q_1,q_0,x)` tight.                                      (UM.F1)

The erroneous step was to assert that the word

`(q_1,q_0,x,k_2,...,k_k)`

was therefore tight. Concatenating a dimer `(q_1,q_0)` with a path beginning `(x,k_2,...)` requires **two** boundary turns:

`(q_1,q_0,x)` and `(q_0,x,k_2)`.

Only the first is certified by (UM.F1). The second is not inherited from `K`.

Worse, in the uniform residue the second turn is forced the wrong way. If `(q_0,x,k_2)` were tight, then

`(q_0,x,k_2,...,k_k)`

would itself be a tight path on `k+1` vertices. Therefore `(q_0,x,k_2)` is bad, and R3 gives the reverse turn `(k_2,x,q_0)` tight. The attempted splice is thus blocked exactly at its omitted seam.

Consequently this argument does **not** eliminate the uniform middle-layer alternative of R927 and does not prove that every smallest counterexample has a universal source crossing. All downstream attention must continue to treat both R927 branches as live unless another valid theorem closes the uniform branch.

The failed calculation is retained as a useful two-seam fence: exact reversal supplies the outer seam of the attempted dimer-to-path splice, while longestness/nonextension reverses the inner seam in the opposite direction. Any successful reversal-based uniform-layer consumer must overcome this paired seam obstruction rather than counting only the first boundary turn.

Status: corrected working limitation. No mathematical conclusion from the previous version SV18559 is usable.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "comparison",
        "revision_id": "R927"
    }
]
```
