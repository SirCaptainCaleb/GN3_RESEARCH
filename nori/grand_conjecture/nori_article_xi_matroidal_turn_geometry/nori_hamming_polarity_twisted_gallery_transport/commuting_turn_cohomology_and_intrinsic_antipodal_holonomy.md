# Commuting-turn cohomology and intrinsic antipodal holonomy

# Commuting-turn cohomology and intrinsic antipodal holonomy

Let \(G=\square_{i=1}^k K_{E_i}\), where \(k\ge2\) and \(|E_i|\ge2\). The **commuting-turn graph** \(T(G)\) is the following ordinary undirected graph:
- its vertices are the graph edges \(e\in E(G)\);
- \(e,f\) are adjacent in \(T(G)\) if they are distinct incident edges of \(G\) which change *different* Cartesian coordinates.

Equivalently, their ordered two-edge turn \((u,v,w)\) has nonadjacent outside endpoints \(u,w\). A binary value on each edge of \(T(G)\) is thus an assignment to the underlying *unoriented* commuting turns of \(G\).

**Lemma 1 (connectivity).** If \(k\ge2\), the graph \(T(G)\) is connected.

*Proof.* The line graph \(L(G)\) is connected since \(G\) is connected. Every adjacency \(ef\) in \(L(G)\) between edges of different Cartesian factors is also an edge of \(T(G)\). If \(e,f\) are incident at \(v\) and change the same factor \(i\), choose any edge \(g\) incident at \(v\) changing a different factor \(j\ne i\). Then \(e,g,f\) is a two-edge walk in \(T(G)\). Thus every line-graph adjacency can be replaced by a \(T(G)\)-walk of length at most two, proving connectivity. \(\square\)

**Theorem 2 (choice-free reconstruction of edge colors from commuting turns).** Let \(B:E(T(G))\to\mathbb F_2\). The following are equivalent:

(i) for every cycle \(C\) of \(T(G)\), \(\sum_{t\in C}B(t)=0\);

(ii) there exists \(c:E(G)\to\mathbb F_2\) such that
\[
B(\{e,f\})=c(e)+c(f)
\quad\text{for every }\{e,f\}\in E(T(G)).
\tag{1}
\]

When these conditions hold, \(c\) is unique up to simultaneous complementation on all edges of \(G\). In particular, for any graph edges \(e,f\), the quantity
\[
\delta_B(e,f)=\sum_{t\in P}B(t)
\tag{2}
\]
is independent of the choice of \(T(G)\)-path \(P:e\leadsto f\), and satisfies \(\delta_B(e,f)=c(e)+c(f)\).

*Proof.* Under (ii), the sum around every cycle telescopes to zero. Conversely, fix \(e_0\in E(G)=V(T(G))\), set \(c(e_0)=0\), and for any \(e\) define \(c(e)\) to be the sum of \(B\) along a \(T(G)\)-path from \(e_0\) to \(e\). Condition (i) makes this path independent, and adding the values at adjacent vertices gives (1). If \(c'\) also satisfies (1), then \(c+c'\) is constant along every edge of the connected graph \(T(G)\), so it is globally constant. Equation (2) follows from the same telescoping argument. \(\square\)

Let \(\tau\) be any involutive automorphism of \(G\) preserving the Cartesian factor directions, such as the canonical central polarity determined by the two-element components of a partition matroid. It acts on \(T(G)\). Say \(B\) is \(\tau\)-invariant if \(B(\tau t)=B(t)\).

**Theorem 3 (intrinsic oddness as a path integral).** Suppose \(B\) satisfies Theorem 2 and is \(\tau\)-invariant. Then there exists one bit \(\omega_\tau(B)\in\mathbb F_2\), independent of the graph edge \(e\), such that
\[
\boxed{\omega_\tau(B)=\delta_B(e,\tau e)
=c(e)+c(\tau e).}
\tag{3}
\]
It is independent of the choice of the reconstructed edge coloring \(c\). In particular,
\[
\boxed{\omega_\tau(B)=1
\quad\Longleftrightarrow\quad
c(\tau e)=1-c(e)\ \text{for all }e\in E(G).}
\tag{4}
\]

