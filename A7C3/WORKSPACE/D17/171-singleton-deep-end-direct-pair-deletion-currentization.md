# END-DIRECT fixed-hub crossings currentize one deletion lower to bidirectional support transfer or a two-crossing component drop

**Workspace:** D17
**State:** established
**Key:** `singleton-deep-end-direct-pair-deletion-currentization`

**Summary:** Each END-DIRECT endpoint fiber first currentizes on H-{a,t} to bidirectional support transfer or a two-crossing component drop. The two endpoint residues then share a literal third-deletion shadow X=H-{s,q,t} with ancestral exact cover M|B, M=(r1,...,p). Trimming the opposite endpoint from each currentized fiber yields component drop or support-partition disagreement unless all mixing localizes at that endpoint. At the terminal q-end, such a quiet localization would make B+s Hamiltonian, contradicting the parent failed-wrap fact H[B+s] non-Hamiltonian. Hence the q-end is FORCED CURRENT on the common shadow: it always yields component drop or genuine support disagreement (with physical selected crossings retained). Only the s-end can have a quiet endpoint transfer, which then Hamiltonizes B+q. Thus the former two-ended DIRECT output is asymmetrically synchronized: one endpoint necessarily remains current on the shared triple-deletion residue.

Retain `singleton-deep-wrap-terminal-endpoint-transfer` in its final END-DIRECT alternative. Thus H-t has an exact cover

  R=(s,r1,...,p,q) | B,                                    (ED.1)

and for an endpoint a in {s,q} the certified fixed-hub dichotomy supplies an exact singleton-deletion cover C_a of H-a selecting a physical adjacency xy with one endpoint in R-a and the other in B. By the definition of the DIRECT output, neither x nor y is the hub t. Work separately for a=s and a=q; no common-fiber synchronization is assumed initially.

### 1. The ancestral pair-deletion row is exact
Put W_a=H-{a,t}. Deleting a from the corresponding endpoint of R leaves the two literal paths

  (R-a) | B.                                                (ED.2)

They cover W_a and form an exact two-cover: if W_a were Hamiltonian, a Hamilton path on W_a together with the vacuous dimer {a,t} would be a spanning two-cover of H. The DIRECT selected edge xy survives trimming t because x,y are old vertices in (R-a) union B and neither is t.

### 2. Endpoint hub: bidirectional same-residue support transfer
Suppose t is an endpoint of its rail in C_a. If that rail were the singleton {t}, the other rail would Hamiltonize W_a, impossible by (ED.2). Hence deleting t leaves an exact two-cover F_a of W_a. The edge xy remains selected in F_a and crosses the support partition of (R-a)|B, so the partitions differ. Accepted R410/P419 applied symmetrically gives a selected crossing in each direction. Retain

  xy selected in F_a across (R-a)|B,
  uv selected in (R-a)|B across the F_a partition.           (ED.3)

No R176 descendant is taken.

### 3. Internal hub: ancestry-bearing component drop with two current crossings
Suppose t is internal in its C_a rail. Deleting t splits that rail into two nonempty contiguous paths and leaves the other rail unchanged, giving a literal three-cover G_a of W_a. The DIRECT edge xy survives. Comparing G_a with the exact two-cover (R-a)|B, the elementary component-count step of P555/R159 forces some selected adjacency uv of (R-a)|B to join two distinct G_a components. Retain both xy and uv together with both source covers. Again no generic R159/R176 payment is taken.

The remaining possibility t singleton in C_a is impossible by the Hamilton-W_a/dimer closure above. Thus every END-DIRECT fiber is already currentized on its natural pair-deletion residue.

### 4. The two endpoint residues have one literal common shadow
Now use both endpoint fibers. Put

  M=(r1,...,p),
  X=H-{s,q,t}.                                              (ED.4)

Because the source and terminal of R are exactly s and q, the two ancestral pair-deletion covers

  (R-s)|B=(M,q)|B  on H-{s,t},
  (R-q)|B=(s,M)|B  on H-{q,t}                              (ED.5)

both restrict after deleting the opposite endpoint to the SAME literal two-cover

  M | B                                                     (ED.6)

of X. It is exact: if X were Hamiltonian, the deleted triple {s,q,t} has a tight Hamilton order by R3 and would pair with X to two-cover H.

Take either currentized endpoint representation from Sections 2-3 and delete the opposite endpoint as well. If the resulting cover has more than two components, compare it with (ED.6): P555 again gives an actual selected edge of M|B crossing its components. If it has exactly two components but a different support partition from M|B, R410 gives bidirectional selected crossings on X. The only potentially quiet outcome is therefore a two-cover of X with support partition exactly {V(M),V(B)}.

### 5. The terminal q-end cannot be quiet on the common shadow
Specialize to a=q, so the opposite endpoint removed in Section 4 is s. The parent failed-wrap theorem `singleton-deep-wrap-terminal-endpoint-transfer` already established

  H[B+s] is non-Hamiltonian.                                (ED.7)

We show this forbids the quiet common-shadow outcome.

If t was internal in C_q, then after deleting t we had a literal three-cover G_q of H-{q,t} retaining the DIRECT crossing xy. For deleting s to leave only two components, s must itself be a singleton component of G_q. Then xy cannot be incident with s and survives into the resulting two-cover of X. Since xy joins the old classes (R-q)-s=M and B, that two-cover has support partition different from M|B. Thus the internal-t branch is never quiet.

If t was an endpoint, let F_q be the exact two-cover of H-{q,t}. If deleting s yields a two-cover of X with the same support partition M|B, then s must be an endpoint of its F_q rail. Moreover the retained DIRECT crossing must be incident with s; otherwise it would survive deletion and cross M|B, forcing partition disagreement. Since the DIRECT crossing joins the old active side s+M to B, this means the F_q rail containing s has support exactly B+s. It is Hamiltonian. Hence H[B+s] is Hamiltonian, contradicting (ED.7).

Therefore the q-end DIRECT fiber is FORCED CURRENT after synchronization to X: it yields either a component-drop representation with an actual ancestral M|B crossing, or an exact two-cover with support partition different from M|B and hence bidirectional R410 crossings. There is no featureless q-end support-copy cell.

### 6. The source s-end has only one quiet form
For a=s the same argument shows that a quiet common-shadow outcome, if it occurs, must come from endpoint t and endpoint q in the trimmed exact cover, with the DIRECT crossing localized at q. Its q-containing rail then Hamiltonizes B+q. Thus the only quiet s-end form is an actual endpoint transfer

  M | (B+q) on H-{s,t},                                    (ED.8)

up to the rail order selected by that cover. No analogous non-Hamiltonicity of B+q is presently available, so (ED.8) is retained rather than excluded.

### 7. Exact conclusion
The two END-DIRECT fibers are not merely two unrelated defects. They synchronize on the common triple-deletion residue X with literal ancestral exact cover M|B. The terminal q-end is necessarily current there: component drop or genuine support-partition disagreement with physical crossings retained. The source s-end has the same current alternatives, with only the additional quiet endpoint-transfer form (ED.8). This is an asymmetric two-ended synchronization theorem. It does not yet consume the q-end crossing or synchronize its physical edge with the possible B+q transfer; those are the next restoration objects.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R410"
    },
    {
        "relation": "dependency",
        "revision_id": "R159"
    }
]
```
