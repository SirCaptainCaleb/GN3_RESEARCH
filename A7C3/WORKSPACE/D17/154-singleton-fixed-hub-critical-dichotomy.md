# A fixed singleton hub has a direct-crossing defect or a fixed-complement critical rail

**Workspace:** D17
**State:** established
**Key:** `singleton-fixed-hub-critical-dichotomy`

**Summary:** Fix a singleton source row C_b=P|Q. For every a on P, either C_a contains a direct selected (P-a)|Q crossing, or H-a admits the support copy (P-a+b)|Q; coherent pairs give it directly and no-direct-crossing incoherent pairs give it by the seam-free R511 bridge repair. Hence absence of direct crossings on P makes P+b a non-Hamiltonian deletion-Hamiltonian block whose every puncture is paired with the same literal complement Q. If neither side has direct defects, P+b and Q+b are overlapping fixed-complement critical blocks covering H.

### Fixed hub row
Let H be a hypothetical smallest counterexample and retain one actual exact singleton-deletion cover

  C_b=P|Q

of H-b by two nonempty Hamilton tight paths. Fix the literal orders P and Q.

For a vertex a in P, compare the a-deletion row C_a against source row C_b in the notation of `codimension-one-coherence`: the source rail containing a is P={a} union S and the opposite source rail is Q=T_0. There are three possibilities.

1. The two support partitions are overlap-coherent. Then, in a counterexample, `codimension-one-coherence` rules out the swapped placement and forces sigma_a=(P-a+b)|Q. Hence P-a+b is Hamiltonian.
2. They are incoherent and C_a contains a selected adjacency directly crossing (P-a)|Q. Retain that physical direct defect.
3. They are incoherent and no selected (P-a)|Q adjacency occurs. Then the exact R511 bridge normal form applies and the seam-free replacement of `singleton-row-weighted-recombination` gives an actual exact cover with support partition (P-a+b)|Q. Hence again P-a+b is Hamiltonian.

Therefore for every a in P, either C_a supplies a current direct selected (P-a)|Q crossing, or the support P-a+b is Hamiltonian. The statement is dual for a in Q.

### No direct P-side crossing produces a deletion-critical block with fixed complement
Assume no a in P supplies the direct-crossing alternative. Put

  Omega_P=P union {b}.

For every a in P, the previous paragraph gives a Hamilton path R_a on Omega_P-a. Deleting b leaves the original Hamilton path P. Thus every one-vertex deletion of Omega_P is Hamiltonian. The whole Omega_P is non-Hamiltonian: otherwise a Hamilton path on Omega_P together with the disjoint literal Q rail would be a spanning two-cover of H. Hence Omega_P is a non-Hamiltonian deletion-Hamiltonian block.

Moreover every puncture can be made current against the SAME literal complementary rail Q. For a in P, take any Hamilton R_a on Omega_P-a furnished above and pair it with the retained original Q order; no seam is introduced because the supports are disjoint. Thus

  H-a = R_a | Q

for every a in P, while

  H-b = P | Q.

So the entire puncture family of Omega_P has one fixed Hamilton complement Q.

The exact dual holds for

  Omega_Q=Q union {b}

when no q in Q has a direct selected (Q-q)|P crossing: Omega_Q is non-Hamiltonian deletion-Hamiltonian and every puncture is paired with the same literal complement P.

### Hub dichotomy
Consequently every fixed hub row C_b=P|Q has the following top-level alternative.

(DIRECT) Some deletion label a on one of the two source rails has a current selected adjacency crossing the two source-rail supports after deleting a. This is a literal source-rail defect, not an abstract support disagreement.

(CRITICAL) If no such direct defect occurs anywhere, then both

  Omega_P=P+b,   Omega_Q=Q+b

are non-Hamiltonian deletion-Hamiltonian blocks, they intersect exactly in b and cover H, and each carries a complete singleton-puncture family with the opposite original rail as a fixed literal Hamilton complement.

A one-sided version is also available: absence of direct defects only on P already gives Omega_P with fixed complement Q, regardless of what happens on Q.

### Scope
This is a support-currentization theorem above the individual R511 packet. It does not consume the DIRECT branch and does not claim that two overlapping critical blocks are impossible. The CRITICAL branch is stronger than a bare cut-vertex/double-critical decomposition because every puncture comes with a fixed literal complementary rail inherited from one source row. The next parent target is to consume either the current direct-crossing fan into a coordinated K descent, or the two fixed-complement critical blocks by R961/R966/R561-type synchronization.
