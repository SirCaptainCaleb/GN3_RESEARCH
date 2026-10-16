# Affine Q4 trap for Fourier ascent under root flips and adjacent swaps

- Stable ID: note_fourier_local_ascent_affine_q4_trap
- Author: unspecified; session provenance retained
- Primary home: subsection:cyclic_variation_selection_for_antipodal_and_boundary_path_galleries
- Labels: counterexample, fourier, affine, local-exchange
- Lifecycle: active
- Epistemic status: proved
- Current version: 4
- Retention: current and at most one previous snapshot
- Created session: session_nori_r9269_1
- Updated session: session_nori_r9269_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

# A four-dimensional affine trap for local Fourier ascent

**Scope:** This note limits a prospective proof strategy based on the sharp first-harmonic objective published in the cyclic variation subsection. It does not challenge NORI1, which holds for this coloring.

Index cube directions by 0,1,2,3. Take the affine antipodally odd coloring
\[
c_0(x)=x_1,\quad
c_1(x)=x_2+1,\quad
c_2(x)=x_1+1,\quad
c_3(x)=x_2 \pmod 2.
\]
Every reader has one off-diagonal variable, so \(c_i(\bar x)=1-c_i(x)\). The reader matrix has rows with bitmasks \((2,4,2,4)\) and offset bitmask \(6\).

Consider the rooted full geodesic starting at \(x=0000\) with direction order \(\pi=(0,2,1,3)\). Its color word is \(0101\), with first-harmonic magnitude
\[
|F_4|=\sqrt{\,4-2\sqrt2\,}
\quad\text{versus the sharp maximum}\quad
M_4=\sqrt{\,4+2\sqrt2\,}.
\]
Its eight root-slide descendants have the color words
\[
\mathcal B=(0101,1011,0110,1101,1010,0100,1001,0010).
\]
All members of \(\mathcal B\) have at least two adjacent color changes, and together they are all eight nonextremal binary words of length four. Every such word has squared harmonic energy \(4-2\sqrt2\).

**Finite local-trap certificate.** At every one of these eight rooted paths, perform any of the four starting-root bit flips or any of the three adjacent direction swaps. Every one of the resulting 56 path words lies again in \(\mathcal B\). The following table lists the sets of results for each root-slide state; repeated words are omitted.

| word | root-bit flips produce | adjacent swaps produce |
|---|---|---|
| 0101 | 0101,1001,0110 | 1001,0101,0110 |
| 1011 | 1011,0010,1101 | 1011,1101 |
| 0110 | 0110,0101,1010 | 1010,0110,0101 |
| 1101 | 1101,1011,0100 | 1101,1011 |
| 1010 | 1010,0110,1001 | 0110,1010,1001 |
| 0100 | 0100,1101,0010 | 0100,0010 |
| 1001 | 1001,1010,0101 | 0101,1001,1010 |
| 0010 | 0010,0100,1011 | 0010,0100 |

The entries follow directly from the displayed four affine edge-color functions. Equivalently, toggling a root bit \(i\) toggles those color-word positions whose direction \(j\) has reader coefficient \(A_{ji}=1\); swapping adjacent directions \(i,j\) transforms their local colors \((a,b)\) into \((b+A_{ji},a+A_{ij})\).

Nevertheless, a one-change witness exists: at root 0000, direction order \((1,0,3,2)\) gives color word \(1100\), which root-slides into a monochromatic full geodesic.

**Conclusion.** No theorem asserting a strict increase of the sharp quadratic Fourier objective by *one* adjacent direction swap or *one* root-bit flip, even after arbitrary root-slide normalization, can hold for all antipodally odd affine colorings. Any ascent-based proof must allow a detour with nonincreasing energy, a more global exchange, or a different potential.

## Nonlinear five-cube obstruction to two-step threshold repair

