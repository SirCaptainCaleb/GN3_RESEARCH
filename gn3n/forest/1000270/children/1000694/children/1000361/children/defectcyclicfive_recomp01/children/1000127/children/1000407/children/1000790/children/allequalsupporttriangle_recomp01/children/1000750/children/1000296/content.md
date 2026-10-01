# A permanently internal complementary endpoint forces double crossing in every deletion cover

## Statement

Let H be a minimum counterexample and let X|C|D be a spanning three-cover, where X is Hamiltonian, C=(c_0,c_1,...,c_m) and D are nonempty tight paths, and m>=1. Suppose H[X union {c_0}] is Hamiltonian but c_0 is internal in every Hamilton tight path on X union {c_0}. Then for any Hamilton path R on X union {c_0}, deleting c_0 splits R into two nonempty tight paths L|R^+, and every two-cover T of H-c_0 has at least two ordinary edges crossing the four-class partition V(L)|V(R^+)|V(C-c_0)|V(D).

## Body

Choose a Hamilton path R on X union {c_0}. Permanent internality means c_0 is not an endpoint of R, so deleting c_0 leaves two nonempty contiguous tight subpaths L and R^+. Since m>=1, C-c_0 is a nonempty tight path, and D is nonempty by hypothesis. Hence H-c_0 has a displayed four-path cover L|R^+|(C-c_0)|D, and each of the four partition classes is Hamiltonian. Let T be any two-cover of H-c_0, which exists by minimum-counterexample calculus. Apply the transition-count identity of coversurg01 Section 6 to the four-class partition and q=2. Since each class has path-cover number one, the number t of ordinary T-edges joining distinct classes satisfies t >= 1+1+1+1-2 = 2. Thus every deletion cover of H-c_0 has at least two support crossings relative to the canonical four-piece split created by the permanently internal vertex.
