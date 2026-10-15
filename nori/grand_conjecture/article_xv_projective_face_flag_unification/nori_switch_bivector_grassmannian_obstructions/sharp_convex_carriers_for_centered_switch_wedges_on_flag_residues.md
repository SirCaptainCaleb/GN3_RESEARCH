# Sharp convex carriers for centered switch wedges on flag residues

### Sharp convex carriers for centered switch wedges

Let \(n\ge2s+3\), \(s\ge0\), and \(W=\{z\in\mathbb R^n:\sum_i z_i=0\}\). For an ordering \(\pi\) of \([n]\), set
\[
Z_j(\pi)=\sum_{h=1}^j e_{\pi_h}-\frac jn\mathbf1.
\]
The permissible prefix ranks for the switches of a centered word of length \(n-2s\) form \(I_s=\{s+1,\ldots,n-s-1\}\).

An ordered partition \(\mathcal P=B_1|\cdots|B_k\), \(k\ge2\), specifies a flag residue whose orders refine the block order. Define its universal extreme-switch carrier
\[
\mathscr E_s(\mathcal P)=
\{Z_p(\pi)\wedge Z_q(\pi):\pi\text{ refines }\mathcal P,\quad
p<q,\ p,q\in I_s\}.
\tag{1}
\]

**Theorem 1 (sharp endpoint-block criterion).**
\[
\boxed{0\notin\operatorname{conv}\mathscr E_s(\mathcal P)
\iff |B_1|\le s+1\text{ and }|B_k|\le s+1.}
\tag{2}
\]
In the positive case a single real linear functional separates all wedges from zero. In the negative case a uniform average of wedges from the residue equals zero.

*Proof.* Suppose the two endpoint blocks have at most \(s+1\) elements, and choose \(a\in B_1\), \(c\in B_k\). For every permissible \(p<q\), all of \(B_1\) belongs to both prefixes and none of \(B_k\) belongs to either prefix. The \((a,c)\)-skew entry of the wedge is
\[
\boxed{(Z_p)_a(Z_q)_c-(Z_p)_c(Z_q)_a=(p-q)/n<0.}
\tag{3}
\]
Thus every wedge in the carrier lies in the same strict open halfspace.

Now suppose \(t=|B_1|\ge s+2\). Set \(p=s+1\), \(q=s+2\), both no greater than \(t\), and fix the orders of all later blocks. Average \(Z_p\wedge Z_q\) over all permutations of the first block \(A=B_1\). Write \(u_A=\sum_{a\in A}e_a\) and \(Z_A=u_A-(t/n)\mathbf1\). For \(r\le t\), define
\[
U_r=\sum_{h=1}^r e_{\pi_h}-\frac rt u_A,\qquad
Z_r=\frac rt Z_A+U_r.
\]
The mean of \(U_r\) over all permutations of \(A\) is zero. Hence the mean wedge is \(\mathbb E(U_p\wedge U_q)\). For every two distinct labels \(a,b\in A\), their transposition reverses the \((a,b)\)-skew entry of this latter wedge and preserves the uniform distribution. Every skew entry therefore has mean zero. Consequently
\[
\boxed{\frac1{t!}\sum_{\pi|_A\in S_A}Z_p(\pi)\wedge Z_q(\pi)=0,}
\tag{4}
\]
placing zero in the convex hull. If the final block has size at least \(s+2\), reverse all orders and replace \((p,q)\) with \((n-q,n-p)\). Since \(I_s\) is reversal-stable and \(Z_j(\pi^{\rm rev})=-Z_{n-j}(\pi)\), the same zero average applies. This proves (2). \(\square\)

**Corollary 2 (canonical high-dimensional fillings).** Suppose every complete path in a rank-exchange residue has at least two switches, and assign each flag the decomposable bivector determined by its first and last switch ranks, as in the preceding Subsection. Whenever the endpoint block sizes satisfy (2), all these flag labels belong to a common open halfspace. Affine interpolation over any common simplicial refinement of the dual cell therefore produces a nowhere-zero map, canonically and consistently over shared faces. The resulting filling is independent of any additional color compatibility assumptions.

**Corollary 3 (rank-two specializations).** For cube edge words \(s=0\), this convex filling applies to residues with singleton first and last dimension blocks. For unrestricted reversal-odd boundary triple words \(s=1\), it applies to residues with first and last vertex blocks of size at most two. Hence *every* commuting-square residue of boundary Hamilton orders admits such a filling, and every braid-hexagon residue does except those permuting the first three or last three vertices.

*Proof.* Dual two-cells of the type-A flag sphere come from either a three-symbol block or two disjoint two-symbol blocks, with the remaining blocks singleton. Apply (2). \(\square\)

**Limitations.** The zero-average half of Theorem 1 is an obstruction to a *universal* convex carrier containing all possible switch pairs. A particular legal coloring may disallow the simultaneous switch-pair choices used in (4). The positive half is unconditional for every legal coloring and every selection of switch pairs. Thus (2) localizes the remaining convex-filling question to residues with more than \(s+1\) freely permutable endpoint symbols. The argument preserves full Hamilton and dimension-simple witnesses and makes no general one-switch claim.