The following antipodally odd coloring shows that two elementary path operations, even with arbitrary root slides, need not reach a one-change path. Number vertices 0,...,31. For each i, let r=min{x,x xor 2^i,x xor 31,x xor 31 xor 2^i}. Assign color b_i(r) on endpoints r and r xor 2^i, and color 1-b_i(r) on their antipodes. For increasing representative values, the eight bits b_i are:
i=0: 00101000 (reps 0,2,4,6,8,10,12,14);
i=1: 11101101 (0,1,4,5,8,9,12,13);
i=2: 11011010 (0,1,2,3,8,9,10,11);
i=3: 10000000 (0,1,2,3,4,5,6,7);
i=4: 00000011 (0,1,2,3,4,5,6,7).

Root zero and order (0,1,2,3,4) give word 01101. Close its orbit under root slides, then permit up to two successive moves, each either flipping one root bit or transposing adjacent directions, with root slides freely interspersed. The successive reachable sets contain 10,110,610 rooted states, or 1,11,61 root-slide orbits. Of the 61 representative color words, 33 have two changes, 20 have three and 8 have four. There is no one-change word within the two-operation closure. There ARE paths of higher Fourier energy than the starting path: the obstruction concerns two-step attainment, not two-step strict ascent. At distance three, order (0,3,2,1,4) from root zero gives 00011. A monochromatic witness exists at root zero with order (0,3,4,1,2), giving 00000.

The displayed truth tables support finite exhaustive checking of this limitation; the construction does not refute NORI1.


## All-dimensional lower bound on Fourier witness repair distance

**Theorem.** For each \(0<\varepsilon<1/2\) and sufficiently large \(n\), there is an antipodally odd undirected edge coloring of \(Q_n\) which has a monochromatic full geodesic, together with a rooted full geodesic \(P_0\), such that reaching *any* path with at most one color change from \(P_0\) takes more than
\[
r=\left\lfloor(1/2-\varepsilon)n/\log_2 n\right\rfloor
\]
moves. Each move may flip one root bit or transpose adjacent directions; cyclic root slides have zero cost. Thus the required repair radius may be \(\Omega(n/\log n)\) even in positive NORI1 instances.

*Proof.* Starting from a fixed \(P_0\), let \(W_r\) be all rooted paths reachable by at most \(r\) moves and arbitrary interspersed root slides. A root-slide orbit has \(2n\) states; each state has at most \(2n-1\) neighbors under the elementary moves. Consequently
\[
|W_r|\le 2n(1+2n(2n-1))^r
=2^{(1-2\varepsilon)n+o(n)}. \tag{LR1}
\]
For large \(n\), both \(4n|W_r|<2^n\) and \(2n|W_r|<2^n\).

Each antipodal pair of undirected edges carries one freely choosable color bit. Let \(E_r\) be all antipodal edge orbits used by paths in \(W_r\), so \(|E_r|\le n|W_r|\). Fix a direction order \(\pi_*\). For a given orbit \(e\in E_r\), at most four starting roots of \(\pi_*\)-ordered paths can cause their paths to use \(e\), since its four incident vertex/direction descriptions fix the root by subtracting the prefix before that direction. Therefore some root \(x_*\) produces a path \(P_*=(x_*,\pi_*)\) avoiding all orbits in \(E_r\), by \(4n|W_r|<2^n\).

Prescribe the color zero on the \(n\) orbits traversed by \(P_*\), so \(P_*\) is monochromatic. Choose all other orbit bits independently and uniformly. Every path in \(W_r\) uses only free orbits, one from each of its \(n\) different directions, hence has independent fair edge colors. Among the \(2^n\) binary words of length \(n\), precisely \(2n\) have at most one adjacent change. The union bound gives
\[
\Pr(\exists P\in W_r\text{ with at most one change})
\le |W_r|\,2n/2^n<1. \tag{LR2}
\]
Thus a choice of the remaining colors has no one-change path in \(W_r\) while retaining \(P_*\). \(\square\)

**Research implication.** Any general proof by bounded-radius root-bit/adjacent-swap repair toward the sharp first-harmonic threshold is impossible, even if one allows free root slides. A successful Fourier method must use global information or more powerful moves. This theorem does not challenge NORI1.
