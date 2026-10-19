# Edge-conditioned turn census and critical-flip forcing

# Edge-conditioned turn census and critical-flip forcing

Let \(n\ge3\) and let \(c\) color the undirected edges of \(Q_n\) by \(0,1\), with \(c_i(x+e_i)=c_i(x)\) and \(c_i(\bar x)=1-c_i(x)\). Let \(\mathcal O_n\) denote the family of coherent projective supports of full antipodal geodesics, so
\[
M=|\mathcal O_n|=2^{n-2}(n-1)!.
\]
For a projective vertex \([v]=\{v,\bar v\}\) and two distinct dimensions \(j,k\), let
\[
t=([v],\{j,k\}),\qquad I_t(c)=[c_j(v)\ne c_k(v)].
\]
This indicator is well defined because both incident colors complement together at \(\bar v\). Write \(T_c(O)=2\sum_{t\in O}I_t(c)\); the possible cyclic energies are \(2,6,10,\ldots\).

For an antipodal edge orbit \(e\) in direction \(i\), choose its unique representative \(\{x,x+e_i\}\) whose endpoint \(x\) has \(i\)-th bit zero. Let
\[
m=(n-1)!,\qquad D=[n]\setminus\{i\}.
\]
The set of supports containing \(e\) has cardinality \(m\).

## The edge-turn factorial incidence theorem

**Theorem 1.** For every projective turn \(t=([y],\{j,k\})\), the number \(N(e,t)\) of coherent supports containing both \(e\) and \(t\) is determined by the following mutually exclusive cases.

1. If \([y]=[x]\) or \([y]=[x+e_i]\), then
\[
N(e,t)=\begin{cases}(n-2)!,&i\in\{j,k\},\\0,&i\notin\{j,k\}.\end{cases}
\tag{1}
\]
2. At any other projective vertex, choose the representative \(y^\sharp\in[y]\) with \(i\)-th bit one, and set
\[
S=\operatorname{supp}(y^\sharp+x+e_i)\subseteq D.
\]
Then \(1\le |S|\le n-2\), and
\[
\boxed{
N(e,t)=
\begin{cases}
(|S|-1)!(n-|S|-2)!,&
j,k\in D,\ |\{j,k\}\cap S|=1,\\
0,&\text{otherwise}.
\end{cases}}
\tag{2}
\]

**Proof.** Each support containing \(e\) has a unique orientation beginning at the projective vertex \([x]\), traversing direction \(i\) first, and then traversing the remaining \(n-1\) dimensions in some permutation. Conversely every permutation of \(D\) yields one support containing \(e\). This proves the count \(m\).

At \([x]\) and \([x+e_i]\), the support turns use direction \(i\) and respectively the last and first dimensions from the permutation of \(D\). Specifying either of these other dimensions leaves \((n-2)!\) possibilities, proving (1).

All other vertices visited by the oriented support are uniquely represented by \(x+e_i+\mathbf1_S\), where \(S\) is a nonempty proper prefix set in the permutation of \(D\). This is the representative with \(i\)-th bit one. The turn at this vertex has as its incident labels the last member \(j\) of the prefix \(S\) and the first member \(k\) of \(D\setminus S\), in either order. Thus a specified turn is possible precisely when one of \(j,k\) belongs to \(S\) and the other to \(D\setminus S\). Ordering the remaining members within these two blocks independently gives \((|S|-1)!(n-|S|-2)!\) supports. \(\square\)

Define the **edge-conditioned turn sum**
\[
\mathcal A_e(c):=\sum_t N(e,t)I_t(c).
\tag{3}
\]
Theorem 1 makes (3) an explicit weighted sum of color comparisons at projective vertices. In expanded form,
\[
\begin{aligned}
\mathcal A_e(c)=&
(n-2)!\sum_{j\in D}
\left(I_{ij}([x])+I_{ij}([x+e_i])\right)\\
&+\sum_{\substack{S\subsetneq D\\ S\ne\varnothing}}
(|S|-1)!(n-|S|-2)!
\sum_{\substack{j\in S\\k\in D\setminus S}}
I_{jk}([x+e_i+\mathbf1_S]).
\end{aligned}
\tag{4}
\]
There is no averaging over alternative colorings in this formula.

**Corollary 2 (anchored first moment).**
\[
\boxed{\sum_{O:e\in O}T_c(O)=2\mathcal A_e(c),\qquad
\mathbb E(T_c\mid e\in O)=\frac{2\mathcal A_e(c)}{(n-1)!}.}
\tag{5}
\]
This follows by interchanging the support sum with its constituent projective turns.

## A sufficient certificate for one-orbit flip stability

Write \(r(v)=|\{i:c_i(v)=1\}|\), and set
\[
\mathcal S(c)=\sum_{[v]}r(v)(n-r(v)).
\]
The unrestricted global turn-star census gives
\[
\sum_{O\in\mathcal O_n}T_c(O)
=2(n-2)!\mathcal S(c).
\tag{6}
\]
Let \(g_{\neg e}(c)\) count the coherent supports containing a monochromatic full geodesic and avoiding the orbit \(e\).

**Theorem 3 (critical-flip exclusion).** Every legal coloring satisfies
\[
\boxed{
g_{\neg e}(c)\ge
\max\left\{0,\
\frac{3\bigl(M-(n-1)!\bigr)-(n-2)!\mathcal S(c)+\mathcal A_e(c)}2
\right\}.}
\tag{7}
\]
In particular, the inequality
\[
\boxed{
(n-2)!\mathcal S(c)-\mathcal A_e(c)
<3\bigl(M-(n-1)!\bigr)
}
\tag{8}
\]
guarantees a monochromatic full antipodal geodesic that avoids \(e\). Such a geodesic survives reversing the colors of the two edges in \(e\). Conversely, at a first good-to-bad antipodal-orbit flip, the good-side coloring necessarily satisfies
\[
\boxed{
(n-2)!\mathcal S(c)-\mathcal A_e(c)
\ge3\bigl(M-(n-1)!\bigr).
}
\tag{9}
\]

**Proof.** There are \(N=M-m\) coherent supports avoiding \(e\). From (5)–(6) their total cyclic turn energy equals
\[
2\bigl((n-2)!\mathcal S(c)-\mathcal A_e(c)\bigr).
\]
A support carrying a monochromatic full geodesic has energy \(2\); every other support has energy at least \(6\). Consequently the energy sum over these \(N\) supports is at least
\[
2g_{\neg e}+6(N-g_{\neg e})=6N-4g_{\neg e}.
\]
Rearranging proves (7). If the right-hand side of (7) is positive, a monochromatic support avoiding \(e\) exists, and changing the two edge colors in \(e\) does not affect it. Hence any good coloring that becomes bad after such a flip must satisfy the reverse inequality (9). \(\square\)

Equivalently put \(\mu=\mathbb E_O T_c(O)\), \(\mu_e=\mathbb E(T_c\mid e\in O)\), and \(\alpha=2^{2-n}\). Then
\[
\boxed{
\mathbb E(T_c\mid e\notin O)
=\frac{\mu-\alpha\mu_e}{1-\alpha},\qquad
g_{\neg e}\ge\frac{M(6-\mu)+m(\mu_e-6)}4,
}
\tag{10}
\]
where the latter lower bound is clipped at zero. Formula (10) shows that edge conditioning can force survival even when \(\mu\ge6\).

## A balanced five-dimensional witness beyond the global first moment

In \(Q_5\), index dimensions by \(0,1,2,3,4\) and let
\[
c_0(x)=x_1,\quad c_1(x)=1+x_0,\quad
c_2(x)=x_0,\quad c_3(x)=1+x_0,\quad c_4(x)=x_0
\qquad(\bmod 2).
\tag{11}
\]
Every edge rule ignores its own dimension, changes under the full antipodal map, and gives vertex color-one degree \(r(x)=2+x_1\). The coloring is maximally balanced, so its global mean is \(\mu=6\), and the unconditioned first-moment bound gives no positive lower bound on the number of two-turn supports.

Take the direction-four antipodal edge orbit represented by the edge with lower endpoint \(x=6\) (binary \(00110\)). Enumerating the \(192\) coherent supports gives the cyclic-energy histograms
\[
\begin{array}{c|rrr}
& T=2&T=6&T=10\\\hline
\text{all supports}&32&128&32\\
\text{supports containing }e&0&18&6\\
\text{supports avoiding }e&32&110&26 .
\end{array}
\tag{12}
\]
Thus \(\mu_e=7\) and
\[
\boxed{\mathbb E(T_c\mid e\notin O)=\frac{41}{7}<6.}
\tag{13}
\]
Theorem 3 alone guarantees at least six two-turn supports avoiding \(e\), while the complete enumeration gives thirty-two. This is a strict gain over the unconditioned mean criterion within one legal coloring. It certifies that this orbit may be flipped without eliminating every monochromatic full geodesic.

## Verification and scope

The incidence formula (1)–(2) was checked by enumerating every coherent support and every edge-orbit/turn pair in dimensions \(3,4,5,6\); the support counts were \(4,24,192,1920\), and the projective-turn counts were \(12,48,160,480\). The anchored moment (5) was also checked on five independent sampled legal colorings per dimension. The five-dimensional histograms (12) were reconstructed independently. Verifier:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/daf5b3ea030d0c2e55d83ce49bc2e59c68c4d8cf/scripts/nori_anchored_turn_census_verify.py.

Theorem 3 imposes a necessary condition on every hypothetical first good-to-bad orbit flip, using the same edge colors for the star census and the anchored turn terms. It is a sufficient one-flip stability criterion, rather than an unrestricted proof that every flip is stable. To close NORI1 through the critical-flip programme, one must exclude (9) jointly with the internal-pivot constraints on monochromatic geodesics in the good-side coloring.

## Relative kernel theorem after deleting one antipodal edge orbit

Let \(A\) be the real support-by-turn incidence matrix: its rows are the coherent supports \(O\in\mathcal O_n\), and its columns the projective turns \(t\), with \(A_{O,t}=\mathbf1_{\{t\in O\}}\). Let \(A_{\neg e}\) retain the rows for supports avoiding a fixed antipodal edge orbit \(e\), in direction \(i\), whose projective endpoints are \(u=[x]\) and \(v=[x+e_i]\). Define \(E_e\) to be the real subspace of turn weightings supported on the \(2(n-1)\) turns at \(u,v\) that involve direction \(i\).

Recall the independently established unrestricted full-incidence kernel theorem from Article VIII: for \(n\ge5\), every \(f\in\ker_{\mathbb R}A\) has
\[
f_{jk}([y])=a_j+a_k+g_j([y])+g_k([y]),
\quad\sum_j a_j=0,\quad g_j([y+e_j])=-g_j([y]).
\tag{14}
\]
In particular, every full-kernel weighting is *pair-additive* at each projective vertex: \(f_{jk}=h_j+h_k\), with \(h_j\) allowed to depend on the vertex.

**Theorem 4 (punctured turn-incidence rigidity).** For every \(n\ge5\) and every projective edge orbit \(e\),
\[
\boxed{\ker_{\mathbb R}A_{\neg e}=\ker_{\mathbb R}A+E_e,}
\qquad
\boxed{\dim_{\mathbb R}(\ker A_{\neg e}/\ker A)=2n-3.}
\tag{15}
\]
Consequently
\[
\boxed{
\operatorname{rank}_{\mathbb R}A_{\neg e}
=2^{n-1}\binom n2-n2^{n-2}-(n-1)-(2n-3).
}
\tag{16}
\]
Every additional kernel freedom caused by deleting the supports through \(e\) can be represented by turn weights at the two endpoints of \(e\), incident with direction \(i\).

**Proof for \(n\ge6\).** Relabel so \(i=0\), write \(D=[n]\setminus\{0\}\), \(m=|D|=n-1\ge5\), and fix the lower-endpoint representative \(x\) of \(e\). Each support containing \(e\) has a unique oriented representative starting at \([x]\), traversing direction \(0\), then traversing the members of \(D\) in a permutation \(\pi=(\pi_1,\ldots,\pi_m)\). For \(f\in\ker A_{\neg e}\), define
\[
H_f(\pi)=\sum_{t\in O(e,\pi)} f_t.
\tag{17}
\]
The assignment \(f\mapsto H_f\) is linear, with kernel \(\ker A\).

**Interior swaps.** Exchanging adjacent entries \(a,b\) in interior positions \(2,\ldots,m-1\) of \(\pi\) leaves \(H_f\) unchanged. To show this, denote their preceding and succeeding labels by \(c,d\), all distinct and in \(D\), and denote the projective vertex just before \(a,b\) by \([z]\). The difference of the two support sums depends only on this local square:
\[
\begin{aligned}
\mathcal D_f(z;c,a,b,d)={}&f_{ca}([z])-f_{cb}([z])\\
&+f_{ab}([z+e_a])-f_{ab}([z+e_b])\\
&+f_{bd}([z+e_a+e_b])-f_{ad}([z+e_a+e_b]).
\end{aligned}
\tag{18}
\]
Choose a spare direction \(q\in D\setminus\{c,a,b,d\}\); one exists because \(m\ge5\). Starting from the common cube root \(y=z+e_0+e_q+e_c\), compare supports whose initial direction blocks are
\[
(0,q,c,a,b,d)\quad\text{and}\quad(q,0,c,a,b,d),
\]
with the same remaining dimensions after \(d\). In either case interchange the adjacent \(a,b\). The vertex just before \(a,b\) is \([z]\), so both exchanges have the same difference (18). The direction-\(0\) edge occurs at \(y\) in the first pair and at \(y+e_q\) in the second; these belong to distinct projective direction-\(0\) edge orbits. Therefore at least one pair avoids the specified \(e\). Its two support sums vanish because \(f\in\ker A_{\neg e}\), so (18) is zero. This proves the interior-swap invariance for every choice of order and root.

The interior permutations are connected by adjacent swaps, hence \(H_f(\pi)\) depends only on the first and last labels of \(\pi\). Write its value as \(H(j,k)\) for \(j\ne k\in D\).

