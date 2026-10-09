# Three nonlinear terminal faults force alternating tails at every parity-monochromatic-prefix root

# General terminal-exception theorem: a bad NORI coloring forces internal switching inside every exceptional suffix

Fix ordered-r-face coloring, 2<=r<n, and a full direction permutation p=(p1,...,pn). Let L=n-r+1 denote the ordered-r-face color-word length and let 1<=k<=r with L>=k+1 (equivalently n>=r+k). Let c0(F,pi)=h(pi)+sum_(t outside free(pi))z_t mod2 be the all-one exterior-parity reference, with arbitrary orientation intercept h. Let c be ANY coloring of actual physical ordered r-faces (potentially nonlinear), agreeing with c0 on the FIRST L-k consecutive ordered-r-face direction TYPES of p, for ALL physical exterior-bit assignments. The FINAL k ordered face types are unrestricted and can satisfy the active antipodal oddness axiom.

Define the subset G of starting roots x whose first L-k reference/actual window colors are all equal. The reference change-vector map has n-r independent equations; its first L-k-1=n-r-k equations remain independent. Thus
 |G| = 2^(n - (n-r-k)) = 2^(r+k).
For x∈G write the common early color q(x) and the exceptional last-k actual color word W(x)=(u1,...,uk).

**THEOREM (shared-coordinate toggle).** Let t=p_(n-k+1), the direction at position n-k+1. It is absent from ALL early ordered-r-face windows (their last possible direction position is n-k), and it lies in EVERY ONE of the last k r-windows, because k<=r. Therefore:
  x∈G => x xor e_t ∈ G,
  q(x xor e_t) = 1-q(x),
  W(x xor e_t)=W(x),
with NO restriction on the Boolean complexity of the k exceptional face colorings.

**THEOREM (terminal suffix obstruction).** If ANY x∈G has a last-k exceptional word W(x) with at most ONE internal color change, then c has a full antipodal p-geodesic with at most ONE change. Specifically, from the paired roots x and x xor e_t choose the one whose repeated prefix color equals u1; its complete window word is u1^(L-k) W(x) and its number of changes is exactly the number of internal changes within W(x). Consequently, if no full good p-geodesic exists, then EVERY x∈G must satisfy
  changes(W(x))>=2.

For k=2, this is impossible: every two-symbol word has <=1 internal change. Thus at least 2^(r+1) good full p-geodesics exist, recovering the two fully nonlinear terminal-fault theorem. For k=3, in any hypothetical counterexample the last three actual window colors must ALTERNATE:
  W(x)=(u,1-u,u) for every x∈G.
Here |G|=2^(r+3); in active NORI (r=3), n>=6, this forces exactly 64 prefix-monochromatic roots all to present alternating final-three-window words. The involutive root flip pairs these 64 roots, so their first prefix bit changes but their bad terminal alternation does not.

**Proof of suffix physical-face invariance.** Each last-k r-window contains t among its FREE coordinate directions. If we change just x_t while retaining the same full permutation p, the physical ordered r-face traversed by that window is unchanged: the only potentially changed coordinate is free and its exterior bits are identical. Thus its color is identical under c without linearity. Every early r-window excludes t, so under the common all-one exterior parity reference changing x_t toggles its binary color (the prefix flips in preceding coordinates do not involve t). This establishes both properties and the extraction.

**Research consequence.** The previous k=2 closure is optimal for this simple single-toggle combinatorial argument: with k=3, a three-symbol alternating suffix has two unavoidable internal switches, so toggling the prefix cannot fix it. But the theorem converts a hypothetical grand counterexample for a coloring differing from parity only on three chosen terminal ordered-face types into a very rigid **uniform alternating defect** across 2^(r+3) actual roots. A future adjacent-direction exchange / five-cycle connector argument would need to disallow that defect for all corresponding terminal orders. It is NOT shown impossible by the present lemma. The result does not claim closure for three arbitrary terminal exceptions.
