# A surplus 2-cut return is a codimension-one defect or a Hamilton complement replacement

**Workspace:** D17
**State:** established
**Key:** `singleton-cover-union-return-defect-or-replacement`

**Summary:** In the hard minimal 2-cut parallel row C_p=(A-q-B)|C, take any actual selected surplus state p-c in another singleton fiber C_x. If x lies in A or B, p-c itself crosses the deleted-label substitution partition induced by source C_p, so kappa(x<-p)>0. If x lies in C, p-c is internal to the substituted side C-x+p; either another selected state gives kappa(x<-p)>0, or kappa=0 and C_x has support partition (C-x+p)|(A-q-B), so C-x+p is Hamiltonian with the actual p-c state retained. Dually for q. Thus every globally forced return from the minimal-equality incidence theorem feeds either the K-repair program as a current defect or the fixed-complement program as an actual Hamilton one-vertex replacement.

### Setup
Retain the hard minimum-equality 2-cut from the preceding sections:

  U-{p,q}=A disjoint-union B disjoint-union C,
  C_p=(A-q-B)|C,
  C_q=(A-p-B)|C,

in the parallel quiet branch. The minimum-equality incidence theorem guarantees that U contains at least one selected p-C state and at least one selected q-C state, each occurring in some other singleton-deletion cover.

Fix an actual selected state p-c in C_x, where c in C. Necessarily x is distinct from p,q,c because the state occurs in H-x and neither distinguished p- nor q-deletion bridge cover selects a p-C state.

We compare C_x with the source fiber C_p using the deleted-label substitution coordinate of `codimension-one-coherence`.

### Owner outside C gives a literal kappa defect
Suppose x lies in A or B. In the source C_p, x lies on the mixed Hamilton rail

  D_q=A-q-B,

while the opposite source rail is C. Substituting the omitted label p for x produces the target support partition of H-x

  (D_q-x+p) | C.

The selected state p-c of C_x has p in the first target class and c in the second. Hence p-c itself is a selected crossing of the substitution cut. Therefore

  kappa(x <- p) > 0.

No further classification is needed to see that this surplus return is already current currency for the global K-repair theorem. In the finer normal form of codimension-one coherence it is the source-deleted-label-to-opposite-rail defect type unless another direct mixed-source crossing is also selected.

### Owner inside C gives defect or Hamilton replacement
Suppose instead x lies in C. Now x lies on the pure C rail of C_p. Deleted-label substitution produces the target partition

  (C-x+p) | D_q.

The selected p-c state lies wholly inside the first target class and is therefore not itself a kappa crossing. There are exactly two possibilities.

If C_x selects any state crossing these two target classes, then by definition

  kappa(x <- p) > 0,

so again the surplus-return owner is a current codimension-one defect row.

If no such crossing exists, then kappa(x<-p)=0. Both target classes are nonempty and C_x has exactly two nonempty rails. Hence each rail lies wholly in one target class and the support partition of C_x is exactly

  (C-x+p) | D_q.

Thus C-x+p is Hamiltonian. More strongly, the actual selected p-c state belongs to the Hamilton rail on C-x+p, so the replacement is current and carries the physical return coordinate rather than merely support Hamiltonicity.

### Dual statement and combined parent
The exact dual holds for every selected q-C surplus state, using source C_q=(A-p-B)|C. Its owner y either satisfies kappa(y<-q)>0 or, when y lies in C and the comparison is quiet, yields an actual Hamilton replacement C-y+q carrying the selected q-C state.

Therefore each of the two globally forced return incidences supplied by the minimum-equality theorem enters one of two already meaningful parent currencies:

1. CURRENT DEFECT: a positive deleted-label substitution defect contributing to K; or
2. CURRENT REPLACEMENT: a Hamilton one-vertex replacement of the non-Hamiltonian fixed complement C+p or C+q, with the bridge label physically selected on that Hamilton rail.

This couples the selected-edge-union separator program to the K-minimization program instead of creating an independent recurrence. A future closure theorem may therefore target a K-minimal family and show that the hard 2-cut cannot support its mandatory return incidences without either lowering K or producing enough complement replacements for fixed-support endpoint/R561 currentization.

Status: complete elementary specialization of the working codimension-one substitution theorem to the minimal-equality double-bridge row; not independently reviewed as a section.