**Boundary swaps.** Fix four distinct \(j,\ell,k,k'\in D\). Choose \(r\in D\setminus\{j,\ell,k,k'\}\), possible since \(m\ge5\). The difference between orders starting \((j,\ell,r)\) and \((\ell,j,r)\) arises from the adjacent exchange \(j,\ell\), preceded by direction \(0\) and followed by \(r\), at the fixed projective location after \(0\). It therefore has the same value regardless of whether the final label is \(k\) or \(k'\). Hence
\[
H(j,k)-H(\ell,k)=H(j,k')-H(\ell,k').
\tag{19}
\]
For each \(j,\ell\) the left-hand difference is thus independent of the third label \(k\notin\{j,\ell\}\). Write the common difference as \(\delta_{j\ell}\). Choosing a label outside any three prescribed distinct labels shows
\(\delta_{j\ell}+\delta_{\ell h}=\delta_{jh}\), so \(\delta_{j\ell}=a_j-a_\ell\) for some numbers \(a_j\). It follows that
\[
\boxed{H(j,k)=a_j+b_k\quad(j\ne k)}
\tag{20}
\]
for certain vectors \(a,b\in\mathbb R^D\).

The space of functions (20) on ordered distinct pairs has dimension \(2m-1\): the only redundancy for \(m\ge3\) is simultaneous replacement \(a_j\mapsto a_j+t\), \(b_k\mapsto b_k-t\). Thus the image of \(f\mapsto H_f\), and hence \(\ker A_{\neg e}/\ker A\), has dimension at most \(2m-1=2n-3\).

Conversely assign arbitrary weights \(a_j\) to turns \(([x+e_0],\{0,j\})\), and weights \(b_k\) to turns \(([x],\{0,k\})\), and zero elsewhere. This weighting belongs to \(E_e\subseteq\ker A_{\neg e}\), and its support sum on \(O(e,\pi)\) is \(a_{\pi_1}+b_{\pi_m}\). These span all functions (20), of dimension \(2m-1\). The upper bound is attained, and subtracting such an endpoint weighting from any \(f\in\ker A_{\neg e}\) leaves a weighting in \(\ker A\). This proves (15), and (16) follows from the full rank theorem. \(\square\)

**Finite boundary \(n=5\).** Here the spare-label argument requires an additional check. The same endpoint subspace furnishes a seven-dimensional quotient of the punctured kernel, so the real rank of \(A_{\neg e}\) is at most \(116-7=109\). An independent characteristic-two Gaussian elimination on the complete \(168\times160\) punctured support-turn incidence matrix yields rank \(109\) over \(\mathbb F_2\). The real rank is at least the binary rank for an integer matrix, so the real rank is \(109\), completing (15) also for \(n=5\). Cube automorphisms carry every orbit into any other, so it suffices to check one. The same reproducible elimination gives ranks
\[
\begin{array}{c|rrrr}
n&4&5&6&7\\\hline
\operatorname{rank}_{\mathbb F_2}A&23&116&379&1114\\
\operatorname{rank}_{\mathbb F_2}A_{\neg e}&18&109&370&1103
\end{array}
\tag{21}
\]
(the uniform theorem is asserted for \(n\ge5\)). Verifier:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/b0e25c09bf20e2b738b9b89251f0fd6498c22587/scripts/nori_punctured_turn_rank_verify.py.

## Relative constant-energy rigidity and the improved flip criterion

**Theorem 5 (relative turn-energy rigidity).** For every \(n\ge5\), every legal coloring \(c\), and every projective edge orbit \(e\),
\[
\boxed{T_c(O)\text{ constant over all supports }O\text{ avoiding }e
\quad\Longrightarrow\quad T_c(O)=2\text{ for all those supports}.}
\tag{22}
\]

**Proof.** Suppose the common energy is \(\tau\). Put
\[
f_t=I_t(c)-\frac{\tau}{2n}.
\]
Each support has \(n\) projective turns, so \(f\in\ker A_{\neg e}\). By Theorem 4, write \(f=f^{(0)}+h\), with \(f^{(0)}\in\ker A\) and \(h\in E_e\). At every projective vertex other than the two endpoints of \(e\), the turn indicators \(I_{jk}([y])\) therefore satisfy the pair-additive four-direction relation
\[
I_{ab}+I_{cd}-I_{ac}-I_{bd}=0
\quad(a,b,c,d\text{ distinct}).
\tag{23}
\]
If at such a vertex at least two incident edges have each color, choose \(a,b\) of the first color and \(c,d\) of the second. Equation (23) becomes \(0+0-1-1=0\), a contradiction. Thus at every projective vertex except possibly the two endpoints of \(e\),
\[
r(y)\in\{0,1,n-1,n\},\qquad r(y)(n-r(y))\le n-1.
\]
At the two exceptional vertices the universal bound is \(r(y)(n-r(y))\le\lfloor n^2/4\rfloor\). Consequently the global turn-star census gives
\[
\begin{aligned}
\mu_{\rm all}
&=\frac4{2^{n-1}(n-1)}\sum_{[y]}r(y)(n-r(y))\\
&\le4+\frac{8\bigl(\lfloor n^2/4\rfloor-(n-1)\bigr)}
{2^{n-1}(n-1)}
<5 \qquad(n\ge5).
\end{aligned}
\tag{24}
\]
Yet the supports avoiding \(e\) form a proportion \(1-\alpha\), with \(\alpha=2^{2-n}\). If \(\tau\ge6\), every avoided support has energy at least \(6\), while every support through \(e\) has energy at least \(2\). It follows that
\[
\mu_{\rm all}\ge6(1-\alpha)+2\alpha
=6-4\alpha\ge\tfrac{11}{2}
\quad(n\ge5),
\]
contradicting (24). Since all cyclic energies belong to \(2+4\mathbb Z_{\ge0}\), necessarily \(\tau=2\). \(\square\)

**Corollary 6 (non-strict anchored forcing, \(n\ge5\)).**
\[
\boxed{\mathbb E(T_c\mid e\notin O)\le6
\quad\Longrightarrow\quad
\exists O\not\ni e:\ T_c(O)=2.}
\tag{25}
\]
Equivalently,
\[
\boxed{
(n-2)!\mathcal S(c)-\mathcal A_e(c)
\le3\bigl(M-(n-1)!\bigr)
\quad\Longrightarrow\quad
\text{a monochromatic full geodesic survives flipping }e.}
\tag{26}
\]
**Proof.** If all avoided supports had energy at least \(6\), their mean at most \(6\) would force all their energies to equal \(6\). Theorem 5 excludes this. Therefore one has energy \(2\) and remains unchanged when the orbit \(e\) is flipped. \(\square\)

This improves the strict first-moment edge-flip certificate (8) to a closed inequality, using the original coloring throughout. For a hypothetical first good-to-bad orbit flip, the necessary inequality from (9) sharpens to the strict form
\[
\boxed{(n-2)!\mathcal S(c)-\mathcal A_e(c)>3\bigl(M-(n-1)!\bigr)\qquad(n\ge5).}
\tag{27}
\]
The implication gives an edge-conditioned forcing theorem in arbitrary dimension. The full unrestricted NORI1 conjecture remains open.


## Quantitative facet bridge: paired-root multiplicity determines bridge diversity

This result joins the critical edge-orbit programme with Article XV's arbitrary-facet paired-root framework. It counts good supports through each direction orbit, not just the existence of some witness.

Put \(d=n-1\), designate dimension \(i\), and identify its upper facet with \(Q_d\). Every legal antipodally odd coloring of \(Q_n\) consists of an arbitrary edge coloring \(f\) of that facet, together with the colors \(g(z)\) of the direction-\(i\) edges, indexed by \(z\in Q_d\), satisfying \(g(\bar z)=1-g(z)\). The colors on the lower facet are then forced by global antipodal oddness. Conversely any such \(f,g\) determine a legal coloring.

For a root \(z\in Q_d\), let \(N_f^+(z)\) count the \(d!\) full direction orders that yield a rooted geodesic with color word \(0^p1^{d-p}\), \(0\le p\le d\). Define \(N_f^-(z)\) analogously for \(1^p0^{d-p}\). Reversing a path proves
\[
\boxed{N_f^-(z)=N_f^+(\bar z).}
\tag{28}
\]
Let \(e_{[z]}\) be the antipodal pair of dimension-\(i\) edges over \(z,\bar z\). Let \(G_{[z]}(c)\) count monochromatic coherent supports through that edge orbit.

**Theorem 7 (quantitative facet bridge).** For every such \(f,g\) and a chosen representative \(z\) of the projective pair \([z]\),
\[
\boxed{
G_{[z]}(c)=
\begin{cases}
N_f^+(z),&g(z)=0,\\
N_f^+(\bar z),&g(z)=1.
\end{cases}}
\tag{29}
\]
Consequently, with \(\mathcal G(c)=\{O\in\mathcal O_n:T_c(O)=2\}\),
\[
\boxed{
\min_{\substack{g:Q_d\to\mathbb F_2\\g(\bar z)=1-g(z)}}
|\mathcal G(c(f,g))|
=
\sum_{\{z,\bar z\}}\min\{N_f^+(z),N_f^+(\bar z)\}.
}
\tag{30}
\]
Furthermore, defining \(P(f)=\{z:N_f^+(z)>0,\ N_f^+(\bar z)>0\}\),
\[
\boxed{
\min_g\#\{e\text{ of dimension }i:\exists O\in\mathcal G(c(f,g)),\ e\in O\}
=\frac{|P(f)|}{2}.
}
\tag{31}
\]
Every orbit corresponding to a pair in \(P(f)\) appears in some good support for **every** allowed \(g\); all other dimension-\(i\) orbits can be suppressed simultaneously by a suitable \(g\).

**Proof.** Each support through \(e_{[z]}\) has one oriented representative that begins in the lower facet over \(z\), traverses \(i\) into the upper facet, and then traverses the remaining \(d\) dimensions in an arbitrary permutation \(\pi\). This gives a bijection between such supports and \(S_d\). If \(w_f(z,\pi)\) is the color word along the resulting upper-facet geodesic, the cyclic projective change count is the number of changes in the extended word
\[
(g(z),\,w_f(z,\pi),\,1-g(z)).
\]
The endpoints differ, so this number equals one precisely when \(w_f(z,\pi)\) is nondecreasing if \(g(z)=0\), or nonincreasing if \(g(z)=1\). This proves (29). Every coherent support has one direction-\(i\) orbit. Sum (29) over representatives of \(\{z,\bar z\}\), noting that the bits \(g(z)\) can be selected independently on these antipodal pairs. Minimizing each term gives (30). Such a term is positive for both choices of \(g(z)\) precisely when \(z,\bar z\in P(f)\). Otherwise its contribution can be set to zero. Hence (31). \(\square\)

**Corollary 8 (root multiplicity criterion for prescribed-orbit avoidance).** The following are equivalent for each \(n\ge3\):

(a) Every legal \(Q_n\) coloring admits, for every prescribed antipodal edge orbit \(e\), a monochromatic coherent support avoiding \(e\).

(b) Every arbitrary coloring \(f\) of \(Q_{n-1}\) has
\[
\boxed{|P(f)|\ge4.}
\tag{32}
\]

**Proof.** Under (b), (31) gives at least two distinct direction-\(i\) orbits used by good supports for every \(i\), so there is always one different from any prescribed \(e\). Conversely, if some \(f\) has no paired roots or only one antipodal root pair, translate its facet roots if necessary so that its sole pair labels the prescribed edge orbit. Choose \(g\) to suppress every other direction-\(i\) orbit, using (31). Every full geodesic uses direction \(i\) once; thus all good supports, if any, use the prescribed orbit, contradicting (a). \(\square\)

This is a rigorous characterization of the strengthened orbit-avoidance target and explains the finite observations. An arbitrary colored square can have \(|P(f)|=2\), so the strengthening fails in \(Q_3\). All arbitrary three-cube colorings have at least four paired roots, as established by the known cross-orientation intersection theorem, giving the \(Q_4\) case. The reported infeasibility calculation for orbit avoidance in \(Q_5\) is equivalently a computation-backed lower bound \(|P(f)|\ge4\) for arbitrary four-cube colorings. The Cartesian product of two extremal colored squares has four paired roots, showing the bound is sharp in dimension four. The universal bound \(|P(f)|\ge4\) in higher dimensions is not established.

**Corollary 9 (persistent support criterion).** A good coherent support through \(e_{[z]}\) remains good after flipping \(e_{[z]}\) if and only if its associated upper-facet full geodesic rooted at \(z\) is monochromatic. In particular, if \(f\) has a rooted monochromatic full geodesic at \(z\), the corresponding support persists regardless of \(g(z)\).

**Proof.** Flipping the orbit changes \(g(z)\) to \(1-g(z)\), keeping \(w_f(z,\pi)\) unchanged. To yield just one change with both endpoint color choices, this facet word must be simultaneously nondecreasing and nonincreasing, hence constant. \(\square\)

The quantitative bridge and per-orbit support counts were checked against full coherent-support enumeration for multiple independent legal colorings in dimensions \(3,4,5\). Certificate:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/88fc6f19b9974bb4409c0b348bf289b1dd686af3/scripts/nori_quantitative_facet_bridge_verify.py.

**Closure obligation.** Instead of another turn-energy estimate, the direct forcing target is now a sharp **paired-root multiplicity theorem for an arbitrary facet coloring**. The already-known root-existence theorem must be strengthened from one antipodal pair to two, without assuming independent factorization. This produces distinct edge-orbit witnesses in every direction and would make critical flips incapable of destroying all monochromatic geodesics.


## Affine bad-extension fibres and critical-flip boundary

Fix an arbitrary coloring \(f\) on \(Q_d\), put \(n=d+1\), and let \(\mathcal R\) contain one representative from each complementary pair of facet vertices. There are \(h=2^{d-1}\) such pairs. Set \(u_z=N_f^+(z)\), \(v_z=N_f^+(\bar z)\), and write \(b_z\) for the freely chosen new-direction edge color over \(z\). Theorem 7 gives
\[
\boxed{G_f(b)=\sum_{z\in\mathcal R}[u_z+(v_z-u_z)b_z].}\tag{34}
\]
Here \(G_f(b)\) is the number of good coherent supports, and the bridge bits \(b_z\) are independent.

Partition the root pairs into \(\mathcal D=\{z:u_zv_z>0\}\), \(\mathcal S=\{z:(u_z>0)\oplus(v_z>0)\}\), and \(\mathcal Z=\{z:u_z=v_z=0\}\).

**Theorem 10 (Boolean-face classification).** The set \(\mathcal B_f=\{b:G_f(b)=0\}\) is either empty or an axis-aligned subcube. It is empty if \(P(f)\ne\varnothing\). When \(P(f)=\varnothing\), its bits at \(\mathcal S\) are forced to select the unfavorable orientation, while its bits at \(\mathcal Z\) are free. Consequently
\[
\boxed{|\mathcal B_f|=\begin{cases}0,&P(f)\ne\varnothing,\\2^{2^{d-1}-|A(f)|},&P(f)=\varnothing.\end{cases}}\tag{35}
\]
If nonempty, the bad face has codimension \(|A(f)|\).

**Proof.** Every summand in (34) is nonnegative. Their sum vanishes precisely when all vanish. A pair with \(u_z,v_z>0\) cannot vanish. A singly favorable pair forces one bridge bit, whereas an entirely unfavorable pair imposes no restriction. In the absence of doubly favorable pairs, \(|\mathcal S|=|A(f)|\), which proves (35). \(\square\)

**Theorem 11 (first-flip boundary).** At any bad extension \(b\), flipping a bridge orbit indexed by \(z\) creates good supports if and only if \(z\in\mathcal S\). All resulting good supports use the flipped orbit, and their number is \(\max(u_z,v_z)\). Thus each bad extension has precisely \(|A(f)|\) good neighbors by flips of the newly designated direction. Conversely a good extension becomes bad upon flipping orbit \(z\) precisely when \(P(f)=\varnothing\), \(z\in\mathcal S\), that orbit selects its favorable orientation, and every other singly favorable orbit selects its unfavorable orientation.

**Proof.** Each bridge orbit contributes just one summand to (34). Flipping it changes no other summand. At a bad extension all summands vanish, so the only possible newly positive term is the flipped one. Its alternative value is \(\max(u_z,v_z)\) for \(z\in\mathcal S\), and zero for \(z\in\mathcal Z\). This proves both directions. \(\square\)

**Theorem 12 (fibre distribution).** For uniformly random legal bridge assignments,
\[
\boxed{\mathbb E_b s^{G_f(b)}=\prod_{z\in\mathcal R}\frac{s^{u_z}+s^{v_z}}2,}\tag{36}
\]
and therefore
\[
\boxed{\mathbb E_bG_f=\tfrac12\sum_{z\in Q_d}N_f^+(z),\quad
\operatorname{Var}_b(G_f)=\tfrac14\sum_{z\in\mathcal R}(u_z-v_z)^2.}\tag{37}
\]
**Proof.** The terms in (34) are independent two-valued random variables; multiply their generating functions and take derivatives. \(\square\)

These formulas hold for an arbitrary fixed facet coloring, not a special class. The required cross-direction closure is not supplied: the possibility of one nonempty bad face remains equivalent to the paired-root existence obstruction in the lower dimension.

**Certificate.** Full enumeration of all 4096 arbitrary facet colorings of \(Q_3\) and all sixteen bridge assignments (65,536 legal \(Q_4\) colorings) verifies (34)–(35) and the support counts independently:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/1145feadeec3041dc85290b869684e5b6edb2c60/scripts/nori_bad_extension_subcube_verify.py.


## Two-direction implication transport and alternating forcing packets

Fix distinct directions \(i,j\) in \(Q_n\), \(n\ge3\), and fix all antipodally odd edge-orbit colors outside those two direction classes. The remaining \(v=2^{n-1}\) antipodal edge-orbit colors are free Boolean variables \(X_e\), each belonging to direction \(i\) or \(j\). On a specified edge in orbit \(e\), the edge color is \(X_e\oplus s_e\), where the sign \(s_e\) is zero on the selected orbit representative and one on its antipodal mate.

For any rooted full direction-distinct geodesic \(P\), consider its \(n-2\) edges in the already colored directions. If two of these have different colors, no extension makes \(P\) monochromatic. Otherwise let \(t\) be their common color, and denote the remaining two edge orbits by \(e_i,e_j\), with signs \(s_i,s_j\).

**Theorem 13 (unrestricted two-direction 2-SAT theorem).** Form the clause
\[
\boxed{(X_{e_i}\ne t\oplus s_i)\ \lor\ (X_{e_j}\ne t\oplus s_j)}
\tag{38}
\]
for every rooted full geodesic \(P\) whose other \(n-2\) edge colors agree. Let \(\Phi_{ij}\) be the conjunction of these clauses. Then
\[
\boxed{X\models\Phi_{ij}\quad\Longleftrightarrow\quad
\text{the completed legal coloring has no monochromatic full geodesic}.}
\tag{39}
\]
Each clause uses one variable from each of the two direction classes. Thus the bad-extension region for any shared fixed partial coloring is the solution set of a bipartite 2-CNF formula.

**Proof.** The path \(P\) is monochromatic in the completed coloring precisely when the two free edge colors both equal \(t\), meaning \(X_{e_i}=t\oplus s_i\) and \(X_{e_j}=t\oplus s_j\). Clause (38) forbids precisely this simultaneous assignment. A completion is bad precisely when every rooted full geodesic is nonmonochromatic, which is the conjunction (39). The two free edges belong to different direction classes, so their variables are distinct and the formula is bipartite. Every omitted antipodal image path yields the same clause because all its edge colors complement simultaneously. \(\square\)

**Theorem 14 (two-direction Boolean-majority closure).** For a fixed coloring outside directions \(i,j\), let \(\mathcal B_{ij}\) be its family of bad completions. For any \(X,Y,Z\in\mathcal B_{ij}\), their componentwise majority also belongs to \(\mathcal B_{ij}\):
\[
\boxed{\operatorname{maj}(X,Y,Z)\in\mathcal B_{ij}.}
\tag{40}
\]
This is a compatibility law involving both free direction classes in one original partial coloring. It extends the single-direction affine-face property from Theorem 10.

**Proof.** Consider any binary clause \(L\lor M\) satisfied by three assignments. If their componentwise majority made both clauses' terms false, each of the two terms would be false in at least two of the three assignments. These two groups of cardinality at least two must intersect, producing one assignment that makes both terms false. This contradicts its assumed satisfaction. Every clause, and hence their conjunction, is therefore preserved by majority. \(\square\)

### Contradictory alternating geodesic packets

A clause forbidding \(X_a=p,X_b=q\) yields the two contrapositive implications
\[
(X_a=p)\Rightarrow(X_b=1-q),
\qquad
(X_b=q)\Rightarrow(X_a=1-p).
\tag{41}
\]
The implication graph has \(2v\) signed states \((e,0),(e,1)\). Every arc moves between the two direction classes, and an arc \(u\to w\) is accompanied by the reversed complemented arc \(\bar w\to\bar u\). Each arc is certified by a rooted full geodesic whose already colored \(n-2\) edges all have one color.

**Theorem 15 (alternating implication-cycle forcing).** For any fixed partial coloring outside directions \(i,j\), the following are equivalent:

(a) Every legal completion in the two free direction classes has a monochromatic full geodesic.

(b) A strongly connected component of the bipartite implication graph contains both signed states \((e,0),(e,1)\) of one edge orbit.

(c) There are two directed alternating implication paths, one from \((e,0)\) to \((e,1)\) and another in the reverse direction.

When these hold, a packet of at most
\[
\boxed{4v-4=2^{n+1}-4}
\tag{42}
\]
rooted full geodesics suffices to force a monochromatic full geodesic **for every assignment of the two free direction classes**. Given any completed coloring, a violated clause identifies one such monochromatic geodesic.

**Proof.** Theorem 13 identifies bad completions with satisfying assignments of a binary CNF. The standard implication-graph criterion says this CNF is inconsistent precisely when one strongly connected component contains both signed states of a variable. This is equivalent to having paths in both directions, proving (a)--(c). Choose simple paths in each direction. Each begins and ends on the same side of the bipartite implication graph, so its arc count is even and no more than \(2v-2\). Their union contains no more than \(4v-4\) arcs, each contributed by a clause and therefore by a rooted full geodesic. This smaller clause set already contradicts both possible values of \(X_e\), so in every assignment some included clause fails. Its associated full geodesic has all the prescribed edges in one color and both free edges matching it, hence is monochromatic. \(\square\)

This is a dimension-uniform constructive forcing mechanism **conditional on an alternating implication-cycle certificate** in the shared partial coloring. The unresolved unrestricted challenge is to establish such certificates for every assignment of the other \(n-2\) direction classes. A satisfiable instance would produce a legal NORI1 counterexample by assigning its remaining two classes accordingly.

**Finite verification.** For \(n=4\), exhaustive computation over the \(256\) possible partial colorings outside two chosen free directions confirms that every resulting 2-CNF is inconsistent. The equivalence between its clauses and full monochromatic geodesics was checked independently for all \(65,536\) legal \(Q_4\) colorings. Greedily reduced inconsistent clause packets have sizes from four to eleven in an independently verified elimination run. Samples in \(Q_5\) and \(Q_6\) also yielded contradictory packets, but cannot establish an all-dimensional existence theorem. Reproducible verifier:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/ce8c86fcfe8ea07cec1d591457bd170c00fae7f5/scripts/nori_two_direction_implication_verify.py.

**Next closure target.** Prove that the near-monochromatic complete paths associated with an arbitrary shared partial coloring necessarily create two opposing alternating implication paths between the states of at least one free edge orbit. That would force a full monochromatic geodesic in every completion, with a certificate using exponentially rather than factorially many complete paths.


## An all-dimensional four-path forcing packet with two free directions

The alternating implication theorem has a particularly short constructive instance that persists under arbitrarily many extra directions. It proves an explicit robust completion theorem, rather than claiming that every partial coloring has such a small packet.

Index the dimensions by \(0,1,\ldots,n-1\), \(n\ge4\). Put \(K=(4,5,\ldots,n-1)\), in this order, and \(M_K=\sum_{k\in K}2^k\). For a cube vertex \(x\), let \(\xi=x\bmod16\) encode its first four bits. Define the colors of all edges in directions other than \(0,1\) by
\[
\boxed{
c_2(x)=x_3,\qquad
c_3(x)=x_2,\qquad
c_k(x)=x_0\oplus\mathbf1_{\{\xi\in\{3,12\}\}}
\quad(k\ge4).
}
\tag{43}
\]
Here \(x_t\) denotes the bit of \(x\) in dimension \(t\). Each rule is independent of its own direction bit. The set \(\{3,12\}\) is invariant under complementing the first four bits, so all these rules reverse color under full antipodality. Assign the colors of every direction-\(0\) and direction-\(1\) edge orbit arbitrarily, subject only to legal antipodal oddness.

For a starting vertex \(r\) and an order \(\pi\), denote the rooted full geodesic by \(P(r;\pi)\). Consider the four paths in the following table, where writing \(K\) means inserting every member of \(K\) in its displayed order.

| Label | Root | Direction order | Color of all edges in directions \(2,\ldots,n-1\) |
|---|---|---|---|
| \(P_{00}\) | \(4+M_K\) | \(K,1,0,2,3\) | \(0\) |
| \(P_{11}\) | \(4\) | \(1,0,K,3,2\) | \(1\) |
| \(P_{01}\) | \(6\) | \(0,2,K,3,1\) | \(0\) |
| \(P_{10}\) | \(6\) | \(0,3,K,2,1\) | \(1\) |

**Theorem 16 (uniform four-geodesic forcing packet).** The four paths above always include a monochromatic full antipodal geodesic, regardless of how the remaining two entire direction classes are legally colored. More precisely, let \(a\) be the color of the direction-\(0\) edge orbit through lower endpoint \(6\), with every added bit zero, and let \(b\) be the color of the direction-\(1\) edge orbit through lower endpoint \(4\), with every added bit zero. Then
\[
\boxed{\text{the path }P_{ab}\text{ is monochromatic}.}
\tag{44}
\]
In particular this packet uses just four predetermined full geodesics for every \(n\ge4\).

**Proof.** The table's fixed-direction entries follow directly from (43). At directions \(2,3\), the respective edge colors of the four paths are \(00,11,00,11\). For each added direction \(k\in K\), the path traverses \(k\) while the first four vertex bits equal respectively \(4,7,3,15\). Formula (43) takes respectively the values \(0,1,0,1\) at these four states, giving the displayed uniform fixed-edge colors.

At every direction-\(0\) step, the current vertex lies in the orbit whose lower endpoint has first-four-bit mask \(6\) and all added bits zero, so its edge color is \(a\). At the direction-\(1\) step, \(P_{00}\) and \(P_{11}\) use the edge with lower endpoint mask \(4\) and all added bits zero, of color \(b\); \(P_{01}\) and \(P_{10}\) use its full antipodal mate, of color \(1-b\). Thus the four paths' two free-edge colors are respectively
\[
(a,b),\qquad(a,b),\qquad(a,1-b),\qquad(a,1-b).
\]
Together with the fixed colors in the table, this shows:
\[
P_{00}\text{ is monochromatic if }(a,b)=(0,0),\quad
P_{11}\text{ if }(a,b)=(1,1),
\]
\[
P_{01}\text{ if }(a,b)=(0,1),\quad
P_{10}\text{ if }(a,b)=(1,0).
\]
These are the four possible assignments, proving (44). \(\square\)

**Robustness.** The proof only uses the colors of the fixed-direction edges lying on these four full paths. There are at most \(4(n-2)\) such antipodal orbit constraints, out of \((n-2)2^{n-2}\) orbit variables in the fixed directions. Therefore at least
\[
\boxed{(n-2)(2^{n-2}-4)}
\tag{45}
\]
other fixed-direction orbit colors may be changed independently without losing the forcing packet, in addition to the entirely free direction-\(0\) and direction-\(1\) orbit colors. This creates a large cylinder of original legal colorings carrying the same short forcing certificate.

The packet is an illustration of a dimension-uniform **positive witness mechanism** arising from two-direction square and antipodal transport. It does not assert that four-clause packets exist in every partial coloring; indeed some four-cube partial colorings need longer implication certificates. In general, Theorem 15's alternating forcing packet, rather than this special four-path packet, remains the closure target.

**Independent certificate:** The stated four paths, their fixed colors, shared free orbit identities, antipodal signs and selection rule (44) were checked by direct integer-bit path traversal for \(4\le n\le10\):
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/4209fc1a341bd6a203fa67634aed713145bfb4c1/scripts/nori_four_path_packet_verify.py.


## Complete geometry of two prescribed edge orbits

The two-direction implication formulation has no geometric absences between edge-orbit variables. Indeed their incidence can be counted by a factorial formula.

Let \(e_i\) and \(e_j\) be antipodal edge orbits in different dimensions \(i\ne j\). Choose the representative \(\{x,x+e_i\}\) of \(e_i\) with \(x_i=0\). Choose the representative \(\{y,y+e_j\}\) of \(e_j\) whose two endpoints have \(i\)-th bit equal to one. Let
\[
S=\{k\notin\{i,j\}:x_k\ne y_k\},\qquad s=|S|.
\]

**Theorem 17 (two-edge factorial incidence).** The number of coherent projective full-geodesic supports containing both prescribed antipodal edge orbits is
\[
\boxed{N(e_i,e_j)=s!(n-2-s)!.}
\tag{46}
\]
Consequently every prescribed pair of different-direction edge orbits belongs to at least one common coherent full geodesic. Moreover, for a support chosen uniformly subject to containing \(e_i\),
\[
\boxed{
\Pr(e_j\in O\mid e_i\in O)=
\frac{1}{(n-1)\binom{n-2}s}.
}
\tag{47}
\]

**Proof.** Every support through \(e_i\) has a unique oriented representation beginning with \(x\to x+e_i\), followed by a permutation of the other \(n-1\) dimensions. In such a representation, the \(i\)-bit is one at the step in dimension \(j\). That step lies in \(e_j\) precisely when the set of dimensions used after \(i\) but before \(j\) is \(S\). Its elements may be ordered in \(s!\) ways; the dimensions remaining after \(j\) may be ordered in \((n-2-s)!\) ways. Every such ordering yields one support, proving (46). Since there are \((n-1)!\) supports through \(e_i\), division gives (47). \(\square\)

Thus any absent implication between two free edge-orbit variables is forced by the **mixed colors of already fixed edges** along all their connecting full geodesics, not by lack of a dimension-distinct path. This distinguishes combinatorial geometry from the still-open color-compatibility step. Exhaustive anchored-support checks of (46) were carried out through \(Q_8\).

## Paired-bridge forks: a four-geodesic forcing lemma

Recall the two-direction setup: edge-orbit bits in directions \(i,j\) are free while all other edge colors are fixed. Let \(X_e\) encode one chosen direction-\(i\) edge orbit \(e\).

Call a pair of rooted full geodesics a *color-\(t\) fork at \(e\)* if: (a) every edge outside \(i,j\) on each path has fixed color \(t\); (b) both paths traverse the same selected member of orbit \(e\) in direction \(i\), whose color is \(X_e\); and (c) their direction-\(j\) edges are antipodal mates of one common direction-\(j\) edge orbit. Condition (c) means that the two \(j\)-edge colors are complementary under every legal assignment.

**Theorem 18 (opposite-color fork forcing).** If the same direction-\(i\) orbit \(e\) admits both a color-zero fork and a color-one fork, then every legal completion of the two free direction classes has a monochromatic full antipodal geodesic among the four fork paths.

**Proof.** If \(X_e=0\), inspect the color-zero fork. Its fixed-direction edges and both chosen direction-\(i\) edges have color zero. Its two direction-\(j\) edges are antipodal mates, and therefore one has color zero. The corresponding rooted full path is monochromatic. If \(X_e=1\), the identical argument applies to the color-one fork. \(\square\)

This is a certificate criterion inside an arbitrary fixed partial coloring. It does not assert that every partial coloring admits a pair of forks.

## A uniform cross-square packet with just three free orbit variables

The fork criterion has a particularly simple realization in every \(n\ge4\). Index directions \(0,1,\dots,n-1\), put \(K=(3,4,\ldots,n-1)\), and fix
\[
\boxed{c_2(x)=1+x_0,\qquad c_k(x)=x_0\ \ (k\ge3)}
\quad\text{over }\mathbb F_2.
\tag{48}
\]
These fixed-direction edge colors satisfy undirectedness and antipodal oddness. Every edge orbit in directions \(0,1\) may be colored freely subject to antipodal oddness.

Let \(A\) denote the color of the direction-zero orbit with lower endpoint \(0\). Let \(B,C\) denote the colors of the two direction-one orbits with lower endpoints \(4\) and \(5\), respectively. These three orbit bits are independent.

| Root | Full direction order | Fixed-edge color | Free-edge colors |
|---|---|---|---|
| \(7\) | \((1,2,0,K)\) | \(0\) | \(A,C\) |
| \(5\) | \((2,0,K,1)\) | \(0\) | \(A,1-C\) |
| \(4\) | \((2,0,K,1)\) | \(1\) | \(A,1-B\) |
| \(6\) | \((1,2,0,K)\) | \(1\) | \(A,B\) |

**Theorem 19 (dimension-uniform cross-square four-path packet).** For every \(n\ge4\) and every legal assignment of the entire two free direction classes, at least one of these four rooted full geodesics is monochromatic.

**Proof.** The entries in the table follow from (48) by tracing the vertices along each direction order. The direction-zero edges all represent the same edge orbit \(A\). The first two paths' direction-one edges represent antipodal mates of orbit \(C\), and the last two paths' direction-one edges represent antipodal mates of orbit \(B\). If \(A=0\), either \(C=0\) or \(1-C=0\), so one of the first two paths is monochromatic zero. If \(A=1\), either \(B=1\) or \(1-B=1\), so one of the last two paths is monochromatic one. \(\square\)

The three distinguished free orbits lie in two different projective squares of the \((0,1)\)-direction square system: the direction-zero orbit lies above the class of the all-zero remaining-direction state, whereas \(B,C\) lie above the class with direction \(2\) toggled. This is a **cross-square** forcing certificate; it cannot be confined to a single projective square.

The union of these four paths uses only \(2(n-2)\) antipodal edge orbits among the \((n-2)2^{n-2}\) already colored orbits. The other
\[
\boxed{(n-2)(2^{n-2}-2)}
\tag{49}
\]
fixed-direction orbit colors may be changed arbitrarily, and the same forcing conclusion holds. This proves a robust all-dimensional forcing cylinder with no conditions on the rest of the coloring.

A separate direct traversal audit checked (48), all four path orders, all eight assignments of \(A,B,C\), and the orbit count through dimension twelve. Reproducible certificate:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/ae7850fe1c8a28edf4d960c0ee31bcc5de49ef46/scripts/nori_two_square_fork_packet_verify.py.

## Universal two-square forcing in five dimensions: finite certificate

Fix free directions \(0,1\) in \(Q_5\); their \(16\) edge-orbit variables split into four disjoint projective-square blocks of four variables each. For an arbitrary legal coloring of the other three direction classes, restrict the bipartite 2-CNF \(\Phi_{0,1}\) of Theorem 13 to clauses whose two free variables lie in the union of a prescribed pair of square blocks.

**Computational Proposition 20.** Every coloring of the other three direction classes in \(Q_5\) has at least one pair of projective-square blocks whose restricted 2-CNF is inconsistent.

**Verification method.** To seek a counterexample, choose the \(24\) remaining fixed edge-orbit bits and, independently for each of the six pairs of projective squares, choose the eight free orbit bits in that pair's union. This gives \(24+6\cdot8=72\) binary variables. Require every rooted full geodesic whose two free orbits belong to one chosen block pair to be nonmonochromatic under that pair's independent assignment. For each such geodesic with colored edge bits \(d_1,\ldots,d_5\), impose the linear inequality \(1\le d_1+\cdots+d_5\le4\), with all edge colors affine in the relevant independent orbit bits. There are 3840 linear path constraints before row duplication reductions.

The resulting feasibility model is logically equivalent to the existence of a fixed three-direction coloring for which **all six** two-square induced 2-CNF instances are satisfiable. SciPy/HiGHS 1.8.0 reported **infeasible** after 1859 branch-and-bound nodes and 37880 LP iterations. Therefore the proposition is established by this computational audit, not by an independent handwritten infeasibility certificate. Verifier:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/4f8faeae42a6e8fd709c874eba3d30eeb5922732/scripts/nori_two_square_q5_milp.py.

The proposition is stronger than the known five-dimensional NORI1 existence statement: after the fixed colors are chosen, **at most eight free orbit variables**, lying on two projective squares, suffice to force a full monochromatic geodesic. Theorem 15 then gives a certificate of at most \(28\) rooted full geodesics for that fixed partial coloring.

The proof obligations in higher dimensions remain open. The positive all-dimensional fork mechanism above demonstrates how cross-square transport can force a geodesic even when all single-square implication formulas admit satisfying assignments; no unrestricted theorem currently forces such a packet for an arbitrary fixed coloring.


## The square-locality dichotomy and the necessity of cross-square transport

The preceding cross-square forcing example has a stronger structural explanation that holds in every dimension and for an arbitrary fixed partial coloring.

Fix free directions \(i,j\), let \(R=[n]\setminus\{i,j\}\), and consider an antipodal pair \(\Sigma=\{F_r,F_{\bar r}\}\) of two-dimensional \((i,j)\)-faces, indexed by a complementary pair of \(R\)-bit states \(r,\bar r\). Its four projective edge orbits—two of direction \(i\), two of direction \(j\)—form one *square block* of the two-direction Boolean variables. Let \(\Phi_{\Sigma}\) be the subformula of the full bipartite 2-CNF whose two variables both belong to this block.

**Lemma 21 (same-square path dichotomy).** Let \(P\) be any full dimension-distinct geodesic whose unique \(i\)-step and \(j\)-step belong to the same square block \(\Sigma\). Then precisely one of the following holds:

(a) the \(i\)-step and \(j\)-step are consecutive in the direction order;

(b) the \(i\)-step and \(j\)-step are the first and last steps, in either order, and the \(n-2\) intervening steps traverse every member of \(R\).

**Proof.** Project the path onto its \(R\)-bit state. At an \(i\)-edge or \(j\)-edge the \(R\)-state does not change. The two free edges belong to the same projective square block precisely when these two \(R\)-states are equal or complementary. Between the two free edges the path flips a subset \(S\subseteq R\), each direction at most once. If the states are equal, \(S=\varnothing\), so the free steps are consecutive. If complementary, \(S=R\), so all fixed-direction steps lie between them. Since there are no other free steps, they occupy the ends of the order. \(\square\)

**Theorem 22 (square-local forcing requires a monochromatic fixed facet).** If the square-block subformula \(\Phi_{\Sigma}\) is inconsistent, then among the four \((n-2)\)-dimensional faces obtained by fixing the \(i,j\) bits, at least one has a monochromatic full \(R\)-geodesic joining the two \(R\)-vertices \(r,\bar r\).

**Proof.** Suppose no such fixed-face full geodesic exists. For any rooted full path whose free edge orbits both belong to \(\Sigma\), Lemma 21 gives two possibilities. In case (b), its intervening fixed-direction edges cannot all have the same color, by assumption, so the path contributes no clause to \(\Phi_\Sigma\). Every clause therefore comes from case (a). Choose the four free orbit bits in block \(\Sigma\) so that, in the face \(F_r\), both direction-\(i\) edges have color zero and both direction-\(j\) edges have color one. Antipodal oddness forces their mates in \(F_{\bar r}\) to have the opposite colors, still different between directions. Consequently every case-(a) path has its two consecutive free edges in different colors and cannot be monochromatic. This assignment satisfies every clause of \(\Phi_\Sigma\), contradicting inconsistency. \(\square\)

**Corollary 23 (a rigorous cross-square necessity criterion).** If the prescribed fixed-direction colors admit no monochromatic full \(R\)-geodesic in any of the four \((i,j)\)-bit faces, then **every** individual projective-square block subformula is satisfiable. Any contradiction in the full two-direction 2-CNF must involve variables from at least two different projective square blocks.

**Proof.** Apply Theorem 22 to every \(\Sigma\). Each single-block formula is satisfiable. An inconsistent full formula therefore cannot be certified by clauses entirely supported on one block. \(\square\)

For the affine fixed-direction coloring of Theorem 19,
\[
c_2(x)=1+x_0,\qquad c_k(x)=x_0\quad(k\ge3),
\]
each \((i,j)=(0,1)\)-bit face fixes \(x_0\). Its direction-two edges therefore have the opposite color from every direction \(k\ge3\). Because \(n\ge4\), both types occur. Consequently no full \(R\)-geodesic in any such face is monochromatic. Corollary 23 proves, without computation and in **all dimensions**, that every individual square-block subformula is satisfiable. Yet the four paths of Theorem 19 force a contradiction using just three free orbit variables drawn from two square blocks.

This proves a dimension-uniform positive distinction: there are robust legal partial colorings for which **cross-square implication transport is mathematically necessary** for the forcing certificate, and an explicit four-path packet completes that transport. It also identifies precisely where a purely face-local strategy must fail. The remaining task is to force some form of cross-square transport for an arbitrary partial coloring, rather than imposing a universal local-square contradiction.


## Two-stage geodesic resolution and signed holonomy on one free direction

This continues the two-direction implication programme with a forcing certificate that transports constraints across several edge orbits rather than relying on a four-clause packet for one edge-orbit pair.

Fix directions \(i\ne j\) and all edge-orbit colors in the other \(n-2\) directions. Let \(X_e\) denote a free direction-\(i\) orbit bit and \(Y_f\) a free direction-\(j\) orbit bit. Theorem 13 associates to each near-monochromatic rooted full geodesic a forbidden assignment
\[
(X_e=p,\ Y_f=q)
\quad\Longleftrightarrow\quad
(X_e\ne p)\lor(Y_f\ne q).
\tag{50}
\]
The fixed partial coloring decides which such clauses are present.

**Theorem 24 (elimination by paired geodesics).** For each direction-\(i\) orbit \(e\), and for every two clauses
\[
(X_e\ne0)\lor(Y_f\ne q),\qquad
(X_e\ne1)\lor(Y_g\ne r),
\]
form the clause
\[
\boxed{(Y_f\ne q)\lor(Y_g\ne r).}
\tag{51}
\]
Let \(\Psi_j\) be the conjunction of all clauses (51), for every eliminated orbit \(e\). Clauses with \(f=g,q\ne r\) impose no restriction and may be discarded; if \(f=g,q=r\), (51) becomes the unit requirement \(Y_f\ne q\). Then
\[
\boxed{\Phi_{ij}\text{ satisfiable}\quad\Longleftrightarrow\quad
\Psi_j\text{ satisfiable}.}
\tag{52}
\]
Every clause of \(\Psi_j\) is certified by two full geodesics whose direction-\(i\) edges lie in the same antipodal orbit but whose prescribed colors there are opposite. The remaining direction-\(j\) orbits \(f,g\) may belong to different projective-square blocks.

**Proof.** If both \(Y_f=q\) and \(Y_g=r\) hold, the first original clause requires \(X_e=1\) and the second requires \(X_e=0\), an impossibility. Therefore every satisfying assignment of the original clauses obeys (51). Conversely, suppose an assignment of all \(Y\)-bits satisfies all the clauses (51), but for some \(e\) neither value of \(X_e\) satisfies the original clauses involving \(e\). There is then a violated clause under \(X_e=0\), having the form of the first displayed clause with \(Y_f=q\), and another violated clause under \(X_e=1\), with \(Y_g=r\). Their resolvent (51) is false, a contradiction. Thus every eliminated bit \(X_e\) admits at least one legal choice. These choices are independent once the \(Y\)-bits are fixed, so they produce a satisfying assignment of \(\Phi_{ij}\). \(\square\)

Theorem 24 is a projection of the full two-direction bad-extension region onto **one** free direction class. It preserves satisfiability without independent changes to the already colored dimensions. Its clauses have the geometric meaning of two near-monochromatic full geodesics passing through a common orbit, requiring opposite colors at that orbit.

**Theorem 25 (parity-holonomy forcing packets).** Suppose the resolved clauses (51) contain both
\[
(Y_f\ne0)\lor(Y_g\ne1),
\qquad
(Y_f\ne1)\lor(Y_g\ne0).
\]
Then every hypothetical bad completion satisfies \(Y_f=Y_g\). If instead the clauses include
\[
(Y_f\ne0)\lor(Y_g\ne0),
\qquad
(Y_f\ne1)\lor(Y_g\ne1),
\]
then every hypothetical bad completion satisfies \(Y_f\ne Y_g\).

Construct a signed multigraph on the direction-\(j\) edge orbits, placing an edge labeled \(\sigma\in\mathbb F_2\) whenever the resolved clauses enforce
\[
Y_f\oplus Y_g=\sigma.
\tag{53}
\]
If this multigraph contains a closed walk whose edge labels sum to one, then every completion contains a monochromatic full antipodal geodesic. A parity-inconsistent cycle of length \(\ell\) gives a certificate involving at most \(4\ell\) full geodesics. In particular, two parallel edges demanding opposite parities give a forcing certificate with at most eight geodesics.

**Proof.** The first two clauses rule out the assignments \((0,1),(1,0)\); the second pair rules out \((0,0),(1,1)\), giving the respective XOR constraints. Along a closed walk, XOR the enforced differences of successive \(Y\)-bits. The vertex terms cancel, leaving zero on the left. If the edge labels sum to one, this is impossible. Each XOR constraint uses two resolved clauses, and each resolved clause arises from two full geodesics by Theorem 24. Therefore \(\ell\) edges require at most \(4\ell\) geodesics; the unsatisfiability argument guarantees at least one is monochromatic in every completion. \(\square\)

This provides a constructive **transport-and-holonomy mechanism** in the original coloring: two full geodesics transport a constraint between free orbits in direction \(j\), and a parity-inconsistent network of such transports forces a monochromatic full geodesic. The unconditional existence of a parity-inconsistent cycle remains unproved in arbitrary dimensions; the general 2-SAT contradiction may instead arise from implication chains not reducible to pairwise XOR constraints.

## A six-geodesic forcing packet with no four-clause orbit pair

In \(Q_5\), fix free directions \(0,1\) and order the 24 already-colored antipodal edge orbits by direction \(2,3,4\), then by their canonical smaller lower endpoint. Give them the color bits of the 24-bit hexadecimal mask
\[
\boxed{\texttt{0xce337b}.}
\]
In the ordered list of 16 free edge orbits, denote bits \(X_0,X_1\) from direction zero and \(Y_0,Y_1\) from direction one. The six full geodesics below have all three fixed-direction edges of the indicated common color. Their free-edge colors must therefore avoid the forbidden assignments in the last column of any hypothetical bad completion.

| Root | Direction order | Fixed color | Forbidden assignment |
|---|---|---|---|
| \(1\) | \(0,1,2,3,4\) | \(0\) | \(X_0=0,\ Y_0=0\) |
| \(15\) | \(2,3,1,0,4\) | \(0\) | \(X_0=0,\ Y_1=0\) |
| \(0\) | \(0,4,3,2,1\) | \(1\) | \(X_0=1,\ Y_0=0\) |
| \(2\) | \(1,0,4,3,2\) | \(1\) | \(X_0=1,\ Y_0=1\) |
| \(3\) | \(0,2,3,4,1\) | \(0\) | \(X_1=0,\ Y_1=1\) |
| \(8\) | \(3,1,0,2,4\) | \(1\) | \(X_1=1,\ Y_0=1\) |

**Proposition 26 (six-path transport certificate).** For this fixed partial coloring, every legal assignment of the two free direction classes makes one of the six displayed full geodesics monochromatic. Yet no *single pair* consisting of a direction-zero orbit and a direction-one orbit admits clauses forbidding all four assignments. Thus a single-pair four-clause contradiction is unavailable, while paired-geodesic resolution forces a contradiction across multiple free orbits.

**Proof.** If \(X_0=1\), the third and fourth paths force \(Y_0=1\) and \(Y_0=0\), respectively, unless one is monochromatic. Thus any hypothetical bad completion has \(X_0=0\). The first and second paths then force \(Y_0=Y_1=1\). The fifth path requires \(X_1=1\), while the sixth requires \(X_1=0\), a contradiction. The claimed absence of a full four-clause orbit pair was independently checked by constructing every eligible rooted full path in this partial coloring and finding at most three forbidden assignments for any individual orbit pair. The six-path certificate is irredundant: deleting any one of its six clauses leaves a satisfying assignment of the four displayed free bits. \(\square\)

The six displayed paths were checked directly against all sixteen assignments of \(X_0,X_1,Y_0,Y_1\), and the fixed-edge color requirements were checked from the stated mask. This shows that the path-pair transport framework can force a monochromatic full geodesic in a case where no individual two-orbit four-clause certificate exists.

**Finite all-context audit.** For every one of the 256 assignments of the fixed-direction orbit colors in \(Q_4\), elimination of direction-zero variables produces direction-one XOR constraints demanding opposite parities on at least one pair of direction-one edge orbits. Thus Theorem 25 alone supplies a forcing certificate for all those partial colorings. Sampled partial colorings in dimensions five and six likewise exhibited an opposite-parity pair, but the existence of this stronger packet in all dimensions is unresolved.

**Verifier:** https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/028d1f475fcef9cb27d9700809ef531fe86cf51d/scripts/nori_two_direction_resolution_holonomy_verify.py.

### Proof-closure direction

The all-dimensional problem can now be sharpened beyond searching for arbitrary contradictory 2-SAT formulas: investigate whether the projective geometry and antipodal color-reversal law always produce a nontrivial parity-holonomy cycle in the resolved direction-one orbit graph. This is stronger than NORI1, and it may fail; in that case a satisfiable parity system together with an inconsistent general 2-SAT instance would identify the extra non-parity forcing that a final proof must accommodate. The theorem and its seven-path certificate establish a rigorous mechanism, not its universal occurrence.


## Parity-holonomy stress tests and limits

Theorem 25 gives a strictly stronger sufficient certificate than general two-direction 2-SAT inconsistency, so its universal validity cannot be assumed.

**Exhaustive affine Q5 audit.** Keep dimensions \(0,1\) free. In each of the three fixed directions \(k=2,3,4\), prescribe an arbitrary affine legal color rule
\[
c_k(x)=b_k+\sum_{\substack{j\ne k\\j\in[n]}}a_{kj}x_j,\qquad
\sum_{j\ne k}a_{kj}=1\pmod2 .
\]
There are sixteen independent choices for each fixed row, hence \(16^3=4096\) legal affine partial colorings. For every one of these 4096 choices, the two-stage resolution of Theorem 24 contains a pair of direction-one edge orbits forced to satisfy **both** equal and unequal parity. Therefore the eight-path forcing criterion of Theorem 25 succeeds throughout this entire affine five-dimensional family.

The number of direction-one orbit pairs carrying both parity requirements ranges from four to twenty-eight; all cases were enumerated. The independently checked histogram by number of contradictory pairs is
\[
\begin{array}{c|rrrrrrrr}
\#\text{pairs}&4&6&8&9&10&12&14&15\\
\#\text{partial colorings}&32&180&204&8&24&348&216&24
\end{array}
\]
\[
\begin{array}{c|rrrrrrrr}
\#\text{pairs}&16&20&21&22&24&26&27&28\\
\#\text{partial colorings}&888&24&48&84&456&360&48&1152 .
\end{array}
\]
The entries total 4096. This is a finite computational theorem about the stated affine family, not an all-dimensional statement about arbitrary partial colorings. The exhaustive routine is included in the updated verifier:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/baffc758042950c000cdf8a9c167efd9c3250dac/scripts/nori_two_direction_resolution_holonomy_verify.py.

**Counterexample to universal forcing on each prescribed pair of square blocks.** In \(Q_6\), there are eight projective \((0,1)\)-square blocks. Number them by increasing tuples of their four associated free orbit-variable indices. For the pair of square blocks indexed \(0,1\), the partial coloring of fixed-direction orbits with 64-bit bitmask
\[
\texttt{0x99109910ef268000}
\]
has a satisfiable two-square-restricted 2-CNF. The orbit-bit order is by direction \(2,3,4,5\), then by increasing canonical lower endpoint. A direct binary integer feasibility model found an assignment of the eight free orbit bits satisfying every clause internal to that pair; an independent implication-graph check confirmed satisfiability. Thus it is false that **every** pair of projective-square blocks must independently force a monochromatic geodesic. The still-open two-square question asks instead whether **some** pair forces one for every partial coloring.

These two stress tests sharpen the next decision: pursue a proof of unavoidable parity holonomy only after controlling nonlinear partial colorings, and avoid the disproved universal assertion about arbitrary square pairs. Theorem 25 is a sufficient color-consistency mechanism, not a theorem claiming that its certificate must always exist.


## Exhaustive five-cube parity-holonomy multiplicity and extremal classification

This section strengthens the finite evidence for the two-stage geodesic-resolution programme. The result is a **complete finite computation**, not a dimension-uniform proof of NORI1. It concerns every antipodally odd partial edge coloring of \(Q_5\) after leaving two fixed direction classes uncolored, including nonlinear rules.

Fix free directions \(0,1\). The three prescribed direction classes \(2,3,4\) contain \(3\cdot2^{5-2}=24\) independent antipodal edge-orbit color bits. Hence there are \(2^{24}=16,777,216\) possible partial colorings. Each free direction has eight edge-orbit variables. Apply the projective geodesic clause construction of Theorem 13 and eliminate all eight direction-zero variables by Theorem 24. For every unordered pair \(f,g\) of distinct direction-one orbits, let \(R_{fg}\subseteq\mathbb F_2^2\) be the set of ordered assignments \((p,q)\) forbidden by the resulting binary clauses \((Y_f\ne p)\lor(Y_g\ne q)\). Define the parity-diamond count
\[
D(c)=\#\{\{f,g\}:f\ne g,\ R_{fg}=\mathbb F_2^2\}.
\tag{54}
\]
Such a pair demands simultaneously \(Y_f=Y_g\) and \(Y_f\ne Y_g\), so by Theorems 24–25 it is a valid forcing certificate using at most eight rooted full geodesics.

**Computational Theorem 27 (universal four-diamond multiplicity in \(Q_5\)).** Every legal partial coloring of \(Q_5\), with arbitrary fixed colors in directions \(2,3,4\), satisfies
\[
\boxed{4\le D(c)\le28.}
\tag{55}
\]
Both inequalities are attained. Among all \(16,777,216\) partial colorings, precisely \(104\) have \(D(c)=4\). Consequently **each** five-dimensional two-direction partial coloring has at least four distinct contradictory parity-orbit pairs, each yielding a forcing packet of at most eight full geodesics. All remaining two-direction orbit colors may be assigned arbitrarily; one of the packet paths is monochromatic.

**Finite verification.** The self-contained C++17 verifier builds all \(16\cdot5!=1920\) rooted projective full geodesics, identifies their orbit-color indices and antipodal signs, and generates the \(1920\) distinct three-fixed-edge patterns for the two-direction clause system. For each of the \(2^{24}\) fixed-color masks, it checks the applicable patterns, forms all binary clauses, resolves the eight direction-zero variables, and counts the direction-one pairs for which all four forbidden assignments occur. The complete census has minimum four, maximum twenty-eight, with 104 minimizers. The histogram totals \(2^{24}\) assignments; its first nonempty entries are
\[
\begin{array}{c|rrrrrrrr}
D&4&6&8&9&10&11&12&13\\\hline
\#c&104&3156&4500&744&7704&8928&35884&33232
\end{array}
\]
and the highest entry is \(D=28\) with \(3,106,200\) colorings. No values \(D=0,1,2,3,5,7\) occur. The C++ verifier enforces the total count and minimum count as runtime assertions. A second Python implementation independently regenerates full geodesic path clauses and the two-step resolutions for all 104 minimizers.

Source:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/5ef8fa6bd14726dc6ae0dc9647c5cf175875ae64/scripts/nori_q5_parity_census.cpp

Compile with \`g++ -O3 -std=c++17 -fopenmp nori_q5_parity_census.cpp -o census\` and run \`OMP_NUM_THREADS=5 ./census\`. The OpenMP implementation is parallel only for speed; the combinatorial procedure and outputs are deterministic.

**Computational Theorem 28 (five extremal symmetry classes).** Consider the group generated by translating cube vertices, permuting directions \(2,3,4\) while leaving directions \(0,1\) fixed, and complementing all edge colors. These operations preserve \(D(c)\). The 104 minimizers split into five orbits under this group:

| Number of minimizers | Representative fixed-orbit mask |
|---:|---|
| 48 | \(\texttt{0x000057}\) |
| 24 | \(\texttt{0x00005f}\) |
| 24 | \(\texttt{0x000055}\) |
| 6 | \(\texttt{0x5555aa}\) |
| 2 | \(\texttt{0x555555}\) |

The orbit-color indexing is by direction \(2,3,4\), then increasing canonical lower endpoint of each antipodal edge orbit, with bit zero in direction \(i\). An independent Python symmetry-classifier verifies that each orbit lies entirely among the 104 minimizers and that their five sizes total 104. It also reconstructs the parity-diamond graph for every minimizer, whose vertices are the eight direction-one orbits and whose edges are the four contradictory pairs. Precisely **96 minimizers** have a four-cycle on four vertices; the remaining **8 minimizers** have a perfect matching on all eight vertices. Thus every extremal partial coloring possesses at least two vertex-disjoint contradictory parity pairs.

Symmetry and independent parity-resolution verifier:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/bc8056c0c830cb90d96959e03a5ac04c6adef2dd/scripts/nori_q5_parity_symmetry.py

This gives a more informative finite forcing result than a bare five-cube NORI1 computation: the *same arbitrary fixed edge assignment* already forces multiple separate short implication certificates, and the sparsest certificates exhibit only two structural graph types. The unresolved step is to find a dimension-uniform geometric reason for their multiplicity, without assuming that a proper five-dimensional face inherits the original coloring's antipodal oddness. Under global complementation in \(Q_n\), a proper five-face is normally sent to a different face, so the five-dimensional census cannot simply be applied to a smaller face of an arbitrary larger cube. That is the principal barrier to transferring (55) into unrestricted NORI1.


## Two disjoint parity diamonds and an orbit-avoiding eight-path certificate in Q5

The preceding complete five-cube census admits a stronger check that directly connects parity holonomy to the critical-orbit avoidance programme. For each partial coloring \(c\), let \(H(c)\) be the simple graph on its eight retained direction-one orbit variables. Put an edge \(\{f,g\}\) in \(H(c)\) precisely when the resolved formula forbids all four assignments of \((Y_f,Y_g)\); these are the parity diamonds counted by \(D(c)\).

**Computational Theorem 29 (disjoint parity diamonds).** For every one of the \(2^{24}\) legal partial colorings of \(Q_5\),
\[
\boxed{\nu(H(c))\ge2,}
\tag{56}
\]
where \(\nu\) denotes maximum matching size.

**Finite verification.** In the same independent 24-bit enumeration as Theorem 27, the C++ certificate computes the intersection of the endpoint sets of all parity-diamond edges. In every one of the \(16,777,216\) cases, this common intersection is empty; the recorded count of star-supported contradiction graphs is zero. By Theorem 27, every \(H(c)\) has at least four edges. A finite simple graph with at least four edges and matching number at most one must have a common vertex incident with every edge: otherwise select two meeting edges \(ab,ac\); a third not using \(a\) must be \(bc\), and no fourth distinct edge can meet all three. Thus the absence of a common vertex together with \(D(c)\ge4\) establishes (56). The verified all-mask census now asserts
\[
\boxed{\texttt{COMMON\_VERTEX\_STAR\_COUNT}=0}.
\]
The updated standalone verifier is:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/07354bcfb9ea43c680e78bab62703f6a5d5ec2c6/scripts/nori_q5_parity_census.cpp.

**Corollary 30 (robust dimension-five orbit avoidance with at most eight paths).** For every legal antipodally odd edge coloring of \(Q_5\) and every prescribed antipodal edge orbit \(e\), there is a monochromatic full antipodal geodesic avoiding \(e\). Moreover, there is a family of at most eight full rooted geodesics, all avoiding \(e\), such that **every legal assignment of the color bits in two chosen direction classes** makes at least one of these paths monochromatic, provided the edge colors of the other three direction classes remain fixed.

**Proof.** Choose one of the two free direction classes to be the direction of \(e\); call it the retained direction \(j\), and choose any different direction \(i\) as the eliminated free direction. All other three direction classes are held fixed, with arbitrary legal colors. By Theorem 29 their two-direction resolved parity graph \(H(c)\) has two vertex-disjoint parity-diamond edges. At least one of these edges \(\{f,g\}\) avoids the selected orbit \(e\). The two opposite parity requirements on \(Y_f,Y_g\) each arise from two resolved clauses, and each resolved clause is certified by two full geodesics through a common eliminated-direction orbit. Hence at most eight full rooted geodesics certify an inconsistent partial-color formula, and none of these geodesics uses \(e\): their retained-direction steps are exclusively in orbits \(f\) and \(g\). Therefore any completion of the two free direction classes must make one of these paths monochromatic, and that path avoids \(e\). By permuting cube dimensions, every direction can be chosen as retained direction \(j\). \(\square\)

This establishes the earlier five-dimensional prescribed-orbit avoidance phenomenon by a separate, stronger finite verification. It is **robust under changing all the color bits in two entire direction classes**, not just flipping the prescribed orbit. The mechanism is constructive given the three fixed direction classes and the implication-packet extraction. The evidence remains finite-dimensional; a dimension-uniform lower bound on the matching number of parity-diamond graphs would provide a direct route to unrestricted NORI1 and orbit-flip stability, but is not proved here.

The two observed four-diamond extremal graph shapes from Theorem 28, a four-cycle and a four-edge perfect matching, both have matching number at least two. The zero-star computation checks this separation across the full five-cube partial-coloring space, not merely among the 104 extremizers.


## Cartesian tensorization of the two-direction implication system

Let \(a\ge3,b\ge2\). Fix distinct free directions \(i,j\) in \(Q_a\), and let \(f\) be a legal antipodally odd *partial coloring*: every edge outside directions \(i,j\) is colored, independently across antipodal edge orbits, and the colors of all direction-\(i,j\) orbits are left unspecified. Let \(g\) be a legal antipodally odd full coloring of \(Q_b\). Define \(f\boxtimes g\) on \(Q_{a+b}\) by taking its fixed first-block edge colors from \(f\), with no dependence on second-block bits, and all second-block edge colors from \(g\), with no dependence on first-block bits. The two first-block free directions remain free.

Write \(\Phi_{ij}(f)\) for the near-monochromatic full-geodesic clause formula from Theorem 13; let \(H_{ij}(f)\) be its resolved parity-diamond graph from Theorem 25, \(D_{ij}(f)=|E(H_{ij}(f))|\), and \(\nu_{ij}(f)\) its matching number. Define
\[
M(g)=\{w\in Q_b:\text{a monochromatic full geodesic from }w
\text{ to }\bar w\text{ exists in }g\}.
\]
The set \(M(g)\) is antipodally invariant. At any \(w\in M(g)\), there are both red and blue monochromatic full geodesics from \(w\) to \(\bar w\): reverse the antipodal translate of a geodesic of the other color.

**Theorem 31 (disjoint Cartesian clause lifting).** If \(M(g)\ne\varnothing\), then \(\Phi_{ij}(f\boxtimes g)\) contains, for each \(w\in M(g)\), a copy of the entire formula \(\Phi_{ij}(f)\), up to a relabeling and complementation of individual free Boolean variables. These copies use pairwise disjoint sets of free edge-orbit variables. Hence
\[
\boxed{D_{ij}(f\boxtimes g)\ge |M(g)|D_{ij}(f),}
\tag{57}
\]
and
\[
\boxed{\nu_{ij}(f\boxtimes g)\ge |M(g)|\nu_{ij}(f).}
\tag{58}
\]
Each contradictory implication-path packet in \(f\) also lifts to \(|M(g)|\) disjoint forcing packets in the product.

**Proof.** Choose one representative cube edge \(e\) from each free antipodal edge orbit of \(Q_a\). For \(w\in M(g)\), associate to this orbit the full-product orbit
\[
\phi_w([e])=\{(e,w),(\bar e,\bar w)\}.
\tag{59}
\]
For a fixed \(w\), the map \(\phi_w\) is injective; the images for distinct \(w\) are disjoint, because the chosen first-block representatives never include both \(e\) and \(\bar e\).

Consider any clause of \(\Phi_{ij}(f)\), witnessed by a full geodesic \(P\) whose colored edges outside \(i,j\) all have color \(t\). Antipodally translate \(P\), if needed, so that \(t=0\). This leaves its forbidden free-variable assignment unchanged: the translate complements both the prescribed color and the two free-edge colors.

Each of the two free edges of \(P\) is either its selected orbit representative or that representative's antipodal mate. Assign it a required second-block state, \(w\) in the first case and \(\bar w\) in the second. If the two required states differ, insert a monochromatic red full \(Q_b\)-geodesic between the two free steps of \(P\). If they agree, insert such a geodesic before both or after both, choosing its starting state accordingly. The connector can traverse from \(w\) to \(\bar w\) in either direction and has color zero. All first-block colored edges still have color zero, because their colors are independent of the second-block state. The lifted path traverses every one of the \(a+b\) dimensions once, and its two free steps lie in the respective full orbits \(\phi_w([e_i]),\phi_w([e_j])\). Their color requirements correspond to the original clause, with possible complementation depending on which edge is chosen as the variable representative in the larger cube.

Thus every clause in \(\Phi_{ij}(f)\) appears in the \(w\)-copy. Resolving the common first-direction variables in the larger formula reproduces all resolved clauses in each copy. Any contradictory parity pair in the base therefore supplies a contradictory pair in every copy. Disjointness yields (57) and allows matchings in the copies to be united, proving (58). The same argument transports a selected implication packet. \(\square\)

**Consequence for minimal obstructions.** A putative partial coloring with no parity diamond cannot split in this way into a first block already containing a diamond and a second block with a monochromatic antipodal geodesic. Theorem 31 therefore gives a certificate-preserving interaction-prime reduction for product decompositions, stronger than a qualitative product-existence argument. It does not show that every interaction-prime partial coloring contains a diamond.

## An all-dimensional sparse parity-diamond graph

The random partial-coloring census cannot reveal how sparse the parity constraints may become. The following nonlinear-in-dimension, but affine-in-bits, family gives a sharp combinatorial benchmark.

Take \(n=m+2\ge3\), leave directions \(0,1\) free, and prescribe
\[
\boxed{c_k(x)=x_0\qquad(2\le k<n).}
\tag{60}
\]
These fixed-direction rules are legal under global antipodal color reversal, and the free directions may be colored in any legal fashion.

Write \(R=\{2,\ldots,n-1\}\), and identify its vertex set with \(\mathbb F_2^m\). For \(s\in\mathbb F_2^m\), define \(X_s\) to be the color of the direction-zero edge whose other bits are \(x_1=0,x_R=s\); define \(Y_s\) as the color of the direction-one edge whose other bits are \(x_0=0,x_R=s\). The antipodal mates have the complementary colors. These are convenient choices of representatives of all free edge orbits; they need not be the smallest-integer representatives used by computer enumerations.

**Theorem 32 (complete star clause formula and matching graph).** In these variables the full near-monochromatic-geodesic 2-CNF forbids precisely the assignments
\[
\boxed{
\begin{aligned}
&(X_s=p,\ Y_r=0)&&\text{for all }s,r\in\mathbb F_2^m,\ p\in\mathbb F_2,\\
&(X_s=1,\ Y_s=1)&&\text{for all }s\in\mathbb F_2^m,\\
&(X_s=0,\ Y_{\bar s}=1)&&\text{for all }s\in\mathbb F_2^m.
\end{aligned}}
\tag{61}
\]
The formula has \(2^{2m+1}+2^{m+1}\) distinct forbidden pairs. After eliminating all \(X\)-variables, for every pair \(r\ne s\) the resolved clauses forbid \((Y_r,Y_s)=(0,0),(0,1),(1,0)\); the fourth assignment \((1,1)\) is also forbidden if and only if \(s=\bar r\). Consequently
\[
\boxed{
H_{01}(c)=\{\{r,\bar r\}:r\in\mathbb F_2^m\},
\quad
D_{01}(c)=\nu_{01}(c)=2^{m-1}=2^{n-3}.
}
\tag{62}
\]
In particular, the parity-diamond graph can be a disjoint matching in arbitrarily high dimension. Its graph connectivity is not a necessary feature of successful parity forcing.

**Proof.** Every fixed-direction edge has color equal to the current bit \(x_0\). Since a full geodesic crosses direction zero once, its \(m\) fixed-direction edges are monochromatic if and only if all their steps lie on the same side of that crossing.

First suppose the direction-one step lies on the side containing all \(R\)-steps. At its crossing, the bit \(x_0\) equals their common color \(t\), and the canonical \(Y_r\)-edge must therefore have color zero to make the full path monochromatic. Conversely, given arbitrary \(s,r,p\), set \(t=0\) and place the direction-zero step last. If \(p=0\), traverse a full \(R\)-geodesic from \(\bar s\) to \(s\), inserting the direction-one step when its \(R\)-state is \(r\), with the direction-one bit changed from one to zero. The last step uses \(X_s\), and the path becomes monochromatic when \(X_s=Y_r=0\). If \(p=1\), traverse a full \(R\)-geodesic from \(s\) to \(\bar s\), inserting the direction-one step at \(R\)-state \(r\), now changing its bit from zero to one. The last direction-zero edge is the antipodal mate of \(X_s\); the path becomes monochromatic when \(X_s=1,Y_r=0\). Every prescribed \(r\) lies on a full monotone cube geodesic from \(s\) to \(\bar s\), by taking the differing directions first. This proves every assignment in the first line of (61) is forbidden.

If instead the direction-one step lies on the other side of the direction-zero crossing from all \(R\)-steps, the two free steps are consecutive. Their \(R\)-states coincide. A short case distinction according to the common fixed-edge color and the intervening direction-one bit shows that the only possible forbidden assignments with \(Y_r=1\) are \((X_s=1,Y_s=1)\) and \((X_s=0,Y_{\bar s}=1)\). Both occur: the full direction order \((1,0,R)\), starting respectively from bit configurations \((x_0,x_1,x_R)=(0,1,s)\) and \((0,0,\bar s)\), has all fixed edges color one and realizes the two indicated assignments. This proves (61).

Resolve a clause \((X_u=0,Y_r=q)\) with a clause \((X_u=1,Y_s=q')\), meaning that both are forbidden, to obtain the forbidden assignment \((Y_r=q,Y_s=q')\). The first line of (61) supplies \((0,0)\) for every pair of retained variables. Combining a first-line clause with either of the last two families gives \((0,1)\) and \((1,0)\). For two clauses both requiring retained color one to have opposite \(X_u\) values, the second line must be paired with the third at the same \(u\), and their retained indices are \(u,\bar u\). Hence \((1,1)\) is forbidden precisely for complementary retained indices. This gives (62). \(\square\)

Theorem 32 is an all-dimensional structural description, but it does not establish a universal lower bound \(D_{ij}(c)\ge2^{n-3}\) for arbitrary legal partial colorings. It identifies a sparse family that such a lower bound, if true, would have to attain.

**Verification.** Full projective geodesic enumeration confirms the clause equality (61), the parity-diamond graph (62), and its disjoint matching in dimensions \(3,4,5,6\). Independent product tests for five sampled \(Q_4\) partial colorings and legal \(Q_2\) factors confirm that every base clause lifts into two disjoint variable sets in \(Q_6\), including the requisite antipodal sign changes. A self-contained verifier is available:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/1c2600f0124849b9e61386b2ac048d86afabf96c/scripts/nori_parity_tensor_star_verify.py.

**Remaining obstacle.** Theorem 31 propagates existing forcing certificates through independent factors, and Theorem 32 supplies a minimal-looking family of disjoint certificates in every dimension. Neither manufactures a parity contradiction inside an arbitrary interaction-prime coloring. That case remains the unrestricted closure target.


**Corollary 33 (four-path star packet).** In the partial coloring (60), fix any \(s\in\mathbb F_2^m\). Four rooted full geodesics already force a monochromatic one, regardless of all free orbit colors. Their forbidden assignments are
\[
\boxed{
(X_s=1,Y_s=0),\quad(X_s=1,Y_s=1),\quad
(X_s=0,Y_{\bar s}=0),\quad(X_s=0,Y_{\bar s}=1).
}
\tag{63}
\]
These arise from the four constructions in the proof of Theorem 32. If \(X_s=1\), one of the first two geodesics is monochromatic, whichever value \(Y_s\) takes; if \(X_s=0\), one of the last two is monochromatic, whichever value \(Y_{\bar s}\) takes. Thus the sparse all-dimensional parity matching in Theorem 32 also contains many four-path local forcing certificates. The distinction matters: a large parity-diamond matching does not imply that the shortest forcing packet must use eight paths.


## Two-sided pivot transport and cross-curvature forcing

Let \(Q_n=Q_A\times Q_B\), where \(|A|=a\ge3\), \(|B|=b\ge1\), and two free directions \(i,j\) belong to \(A\). Fix a third direction \(k\in A\setminus\{i,j\}\). For a root \(w\in Q_B\), suppose:

(C1) For every prescribed direction \(\ell\in A\setminus\{i,j\}\), every \(x\in Q_A\) satisfies \(c_\ell(x,w)=c_\ell(x,\bar w)\).

(C2) For every direction-\(k\) edge \(\{z,z+e_k\}\subset Q_A\) and each color \(t\in\mathbb F_2\), **at least one endpoint** has a monochromatic full \(B\)-geodesic of color \(t\) between \(w\) and \(\bar w\), in its induced \(B\)-slice.

Write \(f^{(w)}\) for the prescribed \(A\)-coloring induced by layer \(w\); by (C1) and the full cube's antipodal oddness, \(f^{(w)}\) is antipodally odd.

**Theorem 34 (two-sided pivot transport).** Under (C1)–(C2), the two-direction implication formula \(\Phi_{ij}(c)\) contains a full copy of \(\Phi_{ij}(f^{(w)})\), up to relabeling and complementation of free orbit bits. Different \(w\)'s yield variable-disjoint copies. Consequently, if \(W_k\) is the family of eligible roots,
\[
\boxed{
D_{ij}(c)\ge\sum_{w\in W_k}D_{ij}(f^{(w)}),\qquad
\nu_{ij}(c)\ge\sum_{w\in W_k}\nu_{ij}(f^{(w)}).
}
\tag{64}
\]

**Proof.** For every free antipodal \(A\)-edge orbit select its member in the \(k\)-bit-zero facet, and for each \(w\) map it to the full-cube edge orbit represented by that edge in layer \(w\). These mappings have disjoint images for distinct \(w\).

Take any near-monochromatic full \(A\)-geodesic \(P=(z_0,\dots,z_a)\) producing a clause of \(\Phi_{ij}(f^{(w)})\), with its prescribed edges all color \(t\). Its unique \(k\)-step is \(z_r\to z_{r+1}=z_r+e_k\). Start the lifted path in \(B\)-layer \(w\) if the initial \(k\)-bit is zero, and in layer \(\bar w\) otherwise. Insert one full \(B\)-geodesic **immediately before or immediately after the \(k\)-step**. In both cases, because no free step lies between those two insertion positions, each free \(A\)-edge occurs in the required \(B\)-layer: \(w\) when its \(k\)-bit is zero, \(\bar w\) otherwise. All prescribed \(A\)-edges retain color \(t\), by (C1). By (C2), either \(z_r\) or \(z_{r+1}\) supplies a monochromatic \(B\)-connector of color \(t\); choose that insertion position. The resulting full \((a+b)\)-geodesic witnesses the mapped clause. Do this for every clause, and sum the disjoint parity-diamond graphs and matchings. \(\square\)

There is **no requirement for both connector colors at the same \(A\)-vertex**. One endpoint of a \(k\)-edge may support only color zero and the other only color one. This mechanism therefore applies to coupled colorings with no two-color connector at any individual vertex.

### A square-curvature criterion when \(B=Q_2\)

Suppose \(B=\{u,v\}\), every \(B\)-slice at fixed \(x\in Q_A\) is itself antipodally odd, and (C1) holds for all \(w\). The slice edge rules have the form
\[
c_u(x,y)=\alpha(x)+y_v,\qquad c_v(x,y)=\beta(x)+y_u,
\]
with \(\alpha,\beta\) antipodally even on \(Q_A\). Put \(s(x)=\alpha(x)+\beta(x)\pmod2\). The roots \(00,11\) possess monochromatic \(B\)-geodesics of both colors if \(s=1\); the roots \(01,10\) possess both if \(s=0\).

**Corollary 35 (cross-curvature imbalance).** If
\[
\boxed{\partial_k s(x)=1\qquad\forall x\in Q_A,}
\tag{65}
\]
then the condition (C2) holds for **all four** \(B\)-roots, and hence
\[
\boxed{D_{ij}(c)\ge\sum_{w\in Q_2}D_{ij}(f^{(w)}),\quad
\nu_{ij}(c)\ge\sum_{w\in Q_2}\nu_{ij}(f^{(w)}).}
\tag{66}
\]
In terms of cross-block square curvatures,
\[
\boxed{\kappa_{k,u}(x,y)+\kappa_{k,v}(x,y)
=\partial_k(\alpha+\beta)(x)=1.}
\tag{67}
\]
Indeed (C1) implies \(\partial_u c_k=\partial_v c_k\) on the two-cube; the other terms in the two curvatures give \(\partial_k\alpha+\partial_k\beta\). Each \(k\)-edge changes the favorable diagonal of its \(B\)-slice, so one of its endpoints supplies both connector colors for each \(w\). Apply Theorem 34.

### Arbitrarily many copies without any two-color connector

**Corollary 36 (monochrome-fibre amplification).** Let \(f\) be any legal antipodally odd partial coloring on \(Q_A\), directions \(i,j\) free, and \(k\) a third direction. Let \(b\ge1\), and choose an arbitrary antipodally even \(\psi:Q_B\to\mathbb F_2\). Define the prescribed colors on \(Q_A\times Q_B\) by
\[
\boxed{
c_\ell(x,y)=f_\ell(x)+\psi(y)\quad(\ell\in A\setminus\{i,j\}),
\qquad c_t(x,y)=x_k\quad(t\in B).
}
\tag{68}
\]
Then
\[
\boxed{
D_{ij}(c)\ge 2^bD_{ij}(f),\qquad
\nu_{ij}(c)\ge2^b\nu_{ij}(f).
}
\tag{69}
\]

**Proof.** The rules (68) are undirected and globally antipodally odd. Condition (C1) follows from the evenness of \(\psi\). All \(B\)-edges in the slice at \(x\) have the single color \(x_k\). At the other endpoint of every \(k\)-edge, all \(B\)-edges have the opposite color. Thus each endpoint supports full \(B\)-geodesics of one color and together they cover both colors: (C2) holds for every \(w\). Apply Theorem 34. The induced coloring is \(f+\psi(w)\). Globally complementing its prescribed edge colors corresponds to complementing every forbidden free-orbit assignment, preserving both \(D\) and \(\nu\). Hence each of the \(2^b\) copies contributes \(D_{ij}(f)\) and \(\nu_{ij}(f)\). \(\square\)

This is not a Cartesian product or the previous two-color gauge lifting: no induced \(B\)-slice has a monochromatic connector of the opposite color. The full coloring may also have a strongly connected directed influence graph.

**Strongly connected legal \(Q_5\) witness.** With \(A\)-bits \(x_0,x_1,x_2\) and \(B\)-bits \(y_0,y_1\), use
\[
\boxed{
c_0=x_1+x_2+y_0,\quad c_1=x_2,\quad
c_2=x_0+y_0+y_1,\quad c_3=x_2,\quad c_4=x_2
}\pmod2.
\tag{70}
\]
The directed influence graph is strongly connected on all five directions. No \(B\)-slice has both connector colors at any root. Nevertheless the two-direction clause formula contains four disjoint copies of the \(Q_3\) formula (12 clauses and one parity diamond in each copy). Direct enumeration finds 144 full-cube clauses and 22 contradictory parity pairs.

**Verification:** Standalone geodesic-order enumeration checked the pivot position and mapped clauses in the strong \(Q_5\) witness, the curvature corollary for four \(B\)-roots, and arbitrary sampled \(Q_4\) fixed-edge colorings with \(Q_2,Q_3\) monochrome-fibre extensions. The tests certify 4 and 8 distinct implication copies in dimensions five, six, and seven. Local scripts: \`nori_two_sided_pivot_verify.py\` and \`nori_pivot_monochrome_verify.py\`.

**Remaining question.** Theorem 34 supplies an all-dimensional conditional forcing mechanism within an unchanged legal coloring, and (69) amplifies certificates through nonseparable block interactions. It does not establish that edgewise connector coverage must exist in every legal coloring. The unrestricted NORI1 conjecture remains open.


## Adaptive odd-seam transport without a fixed pivot

Write \(Q_n=Q_A\times Q_B\), with \(|A|=a\ge3\) and free directions \(i,j\in A\). Fix a family \(W\subseteq Q_B\). Assume:

(A1) For every \(w\in W\), prescribed \(A\)-edge colors agree between the layers \(w,\bar w\).

(A2) There is one Boolean function \(h:Q_A\to\mathbb F_2\), independent of \(w\), satisfying
\[
\boxed{h(\bar x)=1-h(x),\qquad \partial_i h=\partial_j h=0.}
\tag{71}
\]

(A3) At every \(A\)-vertex \(x\) and every \(w\in W\), some full \(B\)-geodesic from \(w\) to \(\bar w\) has constant edge color \(h(x)\) in the induced \(B\)-slice at \(x\). No geodesic of the opposite color is required.

Denote by \(f^{(w)}\) the legal antipodally odd prescribed \(A\)-coloring induced in layer \(w\).

**Theorem 37 (adaptive odd-seam lifting).** For each \(w\in W\), the two-direction clause formula \(\Phi_{ij}(f^{(w)})\) embeds into \(\Phi_{ij}(c)\) after consistent relabeling and complementation of its free orbit bits. These clause copies use disjoint variable sets for distinct \(w\). Consequently
\[
\boxed{D_{ij}(c)\ge\sum_{w\in W}D_{ij}(f^{(w)}),\qquad
\nu_{ij}(c)\ge\sum_{w\in W}\nu_{ij}(f^{(w)}).}
\tag{72}
\]

**Proof.** The value of \(h\) is constant along any edge in either free direction. Antipodal oddness of \(h\) therefore selects one member of every free antipodal \(A\)-edge orbit, namely the one on which \(h=0\). Map that representative into \(B\)-layer \(w\) as a representative of the corresponding full-cube free orbit. Use these same \(A\)-representatives for all \(w\); their full-cube images have disjoint variable sets.

Consider a rooted full \(A\)-geodesic \(P\) witnessing a clause, with all prescribed \(A\)-edge colors equal to \(t\). Let \(\alpha,\beta\) be the values of \(h\) at its first and second free steps, in traversal order. The two free steps must lie in layer \(w\) when their \(h\)-value is zero, and in layer \(\bar w\) when that value is one.

If \(\alpha\ne\beta\), insert the full \(B\)-connector *between* the two free steps. The vertex immediately after the earlier free step has \(h=\alpha\), whereas the vertex immediately before the later free step has \(h=\beta\). Since these values differ, one of these insertion vertices has \(h=t\). By (A3), it supports the required monochromatic connector. Choose the initial \(B\)-layer to place the two free steps in their desired layers.

If \(\alpha=\beta\), insert the connector at the start or the end of the full \(A\)-path. Its root and terminal vertex are antipodal, so their \(h\)-values are complementary. One is \(t\), giving a color-\(t\) connector by (A3). Again choose the initial layer to put both free steps in their common desired layer.

In both cases, all prescribed \(A\)-edge colors remain \(t\) by (A1), and the inserted \(B\)-geodesic also has color \(t\). The new full geodesic therefore witnesses the mapped clause, including its projective orbit-color signs. Repeat over all clauses and all \(w\). The disjoint variable copies imply (72). \(\square\)

**Corollary 38 (arbitrary odd-selector amplification).** Let \(f\) be any legal partial antipodally odd \(A\)-coloring with directions \(i,j\) free, and \(h\) any antipodally odd Boolean function independent of those two direction bits. For any \(b\ge1\) and antipodally even \(\psi:Q_B\to\mathbb F_2\), prescribe
\[
\boxed{
c_\ell(x,y)=f_\ell(x)+\psi(y)\quad(\ell\in A\setminus\{i,j\}),\qquad
c_t(x,y)=h(x)\quad(t\in B).
}
\tag{73}
\]
Then
\[
\boxed{D_{ij}(c)\ge2^bD_{ij}(f),\qquad
\nu_{ij}(c)\ge2^b\nu_{ij}(f).}
\tag{74}
\]
Every full \(B\)-geodesic at \(x\) has color \(h(x)\), meeting (A3) for all \(2^b\) roots. The induced \(A\)-coloring is \(f\) or its complement, which have identical parity-diamond counts and matching numbers.

**Strict improvement over the fixed-pivot theorem.** In \(Q_A=Q_5\), leave directions \(0,1\) free and let \(h(x)\) be the majority of the three bits \(x_2,x_3,x_4\). Then \(h\) is antipodally odd and independent of the free directions. For each \(k\in\{2,3,4\}\) there is a \(k\)-edge on which \(h\) is unchanged, so no \(k\) meets the everywhere-toggling hypothesis of the earlier monochrome-fibre pivot theorem. Yet Corollary 38 applies for every legal lower partial coloring \(f\); one explicit choice is \(f_\ell(x)=x_{(\ell+1)\bmod5}\) in each prescribed direction \(\ell=2,3,4\).

**Boundary example (free-direction dependence cannot simply be ignored).** Let \(A=Q_3\), free directions \(0,1\), and sole prescribed edge rule \(f_2(x)=x_1\). Attach \(Q_B=Q_1\), with its edge color \(h(x)=1\) at the four vertices with binary indices \(0,4,5,6\), and color zero at indices \(1,2,3,7\). This \(h\) is antipodally odd but depends on both free bits. The base two-direction formula has twelve clauses. For each of the sixteen ways to choose a representative from each of the four free antipodal \(A\)-edge orbits, map the chosen representatives into one \(B\)-layer and transport the signed clauses. Independent full-geodesic enumeration finds the overlap with the full \(Q_4\) clause set to be eight for four choices, nine for eight choices, and ten for four choices. **No representative-based mapping preserves all twelve original clauses.** This disproves the unconditional extension of the present clause-copy rule without (A2); it does not supply a counterexample to NORI1.

**Executable audit.** A self-contained full-geodesic enumerator tests the signed clause copies in 44 randomly generated legal partial colorings of dimensions \(Q_3\times Q_1\), \(Q_4\times Q_1\), \(Q_3\times Q_2\), \(Q_4\times Q_2\), \(Q_3\times Q_3\), and \(Q_5\times Q_1\), as well as the majority witness and all sixteen boundary representative choices. Verifier:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/3ea7c0767f4a606c72f1756f9d23c2ebdf62ed9d/scripts/nori_adaptive_odd_seam_verify.py.

**Closure obligation.** Adaptive seam transport removes the need for one fixed pivot direction, but requires the connector-selector function \(h\) to be well-defined on free edges. A universal proof must either produce such compatibility within every hypothetical bad coloring, or replace this free-edge obstruction with a different way of transporting clause contradictions.


## Four-vertex connector-selector test and local failure certificates

The selector \(h\) in Theorem 37 can be tested within any original legal partial coloring without guessing a Boolean function. Fix the partition \(A\sqcup B\), free directions \(i,j\in A\), and a nonempty collection of \(B\)-roots \(W\). For \(w\in W\) and \(x\in Q_A\), define the available monochromatic connector-color set
\[
S_w(x)=\{t\in\mathbb F_2:\text{the induced }B\text{-slice at }x
\text{ has a monochromatic full }w\text{-to-}\bar w\text{ geodesic of color }t\}.
\]
Put \(S_W(x)=\bigcap_{w\in W}S_w(x)\). These sets may be empty. Global antipodal oddness and reversal of undirected geodesics imply
\[
\boxed{S_w(\bar x)=1-S_w(x),\qquad S_W(\bar x)=1-S_W(x).}
\tag{75}
\]
Here \(1-S=\{1-t:t\in S\}\).

Write \(R=A\setminus\{i,j\}\). For each \(R\)-bit assignment \(z\), let \(F_z\) be the four-vertex \(i,j\)-face having those fixed \(R\)-bits, and define
\[
\boxed{I_W(z)=\bigcap_{x\in F_z}S_W(x).}
\tag{76}
\]
Then \(I_W(\bar z)=1-I_W(z)\).

**Theorem 39 (free-face selector criterion).** There exists a Boolean function \(h:Q_A\to\mathbb F_2\) that is antipodally odd, independent of the two free bits, and satisfies \(h(x)\in S_w(x)\) for every \(x\) and \(w\in W\), **if and only if**
\[
\boxed{I_W(z)\ne\varnothing\qquad\forall z\in Q_R.}
\tag{77}
\]

**Proof.** Independence of the free bits means that \(h\) is constant on each \(F_z\), so its value must belong to \(I_W(z)\); necessity follows. Conversely choose a representative \(z\) from each complementary pair \(\{z,\bar z\}\) of \(Q_R\), and any \(t_z\in I_W(z)\). Set \(h=t_z\) throughout \(F_z\) and \(h=1-t_z\) throughout \(F_{\bar z}\). Identity (75) ensures that the second value belongs to \(I_W(\bar z)\). The resulting \(h\) is independent of \(i,j\), antipodally odd, and supported at every selected connector root. \(\square\)

**Corollary 40 (two-vertex failure certificate).** If the selector does not exist, then some free \(i,j\)-face \(F_z\) contains either (a) a vertex \(x\) with \(S_W(x)=\varnothing\), or (b) two vertices \(x,x'\) with \(S_W(x)=\{0\}\), \(S_W(x')=\{1\}\). Conversely either conflict prevents a selector. This follows because each \(S_W(x)\) is a subset of the two-element set \(\mathbb F_2\): an empty intersection is witnessed by one empty set or two incompatible singleton sets.

Together with opposite-layer consistency (A1), criterion (77) therefore gives a finite, directly checkable sufficient condition for the all-dimensional forcing and certificate amplification of Theorem 37. The criterion does not hold for every legal coloring. A hypothetical coloring in which all such adaptive transports fail must exhibit a local connector-color conflict (or connector absence) on a free two-face for every attempted layer family; establishing an incompatible global arrangement of these local failures remains the missing step to unrestricted NORI1.


## Sparse selector conflicts: packet robustness measured by Boolean influence

The adaptive seam proof can still transport clauses when the odd connector selector changes along *some*, but not all, free-direction edges. This yields a robustness theorem for arbitrary antipodally odd selector functions, including those depending on both free directions.

Retain the partition \(Q_n=Q_A\times Q_B\), \(|A|=a\ge3\), free directions \(i,j\in A\), and selected \(B\)-roots \(W\). Assume opposite-layer consistency of all prescribed \(A\)-edge colors for each \(w\in W\). Suppose a single antipodally odd Boolean function \(h:Q_A\to\mathbb F_2\), now allowed to depend on **every** \(A\)-bit, satisfies: at each \(x\in Q_A\) and \(w\in W\), a monochromatic full \(B\)-geodesic of color \(h(x)\) joins \(w\) to \(\bar w\) inside the \(B\)-slice at \(x\).

Call a free direction-\(r\) antipodal edge orbit \(e\), \(r\in\{i,j\}\), *safe* when \(h\) is constant across its edge. This is a well-defined orbit property because \(h(\bar x)=1-h(x)\) gives the same derivative on antipodal edges. Let \(U_r(h)\) count unsafe orbits in free direction \(r\), and \(U=U_i+U_j\). Define the ordinary Boolean influence
\[
\operatorname{Inf}_r(h)=2^{-a}\sum_{x\in Q_A}[h(x)\ne h(x+e_r)].
\]
Then
\[
\boxed{U_r(h)=2^{a-2}\operatorname{Inf}_r(h),\qquad
U(h)=2^{a-2}(\operatorname{Inf}_i(h)+\operatorname{Inf}_j(h)).}
\tag{78}
\]

**Theorem 41 (safe-orbit clause transport).** For each \(w\in W\), let \(\Phi^{\rm safe}_{ij}(f^{(w)})\) consist of those near-monochromatic full-geodesic clauses from the induced \(A\)-coloring whose two free edge orbits are both safe. Then this entire restricted clause family embeds in \(\Phi_{ij}(c)\), up to consistent orbit-variable relabeling and complementation. Copies belonging to different \(w\)'s use disjoint full-cube free-orbit variables.

**Proof.** For each safe free antipodal orbit, the member on which \(h=0\) is well-defined because \(h\) is constant along each safe edge and reverses under antipodality. Choose that member as representative for every layer root \(w\). Consider a full \(A\)-geodesic producing a clause with both free orbits safe, and let \(t\) be its prescribed-edge color. The values \(\alpha,\beta\) of \(h\) at the two free steps are constant across those particular steps; no other free-edge invariance of \(h\) is needed. If \(\alpha\ne\beta\), the vertices immediately after the first free step and before the second have \(h\)-values \(\alpha,\beta\), so one permits a color-\(t\) \(B\)-connector between them. If \(\alpha=\beta\), the two antipodal endpoints of the full \(A\)-path have complementary \(h\)-values, so one supplies a color-\(t\) connector before or after the full \(A\)-path. This is the insertion argument from Theorem 37, now applied to the selected safe clauses only. Opposite-layer consistency preserves all prescribed \(A\)-edge colors. The chosen orbit representatives do not depend on \(w\), giving pairwise disjoint copies. \(\square\)

Call a family of full-geodesic clauses a *forcing packet* if its associated two-direction Boolean formula is inconsistent. Define \(\mathscr P(\Phi)\) to be the maximum number of forcing packets with **pairwise disjoint sets of free edge-orbit variables**. This is a stronger disjointness requirement than a matching in the parity-diamond graph: distinct parity diamonds may use the same eliminated-direction orbit in their supporting clauses.

**Theorem 42 (influence-versus-packing survival).** Write \(L_w=\mathscr P(\Phi_{ij}(f^{(w)}))\). Under the hypotheses of Theorem 41,
\[
\boxed{
\mathscr P(\Phi_{ij}(c))\ \ge\
\sum_{w\in W}\max\{0,L_w-U(h)\}.
}
\tag{79}
\]
In particular, if some \(L_w>U(h)\), every legal completion of the two free direction classes contains a monochromatic full antipodal geodesic.

**Proof.** For each \(w\), choose \(L_w\) forcing packets with disjoint free-variable supports. Each unsafe orbit belongs to the support of at most one of these packets, so deleting all packets touching an unsafe orbit removes at most \(U(h)\) packets. Every remaining packet uses only safe orbits. By Theorem 41, it embeds as an inconsistent clause packet in the full formula. Distinct safe packets are variable-disjoint, and their copies for distinct \(w\)'s are disjoint. This gives (79) and the forcing conclusion. \(\square\)

**Corollary 43 (a dimension-uniform low-influence forcing family).** Let the prescribed \(A\)-direction colors be
\[
f_k(x)=x_i,\qquad k\in A\setminus\{i,j\},
\]
where \(a\ge3\). The complete star-clause formula from Theorem 32 contains \(2^{a-3}\) orbit-disjoint four-geodesic forcing packets: one for each unordered complementary pair \(\{s,\bar s\}\) of assignments to the other \(a-2\) directions. Each packet uses one free direction-\(i\) orbit and two free direction-\(j\) orbits, and packets for different complementary pairs have disjoint supports.

Extend this partial coloring by prescribing \(c_t(x,y)=h(x)\) for every new \(B\)-direction \(t\), with any antipodally odd \(h\), and take the prescribed \(A\)-edge colors independent of \(B\). Then
\[
\boxed{
\mathscr P(\Phi_{ij}(c))\ge
2^b\max\{0,\,2^{a-3}-2^{a-2}
(\operatorname{Inf}_i(h)+\operatorname{Inf}_j(h))\}.
}
\tag{80}
\]
Thus \(\operatorname{Inf}_i(h)+\operatorname{Inf}_j(h)<1/2\) is sufficient for a monochromatic full antipodal geodesic, **even when \(h\) depends nontrivially on the two free bits**. This is a direct forcing criterion inside the given legal coloring, not merely an instruction to change its edge colors.

**Perturbation witness beyond every global odd-seam selector.** Set \(a=6\), \(i=0,j=1\), let \(f_k(x)=x_0\) for \(k=2,3,4,5\), and define
\[
\boxed{h(x)=x_2+\mathbf1_{\{x\in\{0,\mathbf1\}\}}\pmod2,}
\tag{81}
\]
where \(\mathbf1\) denotes the all-one vertex of \(Q_6\). The exceptional two-vertex set is antipodally invariant, so \(h\) is odd. The only unsafe free orbits are one in direction zero and one in direction one, giving \(U(h)=2\). The base star formula has eight mutually orbit-disjoint four-path forcing packets. Formula (80) guarantees six intact packets per \(B\)-root. Direct orbit-and-clause enumeration in \(Q_6\times Q_1\) finds that seven of the eight packets survive in each of the two opposite \(B\)-layers. The selector varies along both free directions, so Theorem 37 does not apply, but Theorem 42 still forces monochromatic full geodesics after **any** legal assignment of the two free direction classes.

**Verification.** A fresh signed-geodesic enumerator tests safe-orbit clause embedding for arbitrary sampled antipodally odd \(h\) with nonzero free-direction influences in dimensions \(Q_3\times Q_1\), \(Q_4\times Q_1\), \(Q_3\times Q_2\), \(Q_4\times Q_2\), and \(Q_5\times Q_1\), including a separate numerical check of (78). Independent complete enumeration of the star formula through \(Q_6\) checks the disjoint four-clause packets and the sparse perturbation example (81), with seven of eight packets intact in each \(B\)-layer. Reproducible certificates: https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/81521d2838a2a3d47574d2445deeaed8ab7a0665/scripts/nori_sparse_selector_verify.py and https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/6842601e3a75ccea32143de7eece3d3f26332722/scripts/nori_star_sparse_perturbation_verify.py.

**Closure implication.** The fixed-pivot and adaptive-seam approaches are no longer all-or-nothing conditions. Unsafe cross-direction variation is measured by Boolean influence, and independent geodesic forcing packets provide redundancy that can absorb it. For a universal proof, the next missing theorem would have to guarantee sufficiently many orbit-disjoint forcing packets in a given arbitrary partial coloring, or show that strong connector influence itself creates alternate forcing. Neither is established here.


## Fractional packet packing and high-influence forcing

Theorem 42 requires inconsistent packets with disjoint free orbit supports. An overlapping family offers more redundancy. For an arbitrary induced legal two-direction partial coloring \(f\), let \(\mathcal P\) be a family of inconsistent subformulas of \(\Phi_{ij}(f)\), and \(V(P)\) the free-orbit variables of packet \(P\). Choose weights \(\lambda_P\ge0\) such that
\[
\boxed{\sum_{P:e\in V(P)}\lambda_P\le1\quad\forall e.}\tag{82}
\]
Let \(L^*=\sum_P\lambda_P\).

**Theorem 44 (fractional unsafe-orbit survival).** Under Theorem 41's opposite-layer and monochromatic-connector hypotheses, let \(S\) be the free orbit set on which the odd connector selector changes. The total weight of forcing packets surviving the clause lift is at least
\[
\boxed{L^*-|S|.}\tag{83}
\]
Thus \(L^*>|S|\) guarantees a monochromatic full antipodal geodesic under every legal completion. For several eligible connector roots \(w\), apply this bound independently to their induced formulas; the resulting full-cube packet copies use disjoint variable sets.

**Proof.** Each packet that cannot be transported meets \(S\). By the union bound and the packing constraints,
\[
\sum_{P:V(P)\cap S\ne\varnothing}\lambda_P
\le\sum_{e\in S}\sum_{P:e\in V(P)}\lambda_P\le|S|.
\]
All remaining packets consist solely of safe clauses, and Theorem 41 transports them as inconsistent packets. Their survival proves the assertion. \(\square\)

More generally, if direction-\(i\) orbits have packet load at most \(\alpha_i\) and direction-\(j\) orbits have load at most \(\alpha_j\), then the surviving weight is at least
\[
\boxed{L^*-\alpha_iU_i(h)-\alpha_jU_j(h).}\tag{84}
\]

**Corollary 45 (two alternative star packets).** For the star partial coloring \(f_k(x)=x_0\), with directions \(0,1\) free, let \(L=2^{a-3}\). At every complementary pair \(\{s,\bar s\}\) of the other \(a-2\) bits, the formula of Theorem 32 contains two alternative contradictory four-clause packets. Their orbit supports are respectively
\(\{X_s,Y_s,Y_{\bar s}\}\) and \(\{X_{\bar s},Y_s,Y_{\bar s}\}\).
Assign each packet weight \(1/2\). Every \(X\)-orbit has load \(1/2\), every \(Y\)-orbit has load one, and total weight is \(L\). Hence a forcing packet survives whenever
\[
\boxed{\tfrac12U_0(h)+U_1(h)<L,}
\tag{85}
\]
equivalently
\[
\boxed{\operatorname{Inf}_0(h)+2\operatorname{Inf}_1(h)<1.}
\tag{86}
\]
This improves the previous criterion
\(\operatorname{Inf}_0(h)+\operatorname{Inf}_1(h)<1/2\).
In fact at least
\[
\boxed{\max\{0,L-U_1(h)-\lfloor U_0(h)/2\rfloor\}}
\tag{87}
\]
complementary pairs retain a packet: a pair fails only if one of its \(Y\)-orbits is unsafe, or both of its \(X\)-orbits are unsafe.

**Verified high-influence witness.** In \(Q_A=Q_6\), choose \(q(x)=[x_3=x_4=x_5]\) and
\[
\boxed{h(x)=\begin{cases}x_2,&q(x)=1,\\x_0,&q(x)=0.\end{cases}}\tag{88}
\]
This \(h\) is antipodally odd, with
\(\operatorname{Inf}_0(h)=3/4,\ \operatorname{Inf}_1(h)=0\), so \((U_0,U_1)=(12,0)\). The old influence criterion proves nothing, but (87) guarantees two surviving four-path packets in each opposite connector layer after adjoining \(Q_B=Q_1\) with its edge color \(h(x)\). Independent enumeration of every rooted full \(Q_7\)-geodesic verifies that both packets' four clauses occur in the full formula for each layer; the entire two-direction formula has 2112 clauses. The signed antipodal orbit conventions are checked separately:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/a2239cd78476f82a5dc003e50078d03ac6a157ae/scripts/nori_fractional_packet_verify.py.

This theorem applies to arbitrary induced formulas, while the worked star family exposes the power of overlapping alternative certificates. The main open difficulty persists: a selector for which every free orbit is unsafe may generate new implication paths rather than preserve existing packets. Fractional packing cannot itself infer those new constraints, so the unrestricted NORI1 conjecture remains open.


## Unsafe seam exchange as a signed two-sheet implication cover

The safe-orbit packing theorem discards every clause touching a free orbit across which the connector selector changes. A different construction retains **every** clause and traces how unsafe exchanges move it between two copies of the free orbit variables.

Let \(a\ge3\), and let \(f\) be an arbitrary legal antipodally odd partial coloring of \(Q_a\), with directions \(i,j\) free. Add one direction \(b\), prescribe the other \(A\)-edge colors by \(c_k(x,y)=f_k(x)\), and prescribe the new-direction color by
\[
\boxed{c_b(x,y)=h(x),\qquad h(\bar x)=1-h(x).}
\tag{90}
\]
The two original free direction classes remain entirely unrestricted. There is no hypothesis on \(\partial_i h\) or \(\partial_j h\).

For each free antipodal edge orbit \(e\) of \(Q_a\), select one member as representative. In the expanded cube the two orbit variables represented by this edge in new-direction layers zero and one are \(X_e^0,X_e^1\). The base variable is \(X_e\).

Consider a rooted full \(Q_a\)-geodesic \(P=(z_0,\ldots,z_a)\), with all its prescribed edges colored \(t\). Let its two free edges, in whatever traversal order, belong to orbits \(e,g\), with base forbidden colors \(p,q\). At a cut \(r\in\{0,\ldots,a\}\), the new-direction step may be inserted into \(P\). Define
\[
\delta(P,r)=[\text{the cut }r\text{ lies strictly between the two free steps}].
\]

**Theorem 46 (complete cut-voltage formula).** The complete two-direction formula of the expanded partial coloring (90) consists of all clauses forbidding
\[
\boxed{
X_e^s=p,\quad
X_g^{\,s\oplus p\oplus q\oplus\delta(P,r)}=q,
\qquad s\in\mathbb F_2,
}
\tag{91}
\]
as \(P\) ranges over the rooted full base geodesics whose prescribed edges all have a common color \(t\), and \(r\) ranges over cuts satisfying
\[
\boxed{h(z_r)=t.}
\tag{92}
\]
Every such \(P\) has at least one permissible cut, because \(h(z_a)=1-h(z_0)\).

**Proof.** Every full geodesic in \(Q_{a+1}\) projects, after deleting its unique new-direction step, to one full \(Q_a\)-geodesic \(P\), with a unique cut \(r\) and initial new-direction bit. Its prescribed \(A\)-edge colors are those of \(P\), irrespective of the new-direction bit, and its new-direction edge has color \(h(z_r)\). Hence its prescribed edges are monochromatic precisely when \(P\)'s prescribed edges all have one color \(t\) and (92) holds.

Let \(\sigma_e,\sigma_g\) indicate whether each free base edge is the selected orbit representative or its antipodal mate. The base forbidden values are \(p=t\oplus\sigma_e\) and \(q=t\oplus\sigma_g\). If the starting new-direction layer is \(u\), the sheet index of the full orbit used at a free step is
\[
u\oplus[\text{step occurs after the cut}]\oplus\sigma.
\]
Taking the difference of the two sheet indices cancels \(u\) and gives
\(\sigma_e\oplus\sigma_g\oplus\delta=p\oplus q\oplus\delta\).
Both starting-layer choices occur, giving both values of \(s\). This establishes (91), and every full geodesic arises in this construction. \(\square\)

Thus the enlarged signed implication graph is a **regular two-sheet cover** of the base implication multigraph. A rooted path together with a permissible cut gives voltage
\[
\boxed{v(P,r)=p\oplus q\oplus\delta(P,r).}
\tag{93}
\]
Each base implication arc \((e,p)\to(g,1-q)\), and its complementary reverse arc, lifts with the same sheet change \(v\). A base arc may have both voltages if different supporting paths or cuts produce them. No base arc disappears, even when every free orbit is unsafe.

## A holonomy criterion for forcing in the expanded cube

Let \(G\) be the base implication multigraph with these voltage-decorated arcs. A strongly connected component \(S\) of \(G\) is *contradictory* if it contains both signed states \((e,0)\) and \((e,1)\) for some free orbit \(e\). Such a component is invariant under the involution \((e,p)\mapsto(e,1-p)\), by contrapositive symmetry.

Call \(S\) *balanced* if every directed closed walk inside \(S\) has total voltage zero. This is equivalent to the existence of a Boolean potential \(\phi\) on its vertices satisfying
\[
\boxed{\phi(v)\oplus\phi(u)=\text{voltage}(u\to v)}
\tag{94}
\]
on every internal arc. In a balanced contradictory component, contrapositive symmetry implies that
\[
\epsilon(S)=\phi(e,0)\oplus\phi(e,1)
\tag{95}
\]
is independent of the choice of orbit \(e\) whose two states lie in \(S\).

**Theorem 47 (holonomy characterization of bad expansions).** The two-direction formula of the expanded partial coloring (90) is satisfiable if and only if **every** contradictory base component \(S\) is balanced and has
\[
\boxed{\epsilon(S)=1.}
\tag{96}
\]
In particular, a single contradictory base component with an odd-voltage closed walk forces a monochromatic full antipodal geodesic for every legal assignment of the two free direction classes. The same forcing conclusion holds for a balanced contradictory component with \(\epsilon(S)=0\).

**Proof.** The full implication graph is the two-sheet voltage cover from Theorem 46. Over a strongly connected base component, an odd-voltage closed walk joins its two sheet copies; the entire inverse image is then strongly connected, including complementary signed states of the same full-orbit variable. That violates 2-SAT satisfiability.

If instead all internal closed walks have voltage zero, choose a potential \(\phi\) satisfying (94). The inverse image separates into two strongly connected components, distinguished by the invariant \(\text{sheet}\oplus\phi(\text{base state})\). Two complementary signed states of the same full-orbit variable lie together precisely when their potential values agree, or \(\epsilon(S)=0\). They lie in different components precisely when \(\epsilon(S)=1\). Finally, any pair of complementary full-orbit signed states lying in the same enlarged strongly connected component projects to a contradictory base component. This proves both directions by the standard 2-SAT implication criterion. \(\square\)

**Corollary 48 (orbit-level parity obstruction).** If the expanded formula is satisfiable, then within every contradictory base component \(S\) there is a Boolean assignment \(\alpha_e\) to its free orbit vertices such that for every internal implication supported by a rooted path \(P\) and permissible cut \(r\),
\[
\boxed{\alpha_e\oplus\alpha_g=1\oplus\delta(P,r).}
\tag{97}
\]
Conversely the existence of such an assignment for every contradictory component implies the expanded formula is satisfiable. Thus a parity-inconsistent closed walk in the corresponding *unsigned-orbit graph with labels \(1\oplus\delta\)* forces a monochromatic full antipodal geodesic.

**Proof.** Under (96), write \(\phi(e,p)=\alpha_e\oplus p\) inside \(S\). Substituting into the implication arc \((e,p)\to(g,1-q)\) of voltage \(p\oplus q\oplus\delta\) gives (97). Conversely, from (97) set \(\phi(e,p)=\alpha_e\oplus p\). It satisfies (94) and has \(\epsilon=1\), so Theorem 47 applies. \(\square\)

**Corollary 49 (straddling-cut forcing).** Suppose a rooted near-monochromatic base path \(P\) yields an implication arc inside a contradictory base component. If it has two permissible insertion cuts \(r,r'\), with one between its free steps and the other outside, then the expanded two-direction formula is inconsistent.

**Proof.** The same base implication arc has the two different sheet voltages from (93), since \(\delta(P,r)\ne\delta(P,r')\). A directed return path exists inside the strongly connected component. Pairing it with the two arcs creates closed walks whose voltage sums differ by one. One is odd, so Theorem 47 forces inconsistency. \(\square\)

This shows why high influence can generate forcing rather than destroy it: different seam positions may give incompatible sheet transports. The relevant obstruction is not the count of unsafe orbits but whether an antipodally antisymmetric orbit potential \(\alpha\) can satisfy all their path-cut requirements simultaneously.

**Computational audit.** Independent full-geodesic enumeration in \(Q_{a+1}\) was compared clause by clause to (91) for fifteen arbitrary legal pairs \((f,h)\) when \(a=3\), twelve when \(a=4\), and four when \(a=5\). Every clause agreed. A separate independent implication-graph checker verified the equivalence (96) for 64 generated pairs when \(a=3\), 50 when \(a=4\), and ten when \(a=5\); all these examples had an odd-voltage closed walk in a contradictory base component. In addition, complete enumeration of the four possible prescribed base colorings and sixteen possible odd connector functions in \(Q_3\) confirms odd holonomy in **all 64** base-and-connector pairs. No all-dimensional theorem of unavoidable odd holonomy is asserted.

**Next closure obligation.** Prove that a hypothetical balanced contradictory base component cannot admit the orbit assignment (97) when its voltages arise from a cube coloring and an odd connector function. The finite experiments support that possibility, but abstract two-sheet covers of contradictory 2-SAT formulas can be satisfiable; the geometry of complete cube geodesics is therefore essential. Theorem 47 isolates the needed global compatibility statement rather than repeating an existence formulation of NORI1.
## Interior seam forcing criterion

**Theorem 50.** In Theorem 46, every rooted base path with prescribed edge color t has an allowed endpoint seam, since its endpoints have opposite h values. Thus every base clause has a baseline lift with voltage p xor q, and all baseline clauses are simultaneously satisfiable by assigning direction-i sheet bits X_e^s=s and direction-j sheet bits Y_f^s=1-s. A seam between the two free steps has opposite voltage p xor q xor 1.

The expanded 2-SAT formula is inconsistent if and only if a near-monochromatic rooted base path has an allowed interior seam h(z_r)=t and its associated implication arc belongs to a contradictory strongly connected component of the base implication graph.

**Proof.** Baseline implication arcs have a potential phi(e,p)=p on free direction i and phi(f,q)=1-q on free direction j; complementary signed states have opposite potentials. If an interior seam contributes an opposite-voltage arc within a contradictory base component, a baseline return path gives odd holonomy, so the lifted component contains opposite signed states. Conversely, a lifted contradictory component projects into a contradictory base component; if that component has no interior seams, every internal arc retains the baseline potential, separating opposite signed states. Thus no lifted contradiction occurs. QED.

A full base implication graph with one strongly connected component therefore needs just one allowed interior seam to force a monochromatic full antipodal geodesic. Complete Q3 base-and-seam enumeration covers 64 cases, and independent tests cover 100 Q4 and 20 Q5 random cases. The all-dimensional occurrence of such seams remains unproved.

## Connector-independent opposite-phase interior forcing

Theorem 50 identifies a permitted interior seam as the obstruction to a satisfactory two-sheet expansion. This leads to a stronger certificate that is determined entirely by the base prescribed-edge coloring and works for **every** odd connector selector.

Call a vertex \(z\in Q_a\) an *opposite-phase interior witness* if there exist rooted full base geodesics \(P_0,P_1\) whose prescribed-edge colors are respectively all zero and all one, such that \(z\) lies between their two free steps, and each path's implication arc belongs to a contradictory strongly connected component of the base implication graph.

**Theorem 52 (connector-independent two-phase forcing).** If a legal partial base coloring has an opposite-phase interior witness, then **for every** antipodally odd Boolean function \(h\) used as the added-direction edge color in (90), the expanded two-direction formula is inconsistent. Consequently every legal assignment of the two free direction classes admits a monochromatic full antipodal geodesic.

**Proof.** At the common witness vertex \(z\), the connector color \(h(z)\) is either zero or one. Choose the path \(P_{h(z)}\), whose prescribed edges all have that color. Its connector step can be inserted at \(z\), between its two free steps. The associated implication belongs to a contradictory base component, so Theorem 50 forces inconsistency. \(\square\)

### An analytic three-dimensional base instance

**Proposition 53.** Let \(a=3\), take free directions \(0,1\), and color the edges in the single prescribed direction \(2\) by an arbitrary legal odd rule \(f_2(x)=F(x_0,x_1)\). Then **every vertex** \(z\in Q_3\) is an opposite-phase interior witness.

**Proof.** For any chosen \(z\), consider the rooted full direction order \((2,0,1)\), starting at \(z+e_2+e_0\). It passes through \(z\) between the free steps, and its prescribed edge has color \(F(1-z_0,z_1)\). Next consider direction order \((2,1,0)\), starting at \(z+e_2+e_1\). It also passes through \(z\) between the free steps, and its prescribed edge has color \(F(z_0,1-z_1)\). These two inputs of \(F\) are complementary, so global antipodal oddness gives opposite prescribed colors. Finally, the base two-direction implication graph is strongly connected on all eight signed states for each of the four possible odd rules \(F\); this follows by direct enumeration of the four binary assignments to \(F(0,0),F(0,1)\). Thus both implication arcs belong to its contradictory component. \(\square\)

The result gives an elementary reason that the one-direction connector extension of any such \(Q_3\) prescribed coloring forces a full monochromatic \(Q_4\)-geodesic regardless of connector variation. This applies even when every free orbit is unsafe.

### Full four-dimensional prescribed-color census

**Computational Proposition 54.** Take an arbitrary legal antipodally odd partial coloring of \(Q_4\) with two specified free direction classes. There are eight prescribed antipodal edge-orbit bits and thus \(2^8=256\) such colorings. For each, form the complete base implication graph and count the vertices admitting both zero-phase and one-phase internal witnesses whose arcs lie inside contradictory components. The complete distribution is
\[
\boxed{
\begin{array}{c|rrr}
\#\text{witness vertices}&8&14&16\\\hline
\#\text{partial colorings}&4&48&204.
\end{array}}
\tag{101}
\]
In particular every such partial coloring has at least eight opposite-phase interior witnesses. Therefore **every legal one-direction connector extension of such a partial coloring**, for any odd connector selector \(h\), forces a monochromatic full antipodal geodesic under every assignment of the two free direction classes.

The calculation enumerates all \(16\cdot4!=384\) rooted base direction orders per prescribed coloring, constructs its signed base implication graph, identifies its contradictory components, and records the colors of the prescribed steps available at each interior vertex. This is a finite computational result, not a dimension-uniform lower bound on the witness count. In 100 sampled five-dimensional and twelve sampled six-dimensional base colorings, the respective witness counts ranged from 26 to 32, and 62 to 64. No conclusion about all higher-dimensional colorings follows from those samples.

**Closure direction.** The positive results suggest replacing the arbitrary connector-selector problem by a question entirely internal to a partial base coloring: must there be a vertex with two opposite-color interior geodesic certificates inside contradictory implication components? Establishing this for an arbitrary dimension would force every one-direction extension of the layer-independent type (90) and would give a geometric reason for the odd sheet holonomy found in the finite computations. It would still not directly cover full colorings whose prescribed old-direction edge rules depend on the added bit; that compatibility remains an independent obligation for unrestricted NORI1.


## Unrestricted opposite-layer seam intervals and two-zone clause compatibility

The preceding voltage-cover theorems assume that prescribed old-direction edge colors are independent of an added direction. An arbitrary legal antipodally odd coloring need not satisfy that assumption. The following interval theorem removes it entirely, while also identifying where a forcing contradiction must occur.

Fix a dimension \(b\) and write \(Q_n=Q_a\times Q_1\), \(a=n-1\ge2\). Keep two old directions \(i,j\) free. Prescribe every other edge orbit legally. Define the lower-facet edge colors \(f_k(x)=c_k(x,0)\), the connector colors \(h(x)=c_b(x)\), and the layer-defect function on each prescribed old-direction edge:
\[
\boxed{D_k(x)=c_k(x,0)\oplus c_k(x,1)
=1\oplus f_k(x)\oplus f_k(\bar x).}
\tag{102}
\]
Here \(\bar x\) is the antipode in \(Q_a\). Antipodal oddness makes \(h\) odd, and makes \(D_k\) antipodally even. Each \(D_k\) is constant across the edge in its own direction. Conversely, **every** antipodally even binary assignment to the old edge orbits can arise as a defect field from an arbitrary lower-facet coloring: choose \(f_k\) on one member of each lower-facet antipodal edge pair, then enforce the displayed identity on the other member. Thus no extra integrability identity on \(D\) follows merely from global antipodal oddness.

Let \(P=(z_0,\ldots,z_a)\) be any rooted full \(Q_a\)-geodesic, using old directions \(\pi_0,\ldots,\pi_{a-1}\). For each prescribed step \(q\) put
\[
\alpha_q=f_{\pi_q}(z_q),\qquad
\varepsilon_q=D_{\pi_q}(z_q).
\]
Choose initial connector-layer bit \(u\), desired prescribed-edge color \(t\), and insertion cut \(r\in\{0,\ldots,a\}\). The color of a prescribed old edge at step \(q\) in the lifted geodesic is
\[
\boxed{
\alpha_q\oplus\varepsilon_q\bigl(u\oplus[q\ge r]\bigr).
}
\tag{103}
\]

**Theorem 55 (unrestricted seam-interval theorem).** Let \(L=L(P,u,t)\) and \(R=R(P,u,t)\) be defined by
\[
\boxed{
\begin{aligned}
L&=\max\bigl(\{0\}\cup\{q+1:\varepsilon_q=1,\
\alpha_q\oplus u\oplus t=0\}\bigr),\\
R&=\min\bigl(\{a\}\cup\{q:\varepsilon_q=1,\
\alpha_q\oplus u\oplus t=1\}\bigr).
\end{aligned}}
\tag{104}
\]
If any prescribed step with \(\varepsilon_q=0\) has \(\alpha_q\ne t\), declare the interval empty. Otherwise all prescribed old edges have color \(t\) after inserting the connector if and only if
\[
\boxed{L\le r\le R.}
\tag{105}
\]
The resulting full lifted path has all its prescribed edges colored \(t\) if and only if, additionally,
\[
\boxed{h(z_r)=t.}
\tag{106}
\]
For each such cut and both choices of the initial connector layer \(u\), the two free edges induce their standard forbidden pair of projective edge-orbit variables. Taking the union over all \(P,u,t,r\) reconstructs the **entire** two-direction 2-CNF \(\Phi_{ij}\) of the original arbitrary legal partial coloring, without requiring the two facets to agree.

**Proof.** Before the seam the old steps lie in layer \(u\); after it they lie in layer \(1-u\). Substituting the defect definition gives (103). A zero-defect edge has color \(\alpha_q\) on both layers, requiring \(\alpha_q=t\). For a defective edge, requiring its color to equal \(t\) is equivalent to
\([q\ge r]=\alpha_q\oplus u\oplus t\). When the right side is zero, the seam must be after that step, \(r\ge q+1\). When it is one, \(r\le q\). Intersecting these half-intervals proves (104)--(105). The connector has color \(h(z_r)\), proving (106). Conversely every full \(Q_n\)-geodesic contains the connector direction once; deleting that step yields one such \(P\), cut and initial layer. Consequently the clause union is complete. \(\square\)

For fixed \(P,u,t\), the defect-one steps, read in traversal order and labeled by \(\alpha_q\oplus u\oplus t\), must form a nondecreasing binary word; the eligible seam positions then form one interval. When all prescribed edges are defect-free, this recovers the earlier layer-independent seam rule. When every prescribed edge has defect one, the lower-facet prescribed-color word must be monotone in one orientation. This links the unrestricted layer-coupling formula to Article XV's arbitrary-facet monotone-root programme.

### Two individually satisfiable seam-zone formulas

Let the two free steps occur at positions \(p<q\) among the old steps. Divide all near-monochromatic full-geodesic clauses into **interior** clauses (connector cut \(p<r\le q\)) and **exterior** clauses (all other cuts). Let their conjunctions be \(\Phi_{\mathrm{in}}\) and \(\Phi_{\mathrm{out}}\). A clause may belong to both families through different supporting paths; their conjunction is the full \(\Phi_{ij}\).

**Theorem 56 (unrestricted two-zone satisfiability).** For every legal prescribed coloring in any dimension,
\[
\boxed{\Phi_{\mathrm{in}}\text{ is satisfiable},
\qquad\Phi_{\mathrm{out}}\text{ is satisfiable}.}
\tag{107}
\]
Two explicit legal completions suffice:
\[
\boxed{
\begin{array}{c|cc}
&c_i(x,y)&c_j(x,y)\\
\Phi_{\mathrm{out}}\text{ model}&y&1\oplus y\\
\Phi_{\mathrm{in}}\text{ model}&y&y
\end{array}}
\tag{108}
\]
where \(y\) is the connector-layer bit.

**Proof.** Each rule (108) is independent of its own edge direction and flips under the full antipode, so defines a legal completion. An exterior path has both free steps in the same connector layer. Under the first completion their colors are \(y\) and \(1-y\), hence differ. An interior path has its two free steps in opposite connector layers. Under the second completion their colors are again different. Thus neither family alone can contain a monochromatic full geodesic under its displayed completion, giving satisfiability. \(\square\)

**Corollary 57 (mixed-zone necessity).** Every contradictory forcing packet in the two-direction formula of an arbitrary fixed coloring contains at least one interior clause and at least one exterior clause. Equivalently, any 2-SAT implication contradiction must rely on interactions between both seam zones. Under the first completion in (108), any monochromatic full antipodal geodesic must cross the connector direction *between* the free directions; under the second completion, any such geodesic must cross the connector *outside* that interval.

Unlike the previous regular two-sheet voltage argument, the interval theorem and zone decomposition make **no layer-independence assumption**. The remaining unrestricted closure question is therefore a compatibility question between two always-satisfiable clause families, with eligible seam cuts governed by the interval inequalities (104)--(106). Neither theorem claims that their union is necessarily inconsistent; that statement remains NORI1 itself.

**Reproducibility.** A standalone Python verifier constructs the full clause formula in two independent ways: enumeration of rooted full \(Q_n\)-geodesics, and the seam-interval inequalities. It separately checks the interior/exterior partition and both legal satisfying assignments. The tests cover all four legal partial colorings for \(Q_3\), all \(256\) for \(Q_4\), forty sampled \(Q_5\) partial colorings, and five sampled \(Q_6\) partial colorings. All checks pass.
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/7068128447b2fefa00deb1d86016a6f39f3535a7/scripts/nori_unrestricted_seam_intervals_verify.py.


## Projective seam-root transport and the finite two-root forcing theorem

The unrestricted seam-interval formula admits a second decomposition that is useful for locating global contradictions. Fix the connector direction \(b\), and for each \(z\in Q_{n-1}\) let \(\Phi_z\) be the subformula of \(\Phi_{ij}\) containing the clauses supported by full geodesics whose unique connector step lies over old vertex \(z\). Let \(\bar z\) denote its antipode in the old \((n-1)\)-cube.

**Theorem 58 (projective seam-root invariance).** In every dimension, for every legal partial coloring,
\[
\boxed{\Phi_z=\Phi_{\bar z}.}
\tag{109}
\]
Thus the two-direction clause formula decomposes into subformulas indexed by the \(2^{n-2}\) antipodal edge orbits of the connector direction, not by the \(2^{n-1}\) individual connector edges.

**Proof.** Apply full-cube antipodal translation to a full geodesic whose connector step lies over \(z\). Its connector step now lies over \(\bar z\), every edge color complements, and every edge stays in its original antipodal edge orbit. Therefore the two free-orbit variable assignments that make the original path monochromatic also make its antipodal translate monochromatic. If one enumerates rooted paths from only one half of the vertex set, reverse the translated path to restore the allowed rooting; edge colors and forbidden orbit assignments do not change. The construction is involutive, so both subformulas contain each other. \(\square\)

**Computational Proposition 59 (two connector orbits suffice in Q4).** Let \(Q_4\) have any prescribed legal antipodally odd colors in two direction classes, with two other direction classes left free. Choose one of the prescribed classes as the connector direction. Then:

1. The clauses from any **one** projective seam-root orbit are satisfiable.
2. There exist **two distinct** projective seam-root orbits whose combined clauses are inconsistent.

Consequently, after the two prescribed direction classes are colored, there is a selection of two antipodal connector edge orbits such that **every** legal completion of both free direction classes produces a monochromatic full antipodal geodesic crossing one of those two connector orbits. A single orbit never suffices for a forcing certificate of this type, so the minimum forcing size is two.

**Verification.** There are eight prescribed edge-orbit bits in \(Q_4\), hence \(2^8=256\) prescribed colorings. The four projective connector-root subformulas were reconstructed directly from full rooted \(Q_4\)-geodesics, and each formula and pairwise union was checked by an independent binary implication-graph satisfiability test. Each single-root formula was satisfiable in all 256 cases. The number of **incompatible unordered pairs** among the four projective roots had the complete distribution
\[
\boxed{
\begin{array}{c|rrrr}
\#\text{incompatible pairs}&2&4&5&6\\\hline
\#\text{prescribed colorings}&4&76&120&56 .
\end{array}}
\tag{110}
\]
In \(Q_3\), the analogous two-projective-root statement holds for all four prescribed colorings: each individual formula is satisfiable and their union is inconsistent.

This calculation identifies transport between two distinct connector-edge orbits as a sufficient finite forcing mechanism even when the prescribed colors on opposite layers differ arbitrarily. It does **not** establish a two-root forcing theorem in higher dimensions. In samples of forty legal \(Q_5\) partial colorings, no single projective seam-root formula was inconsistent, while many pairs were; these samples are not an all-coloring certificate.

Independent standard-library verifier:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/8176a237e2bbba3f8a82ceccc521fb85e436a2b6/scripts/nori_projective_seam_pair_census.py.

**Next global compatibility question.** Theorems 55, 56 and 58 replace an assumed layer-independent voltage cover by a collection of seam-root interval constraints in one arbitrary coloring. The two exterior/interior clause families each admit a canonical satisfying assignment, and the finite census shows that individually satisfiable projective seam-root families may jointly force a contradiction. The dimension-uniform challenge is to prove a transport contradiction between a small number of these families, rather than impose a nonexistent restriction on the defect field \(D\). NORI1 remains open.


## Affine five-cube obstruction to universal two-root forcing; a triadic closure packet

The Q4 result that two projective connector-edge orbits can always force a monochromatic full geodesic does **not** extend to Q5, even for affine legal partial colorings.

Fix free directions 0 and 1, connector direction 4, and prescribe
\[
\boxed{c_2(x)=x_1,\quad c_3(x)=1\oplus x_0,\quad c_4(x)=1\oplus x_1.}
\tag{111}
\]
These rules are undirected and antipodally odd. In canonical fixed-orbit order (directions 2,3,4; smaller lower endpoint ascending) the 24-bit mask is \`0x3355cc\`. Label the eight projective connector-step positions by \(0,1,\ldots,7\) and their clause systems by \(\Phi_z\).

**Proposition 60 (seam-root Helly number three).** Every individual \(\Phi_z\) and every pairwise conjunction \(\Phi_z\land\Phi_{z'}\) is satisfiable, but the conjunction on roots \(0,1,4\) is inconsistent. Only six rooted full geodesics suffice.

For pairwise satisfiability there are explicit 16-bit free-orbit assignments for each of the 28 pairs. Number the sixteen free orbits lexicographically by direction then canonical smaller lower endpoint. The upper triangular table provides satisfying assignment words in hexadecimal:

| \(z\backslash z'\) | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| 0 | cc44 | e80f | aaaa | aaaa | cc70 | cc44 | cc44 |
| 1 | — | e916 | 33d0 | 3bf0 | 00f0 | cc44 | cc44 |
| 2 | — | — | 3311 | 3311 | 3311 | 000f | cc07 |
| 3 | — | — | — | 3311 | 3311 | b30f | aaaa |
| 4 | — | — | — | — | 3311 | b30d | aaaa |
| 5 | — | — | — | — | — | a659 | ccf0 |
| 6 | — | — | — | — | — | — | cc44 |

Each word was checked directly against all corresponding full-geodesic clauses.

**Six-path proof.** Denote free orbit-color variables by
\(A=X_{(0,10)}, B=X_{(0,4)}, C=X_{(0,8)}, D=X_{(1,12)}, E=X_{(1,9)}\).
For each rooted path below, its three prescribed-direction edges have one common color under (111). The listed pair is the free-orbit assignment that would make that full path monochromatic and must therefore be forbidden by any bad completion.

| Path root | Direction order | Seam root | Forbidden pair |
|---:|---|---:|---|
| 11 | 0,2,1,3,4 | 4 | \(A=1,D=1\) |
| 4 | 0,2,3,1,4 | 4 | \(B=0,E=0\) |
| 10 | 0,4,3,1,2 | 4 | \(A=0,D=1\) |
| 5 | 0,4,1,2,3 | 4 | \(B=1,E=0\) |
| 1 | 3,0,2,1,4 | 1 | \(C=0,D=0\) |
| 15 | 2,1,0,3,4 | 0 | \(C=1,E=1\) |

Avoiding both first and third forbidden pairs forces \(D=0\). Avoiding both second and fourth forces \(E=1\). The fifth then forces \(C=1\), but the sixth forces \(C=0\). Contradiction. Every one of the six clauses is essential to this displayed packet. All 28 pairwise root unions remain satisfiable by the witnesses above, so all three root systems are needed.

**Theorem 61 (triadic bridge-fork rule).** The preceding six-clause pattern is an unrestricted dimension-uniform sufficient forcing criterion: whenever three seam-root families support four clauses forcing \(D=0,E=1\) and two further clauses respectively forbidding \(C=0,D=0\) and \(C=1,E=1\), every completion contains a monochromatic full geodesic. This is a local-to-global **three-root** forcing operation, not a theorem asserting that every coloring possesses the pattern.

**Computational Proposition 62 (complete affine Q5 classification).** Among the \(16^3=4096\) legal affine assignments to the three prescribed direction classes in Q5, precisely 4080 have some inconsistent pair of seam-root systems; the remaining 16 have every pair satisfiable but at least one inconsistent triple. Those 16 are precisely
\[
\boxed{
c_2=x_u\oplus a,\quad
c_3=x_{1-u}\oplus b,\quad
c_4\in\{1\oplus c_2,\ 1\oplus c_3\},
\qquad u,a,b\in\mathbb F_2.
}
\tag{112}
\]
The affine census builds 1920 rooted projective full geodesics, runs the two-direction implication-graph test for all root pairs, and tests triples for all 16 exceptions. Its source is
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/ca778e150b205fc21dbfe4d987ca50461157a643/scripts/nori_q5_affine_seam_helly_census.cpp.
An independent Python audit checks the 28 satisfying assignments and each of the six forcing paths:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/d8fc9f576913de1e188e18f27c9167cd3cd2ce31/scripts/nori_q5_three_root_seam_certificate.py.

**Research consequence.** The proposed universal two-root principle is refuted already by an affine coloring. Any higher-dimensional seam-root compatibility proof must admit cooperation among at least three separately satisfiable root systems. The six-path triadic rule exhibits one positive mechanism, but neither a universal three-root bound nor unrestricted NORI1 follows from the finite computations.


## Two seam-disjoint triadic forcing packets and robust connector-orbit avoidance

The affine \(Q_5\) partial coloring (111) has more robust three-root forcing than Proposition 60 alone states. Its eight projective connector-step roots admit twenty inconsistent triples out of the \(\binom83=56\) possible triples; every one-root and two-root union is satisfiable. In particular, the two triples
\[
\boxed{T_1=\{0,1,4\},\qquad T_2=\{3,6,7\}}
\tag{113}
\]
are disjoint and each admits a six-geodesic contradictory packet.

Proposition 60 exhibits the six-geodesic packet on \(T_1\). For \(T_2\), set
\[
A'=X_{(0,2)},\quad B'=X_{(0,4)},\quad C'=X_{(0,0)},
\quad D'=X_{(1,4)},\quad E'=X_{(1,5)}.
\]
The second packet is:

| Root | Full direction order | Seam root | Forbidden free-orbit assignment |
|---:|---|---:|---|
| 3 | \(0,2,1,3,4\) | 3 | \(A'=1,D'=1\) |
| 9 | \(2,3,0,1,4\) | 6 | \(B'=0,D'=0\) |
| 0 | \(0,2,1,4,3\) | 7 | \(C'=0,E'=0\) |
| 3 | \(2,1,0,3,4\) | 3 | \(B'=1,E'=1\) |
| 2 | \(0,4,3,1,2\) | 3 | \(A'=0,D'=1\) |
| 1 | \(0,3,4,1,2\) | 7 | \(C'=1,E'=0\) |

The first and fifth clauses force \(D'=0\); the third and sixth force \(E'=1\). The second clause then forces \(B'=1\), whereas the fourth forces \(B'=0\). Thus this second six-path packet is inconsistent for every assignment of the two free direction classes, independently of the first packet.

**Corollary 63 (robust connector-orbit avoidance in the affine obstruction).** For the fixed prescribed colors (111), for **every** legal completion of free directions \(0,1\), and for **every** prescribed antipodal edge orbit \(e\) in connector direction \(4\), there is a monochromatic full antipodal geodesic avoiding \(e\). More strongly, a predetermined packet of at most six full rooted geodesics, all avoiding \(e\), guarantees a monochromatic witness under **every** legal completion of the free direction classes.

**Proof.** The connector orbit \(e\) belongs to at most one of the disjoint projective seam-root sets \(T_1,T_2\). Choose the forcing packet belonging to the other set. Each of its six full paths crosses direction \(4\) at a seam root different from \(e\), hence avoids that antipodal orbit. One of the six is monochromatic under every legal free-direction assignment, by the two triadic contradictions above. \(\square\)

This is a positive robustness statement for the same affine partial coloring that refutes universal two-root forcing. It demonstrates that a failed low-Helly-number assertion does **not** imply fragility under connector-orbit flips. Any full NORI1 proof based on critical flips must account for such redundant multi-root forcing networks, rather than expecting one or two seam-root groups to be universally sufficient.

Direct complete-path verification of both packets, their disjoint seam-root sets, the 28 satisfying pair assignments, and all Boolean cases for their six clauses:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/a246800447a8c7548c9fb31f4bcaa8781d511d0a/scripts/nori_q5_three_root_seam_certificate.py.
