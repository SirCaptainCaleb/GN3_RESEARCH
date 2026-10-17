# Projective two-turn incidence, Fourier kernel rigidity, and the five-cube theorem

# Projective two-turn incidence, Fourier kernel rigidity, and the five-cube theorem

Let \(n\ge5\). A legal edge coloring of \(Q_n\) consists of bits \(c_i(x)\) satisfying \(c_i(x+e_i)=c_i(x)\) and \(c_i(\bar x)=1-c_i(x)\). Write \([x]=\{x,\bar x\}\). A **projective turn** is a pair \(t=([x],\{i,j\})\), with \(i\ne j\); its color-change indicator is
\[
I_t=\mathbf1_{\{c_i(x)\ne c_j(x)\}}.
\]
This is independent of the representative of \([x]\). A coherent support is the projective \(n\)-cycle obtained from an antipodal full geodesic by identifying antipodal edges. Its successive direction labels are all different. Write \(\mathcal O_n\) for these supports, \(M=|\mathcal O_n|=2^{n-2}(n-1)!\), and \(A\) for the \(\{0,1\}\)-incidence matrix whose rows are supports and columns are projective turns. If \(T_c(O)\) denotes the number of cyclic color transitions on the lifted \(2n\)-cycle, then
\[
T_c(O)=2(AI)_O,\qquad T_c(O)\in 2+4\mathbb Z_{\ge0}.
\tag{1}
\]
The congruence follows because the length-\(2n\) color word is antiperiodic.

## The two-turn incidence formula

**Theorem 1.** Let \(t=([x],\{i,j\})\) and \(u=([y],\{k,l\})\) be projective turns, and let \(N(t,u)=(A^\top A)_{t,u}\). For \(n\ge3\), the following exhaust the possibilities.

* If \(t=u\), then \(N(t,u)=(n-2)!\).
* If \(t\ne u\) and \([x]=[y]\), then \(N(t,u)=0\).
* If the direction pairs have one common member \(h\), then \(N(t,u)=(n-3)!\) when \([y]=[x+e_h]\), and \(N(t,u)=0\) otherwise.
* Suppose \(i,j,k,l\) are distinct. Put \(d=x+y\) in \(\mathbb F_2^n\). If \(d_i=d_j\) or \(d_k=d_l\), then \(N(t,u)=0\). Otherwise let \(B\) be the unique set among \(\operatorname{supp}(d)\) and its complement with \(j\in B\) and \(i\notin B\). Then
\[
\boxed{N(t,u)=(|B|-2)!(n-|B|-2)!.}
\tag{2}
\]

**Proof.** Fix the lift \(x\) of the first projective vertex and orient the support so its first direction is \(j\) and last direction is \(i\). Supports through \(t\) correspond bijectively to permutations of the remaining \(n-2\) directions; this gives the diagonal count. A projective support is a simple cycle, hence two distinct turns at one projective vertex cannot coexist.

A direction occurs once on a projective support. If it occurs in both turns, those turns must be the endpoints of that direction's projective edge; fixing their adjacent positions leaves \((n-3)!\) permutations.

For four different directions, a second projective vertex reached from \(x\) after the initial segment of the rooted order corresponds to a proper prefix set \(B\) with \(j\in B\), \(i\notin B\). Equality of that vertex with \([y]\) means that \(B\) is one of \(\operatorname{supp}(d)\) and its complement, which is possible precisely when \(d_i\ne d_j\). For the turn at \(y\) to involve \(k,l\), these directions must lie on opposite sides of the prefix, equivalently \(d_k\ne d_l\). One specified member of \(\{k,l\}\) must terminate the permutation of \(B\setminus\{j\}\), and the other must begin the permutation of \(B^c\setminus\{i\}\). The independent orders of their remaining members have respectively \((|B|-2)!\) and \((n-|B|-2)!\) possibilities. \(\square\)

Consequently the second moment is a quadratic expression entirely in incident edge colors:
\[
\boxed{\mathbb E_{O}T_c(O)^2=
\frac4M\sum_{t,u}N(t,u)I_tI_u.}
\tag{3}
\]
The sum is over ordered pairs of projective turns.

## Complete real kernel of projective turn incidence

