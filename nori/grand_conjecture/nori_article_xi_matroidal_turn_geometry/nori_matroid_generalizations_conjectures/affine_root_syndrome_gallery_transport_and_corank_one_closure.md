# Affine root-syndrome gallery transport and corank-one closure

# Affine root-syndrome gallery transport and corank-one closure

Let \(n\ge2\), \(M\in\mathbb F_2^{n\times n}\) have zero diagonal and \(M\mathbf1=\mathbf1\), and color the undirected coordinate-\(i\) edges of \(Q_n\) by
\[
c_i(x)=a_i+\sum_jM_{ij}x_j.
\tag{1}
\]
The row-oddness condition \(M\mathbf1=\mathbf1\) is the antipodal-odd coloring law. For a coordinate permutation \(\pi\in S_n\), put
\[
t_i(\pi)=\sum_{\pi^{-1}(j)<\pi^{-1}(i)}M_{ij}.
\tag{2}
\]
Let \(R=\operatorname{im}M\), \(q=n-\operatorname{rk}M\), and \(\Phi(\pi)=t(\pi)+R\in\mathbb F_2^n/R\).

**Theorem 1 (root criterion).** A monochromatic full geodesic with coordinate order \(\pi\) exists if and only if \(\Phi(\pi)=a+R\). For each qualifying \(\pi\), there are \(2^{q+1}\) directed monochromatic geodesics with that order, counted over both colors and all roots. Swapping two consecutive directions \(i,j\) changes the quotient syndrome by
\[
\boxed{\Phi(\pi')-\Phi(\pi)=\Delta_{ij}+R,\qquad
\Delta_{ij}=M_{ij}e_i+M_{ji}e_j.}
\tag{3}
\]

**Proof.** The edge traversed in direction \(i\) from root \(x\), after visiting the earlier directions, has color \(a_i+(Mx)_i+t_i(\pi)\). Hence the full word is constant \(s\) if and only if \(Mx=a+t(\pi)+s\mathbf1\). Since \(\mathbf1=M\mathbf1\in R\), existence is independent of \(s\) and is equivalent to the quotient criterion. Each solvable equation has \(2^q\) solutions \(x\) for either \(s\). Adjacent exchange modifies only the two preceding-direction sums for \(i,j\), giving (3). \(\square\)

**Theorem 2 (universal quotient span and balanced characters).** For every matrix satisfying (1),
\[
\boxed{R+\operatorname{span}\{\Delta_{ij}:i<j\}=\mathbb F_2^n.}
\tag{4}
\]
Consequently the affine span of \(\Phi(S_n)\) is the entire quotient. Moreover, every nonzero linear character of \(\mathbb F_2^n/R\) takes each of its values on at least \((n-1)!\) permutations.

**Proof.** A vector \(z\) annihilating both \(R\) and all the \(\Delta_{ij}\) obeys \(M^Tz=0\) and \(z_iM_{ij}+z_jM_{ji}=0\) for all \(i\ne j\). Fixing \(i\) and summing the latter relations over \(j\ne i\) gives
\[
0=z_i\sum_jM_{ij}+\sum_jM_{ji}z_j=z_i+(M^Tz)_i=z_i.
\]
Thus \(z=0\), proving (4). Every \(\Delta_{ij}\) appears as a difference of \(\Phi\)-values on two permutations in which \(i,j\) are adjacent, giving the affine-span assertion.

For nonzero \(z\in\ker M^T\), (4) ensures some \(i,j\) satisfy \(z\cdot\Delta_{ij}=1\). There are \((n-1)!\) permutations containing \(i,j\) consecutively in that order and the same number containing \(j,i\) consecutively. Swapping the two entries pairs them and flips the value of \(z\cdot\Phi\). Thus each character value occurs at least \((n-1)!\) times. \(\square\)

**Corollary 3 (unrestricted nonsymmetric affine closure in corank at most one).** If \(\operatorname{rk}M\ge n-1\), then for every choice of \(a\), the coloring (1) admits a monochromatic full antipodal geodesic. There are \(2n!\) directed such geodesics when \(\operatorname{rk}M=n\), and at least \(4(n-1)!\) when \(\operatorname{rk}M=n-1\).

**Proof.** If \(q=0\), the quotient is trivial and every order qualifies. If \(q=1\), Theorem 2 forces both elements of the quotient to be attained and guarantees at least \((n-1)!\) permutations in either class. Apply Theorem 1. \(\square\)

**Proposed affine quotient-surjectivity conjecture.** Every zero-diagonal row-odd binary matrix satisfies
\[
\Phi(S_n)=\mathbb F_2^n/\operatorname{im}M.
\tag{5}
\]
Its proof would settle all antipodally odd *affine* cube-edge colorings. Full affine span from Theorem 2 is a necessary step but does not alone imply (5) when \(q\ge2\). The general nonlinear NORI1 conjecture remains separate.

**Falsification check.** Direct exhaustive enumeration of all row-odd zero-diagonal matrices at dimensions \(3,4,5\) found no counterexample to (5): respectively \(8,256,32768\) matrices. The largest observed coranks were respectively \(1,2,3\). No computation is used in the proofs.

**Relationship to prior work.** The manuscript's forest-coupling theorem gives rooted switch bounds for sparse symmetric \(M\). The results here apply to arbitrary nonsymmetric matrices of corank at most one and establish an unrestricted-dimensional gallery-exchange span statement for every affine antipodally odd interaction matrix.

## Theorem 4 (corank-two affine NORI1 closure)

Under the assumptions of Theorem 1, if
\[
\boxed{\operatorname{rk}_{\mathbb F_2}M\ge n-2,}
\tag{11}
\]
then **every** choice of \(a\) yields a monochromatic full antipodal geodesic. When \(\operatorname{rk}M=n-2\), there are at least \(16\) directed monochromatic full geodesics. Thus affine root-syndrome surjectivity (5) holds for quotient dimensions \(q=0,1,2\), with no symmetry condition on \(M\).

**Lemma 4.1 (cyclic gallery transport).** Let \(\pi=(i_1,\ldots,i_n)\) and let \(\rho\pi=(i_2,\ldots,i_n,i_1)\). In \(Q=\mathbb F_2^n/\operatorname{im}M\), write \(g_i=e_i+\operatorname{im}M\). Then
\[
\boxed{\Phi(\rho\pi)=\Phi(\pi)+g_{i_1}.}
\tag{12}
\]
Successive cyclic rotations visit the cosets
\[
\Phi(\pi),\quad\Phi(\pi)+g_{i_1},\quad
\Phi(\pi)+g_{i_1}+g_{i_2},\quad\ldots.
\tag{13}
\]

**Proof.** Moving \(i_1\) from first to last reverses its order relative to every other direction. Its own coordinate of \(t\) changes by \(\sum_{j\ne i_1}M_{i_1j}=1\), while coordinate \(j\ne i_1\) changes by \(M_{j i_1}\). Thus
\[
t(\rho\pi)+t(\pi)=e_{i_1}+Me_{i_1},
\]
whose quotient class is \(g_{i_1}\). Iteration proves (13). \(\square\)

**Proof of Theorem 4.** The cases \(q=0,1\) are Corollary 3, so suppose \(q=2\). The \(n\) vectors \(g_i\in Q=\mathbb F_2^2\) span \(Q\) and satisfy \(\sum_i g_i=\mathbf1+\operatorname{im}M=0\).

First suppose some nonzero class \(u\in Q\) occurs as \(g_i=g_{i'}=u\) at two distinct coordinates, and some other coordinate has class \(v\notin\{0,u\}\). Take a permutation beginning with \(i,j,i'\), where \(g_j=v\). By (13), four successive cyclic rotations have syndrome classes
\[
z,\quad z+u,\quad z+u+v,\quad z+v.
\]
They are the four elements of \(Q\). Therefore \(\Phi(S_n)=Q\).

Otherwise, because the \(g_i\) span \(Q\) and sum to zero, the only nonzero \(g_i\)'s consist of **three distinct nonzero classes appearing once each**. Denote the corresponding coordinates by \(a,b,c\), and let \(S=\{a,b,c\}\). Every \(e_u\) with \(u\notin S\) lies in \(R=\operatorname{im}M\), and \(e_a+e_b+e_c\in R\). These \(n-2\) vectors are independent, so
\[
R=\operatorname{span}\{e_u:u\notin S\}
+\operatorname{span}\{e_a+e_b+e_c\}.
\tag{14}
\]
Every column \(Me_j\) lies in \(R\); restriction of such a column to the coordinates \(a,b,c\) therefore has either \(000\) or \(111\). Consequently rows \(a,b,c\) of \(M\) are identical; denote their common row by \(w\). The zero diagonal gives \(w_a=w_b=w_c=0\). Since the row sum is odd, some \(u\notin S\) satisfies \(w_u=1\).

Choose permutations beginning with the four-letter blocks
\[
(a,b,c,u),\qquad (a,u,b,c),\qquad
(b,u,a,c),\qquad (c,u,a,b),
\]
and place all other coordinates afterward, in any common order. For their syndrome vectors \(t(\pi)\), the entries at \(a,b,c\) are respectively
\[
000,\qquad 011,\qquad 101,\qquad 110.
\]
Indeed, within \(S\) the common row \(w\) vanishes, all other outside coordinates come after the block, and the sole preceding \(w\)-active coordinate inside the block is \(u\). By (14), the four triples represent the four quotient classes. Hence \(\Phi(S_n)=Q\) also in this case.

For any \(a+R\), therefore, a qualifying permutation exists. Reversing a qualifying permutation gives another: because \(M\mathbf1=\mathbf1\), formula (2) gives \(t(\operatorname{rev}\pi)=t(\pi)+\mathbf1\), and \(\mathbf1\in R\). The two permutations are distinct for \(n\ge3\). Each supplies \(2^{q+1}=8\) directed full monochromatic geodesics by Theorem 1, giving the lower bound \(16\). \(\square\)

**Scope.** This handles affine antipodally odd cube-edge colorings whenever the binary interaction matrix has corank at most two. It strengthens the corank-one case without assuming symmetry or a sparse interaction graph. The first unresolved affine quotient dimension is \(q=3\).

## Theorem 5 (fixed-support rank-defect control)

The following holds even for a zero-diagonal affine matrix \(M\) without the row-oddness condition. Write \(q=n-\operatorname{rk}M\). There is a set \(I\subseteq[n]\) of cardinality \(q\), depending only on \(M\), with this property: **for every prescribed permutation \(\pi\)** there is a root \(x\) for which all edges of its full geodesic in directions outside \(I\) have color zero. Its color-one counterpart on those directions exists whenever \(M\mathbf1=\mathbf1\). In particular, some full antipodal geodesic has at most \(q\) color changes:
\[
\boxed{\mu(c)\le n-\operatorname{rk}M.}
\tag{15}
\]

**Proof.** Choose \(I\) such that the coordinate cosets \(\{e_i+R:i\in I\}\) form a basis of \(\mathbb F_2^n/R\), with \(R=\operatorname{im}M\). Then every coset has one representative supported on \(I\). For any \(\pi\), choose that representative \(w\) for the coset \(a+t(\pi)+R\). Solve \(Mx=a+t(\pi)+w\). Formula (4) of Theorem 1 says the associated edge-color vector is \(w\), vanishing outside \(I\). If \(M\mathbf1=\mathbf1\), replace \(x\) by \(x+\mathbf1\) to complement the colors. Finally choose \(\pi\) to traverse every direction outside \(I\) first and the \(q\) directions in \(I\) last. Its word is \(0^{n-q}w_I\), which changes color at most \(q\) times. \(\square\)

For \(q=1\) and antipodal oddness, the ordinary odd-change rotation of the full path converts the resulting at-most-one-switch path into a monochromatic full path. Theorem 4 strengthens this conclusion to the larger class \(q=2\).

## Theorem 6 (binary cut transport and a Gray-code saturation criterion)

For any subset \(S\subseteq[n]\), let \(\mathbf1_S\) be its indicator vector. Moving a consecutive initial block whose coordinate set is \(S\) to the end of the permutation, preserving the internal order of both blocks, changes its syndrome by
\[
\boxed{\Phi(\text{block rotated }\pi)-\Phi(\pi)=\mathbf1_S+R.}
\tag{16}
\]
Indeed the cross-block swaps contribute
\[
\sum_{i\in S,j\notin S}\Delta_{ij}
=\mathbf1_S+M\mathbf1_S
\]
because each full transposition star obeys
\(\sum_{j\ne i}\Delta_{ij}=e_i+Me_i\) and the internal pairs cancel twice. Reduction modulo \(R\) proves (16).

More generally, suppose the projected coordinate vectors \(g_i=e_i+R\) contain a quotient basis \(h_1,\ldots,h_q\) with at least \(2^{q-j}\) distinct coordinate representatives of \(h_j\) for every \(j=1,\ldots,q\). Then \(\Phi:S_n\to\mathbb F_2^n/R\) is surjective, and every affine antipodally odd coloring with this matrix \(M\) has a monochromatic full geodesic.

**Proof.** The standard reflected binary Gray sequence on \(\mathbb F_2^q\) visits all \(2^q\) vectors, starting at zero, using \(2^{q-j}\) steps in basis direction \(h_j\). Choose distinct coordinates representing those steps and place them first in a coordinate permutation, ordered as in this Gray sequence; place the remaining coordinates afterward. By Lemma 4.1, consecutive cyclic rotations traverse its successive quotient prefix sums. They visit all \(2^q\) quotient syndromes, proving surjectivity and then the existence assertion by Theorem 1. \(\square\)

The cut identity (16) is the affine root-transport analogue of the cycle–cocycle relation: the sum of local pair exchanges across a coordinate cut equals its indicator modulo the root-change image. The Gray-code condition is a sufficient structural criterion, while Theorem 4 proves the entire corank-two family without a repetition hypothesis.

## Theorem 7 (all rank-two antipodally odd affine interactions admit monochromatic full paths)

Suppose \(M_{ii}=0\), \(M\mathbf1=\mathbf1\), and
\[
\boxed{\operatorname{rk}_{\mathbb F_2}M=2.}
\tag{17}
\]
Then for every constant vector \(a\), the affine coloring \(c_i(x)=a_i+(Mx)_i\) admits a monochromatic antipodal geodesic. Moreover, there exist two fixed coordinate directions \(u,t\), depending only on \(M\), such that for every \(a\) a monochromatic full geodesic begins at one of the four roots \(0,e_u,e_t,e_u+e_t\).

**Proof.** Because all rows of \(M\) have odd parity, and the two-dimensional row space contains only two odd-parity vectors, there are precisely two distinct row types \(v,w\). Let \(A\) be the nonempty set of row indices of type \(v\) and \(B\) those of type \(w\), partitioning \([n]\). The zero diagonal forces \(v_i=0\) for \(i\in A\) and \(w_j=0\) for \(j\in B\). Therefore
\[
U=\operatorname{supp}v\subseteq B,\qquad
T=\operatorname{supp}w\subseteq A,
\]
and both \(|U|\) and \(|T|\) are odd. For any \(u\in U\) and \(t\in T\), the columns of \(M\) satisfy
\[
Me_u=\mathbf1_A,\qquad Me_t=\mathbf1_B.
\tag{18}
\]
Hence the root-change image is \(R=\operatorname{span}\{\mathbf1_A,\mathbf1_B\}\).

Choose bits \(\alpha,\beta\), and define target labels \(h_i=a_i+\alpha\) on \(A\) and \(h_j=a_j+\beta\) on \(B\). Because \(|T|\) is odd, one can choose \(\alpha\) so that
\[
|T_0|:=|\{i\in T:h_i=0\}|\quad\text{is even};
\]
because \(|U|\) is odd, choose \(\beta\) so that
\[
|U_0|:=|\{j\in U:h_j=0\}|\quad\text{is odd}.
\]
Write \(T_1=T\setminus T_0\), \(U_1=U\setminus U_0\). Construct a coordinate permutation whose active-coordinate blocks occur in the order
\[
\boxed{T_0,\quad U_0,\quad T_1,\quad U_1.}
\tag{19}
\]
Every \(i\in T_0\) encounters zero earlier members of \(U\), so \(t_i(\pi)=0=h_i\). Every \(j\in U_0\) encounters \(|T_0|\) earlier members of \(T\), an even number, so \(t_j(\pi)=0=h_j\). Every \(i\in T_1\) encounters \(|U_0|\) earlier members of \(U\), an odd number, so \(t_i(\pi)=1=h_i\). Every \(j\in U_1\) encounters all \(|T|\) earlier members of \(T\), also odd, so \(t_j(\pi)=1=h_j\).

For \(i\in A\setminus T\), the same formula \(t_i(\pi)=|\{u\in U:u\text{ precedes }i\}|\pmod2\) applies. Insert such an inactive coordinate at the very beginning if \(h_i=0\), and at the very end if \(h_i=1\). For \(j\in B\setminus U\), insert it at the beginning if \(h_j=0\) and at the end if \(h_j=1\). Their insertion does not change any active parity, since inactive \(A\)-vertices are absent from \(T\) and inactive \(B\)-vertices are absent from \(U\). All target equalities \(t_i(\pi)=h_i\) are therefore realized.

Thus
\[
a+t(\pi)=\alpha\mathbf1_A+\beta\mathbf1_B
=M(\alpha e_u+\beta e_t).
\]
Choose root \(x=\alpha e_u+\beta e_t\). The edge-color formula (4) yields
\[
a+Mx+t(\pi)=0,
\]
so the full path from \(x\) in direction order \(\pi\) is monochromatic. The possible roots form the stated four-element set. \(\square\)

**Corollary (affine gap reduced to intermediate ranks).** A zero-diagonal row-odd binary matrix has rank at least two: if it had rank one, all nonzero odd rows would coincide, and the zero diagonal would force their common row to vanish. Combining Theorems 4 and 7, every antipodally odd affine cube-edge coloring is solved when
\[
\operatorname{rk}M=2\quad\text{or}\quad \operatorname{rk}M\ge n-2.
\]
The first potentially unresolved interaction ranks are \(3\le\operatorname{rk}M\le n-3\), beginning at dimension \(n=6\). In particular all affine antipodally odd cube-edge colorings in dimensions \(n\le5\) are covered by theorems in this subsection.

**Structural interpretation.** A rank-two odd interaction matrix forces a bipartite two-row-type dependence system. The four-block permutation (19) is an explicit resource-basis gallery that solves the root syndrome. It complements the high-rank quotient approach and applies in arbitrarily large dimensions with corank \(n-2\).
