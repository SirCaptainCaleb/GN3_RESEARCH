# Every critical-block puncture path lies in a common-complement R966 Reverse-Ear triple

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-critical-block-universal-r966`

**Summary:** Let V(H)=Omega disjoint-union Q be a smallest-counterexample fixed-complement critical block. Fix any actual Hamilton puncture path P_a on Omega-a with endpoints h,t. Because Omega is deletion-Hamiltonian, Omega-h and Omega-t are Hamiltonian, so they are exactly the two endpoint-replacement supports required by accepted R966 when P_a is the base path and a is the exterior vertex. Since Omega=P_a+a is non-Hamiltonian, R966 cannot take its Hamilton-extension outcome. Therefore P_a together with arbitrary retained Hamilton paths on Omega-h and Omega-t has explicit R435 geometry in at least one of the three pairwise comparisons. All three paths pair with the same literal Q in exact singleton-deletion covers. Hence every puncture path, including every member of an R961-quiet anchored packet, belongs to a source-visible common-complement Reverse-Ear triple. The R961 quiet branch is not globally R435-free.

### 1. Universal endpoint-replacement setup
Let H be a hypothetical smallest counterexample with

  V(H)=Omega disjoint_union V(Q),

where Q is a literal Hamilton path and Omega is non-Hamiltonian deletion-Hamiltonian. Fix any a in Omega and any ACTUAL Hamilton path

  P_a=(p_0,p_1,...,p_r)

on Omega-a. Since |Omega|>=5 in the live critical-block setting, r>=3; in particular the endpoint-replacement theorem R966 applies.

Put h=p_0 and t=p_r. Because Omega is deletion-Hamiltonian, both supports

  Omega-h = ((Omega-a)-h)+a,
  Omega-t = ((Omega-a)-t)+a                               (UR.1)

are Hamiltonian. Choose arbitrary actual Hamilton paths L_h on Omega-h and R_t on Omega-t.

### 2. Accepted R966 must emit Reverse-Ear geometry
Apply accepted R966 with

  X=Omega-a,
  base path=P_a,
  exterior vertex=a,
  left endpoint replacement=L_h,
  right endpoint replacement=R_t.

Its full-extension support is

  X+a=Omega,

which is non-Hamiltonian by hypothesis. Therefore the Hamilton-extension outcome of R966 is impossible. At least one of the three comparisons

  (P_a,L_h), (P_a,R_t), (L_h,R_t)                       (UR.2)

has an explicit R435 output: a reversed ancestral selected state, a tight reverse trimer at an ear seam, or a vertex-simple proper tight cycle.

This holds for EVERY choice of P_a and for EVERY retained choice of the two endpoint-replacement Hamilton paths L_h,R_t.

### 3. All three paths are current with one literal complement
The fixed-complement hypothesis currentizes all three paths without further work:

  P_a | Q   is an exact two-cover of H-a,
  L_h | Q   is an exact two-cover of H-h,
  R_t | Q   is an exact two-cover of H-t.                (UR.3)

Thus the R435 output in (UR.2) is always source-visible across three singleton fibers sharing the SAME literal Hamilton complement Q. No representative synchronization has been lost.

### 4. Closure-map consequence
A fixed-complement critical block is therefore intrinsically Reverse-Ear active around every puncture path. In particular, even when accepted R961 selects an R435-quiet constant-role HHH/TTT triangle relative to its own three adjacent comparisons, each individual puncture path in that quiet packet still belongs to some R966 triple (UR.2) that emits explicit R435 geometry.

Hence the R961 dichotomy must not be interpreted as partitioning CBCA into a globally R435-free quiet world and an R435-active world. Quietness is comparison-relative. The whole critical block remains a common-complement R435 reservoir.

The unresolved grand consumer is correspondingly sharper: consume source-visible R435 reversal/reverse-trimer/proper-cycle geometry while retaining Q, rather than treating the quiet anchored triangle as the only structured entry to CBCA. No spanning two-cover is claimed here.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R966"
    }
]
```