**Theorem 2 (turn-incidence kernel).** For \(n\ge5\), a real weighting \(f_{ij}([x])=f_{ji}([x])\) of projective turns satisfies
\[
\sum_{t\in O}f_t=0\quad\text{for every }O\in\mathcal O_n
\tag{4}
\]
if and only if there are constants \(a_i\) with \(\sum_i a_i=0\), and real functions \(g_i\) on projective vertices satisfying \(g_i([x+e_i])=-g_i([x])\), such that
\[
\boxed{f_{ij}([x])=a_i+a_j+g_i([x])+g_j([x]).}
\tag{5}
\]
In particular,
\[
\boxed{\dim_{\mathbb R}\ker A=n2^{n-2}+n-1,\qquad
\operatorname{rank}_{\mathbb R}A=
2^{n-1}\binom n2-n2^{n-2}-(n-1).}
\tag{6}
\]

**Proof.** The characters \(\chi_S(x)=(-1)^{\sum_{i\in S}x_i}\) of even cardinality \(S\subseteq[n]\) form a Fourier basis on the projective vertex group. Expand
\[
f_{ij}([x])=\sum_{|S|\ {\rm even}}\chi_S(x)b_{ij}(S).
\]
For a cyclic ordering \(\pi=(\pi_1,\ldots,\pi_n)\), set \(\pi_0=\pi_n\). The projective turns based at the prefixes \(x+\sum_{r\le k}e_{\pi_r}\), \(0\le k<n\), are \((\pi_k,\pi_{k+1})\). Requiring (4) at every translated root and taking Fourier coefficients gives, for each even \(S\),
\[
\sum_{k=0}^{n-1}
(-1)^{|S\cap\{\pi_1,\ldots,\pi_k\}|}
b_{\pi_k,\pi_{k+1}}(S)=0
\quad\text{for every }\pi.
\tag{7}
\]
Suppress \(S\) and put \(s_i=\mathbf1_{\{i\in S\}}\). Compare a direction order containing four consecutive distinct entries \(h,a,b,k\) to the order with \(a,b\) exchanged. Cancellation of all unchanged turns in (7) gives
\[
b_{ha}-b_{hb}
+\big((-1)^{s_a}-(-1)^{s_b}\big)b_{ab}
+(-1)^{s_a+s_b}(b_{bk}-b_{ak})=0.
\tag{8}
\]
The labels \(h,k\) may be any two distinct labels outside \(\{a,b\}\).

If \(S=\varnothing\) or \(S=[n]\), all signs \(s_i\) agree and (8) becomes
\(b_{ha}-b_{hb}=b_{ka}-b_{kb}\).
As there are at least three labels outside each \(\{a,b\}\), the standard four-point additive identity follows: \(b_{ij}=v_i+v_j\) for some real \(v_i\). In the empty-set mode, (7) then gives \(2\sum_i v_i=0\). In the full-set mode (which is present only when \(n\) is even), (7) vanishes for every additive weighting, since the sign reverses at each dimension.

