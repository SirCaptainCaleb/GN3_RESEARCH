# Center-indexed alternating forms for all boundary tournaments

Let \(V\) be a set of \(n\ge3\) symbols and
\[
W=\{z\in\mathbb R^V:\sum_{v\in V}z_v=0\},\qquad
u_a^{\,h}=e_a-e_h\quad(a\ne h).
\]
For each \(h\in V\), the \(n-1\) vectors \(u_a^{\,h}\), \(a\ne h\), form a basis of \(W\). Write \(\operatorname{Alt}^2(W)\) for the space of alternating real bilinear forms on \(W\). The two-valued sign convention below is \(s(a,h,c)=(-1)^{b(a,h,c)}\).

**Theorem 1 (faithful center-indexed two-form representation).** Assignment
\[
\boxed{\quad
\omega_h(u_a^{\,h},u_c^{\,h})=(-1)^{b(a,h,c)}
\quad(a,c\ne h,\ a\ne c)
\quad}                                                   \tag{1}
\]
is a bijection between ordinary reversal-odd boundary 3-tournaments \(b\) on \(V\) and families \((\omega_h)_{h\in V}\) of alternating bilinear forms on \(W\) whose values in (1) belong to \(\{-1,1\}\). The forms at distinct centers \(h\) may be prescribed independently.

Moreover, if \(q_1,\ldots,q_{n-1}\) is the alternating rook encoding of a Hamilton ordering \(v_1,\ldots,v_n\), and \(r_i=e_{(q_i)_1}-e_{(q_i)_2}\), then
\[
\boxed{\quad
(-1)^{b(v_i,v_{i+1},v_{i+2})}
=\omega_{v_{i+1}}(r_i,r_{i+1})
\qquad(1\le i\le n-2).
\quad}                                                   \tag{2}
\]
Thus the boundary one-switch Hamilton problem is equivalent to finding an ordered root basis \(r_1,\ldots,r_{n-1}\) with Gram matrix \(2I+A(P_{n-1})\) for which the sequence of signs in (2) changes at most once.

*Proof.* For fixed \(h\), specifying the values of an alternating form on the ordered pairs of distinct basis vectors \(u_a^{\,h}\) determines that form uniquely. The condition \(b(c,h,a)=1-b(a,h,c)\) says
\[
(-1)^{b(c,h,a)}=-(-1)^{b(a,h,c)},
\]
precisely the alternating condition. Conversely, prescribing arbitrary values \(+1\) or \(-1\) for the \(\binom{n-1}{2}\) unordered pairs of basis vectors produces a unique \(\omega_h\) and the corresponding \(b\) at center \(h\). Different centers involve disjoint reversal orbits of ordered triples; there are therefore
\[
n\binom{n-1}{2}=3\binom n3
\]
independent bits, as required.

For the rook gallery, put \(h=v_{i+1}\). If \(i\) is odd, then
\[
(r_i,r_{i+1})=(u_{v_i}^{\,h},u_{v_{i+2}}^{\,h});
\]
if \(i\) is even, both roots are the negatives of these two vectors. Bilinearity makes simultaneous negation invisible, proving (2). This also proves that the formula respects entry swap \(\tau\) of rook states, while alternation changes its sign upon reversing a directed rook arc. The Gram characterization of Hamilton rook galleries supplies the final equivalence. \(\square\)

The use of one form per center is intrinsic to the full tournament class. Replacing the family by one alternating form on \(W\) introduces an additional constraint.

**Proposition 2 (cyclic restriction of a global two-form).** Let \(\omega\in\operatorname{Alt}^2(W)\), and put
\[
B_\omega(a,h,c)=\omega(e_a-e_h,e_c-e_h).
\]
Then \(B_\omega\) is alternating under every permutation of its three distinct arguments. In particular,
\[
B_\omega(a,h,c)=B_\omega(h,c,a)=B_\omega(c,a,h).
\tag{3}
\]
Consequently, any boundary 3-tournament obtained by taking the signs of \(B_\omega(a,h,c)\), assuming these values are nonzero, is invariant under cyclic rotation of its ordered triples. For \(n\ge3\), the cyclically invariant tournaments form a fraction
\[
2^{-2\binom n3}                                          \tag{4}
\]
of all reversal-odd boundary 3-tournaments.

*Proof.* Extend \(\omega\) to the formal basis vectors \(e_v\) by restricting their arguments to \(W\), and write \(\Omega_{ac}=\omega(e_a-e_o,e_c-e_o)\) for an arbitrary reference symbol \(o\). The expansion
\[
B_\omega(a,h,c)=\Omega_{ac}+\Omega_{ha}+\Omega_{ch}
\tag{5}
\]
is independent of the reference \(o\). Its cyclic invariance and change of sign under exchange of two arguments are immediate. A reversal-odd boundary 3-tournament has three independent reversal-orbit bits on each unordered three-element set; cyclic invariance identifies those three bits. Hence there are \(2^{3\binom n3}\) unrestricted tournaments and \(2^{\binom n3}\) cyclically invariant ones, giving (4). \(\square\)

The restriction can be sharpened for **real-valued** arc data, independently of a sign threshold.

**Proposition 3 (cocycle criterion for a global two-form).** Suppose \(B(a,h,c)\in\mathbb R\) is defined on ordered distinct triples. There exists \(\omega\in\operatorname{Alt}^2(W)\) such that
\[
B(a,h,c)=\omega(e_a-e_h,e_c-e_h)
\tag{6}
\]
for every ordered triple if and only if \(B\) is alternating under all permutations and satisfies
\[
B(b,c,d)-B(a,c,d)+B(a,b,d)-B(a,b,c)=0                    \tag{7}
\]
for all distinct \(a,b,c,d\). When \(n=3\), condition (7) is vacuous.

*Proof.* Equation (5) writes \(B\) as the negative of the simplicial coboundary of the alternating edge values \(\Omega_{ab}\). Alternation and (7) follow by cancellation. Conversely, fix \(o\in V\), and prescribe alternating edge values by
\[
\Omega_{oa}=0,\qquad
\Omega_{ac}=-B(o,a,c)\quad(a,c\ne o).
\]
These values define an alternating form on \(W\) through the basis \(\{e_a-e_o:a\ne o\}\). If \(a,h,c\ne o\), (7) on \(o,a,h,c\) gives
\[
B(a,h,c)
=B(o,h,c)-B(o,a,c)+B(o,a,h)
=\Omega_{ac}+\Omega_{ha}+\Omega_{ch}.
\]
The same identity is immediate when one of \(a,h,c\) equals \(o\), using alternation. Equation (6) follows. \(\square\)

Propositions 2–3 locate the limitation of a single exterior two-form: it enforces cyclic symmetry, and its real values also satisfy tetrahedral identities. The full boundary class instead corresponds to the independent center-indexed forms of Theorem 1. The antipodal root map acts by \(r\mapsto-r\), and each alternating form satisfies \(\omega_h(-r,-s)=\omega_h(r,s)\). Consequently the induced rook-arc labels are invariant under simultaneous antipodal entry swap and reversed upon reversal of the directed arc, matching the required two distinct symmetries.

This representation retains every Hamilton gallery and every tournament coloring, and it supplies a finite-dimensional algebraic formulation for a potential chain-level selector. No existence theorem for a one-switch Hamilton gallery follows from bilinearity alone: the forms \(\omega_h\) are independent, while the sought roots must jointly satisfy the Gram condition.
