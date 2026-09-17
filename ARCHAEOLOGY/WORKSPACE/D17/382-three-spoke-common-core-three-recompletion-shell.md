# A three-spoke source frame forces one non-Hamiltonian common core and three coupled 3-to-2 recompletion rows

**Workspace:** D17
**State:** established
**Key:** `three-spoke-common-core-three-recompletion-shell`

**Summary:** Let H-{a,c}=U|V be an exact source frame with three distinct internal same-orientation spokes p,q,r, and put W=V(H)-{a,c,p,q,r}. The three-spoke lemma makes K={a,c,p,q,r} Hamiltonian, so W cannot be Hamiltonian in a counterexample; by minimality pc(W)=2. For each spoke s, the pairwise outer-four theorem gives a Hamilton P4 on {a,c} plus the other two spokes. Hence W+s cannot be Hamiltonian, or that P4 together with a Hamilton W+s path would two-cover H. Thus pc(W+s)=2 for all three s. But deleting the other two internal spokes from the original source cover U|V leaves a literal cover of W+s with at least three components. Therefore the one source frame canonically carries three simultaneous source-visible 3-to-2 recompletion problems W+p, W+q, W+r over the same non-Hamiltonian exactly-two-covered core W. This is graph-intrinsic common-parent structure, not three independent anonymous R159 events.

### 1. Source frame and common core
Let H be a hypothetical smallest Strong Level-(1) counterexample. Retain one exact pair-deletion frame

  H-{a,c}=U|V

and three distinct vertices p,q,r that are internal in the displayed source rails and have one common outer orientation

  (a,p,c), (a,q,c), (a,r,c)

tight. Put

  K={a,c,p,q,r},
  W=V(H)-K.

The existential three-spoke theorem SV58280 gives a Hamilton tight P5 on the support K. No particular Hamilton order is assumed.

### 2. The common core W is non-Hamiltonian and exactly two-covered
If W had a Hamilton tight path, that path together with any Hamilton P5 on K would be a spanning two-path cover of H, contradicting counterexamplehood. Hence W is non-Hamiltonian.

W is a nonempty proper induced subsystem in the live range |H|>10. Smallest-counterexample minimality R4 therefore gives pc(W)<=2. Since W is not Hamiltonian,

  pc(W)=2.                                               (CR.1)

Fix when needed one actual exact two-cover A|B of W, but no canonical representative is asserted.

### 3. Every one-spoke extension W+s is non-Hamiltonian
Fix s in {p,q,r}, and let t,u be the other two spokes. Exact unit SV89302 gives a Hamilton P4 on the four-set

  {a,c,t,u}.

If W+s were Hamiltonian, that Hamilton path and the outer Hamilton P4 would have disjoint supports whose union is V(H). They would therefore form a spanning two-cover of H. Hence

  W+p, W+q, W+r are all non-Hamiltonian.                 (CR.2)

Each W+s is proper, so R4 again gives a cover by at most two paths; non-Hamiltonicity forces

  pc(W+s)=2 for every s in {p,q,r}.                      (CR.3)

### 4. The original source frame gives a >=3-component cover of each W+s
Fix s and delete the other two spokes t,u from the original source rails U|V. Both t and u were internal in their displayed rails.

If they lie on different source rails, each deletion splits its rail into two nonempty old-order intervals, so the restriction to W+s has at least four nonempty path components.

If t,u lie on the same source rail, deleting two internal vertices leaves at least two nonempty old-order intervals on that rail even when t,u are adjacent; the untouched source rail remains one nonempty component. Hence the restriction again has at least three nonempty components.

Therefore for each s there is a literal source-visible cover

  R_s of W+s

with

  c(R_s)>=3.                                             (CR.4)

Together with (CR.3), each s gives a genuine source-visible component drop from R_s to some exact two-cover T_s of W+s.

### 5. Three coupled recompletion rows
The three drops for s=p,q,r are not unrelated R159 events. They coexist in one common parent and share:

- the exact source frame U|V,
- the physical anchors a,c,
- the same three internal spoke positions,
- the common residual vertex set W,
- the old source orders on every surviving interval,
- and the fact pc(W)=2.

Only the retained spoke differs. Thus the source frame canonically carries a three-row recompletion shell

  R_p -> T_p on W+p,
  R_q -> T_q on W+q,
  R_r -> T_r on W+r,                                   (CR.5)

where each left side is a restriction of the SAME physical source cover and each right side is an actual exact two-cover of its one-spoke extension.

### 6. Scope and strategic use
R159 may be applied separately to each row, but the existence of another balanced pair is not the content of this theorem. The gain is the simultaneous source-visible shell (CR.5) over one common exactly-two-covered non-Hamiltonian core W. Any source-frame absorption argument should couple these three recompletions or couple one of them to the actual two-cover A|B of W before collapsing them to anonymous payment currency.

No special Hamilton order on K is used. R24 and R5 are unused.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R4"
    }
]
```
