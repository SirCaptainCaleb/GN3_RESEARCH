# Logarithmic monochromatic-path obstruction and near-linear switch amplification

# Logarithmic monochromatic geodesics and near-linear compulsory switches

**Theorem (two-sentinel antichain construction).** Fix \(k\ge3\) and \(n\ge k+2\). Put \(N=n-2\) and
\[
m=\min\{d\ge2:\binom d{\lfloor d/2\rfloor}\ge N\}.
\]
There is a legal binary coloring of ordered PHYSICAL \(k\)-faces of \(Q_n\) such that every monochromatic coordinate-distinct geodesic has at most \(3m+3k-4\) edges, while every full antipodal geodesic has at least
\[
\boxed{\max\{0,\lceil(n-3k+1)/(m-1)\rceil-3\}}
\]
switches. In particular, for each fixed \(k\ge3\), the longest monochromatic geodesic can be \(O(\log n)\), and the compulsory switch count can be \((1-o(1))n/\log_2n\).

**Rank-map proof.** Choose \(N\) distinct equal-size subsets \(A_u\subseteq[m]\), indexed by ordinary directions. Define \(\lambda(u,v)=\min(A_u\setminus A_v)\) for \(u\ne v\). For distinct \(u,v,w\), the label \(\lambda(u,v)\notin A_v\), whereas \(\lambda(v,w)\in A_v\), so these two labels are distinct. Put
\[
h(u,v,w)=\mathbf1_{\{\lambda(u,v)<\lambda(v,w)\}}.
\]
A monochromatic run of consecutive \(h\)-triples forces all successive directed-pair labels to strictly increase (color 1) or decrease (color 0). There are only \(m\) possible labels, so such a run contains at most \(m-1\) triple windows. The same statement holds for the reverse rule \(h(w,v,u)\), by reading the word backward.

**Physical coloring and legality.** Adjoin distinct sign and selector directions \(s,t\). For an ordered physical \(k\)-face \((F,\pi)\) with neither sentinel free, let \(g(\pi)=h(\pi_1,\pi_2,\pi_3)\). Assign color \(z_s(F)\oplus g(\pi)\) if \(z_t(F)=0\), or \(z_s(F)\oplus g(\operatorname{rev}\pi)\) if \(z_t(F)=1\). If at least one sentinel is free, assign \(\mathbf1_{\{\pi_1>\pi_k\}}\) using an arbitrary fixed strict order of all coordinate directions. The rule depends only on the genuine physical face and its free-direction order; it never depends on the traversing corner.

Under antipodal reversal both exterior sentinel bits flip, and reversal swaps the two selector alternatives. Thus the chosen \(g\)-term remains unchanged and the XOR sign flips. If a sentinel is free, the distinct first and last ordered free directions exchange, complementing their strict-order comparison. Hence for EVERY physical ordered face,
\[
c(\bar F,\operatorname{rev}\pi)=1-c(F,\pi).
\]

**Monochromatic length.** Delete the at most two sentinel steps from any direction-distinct monochromatic geodesic, splitting ordinary directions into at most three contiguous blocks. Within each block both sentinel bits are fixed. The colors of consecutive ordinary \(k\)-windows therefore reproduce, up to one constant XOR, consecutive \(h\)-triples on either the first three or reversed last three directions of each window. A block of \(b\ge k\) ordinary directions contains \(b-k+1\) such windows, so \(b-k+1\le m-1\), or \(b\le m+k-2\). A shorter block obeys this bound trivially. Adding at most three blocks and two sentinels yields length at most \(3(m+k-2)+2=3m+3k-4\).

**Compulsory switches, with arbitrary interleaving.** In a full \(n\)-direction geodesic, let the at most three ordinary blocks have lengths \(b_i\), with \(\sum_i b_i=n-2\). Block \(i\) contains \(w_i=\max(0,b_i-k+1)\) actual consecutive ordinary physical \(k\)-window colors. Each monochromatic run among those \(w_i\) colors has at most \(m-1\) terms, so its INTERNAL physically adjacent comparisons force at least \(w_i/(m-1)-1\) switches. Those internal comparisons from distinct blocks are disjoint genuine comparisons of the full geodesic's color word; NO addition or noncancellation assumption is made about intervening sentinel windows. Summing gives
\[
\sigma(P)\ge\frac{\sum_i w_i}{m-1}-3
\ge\frac{n-2-3(k-1)}{m-1}-3.
\]
Take a ceiling and the trivial nonnegative bound. Stirling gives \(m=\log_2n+O(\log\log n)\), completing the theorem.

**Relation to the scrapbook snake bound.** The boundary 3-tournament \(\sqrt n\) proof uses reversal antisymmetry at the SAME triple to orient a tournament of terminal-pair competitors. The active NORI axiom relates different ANTIPODAL physical faces instead. Two exterior coordinates legally encode the arbitrary rank-comparison \(h\) and its reverse in complementary charts, refuting a universal \(\Omega(\sqrt n)\) monochromatic-geodesic claim already for NORI3. The universal positive longest-path lower bound and matching extremal switch upper bound are still open; NORI1 and NORI2 are not addressed.

**Verification.** Independently coded tests checked antipodal-reversal legality on every ordered physical \(k\)-face in dimensions \(5\) through \(8\), \(3\le k\le5\) where applicable, using actual exterior bitmasks. Further checks covered randomly rooted coordinate-distinct paths and verified \(\lambda(u,v)\ne\lambda(v,w)\) for ordinary-set sizes \(3\) through \(119\). The proof above is independent of these tests.
