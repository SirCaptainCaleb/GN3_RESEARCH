# The aligned-or-lower-rank dichotomy sharpens the global bound to (43ell-75)n/48

## Statement

Let H be a finite linear 3-uniform hypergraph, let p(v)=phi(v) for each nonisolated vertex, and let m=|E(H)|. Define
beta(1)=0, beta(2)=1, beta(3)=2, beta(4)=2, beta(5)=3, beta(6)=5,
and beta(p)=floor((11p-16)/8) for p>=7.
Then
6m <= sum_{v nonisolated}(4p(v)-2+beta(p(v))).

Consequently, for every integer ell>=8, every n-vertex P_ell^(3)-free linear 3-graph satisfies
m <= [4ell-6+floor((11ell-27)/8)] n /6
  = [(43ell-75-rho_ell)/48] n,
where rho_ell is the least nonnegative residue of 11ell-27 modulo 8. In particular
m <= ((43ell-75)/48)n.
The same argument gives m<=2n, (8/3)n, (7/2)n, and (9/2)n for ell=4,5,6,7 respectively.

More precisely choose maximum endpoint paths as described in the proof. Let A count ascending edges, C count clean incidences, D count double incidences, U be total unused contact capacity, and eta=sum_v[beta(p(v))-t(v)+D_v]. Then eta>=0 and the exact identity is
6m = sum_v(4p(v)-2+beta(p(v))) - D - eta - 2(A-C) - 2U.
All four subtracted terms are nonnegative.

## Body

This is a global synthesis of the exact fixed-entrance theorem eb40ddcc33ca (math_version 1), the maximum-path central-window lemma 49080cbf1371 (math_version 1), and the certified clean-minus-double identity 4e165e65be58 (math_version 1). It extracts the one-rank saving in the misaligned case instead of replacing q(v) by p(v). The existing master inequality 178e5b72caae contains the needed local estimates, but did not maximize them into this unconditional global bound.

Notation. For each nonisolated v put p=phi(v). Let t(v) count ascending nonspecial edges terminal at v; if t(v)>0 let q(v) be their maximum edge rank. Always q(v)<=p. Let gamma(1)=0, gamma(2)=1, gamma(3)=2, and gamma(j)=floor((11j-5)/8) for j>=4. Choose a maximum p-edge path P_v ending at v. If q(v)=p, choose it to end in an ascending edge of rank p. Let D_v count the incident edges having two off-v contacts on the precursor of P_v; the last edge itself is assigned multiplicity one. Let D=sum_v D_v.

Local estimate. We prove t(v)-D_v<=beta(p).
If t(v)=0 this is immediate.
If q(v)=p>=4, the fixed-entrance theorem bounds singleton contacts other than the last edge by ceil((3p-8)/4). Every double among the ascending terminal incidences is paid by D_v, so
t(v)-D_v<=1+ceil((3p-8)/4)=ceil((3p-4)/4).
For p=2,3 the simpler estimates t(v)<=gamma(p)=1,2 suffice and give the same displayed bound.
If q(v)<p, monotonicity gives
t(v)<=gamma(q(v))<=gamma(p-1).
On the other hand, after subtracting D_v only single-contact ascending terminal incidences can contribute positively. The central-window lemma bounds their number by max(0,4q(v)-2p-3), which is at most max(0,2p-7). Hence
t(v)-D_v<=min{gamma(p-1),max(0,2p-7)}.

Both cases are therefore bounded, for p>=2, by
max{ceil((3p-4)/4), min{gamma(p-1),max(0,2p-7)}}.
For p=1 there are no ascending terminal incidences, since a rank-one edge is special.
Direct substitution at p=2,3,4,5,6,7 gives 1,2,2,3,5,7.
For p>=8,
gamma(p-1)<= (11p-16)/8 <=2p-7,
and
gamma(p-1)>= (11p-23)/8 >= (3p-1)/4 >=ceil((3p-4)/4).
Thus the maximum equals gamma(p-1)=floor((11p-16)/8). This also holds at p=7. The local estimate follows.

Global accounting. Let n_+ count nonisolated vertices and S=sum_v p(v). For each P_v let mu_v(e) be its contact multiplicity, with its last edge assigned multiplicity one. Set
U=sum_v [2p(v)-1-sum_{e containing v}mu_v(e)].
Linearity gives U>=0. If C counts multiplicity-zero incidences, the exact contact count is
3m-C+D=2S-n_+-U.
Every clean incidence belongs to the unique entrance of an ascending edge, so C<=A. Each ascending edge has exactly two terminals, giving sum_v t(v)=2A.
Define eta=sum_v[beta(p(v))-t(v)+D_v]>=0. Then
sum_v beta(p(v))=2A-D+eta.
Substitution into the preceding exact contact identity yields
6m=4S-2n_++sum_v beta(p(v))-D-eta-2(A-C)-2U,
which proves both the exact identity and the stated rank-sensitive upper bound.

Forbidden-path bound. If H is P_ell-free, p(v)<=L:=ell-1. The function 4p-2+beta(p) is increasing for positive integer p: the listed initial values and the increasing floor formula make this immediate. Therefore
6m<=[4L-2+beta(L)]n_+<=[4L-2+beta(L)]n.
For ell>=8, L>=7 and beta(L)=floor((11ell-27)/8), so this is the advertised formula. Writing
floor((11ell-27)/8)=(11ell-27-rho_ell)/8
gives (43ell-75-rho_ell)n/48. Substitution of L=3,4,5,6 gives the four smaller-length bounds.

Interpretation. The formerly displayed uniform bound was (43ell-64)n/48. This improves that bound by at least 11n/48 for ell>=8, plus the residue correction; it does not change the leading coefficient 43/48. The improvement uses a dichotomy: aligned vertices have substantial multiplicity compensation, while misaligned vertices lose at least one whole rank in their ascending terminal count. No source-rail overlap classification is needed.

Research consequence of the exact identity. Near equality in the new bound simultaneously requires small total double-contact mass D, small unclean ascending-source mass A-C, small unused contact capacity U, and small local deficit eta. These are quantitative restrictions for any admissible choice of the maximum paths above; they should be retained when pursuing a leading-coefficient improvement.
