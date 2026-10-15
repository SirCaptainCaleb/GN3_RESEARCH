# Global Petrie switch moment and local-turn counting

# Global Petrie switch moment and local-turn counting

The type-D chamber-tree and Petrie-cycle geometry allows a global first switch moment to be computed by elementary local counts for *every* antipodally odd edge coloring of \(Q_n\). This yields a sufficient condition, expressed entirely in the monochromatic degrees of projective cube vertices, for a monochromatic antipodal geodesic. It also imposes a universal double root on the mod-two global switch-grade enumerator.

Fix \(n\ge3\) and a legal antipodally odd coloring \(c\) of undirected cube edges. Let \(\mathcal P_n\) be the set of all undirected Petrie cycles (antipodal completions of full dimension-simple cube geodesics), and let \(h_c(C)\) be the twisted cyclic switch defect of a Petrie cycle. Put
\[
M_n=|\mathcal P_n|=2^{n-2}(n-1)!.
\tag{1}
\]
For each antipodal vertex pair \([v]=\{v,\bar v\}\), choose either representative and let \(s_v\) be the number of its \(n\) incident cube edges of color one. Because antipodal inversion complements all incident colors, changing representatives replaces \(s_v\) by \(n-s_v\). Therefore the local bichromatic-turn count \(s_v(n-s_v)\) is well defined at the projective vertex. Set
\[
N_c=\sum_{[v]\in V(Q_n)/A}s_v(n-s_v).
\tag{2}
\]

**Theorem 1 (global Petrie first-moment identity).** For every \(n\ge3\) and every legal coloring,
\[
\boxed{
\sum_{C\in\mathcal P_n}(2h_c(C)+1)=(n-2)!\,N_c.
}
\tag{3}
\]
Consequently
\[
\boxed{
\sum_{C\in\mathcal P_n}h_c(C)
=\frac{(n-2)!N_c-M_n}{2}.
}
\tag{4}
\]

*Proof.* A full Petrie cycle has \(2n\) edges. Its edge colors in cyclic order consist of a length-\(n\) binary word \(w\) followed by its bitwise complement, since the coloring is antipodally odd. The number of cyclic color changes around the \(2n\)-cycle is
\[
2\left(\sum_{q=1}^{n-1}[w_q\ne w_{q+1}]+[w_n=w_1]\right)
=2(2h_c(C)+1).
\]
The color changes are paired by antipodal inversion. Their number after dividing by two is therefore the number of bichromatic two-edge turns on the projective Petrie loop, equal to \(2h_c(C)+1\).

For any fixed projective cube vertex \([v]\) and pair of distinct incident dimensions \(i,j\), there are precisely \((n-2)!\) projective Petrie loops using those two incident edges consecutively at \([v]\): choose a lift \(v\), traverse the two specified directions in one prescribed order, and permute the remaining \(n-2\) directions arbitrarily. Reversal gives the same undirected loop, so each permutation determines one such loop and there is no further duplication. This count is independent of the coloring. The number of bichromatic unordered incident-edge pairs at \([v]\) is \(s_v(n-s_v)\). Double-counting the pairs (projective Petrie loop, bichromatic projective turn on that loop) gives (3). Summing the constant one in (3) over the \(M_n\) cycles yields (4). \(\square\)

**Theorem 2 (uniform parity of projective bichromatic turns).** For every \(n\ge3\) and every legal coloring,
\[
\boxed{N_c\equiv0\pmod2.}
\tag{5}
\]

*Proof.* If \(n\) is odd, \(s_v(n-s_v)\) is even for every integer \(s_v\), proving the claim. Let \(n\) be even. Then
\[
N_c=\sum_{[v]}s_v(n-s_v)\equiv\sum_{[v]}s_v\pmod2.
\]
If we change the color on an antipodal orbit of two cube edges, the two corresponding projective endpoint vertices each have one incident bit flipped. Hence \(\sum_{[v]}s_v\pmod2\) is independent of the legal coloring.

Choose the reference legal affine coloring \(c_0(\{x,x\oplus e_d\})=x_{d+1\pmod n}\), with dimension indices \(0,\ldots,n-1\). The selected vertex bit does not change along a direction-\(d\) edge, while antipodal complementation flips it, so this coloring is legal. For each chosen projective representative \(x\) with \(x_0=0\),
\[
s_x\equiv\sum_{d=0}^{n-1}x_{d+1\pmod n}
=\sum_{d=0}^{n-1}x_d\pmod2.
\]
Each free bit among \(x_1,\ldots,x_{n-1}\) occurs as one in \(2^{n-2}\) of these representatives, an even number for \(n\ge3\). Therefore \(\sum_{[v]}s_v\equiv0\), and the claim follows for every legal coloring. \(\square\)

