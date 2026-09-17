# Singleton incoherence amplifies to a complete fixed-witness defect fan

**Workspace:** D17
**State:** established
**Key:** `singleton-disagreement-fan`

**Summary:** For any chosen singleton-deletion cover family in a hypothetical counterexample, failure of support-partition coherence is witnessed by some physical pair {u,v} whose same-block status splits all eligible deletion labels into two nonempty classes. Every cross-class pair of deletion labels is then an overlap disagreement in both ordered directions, hence by codimension-one coherence carries positive actual substitution defect kappa and therefore selected crossing/R511 bridge geometry. Thus incoherence yields at least n-3 unordered and 2(n-3) ordered defects sharing one witness pair, providing a canonical collective repair region for a global K-descent theorem.


### Setup
Choose one actual exact two-nonempty-path cover C_x of H-x for every physical vertex x of a hypothetical smallest counterexample H, and let sigma_x be its unordered support partition. Retain the codimension-one substitution defects kappa(a<-b) from `codimension-one-coherence`.

Assume the family is not coherent. Then there exist distinct physical vertices u,v and two deletion labels a,b outside {u,v} such that u,v have different same-block status in sigma_a and sigma_b. Put

  U=V(H)-{u,v}.

For every deletion label x in U define

  f(x)=1 if u,v lie in the same sigma_x block,
       0 otherwise.

The function f is nonconstant. Split

  A={x in U : f(x)=0},
  B={x in U : f(x)=1}.

Both A and B are nonempty and |A|+|B|=n-2.

### Complete bipartite defect fan
Fix any a in A and b in B. The two singleton-deletion partitions sigma_a and sigma_b disagree on their common residue H-{a,b}, witnessed by the surviving physical pair {u,v}. By the exact equivalence proved in `codimension-one-coherence`, overlap disagreement in a counterexample is equivalent to positive deleted-label substitution defect in each ordered comparison. Hence

  kappa(a<-b)>0,
  kappa(b<-a)>0.

Therefore every cross pair A x B is an actual two-way substitution-conflict pair. The unordered conflict graph contains the complete bipartite graph K_{|A|,|B|}, all conflicts witnessed by the same physical pair {u,v}. Since A,B are nonempty,

  |A||B| >= n-3,

with equality only when one class has size one. Counting ordered comparisons gives at least

  2|A||B| >= 2(n-3)

positive kappa defects sharing the same witness pair.

This is stronger than merely saying the global potential K is positive. Every one of these positive ordered defects is already cover-valued. By the classification in `codimension-one-coherence`, each is realized either by

1. an actual selected adjacency crossing the two source-rail supports of the comparison source, or
2. the exact R511 unique-transition bridge cell after the direct source-rail crossing is absent.

Thus any incoherent singleton family contains a canonical fixed-witness multi-fiber repair region rather than an isolated bad comparison.

### Consequences for a K-minimizing family
If the chosen family minimizes total substitution defect

  K=sum_{a != b} kappa(a<-b),

then K>0 forces the complete fan above for some {u,v}. A successful repair theorem need not descend one defect at a time. It may alter a whole subfamily indexed by one side of A|B, provided the total effect on all ordered comparisons is audited. The fixed witness pair gives a natural synchronization coordinate for such a simultaneous move.

No assertion is made that flipping the minority class preserves realizability, that the same selected crossing witnesses all fan edges, or that collateral kappa terms decrease. Those are precisely the remaining multi-fiber exchange issues.

### Scope
The fan amplification is elementary once codimension-one coherence is available. It uses only support-partition disagreement plus the already proved equivalence between disagreement and positive actual substitution defect. It is not a closure theorem and does not promote the proposed global K-repair theorem.

