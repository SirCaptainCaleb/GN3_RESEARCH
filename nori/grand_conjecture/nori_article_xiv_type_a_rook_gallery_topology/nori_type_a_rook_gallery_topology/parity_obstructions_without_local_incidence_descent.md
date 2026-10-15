# Parity obstructions without local incidence descent

# Alternating-word obstructions on type-A and type-B chambers

Put \(\epsilon(\pi)=\operatorname{inv}(\pi)\bmod2\) and \(\operatorname{rot}(\pi)=(\pi_2,\ldots,\pi_n,\pi_1)\). Then
\[
\epsilon(\operatorname{rot}\pi)=\epsilon(\pi)+n-1,\qquad
\epsilon(\pi^{\rm rev})=\epsilon(\pi)+\binom n2\pmod2.
\tag{1}
\]

**Theorem 1 (type-B example).** For \(n\ge7\), \(n\equiv3\pmod4\), prescribe the following word on every root-and-order flag \((x,\pi)\) of an antipodal cube geodesic:
\[
w_j(x,\pi)=j-1+|x|+\epsilon(\pi)\pmod2,\qquad1\le j\le n.
\tag{2}
\]
Each word alternates, so has \(n-1\) switches. Nevertheless, the family obeys
\[
w(x\oplus e_{\pi_1},\operatorname{rot}\pi)
=(w_2,\ldots,w_n,1-w_1),\quad
w(x,\pi^{\rm rev})=\mathbf1-\operatorname{rev}w(x,\pi).
\tag{3}
\]
Every represented geodesic is dimension-simple. The family cannot arise from an undirected cube-edge coloring because it violates (C1), the adjacent-exchange incidence identity.

*Proof.* Rotation of an odd-length permutation preserves its parity, whereas changing the initial root by one dimension flips \(|x|\bmod2\). The new word therefore has letters \(w'_j=j+|x|+\epsilon(\pi)\); they equal \(w_{j+1}\) for \(j<n\) and \(1-w_1\) for \(j=n\). Reversal of the permutation flips parity because \(\binom n2\) is odd. For odd \(n\), reversal preserves the alternating position word, so complementing it gives the stated reversal relation. Finally, any adjacent permutation swap flips \(\epsilon(\pi)\), complementing even the unaffected edge positions, contrary to (C1). \(\square\)

**Theorem 2 (type-A example).** For \(n\ge8\), \(n\equiv0\pmod4\), prescribe on every Hamilton vertex-order flag \(\pi\)
\[
u_j(\pi)=j-1+\epsilon(\pi)\pmod2,\qquad1\le j\le n-2.
\tag{4}
\]
Each word alternates, hence has \(n-3\) switches. Nevertheless,
\[
u_j(\operatorname{rot}\pi)=u_{j+1}(\pi)\ (1\le j\le n-3),
\quad u(\pi^{\rm rev})=\mathbf1-\operatorname{rev}u(\pi).
\tag{5}
\]
The family cannot arise from an ordinary reversal-odd boundary 3-tournament because it violates (T1), the adjacent-exchange shared-triple identity.

*Proof.* Rotation of an even-length permutation changes its parity, giving the cyclic overlap relation in (5). Reversal preserves parity for \(n\equiv0\pmod4\); the alternating word of even length has complementary reversal, yielding the second relation. An adjacent swap complements all word letters, including windows that do not touch the swapped positions, contrary to (T1). \(\square\)

**Corollary.** Full matroid rank, antipodally symmetric type-A or type-B chamber spheres, reversal of color words, and their respective cyclic shift laws do not together force one-switch maximal paths. Counterexamples exist in arbitrarily high dimensions in *both* classes of flag spaces, although neither example descends to a coloring of the shared local incidences. Every proposed unification must include this descent compatibility and employ it in the existence argument.

The formulas were independently checked for thousands of random type-B flags with \(n=7\) and for all \(8!\) type-A flags with \(n=8\).