**Corollary 3 (a universally vanishing first mod-two grade moment).** Let
\[
P_c(t)=\sum_{C\in\mathcal P_n}t^{h_c(C)}\in\mathbb F_2[t].
\]
For every legal coloring in dimension \(n\ge4\),
\[
\boxed{P_c(1)=P_c'(1)=0,\qquad (t+1)^2\mid P_c(t).}
\tag{6}
\]

*Proof.* There are \(M_n=2^{n-2}(n-1)!\) cycles, an even number. Thus \(P_c(1)=0\). By Theorems 1--2,
\[
P_c'(1)=\sum_C h_c(C)\pmod2
=\frac{(n-2)!N_c-M_n}{2}\pmod2.
\]
For \(n=4,5\), \(N_c\) is even, so \((n-2)!N_c\) is divisible by four; for \(n\ge6\), the factorial \((n-2)!\) is itself divisible by four. Also \(M_n\) is divisible by four for \(n\ge4\). Therefore \(P_c'(1)=0\). A polynomial over \(\mathbb F_2\) has a double root at one precisely when its value and formal derivative at one vanish, proving (6). \(\square\)

**Corollary 4 (a lower bound on the number of monochromatic Petrie cycles).** Let \(Z_c\) be the number of cycles \(C\in\mathcal P_n\) for which \(h_c(C)=0\), equivalently cycles having a monochromatic full antipodal geodesic among their cyclic root slides. Then
\[
\boxed{
Z_c\ge
\max\left\{0,\frac{3M_n-(n-2)!N_c}{2}\right\}.
}
\tag{7}
\]
In particular,
\[
\boxed{
\frac1{2^{n-1}}\sum_{[v]}s_v(n-s_v)<\frac32(n-1)
\quad\Longrightarrow\quad Z_c>0.
}
\tag{8}
\]
Thus every antipodally odd coloring satisfying (8) has a monochromatic dimension-simple antipodal geodesic, with no additional hypotheses.

*Proof.* A cycle with \(h_c(C)>0\) contributes at least one to \(\sum_Ch_c(C)\). Therefore
\[
M_n-Z_c\le\sum_C h_c(C)
=\frac{(n-2)!N_c-M_n}{2},
\]
which rearranges to (7). There are \(2^{n-1}\) projective vertices; substituting \(M_n=2^{n-2}(n-1)!\) gives (8). A grade-zero Petrie cycle has antiperiodic cyclic switch count one. Sliding its chosen root past this sole twisted switch gives a full geodesic with no ordinary color switches, as established by the root-slide criterion in Article XIV. \(\square\)

**Corollary 5 (necessary local-turn density in a hypothetical NORI1 counterexample).** If a legal coloring has no monochromatic full antipodal geodesic, then
\[
\boxed{
N_c\ge3\cdot2^{n-2}(n-1),\qquad
\frac{N_c}{2^{n-1}}\ge\frac32(n-1).
}
\tag{9}
\]
Any candidate counterexample must therefore have a quantitatively large average number of bichromatic incident-edge pairs per projective vertex.

*Proof.* Such a coloring has \(Z_c=0\), so apply Corollary 4. \(\square\)

**Interpretation and limitations.** The first moment (3) is entirely local, whereas the number of grade-zero Petrie cycles is global; inequality (7) transfers local information into a rigorous global count of dimension-simple monochromatic witnesses. The condition is sufficient, not necessary: for large dimensions it excludes only colorings with relatively few bichromatic local turns, and many legal colorings outside this regime still have monochromatic geodesics. Corollary 3 also shows why a first-order global mod-two moment cannot by itself serve as an equivariant obstruction in dimensions \(n\ge4\). The higher moments of \(P_c(t)\), whose cancellation is not settled by this theorem, remain possible targets for a graded chain construction.


## Pair-turn incidence and the second global switch moment

The first-moment double count above extends to a closed combinatorial count for **pairs** of prescribed projective turns. Unlike an unrestricted graph-walk calculation, the formula respects dimension-simplicity at every stage.

A projective turn is a pair \(\tau=([v],\{i,j\})\), where \([v]\) is an antipodal vertex class and \(i,j\) are distinct incident cube directions. Write \(\delta_c(\tau)=1\) if the two edges have different colors at a lift \(v\). This does not depend on the lift because antipodal inversion complements both edge colors. Let \(\lambda_n(\tau,\upsilon)\) be the number of projective Petrie cycles containing both distinct turns.

For a nonempty finite direction set \(S\), define
\[
L(S;p,q)=
\begin{cases}
1,&|S|=1,\quad p=q\in S,\\
(|S|-2)!,&|S|\ge2,\quad p,q\in S,\quad p\ne q,\\
0,&\text{otherwise}.
\end{cases}
\tag{11}
\]
This counts the permutations of \(S\) beginning with \(p\) and ending with \(q\).

**Theorem 6 (two-turn extension formula).** Let \(n\ge3\) and let \(\tau=([v],\{i,j\})\), \(\upsilon=([w],\{k,l\})\) be distinct projective turns. If \([v]=[w]\), then \(\lambda_n(\tau,\upsilon)=0\). Otherwise choose lifts \(v,w\) and put
\[
D=\{d:v_d\ne w_d\},\qquad E=[n]\setminus D.
\]
If either \(\{i,j\}\) or \(\{k,l\}\) fails to contain one dimension from \(D\) and one from \(E\), then \(\lambda_n(\tau,\upsilon)=0\). In the remaining case let
\[
a=\{i,j\}\cap D,\quad b=\{i,j\}\cap E,\quad
c=\{k,l\}\cap D,\quad d=\{k,l\}\cap E,
\]
where the four symbols denote the uniquely determined dimensions in the singleton intersections. Then
\[
\boxed{\lambda_n(\tau,\upsilon)=L(D;a,c)L(E;d,b).}
\tag{12}
\]
The answer is unchanged if either lift is replaced by its antipode, or if the two turns are interchanged. The formula holds for any binary coloring, since it concerns only complete dimension-simple path incidence.

*Proof.* A projective Petrie cycle containing \([v]\) and \([w]\) has two complementary arcs between these vertices. Lift the cycle from \(v\). One arc ends at the chosen lift \(w\) and traverses precisely the dimensions \(D\), once each; the other ends at the antipodal lift and traverses precisely \(E\). Each prescribed two-edge turn must therefore straddle the partition \(D\sqcup E\), since one incident edge lies on each of the two arcs. This proves the zero cases, including distinct turns at the same projective vertex because a Petrie loop visits each projective vertex only once.

When both turns straddle the partition, orient the \(D\)-arc from \(v\) to \(w\). It begins in direction \(a\) and ends in direction \(c\). The complementary \(E\)-arc from \(w\) back to \([v]\) begins with \(d\) and ends with \(b\). Conversely, choosing any permutation of \(D\) with first letter \(a\) and last letter \(c\), together with any permutation of \(E\) with first letter \(d\) and last letter \(b\), constructs one projective Petrie cycle containing both turns. Each such cycle is reconstructed uniquely by these two arcs; no repeated direction can occur because \(D,E\) partition \([n]\). Thus the number is the product (12). Exchanging lifts swaps the roles of \(D,E\) and reverses arc orientation, leaving the product unchanged. \(\square\)

Let \(M_n=2^{n-2}(n-1)!\), and put
\[
w_c(C)=2h_c(C)+1,\qquad
S_1(c)=\sum_C w_c(C)=(n-2)!\,N_c,
\]
\[
\boxed{S_2(c)=\sum_{\{\tau,\upsilon\}\subseteq\mathcal T}
\lambda_n(\tau,\upsilon)\delta_c(\tau)\delta_c(\upsilon),}
\tag{13}
\]
where \(\mathcal T\) is the set of all projective turns, and the sum is over unordered distinct pairs.

**Theorem 7 (quadratic second-moment identity).** For every unrestricted antipodally odd binary edge coloring of \(Q_n\),
\[
\boxed{
S_2(c)=\sum_{C\in\mathcal P_n}\binom{w_c(C)}2.
}
\tag{14}
\]
Therefore, if
\[
W_n=2\left\lfloor\frac{n-1}{2}\right\rfloor+1
=
\begin{cases}n,&n\text{ odd},\\n-1,&n\text{ even},\end{cases}
\]
and \(Z_c=\#\{C:h_c(C)=0\}\), then
\[
\boxed{
Z_c\ge
\max\left\{0,\,
\frac{2S_2(c)-(W_n+2)S_1(c)+3W_nM_n}
{2(W_n-1)}\right\}.
}
\tag{15}
\]
In particular, the **quadratic local-turn certificate**
\[
\boxed{
2S_2(c)>(W_n+2)(n-2)!\,N_c-3W_nM_n
}
\tag{16}
\]
guarantees a monochromatic full antipodal geodesic for the unrestricted legal coloring class.

*Proof.* Every Petrie loop \(C\) has \(w_c(C)\) bichromatic turns. It contributes \(\binom{w_c(C)}2\) unordered pairs of such turns. Interchanging the order of summation and applying Theorem 6 gives (14).

Every \(w_c(C)\) is an odd number between \(1\) and \(W_n\). Consider
\[
f(w)=(w-3)(W_n-w).
\]
For \(w=1\), this equals \(-2(W_n-1)\); for every other permitted value \(w=3,5,\ldots,W_n\), it is nonnegative. Therefore
\[
\sum_C f(w_c(C))\ge -2(W_n-1)Z_c.
\]
Expanding the left side using \(\sum_Cw_c(C)=S_1\) and
\(\sum_Cw_c(C)^2=S_1+2S_2\) yields
\[
(W_n+2)S_1-2S_2-3W_nM_n\ge-2(W_n-1)Z_c.
\]
Rearranging gives (15), and strict positivity of its numerator gives (16). Grade zero yields a monochromatic full geodesic by the root-slide criterion. \(\square\)

**Corollary 8 (complete determination in dimensions three through six).** For every legal coloring of \(Q_n\) with \(3\le n\le6\), the inequality (15) is an equality without the outer maximum:
\[
\boxed{
Z_c=
\frac{2S_2(c)-(W_n+2)S_1(c)+3W_nM_n}
{2(W_n-1)}.}
\tag{17}
\]
Thus in these dimensions the number of monochromatic Petrie cycles is computable entirely from the one-turn and two-turn color incidence sums of the original cube.

*Proof.* For \(n\le6\), \(W_n\le5\). The permitted turn counts are therefore \(w=1,3,5\) where applicable. The polynomial \(f(w)\) used in Theorem 7 vanishes at every permitted value \(w>1\), and equals \(-2(W_n-1)\) when \(w=1\). The preceding inequality is consequently an equality. \(\square\)

**Corollary 9 (a necessary quadratic restriction on any NORI1 counterexample).** If an unrestricted legal coloring has no monochromatic antipodal geodesic, then
\[
\boxed{2S_2(c)\le(W_n+2)(n-2)!\,N_c-3W_nM_n.}
\tag{18}
\]
This is a restriction on the pairwise correlations among bichromatic turns, sharper in some legal colorings than the first-moment necessary density bound.

*Proof.* Substitute \(Z_c=0\) in (15). \(\square\)

### Affine calibration: an entire grade distribution

The quadratic criterion can outperform the first-moment criterion, but it does not by itself settle the unrestricted problem. The following unrestricted-dimension family makes that distinction transparent.

**Theorem 10 (binomial switch distribution for invertible affine readers).** Index dimensions by \(0,\ldots,n-1\), \(n\ge3\). Let \(L\in GL_n(\mathbb F_2)\) satisfy \(L_{dd}=0\) and \(L\mathbf1=\mathbf1\), and fix any \(a\in\mathbb F_2^n\). Define
\[
c(\{x,x\oplus e_d\})=(Lx)_d+a_d.
\tag{19}
\]
Then \(c\) is a legal antipodally odd undirected edge coloring. For each \(0\le h\le\lfloor(n-1)/2\rfloor\),
\[
\boxed{
\#\{C\in\mathcal P_n:h_c(C)=h\}
=\frac{(n-1)!}{2}\binom{n}{2h+1}.
}
\tag{20}
\]
In particular, **every such coloring has**
\[
\boxed{Z_c=\frac{n!}{2}}
\tag{21}
\]
monochromatic Petrie cycles, or \(2n!\) rooted and oriented monochromatic full antipodal geodesics.

*Proof.* The zero diagonal makes the edge label independent of which endpoint represents its undirected edge. The odd row sums give \(c(Ae)=1-c(e)\). Fix a full dimension order \(\pi\). As its root \(x\) varies through \(\mathbb F_2^n\), the \(n\)-bit path-color word is obtained from \(Lx\) by permuting its rows according to \(\pi\) and adding a fixed order-dependent correction. Invertibility of \(L\) makes this map a bijection from the roots to all binary words of length \(n\).

A binary word has twisted antiperiodic comparison count \(k\) precisely when its \(n\) antiperiodic transition positions form a prescribed odd \(k\)-element subset. There are two words for each such subset, so there are \(2\binom nk\) words with \(k\) comparisons, for each odd \(k\). Summing over \(n!\) dimension orders gives \(2n!\binom nk\) rooted directed geodesics with grade \((k-1)/2\). Every unoriented Petrie cycle has precisely \(4n\) rooted directed representatives, all of that same grade. Division proves (20). Its \(h=0\) specialization gives (21); each grade-zero Petrie cycle supports four monochromatic rooted directed geodesics. \(\square\)

For the cyclic derangement permutation matrix \(L\) with \((Lx)_d=x_{d+1\bmod n}\), Theorem 10 applies in every dimension. At \(n=6\), its bichromatic-turn sum is
\(N_c=240\), precisely the threshold at which Corollary 4's *first-moment* bound becomes zero. Nevertheless (17) gives
\[
\boxed{Z_c=360,}
\tag{22}
\]
a positive certificate supplied by the pair-turn quadratic moment. In dimension seven the same family has \(Z_c=2520\), while the right side of (15) can be zero; hence the quadratic criterion is not universally decisive.

**Interpretation.** The pair-extension kernel (12) is intrinsic to full dimension-simple Petrie cycles. No small-dimensional case assumption enters Theorems 6 or 7. The resulting quadratic certificate is a new necessary obstruction for a hypothetical NORI1 failure and can detect monochromatic witnesses even when the local-turn first moment is inconclusive. The explicit affine benchmark also shows why further progress may require third and higher compatible-turn incidences, or the support-sensitive equivariant chain methods developed elsewhere in Article XIV. These are complementary routes: moments constrain the global distribution, while Smith-transfer and supported-index methods try to force a forbidden degree-zero witness topologically.



## Higher-order turn extensions and moment certificates

The pair-incidence kernel admits a finite extension to any prescribed family of projective turns. The important point is that *every segment of the extension traverses a disjoint set of cube directions*, so the construction never leaves the class of complete dimension-simple antipodal geodesics.

Let \(\mathcal T_n\) denote the projective turns \(\tau=([v],\{i,j\})\), and let \(\Lambda_n(\tau_1,\ldots,\tau_k)\) denote the number of projective Petrie cycles containing all the listed distinct turns, \(1\le k\le n\). If two distinct listed turns have the same projective vertex, put \(\Lambda_n=0\).

Fix one distinguished turn \(\tau_1=([v_1],\{p,q\})\), with \(p<q\), and choose its lift \(u_1=v_1\). At this turn prescribe the outgoing direction \(\beta_1=p\) and incoming direction \(\alpha_1=q\). Consider all \((k-1)!\) orders of the remaining turns, and independently choose either lift of each of their projective vertices, giving vertices \(u_2,\ldots,u_k\); close with \(u_{k+1}=\bar u_1\). Put
\[
D_j=\{d:(u_j)_d\ne(u_{j+1})_d\},\quad1\le j\le k.
\tag{23}
\]
Discard the choice unless the \(D_j\) are nonempty, pairwise disjoint, and partition \([n]\). At each intermediate prescribed turn \(\tau_j\), require that precisely one of its incident directions belongs to \(D_{j-1}\) and the other to \(D_j\). Call these uniquely defined incoming and outgoing dimensions \(\alpha_j\) and \(\beta_j\), respectively. Also require \(\beta_1\in D_1,\alpha_1\in D_k\), and put \(\alpha_{k+1}=\alpha_1\). Write \(L\) for the endpoint-permutation kernel from (11).

**Theorem 11 (all-order dimension-simple turn-extension kernel).** With the preceding conventions,
\[
\boxed{
\Lambda_n(\tau_1,\ldots,\tau_k)=
\sum_{\substack{\text{orders of }\tau_2,\ldots,\tau_k\\
\text{choices of their lifts}\\
\text{compatible disjoint }D_j}}
\ \prod_{j=1}^{k}L(D_j;\beta_j,\alpha_{j+1}).
}
\tag{24}
\]
There are at most \((k-1)!2^{k-1}\) candidate terms. In particular \(k=1\) yields \((n-2)!\), \(k=2\) recovers Theorem 6, and \(k=3\) has at most eight terms. The formula is independent of the coloring and valid in every cube dimension \(n\ge3\).

*Proof.* A projective Petrie cycle containing \(\tau_1\) has a unique orientation in which it exits the chosen vertex along the smaller of the two directions \(p,q\). With that orientation fixed, its other prescribed turns occur in one cyclic order. Starting at the chosen lift \(u_1\), the unique lift of this oriented projective loop visits one lift of each other prescribed vertex and ends at \(\bar u_1\), since its complete edge word traverses every dimension once. The dimensions traversed between successive prescribed vertices are the nonempty disjoint sets \(D_j\) of (23). At a prescribed turn, the entering and leaving dimensions lie in its two successive segment sets. The internal dimension permutation of segment \(j\) must begin with \(\beta_j\) and end with \(\alpha_{j+1}\), and it has \(L(D_j;\beta_j,\alpha_{j+1})\) choices. Conversely, any choice counted by (24) concatenates into a full length-\(n\) path with disjoint direction sets, hence a dimension-simple antipodal geodesic; its projective Petrie loop contains all the prescribed turns. The fixed outgoing direction at \(\tau_1\) removes the twofold orientation ambiguity, so no cycle is counted twice. \(\square\)

**Theorem 12 (all factorial switch moments from turn incidence).** For \(0\le k\le n\) define
\[
S_k(c)=\sum_{C\in\mathcal P_n}\binom{w_c(C)}{k},
\quad w_c(C)=2h_c(C)+1.
\]
Then
\[
\boxed{
S_k(c)=
\sum_{\{\tau_1,\ldots,\tau_k\}\subseteq\mathcal T_n}
\Lambda_n(\tau_1,\ldots,\tau_k)
\prod_{j=1}^k\delta_c(\tau_j).
}
\tag{25}
\]
The convention \(S_0=M_n\) applies. Consequently the complete switch-grade distribution can be reconstructed from finite collections of locally specified bichromatic turns, using only dimension-simple extension counts.

*Proof.* For every cycle, selecting \(k\) of its \(w_c(C)\) bichromatic turns can be counted either from that cycle or by first selecting the turn family and then counting the complete cycles containing it. The latter multiplicity is given by Theorem 11. \(\square\)

### A rank-three obstruction to pairwise gluing

**Theorem 13 (three pairwise extendable turns without a joint extension).** In \(Q_6\) consider the three projective turns
\[
\boxed{
\tau_1=([0],\{0,1\}),\qquad
\tau_2=([17],\{2,4\}),\qquad
\tau_3=([30],\{3,5\}).
}
\tag{26}
\]
Their two-turn extension counts satisfy
\[
\boxed{\Lambda_6(\tau_1,\tau_2)
=\Lambda_6(\tau_1,\tau_3)
=\Lambda_6(\tau_2,\tau_3)=2,}
\tag{27}
\]
yet
\[
\boxed{\Lambda_6(\tau_1,\tau_2,\tau_3)=0.}
\tag{28}
\]

*Proof.* The pair counts follow from (12): the relevant Hamming-difference partitions have sizes two and four, their required endpoint dimensions belong to opposite parts, and their internal endpoint constraints leave \(0!\,2!=2\) complete extensions.

Suppose a projective Petrie loop contained all three turns. The three incident-dimension pairs in (26) are disjoint and together comprise all six directions. Consequently none of the three specified turn vertices is adjacent along the loop to another: adjacent turns would share an intervening direction. On a six-edge projective Petrie loop the three vertices must therefore occupy alternating positions, so their three successive arcs have length two each. The only possible direction sets of these projective two-step arcs, obtained by taking the shorter Hamming-difference set between the corresponding vertex classes, are
\[
\{0,4\}\quad\text{between }[0],[17],
\qquad
\{4,5\}\quad\text{between }[17],[30],
\qquad
\{0,5\}\quad\text{between }[30],[0].
\]
These sets repeat directions \(0,4,5\) and omit \(1,2,3\). They cannot form a dimension-simple full loop, which must traverse every direction once. Contradiction. \(\square\)

This example is a rank-three compatibility failure in the **unrestricted, color-independent** family of complete cube geodesics. It prevents replacing higher-turn incidence with mere pairwise compatibility. It is distinct from the coloring-dependent rank-three Freudenthal carrier defects discussed elsewhere in Article XIV.

### Third and higher moment certificates

**Theorem 14 (universal odd-order moment hierarchy).** For any odd positive integer \(r\), let
\[
G_r(w)=\prod_{j=1}^{r}\bigl(w-(2j+1)\bigr).
\tag{29}
\]
Then every legal antipodally odd coloring of \(Q_n\) satisfies
\[
\boxed{
Z_c\ge \max\left\{0,\,
-\frac{1}{2^r r!}\sum_{C\in\mathcal P_n}G_r(w_c(C))
\right\}.
}
\tag{30}
\]
The expression on the right depends only on the local-turn moments \(S_0,\ldots,S_r\) from Theorem 12. Whenever \(W_n\le2r+1\), equality holds before applying the outer maximum.

For \(r=3\), put \(S_3=\sum_C\binom{w_c(C)}3\). Then
\[
\boxed{
Z_c\ge
\max\left\{0,\,
\frac{105M_n-57S_1(c)+24S_2(c)-6S_3(c)}{48}\right\}.
}
\tag{31}
\]
For every \(3\le n\le8\), the right-side fraction in (31) equals \(Z_c\), without the maximum. Thus the number of monochromatic Petrie cycles in dimensions seven and eight is determined by the first **three** local-turn moments.

*Proof.* The only allowed turn counts are the positive odd integers \(1,3,\ldots,W_n\). At \(w=1\), \(G_r(1)=(-2)^r r!=-2^r r!\) because \(r\) is odd. At every other allowed value \(w\), either one of the factors vanishes (when \(w\le2r+1\)) or all factors are positive. Hence
\[
\sum_C G_r(w_c(C))\ge -2^r r!\,Z_c,
\]
which rearranges to (30), with equality when \(W_n\le2r+1\).

For \(r=3\),
\(G_3(w)=w^3-15w^2+71w-105\). Since
\[
\sum_C w_C^2=S_1+2S_2,\qquad
\sum_C w_C^3=S_1+6S_2+6S_3,
\]
we obtain
\(\sum_CG_3(w_C)=6S_3-24S_2+57S_1-105M_n\).
This proves (31). For \(n\le8\), \(W_n\le7\), so the equality clause applies. \(\square\)

**Research consequence.** The dimension-simple Petrie path family has an explicit complete hierarchy of local-turn incidence kernels, with nontrivial compatibility already at rank three. The quadratic and cubic moment certificates provide increasingly sensitive necessary constraints on hypothetical NORI1 counterexamples. They do not, by themselves, force grade zero for every coloring; the affine binomial family already shows that low moments can have vanishing certificates despite many favorable cycles. The natural next problem is to identify topological or antipodal inequalities among the locally defined moments, rather than only evaluating them. Such inequalities would preserve unrestricted legal colorings and complete dimension-simple witnesses throughout.



**Corollary 15 (hereditary rank-three incompatibility in every higher cube).** For every \(n\ge6\), embed the three turns from (26) into \(Q_n\) by using the same six directions and appending zero bits to each displayed vertex representative. Each pair still belongs to at least one complete dimension-simple Petrie cycle of \(Q_n\), but no Petrie cycle contains all three:
\[
\boxed{\Lambda_n(\tau_a,\tau_b)>0\quad(a\ne b),
\qquad \Lambda_n(\tau_1,\tau_2,\tau_3)=0.}
\tag{32}
\]
Thus pairwise extendability is not sufficient for joint dimension-simple turn compatibility in any dimension \(n\ge6\).

*Proof.* Every pair remains compatible by Theorem 6. The Hamming-difference partitions of its two projective vertices have sizes \(2,n-2\) or \(4,n-4\), and each prescribed pair of incident dimensions straddles the partition with different prescribed entry and exit dimensions in every part of size at least two. Both permutation factors in (12) are therefore positive for \(n\ge6\).

Suppose a complete geodesic in \(Q_n\) contained all three prescribed turns. Delete its steps in the \(n-6\) additional directions and project all vertices onto the first six bit positions. Because every original direction is used once, the resulting six-edge path is a full dimension-simple antipodal geodesic in \(Q_6\). Both directions at each prescribed turn belong to the first six, so their adjacency survives deletion; and antipodally paired vertices project to antipodally paired six-bit vertices. The projected Petrie cycle would therefore contain the three turns (26), contradicting Theorem 13. \(\square\)

This is a dimension-independent obstruction to inferring common complete-path compatibility from its pairwise restrictions. The extra dimensions do not rescue the three incompatible turns, because restriction to their six supporting dimensions preserves all three prescribed local incidences.



## Uniform odd-cycle marginals across the full legal coloring space

The cographic switch presentation in the preceding cubical-curvature section gives a sharp probabilistic calibration for the global turn-moment formulas. The calibration is over **every** legal antipodally odd coloring, not a restricted family.

Write \(m=n2^{n-2}\) for the number of antipodal cube-edge orbits, \(M=2^{n-2}(n-1)!\) for the number of projective Petrie cycles, and \(h_c(C)\) for the twisted switch grade of \(C\). Give the \(2^m\) legal colorings the uniform distribution.

**Theorem 16 (universal odd-word law).** For every fixed projective Petrie cycle \(C\), its vector of \(n\) projective turn comparisons is uniformly distributed over the \(2^{n-1}\) binary words with odd sum. Consequently
\[
\boxed{\Pr[h_c(C)=j]=2^{-(n-1)}\binom{n}{2j+1}}
\qquad (0\le j\le\lfloor(n-1)/2\rfloor).
\tag{33}
\]
The number of legal colorings for which a fixed cycle has grade \(j\) is \(2^{m-n+1}\binom n{2j+1}\). In particular, a fixed Petrie cycle contains a monochromatic full geodesic with probability \(n/2^{n-1}\).

*Proof.* By the projective line-graph theorem, the switch vectors of all legal colorings form one affine translate of the cut space of the projective line graph \(H=L(Q_n/A)\). A fixed projective Petrie cycle \(C\) becomes a simple cycle of length \(n\) in \(H\): its vertices are the \(n\) distinct projective cube-edge orbits, and its edges are their consecutive incident-turn pairs. A uniformly chosen vertex potential on \(H\) induces every even-parity comparison vector on that cycle with equal multiplicity. Adding the fixed odd-period signature gives every odd-parity comparison vector with equal multiplicity. Dividing by the \(2^{n-1}\) possible odd words proves (33), and multiplying by \(2^m\) gives the counting formula. Grade zero corresponds to a single active turn, with \(n\) possible positions. \(\square\)

**Corollary 17 (the affine binomial law is the universal mean).** Let \(Z_j(c)=\#\{C\in\mathcal P_n:h_c(C)=j\}\). Then
\[
\boxed{\mathbb E_c Z_j(c)=\frac{(n-1)!}{2}\binom n{2j+1},\qquad
\mathbb E_c Z_0(c)=\frac{n!}{2}.}
\tag{34}
\]
In particular, the full grade histogram of every invertible affine-reader coloring in Theorem 10 agrees, grade by grade, with the expectation over **all** unrestricted legal colorings.

*Proof.* Sum the probabilities (33) over all \(M=2^{n-2}(n-1)!\) Petrie cycles. The resulting factor is \(M/2^{n-1}=(n-1)!/2\), giving (34). Theorem 10 establishes the same values without expectation for each invertible affine-reader coloring. \(\square\)

**Scope.** Uniform positive expectation alone does not force \(Z_0(c)>0\) for each coloring: there could in principle be exceptional colorings with zero favorable cycles compensated by others with more. The theorem identifies the affine binomial distributions as fully representative of the *first marginal* on every distinguished full path and of the ensemble-mean global histogram. To strengthen it toward NORI1 would require control of correlations between the events that different Petrie cycles have only one active turn. The rank-three turn-incidence obstructions earlier in this Subsection show that those correlations cannot be reduced to independent local switches.



## Directional switch incidence and rigidity

For a legal odd coloring \(c\) of \(Q_n\), let \(c_i(x)\) be the color of the direction-\(i\) edge incident with \(x\), and let \(N_i\) count the active projective turns containing direction \(i\). Put \(g_i(x)=(-1)^{c_i(x)}\). Thus \(g_i\) is independent of \(x_i\) and satisfies \(g_i(\bar x)=-g_i(x)\).

**Theorem 18.** For every \(n\ge3\) and every direction \(i\),
\[
\boxed{N_i\ge2^{n-2}.}
\]
Equality for any one \(i\) holds if and only if there exist \(k\ne i\) and \(a\in\mathbb F_2\) such that
\[
\boxed{c_d(x)=x_k+a\quad\text{for every }d\ne k,}
\]
while direction-\(k\) edges have arbitrary legal odd colors. Such a coloring makes **every** complete Petrie cycle have one active turn.

More quantitatively,
\[
\boxed{N_i\ge2^{n-2}\left(1+
\sum_{\substack{|S|\ge3\\|S|\text{ odd}}}
(|S|-1)\widehat g_i(S)^2\right).}
\]

*Proof.* At a uniform cube vertex \(x\), put \(p_{ij}=\Pr[g_i(x)\ne g_j(x)]\). Since \(g_j(x)=g_j(x\oplus e_j)\), every pair where \(g_i\) changes under \(e_j\) contains at least one endpoint disagreeing with \(g_j\). Hence
\(p_{ij}\ge\frac12\operatorname{Inf}_j(g_i)\).
Counting projective vertices gives
\[
N_i=2^{n-1}\sum_{j\ne i}p_{ij}
\ge2^{n-2}\sum_{j\ne i}\operatorname{Inf}_j(g_i).
\]
The antipodal oddness of \(g_i\) eliminates its even Fourier levels, while independence of \(x_i\) removes that variable. Parseval and the influence identity yield
\[
\sum_{j\ne i}\operatorname{Inf}_j(g_i)
=1+\sum_{|S|\ge3}(|S|-1)\widehat g_i(S)^2.
\]
This proves both bounds. Equality implies \(g_i\) has Fourier degree one, so the Boolean equation \(g_i^2=1\) forces \(g_i=\pm(-1)^{x_k}\) for some \(k\ne i\). For every \(j\notin\{i,k\}\), its influence in direction \(j\) vanishes; equality in the comparison bound then forces \(g_j=g_i\) everywhere. Conversely this one-direction seam coloring attains equality, regardless of the odd color on its direction-\(k\) edges.

On any full geodesic, the non-\(k\) edge colors before dimension \(k\) are \(x_k+a\), and afterward are their complements. The \(k\)-edge color equals one of these values, so the full word changes at most once. Its antipodally completed projective cycle has precisely one active turn. \(\square\)

**Corollary 19.** Attaining the directional lower bound for even one dimension forces the global minimum total turn support \(N_c=2^{n-2}(n-1)\), and all Petrie cycles have switch grade zero. The Fourier formula also bounds the mass of \(g_i\) on levels above one by \((N_i/2^{n-2}-1)/2\).

## Fourier cancellation under antipodal Petrie rotation

The first and second switch-moment identities above may also be approached by expanding the *monochromatic-path indicator* on each individual Petrie cycle. The resulting cancellation supplies a high-order constraint on legal color repairs.

Fix \(n\ge3\). A projective Petrie cycle \(C\) has an oriented lift consisting of \(2n\) consecutive cube edges. Denote the color-zero spin values of its first \(n\) edges by \(t_0,\ldots,t_{n-1}\in\{-1,+1\}\), where \(t_j=(-1)^{c(e_j)}\). The spins on the following \(n\) edges are \(-t_0,\ldots,-t_{n-1}\). Each length-\(n\) cyclic window is an undirected antipodal full geodesic, and there are \(2n\) distinct windows when \(n\ge3\). Let \(Z_C(t)\) be the number of these windows whose edges all have color zero.

**Theorem (Petrie packet Fourier formula).** For every projective Petrie cycle,
\[
\begin{aligned}
Z_C(t)
&=2^{-n}\sum_{k=0}^{n-1}
\left[
\prod_{j<k}(1-t_j)\prod_{j\ge k}(1+t_j)
+\prod_{j<k}(1+t_j)\prod_{j\ge k}(1-t_j)
\right]\\
&=\sum_{S\subseteq\{0,\ldots,n-1\}}\widehat Z_C(S)\prod_{j\in S}t_j,
\end{aligned}
\tag{PF1}
\]
where
\[
\boxed{
\widehat Z_C(S)=
\begin{cases}
2^{1-n}\displaystyle\sum_{k=0}^{n-1}(-1)^{|S\cap\{0,\ldots,k-1\}|},&|S|\ \mathrm{even},\\
0,&|S|\ \mathrm{odd}.
\end{cases}}
\tag{PF2}
\]
Moreover \(Z_C\) takes only the values zero and one, with value one precisely when the projective cyclic color word has a single twisted switch. For \(S=\{a,b\}\), \(0\le a<b<n\),
\[
\boxed{\widehat Z_C(\{a,b\})=2^{1-n}\bigl(n-2(b-a)\bigr).}
\tag{PF3}
\]

*Proof.* For \(0\le k<n\), the forward length-\(n\) window beginning at position \(k\) reads spins \((t_k,\ldots,t_{n-1},-t_0,\ldots,-t_{k-1})\); the opposite window has their negatives. The indicator that all the window spins are \(+1\) is the corresponding product of factors \((1+t)/2\). Adding the two opposite windows gives the first line of (PF1). In the expansion of a monomial \(\prod_{j\in S}t_j\), the two opposite windows cancel for odd \(|S|\) and add for even \(|S|\). For an even subset, the window at shift \(k\) contributes the sign \((-1)^{|S\cap\{0,\ldots,k-1\}|}\), proving (PF2).

Two different zero-colored windows are impossible: moving the start of an all-zero window forward by \(1\le k<n\) replaces its first \(k\) zero edges with their antipodal complementary one edges; the same argument with the shorter reverse shift covers all other cyclic offsets. Hence \(Z_C\in\{0,1\}\). A zero window exists precisely when the antiperiodic cyclic word has one projective color transition. For a two-element set \(\{a,b\}\), the prefix-intersection parity is odd for the \(b-a\) indices \(a<k\le b\), and even at the remaining \(n-(b-a)\) indices. Substitution into (PF2) gives (PF3). \(\square\)

**Theorem (global degree drop and high-order restoration cancellation).** For a legal antipodally odd coloring \(c\), let \(F_n(c)\) be its number of unoriented monochromatic-zero antipodal full geodesics. Give each antipodal orbit of cube edges an independent spin variable \(s_q\in\{-1,+1\}\), so the spin on its antipodal mate is \(-s_q\). Then the unique multilinear polynomial representing \(F_n\) in these variables has degree at most
\[
\boxed{D_n=2\left\lfloor\frac{n-1}{2}\right\rfloor
=\begin{cases}n-2,&n\ {\rm even},\\n-1,&n\ {\rm odd}.\end{cases}}
\tag{PF4}
\]
For distinct antipodal edge orbits \(q_1,\ldots,q_r\) with \(r>D_n\), and every legal \(c\),
\[
\boxed{
\sum_{U\subseteq[r]}(-1)^{r-|U|}
F_n\!\left(c^{\{q_j:j\in U\}}\right)=0.
}
\tag{PF5}
\]
In particular every \(n\)-fold repair interaction vanishes; when \(n\) is even, every \((n-1)\)-fold repair interaction vanishes as well.

*Proof.* Each complete geodesic reads every direction once, so the first \(n\) observations of a Petrie cycle use distinct antipodal edge orbits. Its packet polynomial (PF1) is therefore multilinear in distinct global orbit spins, up to fixed spin signs. By (PF2), all odd Fourier degrees vanish. Its degree-\(n\) coefficient vanishes when \(n\) is even: for \(S=\{0,\ldots,n-1\}\), the inner sum is \(\sum_{k=0}^{n-1}(-1)^k=0\). When \(n\) is odd, degree \(n\) is already excluded by odd parity. The degree bound (PF4) follows by adding packet polynomials over all projective Petrie cycles, each unoriented full geodesic belonging to one such cycle. A flip of orbit \(q\) changes the sign of \(s_q\). Every multilinear monomial of degree at most \(D_n\) is annihilated by an iterated finite difference in more than \(D_n\) distinct variables, yielding (PF5). \(\square\)

**Corollary (quadratic reduction in dimension four).** A four-dimensional packet has
\[
\boxed{
Z_C(t)=\frac12+\frac14
(t_0t_1+t_1t_2+t_2t_3-t_0t_3).
}
\tag{PF6}
\]
Thus the full path-count function \(F_4\) is quadratic in the sixteen legal edge-orbit spins, and all its triple and higher mixed repair differences vanish. Formula (PF6) has been independently checked on all \(2^4\) packet spin assignments; the global packet decomposition and formula have been checked on sampled legal \(Q_4\) colorings.

**Implication for closure.** A hypothetical bad coloring has \(F_n=0\), and the pair-restoration theorem gives positive values at selected nearest-neighbor recolorings. The mixed-direction repair values are now constrained by (PF5), in addition to the single-direction additivity proved in the restoration-fan manuscripts. These equalities impose higher-order compatibility across color repairs without a selected root or endpoint seam. They do not by themselves force a positive value at the original coloring: a nonnegative low-degree multilinear polynomial may vanish at a vertex while being positive on all its neighbors. A completing theorem must couple these spectral cancellations to the incidence geometry of the cube's Petrie packets or to an appropriate topological nonvanishing principle.

## A factorial kernel for the quadratic restoration interaction

Let \(F_n(c)\) count unoriented monochromatic-zero full antipodal geodesics in a legal odd coloring of the undirected edges of \(Q_n\). For each antipodal edge orbit \(q=\{e,\bar e\}\), select one edge \(e_q\) and define its spin \(s_q=(-1)^{c(e_q)}\). The multilinear Fourier expansion of \(F_n\) has a closed degree-two component.

**Theorem (two-edge factorial kernel).** For \(n\ge3\), the constant coefficient of \(F_n\) is \(n!/2\); all odd-degree coefficients vanish. Two orbits in the same direction have quadratic coefficient zero. For orbits in distinct directions \(i,j\), choose representative edges, after a cube translation, of the form
\[
e=\{0,e_i\},\qquad f=\{y,y\oplus e_j\},\qquad y_i=y_j=0.
\]
Let \(k\) be the number of ones among the \(n-2\) bits of \(y\) outside \(i,j\), and let \(\ell=n-2-k\). Relative to the spins of these representatives,
\[
\boxed{\widehat F_n(\{[e],[f]\})
=2^{1-n}(\ell-k)k!\ell!
=2^{1-n}(n-2-2k)k!(n-2-k)!.}
\tag{FK1}
\]

*Proof.* Every unoriented full geodesic uses \(n\) distinct edge orbits, and its all-zero indicator is \(2^{-n}\prod_{q\in P}(1+\varepsilon_{P,q}s_q)\), where \(\varepsilon_{P,q}\) records the antipodal lift used by the geodesic. There are \(2^{n-1}n!\) such paths, so their constant contribution is \(n!/2\). Simultaneously negating all spins exchanges zero and one paths, which are equinumerous by cube antipodality. This eliminates all odd Fourier degrees. Each path uses any one direction only once, so two orbits of the same direction never appear together.

For the other coefficients let \(K\) be the \(k\) far directions where the two prescribed edges differ, and \(L\) the remaining \(\ell\) directions outside \(i,j\). A directed full geodesic containing the prescribed \(e\) before \(f\) must traverse all \(K\)-directions between these edges; each \(L\)-direction can occur before both or after both. For any choice of \(a\) early \(L\)-directions the number of orders is \(\binom{\ell}{a}a!k!(\ell-a)!=\ell!k!\). Summing over \(a=0,\ldots,\ell\) gives \((\ell+1)\ell!k!\). Reversing the temporal order of the two prescribed edges gives the same number. Upon identifying opposite path orientations, \((\ell+1)\ell!k!\) unoriented geodesics contain \(e,f\).

Replacing \(f\) by its antipodal mate exchanges \(K,L\), leaving \((k+1)\ell!k!\) unoriented paths containing \(e,\bar f\). Antipodality doubles both populations with their respective spin-product signs, so the signed path count is
\(2[(\ell+1)-(k+1)]k!\ell!=2(\ell-k)k!\ell!\).
Each term contributes \(2^{-n}\), establishing (FK1). \(\square\)

**Corollary (projective equator and the four-cube positive certificate).** When \(n\) is even, the coefficient (FK1) vanishes for \(k=(n-2)/2\); otherwise its sign distinguishes the two sides of this middle rank. The integer sequences \(2^{n-1}\widehat F_n(k)\), for \(k=0,\ldots,n-2\), begin
\[
\begin{array}{c|c}
n&\text{sequence}\\
4&(4,0,-4)\\
5&(18,2,-2,-18)\\
6&(96,12,0,-12,-96)\\
7&(600,72,12,-12,-72,-600).
\end{array}
\tag{FK2}
\]
These values were independently enumerated over the projective Petrie cycles through dimension seven.

In \(Q_4\), every nonzero quadratic coefficient comes from edge orbits meeting at a projective cube vertex. The prior Fourier-degree bound gives \(\deg F_4\le2\). Let \(r_v\) count the one-colored edges incident to a representative of the antipodal vertex class \([v]\). Then
\[
\boxed{F_4(c)=4+\sum_{[v]}(r_v-2)^2\ge4.}
\tag{FK3}
\]
Indeed the four incident spins \(u_i\) give \((r_v-2)^2=\frac14(\sum_i u_i)^2=1+\frac12\sum_{i<j}u_iu_j\). Summing over the eight projective vertex classes reproduces all quadratic terms by (FK1), and the constant \(4+8=12=4!/2\). Hence the multilinear polynomials agree.

**Corollary (mean two-pair repair synergy).** Fix two orbit spins and randomize all remaining spins independently. If \(F^{ab}\) counts zero geodesics with the two fixed spins \(a,b\in\{\pm1\}\), then
\[
\boxed{\mathbb E_{\rm others}[F^{++}-F^{+-}-F^{-+}+F^{--}]=4\widehat F_n(\{q,r\}).}
\tag{FK4}
\]
*Proof.* The displayed difference kills all terms omitting either chosen variable; expectation kills every term involving any additional variable. The degree-two term survives with multiplier four. \(\square\)

The quadratic restoration effect is therefore governed by a signed, translation-invariant factorial kernel on pairs of projective edge orbits. The positivity certificate (FK3) exhausts the polynomial in dimension four. Higher even-degree terms remain in larger dimensions, and coupling them to (FK1) is the outstanding step toward a strict positive certificate.

## Complete Walsh diagonalization of the quadratic geodesic-count polynomial

The factorial two-edge kernel admits a closed Walsh transform. This diagonalizes the entire quadratic sector and gives a sharp universal lower bound, together with explicit legal colorings demonstrating why the quadratic sector alone cannot establish unrestricted NORI1.

For each direction \(i\) represent its undirected-edge coloring by the spin function
\[
f_i:\{0,1\}^{[n]\setminus\{i\}}\longrightarrow\{-1,+1\},\qquad
f_i(x)=(-1)^{c(\{x,x\oplus e_i\})}.
\]
Antipodal oddness reads \(f_i(\bar x)=-f_i(x)\). Let \(\chi_T(x)=(-1)^{\sum_{j\in T}x_j}\), and define normalized Walsh coefficients
\[
a_{i,T}=2^{-(n-1)}\sum_{x_i=0}f_i(x)\chi_T(x)
\qquad(T\subseteq[n]\setminus\{i\}).
\]
Thus \(a_{i,T}=0\) for even \(|T|\), and Parseval gives \(\sum_{T\not\ni i}a_{i,T}^2=1\). Write \(Q_n(c)\) for the constant-plus-degree-two Fourier truncation of the monochromatic-zero full-geodesic count \(F_n(c)\) in independent antipodal edge-orbit spin variables.

**Lemma (factorial Hamming-kernel transform).** Let \(d\ge1\), \(K_d(z)=(d-2|z|)|z|!(d-|z|)!\), and \(T\subseteq[d]\), \(t=|T|\). Then
\[
\boxed{
\sum_{z\in\{0,1\}^d}K_d(z)\chi_T(z)
=\begin{cases}
(d+2)!/(t+2),&t\text{ odd},\\
0,&t\text{ even}.
\end{cases}}
\tag{WD1}
\]

*Proof.* Euler's beta integral gives \(k!(d-k)!=(d+1)!\int_0^1u^k(1-u)^{d-k}\,du\). For independent Bernoulli-\(u\) bits \(Z_j\), the integrand after summing over all \(z\) is
\[
\mathbb E\left[\left(\sum_{j=1}^d(1-2Z_j)\right)\chi_T(Z)\right]
=t(1-2u)^{t-1}+(d-t)(1-2u)^{t+1}.
\]
For odd \(t\), integration gives \(t/t+(d-t)/(t+2)=(d+2)/(t+2)\). For even \(t\), both contributing odd powers integrate to zero (with the first term absent at \(t=0\)). Multiplication by \((d+1)!\) proves (WD1). \(\square\)

**Theorem (Walsh block decomposition).** For every \(n\ge3\),
\[
\boxed{
Q_n(c)=\frac{n!}{2}+
\frac{n!}{4}
\sum_{\substack{T\subseteq[n]\\ |T|\ {\rm odd}}}
\frac{
\left(\sum_{i\notin T}a_{i,T}\right)^2
-\sum_{i\notin T}a_{i,T}^2
}{|T|+2}.}
\tag{WD2}
\]
For every odd \(T\), the quadratic edge-orbit coefficient matrix has a Walsh block on the \(p=n-|T|\) available directions. If \(p\ge2\), its eigenvalues, in the ordinary Euclidean normalization on the \(n2^{n-2}\) orbit-spin variables, are
\[
\boxed{
\lambda_T^{\rm parallel}=
\frac{(p-1)n!}{2^{n-1}(|T|+2)},\qquad
\lambda_T^{\rm transverse}=
-\frac{n!}{2^{n-1}(|T|+2)}
\quad\text{(multiplicity }p-1\text{)}.}
\tag{WD3}
\]
For \(p=1\) the block has eigenvalue zero. Consequently
\[
\boxed{
\lambda_{\min}=-\frac{n!}{3\cdot2^{n-1}},\qquad
Q_n(c)\ge\frac{n!(6-n)}{12}.}
\tag{WD4}
\]

*Proof.* Fix \(i\ne j\), and put \(D=[n]\setminus\{i,j\}\), \(d=n-2\). Extend each direction-spin function to all \(2^{n-1}\) undirected edges in that direction, with the antipodal oddness relation. Averaging \(f_i\) over its bit \(j\) gives \(g_i\) on \(\{0,1\}^D\); similarly average \(f_j\) over its bit \(i\) to get \(g_j\). The factorial pair-kernel theorem, with the four choices of antipodal lifts identified, makes the coupling between directions \(i,j\)
\[
2^{1-n}\sum_{z,z'\in\{0,1\}^D}K_d(z\oplus z')g_i(z)g_j(z').
\]
The Walsh coefficient of \(g_i\) at \(T\subseteq D\) is \(a_{i,T}\). Orthogonality of the Walsh characters and (WD1) therefore turn this coupling into
\[
\frac{n!}{2}\sum_{\substack{T\subseteq D\\|T|\ {\rm odd}}}
\frac{a_{i,T}a_{j,T}}{|T|+2}.
\]
Summing over \(i<j\), and using \(2\sum_{i<j}a_i a_j=(\sum_i a_i)^2-\sum_i a_i^2\), yields (WD2).

Each direction contains \(2^{n-2}\) independent antipodal edge-orbit variables, so a normalized Walsh vector on that direction has Euclidean squared norm \(2^{n-2}\). For a fixed odd \(T\), the Walsh block is a \(p\)-by-\(p\) matrix with zero diagonal and common off-diagonal entry \(n!/[2^{n-1}(|T|+2)]\). Its eigenvalues are (WD3). The most negative eigenvalue is obtained for \(|T|=1\), giving the first identity in (WD4). Alternatively, dropping the nonnegative squares in (WD2), bounding \(1/(|T|+2)\le1/3\), and applying Parseval across all \(n\) directions gives directly
\[
Q_n\ge\frac{n!}{2}-\frac{n!}{12}\sum_{i,T}a_{i,T}^2
=\frac{n!(6-n)}{12}.
\]
\(\square\)

**Theorem (sharpness in even dimension and failure of quadratic-only positivity).** For every even \(n\ge4\), equality is attained in (WD4) by a legal affine edge coloring. In particular \(Q_6\) can equal zero, and \(Q_n<0\) for every even \(n\ge8\), although the full count \(F_n(c)\) remains nonnegative.

*Proof.* Partition the directions into nonempty even sets \(G,H\), each of size at least two. Choose a reader \(u\in G\) and another reader \(v\in H\). For directions \(i\in G\), take
\[
f_i(x)=\epsilon_i(-1)^{x_v},
\]
and for \(j\in H\), take
\[
f_j(x)=\eta_j(-1)^{x_u},
\]
where the signs in each group are balanced: \(\sum_{i\in G}\epsilon_i=\sum_{j\in H}\eta_j=0\). Every color is independent of the bit in its own direction, and antipodal complementation negates its spin, so this is a legal coloring. Each \(f_i\) has a single Walsh character of order one. Its only nonzero group sum \(\sum_{i\notin T}a_{i,T}\) vanishes by balance, making every retained square term in (WD2) zero. All \(n\) Parseval masses have denominator three, so (WD4) is an equality.

For \(n=6\) the value is zero, and for even \(n\ge8\) it is negative. These colorings still admit monochromatic-zero full geodesics. To see this, choose \(u\in G\) with \(\epsilon_u=+1\) and \(v\in H\) with \(\eta_v=-1\); such readers exist by balance. Start with both reader bits zero. First traverse the \(\eta_j=+1\) directions in \(H\), then the \(\epsilon_i=+1\) directions in \(G\) (including \(u\)), then the \(\eta_j=-1\) directions in \(H\) (including \(v\)), and finally the \(\epsilon_i=-1\) directions in \(G\). The reader bits change at \(u\) and \(v\) in that order, so every traversed edge has spin \(+1\). Thus the negative quadratic values are compensated by higher even Fourier terms in the full path count. \(\square\)

**Corollary (odd dimensions beyond eight).** For every odd \(n\ge9\), there are legal affine edge colorings with
\[
\boxed{Q_n(c)=\frac{n!(7-n)}{12}<0.}
\tag{WD5}
\]
*Proof.* Partition \(n-1\) directions into two nonempty even groups \(G,H\), and leave one extra direction \(z\). Use the preceding balanced reader assignments for \(G,H\). Let the extra direction \(z\) also read the bit \(x_u\) for \(u\in G\), with either fixed sign. Its Walsh character adds one unit of squared group sum at \(T=\{u\}\), while increasing the Parseval mass by one. Formula (WD2) now gives \(Q_n=n!/2-(n-1)n!/12\), as claimed. \(\square\)

**Scope for closure.** Formula (WD2) yields a complete spectral solution for the quadratic sector, and (WD4) recovers \(Q_4\ge4\) without invoking the cycle-by-cycle count. The sharp affine families show that this sector alone cannot provide a dimension-uniform strictly positive geodesic-count certificate. The remaining opportunity is to find an inequality linking the fourth- and higher-order Fourier tensors to the low-order Walsh blocks, forced by complete-path incidence rather than by unconstrained polynomial positivity.

### Sharp-bound rigidity and monochromatic paths

**Proposition (classification of spectral minimizers).** Equality in the Walsh lower bound
\[
Q_n=\frac{n!(6-n)}{12}
\]
holds precisely when the direction spins have the form
\[
f_i(x)=\epsilon_i(-1)^{x_{r(i)}},\quad r(i)\ne i,\quad\epsilon_i\in\{-1,1\},
\tag{WD6}
\]
with the balance rule
\[
\boxed{\sum_{i:r(i)=j}\epsilon_i=0\quad\text{for every reader }j.}
\tag{WD7}
\]
Hence equality is possible only for even \(n\). Every coloring of the form (WD6), with or without the balance rule, has a monochromatic full antipodal geodesic.

*Proof.* The Walsh formula (WD2) and Parseval give the nonnegative deficit
\[
\boxed{
Q_n-\frac{n!(6-n)}{12}
=\frac{n!}{4}\left[
\sum_{\substack{T\subseteq[n]\\|T|\ {\rm odd}}}
\frac{(\sum_{i\notin T}a_{i,T})^2}{|T|+2}
+
\sum_{i,T}\left(\frac13-\frac1{|T|+2}\right)a_{i,T}^2
\right].}
\tag{WD8}
\]
Equality requires all Fourier mass on singleton sets and every singleton group sum to vanish. A Boolean function with only degree-one Walsh coefficients is a signed single character: if \(f_i=\sum_j a_j\chi_j\), then the degree-two coefficient of \(f_i^2=1\) at \(\chi_j\chi_k\) is \(2a_ja_k\), forcing at most one \(a_j\ne0\). Parseval makes its value \(\pm1\). This proves (WD6) and (WD7). The balanced reader fibers have even sizes; their total size \(n\) is therefore even.

For the path assertion, form the functional digraph \(i\mapsto r(i)\). From a starting vertex \(x\), require \(i\) to occur before \(r(i)\) if \(\epsilon_i(-1)^{x_{r(i)}}=+1\), and after \(r(i)\) otherwise. Both cases make the traversed direction-\(i\) edge color zero, since crossing the reader reverses its bit. Each weak component of the functional graph consists of a cycle with attached trees. The starting bit of a reader on a cycle controls the orientation of its one incoming cycle dependency, independently of the other cycle orientations. Choose those bits so that the cycle precedence constraints have at least one edge opposed to the cyclic direction and at least one along it; in a two-cycle, orient the two parallel dependencies in the same undirected direction. This prevents any directed precedence cycle. Trees introduce none. A topological ordering of all directions then traverses every direction once with color zero and ends at the antipode. \(\square\)

This classifies the quadratic minimizers and proves they satisfy NORI1. The deficit (WD8) isolates the high-order Walsh mass and unbalanced singleton-reader sums as the two quantities a perturbative closure argument would need to control.

## Rigidity radius for the quadratic Fourier deficit

Let \(Q_n(c)\) denote the degree-at-most-two Walsh truncation of the monochromatic-zero full-antipodal-geodesic count in a legal odd coloring. The quadratic spectral theorem proves \(Q_n(c)\ge B_n:=n!(6-n)/12\). Write \(\Delta=Q_n(c)-B_n\).

**Lemma (elementary rounding of odd Boolean spins).** Suppose \(f:\{0,1\}^m\to\{-1,+1\}\) obeys \(f(\bar x)=-f(x)\), and let \(\varepsilon=\sum_{|T|\ge3}\widehat f(T)^2\le1/2\). Then some signed singleton Walsh character \(\eta\chi_{\{j\}}\) differs from \(f\) on a fraction at most \(8(m+1)\varepsilon\) of its inputs.

*Proof.* Decompose \(f=g+h\), where \(g=\sum_j a_j\chi_{\{j\}}\) is the degree-one projection. Oddness yields \(\|h\|_2^2=\varepsilon\) and \(\|g\|_2^2=s=1-\varepsilon\). By Cauchy, \(\|g\|_\infty\le\sqrt m\) and \(\|h\|_\infty\le1+\sqrt m\). Taking the degree-two projection of \(f^2=1\) gives
\[
\operatorname{Proj}_2(g^2)=-\operatorname{Proj}_2(2gh+h^2),
\]
so
\[
\|\operatorname{Proj}_2(g^2)\|_2\le (1+3\sqrt m)\sqrt\varepsilon
\le4\sqrt{m\varepsilon}.
\]
But \(\operatorname{Proj}_2(g^2)=2\sum_{j<k}a_ja_k\chi_{\{j,k\}}\), hence \(\sum_{j<k}a_j^2a_k^2\le4m\varepsilon\). Put \(M=\max_j a_j^2\). Then
\[
s(s-M)\le s^2-\sum_j a_j^4
=2\sum_{j<k}a_j^2a_k^2\le8m\varepsilon.
\]
Since \(s\ge1/2\), one has \(1-M\le(16m+1)\varepsilon\). Choose a maximizing \(j\) and the sign of \(a_j\). Their disagreement fraction equals \((1-\sqrt M)/2\), bounded by \((1-M)/2\le8(m+1)\varepsilon\). \(\square\)

**Theorem (spectral stability moat).** If
\[
\boxed{0\le\Delta<
\frac{n!}{240n\,2^{n-2}},}
\tag{SR1}
\]
then each direction spin of \(c\) is a signed one-bit reader \(f_i(x)=\eta_i(-1)^{x_{r(i)}}\), with \(r(i)\ne i\). Consequently \(c\) has a monochromatic antipodal geodesic and at least \(2^{\lceil n/2\rceil}\) monochromatic-zero geodesic roots. Every hypothetical NORI1 counterexample obeys the reverse inequality
\[
\boxed{\Delta\ge \frac{n!}{240n\,2^{n-2}}.}
\tag{SR2}
\]

*Proof.* The nonnegative Walsh deficit identity (WD8) gives
\[
E:=\sum_i\sum_{|T|\ge3}a_{i,T}^2\le30\Delta/n!.
\]
Under (SR1), \(E<1/(8n2^{n-2})\le1/2\). Apply the lemma to each direction spin, a Boolean odd function on \(n-1\) independent bits. Its disagreement proportion from an appropriate signed reader is at most \(8n\varepsilon_i\). Since each direction contains \(2^{n-2}\) independent antipodal edge pairs, the total number \(k\) of pairs differing from the selected reader template satisfies
\[
k\le2^{n-2}\cdot8n\sum_i\varepsilon_i
\le240n2^{n-2}\Delta/n!<1.
\]
The integer \(k\) must be zero. Thus every direction is a signed reader, and the functional-reader root census from the affine-root Subsection proves the path existence and root bound. The contrapositive proves (SR2). \(\square\)

This isolates a proven spectral neighborhood in which every legal coloring is good, without invoking an external Fourier rounding theorem. The neighborhood is exponentially narrow in dimension; controlling large higher-order Walsh mass remains the required step for general closure.



## Monochromatic affine reader geodesics for reader matrices of corank at most two

The invertible affine reader theorem guarantees monochromatic full antipodal geodesics when the zero-diagonal binary reader matrix is invertible. There is a structural extension to **all** row-odd reader matrices of corank at most two, with arbitrary offsets. The proof uses the cyclic-root rotation of dimension orders and a quotient-space covering lemma.

Fix \(n\ge3\). Let \(L\in\mathbb F_2^{n\times n}\) satisfy \(L_{ii}=0\) and
\[
\boxed{L\mathbf1=\mathbf1.}
\tag{AR1}
\]
For arbitrary \(a\in\mathbb F_2^n\), color the direction-\(i\) cube edge incident with \(x\) by
\[
\boxed{c_i(x)=(Lx)_i+a_i.}
\tag{AR2}
\]
The zero diagonal makes this an undirected edge coloring, and (AR1) makes it antipodally odd.

For a dimension order \(\pi=(i_1,\ldots,i_n)\), let
\[
b_\pi(i)=\sum_{j:\pi^{-1}(j)<\pi^{-1}(i)}L_{ij}.
\tag{AR3}
\]
The full path from root \(x\) along \(\pi\) has direction-\(i\) edge bit
\[
(Lx)_i+a_i+b_\pi(i).
\]
Thus it is entirely zero-colored if and only if
\[
\boxed{Lx=a+b_\pi.}
\tag{AR4}
\]
For the reversed dimension order \(\pi^R\), (AR1) gives \(b_{\pi^R}=b_\pi+\mathbf1\). Hence any solution to (AR4) gives a **one-colored path along the reversed order from the same root**.

Let \(V=\mathbb F_2^n/\operatorname{im}L\), with quotient projection \(q\), and put \(q_i=q(e_i)\).

**Lemma (root-rotation quotient walk).** If \(\rho\pi=(i_2,\ldots,i_n,i_1)\) rotates the first direction to the end, then
\[
\boxed{b_{\rho\pi}=b_\pi+Le_{i_1}+e_{i_1},\qquad
q(b_{\rho\pi})=q(b_\pi)+q_{i_1}.}
\tag{AR5}
\]
Consequently, if some dimension order \(\pi\) has quotient-prefix sequence
\[
0,\ q_{i_1},\ q_{i_1}+q_{i_2},\ldots,
\sum_{t=1}^{n-1}q_{i_t}
\tag{AR6}
\]
covering all elements of \(V\), then for **every** offset \(a\) there is a cyclic rotation \(\rho^t\pi\) for which (AR4) is solvable. The full path from that solution root is monochromatic zero, and its reversed order is monochromatic one.

*Proof.* Rotating the first direction \(j=i_1\) to the end removes \(j\) from the predecessors of every other direction \(i\), changing \(b_\pi(i)\) by \(L_{ij}\). The new predecessors of \(j\) are all other directions, changing \(b_\pi(j)\) by its row sum one. Since \(L_{jj}=0\), the resulting vector difference is \(Le_j+e_j\), proving (AR5). Iterating gives the cosets \(q(b_\pi)+\sum_{s\le t}q_{i_s}\). If the prefixes cover \(V\), one of these cosets equals \(q(a)\), so \(a+b_{\rho^t\pi}\in\operatorname{im}L\); choose a preimage root \(x\). Reversal complements every edge color by (AR1). \(\square\)

**Theorem (all corank-zero, -one and -two affine readers are favorable).** If
\[
\boxed{\dim\ker L\le2,}
\tag{AR7}
\]
then for **every** offset \(a\) there exists a cube root \(x\) and a dimension order \(\pi\) giving a monochromatic-zero antipodal geodesic, while the reverse order \(\pi^R\) from \(x\) gives a monochromatic-one antipodal geodesic. In particular NORI1 holds for every such affine coloring, and at least \(2^{\dim\ker L}\) starting roots admit both monochromatic words.

*Proof.* Corank zero is immediate from (AR4). Suppose \(\dim V=1\). The elements \(q_i\) span \(V\), so at least one \(q_i\) is nonzero. Choosing an order beginning with that dimension makes the first two prefix cosets in (AR6) cover \(V\). Apply the rotation lemma.

Now suppose \(\dim V=2\). The \(q_i\) span \(V\). Moreover
\[
\sum_iq_i=q(\mathbf1)=q(L\mathbf1)=0,
\tag{AR8}
\]
by (AR1). Let the three nonzero elements of \(V\) be \(u,v,w=u+v\), and let \(n_u,n_v,n_w\) be their multiplicities among the projected basis vectors \(q_i\). Relation (AR8) implies
\[
n_u\equiv n_v\equiv n_w\pmod2.
\tag{AR9}
\]

If some nonzero element \(u\) appears at least twice, and another independent element \(v\) appears at least once, begin the order with three dimensions whose projected vectors are \(u,v,u\). The resulting quotient prefix sequence is
\[
\boxed{0,\ u,\ u+v=w,\ v,}
\]
which covers all of \(V\). Such a pair of vectors exists unless the three nonzero quotient elements \(u,v,w\) each appear *once*, with all other \(q_i=0\): if the multiplicities are even, spanning requires two distinct nonzero types and each appears at least twice; if they are odd, either one multiplicity is at least three or all three are one.

It remains to handle the exceptional triple of indices \(T=\{i,j,k\}\) with projected vectors \(u,v,w\), respectively, and all other \(q_t=0\). The two-dimensional dual space \(V^*\) is \(\ker L^T\). Under evaluation on the projected basis vectors, its three nonzero elements are precisely the pair indicators
\(e_i+e_j,\ e_i+e_k,\ e_j+e_k\).
Since these belong to \(\ker L^T\), the three matrix rows indexed by \(i,j,k\) are identical:
\[
L_{i,*}=L_{j,*}=L_{k,*}=r.
\]
Their common row vanishes in columns \(i,j,k\) because all three diagonal entries of \(L\) vanish. Its row sum is one, so some direction \(t\notin T\) satisfies \(r_t=1\).

For any prescribed three-bit pattern \((\beta_i,\beta_j,\beta_k)\), choose a dimension order by placing precisely those indices of \(T\) with \(\beta=0\) before \(t\), then \(t\), then the remaining indices of \(T\), and finally all other directions. The predecessor sum in each of the three identical rows is precisely \(\beta_i,\beta_j,\beta_k\). Thus the three components of \(b_\pi\) on \(T\) can be independently prescribed. Since \(V^*=\ker L^T\) is supported on \(T\), these three components determine \(q(b_\pi)\), and all four elements of \(V\) occur among such orders. Select one with \(q(b_\pi)=q(a)\). Then (AR4) is solvable.

In every case at least one compatible order exists. The solution set of (AR4) is an affine translate of \(\ker L\), so it contains \(2^{\dim\ker L}\) roots, each producing opposite monochromatic full paths by order reversal. \(\square\)

**Scope and closure route.** This theorem removes the invertibility assumption for affine antipodally odd colorings through corank two. It uses only full dimension-simple geodesics and has an explicit constructive proof. For higher corank, (AR6) is a sufficient condition for full coset coverage, but need not hold for one cyclic order; the precise remaining affine problem is to show that the vectors \(q(b_\pi)\), as \(\pi\) ranges over **all** dimension orders, cover \(\mathbb F_2^n/\operatorname{im}L\). That would prove the monochromatic affine subclass for all row-odd reader matrices, independent of rank. It is a finite-group quotient-cover problem naturally compatible with cyclic Petrie root slides, offering a more direct topological target than unrestricted edge-color minimization.



## Arbitrarily high corank from a single identical-row dependency class

The quotient-order method also handles a family of affine reader matrices with **unbounded nullity**, complementing the corank-at-most-two theorem.

**Theorem (single clone-class corank elimination).** Let \(L\in\mathbb F_2^{n\times n}\) have zero diagonal and every row sum one. Suppose there is an index set \(T\subseteq[n]\), \(|T|=m\ge2\), such that:
1. all rows \(L_{i,*}\), \(i\in T\), are identical to a common row \(r\);
2. \(\operatorname{rank}L=n-m+1\), so the \(m-1\) pairwise row differences within \(T\) span the entire left kernel.

Then for every offset vector \(a\in\mathbb F_2^n\), there is a starting vertex \(x\) and a full dimension ordering \(\pi\) whose edge colors \(Lx+a\) along the geodesic are all zero. The reverse order from the same root is entirely one-colored. Moreover, at least \(2^{m-1}\) starting roots support such opposite monochromatic paths.

*Proof.* Since \(L\) has zero diagonal and its rows indexed by \(T\) equal \(r\), we have \(r_i=0\) for every \(i\in T\). The row sum of \(r\) is one, so some direction \(t\notin T\) has \(r_t=1\).

The left kernel of \(L\) is precisely the \((m-1)\)-dimensional space of even-parity vectors supported on \(T\), by assumptions (1)--(2). Therefore
\[
\operatorname{im}L
=\{v\in\mathbb F_2^n:v_i=v_j\text{ for all }i,j\in T\}.
\]
Construct an order \(\pi\) beginning with all \(i\in T\) having \(a_i=0\), then \(t\), then all \(i\in T\) having \(a_i=1\), followed by all remaining directions. When traversing an index \(i\in T\), its predecessor sum \(b_\pi(i)\) for row \(r\) equals zero if \(i\) precedes \(t\) and one if \(i\) follows \(t\). All other nonzero positions of \(r\) occur after the entire \(T\)-block. Hence
\[
b_\pi(i)=a_i\quad(i\in T),
\]
and thus \(a+b_\pi\) is identically zero on \(T\). By the displayed characterization of \(\operatorname{im}L\), this vector belongs to \(\operatorname{im}L\). Choose \(x\) with \(Lx=a+b_\pi\). The path in order \(\pi\) is monochromatic zero, and reversal of \(\pi\) complements every edge color because every row sum of \(L\) is one.

Every solution of \(Lx=a+b_\pi\) differs by an element of \(\ker L\), whose dimension is \(m-1\); thus there are \(2^{m-1}\) starting roots with the same two favorable orders. \(\square\)

**Closure significance.** Large affine-reader nullity does not necessarily obstruct a monochromatic geodesic: a single repeated-row class can account for almost the entire kernel, yet the syndromes remain freely controllable through a single external reader direction. The more difficult high-corank case is one with several interlocking row-dependency classes or higher-support binary linear circuits among distinct rows. These are natural matroidal obstructions for the next quotient-order step, not evidence of failure of NORI1.



## Rank-two affine reader closure by an Euler trail on the parity square

The preceding quotient-order theorem handles reader matrices whose rank is within two of full rank. The opposite extreme also admits a complete all-order solution: **every rank-two row-odd reader matrix** has monochromatic full antipodal geodesics for every offset vector.

Keep the affine model
\[
c_i(x)=(Lx)_i+a_i,\qquad
L_{ii}=0,\quad L\mathbf1=\mathbf1.
\tag{AR9}
\]

**Theorem (rank-two Euler closure).** Let \(n\ge3\), and suppose the binary matrix \(L\) in (AR9) has rank two. Then for every \(a\in\mathbb F_2^n\) there exist a starting root \(x\) and a full dimension order \(\pi\) making every traversed edge color zero. The reverse order from the same root makes every edge color one. Thus this entire unbounded-dimensional affine family satisfies NORI1.

*Proof.* The parity functional \(s(v)=\sum_jv_j\) equals one on every row of \(L\). Since the row space has dimension two, precisely two of its three nonzero vectors have odd parity. Therefore the rows of \(L\) take just two distinct values \(u,v\), both occurring. Let
\[
A=\{i:L_{i,*}=u\},\qquad
B=\{j:L_{j,*}=v\}.
\]
These form a partition of the direction set. Zero diagonal forces \(u_i=0\) for \(i\in A\) and \(v_j=0\) for \(j\in B\). Hence
\[
U=\operatorname{supp}u\subseteq B,\qquad
V=\operatorname{supp}v\subseteq A.
\tag{AR10}
\]
Their sizes are nonzero and odd by the row-sum condition.

At a current cube vertex \(y\), put
\[
p=u\cdot y,\qquad q=v\cdot y.
\]
A direction \(i\in A\) has edge color \(p+a_i\); a direction \(j\in B\) has color \(q+a_j\). Traversing a direction in \(V\subseteq A\) toggles \(q\) and leaves \(p\) fixed; traversing a direction in \(U\subseteq B\) toggles \(p\) and leaves \(q\) fixed. Every remaining direction leaves both parity states unchanged.

Construct an undirected multigraph on the four states \((p,q)\in\mathbb F_2^2\). For every \(i\in V\), insert one vertical edge at the fixed first-state bit \(p=a_i\), joining \((p,0)\) to \((p,1)\). For every \(j\in U\), insert one horizontal edge at the fixed second-state bit \(q=a_j\), joining \((0,q)\) to \((1,q)\). These are precisely the permitted transitions for the *active* direction steps to have color zero. Every vertical edge meets every horizontal edge at a corner of the square. Since \(U,V\) are both nonempty, the subgraph of nonisolated vertices is connected.

Let \(v_0,v_1\) be the numbers of vertical edges in the two columns, and \(h_0,h_1\) the numbers of horizontal edges in the two rows. Their totals satisfy
\[
v_0+v_1=|V|\equiv1,\qquad
h_0+h_1=|U|\equiv1\pmod2.
\]
At the two vertices of either fixed column \(p\), the degree parities are \(v_p+h_0\) and \(v_p+h_1\), which differ since \(h_0+h_1\) is odd. Hence each column has precisely one odd-degree vertex, and the full transition multigraph has precisely two odd-degree vertices.

By Euler's trail criterion, there exists a trail traversing every active edge once, beginning at one odd-degree state \((p_*,q_*)\). Because \(U\subseteq B\) and \(V\subseteq A\) are disjoint nonempty sets, the initial root bits can be chosen to satisfy
\[
u\cdot x=p_*,\qquad v\cdot x=q_*
\]
independently. Follow the Euler trail, traversing the original cube dimension corresponding to each used multigraph edge. Every active step has color zero by construction, and the parity state evolves along the trail as prescribed.

The trail traverses at least one horizontal and one vertical edge, so its visited states include both values of \(p\) and both values of \(q\). Every remaining direction \(i\in A\setminus V\) has color \(p+a_i\) and does not change either parity, so insert it at any visited state with \(p=a_i\). Likewise, for every \(j\in B\setminus U\), insert its step at a visited state with \(q=a_j\). These insertions do not alter the state or the validity of the active Euler trail. They give a full dimension-simple cube path in which every direction is used once and every edge has color zero.

Finally, reversing the dimension order from the same initial root replaces each predecessor set by its complement among the other directions. The change in the direction-\(i\) color is the odd row sum \(\sum_{j\ne i}L_{ij}=1\). Thus the reversed full path is entirely one-colored. \(\square\)

**Corollary (both rank extremes are favorable).** Every antipodally odd affine coloring whose zero-diagonal reader matrix has either
\[
\operatorname{rank}(L)=2
\qquad\text{or}\qquad
\operatorname{rank}(L)\ge n-2
\]
admits opposite monochromatic full geodesics from a common root. The rank-two result applies in every dimension, including matrices of corank \(n-2\). Together with the single repeated-row-class theorem, this disposes of broad singular families on both sides of the rank range.

**Closure perspective.** The Euler-trail mechanism is not a small-order argument: it is a uniform realization theorem for arbitrarily many repeated color constraints, using oddness to satisfy the graph-theoretic trail parity condition. For higher reader rank, one can similarly view the current values of a basis of row-function parities as vertices of an \(r\)-cube, with each direction step prescribed to one allowed hyperplane and toggling a fixed state vector \(Le_i\). Rank two yields an ordinary four-state Euler trail; a general closure would need a parity-balanced spanning trail or analogous matroidal state-walk through the \(2^r\)-state quotient. Unlike a direct exhaustive path search, this points to a finite-dimensional structural control point for affine colorings of arbitrary ambient dimension.

### Stronger spectral separation from one-pair restoration resilience

The previous spectral moat becomes twice as wide once one uses the affine-root Subsection's no-compulsory-edge-pair theorem.

**Corollary (two-orbit spectral moat).** For every \(n\ge4\), a legal antipodally odd coloring satisfying
\[
\boxed{Q_n(c)-\frac{n!(6-n)}{12}
<\frac{n!}{120n\,2^{n-2}}}
\tag{SR3}
\]
has a monochromatic antipodal full geodesic. Consequently every hypothetical NORI1 counterexample satisfies the reverse non-strict inequality.

*Proof.* The rounding lemma and spectral estimate already proved above give
\[
E=\sum_i\sum_{|T|\ge3}a_{i,T}^2\le\frac{30\Delta}{n!},
\qquad\Delta=Q_n(c)-\frac{n!(6-n)}{12}.
\]
Under (SR3), \(E<1/(4n2^{n-2})<1/2\), so rounding every direction spin to a signed one-bit reader changes at most
\[
k\le 8n2^{n-2}E
\le \frac{240n2^{n-2}\Delta}{n!}<2
\]
independent antipodal edge orbits. Therefore \(k\in\{0,1\}\). The no-compulsory-pair theorem in “Affine roots, cycle constraints, and odd-degree flag transport” proves that any one-reader legal coloring in dimension at least four remains good after flipping any single orbit. Thus the original \(c\) is good. \(\square\)

**Reader-leaf refinement.** If the rounding template has \(\ell\ge1\) unused reader bits, the leaf-translation theorem makes it good after fewer than \(2^{\ell-1}\) orbit flips. The same argument therefore proves goodness whenever
\[
\frac{240n2^{n-2}\Delta}{n!} <\max\{2,2^{\ell-1}\}.
\tag{SR4}
\]
The parameter \(\ell\) pertains to the selected rounded reader template. These are dimension-uniform structural neighborhoods; the general large-deficit case remains open.



## Rank-three affine reader parity-chain theorem

The rank-two Euler construction extends at the level of *antipodal boundary* to all rank-three row-odd reader matrices. This settles the parity constraint for a monochromatic state walk, leaving the joining of disconnected state cycles as the isolated unproved step.

Let \(L\in\mathbb F_2^{n\times n}\) have rank three, zero diagonal, and \(L\mathbf1=\mathbf1\). Choose a three-row basis \(U\) of its row space. Each basis row has odd parity, so \(U\mathbf1=\mathbf1_3\). Express row \(i\) as \(L_{i,*}=\ell_i^TU\) and put \(t_i=Ue_i\). Then \(\ell_i\) is odd, \(\ell_i\cdot t_i=0\), and \(\sum_i t_i=\mathbf1_3\). The state \(s=Ux\in\mathbb F_2^3\) changes by \(t_i\) upon traversing dimension \(i\), whose edge color is \(\ell_i\cdot s+a_i\).

For every active direction \(t_i\ne0\), the allowed states form a four-point affine plane \(H_i=\{s:\ell_i\cdot s=a_i\}\). Its translation by \(t_i\) partitions its four states into two undirected edges. Choose one such edge per active dimension.

**Theorem (antipodal odd-degree boundary always selectable).** These choices can always be made so that the resulting labeled state multigraph has precisely two odd-degree vertices \(s,s+\mathbf1_3\). It therefore decomposes into a trail connecting antipodal states together with possible disconnected closed trails. If a choice can also be made connected on all edge-bearing vertices, its Euler trail, after insertion of passive directions, gives a monochromatic full dimension-simple cube geodesic. Connectivity is not asserted here.

*Proof.* If the rows \(\ell_i\) of active directions span at most two dimensions, remove the zero-column passive directions. The remaining reader matrix has rank two: rank one would force every nonzero row to coincide and vanish on all active columns by the zero-diagonal condition, contradicting odd row sums. Apply the rank-two Euler theorem and insert passive directions at an endpoint where their odd-row color equals zero.

Otherwise the active \(\ell_i\) span all of \(\mathbb F_2^3\). For an arbitrary initial selection let \(\beta\in\mathbb F_2^{\mathbb F_2^3}\) indicate the state vertices of odd degree. It has even total parity and first moment \(\sum_s\beta(s)s=\sum_i t_i=\mathbf1_3\). Each antipodal-pair indicator \(p_z=\delta_z+\delta_{z+\mathbf1_3}\) has the same two properties.

The first-order binary Reed--Muller code \(R=\operatorname{span}\{1,s_1,s_2,s_3\}\) on the eight state vertices is self-dual: affine polynomials have pairwise zero inner product and \(\dim R=4\). Therefore
\[
\boxed{\beta+p_z\in R\quad\text{for every antipodal pair }z.}
\]
Switching the two admissible choices for dimension \(i\) toggles the four odd-degree bits on \(H_i\), whose indicator is the affine polynomial \(1+a_i+\ell_i\cdot s\). Let \(W\le R\) be the span of these indicators. The active normals span three dimensions, so \(\dim W\ge3\); moreover \(W\) contains an affine polynomial with odd-weight linear normal.

Differences between the four antipodal-pair indicators \(p_z\) span the three-dimensional subspace
\[
D=\{b+\lambda\cdot s:\lambda\cdot\mathbf1_3=0\}
\]
of affine functions with even-weight linear normal. Since \(W\) has an odd-normal member, \(W\ne D\). If \(W=R\), some choice of switches clearly makes \(\beta=p_z\). Otherwise \(\dim W=3\); the four targets \(p_z\) represent both cosets modulo \(W\), because their differences span \(D\not\subseteq W\). Therefore at least one \(z\) satisfies \(\beta+p_z\in W\). Toggle the corresponding selected dimension edges. Their boundary change equals \(\beta+p_z\), giving the desired antipodal pair as the sole odd-degree vertices. Euler decomposition finishes. \(\square\)

**Closure obligation.** Prove a *connected rainbow parity-chain selection* in the above eight-state geometry. The parity and antipodal homology conditions are already resolved; the only remaining defect for affine rank three is joining the disjoint Euler cycles without repeating an original dimension. An independent finite audit of all \(23{,}040\) rank-three, four-label transition systems satisfying these constraints found a connected selection for every one, and further random systems with up to eight labels agreed. The theorem itself uses no finite verification.



## Twin-direction deletion and a finite kernel for fixed reader rank

The rank-three parity-chain theorem leaves connectivity unresolved. There is nevertheless an all-dimensional **reduction to finitely many active direction types**: identical affine row-column twins can be deleted two at a time and later reinserted into a monochromatic full geodesic. Importantly, this works even when their constant color offsets differ.

Consider any zero-diagonal row-odd matrix \(L\in\mathbb F_2^{n\times n}\) and offset vector \(a\), defining \(c_i(x)=(Lx)_i+a_i\).

**Lemma (passive-direction deletion).** If column \(j\) of \(L\) vanishes, delete row and column \(j\) to obtain \(L'\). The remaining matrix is zero-diagonal and row-odd. Every monochromatic-zero full geodesic for the smaller affine coloring lifts to one in the original cube.

*Proof.* With \(x_j=0\), all other direction colors agree with those of the smaller coloring, and crossing dimension \(j\) does not alter them because the column vanishes. The direction-\(j\) edge bit is independent of \(x_j\). Its value at the initial smaller-cube root and at the antipodal endpoint differ by one, since row \(j\) has odd sum entirely on the remaining columns. Insert dimension \(j\) at whichever endpoint gives edge color zero. The resulting path uses all directions once and is monochromatic. \(\square\)

**Theorem (row-column twin-pair deletion).** Suppose distinct indices \(i,j\) have
\[
\boxed{L_{i,*}=L_{j,*},\qquad L_{*,i}=L_{*,j}.}
\tag{AT1}
\]
Delete both rows and columns to obtain \(L'\) on \(n-2\) directions, with restricted offset \(a'\). Then \(L'\) is still zero-diagonal and row-odd. If the smaller coloring admits a monochromatic-zero full antipodal geodesic, so does the original coloring, **for either choice of \(a_i,a_j\)**.

*Proof.* Identical rows and the zero diagonal imply \(L_{ij}=L_{ji}=0\). Identical columns imply \(L_{ki}=L_{kj}\) for every remaining direction \(k\). Hence deleting both columns changes each remaining row sum by zero modulo two, preserving oddness and zero diagonal.

Let \(r\) denote the common reader row restricted to the remaining directions. It has odd sum, so \(r\cdot\bar x=r\cdot x+1\). A monochromatic-zero geodesic in the smaller cube from \(x\) can be reversed to give one from \(\bar x\). Thus we are free to choose either antipodal starting root for the smaller monochromatic path.

If \(a_i=a_j\), take initial bits \(x_i=x_j=0\). The two deleted dimensions do not read each other, and their edge colors are both \(r\cdot x+a_i\) if traversed consecutively at the start, or both \(r\cdot\bar x+a_i\) if traversed consecutively at the end. These values are complementary, so one endpoint permits a zero-colored consecutive pair. Traversing the pair changes the other direction colors by \(L_{ki}+L_{kj}=0\), leaving every smaller-path color unchanged.

If \(a_i\ne a_j\), arrange the deleted bits initially as \(x_i=1,x_j=0\). Traverse \(i\) first, then the entire smaller monochromatic path, and finally \(j\). During the smaller path both deleted bits equal zero, so its colors are unchanged. The first deleted edge has bit \(r\cdot x+a_i\); the final deleted edge has bit
\[
r\cdot\bar x+a_j=r\cdot x+1+a_i+1=r\cdot x+a_i.
\]
Choose between the two antipodal smaller starting roots so this common bit is zero, using the oddness of \(r\). After the two deleted steps the pair of deleted bits is \((0,1)\), the complement of its initial \((1,0)\), and all remaining bits are also complemented. The resulting complete dimension-simple path is monochromatic zero. \(\square\)

**Corollary (bounded fixed-rank affine kernel).** Suppose \(\operatorname{rank}L=r\ge2\). Choose \(r\) linearly independent odd rows as a matrix \(U\) and write
\[
L_{i,*}=\ell_i^TU,\qquad t_i=Ue_i.
\]
Then \(\ell_i\) has odd weight, \(\ell_i\cdot t_i=0\), and column \(i\) of \(L\) vanishes if and only if \(t_i=0\). Every active direction has a type \((\ell_i,t_i)\) with \(\ell_i\) of odd weight and \(t_i\ne0\) in its orthogonal hyperplane. The number of possible active types is
\[
\boxed{N_r=2^{r-1}(2^{r-1}-1).}
\tag{AT2}
\]
If two active directions have the same type, their full reader rows and full reader columns coincide, and the twin-pair theorem deletes both, regardless of offsets. Delete all passive directions singly, and repeatedly delete repeated active types in pairs. The residual matrix has rank at most \(r\), retains odd row sums, and has at most \(N_r\) directions. A monochromatic full geodesic in that residual matrix lifts constructively through all deletions to one in the original cube.

In particular,
\[
\boxed{N_2=2,\qquad N_3=12,\qquad N_4=56.}
\tag{AT3}
\]
Therefore proving the monochromatic affine reader theorem for all zero-diagonal row-odd matrices of rank at most three requires checking only the finite family of residual configurations on at most **12 directions**, rather than cubes of unbounded dimension.

*Proof.* Since \(U\mathbf1=\mathbf1_r\), the row-odd condition makes every coefficient \(\ell_i\) odd. The zero diagonal gives \(\ell_i\cdot t_i=0\). For a fixed odd \(\ell\), its orthogonal hyperplane has \(2^{r-1}\) vectors, of which \(2^{r-1}-1\) are nonzero. There are \(2^{r-1}\) odd \(\ell\), giving (AT2). Equality of \(\ell\) implies equality of full rows, while equality of \(t\) implies equality of full columns. Every deletion preserves zero diagonal and odd row sums, and the preceding lifting lemmas preserve the existence of monochromatic full geodesics. Each application reduces the ambient dimension, so the procedure terminates with distinct active types and at most \(N_r\) directions. \(\square\)

**Proof-closure target.** At rank three, the previous Reed--Muller theorem already permits selection of one state edge per active dimension with antipodal odd-degree boundary. The new twin deletion theorem bounds the remaining *connectedness* problem to at most twelve active labels, one of each permissible \((\ell,t)\) type. The only unresolved local claim for the full rank-three affine subclass is that one of the two state-edge choices per label can be selected to connect the antipodal Euler trail and every Euler circuit. A proof or exhaustive certified resolution of that bounded structural kernel would establish the rank-three affine result in **every ambient dimension**.



## Computer-assisted proof of the all-dimensional rank-three affine reader case

**Theorem (rank-three affine monochromatic-geodesic closure).**
Let \(n\ge3\) and \(L\in\mathbb F_2^{n\times n}\) satisfy
\[
L_{ii}=0,\qquad L\mathbf1=\mathbf1,\qquad \operatorname{rank}L=3.
\]
For every \(a\in\mathbb F_2^n\), the antipodally odd coloring \(c_i(x)=(Lx)_i+a_i\) has a full dimension-simple monochromatic-zero antipodal geodesic. Reversing its dimension order from the same root yields a monochromatic-one antipodal geodesic.

The theorem is **computer-assisted**. The reduction to a fixed-rank finite kernel is the analytic row-column twin theorem of this Subsection; two independent exhaustive verifiers establish feasibility for every remaining rank-three kernel configuration.

**Analytic reduction.** Choose three independent odd rows of \(L\) as a matrix \(U\). Write \(L_{i,*}=\ell_i^TU\) and \(t_i=Ue_i\). Then
\[
\ell_i\cdot\mathbf1_3=1,\quad
\ell_i\cdot t_i=0,\quad
\sum_i t_i=\mathbf1_3.
\tag{K1}
\]
Remove every passive direction \(t_i=0\) using the passive-direction deletion lemma. When two active labels have the same pair \((\ell_i,t_i)\), their full reader rows and columns are identical. Remove them using the twin-pair deletion theorem, whether their offsets agree or differ. Every deletion preserves the odd row sum and allows a monochromatic full geodesic of the reduced cube to lift back to the original cube.

There are four odd vectors \(\ell\in\mathbb F_2^3\), namely \(1,2,4,7\) in binary notation. Each has three nonzero orthogonal vectors \(t\). Thus at most
\[
\boxed{4\cdot3=12}
\tag{K2}
\]
active row-column types remain, with at most one label per type and an arbitrary bit offset. The remaining reader rank is at most three. Rank two is solved by the four-state Euler theorem. Rank one is impossible for a nonempty zero-diagonal row-odd matrix, because every row would have to be the same odd vector and simultaneously vanish on all diagonal positions. The empty case is trivial.

**Finite kernel lemma (exhaustively verified).** Define
\[
\mathcal T=\{(\ell,t):
\ell\in\{1,2,4,7\},\quad
1\le t\le7,\quad
\ell\cdot t=0\}.
\tag{K3}
\]
For each of the twelve types independently choose absent, offset zero, or offset one. Retain only ternary configurations satisfying
\[
\boxed{\bigoplus_i t_i=7,\qquad
\operatorname{rank}\{\ell_i\}=3,\qquad
\operatorname{rank}\{t_i\}=3.}
\tag{K4}
\]
All such configurations arise as reduced rank-three odd affine reader systems: define the reader matrix by \(L_{ij}=\ell_i\cdot t_j\). Zero diagonal follows from type orthogonality, row oddness follows from \(\bigoplus_jt_j=7\), and rank three follows from both spanning conditions.

There are \(3^{12}=531{,}441\) ternary configurations. Precisely **65,664** satisfy (K4). In every one there exists a starting state \(s\in\mathbb F_2^3\) and an ordering of all active labels such that before traversing label \(i\) its state satisfies
\[
\boxed{\ell_i\cdot s=a_i,\qquad s\gets s+t_i.}
\tag{K5}
\]

**Verification method 1 (direct dimension-simple path dynamic program).** For each retained instance with \(m\le12\) labels, represent a set of possible parity states by an eight-bit mask. Initialize \(R[\varnothing]=\mathbb F_2^3\). For every subset \(S\) and unused label \(i\), update
\[
\boxed{
R[S\cup\{i\}]\gets
R[S\cup\{i\}]\cup
\{s+t_i:s\in R[S],\ \ell_i\cdot s=a_i\}.
}
\tag{K6}
\]
Subsets are processed in increasing binary-mask order. Every transition uses a previously unused dimension, so the recurrence records full dimension-simple paths. The independent C++17 implementation reported **65,664 successful final-state masks among 65,664 admissible instances**. A nonempty final mask witnesses a monochromatic full geodesic from some initial state.

**Verification method 2 (Euler parity and connectivity).** Independently, for each active label choose one of the two possible undirected edges joining states \(s,s+t_i\) in its admissible four-state plane \(\ell_i\cdot s=a_i\). Enumerate these binary choices in Gray order. Retain those whose odd-degree boundary is one antipodal pair of states, and test that all edge-bearing vertices lie in one connected component. Such a connected multigraph has an Euler trail from one odd state to its antipode, using every label once. The second C++17 implementation found an accepted choice for **all 65,664** admissible rank-three instances, inspecting **272,950** edge-choice configurations in total and bypassing **2,859** antipodal-boundary selections that were disconnected. Although the analytic reduction permits twelve labels, the largest admissible cases in this enumeration contained ten.

The two algorithms agree but decide feasibility in different ways: the first directly constructs subset-reachable dimension orders without using graph Euler criteria, while the second searches for connected antipodal Euler selections.

**Lift to the original cube.** For a reduced feasible state \(s\), choose a cube root \(x\) with \(Ux=s\); such a root exists because the displacement columns \(t_i\) span \(\mathbb F_2^3\). The state path from (K5) realizes a monochromatic full cube geodesic using each residual direction once. Reverse all passive and twin deletions using the proven lifting lemmas. The resulting original path is dimension-simple and monochromatic zero. As \(\sum_{j\ne i}L_{ij}=1\) for every row \(i\), reversing its dimension order from the same root complements every edge bit, producing the monochromatic-one full path. This proves the stated rank-three theorem, conditional only on the fully specified finite computation (K3)--(K6). \(\square\)

**Reproducibility.** Two source files were created and successfully compiled with C++17 optimization -O3:
- nori_rank3_kernel_dp.cpp, SHA-256 2e121bf1f95042109ed06027ec9fb90b1fe618f7f9ee48284696ac24a56ca10c;
- nori_rank3_kernel_verify.cpp, SHA-256 95a1c73e5179b8cf7139ed1d22644bcc6a5b27b79086004b5fea60f75ea5d889.

Their enumeration space, rank restrictions, transition predicate and outputs are all specified above so the finite verification can be independently reimplemented. A separately reviewed execution is desirable before external publication.

**Consequences and remaining closure.** The complete affine odd reader subclass of NORI1 is now proved for reader rank **two or three**, corank **at most two**, and all left-nullity generated by a single repeated-row class, without restricting ambient cube dimension. Affine systems of larger rank with substantial nullity and arbitrary nonlinear edge colorings remain outside these theorems. The twin kernel bound \(2^{r-1}(2^{r-1}-1)\) supplies a general all-order reduction for each fixed reader rank \(r\), suggesting a systematic finite-state route through further affine ranks.



## Cokernel exchange geometry for affine antipodally odd edge colorings

Let \(L\in\mathbb F_2^{n\times n}\) have zero diagonal and satisfy \(L\mathbf1=\mathbf1\). Color dimension-\(i\) edges by \(c_i(x)=(Lx)_i+a_i\). For a permutation \(\pi\), put
\[
b_\pi(i)=\sum_{\pi^{-1}(j)<\pi^{-1}(i)}L_{ij},
\qquad
V=\mathbb F_2^n/\operatorname{im}L,
\quad q:\mathbb F_2^n\to V.
\]
A monochromatic-zero full geodesic with dimension order \(\pi\) exists if and only if \(q(b_\pi)=q(a)\). Reversing a favorable order from the same root produces a monochromatic-one geodesic.

Set
\[
d_{ij}=L_{ij}e_i+L_{ji}e_j,\qquad w_{ij}=q(d_{ij}).
\]

**Theorem (inversion statistic and universal cut sum).** Swapping consecutive dimensions \(i,j\) changes \(q(b_\pi)\) by \(w_{ij}\), independently of their positions. For any reference total order \(\pi_0\),
\[
\boxed{
q(b_\pi)=q(b_{\pi_0})+
\sum_{\{i,j\}\text{ inverted relative to }\pi_0}w_{ij}.
}
\tag{EX1}
\]
Moreover, for every subset \(S\subseteq[n]\),
\[
\boxed{
\sum_{\substack{i\in S\\j\notin S}}d_{ij}
=(I+L)\mathbf1_S,
\qquad
\sum_{\substack{i\in S\\j\notin S}}w_{ij}
=q(\mathbf1_S).
}
\tag{EX2}
\]
Consequently the swap labels \(w_{ij}\) span the **entire** cokernel \(V\). In particular, every nonzero left-kernel functional \(y\in\ker L^T\) takes both values on the collection of order syndromes \(b_\pi\).

*Proof.* An adjacent swap changes only the predecessor relation of the swapped pair. Its effects in rows \(i,j\) are \(L_{ij},L_{ji}\); all other rows are unchanged. Every permutation is obtained from \(\pi_0\) by such swaps, whose parity for each pair is its inversion indicator, proving (EX1). For a bit position \(k\in S\), the cut sum of the vectors \(d_{ij}\) has value
\(\sum_{j\notin S}L_{kj}=1+\sum_{j\in S}L_{kj}\), by row oddness. For \(k\notin S\) it has value \(\sum_{i\in S}L_{ki}\). These are precisely the bits of \((I+L)\mathbf1_S\). Quotienting eliminates \(L\mathbf1_S\) and proves (EX2). Taking singleton \(S\) expresses each \(q(e_i)\) as a sum of swap labels; these projected basis vectors span \(V\). If \(y\) is a nonzero left-kernel functional, some adjacent swap label pairs nontrivially with \(y\), so two adjacent-swap-related orders have opposite \(y\)-syndrome. \(\square\)

**Theorem (forest exchange-graph criterion).** Let \(G_L\) have vertex set \([n]\), joining \(i,j\) when \(w_{ij}\ne0\). If \(G_L\) is a forest, then **every offset** \(a\) admits a monochromatic-zero full antipodal geodesic and its complementary reversed-order partner.

*Proof.* Any orientation of a forest is acyclic and extends to a total order. Relative to \(\pi_0\), the inversions on all edges of \(G_L\) can therefore be selected independently. Inversions off that graph have weight zero. Consequently (EX1) realizes the affine set
\(q(b_{\pi_0})+\{\sum_{e\in F}w_e:F\subseteq E(G_L)\}
=q(b_{\pi_0})+\operatorname{span}\{w_e\}=V\),
using (EX2). Choose an order whose syndrome equals \(q(a)\). \(\square\)

**Theorem (independent exchange matching).** Put \(k=\dim V\). If there are \(k\) disjoint pairs \(\{i_s,j_s\}\) for which the labels \(w_{i_sj_s}\) form a basis of \(V\), then every offset is favorable.

*Proof.* Arrange the chosen pairs as consecutive two-direction blocks in a fixed permutation. Swapping any subcollection of these disjoint blocks changes the order syndrome by the sum of its selected basis labels, without disturbing any other relative order. Thus all \(2^k\) quotient syndromes occur. \(\square\)

**Theorem (common-pivot exchange criterion).** If a set \(T\) of dimensions and \(p\notin T\) satisfy \(w_{ij}=0\) for all \(i,j\in T\) while \(\{w_{ip}:i\in T\}\) spans \(V\), then every offset is favorable.

*Proof.* Arrange all elements of \(T\cup\{p\}\) consecutively, and distribute any selected subset of the leaves \(T\) before the pivot \(p\), placing the rest after it. The relative order changes within \(T\) affect only zero-weight labels; placing leaf \(i\) on the opposite side of the pivot toggles \(w_{ip}\). Hence every subset sum of the spanning pivot labels is realized in (EX1). \(\square\)

**Theorem (Gray-rotation criterion).** If \(V\) has dimension \(k\) and admits a basis \(u_1,\ldots,u_k\) such that at least \(2^{k-j}\) distinct dimension indices satisfy \(q(e_i)=u_j\) for each \(j\), then every offset is favorable.

*Proof.* The binary reflected Gray path through \(\mathbb F_2^k\) has \(2^k-1\) successive moves, comprising \(2^{k-j}\) steps of basis type \(u_j\). Order distinct dimensions with the requisite projected values according to those moves, leaving the remaining dimensions last. Sliding the root by cyclically rotating the first dimension to the end changes the quotient syndrome by \(q(e_i)\), as in the previously proved root-rotation lemma. The first \(2^k\) cyclic rotations therefore visit every class in \(V\), one of which equals \(q(a)\). \(\square\)

**Path toward closure.** The general affine-coloring problem is now a binary-weighted **acyclic-orientation covering problem**. The universal cut formula proves that elementary adjacent swaps have enough linear directions to reach the entire cokernel; missing monochromatic paths can arise only from an inability to realize a required combination of these directions through one transitive dimension order. Forest visible exchange graphs, independent disjoint exchange bases, common-pivot stars, and Gray-rotation multiplicities all satisfy the required coverage in arbitrary dimension. The remaining affine challenge is to show that every cokernel syndrome is represented by some *acyclic* orientation of the visible exchange graph for **every** zero-diagonal row-odd matrix. This would close the entire affine subclass of NORI1 and identifies a matroidal/transitivity obstruction potentially relevant to the nonlinear cubical exchange problem.



## Cut-switch protection on even cycles: affine closure beyond forests

Let \(L\) be a zero-diagonal binary matrix with \(L\mathbf1=\mathbf1\). Let \(V=\mathbb F_2^n/\operatorname{im}L\), and give the unordered dimension pair \(i,j\) the quotient label
\(w_{ij}=q(L_{ij}e_i+L_{ji}e_j)\). Define the visible exchange graph \(G_L\) by retaining precisely the edges whose labels are nonzero.

For an orientation \(O\) of \(G_L\) and a vertex subset \(S\), let \(O^S\) reverse the directions of all edges crossing \(\delta(S)\).

**Theorem (even-cycle parity protected affine closure).** Assume \(G_L\) has no odd cycle and admits an orientation \(O\) such that every simple cycle has an **odd** number of edges directed against either cyclic traversal. Then every affine offset \(a\) gives a full dimension-simple monochromatic-zero antipodal geodesic, and reversing its dimension order from the same root gives a monochromatic-one geodesic.

*Proof.* A graph orientation with an odd number of edges opposing a cyclic traversal cannot direct that cycle consistently. Every cycle intersects each cut in an even number of edges. Therefore switching an arbitrary cut \(\delta(S)\) preserves the odd opposition parity on every cycle, because reversing an even number of its edges does not change the parity. Thus every switched orientation \(O^S\) is acyclic and extends to a total order \(\pi_S\) on the dimension symbols. Let \(\pi_0\) extend \(O\).

The inversion-weight theorem says that the quotient syndrome of the order changes by the sum of its reversed visible-edge labels:
\[
q(b_{\pi_S})=q(b_{\pi_0})+\sum_{e\in\delta(S)}w_e.
\]
The universal cut formula gives \(\sum_{e\in\delta(S)}w_e=q(\mathbf1_S)\). Hence
\[
\boxed{q(b_{\pi_S})=q(b_{\pi_0})+q(\mathbf1_S).}
\]
As \(S\) ranges over all subsets of dimensions, the projected indicator vectors \(q(\mathbf1_S)\) range over all of \(V\). Choose one with \(q(b_{\pi_S})=q(a)\). The monochromatic-path system \(Lx=a+b_{\pi_S}\) is then soluble. Reversing the order changes every edge color by the odd row sum, yielding the claimed complementary path. \(\square\)

**Corollary (even-cycle cactus closure).** If \(G_L\) is a cactus with all its cycles even, then every offset is favorable, in every ambient dimension and at every reader-matrix corank.

*Proof.* The simple cycles of a cactus have disjoint edge sets. For each cycle, choose a cyclic traversal and orient all its edges in that traversal except one, which is oriented backward. Orient bridge edges arbitrarily. These choices are consistent across cycles, and every cycle has odd opposition parity. Apply the theorem. A forest is the special case without cycles. \(\square\)

**Corollary (cut-orbit criterion).** More generally, suppose the visible exchange graph admits an orientation \(O\) for which **every** cut-switched orientation \(O^S\) is acyclic. Then the same quotient-syndrome argument proves monochromatic full geodesics for all affine offsets. The odd-even-cycle criterion is a sufficient condition for this cut-orbit property.

This removes arbitrarily many independent even cycles from the affine proof obstruction. The remaining challenge is to repair the cyclic orientations produced by cut switches on more intricately overlapping feedback blocks while preserving the quotient syndrome. The theorem uses complete dimension orders and does not invoke finite-order verification.



## Odd-cycle repair: all unicyclic exchange graphs are favorable

The previous cut-switch theorem settled visible exchange graphs with an orientation that is odd on every even cycle, including even-cycle cacti. A single **odd** cycle can also be handled for every affine offset, by using the reader-matrix image as a syndrome-preserving cut adjustment. This is a stronger all-corank result and introduces a quantitative repair criterion for multiple odd cycles.

Keep the zero-diagonal row-odd reader matrix \(L\), the projection \(q:\mathbb F_2^n\to V=\mathbb F_2^n/\operatorname{im}L\), and visible exchange graph \(G_L\). Its edge weights \(w_{ij}=q(L_{ij}e_i+L_{ji}e_j)\) obey
\[
\sum_{e\in\delta(S)}w_e=q(\mathbf1_S).
\tag{UC1}
\]
For a graph cycle \(C\), let
\[
D_C:\mathbb F_2^n\to\mathbb F_2^{E(C)},\qquad
D_C(x)_{\{i,j\}}=x_i+x_j,
\]
be restriction of the usual vertex-cut map to the edges of \(C\). Define its *reader-image cut rank*
\[
\boxed{t_C=\dim D_C(\operatorname{im}L).}
\tag{UC2}
\]

**Lemma (visible cycles are moved by reader-image cuts).** Every cycle \(C\) of \(G_L\) satisfies \(t_C\ge1\).

*Proof.* If \(t_C=0\), then for every \(x\in\mathbb F_2^n\), the entries of \(Lx\) agree at the two endpoints of each edge of \(C\). Connectivity of \(C\) makes all its indexed matrix rows \(L_{i,*}\), \(i\in V(C)\), identical. The zero diagonal then forces this common row to vanish on every column indexed by \(V(C)\). Hence \(L_{ij}=L_{ji}=0\) for the endpoints of every cycle edge. All such exchange weights \(w_{ij}\) would vanish, contrary to their presence in the visible exchange graph. \(\square\)

**Theorem (unicyclic affine closure in every dimension).** If the visible exchange graph \(G_L\) has at most one simple cycle, with arbitrary attached forest components, then for **every** offset \(a\), the coloring \(c_i(x)=(Lx)_i+a_i\) has a monochromatic-zero full antipodal geodesic and the complementary one-colored geodesic obtained by reversing its dimension order. The cycle may have odd or even length, and the reader matrix may have any rank or corank.

*Proof.* The forest case and the even-cycle case follow from the cut-switch acyclic-orientation theorem. Suppose the only cycle \(C\) has odd length \(m\). Orient its edges in cyclic order except for one backward edge; orient every edge outside \(C\) arbitrarily. The resulting orientation \(O\) is acyclic. Choose a total order \(\pi_0\) extending it.

For each vertex subset \(S\), cut-switch \(O\) to \(O^S\). Along \(C\), the number of edges opposing the chosen cyclic traversal was initially one, and changes by an even number modulo two because every cut meets \(C\) evenly. A clockwise directed cycle has zero opposing edges (even), so it is never attained by a cut switch. A counterclockwise directed cycle has \(m\) opposing edges (odd), and is the **only** directed cycle orientation that could occur. To obtain it from \(O\), the cut-reversal vector \(D_C(\mathbf1_S)\) must equal one fixed vector \(\eta_C\) in the cycle's edge space.

Fix an arbitrary target cokernel class \(v\in V\). Its candidate vertex cuts have indicators in one affine coset \(S_0+\operatorname{im}L\), because \(q(\mathbf1_S)=v\) precisely for those subsets. As \(S\) varies over this coset, the restricted edge-cut pattern \(D_C(\mathbf1_S)\) runs uniformly through an affine translate of \(D_C(\operatorname{im}L)\), which has at least two elements by the lemma. Therefore not every candidate cut has pattern \(\eta_C\). Choose a cut \(S\) with a different pattern. The switched orientation \(O^S\) then has no directed cycle: the unique cycle \(C\) is not consistently oriented, and forest edges belong to no cycle. Thus \(O^S\) extends to a total order \(\pi_S\).

The inversion-weight and cut identities yield
\[
q(b_{\pi_S})=q(b_{\pi_0})+q(\mathbf1_S).
\]
Choose target \(v=q(a)+q(b_{\pi_0})\). The corresponding acyclic cut switch gives \(q(b_{\pi_S})=q(a)\). Hence \(Lx=a+b_{\pi_S}\) is solvable, providing the monochromatic-zero geodesic. Its reversed dimension order from the same root is monochromatic one because every row sum is odd. \(\square\)

**Theorem (multiple odd-cycle probabilistic cut repair).** Suppose \(G_L\) is a cactus, with odd simple cycles \(C_1,\ldots,C_h\) and any number of even cycles. Define \(t_{C_j}\) by (UC2). If
\[
\boxed{\sum_{j=1}^h2^{-t_{C_j}}<1,}
\tag{UC3}
\]
then for every affine offset \(a\), the same monochromatic full geodesics exist.

*Proof.* Orient each simple cycle consistently around it except for one backward edge, and choose arbitrary orientations of the other edges. Since a cactus has edge-disjoint cycles, the prescriptions are consistent, and the initial orientation is acyclic. Cut switching preserves odd opposition parity on every even cycle, so no even cycle can become directed. For each odd cycle, only the opposite cyclic orientation can become directed, corresponding to one prescribed restricted cut pattern \(D_{C_j}(\mathbf1_S)=\eta_{C_j}\).

Fix a target cokernel syndrome \(v\), and choose \(S\) uniformly in the affine fiber \(S_0+\operatorname{im}L\) with \(q(\mathbf1_S)=v\). The random image \(D_{C_j}(\mathbf1_S)\) is uniform on an affine space of size \(2^{t_{C_j}}\). Thus the probability of the one forbidden pattern for cycle \(C_j\) is either zero or \(2^{-t_{C_j}}\). By the union bound, the probability that any odd cycle becomes directed is at most \(\sum_j2^{-t_{C_j}}<1\). Hence some cut in the prescribed syndrome fiber avoids every directed cycle. Its switched orientation is acyclic and extends to a dimension order realizing the required \(q(b_\pi)\) syndrome, as in the unicyclic proof. \(\square\)

**Consequences.** The unicyclic theorem handles odd or even feedback cycles of arbitrary length and all attached trees without assuming a small quotient, a near-invertible reader matrix, or an affine-row clone class. The multicycle criterion quantifies how much the image of \(L\) can vary the cut pattern independently on each odd cycle; every visible cycle has \(t_C\ge1\), but several interacting odd cycles may still defeat the simple union bound. The remaining affine closure problem can therefore be approached through *syndrome-preserving, cycle-breaking cut choices*, rather than through an unstructured search across all dimension permutations.



## Reader-row cut rank and three-odd-cycle affine closure

The earlier multiple-cycle cut-repair theorem has a stronger universal input: every odd exchange-visible cycle has at least two independent reader-image cut variations.

For any connected subgraph \(H\) of the visible exchange graph \(G_L\), let \(D_H\) denote its vertex-to-edge cut map over \(\mathbb F_2\), and set
\[
t_H=\operatorname{rank}(D_HL).
\]

**Theorem (exchange chromatic-rank inequality).** Every connected subgraph \(H\subseteq G_L\) satisfies
\[
\boxed{\chi(H)\le2^{t_H},\qquad
t_H\ge\lceil\log_2\chi(H)\rceil.}
\]
In particular, if \(C\) is an odd simple cycle, then
\[
\boxed{t_C\ge2.}
\]

*Proof.* Each row of \(D_HL\) is a reader-row difference \(L_{i,*}+L_{j,*}\) along an edge \(\{i,j\}\) of \(H\). Fix a base vertex \(v\). As \(H\) is connected, adding these row differences along a path from \(v\) to another vertex \(i\) produces \(L_{i,*}+L_{v,*}\). Thus all reader rows on \(H\) lie in one affine space of dimension at most \(t_H\), and there are at most \(2^{t_H}\) distinct row patterns.

The row patterns properly color \(H\): if rows \(i,j\) on a visible edge were identical, their zero diagonal entries would force \(L_{ij}=L_{ji}=0\), making the adjacent-exchange weight \(q(L_{ij}e_i+L_{ji}e_j)\) vanish. This contradicts the definition of a visible edge. Therefore adjacent vertices have different row patterns, giving the chromatic-number bound. Every odd cycle has chromatic number three, so \(t_C\ge2\). \(\square\)

**Corollary (cactus graphs with up to three odd cycles).** If the visible exchange graph of a zero-diagonal row-odd affine reader matrix is a cactus containing at most three odd cycles, then every affine offset admits a monochromatic-zero full dimension-simple antipodal geodesic, and reversal of its dimension order from the same root gives an all-one geodesic. The graph may have arbitrarily many even cycles and attached trees; no restriction is imposed on ambient dimension, rank, or corank.

*Proof.* The odd-cycle cut-repair theorem states that for a fixed target cokernel syndrome and a uniformly chosen cut in its affine fiber, an odd cycle \(C\) becomes directed with probability at most \(2^{-t_C}\). By the present theorem, \(2^{-t_C}\le1/4\). A union bound over at most three odd cycles gives probability at most \(3/4<1\). Some syndrome-preserving cut therefore makes every cycle nondirected; the cactus orientation is acyclic and extends to a total order realizing that syndrome. Apply the affine path equation and reverse-order oddness. \(\square\)

**Corollary (four odd cycles).** The same conclusion holds for a cactus having four odd cycles provided at least one of them has \(t_C\ge3\): their total failure-probability upper bound is then at most \(3/4+1/8=7/8<1\). Thus failure of the present union-bound technique with four odd cycles can occur only if all four have reader-image cut rank two. This does not assert a NORI1 counterexample in that case.

The chromatic-rank inequality is a new all-order constraint on the exchange graph: an odd feedback cycle forces two independent variations inside \(\operatorname{im}L\), and any higher chromatic complexity forces still more. The remaining affine closure challenge lies in coupled forbidden patterns across several odd cycles, rather than isolated cyclic feedback.



## Joint-rank counting of syndrome-preserving odd-cycle repairs

Let \(L\) be a zero-diagonal row-odd affine reader matrix, and let its visible exchange graph be a cactus with odd cycles \(C_1,\ldots,C_h\). Put \(K=\operatorname{im}L\), \(r=\dim K\). Fix a base orientation with one backward edge on each simple cycle and arbitrary bridge orientations. For each odd cycle let \(D_j\) be the vertex-to-edge cut map on its edges and let \(\eta_j\) be the one cut-reversal pattern that makes that cycle directed.

Fix any desired quotient syndrome represented by \(s_0\in\mathbb F_2^n\). The cuts realizing that syndrome are \(s_0+k\) with \(k\in K\). For \(J\subseteq[h]\), write \(D_J=(D_j)_{j\in J}\), \(t_J=\operatorname{rank}(D_J|_K)\), and let \(\epsilon_J=1\) if the equations \(D_Jk=(\eta_j+D_js_0)_{j\in J}\) are consistent on \(K\), and zero otherwise. Take \(t_\varnothing=0,\epsilon_\varnothing=1\).

**Theorem (joint-rank repair count).** The number of cut switches having that quotient syndrome and preserving acyclicity is
\[
\boxed{N(s_0)=\sum_{J\subseteq[h]}(-1)^{|J|}\epsilon_J2^{r-t_J}.}
\tag{JR1}
\]
In particular, \(N(s_0)>0\) for every quotient syndrome implies monochromatic full antipodal geodesics for every affine offset.

*Proof.* An even cycle never becomes directed under cut switching: its odd opposition parity is unchanged. For an odd cycle \(C_j\), the one directed orientation compatible with the initial opposition parity occurs if and only if \(D_j(s_0+k)=\eta_j\). For each \(J\), the simultaneous bad events comprise an affine solution set of the map \(D_J|_K\), empty if inconsistent and otherwise containing \(2^{r-t_J}\) cuts. Inclusion–exclusion therefore counts the cuts avoiding every directed cycle. A cactus has no other simple cycles, so each counted orientation is acyclic and extends to a total dimension order. The previously proved cut-sum identity realizes the desired cokernel syndrome. \(\square\)

**Corollary (arbitrarily many independent odd cycles).** If
\[
\boxed{t_{[h]}=\sum_{j=1}^h t_{\{j\}},}
\tag{JR2}
\]
then every affine offset is favorable, regardless of the number of odd cycles. Quantitatively,
\[
\boxed{N(s_0)\ge 2^r\prod_{j=1}^h(1-2^{-t_{\{j\}}})>0.}
\tag{JR3}
\]
Equality holds when every individual bad-cycle pattern is attainable for that syndrome.

*Proof.* Condition (JR2) says the joint map \(K\to\bigoplus_jD_j(K)\) is surjective. Therefore for uniformly chosen \(k\in K\), the images \(D_jk\) are independent and uniform. Each bad-cycle event has probability zero if its target lies outside the affine image, and otherwise \(2^{-t_j}\). Independence gives the claimed product lower bound, with the stated equality condition. Every \(t_j\ge2\) by the earlier chromatic-rank theorem. \(\square\)

**Corollary (four odd cycles).** For a cactus with four odd cycles, the cut repair works for every syndrome if at least one cycle has \(t_j\ge3\), or if all \(t_j=2\) and one pair of cycle maps has joint rank four. More generally, in a fixed syndrome fiber with four rank-two bad events, any overlap of two bad-event affine subspaces forces an acyclic cut.

*Proof.* If one rank is at least three, the union bound gives total bad probability at most \(1/8+3/4<1\). Otherwise each of four bad events has size at most \(2^{r-2}\). An overlapping pair makes the union strictly smaller than \(2^r\). Joint rank four forces overlap whenever both bad patterns are individually attainable, and if one is unattainable then only three bad events remain. \(\square\)

**Remaining obstruction.** Failure of the four-cycle repair for a particular syndrome would require four pairwise disjoint codimension-two affine bad-event subspaces partitioning the syndrome fiber. This is an obstruction only to the chosen cut-switch orbit; other acyclic orientations can still realize the same syndrome. The new counting formula retains the interactions among odd cycles discarded by the earlier union bound.



## Four-cycle cut obstruction has rank at most three

**Lemma (four-flat partition).** If four affine codimension-two subspaces \(E_1,\ldots,E_4\) cover a binary vector space \(K\), their four defining two-dimensional normal spaces \(R_i\subseteq K^*\) together span a space of dimension at most three.

*Proof.* Each flat has one quarter of \(K\), so the four covering flats are pairwise disjoint. Two disjoint codimension-two affine flats must have intersecting normal spaces: if their normals were disjoint, their joint affine equations would have full rank four and hence always admit a solution. Thus all \(R_i\) meet pairwise. If at most two distinct normal planes occur, their sum has dimension at most three. If three distinct normal planes all share a common line \(\langle\phi\rangle\), their three pairwise disjoint affine flats would need pairwise different values of the single binary functional \(\phi\), impossible. Otherwise three normal planes have three different pairwise intersection lines and span a three-dimensional space \(W\), with trivial common intersection. Any fourth plane meeting all three must lie inside \(W\): a plane outside \(W\) meets \(W\) in at most one line, which would then need to belong to all three. Hence the total normal span has dimension at most three. \(\square\)

**Theorem (four odd cycles at joint rank four).** Let the visible exchange graph of a zero-diagonal row-odd affine reader matrix be a cactus with at most four odd cycles \(C_j\). Put \(K=\operatorname{im}L\). If the joint map \(k\mapsto(D_{C_j}k)_j\) on \(K\) has rank at least four, then every offset admits a monochromatic-zero full antipodal geodesic and its complementary reversed-order partner.

*Proof.* Every odd cycle has individual reader-image cut rank at least two. If there are at most three cycles, or if one of the four ranks is at least three, the earlier union bound works. Otherwise four cycle-bad events in a fixed target syndrome fiber are affine codimension-two flats. If they covered the fiber, they would partition it into four flats, forcing the combined rank of their normal spaces at most three by the lemma. That contradicts joint rank at least four. Hence some cut in every target syndrome fiber makes the exchange orientation acyclic; extend it to a total dimension order and apply the affine monochromatic path equation. \(\square\)

The remaining four-odd-cycle obstruction to this cut-switch method requires all four individual ranks equal two and combined rank at most three. This does not assert a coloring counterexample. The four-flat rank lemma was also independently checked in binary dimensions three and four; its proof applies for all dimensions.


## Single-edge pivot theorem for four odd cycles

**Lemma.** Let \(C\) be an odd cycle in the visible exchange graph of a zero-diagonal row-odd reader matrix \(L\). Orient \(C\) with one backward edge \(b\). Reversing a forward edge \(e=\{i,j\}\ne b\) changes the base order syndrome by \(q(d_e)\), where \(d_e=L_{ij}e_i+L_{ji}e_j\). Compensate by changing the cut indicator from \(s_0+k\) to \(s_0+d_e+k\). Then the forbidden directed-cycle equation for \(C\) shifts by
\[
\boxed{\Delta_C(e)=\mathbf1_{E(C)\setminus\{e\}}+D_C(d_e).}
\]
It is nonzero if \(|C|\ge5\). For a triangle it is zero if and only if \(L_{ij}=L_{ji}=1\).

*Proof.* With one backward edge \(b\), the possible directed-cycle target in its cut class is reached by switching all edges except \(b\). After flipping forward edge \(e\), the base orientation has two backward edges \(b,e\) and its possible directed-cycle target requires switching \(b,e\). The two required patterns differ on every edge other than \(e\). The compensated cut shift contributes \(D_C(d_e)\). Since \(d_e\) is supported on the endpoints of \(e\), its cycle cut has at most two edges. If \(|C|\ge5\), the first term has at least four and cannot cancel. On a triangle its cancellation requires both coefficients of \(d_e\) equal one. \(\square\)

**Theorem.** Suppose the visible exchange graph is a cactus with at most four pairwise vertex-disjoint odd cycles. If there are four, assume some odd cycle has length at least five or some triangle edge fails \(L_{ij}=L_{ji}=1\). Then every affine offset admits monochromatic full antipodal geodesics.

*Proof.* Three or fewer odd cycles are covered by the existing union bound. With four, orient each cycle with one backward edge, choosing the designated cycle's backward edge different from the pivot \(e\) above. Fix a target syndrome and its affine cut fiber \(s_0+\operatorname{im}L\). If it contains no acyclic cut, the four cycle-bad events must partition the fiber, since each has size at most one quarter. Pick \(k\) in the bad event of the designated cycle \(C\); the other odd cycles are not directed by this cut. Reverse the base edge \(e\) and change the cut to \(s_0+d_e+k\). Vertex-disjointness means every other odd cycle retains its previous cut pattern and stays nondirected. The forbidden equation for \(C\) shifts by \(\Delta_C(e)\ne0\), so \(C\) also becomes nondirected. Every even cycle is protected by its opposition parity. The switched orientation is acyclic, extends to a total order, and has the target syndrome. Solve the affine monochromatic-path equation. \(\square\)

Only four fully bidirectionally saturated triangles remain outside this pivot criterion; the joint-rank-four theorem handles those when their combined reader-image cut rank is at least four.


## Pivot repair when odd cycles share vertices

The syndrome-preserving orientation pivot only needs its selected edge's two endpoints to avoid all *other odd cycles*. Full pairwise vertex-disjointness of the odd cycles is unnecessary.

**Theorem (an exposed pivot edge).** Let the visible exchange graph of a zero-diagonal row-odd affine reader matrix be a cactus with at most four odd cycles. Suppose that, if four are present, some odd cycle \(C\) contains an edge \(e=\{i,j\}\) whose two endpoints belong to no other odd cycle, and either (i) \(|C|\ge5\), or (ii) \(C\) is triangular and \(L_{ij},L_{ji}\) are not both one. Then every affine offset admits a monochromatic-zero full geodesic and its complementary reversed-order geodesic.

*Proof.* Use the preceding pivot theorem's argument. A hypothesized missing target syndrome forces the four odd-cycle bad-event flats to partition its cut fiber. Choose a cut which directs only the designated cycle \(C\). Reverse the chosen forward base edge \(e\) and compensate for its syndrome change by shifting the cut indicator by \(d_e=L_{ij}e_i+L_{ji}e_j\). The pivot-change vector
\[
\Delta_C(e)=\mathbf1_{E(C)\setminus\{e\}}+D_C(d_e)
\]
is nonzero under (i) or (ii), so the designated cycle becomes nondirected. Because the support of \(d_e\) lies at endpoints belonging to no other odd cycle, the other three odd cycles retain their safe cut patterns. Even cycles are protected by the parity of their oppositely oriented edges. Thus the new orientation is acyclic, with the required cokernel syndrome, and extends to a favorable dimension order. \(\square\)

**Corollary (every exposed long odd cycle is harmless).** In particular, every visible exchange cactus with at most four odd cycles and **at least one odd cycle of length seven or greater** is favorable for every affine offset, even if the odd cycles share vertices.

*Proof.* A cactus's distinct simple cycles share at most one vertex. Hence a chosen odd cycle \(C\) meets the other at most three odd cycles in at most three vertices. If \(|C|=m\ge7\) is odd, at least \(m-3\) of its vertices belong to no other odd cycle. Since \(m-3>\lfloor m/2\rfloor\), those vertices cannot be an independent set of the cycle, so some edge has both endpoints unshared. The pivot theorem applies. \(\square\)

For a five-cycle, the same conclusion holds when at most two of its vertices lie on other odd cycles. The remaining four-cycle cut-repair configurations now involve only short odd feedback cycles or a small number of heavily shared junction vertices. These are limitations of the cut-switch construction, not counterexamples to NORI1.



## Classification of the four-flat rank-three cut obstruction

The previous joint-rank and edge-pivot theorems leave a tightly constrained cut-switch obstruction with four odd cycles. When their four codimension-two forbidden affine sets partition one syndrome fiber and their combined normal rank is three, the quotient is a perfect matching of the eight points of \(\mathbb F_2^3\). The matchings admit a complete affine-symmetry classification.

**Theorem (three affine matching types).** Let \(K\) be a binary vector space partitioned into four affine subspaces of codimension two, and suppose the span \(W\le K^*\) of their defining normal spaces has dimension three. Quotienting by \(W^\perp\) yields four disjoint affine lines (two-point sets) partitioning \(\mathbb F_2^3\). Up to the action of \(\operatorname{AGL}(3,2)\), there are precisely three possible perfect-matching types, distinguished by the multiplicities of their four nonzero pair-difference vectors:
\[
\boxed{(4),\qquad(2,2),\qquad(1,1,1,1).}
\]
Among all \(105\) perfect matchings of eight points, these classes contain respectively
\[
\boxed{7,\qquad42,\qquad56}
\]
matchings. In the stipulated combined-normal-rank-three case, the all-parallel type \((4)\) is impossible; only \((2,2)\) and \((1,1,1,1)\) remain.

*Proof.* For the four matched pairs \(\{x_j,y_j\}\) put \(d_j=x_j+y_j\in\mathbb F_2^3\setminus\{0\}\). Since each of the eight points occurs once,
\[
d_1+d_2+d_3+d_4=\sum_{x\in\mathbb F_2^3}x=0.
\]
Four nonzero binary vectors summing to zero can have multiplicities only \((4)\), \((2,2)\), or \((1,1,1,1)\): three copies of one vector and a fourth would force all four equal, and one repeated pair with two distinct singletons would force those singletons equal.

If all four differences equal \(d\ne0\), the matching must be the translation pairing \(x\leftrightarrow x+d\). There is one for each of seven nonzero \(d\), giving seven matchings.

If two different directions \(d,e\) each occur twice, partition \(\mathbb F_2^3\) into the two cosets of the plane \(\langle d,e\rangle\). The matching on each four-point coset must consist of two parallel pairs, and the two cosets must use opposite directions to achieve multiplicities \((2,2)\). There are two such matchings for each of the \(\binom72=21\) unordered pairs \(\{d,e\}\), giving 42.

There are \((8-1)!!=105\) perfect matchings in total, leaving \(105-7-42=56\) with four distinct directions. Their four difference vectors sum to zero and hence form one of seven four-direction sets, each the complement of the three nonzero vectors of a two-dimensional linear subspace. For each fixed direction set there are eight matchings. The translation group of \(\mathbb F_2^3\) acts freely on these eight matchings: a nonzero translation preserving one would preserve every pair difference; as those differences are all distinct, it would fix each pair individually. A fixed two-point pair must have that translation as its difference, which cannot equal four distinct differences simultaneously. Thus translations act transitively for each fixed direction set. The linear group is transitive on the seven nonzero directions, on unordered pairs of distinct nonzero directions, and on the seven four-direction sets. Consequently each of the three multiplicity types is one affine orbit.

For the all-parallel type, all four two-point affine lines have the same direction \(d\), so their normal spaces coincide with \(d^\perp\), of dimension two. It cannot have combined normal rank three. \(\square\)

**Corollary (two residual rank-three cut templates).** In the four-odd-cycle cactus cut-switch analysis, suppose a target syndrome has no acyclic cut in the selected base orientation, and suppose the combined reader-image cut rank equals three. Then the four forbidden-cycle affine subspaces form, on a three-bit quotient, one of only the \((2,2)\) and \((1,1,1,1)\) affine matching templates. This classifies failures of this *cut-switch construction*, not counterexamples to the monochromatic affine path theorem or NORI1.

**Next repair target.** Study how the syndrome-preserving single-edge pivot acts on these two matching templates, especially when all four odd cycles are internally saturated triangles or share junction vertices. The preceding exposed-edge theorem already eliminates every four-cycle cactus with an exposed nonsaturated pivot edge; the classification isolates the remaining three-bit configurations.


Saturated-cycle flux. For the zero-diagonal odd-row reader matrix L, let alpha_i=[e_i] in coker L and w_ij=[L_ij e_i+L_ji e_j]. At a bidirectionally saturated visible cycle C with consecutive vertices i-1,i,i+1, let sigma_i be the sum of incident visible exchange weights outside C. The singleton cut formula yields alpha_(i-1)+alpha_i+alpha_(i+1)=sigma_i. On a saturated triangle all three exterior fluxes are equal to [e_i+e_j+e_k]. Hence no saturated triangle can have precisely one exterior bridge, and a bare bow tie of two saturated triangles is impossible. If an odd saturated cycle has external edges at at most one vertex, the homogeneous binary recurrence is period three. For length indivisible by three, an isolated forcing would restrict all alpha_i to {0,sigma}, contradicting visibility on an odd cycle. For length divisible by three, the self-adjoint recurrence and a period-three kernel vector force sigma=0. Thus such a cycle has length divisible by three and zero net exterior flux.


### Structural proof and four-block consequence of the flux law

For a saturated visible cycle of length m, write alpha_i=[e_{v_i}], and denote by sigma_i the sum of exchange weights on visible edges incident at v_i but not on the cycle. The singleton cut law gives
\[
\alpha_{i-1}+\alpha_i+\alpha_{i+1}=\sigma_i.
\]
If at most one sigma_i is nonzero, the homogeneous recurrence alpha_(i+1)=alpha_i+alpha_(i-1) has period three. If 3 does not divide m, the cyclic recurrence operator is invertible: any homogeneous solution of period dividing both m and three must be constant and hence zero. A single localized source therefore makes every alpha_i either zero or the same source vector, contradicting nonzero edge weights alpha_i+alpha_(i+1) around an odd cycle. If 3 divides m, choose a homogeneous period-three binary solution taking value one at the source location. Self-adjointness of the recurrence operator forces the source to vanish. Thus m is divisible by three and all projected vertex classes repeat as u,v,u+v.

For a saturated triangle T=(h,u,v), each of its three exterior fluxes equals [e_h+e_u+e_v]. If u and v have no exterior visible edges, the exterior flux at h must be zero. If h has one exterior bridge, its nonzero weight contradicts this. If a second saturated triangle is attached to T solely at h, its two edges at h sum to the nonzero weight of the edge opposite h, again a contradiction.

**Corollary (four bare saturated triangle blocks cannot occur).** A connected visible exchange cactus whose only edge-blocks are four saturated triangular blocks and which has no bridge edges is impossible.

*Proof.* A leaf triangle of the block-cut tree cannot attach through an articulation belonging to only two blocks, by the preceding bow-tie computation. With only four triangle blocks, avoiding such a leaf requires all four triangles to share one articulation h. Let a_i be the nonzero weight of the edge of triangle i opposite h. The exterior-flux identity at the other two vertices of each triangle gives sum_(j != i) a_j=0. Thus all a_i equal A=sum_j a_j. But A=4A=0 in characteristic two, contradicting a_i != 0. \(\square\)

This identifies a real matrix obstruction to the four-saturated-triangle cactus scenario: additional visible edges must enter to balance its cycle fluxes.



## Bridge-compensated cycle-edge pivot

The remaining four-odd-cycle syndrome problem admits an additional constructive closure criterion. Let G be the visible exchange cactus and let B be the binary linear span of its **bridge-edge exchange weights** in V=coker(L).

**Theorem (bridge-compensated pivot).** Suppose G has at most four odd simple cycles. If one of those odd cycles C contains an edge e whose exchange weight satisfies
\[
\boxed{w_e\in B,}
\]
then every affine offset admits a monochromatic-zero full antipodal geodesic, and the reversed full dimension order from the same root gives a monochromatic-one geodesic. No reader-rank or ambient-dimension restriction is required.

*Proof.* Begin with the cactus orientation having one backward edge on every simple cycle, and orient its bridge edges arbitrarily. Fix a desired cokernel syndrome. If a cut switch within its required affine cut fiber makes all cycles nondirected, the established order-syndrome equation yields a favorable path.

Otherwise the prior rank bound for odd visible cycles applies: with three or fewer odd cycles the total density of bad cuts is below one. Therefore there are four odd cycles. Each bad-cycle event has density at most one quarter in the cut fiber. Because the four events cover that fiber, they are necessarily four nonempty, pairwise disjoint events of density one quarter each. Choose a cut which makes C directed and leaves the other three odd cycles nondirected; even cycles cannot become directed by cut switching, because their odd opposition parity is invariant.

The resulting orientation is cyclic solely on C. Reverse the orientation of the chosen edge e on C; this breaks its directed cycle. Since w_e lies in the bridge-weight span, select a set of bridges whose weights sum to w_e and reverse their orientations too. Every bridge lies on no simple cycle, so these extra reversals affect no cycle orientations. The total change in the permutation-inversion syndrome equals w_e plus the selected bridge-weight sum, which is zero. The new orientation is acyclic, has the required cokernel syndrome, and extends to a total order of the cube dimensions. Solve Lx=a+b_pi for its starting root. Odd row sums imply the reverse dimension order from that root has all colors complemented. \(\square\)

**Corollary.** A failure of the current cut-repair strategy on a cactus with four odd cycles requires, for every odd cycle C, that **none** of its edge exchange weights lie in the span of all bridge weights. This is a further restriction on the residual saturated-triangle patterns. It is not an obstruction to NORI1 itself.

**Proof-closure route.** The saturated-triangle exterior-flux law forces balanced visible attachments, and the present theorem converts suitably related bridge weights into a complete orientation repair. The remaining local question is whether the row-odd, zero-diagonal reader conditions force a nontrivial bridge-span intersection with some cycle-edge label whenever four saturated triangles produce a rank-three bad-flat partition. A positive answer would close that residual affine cactus case.


## Hall–Rado repair of arbitrarily many odd affine exchange cycles

Let \(L\) be a zero-diagonal binary matrix with \(L\mathbf1=\mathbf1\), and assume its visible exchange graph is a cactus. Write \(K=\operatorname{im}L\) and let \(D_C\) be the cut map of an odd visible cycle \(C\).

**Theorem.** Suppose every nonempty family \(S\) of odd cycles obeys
\[
\boxed{\operatorname{rank}(D_SL)\ge |S|.}
\]
Then for every offset \(a\), the affine coloring \(c_i(x)=(Lx)_i+a_i\) admits a monochromatic full antipodal geodesic and its complementary reversed-order geodesic, regardless of the number of odd cycles.

*Proof.* Start with an acyclic orientation containing one backward edge per simple cycle, and choose a cut representative \(s_0\) giving the desired quotient syndrome. All admissible cut adjustments are \(s_0+k\) with \(k\in K\). Each odd cycle has one forbidden directed cut pattern \(\eta_C\); even cycles remain nondirected because cut switches preserve odd opposition parity. The row space \(U_C\subseteq K^*\) of \(D_C|_K\) consists of linear tests of the cycle cut pattern. The displayed rank condition is the Hall--Rado independent-transversal condition. It selects independent nonzero \(\phi_C=\lambda_CD_C|_K\), one per odd cycle. Impose \(\phi_C(k)=1+\lambda_C(\eta_C+D_Cs_0)\). These independent affine equations have a solution, making every odd cycle nondirected. The resulting orientation extends to a total dimension order \(\pi\) whose predecessor syndrome equals the prescribed class. Thus \(Lx=a+b_\pi\) is solvable and gives a monochromatic full geodesic. Reversing \(\pi\) complements every edge bit. \(\square\)

Unlike the previous criterion requiring complete independence of the cycle cut-variation spaces, this theorem needs only one independent test per cycle. It is the same subspace-matroid selection mechanism previously used for favorable-root gluing in Article XV.

## Simultaneous exposed pivots and hybrid matroid repair

For an odd cycle \(C\) in the visible exchange cactus, call an edge \(e=\{i,j\}\) **exposed** when neither endpoint belongs to another odd cycle. Put \(d_e=L_{ij}e_i+L_{ji}e_j\) and \(\Delta_C(e)=\mathbf1_{E(C)\setminus\{e\}}+D_C(d_e)\). An exposed edge is **effective** if \(\Delta_C(e)\ne0\). Every odd-cycle edge in length at least five is effective; in a triangle, an edge is effective unless \(L_{ij}=L_{ji}=1\).

**Theorem (unbounded simultaneous pivot closure).** If every odd cycle has an exposed effective edge, every affine offset yields opposite monochromatic full geodesics, with **no restriction on the number of odd cycles**.

*Proof.* Choose an acyclic base orientation having one backward edge per cycle, distinct from its designated effective edge. Fix any cut \(s\) representing the desired quotient syndrome, and let \(\mathcal B\) be all odd cycles that it makes directed. For every \(C\in\mathcal B\), flip the designated base edge \(e_C\), and change the cut to \(s'=s+\sum_{C\in\mathcal B}d_{e_C}\). The change in base-order syndrome equals \(\sum_{C\in\mathcal B}q(d_{e_C})\), so compensation preserves the target quotient. On a repaired cycle \(C\), all other compensation vectors restrict to zero because their endpoints lie outside \(C\). Its forbidden equation changes by \(\Delta_C(e_C)\ne0\), so it is no longer directed. Unmodified odd cycles receive no change. Every even cycle remains nondirected by its opposition parity. Each modified base cycle has two backward edges, so the new base orientation is still acyclic. The final switched orientation is acyclic, extends to a dimension order, and solves the monochromatic affine path equation. \(\square\)

**Theorem (hybrid matroid-pivot closure).** Partition the odd cycles into \(\mathcal H\) and \(\mathcal P\). Suppose every subfamily \(S\subseteq\mathcal H\) satisfies \(\operatorname{rank}(D_SL)\ge|S|\), and each cycle in \(\mathcal P\) has an exposed effective edge relative to all odd cycles. Then every affine offset is favorable, regardless of the number of cycles.

*Proof.* Apply the preceding Hall--Rado theorem's independent linear tests to obtain a syndrome-compatible cut protecting all cycles in \(\mathcal H\). Pivot simultaneously those cycles in \(\mathcal P\) that remain directed. Exposure makes all compensations vanish on every other odd cycle, including those in \(\mathcal H\). The resulting orientation is acyclic with the prescribed syndrome. \(\square\)

This removes the earlier three- or four-odd-cycle counting threshold whenever cycle-local pivots or independent reader-image tests are available. A residual obstruction to **this proof method** must consist of a rank-deficient cycle cluster that cannot be eliminated by exposed effective pivots; it is not a counterexample to NORI1.

## Chordless-cycle independent tests for general exchange graphs

The Hall--Rado safe-test method also applies to **arbitrary** visible exchange graphs, not only cacti. Fix an acyclic orientation \(O\) and its total order \(\pi_0\). It suffices to control the chordless cycles: a shortest directed cycle has no chord, since either direction of a chord would form a shorter directed cycle.

For each chordless cycle \(C\), choose a cyclic traversal, let \(B_C\) record the base edges pointing against it, and let \(D_C\) be its vertex-cut map. For cuts \(s\), the opposition pattern becomes \(B_C+D_Cs\), whose parity is unchanged because every cycle meets a cut evenly. Thus an odd cycle has one potentially directed opposition pattern; an even cycle with odd base opposition parity has none; and an even cycle with even base opposition parity has two, namely \(0\) and \(\mathbf1_C\).

Set \(K=\operatorname{im}L\). For each **nonprotected chordless cycle**, define its linear safe-test space in \(K^*\):
\[
U_C=\begin{cases}
\{\lambda D_C|_K:\lambda\in\mathbb F_2^{E(C)}\},&|C|\text{ odd},\\
\{\lambda D_C|_K:\lambda\cdot\mathbf1_C=0\},&|C|\text{ even and unprotected}.
\end{cases}
\]
For an even cycle, a test in \(U_C\) takes the same value on both directed opposition patterns; choosing the opposite value eliminates both. Its dimension is at least \(\operatorname{rank}(D_CL)-1\).

**Theorem (general chordless-cycle Hall closure).** If for every subfamily \(S\) of the nonprotected chordless cycles,
\[
\boxed{\dim\sum_{C\in S}U_C\ge|S|,}
\]
then every affine offset \(a\) admits a full monochromatic antipodal geodesic.

*Proof.* Rado's theorem supplies linearly independent nonzero safe tests \(\phi_C=\lambda_CD_C|_K\), one for each nonprotected chordless cycle. Fix a cut representative \(s_0\) of the target quotient syndrome. For each odd cycle prescribe \(\phi_C(k)\) opposite to its single forbidden opposition-pattern evaluation, accounting for \(B_C+D_Cs_0\). For each unprotected even cycle, its two forbidden evaluations coincide because \(\lambda_C\cdot\mathbf1_C=0\); prescribe the opposite value. The independent affine system on \(k\in K\) is solvable. The cut \(s_0+k\) cannot direct any chordless cycle and therefore cannot direct any cycle. The switched orientation has a topological dimension order realizing the chosen quotient syndrome, which solves \(Lx=a+b_\pi\) and produces a monochromatic full geodesic. \(\square\)

**Limit.** Dense exchange graphs may have many more chordless cycles than the rank of \(L\), preventing independent tests even when monochromatic paths exist. This theorem is a checkable sufficient criterion, not full affine closure. It extends the safe-parity matroid mechanism from favorable-root factor constraints in Article XV to the topology of permutation-exchange cycles in Article XIV.

## Minimal deficient cycle clusters and leaf saturated triangles

**Lemma (minimal Hall defect).** Let \(U_C\) be the safe-test spaces of a family of odd exchange cycles, and choose an inclusion-minimal family \(S\) with \(\dim\sum_{C\in S}U_C<|S|\). Then
\[
\boxed{\dim\sum_{C\in S}U_C=
\dim\sum_{C\in S\setminus\{D\}}U_C=|S|-1
\quad\text{for all }D\in S.}
\]
*Proof.* By minimality, deleting any member leaves rank at least \(|S|-1\). The full family has rank below \(|S|\), so both ranks equal \(|S|-1\). Thus no cycle has a private test direction, while every proper subfamily admits independent tests. \(\square\)

**Lemma (a leaf reader supplies a private repair).** Let \(C=\{i,j,h\}\) be a bidirectionally saturated visible triangle, with \(i\) having visible degree two, so its only visible neighbors are \(j,h\). Suppose there exists \(t\notin C\), lying on no other odd cycle, such that \(L_{it}=1\). Then some \(u\in\operatorname{im}L\) satisfies
\[
\boxed{D_Cu\ne0,\qquad D_Du=0
\quad\text{for every other odd cycle }D.}
\]
*Proof.* The exchange edge \(\{i,t\}\) is invisible by the degree-two assumption; hence \(u=d_{it}=e_i+L_{ti}e_t\in\operatorname{im}L\). Its endpoints lie outside all other odd cycles, so their cut restrictions there are zero. On \(C\), its restriction is the singleton \(i\), which changes the two incident triangle edges and is nonzero. \(\square\)

Since a saturated triangle row has two internal ones, odd row parity forces each triangle vertex to read an odd number of directions outside the triangle. Accordingly, any saturated leaf triangle resisting this repair must have every outside reader of its nonattachment vertices lying on another odd cycle. This is a structural condition on failure of the *repair method*, not a counterexample to the affine conjecture.

## Neutral cohomology identity and editorial correction

Let K=im L, q:F2^n -> F2^n/K, G the visible exchange graph with n vertices, m edges, c components and g=m-n+c independent graph cycles. Let D be the graph cut map, B the map taking visible edge ij to L_ij e_i+L_ji e_j, and W=qB. The universal cut identity gives WD=q.

**Theorem.** The neutral edge-change code Z=ker W obeys
[
Z=im(I+DB)+D(K),qquad Zcap im(D)=D(K).
]
There is a short sequence
[
0longrightarrow D(K)longrightarrow Z
longrightarrow H^1(G;F2)longrightarrow0.
]
Moreover ker D is contained in K, dim D(K)=rank(L)-c and dim Z=rank(L)-c+g. Every target syndrome fiber has 2^g graph-cycle parity classes, all of cardinality 2^(rank(L)-c).

*Proof.* WD=q gives W(I+DB)=W+qB=0. If Wz=0 then Bz belongs to K and z=(I+DB)z+D(Bz). If Ds belongs to Z then q(s)=WDs=0, hence s belongs to K. This proves the neutral cut identity and also ker D subset K. Its dimension is c, giving dim D(K)=rank(L)-c; surjectivity of W gives dim Z=m-n+rank(L). Every generator (I+DB)e has the same graph-cycle intersection parities as e, as DB(e) is a cut. Such edge vectors span H^1(G;F2), proving the sequence and uniformity. QED.

**Correction.** The full parity-preserving neutral code coincides with the reader-image cut code D(K); the former Hall condition is not stronger. Under h independent tests on odd cycles in D(K), the proof guarantees 2^(rank(L)-c-h) favorable orientations and at least 2^(n-c-h) root/order witnesses, not the previously stated 2^(n-c). The existence assertion survives. Any neutral move outside D(K) must change graph-cycle parity.

Each visible graph component indicator lies in im L, since it belongs to ker D.


## A full neutral-code Hall theorem for arbitrary exchange graphs

The cohomology sequence above identifies the limitation of parity-preserving cuts. A stronger orientation theorem works directly in the full neutral code \(Z=\ker W\), allows changes of graph-cycle parity, and handles graphs with overlapping cycles and chords.

Fix any zero-diagonal row-odd reader matrix \(L\). Let \(G\) be its visible exchange graph with \(m\) edges and \(c\) connected components, let \(V=\mathbb F_2^n/\operatorname{im}L\), and let \(W:\mathbb F_2^{E(G)}\to V\) be the exchange-weight map. The preceding theorem shows \(W\) is onto. Let \(\mathcal C\) be the collection of *chordless* simple cycles of \(G\).

For \(C\in\mathcal C\), let \(P_C\) restrict edge-change vectors to the edges of \(C\). Define the **bidirectional-safe test space**
\[
U_C=\{\ z\mapsto\lambda\cdot P_Cz:\ \lambda\in\mathbb F_2^{E(C)},\
\lambda\cdot\mathbf1_{E(C)}=0\ \}\subseteq Z^*.
\tag{NT1}
\]
These linear tests involve an even number of edges of \(C\). Because the clockwise and counterclockwise fully directed orientations differ by \(\mathbf1_{E(C)}\), every such test takes the same value on **both** directed orientations.

**Theorem (full neutral-code independent-test closure).** If
\[
\boxed{\dim\sum_{C\in S}U_C\ge|S|
\qquad\text{for every }S\subseteq\mathcal C,}
\tag{NT2}
\]
then every affine offset \(a\) gives a full dimension-simple monochromatic-zero antipodal geodesic, and reversal of its dimension order from the same root gives a monochromatic-one geodesic. Quantitatively, there are at least
\[
\boxed{2^{m-|\mathcal C|}}
\tag{NT3}
\]
different root-and-dimension-order monochromatic-zero certificates for each offset.

*Proof.* Fix a reference dimension order and encode every orientation of \(G\) by its difference from that reference. A vector \(o\in\mathbb F_2^{E(G)}\) has the target affine monochromatic syndrome precisely when \(W(o)\) equals the prescribed class in \(V\). Since \(W\) is onto, choose one such orientation vector \(o_0\). All target-syndrome orientations form the affine fiber \(o_0+Z\).

For each chordless cycle \(C\), choose one of its two directed orientations and let \(\gamma_C\in\mathbb F_2^{E(C)}\) be its bit pattern relative to the global orientation reference. The opposite directed orientation has pattern \(\gamma_C+\mathbf1_{E(C)}\). Any even-edge functional \(\lambda\) satisfying (NT1) has the same value \(\lambda\cdot\gamma_C\) on these two patterns.

By Rado's independent-transversal theorem, the rank inequalities (NT2) permit nonzero linearly independent test functionals \(\phi_C\in U_C\), one for each \(C\). Choose any even-edge representative \(\lambda_C\) for each \(\phi_C\). Impose on the neutral correction \(z\in Z\) the affine equations
\[
\phi_C(z)=1+\lambda_C\cdot\gamma_C+\lambda_C\cdot P_C(o_0)
\quad(C\in\mathcal C).
\]
Since the functionals are independent, these equations have \(2^{\dim Z-|\mathcal C|}\) solutions. For every solution, each chordless cycle's chosen test differs from the common value on its two directed orientations, so no chordless cycle is directed. Every directed cycle contains a chordless directed cycle (split a directed cycle along a chord, taking the direction of the chord that closes one of the two directed segments). Hence the resulting orientation of \(G\) is acyclic and extends to a total dimension order \(\pi\). The affine syndrome equation gives a solution root \(x\) to \(Lx=a+b_\pi\). Reversal from \(x\) complements each edge color by the odd row sum.

The count of neutral corrections is \(2^{m-\operatorname{corank}L-|\mathcal C|}\). Distinct corrections give distinct visible orientations and therefore distinct resulting total orders; every such order has \(2^{\operatorname{corank}L}\) starting roots. Their product is \(2^{m-|\mathcal C|}\), proving (NT3). \(\square\)

**Corollary (cactus multiplicity).** If the visible exchange graph is a cactus with \(g\) simple cycles and (NT2) holds for its cycle-test spaces, then every affine offset has at least
\[
\boxed{2^{n-c}}
\]
root/order certificates, because \(m=n-c+g\). This is a **different, stronger hypothesis** than the old Hall theorem restricted to parity-preserving reader-image cuts; the corrected bound for that old theorem remains \(2^{n-c-h}\), where \(h\) is its number of odd-cycle tests.

**Lemma (no vacuous single-cycle test).** For every visible simple cycle \(C\), the safe-test space \(U_C\) is nonzero. If \(C\) has even length, choose an edge \(e\in C\). Its neutral generator \(F_e=(I+DB)e\) has odd edge-change parity on \(C\), whereas the all-one cycle pattern has even parity. Thus some even-edge functional detects \(F_e\). If \(C\) has odd length, the chromatic-rank theorem gives \(\dim D_C(K)\ge2\). If all even-edge tests vanished, this image would lie in the one-dimensional orthogonal complement of the even-edge functionals, a contradiction. This is a necessary local ingredient, though it does not by itself imply the joint Hall condition for many cycles.

**Closure interpretation.** The theorem reduces affine NORI1 on **arbitrary visible exchange graphs** to a representable-matroid transversal problem on the full syndrome-neutral edge code. Unlike fixed-parity cut arguments, the test may simultaneously veto the two directed orientations of a cycle, so odd and even cycles are handled uniformly and overlapping cycles pose no logical difficulty beyond their linear dependence. A minimal failure of (NT2) yields a rank-deficient family of chordless cycles, providing a specific structural target for further repair surgery. Failure of this sufficient condition does not demonstrate a counterexample to NORI1.



## Triangular neutral repairs and feedback exchange matrices

The full neutral-code Hall theorem admits a direct constructive form in terms of syndrome-neutral orientation footprints. It includes simultaneously exposed pivots as a special case and works on **any** visible exchange graph, including graphs with chords and overlapping cycles.

Let \(\mathcal C\) be the chordless cycles of \(G\), \(Z=\ker W\). For every \(C\in\mathcal C\), choose a neutral edge-change vector \(z_C\in Z\) such that its restriction \(p_C=z_C|_{E(C)}\) is neither zero nor the all-one vector. There is then an even-cardinality edge subset \(\lambda_C\subseteq E(C)\) with
\[
\lambda_C\cdot p_C=1.
\tag{TR1}
\]
Indeed the orthogonal complement of all even-cardinality subsets is the span of the all-one vector, so (TR1) is possible precisely for nonconstant \(p_C\).

Define the **interaction matrix** on these cycles by
\[
M_{C,D}=\lambda_C\cdot(z_D|_{E(C)}).
\tag{TR2}
\]

**Theorem (invertible neutral-repair matrix).** If \(M\) is invertible over \(\mathbb F_2\), then every affine offset yields opposite monochromatic full geodesics. There are at least \(2^{m-|\mathcal C|}\) root-and-order certificates per offset. The conclusion requires neither a cactus condition nor acyclic interaction between the repairs.

*Proof.* Fix any desired syndrome and one orientation \(o_0\) with that syndrome, which exists because \(W\) is onto. For each chordless cycle choose one fully directed orientation \(\gamma_C\). Its reversed directed orientation differs by the all-one vector on that cycle; because \(\lambda_C\) has even cardinality, both have the same \(\lambda_C\) evaluation. Seek a neutral correction \(z=\sum_Du_Dz_D\) with
\[
\lambda_C\cdot(o_0|_{E(C)}+z|_{E(C)})
=1+\lambda_C\cdot\gamma_C
\quad\text{for all }C.
\]
These equations are \(Mu=b\), soluble by the invertibility assumption. Their solution prevents either directed orientation on every chordless cycle. Any directed cycle contains a chordless directed cycle, so the resulting orientation is acyclic and extends to a dimension order realizing the chosen syndrome.

Moreover, the selected functionals are linearly independent on \(Z\): a relation among their rows would give the same relation among rows of \(M\), contradicting invertibility. The full neutral Hall theorem thus supplies \(2^{m-|\mathcal C|}\) root/order certificates. \(\square\)

**Corollary (acyclic repair influence).** Draw a directed edge \(D\to C\) whenever \(z_D\) changes at least one edge of cycle \(C\), for distinct cycles. If this influence digraph is acyclic, then the theorem applies whenever every \(p_C\) is nonconstant.

*Proof.* Choose the even tests \(\lambda_C\) from (TR1) and order cycles topologically in the influence digraph. If \(D\) occurs later than \(C\), then \(z_D\) does not affect \(C\), so \(M_{C,D}=0\). The diagonal entries are one by construction. Thus \(M\) is triangular with diagonal one, hence invertible. \(\square\)

**Research implication.** The earlier local-exchange argument worked by repairing currently directed cycles in dependency order. The matrix theorem shows the deeper reason: each chosen repair supplies one independent linear test on the full neutral code. Even when repair influences form directed cycles, the procedure still succeeds if their binary interaction matrix is nonsingular. A minimal failure of this construction is therefore a *singular exchange matrix*, not automatically a bad cube coloring. This offers a precise target for restoration surgery: replace or combine neutral footprints until their interaction matrix becomes invertible.



## A rank-two family disproves universal one-test-per-cycle Hall closure

The full-neutral independent-test theorem is a sufficient condition, but it **cannot** hold for every favorable affine coloring. There is an infinite family of row-odd affine reader matrices, of rank only two, whose visible graph has more chordless cycles than the dimension of its neutral code. This gives a structural reason to seek global cycle compression rather than one separate linear test for every chordless cycle.

**Theorem (complete bipartite calibration).** Fix odd integers \(a,b\ge3\), partition the \(n=a+b\) dimension set into \(A,B\) of those sizes, and define
\[
L_{ij}=
\begin{cases}
1,&i\in A,\ j\in B\text{ or }i\in B,\ j\in A,\\
0,&\text{otherwise}.
\end{cases}
\]
Then \(L\) is zero-diagonal, has odd row sums, and has rank two. Every affine offset yields a monochromatic-zero full antipodal geodesic and its monochromatic-one reversed-order partner. However the visible exchange graph is \(K_{a,b}\), and
\[
\boxed{
|\mathcal C|=\binom a2\binom b2,\qquad
\dim\ker W=(a-1)(b-1)+1.
}
\tag{KB1}
\]
Consequently \( |\mathcal C|>\dim\ker W\) for all \(a,b\ge3\), so the Hall criterion selecting one independent cycle-safe test per chordless cycle **necessarily fails** throughout this favorable family.

*Proof.* The rows indexed by \(A\) all equal \(\mathbf1_B\) and those indexed by \(B\) all equal \(\mathbf1_A\); they are independent, giving rank two. Row sums are \(b\) and \(a\), both odd. The image of \(L\) is \(K=\operatorname{span}\{\mathbf1_A,\mathbf1_B\}\). For a cross pair \(i\in A,j\in B\), its exchange vector is \(e_i+e_j\), whose quotient by \(K\) is nonzero because each part has at least three vertices. Within either part the exchange vector vanishes. Thus \(G_L=K_{a,b}\).

A chordless cycle in a complete bipartite graph must have length four, and is determined by choosing two vertices in each part, giving \(\binom a2\binom b2\) such cycles. Its edge number is \(ab\), so the general neutral-code dimension formula gives
\(\dim\ker W=ab-(a+b-2)=(a-1)(b-1)+1\). For odd \(a,b\ge3\), direct comparison yields the displayed strict inequality (the smallest case \(a=b=3\) gives nine chordless cycles and neutral-code dimension five).

Favorability follows from the previously proved rank-two Euler-trail theorem. Alternatively, record the two parity states \(p=\sum_{j\in B}x_j\), \(q=\sum_{i\in A}x_i\). Traversing an \(A\)-direction toggles \(q\) and requires \(p=a_i\) for zero color; traversing a \(B\)-direction toggles \(p\) and requires \(q=a_j\). Represent these steps as vertical and horizontal edges of the four-state square, respectively. Both groups have odd cardinality, making the connected transition multigraph have precisely two odd-degree states. An Euler trail gives a zero-colored full dimension order from an appropriate root. Odd row sums make its reversed dimension order one-colored. \(\square\)

**Implication for closure.** The Hall theorem on all chordless cycles may fail for dimensional reasons even when NORI1 holds strongly. A general affine proof must replace many individually protected cycles by a smaller set of *global, jointly acyclic orientation certificates*. The rank-two Euler trail accomplishes this by state connectivity rather than by imposing a separate linear inequality per cycle. The complete-bipartite family is therefore a calibration for any proposed universal orientation-index or cycle-compression theorem.



## Higher-rank Reed--Muller boundary constraint and the local simplex obstruction

The rank-three affine state-walk proof used a parity-zero-chain argument in the eight-state cube. The *moment constraint* extends uniformly to all reader ranks, but the admissible per-dimension edge choices cease to be affine once the reader rank reaches four. This identifies a structural obstruction to extending the rank-three parity-chain argument by linear algebra alone.

Let \(L\) be zero-diagonal and row-odd, of rank \(r\ge3\). Choose \(r\) independent odd rows as a matrix \(U\), write
\[
L_{i,*}=\ell_i^TU,\qquad t_i=Ue_i,
\]
so \(\ell_i\cdot\mathbf1_r=1\), \(\ell_i\cdot t_i=0\), and \(\sum_i t_i=\mathbf1_r\). At a state \(s=Ux\in\mathbb F_2^r\), the direction-\(i\) edge has color \(\ell_i\cdot s+a_i\) and changes state by \(t_i\). For each active label \(t_i\ne0\), its admissible states form the affine hyperplane
\(H_i=\{s:\ell_i\cdot s=a_i\}\); translation by \(t_i\) partitions this hyperplane into \(M_r=2^{r-2}\) disjoint admissible undirected edges.

**Theorem (all-rank affine moment / Reed--Muller obstruction).** Select one admissible state edge for every active dimension. Let \(\beta:\mathbb F_2^r\to\mathbb F_2\) be the indicator of odd-degree vertices of their selected multigraph. Then
\[
\boxed{\sum_s\beta(s)=0,\qquad
\sum_s\beta(s)s=\mathbf1_r.}
\tag{RM1}
\]
For every antipodal state pair \(s,s+\mathbf1_r\), let \(p_s=\delta_s+\delta_{s+\mathbf1_r}\). Then
\[
\boxed{\beta+p_s\in\mathrm{RM}(r-2,r),}
\tag{RM2}
\]
where \(\mathrm{RM}(r-2,r)\) is the evaluation code of Boolean polynomials of degree at most \(r-2\) on \(r\) binary variables.

*Proof.* Each selected edge contributes two endpoints to the degree boundary, so the total boundary parity is zero. Its endpoint-state sum equals its displacement \(t_i\). Summing over active labels gives \(\sum_i t_i=\mathbf1_r\), since passive labels have displacement zero. The antipodal-pair boundary \(p_s\) has the same two moments, because \(s+(s+\mathbf1_r)=\mathbf1_r\). Thus \(\beta+p_s\) is orthogonal to the constant function and all \(r\) linear state functions. These functions span the first-order Reed--Muller code \(\mathrm{RM}(1,r)\); its binary dual is \(\mathrm{RM}(r-2,r)\), proving (RM2). \(\square\)

**Theorem (local choice simplex).** For one active label \(i\), denote by \(e_1,\ldots,e_{M_r}\in\mathbb F_2^{\mathbb F_2^r}\) the boundary indicators of its \(M_r\) admissible state edges. They have disjoint two-vertex supports and are linearly independent. Their attainable boundary set
\[
\boxed{\mathcal E_i=\{e_1,\ldots,e_{M_r}\}}
\tag{RM3}
\]
is an affine set of dimension zero for \(r=2\), an affine line for \(r=3\), but **not an affine subspace for any \(r\ge4\)**. Its affine hull has dimension \(M_r-1\) and contains \(2^{M_r-1}\) vectors, whereas only \(M_r\) are admissible single-edge choices.

*Proof.* The edges in \(H_i\) partition that hyperplane, so their boundary indicators are nonzero with pairwise disjoint supports. Their linear independence follows immediately. Fix \(e_1\); the differences \(e_1+e_j\), \(j\ge2\), are linearly independent, proving the affine-hull dimension \(M_r-1\). If \(M_r\ge4\), the affine hull has at least \(2^{M_r-1}>M_r\) points, so the attainable set is a proper subset and not an affine subspace. For \(M_r=1,2\), all points in its affine hull are attained. \(\square\)

**Corollary (why rank three is special).** For rank three, each active dimension offers two admissible state edges, and changing its choice toggles one four-point affine face. Therefore changes of selections are governed by a binary linear space, as used in the earlier \(\mathrm{RM}(1,3)\) proof. From rank four onward, the linear span of allowed four-point face toggles includes formal sums that would use **multiple edges or zero edges for the same dimension** and thus are not valid dimension-simple walks. A proof based only on solving the Reed--Muller moment constraints (RM1)--(RM2) would not establish the required rainbow one-edge-per-dimension selection.

**Path toward closure.** An all-rank extension requires a *nonlinear selection/restoration lemma*: given a desired antipodal degree boundary in the permitted Reed--Muller coset, choose one eligible edge from each affine-hyperplane family while maintaining connectivity. The affine rank-three proof solved the boundary choice because each family was a two-point affine line; at higher rank one must preserve the local choice simplex rather than replace it by its much larger affine hull. This is precisely the control point where matroidal selection, state-walk connectivity, and the earlier restoration lemmas may combine.