Now suppose \(\varnothing\ne S\ne[n]\). Choose \(a\in S\), \(b\notin S\). Equation (8) reads
\[
(b_{ha}-b_{hb})+(b_{ka}-b_{kb})=2b_{ab}.
\]
With at least three other labels, this forces
\[
b_{va}-b_{vb}=b_{ab}\qquad(v\notin\{a,b\}).
\tag{9}
\]
Fix one \(b_0\notin S\) and set \(v_a=b_{a b_0}\) for \(a\in S\), \(v_b=0\) for \(b\notin S\). Equation (9) first gives \(b_{aa'}=v_a+v_{a'}\) for \(a,a'\in S\). For distinct \(b,b'\notin S\), applying (9) to the mixed pairs \((a,b)\) and \((a,b')\) gives
\(b_{ab'}-b_{bb'}=b_{ab}\) and \(b_{ab}-b_{bb'}=b_{ab'}\). Thus \(b_{bb'}=0\) and \(b_{ab}=v_a\), independently of \(b\notin S\). The same conclusion holds when there is only one outside label. Hence
\[
b_{ij}(S)=v_i(S)+v_j(S),\qquad v_i(S)=0\quad(i\notin S).
\tag{10}
\]
Conversely these Fourier weightings satisfy (7): every \(v_i(S)\) with \(i\in S\) occurs at the two turns incident with the \(i\)-edge with opposite Fourier signs. The empty mode satisfies (7) precisely when the constants sum to zero.

Reassembling the Fourier modes gives (5), where the nonconstant modes of \(g_i\) all contain \(i\), equivalently \(g_i([x+e_i])=-g_i([x])\). Conversely each \(g_i\) cancels across its projective edge on every support, and the constant terms contribute \(2\sum_i a_i=0\).

For each \(i\), the anti-invariant functions under translation by \(e_i\) have dimension \(2^{n-2}\) on the projective vertex group. The constant \(a_i\) have dimension \(n-1\). For \(n\ge3\), the map sending \((a_i+g_i)_i\) to the pair sums in (5) is injective, since all pair sums of \(n\) real numbers determine those numbers. This proves (6). \(\square\)

**Corollary 3 (local four-direction constraint).** Every \(f\in\ker A\) satisfies, at every projective vertex and for every four distinct directions,
\[
\boxed{f_{ij}+f_{kl}-f_{ik}-f_{jl}=0.}
\tag{11}
\]
This gives an explicit local obstruction to constant support sums.

## Rigidity of constant turn energy

**Theorem 4.** In every dimension \(n\ge5\), if a legal coloring has the same cyclic turn energy \(T_c(O)=\tau\) on all coherent supports, then \(\tau=2\). Consequently every coherent support contains a monochromatic full antipodal geodesic.

**Proof.** The constant-one turn weighting has support sum \(n\). Thus
\[
f_{ij}([x])=I_{ij}([x])-\frac{\tau}{2n}
\]
belongs to \(\ker A\). By Corollary 3 the unlike-color indicators \(I_{ij}([x])\) satisfy the local four-direction identity (11). If at a vertex at least two incident edges have each color, choose distinct \(i,j\) of color zero and \(k,l\) of color one. Then
\[
I_{ij}+I_{kl}-I_{ik}-I_{jl}=0+0-1-1=-2,
\]
a contradiction. Therefore the number \(r(x)\) of color-one incident edges belongs to \(\{0,1,n-1,n\}\) at every vertex.

For completeness, each projective turn lies on \((n-2)!\) coherent supports, and the number of unlike-color turns at \([x]\) is \(r(x)(n-r(x))\). Counting turn incidences and using \(M=2^{n-2}(n-1)!\) gives
\[
\mathbb E_O T_c(O)=
\frac{4}{n-1}\mathbb E_x r(x)(n-r(x)).
\tag{12}
\]
The permitted values of \(r(x)\) imply \(r(x)(n-r(x))\le n-1\), whence \(\tau\le4\). By (1), \(\tau\) is a positive integer congruent to \(2\pmod4\); therefore \(\tau=2\). The equivalence between two transitions and a monochromatic half-cycle proves the assertion. \(\square\)

**Corollary 5 (NORI1 in dimension five).** Every legal antipodally odd edge coloring of \(Q_5\) has a monochromatic full antipodal geodesic.

**Proof.** In odd dimension the signed vertex-star sum \(S(x)=\sum_i(-1)^{c_i(x)}\) is odd, hence \(S(x)^2\ge1\). Equation (12), together with \(S=n-2r\), yields
\[
\mathbb E_O T_c(O)=\frac{n^2-\mathbb E_x S(x)^2}{n-1}
\le n+1.
\]
For \(n=5\) this mean is at most \(6\). If no support contained a monochromatic full geodesic, (1) would give \(T_c(O)\ge6\) on every support. Every support would therefore have energy \(6\), contradicting Theorem 4. \(\square\)

## Quantitative variance consequence

Let \(m(c)\) count projective vertices at which both colors occur at least twice. Let \(\lambda_n>0\) denote the smallest positive eigenvalue of the explicitly determined matrix \(A^\top A=(N(t,u))\). Then for \(n\ge5\),
\[
\boxed{\operatorname{Var}_O(T_c(O))\ge
\frac{4\lambda_n}{2^{n-2}(n-1)!}\,m(c).}
\tag{13}
\]
Indeed, at each such vertex choose two directions of each color. The four-turn vector \(L=e_{ij}+e_{kl}-e_{ik}-e_{jl}\) has norm \(2\), annihilates the kernel by (11), and has inner product \(-2\) with \(I\). The vectors \(L/2\) at different projective vertices are orthonormal. If \(P\) is orthogonal projection onto \((\ker A)^\perp\), Bessel's inequality gives \(\|PI\|^2\ge m(c)\). Since \(T=2AI\), \(\operatorname{Var}(T)=4\|A(I-\frac{\mathbb E T}{2n}\mathbf1)\|^2/M\); the spectral lower bound proves (13).

A stronger, degree-explicit variance bound holds. Put \(s(x)=n-r(x)\) and
\[
D_n(r)=\frac{2r(n-r)\big(r(n-r)-(n-1)\big)}{(n-1)(n-2)}.
\]
Then
\[
\boxed{\operatorname{Var}_O(T_c(O))
\ge\frac{4\lambda_n}{M}\sum_{[x]}D_n(r(x)).}
\tag{17}
\]
To prove this, view the turn indicators at one projective vertex as a vector in \(\mathbb R^{\binom n2}\). The subspace of pair-additive vectors \(v_{ij}=z_i+z_j\) is the image of the unsigned vertex-edge incidence matrix \(B\) of \(K_n\), whose Gram matrix is \(B^\top B=(n-2)I+J\). For a color split of sizes \(r,s=n-r\), the turn indicator has squared norm \(rs\), while its image under \(B^\top\) has \(r\) entries equal to \(s\) and \(s\) entries equal to \(r\). Orthogonal projection gives squared distance
\[
rs-\frac{rs\,n-2r^2s^2/(n-1)}{n-2}=D_n(r).
\]
Every member of \(\ker A\) is pair-additive at each projective vertex by Theorem 2. Thus the squared distance from \(I\) to \(\ker A\) is at least \(\sum_{[x]}D_n(r(x))\). The same spectral estimate used for (13) proves (17). In particular \(D_n(r)>0\) precisely when both colors occur at least twice at that vertex.

If no monochromatic support exists, \(6\le T_c(O)\le2n\). For \(\mu=\mathbb E T_c(O)\), the elementary bounded-variance inequality gives \(\operatorname{Var}(T_c)\le(2n-\mu)(\mu-6)\). Therefore the following sufficient condition applies to every legal coloring:
\[
\boxed{\frac{4\lambda_n}{M}m(c)>(2n-\mu)(\mu-6)
\quad\Longrightarrow\quad\text{a monochromatic full antipodal geodesic exists}.}
\tag{14}
\]
The kernel theorem and the five-cube conclusion require no spectral numerical approximations. The higher-dimensional implication of (14) depends on the coloring's star data.

## Finite verification

An independent exhaustive support enumerator checked (2) on all unordered turn pairs in dimensions \(3,4,5,6\): respectively \(78,1176,12880,115440\) pairs, with support counts \(4,24,192,1920\). The first and second moments were also compared against direct cyclic-energy evaluation for three independently sampled legal colorings in each dimension. Numerical real-rank checks found \(\operatorname{rank} A=116\) for \(n=5\) and \(379\) for \(n=6\), agreeing with (6). These checks are supplementary to the proofs above.

## A uniform three-support theorem in the five-cube

**Theorem 6.** Every legal edge coloring of \(Q_5\) has at least five distinct coherent supports containing monochromatic full antipodal geodesics. More precisely, let \(b\) be the number of projective vertices where \(r(x)\notin\{2,3\}\). If \(b>0\), there are at least \(6b\) such supports; if \(b=0\), there are at least five.

**Proof.** There are \(192\) coherent supports and \(16\) projective vertices. The only possible energies are \(2,6,10\); let their multiplicities be \(a,d,h\). At a balanced projective vertex, \((5-2r)^2=1\), while at each of the \(b\) other vertices it is at least \(9\). Thus the first-moment identity gives
\[
\mu=\mathbb E T_c(O)\le 6-b/8.
\]
Since \(\mu=6+4(h-a)/192\), we have \(a-h\ge6b\), and hence \(a\ge6b\). This settles \(b>0\).

Suppose \(b=0\). Then \(\mu=6\), \(a=h\), and \(\operatorname{Var}(T_c)=32a/192\). The spectrum of the turn Gram matrix can be found directly from Theorem 1 using Fourier transform over the projective vertex group. For any even \(S\subseteq[5]\), let the \(10\times10\) Fourier block be
\[
K_S(P,Q)=\sum_{[y]}(-1)^{\sum_{i\in S}y_i}\,
N(([0],P),([y],Q)),
\qquad P,Q\in\binom{[5]}2.
\tag{15}
\]
The symmetric-group action shows that its eigenvalues depend only on \(|S|\). Substitution of (2) and computation of the three characteristic polynomials give the following eigenvalue multisets:
\[
\begin{array}{c|l}
|S|&\operatorname{spec}(K_S)\\ \hline
0& 0^{(4)},\,6^{(5)},\,30\\
2&0^{(2)},\,6^{(2)},\,10-4\sqrt5,\,10+4\sqrt5,\,
(7-\sqrt{17})^{(2)},\,(7+\sqrt{17})^{(2)}\\
4&0^{(4)},\,6^{(3)},\,14^{(3)}
\end{array}
\tag{16}
\]
Here superscripts in parentheses denote multiplicities. These are characteristic-polynomial computations of matrices defined by the finite integer formula (2); no assumption about the coloring enters. Thus
\(\lambda_5=10-4\sqrt5>1\).
All \(16\) projective vertices have \(r(x)\in\{2,3\}\), hence \(D_5(r(x))=2\). Applying the stronger bound (17) gives
\[
\frac{32a}{192}=\operatorname{Var}(T_c)
\ge \frac{4\lambda_5\cdot32}{192}.
\]
Therefore \(a\ge4\lambda_5>4\); since \(a\) is an integer, \(a\ge5\). \(\square\)

The Fourier spectra in (16) may also be verified by forming the three \(10\times10\) integer matrices from (15), computing their characteristic polynomials over \(\mathbb Z\), and factoring them over \(\mathbb Q(\sqrt5,\sqrt{17})\).

## Incidence of arbitrary finite families of projective turns

**Theorem 7 (nested-prefix factorial extension).** Fix \(n\ge3\) and a finite set \(U=\{t_0,t_1,\dots,t_m\}\) of distinct projective turns, with \(t_0=([x],\{i,j\})\). The number
\[
N(U)=|\{O\in\mathcal O_n:U\subseteq O\}|
\]
is determined as follows. Take the orientation at \([x]\) whose last dimension is \(i\) and first dimension is \(j\). For each \(t_h=([y_h],\{a_h,b_h\})\), \(h\ge1\), put \(d_h=x+y_h\). If \([y_h]=[x]\), or if \((d_h)_i=(d_h)_j\), put \(N(U)=0\). Otherwise there is a unique set \(B_h\) among \(\operatorname{supp}(d_h)\) and its complement containing \(j\) and omitting \(i\). If \(|B_h\cap\{a_h,b_h\}|\ne1\), put \(N(U)=0\). Write \(\alpha_h\) for the unique member of \(B_h\cap\{a_h,b_h\}\), and \(\beta_h\) for the other member.

If the distinct sets \(B_h\) cannot be ordered as a strict inclusion chain, put \(N(U)=0\). Otherwise relabel so that
\[
\varnothing=B_0\subsetneq B_1\subsetneq\cdots\subsetneq B_m
\subsetneq B_{m+1}=[n].
\]
Set \(\beta_0=j,\alpha_{m+1}=i\), and \(C_h=B_h\setminus B_{h-1}\) for \(1\le h\le m+1\). Define
\[
F(C;p,q)=
\begin{cases}
1,&|C|=1,\ p=q\in C,\\
(|C|-2)!,&|C|\ge2,\ p\ne q,\ p,q\in C,\\
0,&\text{otherwise}.
\end{cases}
\]
Then
\[
\boxed{N(U)=\prod_{h=1}^{m+1}F(C_h;\beta_{h-1},\alpha_h).}
\tag{18}
\]
For \(m=0\), formula (18) gives \(N(\{t_0\})=(n-2)!\).

**Proof.** Every coherent support containing \(t_0\) has a unique rooted direction order
\[
(j,p_2,\ldots,p_{n-1},i)
\]
whose projective root is \([x]\), whose outgoing dimension is \(j\), and whose incoming dimension is \(i\). This establishes a bijection with permutations of the remaining \(n-2\) dimensions. The projective vertex reached after a proper prefix \(B\) of this order is \([x+\mathbf1_B]\), and every such prefix includes \(j\) and excludes \(i\). The prescribed second vertex \([y_h]\) can therefore occur only at the uniquely selected \(B_h\), which exists precisely when \((d_h)_i\ne(d_h)_j\). At that vertex, the incident direction labels are the final dimension of \(B_h\) and the initial dimension outside \(B_h\). These must be respectively \(\alpha_h,\beta_h\). Distinct prescribed turns cannot occur at the same projective vertex; thus all \(B_h\) must form a strict chain. The intervening blocks \(C_h\) independently permute their dimension labels, with initial member \(\beta_{h-1}\) and terminal member \(\alpha_h\). Their counts are \(F(C_h;\beta_{h-1},\alpha_h)\); multiplying proves (18). \(\square\)

For any legal coloring and \(X_c(O)=T_c(O)/2=\sum_{t\in O}I_t(c)\), this theorem gives every factorial moment:
\[
\boxed{
\mathbb E_O\binom{X_c(O)}k
=\frac1{|\mathcal O_n|}
\sum_{\substack{U\subseteq\mathcal T_n\\|U|=k}}
N(U)\prod_{t\in U}I_t(c).
}
\tag{19}
\]
Here \(\mathcal T_n\) denotes the projective-turn set. In particular, the cubic turn moment is obtained by the \(k=1,2,3\) cases of (19), and every summand is determined by the original edge colors and factorial block multiplicities. This supplies the third-order incidence geometry without a support-by-support expansion.

## Seven-dimensional spectral calculation

For \(n=7\), the Gram matrix \(A^\top A\) decomposes under Fourier transform in the projective vertex variable into \(21\times21\) blocks \(K_S\), with \(|S|\) even. Writing \(z\) for the characteristic-polynomial variable, the four representative characteristic polynomials are
\[
\begin{aligned}
|S|=0:&\quad z^6(z-840)(z-120)^{14};\\
|S|=2:&\quad z^2(z-120)^4(z-88)^5
 (z^2-480z+20160)(z^2-280z+15360)^4;\\
|S|=4:&\quad z^4(z-312)(z-216)^2(z-120)^9(z-72)
 (z^2-312z+18432)^2;\\
|S|=6:&\quad z^6(z-264)(z-184)^9(z-120)^5.
\end{aligned}
\tag{20}
\]
Each polynomial follows by evaluating (2) on projective vertex differences, Fourier-transforming, and factoring the integer characteristic polynomial. Consequently
\[
\boxed{\lambda_7=240-24\sqrt{65}>0.}
\tag{21}
\]
The nullities sum to \(6+21\cdot2+35\cdot4+7\cdot6=230\), agreeing with (6).

For a legal coloring of \(Q_7\) whose vertex degrees are \(3\) or \(4\), one has \(D_7(r)=24/5\) at every one of the \(64\) projective vertices. Thus (17) specializes to
\[
\boxed{\operatorname{Var}_O(T_c(O))
\ge\frac4{75}(240-24\sqrt{65})\approx2.480310.}
\tag{22}
\]
This inequality is substantially below the variance \(36/5\) exhibited by the balanced coloring in the associated research note, and therefore does not by itself force a two-transition support in dimension seven.


## A maximally balanced binomial-square energy law

**Theorem 8 (balanced binomial-square turn distribution).** For each integer \(m\ge1\), put \(n=2m+1\) and partition the dimensions \(\{1,\ldots,2m\}=A\sqcup B\), with \(|A|=|B|=m\) and \(1\in B\). Define
\[
c_0(x)=x_1,\qquad c_i(x)=x_0\ (i\in A),\qquad
c_i(x)=1+x_0\ (i\in B).
\tag{23}
\]
Then the coloring is antipodally odd and has color-one vertex degree \(r(x)=m+x_1\). Its cyclic turn-energy distribution is
\[
\boxed{\Pr_{O\in\mathcal O_n}\bigl(T_c(O)=2+4j\bigr)
=\frac{\binom mj^2}{\binom{2m}m}\quad(0\le j\le m).}
\tag{24}
\]
Consequently
\[
\boxed{\mathbb E T_c=n+1,\qquad
\operatorname{Var}(T_c)=\frac{4m^2}{2m-1},\qquad
\Pr(T_c=2)=\binom{2m}m^{-1}.}
\tag{25}
\]

**Proof.** Every \(c_i\) is independent of its own dimension and changes when all vertex bits are complemented. Precisely \(m\) of the \(2m\) nonzero-direction edges have color one at every vertex, so \(r(x)=m+x_1\).

Root a uniform coherent support at its projective edge in direction \(0\), oriented with dimension \(0\) first. Every support has four rooted direction-order representatives with this property, so the resulting rooted orders are uniformly distributed. The remaining \(2m\) dimensions occur in a uniform random order. After traversing direction \(0\), their color word \(w=(w_1,\ldots,w_{2m})\) contains \(m\) zeros and \(m\) ones; all \(\binom{2m}m\) such words are equally likely. The color \(b\) of direction \(0\) is an independent uniform bit, by variation of starting vertex bit \(x_1\). Extend the word to \((b,w_1,\ldots,w_{2m},1-b)\). The number \(X=T_c/2\) of changing projective turns is the number of adjacent changes in this extended word.

Since the endpoints are opposite, \(X=2j+1\) precisely when the extended word has \(j+1\) runs of each color. For fixed \(b\), it contains \(m+1\) occurrences of each bit. The positive run lengths of either color form ordered compositions of \(m+1\) into \(j+1\) parts, counted by \(\binom mj\). Independently choosing both sets of run lengths gives \(\binom mj^2\) words producing \(X=2j+1\), proving (24).

The variable \(J=(T_c-2)/4\) has the hypergeometric distribution of the intersection size of two uniform \(m\)-element subsets of a \(2m\)-element set. Thus \(\mathbb EJ=m/2\) and \(\operatorname{Var}J=m^2/[4(2m-1)]\), proving (25). \(\square\)

The proportion of coherent supports carrying a monochromatic full antipodal geodesic can therefore be as small as
\[
\binom{2m}m^{-1}\sim\frac{\sqrt{\pi m}}{4^m}
\]
while all vertex stars are maximally balanced.


## Zero-frequency turn spectrum and a dimension-uniform witness certificate

Let \(n\ge3\). For every unordered pair \(P=\{i,j\}\subset[n]\) put
\[
p_P=\mathbb E_{[x]}\mathbf1_{\{c_i(x)\ne c_j(x)\}}.
\]
The expectation ranges over \(2^{n-1}\) projective vertices; because the indicator is antipodally invariant, the same number is obtained by averaging over all cube vertices. Let \(B\) be the \(\binom n2\times n\) unsigned pair–dimension incidence matrix, \(B_{P,i}=\mathbf1_{\{i\in P\}}\). Write \(J\) for the all-ones \(\binom n2\times\binom n2\) matrix.

**Theorem 9 (complete zero-frequency Gram spectrum).** The zero-frequency Fourier block of the projective turn Gram matrix \(A^\top A\) is
\[
\boxed{K_\varnothing=(n-3)!\big((n-2)I-BB^\top+2J\big).}
\tag{26}
\]
Its eigenvalues, with multiplicities, are
\[
\boxed{
n(n-2)(n-3)!\ (1),\quad
0\ (n-1),\quad
(n-2)!\ \left(\frac{n(n-3)}2\right).
}
\tag{27}
\]
The last multiplicity is zero at \(n=3\).

**Proof.** By translation invariance, the matrix entry \(K_\varnothing(P,Q)\) is the total number of coherent supports containing the turn at \([0]\) with dimension pair \(P\) and another turn with dimension pair \(Q\), summed over its projective vertex. The two-turn incidence theorem gives \((n-2)!\) when \(P=Q\), and \((n-3)!\) when \(|P\cap Q|=1\): in the latter case the second vertex is the other endpoint of the shared projective edge.

For disjoint pairs \(P,Q\), orient the first turn with incoming dimension \(i\), outgoing dimension \(j\). A compatible projective second vertex corresponds to a prefix \(D\subset[n]\) with \(j\in D\), \(i\notin D\), and precisely one member of \(Q\) in \(D\). If \(|D|=b\), there are \(2\binom{n-4}{b-2}\) such prefixes, each admitting \((b-2)!(n-b-2)!\) supports. Therefore
\[
K_\varnothing(P,Q)
=2\sum_{b=2}^{n-2}\binom{n-4}{b-2}(b-2)!(n-b-2)!
=2(n-3)!.
\]
For \(n=3\), disjoint pairs do not occur. The three cases yield (26), since \(BB^\top\) has diagonal \(2\), off-diagonal \(1\) for pairs sharing a dimension, and \(0\) otherwise.

Now \(B^\top B=(n-2)I+J_n\), where \(J_n\) is the \(n\times n\) all-ones matrix. The pair-space decomposes orthogonally into constants, vectors \(Ba\) with \(\sum_i a_i=0\), and \((\operatorname{im}B)^\perp\). Formula (26) acts on these subspaces by the three eigenvalues in (27), respectively. \(\square\)

Define
\[
R=\sum_{i<j}p_{ij},\qquad
d_i=\sum_{j\ne i}p_{\min(i,j),\max(i,j)},\qquad
z_i=\frac{d_i-R/(n-1)}{n-2},
\]
and the pair-additivity residual
\[
\mathcal D(c)=\sum_{i<j}(p_{ij}-z_i-z_j)^2.
\tag{28}
\]
Here \(z=(B^\top B)^{-1}B^\top p\), so \(\mathcal D(c)\) is the squared Euclidean distance of \(p\) from \(\operatorname{im}B\).

**Theorem 10 (direction-pair variance and quantitative forcing).** For every legal antipodally odd coloring, writing \(M=2^{n-2}(n-1)!\) and \(\mu=\mathbb E_O T_c(O)\), one has
\[
\boxed{\operatorname{Var}_O(T_c(O))\ge\frac8{n-1}\mathcal D(c).}
\tag{29}
\]
Consequently, with \(p_{\rm good}=\Pr_O(T_c(O)=2)\),
\[
\boxed{
p_{\rm good}\ge
\max\left\{0,\,
\frac{\frac8{n-1}\mathcal D(c)-(2n-\mu)(\mu-6)}
{8(n-1)}
\right\}.}
\tag{30}
\]
In particular, positivity of the displayed numerator forces a monochromatic full antipodal geodesic within the given coloring.

**Proof.** Define \(u_{[x],P}=I_{([x],P)}-\mu/(2n)\). Each support contains \(n\) projective turns, so the support-energy deviation vector equals \(2Au\). Hence
\[
M\operatorname{Var}(T_c)=4\|Au\|^2.
\]
The projective-vertex Fourier transform of \(u\) has constant character coefficient \(p-\bar p\mathbf1\), where \(\bar p=\mu/(2n)\); all other Fourier blocks contribute nonnegatively to \(\|Au\|^2\). By (27) its zero-frequency contribution satisfies
\[
\|Au\|^2\ge 2^{n-1}(n-2)!\mathcal D(c).
\]
Indeed \(p-\bar p\mathbf1\) has no constant-vector component, and its projection onto \((\operatorname{im}B)^\perp\) is precisely the residual vector in (28). Substituting \(M=2^{n-2}(n-1)!\) proves (29).

Every support has \(T_c(O)\in\{2,6,10,\ldots,2n\}\). Therefore the pointwise inequality
\[
(T_c(O)-6)(2n-T_c(O))\ge
-8(n-1)\mathbf1_{\{T_c(O)=2\}}
\]
holds. Taking expectations and expanding gives
\[
\operatorname{Var}(T_c)\le
(2n-\mu)(\mu-6)+8(n-1)p_{\rm good}.
\]
Combining this with (29) proves (30). \(\square\)

**Proposition 11 (strict improvement over the first moment).** There is a legal coloring of \(Q_7\) with \(\mu=289/48>6\) for which (30) certifies at least \(650\) monochromatic coherent supports.

**Construction and verification.** Start from
\[
c_0=c_1=c_2=x_3,\qquad
c_3=c_4=c_5=x_0,\qquad c_6=1+x_0.
\]
Reverse the color on the undirected edge \(\{0,e_3\}\) and on its antipodal edge \(\{\mathbf1,\mathbf1+e_3\}\); leave all other edge colors fixed. The resulting coloring remains legal.

For this coloring, \(p_{ij}=0\) within \(\{0,1,2\}\) and for \(i,j=4,5\); \(p_{ij}=1/2\) when \(i\in\{0,1,2\}\) and \(j\in\{3,4,5,6\}\). The remaining values are
\[
p_{34}=p_{35}=\frac1{32},\qquad
p_{36}=\frac{31}{32},\qquad
p_{46}=p_{56}=1.
\]
Direct substitution in (28), and the vertex-star census, give
\[
\mathcal D(c)=\frac{8753}{7680},\quad
\mathbb E_x S(x)^2=\frac{103}{8},\quad
\mu=\frac{289}{48}.
\]
Therefore
\[
\frac8{n-1}\mathcal D(c)=\frac{8753}{5760}
>\frac{383}{2304}=(14-\mu)(\mu-6).
\]
Formula (30) supplies
\[
\boxed{
p_{\rm good}\ge\frac{5197}{184320}>0.
}
\]
As \(M=23040\), this guarantees at least \(650\) coherent supports with \(T_c=2\). The earlier first-moment certificate requires \(\mu<6\) and therefore gives no guarantee for this coloring. Independent complete enumeration yields the support-energy histogram
\[
(a_2,a_6,a_{10},a_{14})=(3944,15160,3808,128),
\]
confirming the conclusion.

A pure-Python verifier of the legal coloring, rational residual calculation, strict forcing inequality, and support histogram is committed at
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/81e9dadddb6af7c2051d3fe5d8f96f7512707fd6/scripts/nori_zero_mode_spectral_certificate.py .
