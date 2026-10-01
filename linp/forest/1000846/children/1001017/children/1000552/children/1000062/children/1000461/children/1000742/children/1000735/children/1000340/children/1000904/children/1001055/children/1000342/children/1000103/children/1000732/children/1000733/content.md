# The one-rank saving improves the global bound for every uniformity

## Statement

For integers r>=3 and ell>=5, every n-vertex linear r-uniform hypergraph containing no linear path of ell edges satisfies
|E(H)| <= [((8r^2-10r+1)ell-(16r^2-22r-3))/(8r(r-1))] n.
This improves the preceding general-r bound by (6r-7)n/(8r(r-1)), without changing its leading coefficient.

For the maximum endpoint paths selected in the proof, let X be total excess contact multiplicity. The stronger estimate subtracts the additional term (r-2)X/[r(r-1)] from the right-hand side.
In particular the displayed coefficients are (43ell-75)/48 for r=3, (89ell-165)/96 for r=4, and (151ell-287)/160 for r=5.

## Body

Write L=ell-1>=4. For an ascending edge, its unique entrance x has phi(x)=phi(e)-1; its other r-1 vertices are terminals. Let A be the number of ascending edges. At each nonisolated vertex v put p=phi(v)<=L, let t(v) count ascending edges terminal at v, and, if t(v)>0, let q(v) be their maximum edge rank. Choose a maximum endpoint path P_v; if q(v)=p, choose it to end in a rank-p ascending terminal edge.

For e containing v, assign contact multiplicity mu_v(e)=1 when e is the last edge of P_v, and otherwise set
mu_v(e)=|(e minus {v}) intersect (V(P_v) minus the last edge)|.
Let X_v=sum_{e containing v} max(mu_v(e)-1,0), and X=sum_v X_v. By the general contact identity 6c9c2c5a0fcb (math_version 1),
rm <= (r-1)S-(r-2)n_+ + A-X,
where S=sum_v p(v). This follows because clean incidences can occur only at ascending entrances.

Define the real-valued linear bound
F_r(s)=((6r-7)s+13-6r)/8.
The fixed-entrance transfer dcf886f98a51 (math_version 1) gives |J_s(v)|<=F_r(s) for s>=4. Indeed its singleton bound satisfies
alpha_r(s-3)<=((2r-3)/4)(s-3)+(r-2),
and substitution in |J_s(v)|<=1+floor(((r-1)(s-1)+alpha_r(s-3))/2) gives F_r(s).
The small cases satisfy |J_2(v)|=1<=F_r(2), and
|J_3(v)|<=1+floor((3r-4)/2)<=F_r(3).
For the latter, all vertices of the first edge of a three-edge anchor path are forbidden singleton positions: the free vertices contradict the entrance rank, while its forward joint gives a longest path entering the last edge through the wrong vertex. Hence at most r-2 singleton positions remain among 2(r-1) precursor vertices. Counting all other contact sets with weight at least two gives the stated bound. The small-case facts also appear in 82162401a222 (math_version 1).

We claim that for every v,
t(v)-X_v<=F_r(L-1).                                      (*)
There is nothing to prove if t(v)=0. If q(v)<p, all t(v) edges lie in the incident-rank family at a maximum-rank ascending anchor, so
t(v)-X_v<=t(v)<=F_r(q(v))<=F_r(L-1).

Suppose instead q(v)=p>=4. On the chosen anchor path, each nonsingleton ascending contact contributes at most zero after its excess multiplicity is subtracted; the last edge contributes one. Thus
t(v)-X_v<=1+alpha_r(p-3)
<=((2r-3)/4)p+(5-2r)/4
<=((2r-3)/4)L+(5-2r)/4.
The difference between F_r(L-1) and the final expression is
((2r-1)L+10-8r)/8.
Since L>=4, this is at least 6/8>0. Hence (*) holds.
If q(v)=p=2 or 3, use t(v)<=1 or t(v)<=F_r(3), respectively, and F_r(3)<=F_r(L-1). There are no ascending edges of rank one. This completes the local argument for every vertex.

Sum (*). Since sum_v t(v)=(r-1)A,
(r-1)A-X<=F_r(L-1)n_+.
Therefore
A-X <= F_r(L-1)n_+/(r-1) -(r-2)X/(r-1).
Insert this into the general contact inequality, and use S<=Ln_+, to obtain
rm <= [(r-1)L-(r-2)+F_r(L-1)/(r-1)]n_+ -(r-2)X/(r-1).
The coefficient of n_+ is positive for L>=4, so n_+ may be replaced by n. Substituting L=ell-1 and simplifying proves
m <= [((8r^2-10r+1)ell-(16r^2-22r-3))/(8r(r-1))]n
     -(r-2)X/[r(r-1)].

The previous constant term in 82162401a222 was -(16r^2-28r+4)/(8r(r-1)); their difference is exactly (6r-7)/(8r(r-1)). At r=3 this recovers the coarser bound in a57007500001, whose residue-sensitive and small-length estimates are stronger. The improvement comes entirely from keeping the aligned case separate and retaining the one-rank gap in the other case. It does not assert a smaller leading coefficient.