*Proof.* Let \(h(e)=c(e)+c(\tau e)\). For adjacent \(e,f\) in \(T(G)\),
\[
h(e)+h(f)
=B(\{e,f\})+B(\{\tau e,\tau f\})=0
\]
by invariance. Connectivity of \(T(G)\) makes \(h\) constant. By Theorem 2 this constant equals the path integral \(\delta_B(e,\tau e)\). Replacing \(c\) by \(c+1\) leaves \(h\) unchanged. The equivalence (4) follows. \(\square\)

For a nontrivial canonical polarity \(\eta\) involving at least two two-element factors, \(\eta\) acts freely on \(E(G)\). The class \(\omega_\eta(B)=1\) is therefore possible: assign arbitrary complementary colors on the two-member orbits of \(\eta\), and construct \(B\) using (1). Formula (3) recovers the familiar nontrivial deck parity entirely from commuting-turn data, without introducing a separate chosen edge coloring.

## A graph-and-matroid intrinsic turn system

For \(k\ge2\), equip every ordered nonbacktracking turn \((u,v,w)\) with a bit \(b(u,v,w)\) subject to:

(C1) if \(u,w\) are nonadjacent, then \(b(u,v,w)=b(w,v,u)\); these common values form \(B:E(T(G))\to\mathbb F_2\) satisfying the cycle condition of Theorem 2;

(C2) if \(u,w\) are adjacent, then \(b(u,v,w)+b(w,v,u)=1\), with no other restrictions on these triangular comparisons;

(C3) when the canonical polarity \(\eta\) is nontrivial, \(B\) is \(\eta\)-invariant and \(\omega_\eta(B)=1\).

Define an **accepted resource gallery** to be a path \(P=(v_0,\ldots,v_\ell)\) whose graph edges are independent in the uniquely determined triangle–square resource matroid \(R(G)\) of the preceding Article XI Subsection and for which, at every internal vertex, both
\[
b(v_{j-1},v_j,v_{j+1})=0,\qquad
\delta_B(v_{j-1}v_j,v_jv_{j+1})=0.
\tag{5}
\]
The second constraint is intrinsic by Theorem 2. On nontriangular turns, the two constraints coincide.

For the one-factor case \(G=K_m\), the commuting-turn graph has no edges. Use instead the intrinsic triangular rule \(b(a,v,c)+b(c,v,a)=1\) and define an accepted gallery using the first constraint of (5) alone. This is the boundary-tournament specialization and involves no edge-color potential.

**Corollary 4 (faithful decoding of the canonical examples).**

(a) For \(M=\bigoplus_{i=1}^nU_{1,2}\), \(n\ge2\), its rank-one root is \(G=Q_n\) and its canonical polarity is cube complementation. Every nonbacktracking turn is commuting, so the turn bit is \(\delta_B(e,f)\). A turn system satisfying (C1)--(C3) is equivalent, up to simultaneous exchange of the color names, to an arbitrary antipodally odd binary coloring of undirected cube edges. The accepted resource galleries are its monochromatic coordinate-distinct geodesics. In particular, a gallery of length \(n\) is a monochromatic antipodal geodesic.

(b) For \(M=U_{2,n}\), \(n\ge3\), the root is \(G=K_n\), and the canonical polarity is the identity. Every nonbacktracking turn is triangular. The turn rule is precisely an arbitrary reversal-odd boundary 3-tournament on distinct ordered triples, and the accepted resource galleries are its monochromatic vertex-simple tight paths.

*Proof.* Part (a) follows from Theorems 2--3 and the triangle–square rigidity characterization \(R(Q_n)\) as the coordinate-direction partition matroid. Part (b) follows from the absence of commuting turns in a complete graph and \(R(K_n)=M(K_n)\), whose independent paths are precisely the vertex-simple paths in the original complete graph. \(\square\)

**Corollary 5 (a turn-only unified conjecture).** Let \(\mathcal C_{\rm can}\) be the intrinsic partition-matroid class whose number \(s\) of two-element connected components satisfies \(s=0\) or \(s\ge2\). Let \(G=\Gamma(M^\flat)\), \(k\) be its Cartesian-factor count, and \(d=\operatorname{rk}R(G)\). Use the turn-only systems (C1)--(C3) for \(k\ge2\) and the unrestricted triangular turn system for \(k=1\). The single quantitative conjecture
\[
\boxed{
L\ge\max\left\{
\left\lceil\frac{k}{2}\right\rceil,
\left\lceil\frac{\sqrt d}{2}\right\rceil,
s
\right\}
}
\tag{6}
\]
for an accepted resource gallery is equivalent to NORI1.

