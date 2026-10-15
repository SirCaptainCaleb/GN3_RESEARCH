# Edge-free factorwise polarities and the maximal Hamming reduction

# Edge-free coordinatewise polarities and the maximal Hamming reduction

Let \(G=\square_{i=1}^kK_{E_i}\), with \(|E_i|\ge2\). Let \(\tau=\prod_i\tau_i\) be any coordinatewise involution of \(G\), allowing fixed symbols in the individual factors. Define
\[
J(\tau)=\{i:\operatorname{Fix}(\tau_i)=\varnothing\},
\qquad h(\tau)=|J(\tau)|.
\tag{1}
\]
A nontrivial binary edge polarity is an undirected-edge coloring \(c\) satisfying \(c(\tau e)=1-c(e)\).

**Theorem 1 (edge-freeness and displacement).** For a nonidentity coordinatewise involution \(\tau\), the following are equivalent:

(i) \(\tau\) fixes no undirected edge of \(G\);

(ii) \(h(\tau)\ge2\);

(iii) there exists a binary edge polarity \(c\) with \(c(\tau e)=1-c(e)\).

Furthermore, for every coordinatewise involution, including the identity,
\[
\boxed{\min_{x\in V(G)} d_G(x,\tau x)=h(\tau).}
\tag{2}
\]

*Proof.* Every factor indexed by \(J(\tau)\) changes its symbol at every vertex, while every factor outside \(J(\tau)\) has at least one fixed symbol. A shortest Hamming path from \(x\) to \(\tau x\) changes precisely the factors on which \(x_i\ne\tau_i x_i\). Choosing fixed symbols in the other factors gives (2).

Assume \(h(\tau)\ge2\). An edge \(e\) changes one coordinate \(j\), leaving every other coordinate constant. At least one factor in \(J(\tau)\setminus\{j\}\) changes its constant symbol under \(\tau\); thus \(\tau e\ne e\), proving (i).

Conversely, assume \(h(\tau)\le1\) and \(\tau\) is nonidentity. Choose a component \(j\) in which \(\tau_j\) exchanges two distinct symbols \(a,b\); if \(h(\tau)=1\), take the sole fixed-point-free component for \(j\). For every \(i\ne j\), choose a fixed symbol of \(\tau_i\), possible by the definition of \(h\). Then the edge whose changing coordinate \(j\) joins \(a\) to \(b\), with all other coordinates fixed, is stabilized setwise by \(\tau\). Hence (i) implies (ii). An edge-stabilizing involution cannot support an odd binary edge polarity since it would require \(c(e)=1-c(e)\). If all edge orbits have size two, assign one arbitrary bit per orbit and its complement to the other edge, producing such a coloring. This proves the equivalence. \(\square\)

**Theorem 2 (NORI1 gives full intrinsic displacement).** Suppose \(\tau\) is nonidentity and \(h(\tau)\ge2\). Let \(c\) be any edge polarity of \(G\) and \(b\) any turn system obeying the triangle-curvature rule
\[
b(u,v,w)+b(w,v,u)=1\quad(uw\in E(G)),
\qquad b(u,v,w)=c(uv)+c(vw)\quad(uw\notin E(G)).
\tag{3}
\]
Assuming NORI1, there is a monochromatic accepted gallery \(P\) from \(x\) to \(\tau x\) of length \(h(\tau)\). Its edge labels are independent in the canonical resource matroid
\(N=\bigoplus_i M(K_{E_i})\).

*Proof.* For every \(i\in J(\tau)\) choose a symbol \(a_i\), and in every component outside \(J(\tau)\) choose a fixed symbol \(f_i=\tau_i(f_i)\). The induced subgraph
\[
Q=\prod_{i\in J(\tau)}\{a_i,\tau_i(a_i)\}
 \times\prod_{i\notin J(\tau)}\{f_i\}
\tag{4}
\]
is an \(h(\tau)\)-cube invariant under \(\tau\), whose restricted involution is its antipode. The restriction of \(c\) to \(Q\) is therefore antipodally odd. NORI1 supplies a monochromatic geodesic \(P\) joining antipodal vertices of \(Q\). The gallery changes every active component once, using pairwise different direct summands of \(N\), so its resource labels are independent. Consecutive steps change different factors, making the endpoints of their turn nonadjacent in the ambient Hamming graph. The second rule in (3) makes the bit of every interior turn zero. Since \(Q\) is induced, \(P\) is a path of \(G\) and its endpoints are \(x,\tau x\). Its length is \(h(\tau)\), which equals the minimum displacement by Theorem 1. \(\square\)

**Corollary 3 (largest coordinatewise polarized class).** Let \(\mathcal H\) consist of all pairs \((M,\tau)\) where \(M=\bigoplus_iU_{r_i,E_i}\) is a partition matroid and \(\tau\) acts coordinatewise on its intrinsic rank-one reduction, subject to either \(\tau=\mathrm{id}\) or \(h(\tau)\ge2\). Equip these pairs with undirected colors and the turn rule (3), imposing \(c(\tau e)=c(e)+\chi_\tau\), where \(\chi_\tau=0\) for the identity and \(1\) otherwise. Every member has an accepted gallery of length at least \(\lceil\sqrt{\operatorname{rk}N}/2\rceil\), by the cycle-dominating resource-matroid terminal theorem. The single strengthened assertion
\[
\boxed{\ell\ge\max\left\{
\left\lceil\tfrac12\sqrt{\operatorname{rk}N}\right\rceil,\,
\min_x d_G(x,\tau x)\right\}
\tag{5}
\]
for an accepted gallery in every member of \(\mathcal H\) is equivalent to NORI1.

*Proof.* The uniform rank-growth theorem in the preceding Article XI Hamming Subsection applies unchanged to \(\mathcal H\); its proof does not require nontrivial polarity. In the nontrivial case Theorem 2 supplies an independent witness of length equal to the second term of (5). The longer of these two witnesses proves (5) assuming NORI1. Conversely take \(M=\bigoplus_{i=1}^n U_{1,2}\) with its antipodal involution. Then the second term of (5) is \(n\), and an accepted gallery of \(n\) edges is a monochromatic antipodal cube geodesic. Thus (5) entails NORI1. \(\square\)

Theorem 1 establishes why this class is maximal among coordinatewise involutions admitting an odd coloring on undirected edges: every excluded nonidentity involution stabilizes an edge and admits no such coloring. Theorem 2 extends the antipodal cube transfer to Hamming products with odd-sized factors, arbitrary mixed component ranks, and fixed symbols in some factors; only the \(h(\tau)\) forced-moving components enter the invariant cube. This extension retains the same graphic resource matroid and the same local turn law that yield unrestricted boundary-tournament square-root paths when \(\tau\) is the identity.
