# The quiet pair-core triangle is forced active by its fourth Hamilton puncture

**Workspace:** D17
**State:** established
**Key:** `universal-one-extension-pair-core-triangle-fourth-puncture-currentization`

**Summary:** In the surviving SV31722 quiet pair-core triangle, the six-set U=T+{a,b,c} is non-Hamiltonian while U-a,U-b,U-c are Hamiltonian and their retained pair orders form a cyclic same-slot defect. Accepted R195 forces at least one additional Hamilton puncture U-t with t in T. Any Hamilton path R on U-t cannot be R435-quiet against all three perimeter paths, because quietness would force the impossible linear-order cycle a<b<c<a inside R. Hence a mandatory fourth puncture creates an explicit one-foreign R435 first-change event. Reverse-trimer output is currentized to an actual maximum three-forest by R4, proper-cycle output to the SV25652 movable-break closed orbit, and selected-reversal output remains literally present in two actual maximum-three-forest representatives obtained from the two Hamilton five-paths by R4. Thus the quiet cyclic triangle is not terminal; only the neighboring-support selected-reversal contraction remains as a local residue.


### 1. Retain the cyclic same-slot triangle
Retain the surviving local cell of SV31722. Thus

  U=T union {a,b,c},

where T has three vertices, U is non-Hamiltonian, and the three punctures

  U-c=T+{a,b},
  U-a=T+{b,c},
  U-b=T+{c,a}                                           (FP.1)

have retained Hamilton paths P_ab,P_bc,P_ca. Their pairwise R435 comparisons are quiet. They induce one common order on T, all three exterior labels occupy one common insertion slot, and their retained pair orders form a directed cycle. Relabel the cycle as

  a <_{P_ab} b,
  b <_{P_bc} c,
  c <_{P_ca} a.                                         (FP.2)

### 2. R195 forces a fourth Hamilton puncture
Apply accepted R195 to the six-set U. At least four of its six five-vertex punctures are Hamiltonian. The three punctures in (FP.1) already account for only three deleted labels a,b,c. Therefore for at least one physical core label

  t in T                                                  (FP.3)

the puncture U-t is Hamiltonian. Choose and retain an actual Hamilton path

  R on U-t.                                               (FP.4)

### 3. The fourth puncture cannot be quiet against all three perimeter paths
Suppose for contradiction that R is R435-quiet against each of P_ab,P_bc,P_ca.

Compare R with P_ab. Their common vertices contain a and b. R435 quietness means all common contacts occur in the P_ab order, hence a occurs before b in R.

Likewise quietness against P_bc forces b before c in R, while quietness against P_ca forces c before a in R.

Thus the one literal linear order R would satisfy

  a before b before c before a,                           (FP.5)

impossible.

Hence at least one of the three one-for-one neighboring-support comparisons

  (R,P_ab), (R,P_bc), (R,P_ca)                            (FP.6)

is R435-nonquiet.

This is exactly a first-change statement: the shortest quiet insertion holonomy cannot absorb the mandatory fourth Hamilton puncture without producing explicit Reverse-Ear geometry.

### 4. The forced event is one-foreign and physically localized
Fix one nonquiet comparison in (FP.6), say R versus P_ab. The two Hamilton supports are

  U-t  and  U-c,

so they differ by one exchanged label on each side and have four common vertices. By the one-foreign localization SV24806, every Reverse-Ear conflict is physically either

1. a common-support adjacent selected-state reversal, or
2. a two-state detour through the unique foreign exchanged label, yielding the corresponding reverse-trimer / proper-cycle R435 geometry.

There is no long anonymous foreign ear.

### 5. Every output is current in maximum-three-forest representative space
The three R435 species have the following current status.

REVERSE TRIMER. The displayed reverse trimer is a proper graph-intrinsic tight path of H. Accepted R4 supplies an exact two-cover of its complement, so it sits literally in an actual maximum spanning three-forest.

PROPER CYCLE. The R435 cycle is proper. The movable-break theorem SV25652 therefore turns it into a closed family of actual maximum spanning three-forests with one fixed exact complement cover.

SELECTED REVERSAL. The two source Hamilton five-paths themselves are proper tight paths. Apply R4 separately to each. This yields two actual maximum spanning three-forest representatives, one containing the first Hamilton five-path and one containing the second. The common physical dimer selected in opposite directions by the R435 output remains literally selected in those two current representatives. No transition between the two representatives is asserted here, but the reversal is no longer an uncurrentized local certificate.

### 6. Consequence for the pair-core triangle
Therefore the cyclic same-slot cell of SV31722 is not a terminal quiet support holonomy. The mandatory fourth Hamilton puncture of its six-union forces a one-foreign R435 first-change event, and that event is currentized as

  an actual maximum-three-forest reverse-trimer representative,
  a closed movable-break maximum-forest orbit,
  or a selected physical reversal retained in two actual maximum-forest representatives.  (FP.7)

The remaining selected-reversal contraction problem is narrower than the original pair-core triangle: it involves two neighboring Hamilton five-supports and one named reversed common dimer. No claim is made that (FP.7) by itself closes H.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R4"
    },
    {
        "relation": "dependency",
        "revision_id": "R195"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    }
]
```
