# Every fully good cyclic root-slide orbit of longest one-switch paths forces m=4 or 6

# Periodic root-slide orbit obstruction for globally longest one-switch NORI paths

Let n>=5 and let c be ANY binary coloring of ordered three-faces of Q_n (antipodal oddness is not required for this lemma). Let m<n be the maximum length of a cube geodesic whose ordered three-face window-color word has at most ONE change. Since every length-four geodesic has two windows, m>=4. Every length-m good geodesic has exactly one change, since a monochromatic window word could be extended through any unused coordinate and still have at most one change.

Fix an arbitrary root x and an arbitrary ordered set p=(p_1,...,p_m) of m distinct cube coordinates. Form the 2m-step cyclic geodesic circuit
\[
x_0=x,\qquad x_{j+1}=x_j\oplus e_{p_{1+(j\bmod m)}}\quad (0\le j<2m).
\]
Since each coordinate occurs twice, x_{2m}=x; each cyclic m-edge arc from x_j to x_{j+m} changes every coordinate of p exactly once, so it is a genuine m-edge geodesic. Let f_j∈F_2 be the ordered-three-face color of the three consecutive circuit edges beginning at j, with indices modulo 2m.

**Theorem (root-slide orbit cannot be uniformly good, except lengths 4 and 6).** If ALL 2m cyclic m-edge arcs are good (at most one window-color change), then
\[
\boxed{m\in\{4,6\}.}
\]
Moreover, in the two permitted cases their complete 2m-cyclic window-color words are rigid, up to rotation and bit complementation:
- m=4: f=01010101;
- m=6: f=000111000111.

Thus whenever m>=5 and m≠6, EVERY full cyclic root-slide orbit of length-m geodesics contains at least one BAD arc with two or more three-face window-color changes. This applies even to cyclic orbits containing a globally maximal good witness, and is dimension-independent.

**Proof.** Each m-edge arc has h=m-2 consecutive ordered-three-face windows. By global maximality and m<n, if it is good its word has EXACTLY one change. Define cyclic transition indicators
\[
\delta_j=f_j\oplus f_{j+1}\in\{0,1\},\qquad j\pmod{2m}.
\]
Every cyclic m-edge arc has exactly L=h-1=m-3 transitions between its consecutive h windows. If all arcs are good, then for every j
\[
\sum_{k=0}^{L-1}\delta_{j+k}=1
\quad\text{(integer sum).}
\]
Subtracting successive equations gives \delta_j=\delta_{j+L}. Let N=2m and g=gcd(N,L). The cyclic binary sequence \delta has period g, and each L-window consists of L/g copies of a g-block. Its sum is one; hence L/g=1 and the g-block has exactly one entry equal to 1. In particular L|2m and there are exactly 2m/L changes along the complete cycle.

Because the binary word f is itself a closed cyclic word, its number of changes 2m/L must be EVEN. Therefore L divides m. But L=m-3, so L divides 3. Since L>=1, L is 1 or 3, giving m=4 or m=6. The periodicity of \delta with precisely one change per L positions makes f alternate between constant runs of length L, yielding exactly the two asserted periodic patterns. QED.

**Exact local root-slide defect dynamics.** Let P be a length-m good geodesic, with h=m-2 windows and its one switch located between positions s and s+1 (1<=s<h). Write a=w_1 and b=w_h=1-a.
- Forward root slide drops the first window and appends one new window color t. If s>1, the new arc is good exactly when t=b; its switch position becomes s-1 and its first color stays a. If s=1, the new arc is AUTOMATICALLY good, so maximality forces t≠b; its switch jumps to position h-1 and its first color becomes b=1-a.
- Backward root slide prepends a new window color u and drops the last. If s<h-1, the new arc is good exactly when u=a; its switch position becomes s+1 and its first color stays a. If s=h-1, the new arc is AUTOMATICALLY good, so maximality forces u≠a; its switch jumps to position 1 and its first color becomes 1-a.

These are exact finite-memory transition laws. Each boundary reflection flips the first-color polarity, while each interior switch translation preserves it. A complete orbit of good root slides would require an even number of boundary reflections, precisely the divisibility obstruction above.

**Scope.** This theorem concerns the ACTIVE NORI ordered-three-face one-switch structure and does not rely on reducing to edge colors. It yields a forced global root-slide defect for every maximum m outside {4,6}; converting such a defect into an extension or a color-free reachability coincidence is still an open forcing problem.

## Quantitative root-slide obstruction: asymptotically one third of maximal arcs are bad

Retain the hypotheses that m<n is the global maximum good one-switch geodesic length, and assume m>=7. For ANY 2m-cyclic root-slide orbit above, let N=2m, L=m-3, let \delta_j=f_j⊕f_{j+1}, and let
\[
a_j=\sum_{k=0}^{L-1}\delta_{j+k}.
\]
An arc is good exactly when a_j=1; it is bad exactly when a_j>=2. The possibility a_j=0 is excluded: it would give a monochromatic length-m window word, which can be extended to a good length-(m+1) path. Let B denote the number of bad arcs, and t=\sum_j\delta_j the total number of cyclic window-color switches.

**Theorem.** For every m>=7, EVERY root-slide orbit satisfies
\[
\boxed{B\ge\max\left\{2,\ \left\lceil\frac{2m-12}{3}\right\rceil\right\}.}
\]
Consequently at least the same fraction divided by 2m of ALL directed length-m cube geodesics are bad. As m tends to infinity, this fraction has lower limit at least 1/3.

**Proof.** The full 2m-cycle has an even number t of binary switches. Since each length-L window contains at least one switch, double counting the incidences of switches with sliding windows gives Lt=\sum_j a_j>=2m. For m>=7, L=m-3< m, so t>2 and being even satisfies t>=4.

Each good arc contributes 1 to the incidence sum; each bad arc contributes at most t. Therefore
\[
Lt=\sum_j a_j\le (2m-B)+tB=2m+(t-1)B,
\]
giving
\[
B\ge\frac{tL-2m}{t-1}.
\]
For fixed N=2m and L=m-3, the right-hand side is an increasing function of t because its derivative is (N-L)/(t-1)^2>0. Hence, using t>=4,
\[
B\ge\frac{4(m-3)-2m}{3}=\frac{2m-12}{3}.
\]

It remains to show B≠1. If exactly one L-window had at least two switches, its two adjacent L-windows both have exactly one. Sliding the window by one position changes its switch count by at most one, so this unique bad window must have exactly TWO switches. Therefore
\[
Lt=\sum_j a_j=(2m-1)\cdot1+2=2m+1,
\]
which is odd. But t is even, making Lt even. Contradiction. Moreover B=0 is impossible for m>=7 by the preceding root-slide periodicity theorem. Thus B>=2, proving the bound.

Finally, the forward root-slide map is a permutation on the family of ALL directed length-m geodesics. It has orbit length exactly 2m: the cyclic direction word repeats after m shifts while the root moves to its distinct U-antipode, and only after 2m shifts do root and word both return. Thus these orbits partition the full directed path family, and the per-orbit lower bound averages to the same global fraction. QED.

**Research significance.** The global longest-one-switch obstruction forces not just one break, but a positive asymptotic density of bad root-slide states (at least one third) around EVERY maximum-rank geodesic carrier. This provides a quantitative boundary/defect resource for a topological connector or double-counting argument. No restriction to small n or any classification of Q7 is used.
