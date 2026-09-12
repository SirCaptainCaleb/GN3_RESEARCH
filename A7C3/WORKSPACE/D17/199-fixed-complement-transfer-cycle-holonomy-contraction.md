# An all-transfer endpoint-return cycle contracts the common complement or collapses to a directed triangle

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-transfer-cycle-holonomy-contraction`

**Summary:** In a fixed-complement critical block, take a directed endpoint-return cycle all in HEAD role whose matched incidences all transfer. Double-prefix pushing q0,q1 across every row gives Hamilton puncture representatives sharing Q[2,t]. If all adjacent pushed comparisons were R435-quiet, quietness forces each original puncture path to start with the next two cycle labels; when cycle length at least four, adjacent quietness forces the next three, contradicting non-Hamiltonicity of Omega because the previous row certifies the turn needed to prepend the missing label. Hence length at least four yields an R435-active adjacent pair after shortening the common complement by two. If length three, all-quiet forces the three forward cyclic turns bad and therefore a physical directed comparison triangle. The TAIL case is dual. Thus an all-transfer closed representative walk either strictly contracts its common-complement holonomy or reaches minimal triangle holonomy.


### 1. Setup
Let H be a hypothetical smallest counterexample with

  V(H)=Omega disjoint_union V(Q),
  Q=(q_0,q_1,...,q_t),

where Omega is non-Hamiltonian but deletion-Hamiltonian and Q is a literal Hamilton tight path. Retain an endpoint-return matching as in accepted R945 and one directed cycle of its functional digraph

  y_0 -> y_1 -> ... -> y_{ell-1} -> y_0,

with ell>=3. Indices below are modulo ell.

Assume the chosen Hamilton puncture path P_i on Omega-y_i realizes the matched endpoint y_{i+1} in the HEAD role, so write

  P_i=(y_{i+1},r_i,...).

Assume further that every matched incidence on this cycle takes the successful HEAD-transfer branch of `fixed-complement-endpoint-return-transfer-compiler` SV23560. The same argument with all paths in the TAIL role is the exact order dual.

### 2. Simultaneous double-prefix push
By SV23560, every successful HEAD transfer first attaches q_0 and then automatically pulls q_1 across using the full critical-block boundary wall. Hence for every i there is a literal Hamilton path

  P_i^1=(q_1,q_0,y_{i+1},r_i,...)

on

  (Omega-{y_i}) union {q_0,q_1},

and

  P_i^1 | Q^{(2)},   Q^{(2)}=(q_2,q_3,...,q_t),

is an exact two-cover of H-y_i. Thus all rows on the endpoint-return cycle survive as actual Hamilton representatives with one common literal complement shortened by two vertices.

### 3. Quiet adjacent pushed rows force the endpoint cycle into their literal prefixes
Fix i and suppose the comparison of P_i^1 and P_{i+1}^1 is R435-quiet. Their common physical vertices occur in the same order. The only Omega-label present in P_i^1 but absent from P_{i+1}^1 is y_{i+1}, while the only Omega-label present in P_{i+1}^1 but absent from P_i^1 is y_i. Both paths begin with the same two labels q_1,q_0.

Delete the noncommon label y_{i+1} from the displayed order of P_i^1. The first common Omega-label after q_0 is r_i. Delete the noncommon label y_i from P_{i+1}^1. Since P_{i+1}^1 begins q_1,q_0,y_{i+2}, the first common Omega-label after q_0 is y_{i+2}. Quietness therefore forces

  r_i=y_{i+2}.

Hence every quiet adjacent pair forces

  P_i=(y_{i+1},y_{i+2},...).                         (HC.1)

Now suppose ell>=4 and both adjacent comparisons at i and i+1 are quiet. Applying (HC.1) at i+1 gives

  P_{i+1}=(y_{i+2},y_{i+3},...).

Because y_i is distinct from y_{i+3} when ell>=4, deleting the noncommon y_i from P_{i+1}^1 does not disturb this second common label. Comparing the common-contact orders once more therefore forces the third Omega-label of P_i to be y_{i+3}:

  P_i=(y_{i+1},y_{i+2},y_{i+3},...).                  (HC.2)

### 4. A quiet cycle of length at least four contradicts non-Hamiltonicity of Omega
Assume every adjacent pushed comparison around the cycle is R435-quiet and ell>=4. Then (HC.2) holds for every i. In particular P_{i-1} begins

  (y_i,y_{i+1},y_{i+2}),

so the turn

  (y_i,y_{i+1},y_{i+2})                               (HC.3)

is tight.

But P_i is a Hamilton path on Omega-y_i beginning (y_{i+1},y_{i+2}). If (HC.3) is tight, prepending y_i to P_i gives a Hamilton tight path on all of Omega, contradicting the defining non-Hamiltonicity of the critical block.

Therefore for ell>=4 at least one adjacent pair P_i^1,P_{i+1}^1 is R435-active. This activity is current in two singleton-deletion fibers sharing the strictly shorter literal complement Q^{(2)}. Thus the closed endpoint-return walk has transported its order holonomy through an actual support transfer while reducing the common-complement length by two.

### 5. The only all-quiet survivor is a physical directed triangle
Let ell=3 and suppose all three pushed adjacent comparisons are R435-quiet. Section 3 still gives

  P_i=(y_{i+1},y_{i+2},...)

for every i. Since Omega is non-Hamiltonian, prepending the missing label y_i is impossible. Hence every cyclic forward turn

  (y_i,y_{i+1},y_{i+2})

is bad. By exact reversal R3, all three reverse cyclic turns

  (y_{i+2},y_{i+1},y_i)

are tight. Equivalently the three ordinary edges on {y_0,y_1,y_2} form a directed comparison triangle.

Thus the all-transfer cycle has only two outcomes:

1. SHORTENED-COMPLEMENT HOLONOMY: an adjacent pushed pair has an explicit R435 output while sharing Q[2,t]; or
2. MINIMAL HOLONOMY: the endpoint-return cycle has length three and its physical labels form a directed comparison triangle.

### 6. Scope
This is not full CBCA. It is a contraction theorem for one global branch: a closed endpoint-return walk whose matched incidences all transfer on one common side cannot remain a long quiet loop after the support push. It either carries its conflict into a strictly shorter common complement or collapses to the smallest ordinary comparison holonomy. No generic R435 output is counted as closure; the progress measure is the common-complement shortening, and the triangle outcome is a physically smaller holonomy species. The TAIL version is the exact dual.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    },
    {
        "relation": "dependency",
        "revision_id": "R945"
    }
]
```
