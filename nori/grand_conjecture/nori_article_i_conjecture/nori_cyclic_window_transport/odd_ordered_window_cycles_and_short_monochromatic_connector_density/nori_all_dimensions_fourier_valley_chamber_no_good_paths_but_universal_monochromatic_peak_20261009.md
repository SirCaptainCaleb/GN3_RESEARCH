# All-dimensional active NORI coloring with no good Fourier-valley full geodesic, yet an all-roots monochromatic peak witness

# Sharp all-dimensional obstruction: Fourier-acyclic full geodesic family can contain NO good NORI witness

Fix n>=5 with cube coordinates ordered 1<2<...<n. Recall Fourier's antipodally invariant middle-maximum feedback set T_mid of all ACTUAL physical ordered 3-face windows whose middle direction exceeds both outer directions. A full direction-distinct n-letter permutation P AVOIDS T_mid iff its sequence has no local maximum, equivalently it is a valley permutation
    P(L) = descending(L),1,ascending({2,...,n}\L)
for some L⊆{2,...,n}.
There are 2^(n-1) such orders, and they form a Boolean-cube family. Under physical antipodal reversal, the full direction word is reversed and L is sent to its complement, so the family is antipodally invariant. For a FIXED starting root x, complement L pairs these full paths; starting root stays x under the full-path antipodal reversal.

**THEOREM (EXPLICIT REVERSAL-ODD NONEXTRACTION FOR ALL n).** For every n>=5 there is a VALID ACTIVE NORI coloring of all genuine physical ordered 3-faces of Q_n, in fact independent of the exterior face bits, such that
 (a) EVERY full antipodal geodesic whose ordered directions avoid T_mid has at least TWO three-window color switches (so NONE is a grand conjecture witness), yet
 (b) for EVERY physical root x, the full direction word
       (1,3,2,4,5,6,...,n)
     gives an ACTUAL MONOCHROMATIC antipodal geodesic (all ordered windows color one).
Thus removing the Fourier middle-maximum transversal can remove ALL successful full geodesics, even when a monochromatic full witness exists from EVERY root. The tau-equivariant one-third feedback transversal cannot, by itself, support a witness-preserving grand-closure reduction to its acyclic complement.

**Explicit coloring.** On every ordered triple (a,b,c) of distinct directions put
    c(F,(a,b,c)) = 1{a<c} XOR epsilon(a,b,c),
independently of the physical face F. Here epsilon equals one precisely in the following two DISJOINT cases, and zero otherwise:
 (I) all a,b,c belong to {1,2,3,4,5}; the triple is strictly monotone (a<b<c or a>b>c); and its unordered free-coordinate set is one of {1,2,3}, {1,2,4}, {1,2,5}, {3,4,5};
 (II) b=1, the unordered outer pair is {a,c}={2,k} for k∈{3,4,5}.
The perturbation epsilon is invariant under reversing (a,b,c)↦(c,b,a). The base bit 1{a<c} is complemented by reversal of the distinct outer directions. Hence c(F,(a,b,c)) + c(bar F,(c,b,a))=1 mod2 for EVERY actual physical ordered face, proving the active NORI axiom.

**Five-coordinate alternating core.** Restrict to ordered triples of {1,2,3,4,5}. For the 13 reversal-orbit representatives, the values are:
 increasing representatives: 123→0,124→0,125→0,134→1,135→1,145→1,234→1,235→1,245→1,345→0;
 center-minimum representatives: 213→0,214→0,215→0.
The reversed triples have the complementary value. Every other triple receives the base sign 1{a<c}.

Consider any of the SIXTEEN valley permutations on symbols {1,2,3,4,5}. Up to reversal (which complements and reverses the three-window word), only the EIGHT cases with 5 lying on the RIGHT are needed. In each case list L, permutation, actual three-window color word:
 L=∅:      12345  → 010
 L={2}:    21345  → 010
 L={3}:    31245  → 101
 L={2,3}:  32145  → 101
 L={4}:    41235  → 101
 L={2,4}:  42135  → 101
 L={3,4}:  43125  → 010
 L={2,3,4}:43215  → 010.
The remaining eight valley permutations are their reversals, and hence also have EXACTLY TWO switches. All values are independent of cube starting root.

**Lifting to EVERY dimension without losing contiguity.** In a valley permutation of the ENTIRE alphabet [n], the five SMALLEST symbols 1,2,3,4,5 appear as a SINGLE CONTIGUOUS FIVE-LETTER BLOCK: every larger direction that belongs to its decreasing left shore precedes all five-block left letters, and every larger right-shore direction succeeds all five-block right letters. The induced order of 1,...,5 is one of the above sixteen five-symbol valleys. Consequently THREE CONSECUTIVE actual physical ordered three-face windows of the full n-edge path have triples all in {1,...,5} and color word 010 or 101. The full path therefore has at least TWO switches, irrespective of other windows and the starting root x. This proves (a) in ALL n>=5.

**Simultaneous universal positive witness.** Take P0=(1,3,2,4,5,6,...,n). Its first three triple words are (1,3,2),(3,2,4),(2,4,5). None meets either epsilon-exception, and each has first coordinate smaller than last, hence color one. Every subsequent triple contains a direction >5 and has strictly increasing outer endpoints, so epsilon zero and baseline one. Therefore ALL ordered-three-face windows of P0 have color one, for every starting root x. Every such P0 is a physical full antipodal monochromatic geodesic. It necessarily meets T_mid at its early triple (1,3,2), because 3 is larger than both neighbors. This proves (b).

**Strategic interpretation.** The n-1 dimensional Boolean cube of Fourier-acyclic full valley permutations (with tau acting as complement) does NOT automatically admit a valid <=1-switch label at any vertex—even when an all-roots monochromatic witness exists elsewhere. Thus high index of the Boolean FAMILY of candidate paths cannot alone imply an extraction theorem. Any viable topological extension must ADD non-valley paths/peak windows with actual physical gluing, perhaps using the exact rooted reversed-two-tail reachability criterion. This is a constructive all-dimensional obstacle, not a counterexample to NORI itself.