*Proof.* The factor-count bound \(\lceil k/2\rceil\) is already established for arbitrary edge colors on Hamming products by the monochromatic factorwise transfer theorem in Article XI. The resource-rank bound \(\lceil\sqrt d/2\rceil\) is established by the cycle-dominating resource-matroid terminal theorem. Both apply to the reconstructed \(c\) by Theorem 2, and for \(k=1\) the rank theorem applies directly to the unrestricted local tournament. If \(s\ge2\), the canonical polarity acts by simultaneous complementation of all binary factors and fixes the remaining factors. Under NORI1, restrict the reconstructed odd coloring to a cube obtained by retaining those binary factors and fixing the others. A monochromatic \(s\)-edge antipodal geodesic on that slice is resource-independent and accepted, giving the third bound. Conversely the pure cube case has \(k=s=d=n\), so (6) forces a monochromatic antipodal geodesic and hence NORI1. \(\square\)

The reconstructed color bit is a gauge choice: changing it globally affects none of the turn data, holonomy, or accepted galleries. Thus both the resource matroid and the antipodal color law can be specified using intrinsic circuit geometry and a binary turn cocycle. The nontrivial remaining mathematical task is the full-rank path-existence theorem for such unrestricted polarized turn systems.

## Dimension of the intrinsic odd-holonomy space

**Theorem 6 (two cosets of invariant commuting-turn cuts).** Let \(\tau\) be a fixed-point-free involution on the vertices of the connected graph \(T(G)\), induced by a factor-preserving graph involution of \(G\). Put \(2m=|V(T(G))|=|E(G)|\), and let \(\mathcal B^\tau\) be the vector space of \(\tau\)-invariant edge functions \(B:E(T(G))\to\mathbb F_2\) whose sum around every graph cycle vanishes. Then
\[
\boxed{\dim_{\mathbb F_2}\mathcal B^\tau=m.}
\tag{7}
\]
The map \(B\mapsto\omega_\tau(B)\) is a surjective linear functional on this space. Its two fibers have
\[
\boxed{|\{B\in\mathcal B^\tau:\omega_\tau(B)=\epsilon\}|
=2^{m-1}\quad(\epsilon\in\mathbb F_2).}
\tag{8}
\]
In particular, antipodally odd edge colorings modulo simultaneous exchange of the two colors correspond bijectively to the nonzero-holonomy fiber.

*Proof.* By Theorem 2, the cycle-zero cochains on \(T(G)\) are precisely the image of the graph coboundary map \(d:C^0(T(G);\mathbb F_2)\to C^1(T(G);\mathbb F_2)\), whose kernel consists of the two constant vertex functions. By Theorem 3, \(dc\) is \(\tau\)-invariant precisely when \(c+\tau c=\alpha\mathbf1\) for some \(\alpha\in\mathbb F_2\), and then \(\omega_\tau(dc)=\alpha\). On each of the \(m\) two-element vertex orbits of \(\tau\), choose the value of \(c\) at one representative freely; the other value is forced to be \(c+\alpha\). Thus all such potentials \(c\), allowing either \(\alpha\), form an \((m+1)\)-dimensional vector space. Quotienting by the one-dimensional constant kernel of \(d\) gives dimension \(m\), proving (7). Both values of \(\alpha\) occur (choose representative values all zero, and then choose either value of \(\alpha\)), so \(\omega_\tau\) is surjective, with kernel of dimension \(m-1\). This proves (8). \(\square\)

For the canonical cube \(Q_n\), \(n\ge2\), the commuting-turn graph has \(|E(Q_n)|=n2^{n-1}\) vertices and its antipodal involution pairs them freely, so \(m=n2^{n-2}\). Thus the entire unrestricted space of antipodally odd edge colorings, modulo exchanging the colors, is a single nonzero-holonomy coset of cardinality \(2^{n2^{n-2}-1}\). No regularity restriction is imposed on the colorings.
