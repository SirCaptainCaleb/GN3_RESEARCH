# Article I — Antipodal-reversal-odd geodesic colorings of the cube

Let \(Q_n=\{0,1\}^n\). An ordered three-face \((F,\pi)\) consists of a three-dimensional cube face \(F\) and an ordering \(\pi\) of its three free directions. A binary coloring \(c\) is **antipodal-reversal odd** when \(c(\bar F,\operatorname{rev}\pi)=1\oplus c(F,\pi)\), where \(\bar F\) complements every cube coordinate. Along an antipodal geodesic, obtained by changing each coordinate exactly once, record the colors of the consecutive length-three windows. The grand conjecture asks for a geodesic whose color word changes at most once. This formulation includes the coordinate-only, reversal-odd ternary problem; color values may depend on all fixed exterior coordinates of \(F\).

**Lemma 1 (unrestricted dimension five).** Every binary coloring of ordered three-faces of \(Q_5\), with no symmetry hypothesis, has a five-direction antipodal geodesic with at most one change.

**Proof.** Otherwise every color word on a five-direction geodesic would be \(010\) or \(101\), so its first and third colors agree. For a fixed coordinate order \((a,b,c,d,e)\), the first window color depends only on the fixed \(d,e\)-bits, while the third depends only on the fixed \(a,b\)-bits (after the first two directions have been toggled). Independence of those four bits forces each of these two window colors to be constant over all face positions. As every ordered triple occurs as the first window of some five-coordinate order, the entire coloring depends only on ordered triples, say \(h(a,b,c)\). Universal failure would force \(h(a,b,c)\ne h(b,c,d)\) for every five-distinct order. Applying this to the five cyclic rotations of \((a,b,c,d,e)\) alternates binary labels around an odd 5-cycle, impossible. \(\square\)

**Lemma 2 (six-path forcing).** Fix distinct directions \(a,b,c,d,e,f\), and a four-edge based path through the first four directions \(a,b,c,d\) whose two ordered-three-face window colors agree. Write its starting bits as \(x=(A,B,C,D,E,F)\) in coordinate order \((a,b,c,d,e,f)\), and use \(\bar A=1\oplus A\), etc. At least one of the following six *complete* antipodal geodesics has at most one color change:

| Direction order | Starting bits |
|---|---|
| \(a\,b\,c\,d\,e\,f\) | \(A,B,C,D,E,F\) |
| \(d\,c\,b\,a\,e\,f\) | \(A,B,C,D,\bar E,\bar F\) |
| \(d\,c\,b\,a\,f\,e\) | \(A,\bar B,\bar C,D,\bar E,\bar F\) |
| \(d\,c\,b\,f\,e\,a\) | \(A,\bar B,\bar C,\bar D,\bar E,\bar F\) |
| \(d\,e\,f\,a\,c\,b\) | \(\bar A,\bar B,\bar C,\bar D,E,F\) |
| \(d\,e\,f\,b\,c\,a\) | \(\bar A,\bar B,\bar C,D,\bar E,\bar F\) |

**Proof.** Complement all colors if necessary so that the given four-edge path's two window colors are \(00\), and suppose all six full geodesics have at least two changes. Write \(W_i\) for the four-window word of table row \(i\). A bad four-window word beginning \(00\) equals \(0010\); one beginning \(11\) equals \(1101\); one beginning with \(1\) and ending with \(0\) equals \(1010\).

First \(W_1=0010\); its final \(def\) face has color 0. The first two windows of row 2 are antipodal reversals, respectively, of the second and first windows of row 1, so \(W_2=1101\), making its final \(aef\) window color 1. The first two windows of row 3 have the same antipodal-reversal relations; thus \(W_3=1101\), making its final \(afe\) window color 1. Row 4 starts with an antipodal reversal of row 1's second window (color 1), and ends with an antipodal reversal of row 2's final \(aef\) window (color 0); hence \(W_4=1010\), making its third \(bfe\) window color 1. Row 5 starts with the *same ordered face* \(def\) as row 1's last window (color 0), and its second \(efa\) window is the antipodal reversal of row 3's final \(afe\) window (color 0); thus \(W_5=0010\), making its last \(acb\) window color 0. Finally row 6 starts with the same ordered \(def\) face as row 1's final window (color 0), has second \(efb\) window antipodally reversed from row 4's third \(bfe\) window (color 0), and ends with \(bca\), antipodally reversed from row 5's last \(acb\) window (color 1). Therefore \(W_6=00*1\), which has at most one change, a contradiction.

To verify every equality and complement used, for an order \(p\) and starting bits \(y\), the window on \(p_i,p_{i+1},p_{i+2}\) has fixed bit \(y_t\oplus \mathbf1_{t\in\{p_1,\ldots,p_{i-1}\}}\) at each exterior coordinate \(t\). Substituting the six displayed starts yields exactly the asserted identical-face or antipodal-reversal pairs, including all three exterior bits. \(\square\)

**Theorem 3 (full NORI closure for \(n=6\)).** Every antipodal-reversal-odd coloring of ordered three-faces of \(Q_6\) has an antipodal geodesic whose color word changes at most once.

**Proof.** Fix any five-dimensional facet. Its induced coloring is arbitrary, so Lemma 1 supplies a five-direction geodesic with at most one change. Among its three consecutive window colors, some adjacent pair agrees. The corresponding contiguous four-edge subpath therefore has two equal window colors. Label those four directions \(a,b,c,d\) and the remaining two directions \(e,f\). Lemma 2 supplies one of six explicit full six-direction geodesics with at most one change. \(\square\)


## Exact change-vector certificates

Let \(Q_n=\{0,1\}^n\). Each ordered three-face \((F,\pi)\) has a binary color depending on its free-coordinate order \(\pi\) and the fixed exterior coordinate bits. For a coordinate order \(p=(p_1,\ldots,p_n)\) and an initial vertex \(x\), write \(w_1(x),\ldots,w_{n-2}(x)\) for the consecutive ordered-three-face colors and \(d_i(x)=w_i(x)\oplus w_{i+1}(x)\) for \(1\le i\le n-3\). A good antipodal geodesic is exactly one with Hamming weight \(|d(x)|\le1\).

**Theorem 1 (exact universal-flipper fiber law).** Partition the coordinate set as \(V=A\sqcup B\), with \(|A|=r\) and \(|B|=m\ge3\). Suppose that whenever an \(a\in A\) is fixed outside an ordered three-face, complementing its fixed bit complements the face color. Fix arbitrary coordinate orders \(\sigma\) of \(A\), \(\tau\) of \(B\), and an arbitrary starting vertex \(y\) in the \(B\)-coordinates. As the \(r\) initial \(A\)-bits vary, the complete change vectors on the full direction order \(\sigma\tau\) are **exactly**
\[
\bigl\{(u,\delta(\tau,y)):u\in\mathbb F_2^r\bigr\},
\]
each occurring exactly once. Here \(\delta(\tau,y)\in\mathbb F_2^{m-3}\) is the change vector along the induced \(B\)-geodesic, with \(A\)-bits omitted (their common fixed parity does not affect changes).

**Proof.** Write \(A=(a_1,\ldots,a_r)\), and let \(z_i\) be the initial bit at \(a_i\). The universal-flipper hypothesis implies
\[
 c(F,\pi)=\bigoplus_{a\in A\setminus\mathrm{free}(F)}x_a(F)\ \oplus\ g(\pi,x_{B\setminus\mathrm{free}(F)})
\]
for a function \(g\) independent of every fixed \(A\)-bit. The \(g\)-contribution \(G_i\) to window \(i\) is therefore determined by \(\sigma,\tau,y\) and independent of \(z\). For \(1\le i\le r\), shifting the three-coordinate window one position to the right fixes the departing \(a_i\) at its already toggled value \(1\oplus z_i\), and removes the untoggled arriving \(a_{i+3}\) if \(i+3\le r\). Consequently
\[
 d_i=G_i\oplus G_{i+1}\oplus 1\oplus z_i
 \oplus\mathbf1_{i+3\le r}z_{i+3}.
\]
For prescribed \(d_1,\ldots,d_r\), solve successively for \(z_r,z_{r-1},\ldots,z_1\). Each equation has coefficient one at the currently solved variable and only uses previously solved higher-index \(A\)-bits. The correspondence \(z\mapsto(d_1,\ldots,d_r)\) is bijective. For \(i>r\), both windows lie within \(B\); all \(A\)-bits have been toggled and contribute the same common parity to both colors. Thus \((d_{r+1},\ldots,d_{r+m-3})=\delta(\tau,y)\). This proves the claim. \(\square\)

**Corollary 1 (exact lifting count).** Put \(q=|\delta(\tau,y)|\). The number of choices of initial \(A\)-bits giving a full geodesic with at most one change is exactly \(r+1\) when \(q=0\), exactly \(1\) when \(q=1\), and \(0\) when \(q\ge2\). Thus a monochromatic residual geodesic admits \(r+1\) distinct good lifts, and a one-change residual geodesic admits one canonical good lift.

**Corollary 2 (complete equidistribution).** If \(m\le3\), then for every prescribed full change vector \(d\in\mathbb F_2^{n-3}\) and fixed coordinate order with \(A\) first, **exactly eight** of the \(2^n\) starting vertices realize \(d\). For \(m=3\), apply Theorem 1 and vary the eight \(B\)-starts. For \(m<3\), the same descending equations freely prescribe all \(n-3\) changes; the remaining \(3-m\) unused \(A\)-bits and the \(m\) \(B\)-bits supply exactly \(2^{3-m+m}=8\) starts. In particular there are exactly \(8(n-2)\) good starts and eight monochromatic starts per such order. The exterior-parity theorem is the special case \(A=V\).

**Theorem 2 (exact affine syndrome criterion).** More generally, suppose the ordered-face colors are affine Boolean functions of their fixed exterior bits. For each fixed direction order \(p\), write its change map as \(d(x)=Mx\oplus b\in\mathbb F_2^s\), where \(s=n-3\) and \(M\) has rank \(\rho\). Let \(H\) be any \((s-\rho)\times s\) matrix of full row rank with \(HM=0\), so \(\ker H=\mathrm{im}M\). Then a good geodesic with this direction order exists **if and only if**
\[
 Hb\in\{0,He_1,\ldots,He_s\}.
\]
Its number of good starting vertices is exactly
\[
 2^{n-\rho}\Bigl|\{0,e_1,\ldots,e_s\}\cap(b+\mathrm{im}M)\Bigr|.
\]
**Proof.** An attainable change vector is precisely an element of the affine coset \(b+\mathrm{im}M=\{v:Hv=Hb\}\), and every such vector has \(2^{n-\rho}\) preimages. The words of Hamming weight at most one are exactly \(0,e_1,\ldots,e_s\). \(\square\)

The syndrome test proves the codimension-at-most-one affine criterion immediately: when \(s-\rho\le1\), the syndromes of zero and the unit vectors cover the entire syndrome space. In dimension six, an affine coloring failing every antipodal geodesic must therefore have \(\mathrm{rank}(M_p)\le1\) for **every** direction order \(p\), an explicit rank-rigidity condition. For larger codimension, the missing syndrome \(Hb\) is the exact linear obstruction for a specified order.

All assertions here are unconditional on antipodal oddness. They concern the stated subclasses and per-order certificates; the grand ordered-three-face conjecture remains unresolved.

## Uncolored geodesic reachability

First consider binary colors on the undirected edges of \(Q_n\), with \(c(\bar e)=1-c(e)\). Put
\[
R(x)=\{z\in Q_n:\text{a monochromatic geodesic of either color joins }x\text{ to }z\},
\]
including the empty path. Reversing a path and complementing its vertices show, respectively, that \(z\in R(x)\) iff \(x\in R(z)\), and that \(R(\bar x)=\overline{R(x)}\).

**Proposition (exact antipodal overlap).** A monochromatic antipodal geodesic exists iff \(R(x)\cap R(\bar x)\ne\varnothing\) for some \(x\), equivalently iff some \(R(x)\) contains an antipodal pair.

**Proof.** If \(z\) belongs to the intersection, take monochromatic geodesics \(x\to z\) and \(z\to\bar x\), reversing the second witness if necessary. Each coordinate differs in exactly one of the endpoint pairs \((x,z)\) and \((z,\bar x)\), so their supports are complementary. Their concatenation is therefore an antipodal geodesic with at most one color change. If its two blocks have different colors \(q,r=1-q\), start at their junction \(z\), follow the \(r\)-block to \(\bar x\), then follow the antipodal copy of the \(q\)-block to \(\bar z\). Both blocks now have color \(r\), and their disjoint supports still use every coordinate once. This is a monochromatic antipodal geodesic. Conversely, a monochromatic path \(x\to\bar x\) puts both endpoints in \(R(x)\), hence also yields the stated overlap. \(\square\)

The topological label can consequently be the uncolored set \(R(x)\). Its extraction uses only actual membership. For example, putting each physical target \(z\) at a distinct vertex \(e_z\) of a simplex gives faces \(\operatorname{conv}\{e_z:z\in R(x)\}\) whose intersection is exactly the face on the common targets.

## Exact reduction of the target alphabet

Let \(G\) be the reflexive graph on \(Q_n\) with \(x\sim z\) iff \(z\in R(x)\). Every edge of \(G\) has a monochromatic geodesic witness in the physical cube. Antipodal complementation \(\tau x=\bar x\) is an automorphism. For a nonempty \(\tau\)-invariant subset \(W\) of physical vertices, set
\[
N_W(x)=R(x)\cap W,\qquad
K_W=\{\sigma\subseteq W:\sigma\subseteq N_W(x)\text{ for some }x\in W\}.
\]
Thus a simplex of \(K_W\) has a common reachable root; the witnesses to its different targets may have different colors. The graph on \(W\) is induced from \(G\), so its witnesses may pass through physical vertices outside \(W\).

**Theorem (maximal-neighborhood compression).** Suppose that no antipodal overlap exists. Choose one representative of each distinct inclusion-maximal set among the neighborhoods \(R(z)\), in antipodal pairs, and call the representative set \(D\). There is an equivariant retraction \(m:Q_n\to D\) satisfying \(R(z)\subseteq R(m(z))\). For every root \(x\),
\[
m(R(x))\subseteq R(x).
\]
Moreover, for every finite nonempty family \(X\) of roots,
\[
\bigcap_{x\in X}R(x)\ne\varnothing
\quad\Longleftrightarrow\quad
\bigcap_{x\in X}\bigl(R(x)\cap D\bigr)\ne\varnothing.
\]
The complex \(K_D\) is the induced subcomplex \(K_{Q_n}[D]\), and its realization is an equivariant strong deformation retract of \(|K_{Q_n}|\).

**Proof.** If a maximal neighborhood class were fixed by \(\tau\), then \(R(z)=R(\bar z)\); since \(z\in R(z)\), this would already give overlap. The maximal classes are therefore paired freely, so their representatives can be chosen equivariantly. Every neighborhood lies in a maximal one by finiteness. Choose \(m(z)\) accordingly, fixing representatives and pairing choices for \(z,\bar z\).

If \(z\in R(x)\), symmetry gives \(x\in R(z)\subseteq R(m(z))\), hence \(m(z)\in R(x)\). In particular, any target common to all roots of \(X\) can be replaced by its representative, proving the intersection equivalence.

If \(\sigma\subseteq R(x)\), then \(\sigma\cup m(\sigma)\subseteq R(x)\). Thus the identity and \(m\), as simplicial maps on \(K_{Q_n}\), are contiguous. A simplex \(\sigma\) with vertices in \(D\) and root \(x\) also has root \(m(x)\), since \(R(x)\subseteq R(m(x))\). This proves the induced-subcomplex assertion. In the standard simplex realization, the homotopy
\[
H_t(p)=(1-t)p+t|m|(p)
\]
stays in a simplex containing \(\sigma\cup m(\sigma)\), is equivariant, and fixes \(K_D\) pointwise. \(\square\)

Further reduction is possible after restricting the neighborhoods to the remaining vertices.

**Theorem (paired domination fold).** Let \(u,v\in W\), with \(v\notin\{u,\tau u\}\), and suppose \(N_W(u)\subseteq N_W(v)\). Delete \(u,\tau u\), obtaining \(W'\), and define
\[
f(u)=v,\quad f(\tau u)=\tau v,\quad f(s)=s\quad(s\in W').
\]
Then \(f:G[W]\to G[W']\) is an equivariant graph retraction,
\[
\exists x\in W:\ N_W(x)\cap N_W(\tau x)\ne\varnothing
\quad\Longleftrightarrow\quad
\exists y\in W':\ N_{W'}(y)\cap N_{W'}(\tau y)\ne\varnothing,
\]
and \(|K_{W'}|\) is an equivariant strong deformation retract of \(|K_W|\).

**Proof.** Equivariance supplies \(N_W(\tau u)\subseteq N_W(\tau v)\). For every \(s\in W\) we have \(N_W(s)\subseteq N_W(f(s))\). If \(a\sim b\), symmetry and these inclusions imply \(f(a)\sim b\) and then \(f(a)\sim f(b)\). Hence \(f\) is a graph homomorphism fixing \(W'\). A common neighbor \(z\) of \(x,\tau x\) maps to a common neighbor \(f(z)\) of \(f(x),\tau f(x)\); conversely the induced graph retains only original relations.

For a simplex \(\sigma\subseteq N_W(x)\), each \(s\in\sigma\) has \(x\sim s\), hence \(x\sim f(s)\). Therefore \(\sigma\cup f(\sigma)\) is a simplex of \(K_W\). If all vertices of \(\sigma\) lie in \(W'\), its root can be replaced by \(f(x)\), proving \(K_{W'}=K_W[W']\). The same linear homotopy as above gives the equivariant strong deformation retraction. \(\square\)

If \(N_W(u)\subseteq N_W(\tau u)\), reflexivity directly gives \(u\sim\tau u\), already a monochromatic antipodal geodesic. Otherwise paired deletions terminate at a finite core admitting no further domination. Each deletion preserves the overlap criterion and the entire equivariant homotopy type. In later folds the root and target of a certificate may move to remaining physical vertices; every retained graph edge continues to have its original cube-geodesic witness.

Under hypothetical failure of closure, no simplex of \(K_W\) contains \(z,\tau z\), since those two reachable targets would give closure. Thus its antipodal action is free. If the final core has \(2s\) vertices, its complex is an invariant subcomplex of the boundary of the \(s\)-dimensional crosspolytope, with one signed coordinate for each remaining antipodal pair. This provides a reduced exact label complex. A useful bound or structural theorem for such cores arising from cube reachability remains to be proved.

## Fixed palettes and their sharp size bound

Adaptive compression preserves every intersection. A second construction keeps a coloring-independent set of actual targets \(D\) and uses \(L_D(x)=R(x)\cap D\). Any antipodal overlap of these labels still gives closure.

**Theorem (universal fixed palettes).** For \(n\ge4\), the labels \(L_D(x)\) are nonempty for every root and every antipodally odd edge coloring iff \(D\) dominates the ordinary cube graph. In particular,
\[
|D|\ge\left\lceil\frac{2^n}{n+1}\right\rceil.
\]
For \(n=2^r-1\), \(r\ge3\), equality is attainable with an antipodally invariant palette.

**Proof.** Every \(R(x)\) contains the closed cube neighborhood \(B_1(x)\), so domination suffices. If \(D\) misses \(B_1(x)\), color every edge between distance layers \(0,1\) about \(x\) by \(0\), and every edge between layers \(1,2\) by \(1\). Prescribe opposite colors on their antipodal edges and extend over remaining edge orbits. The four layer pairs involved are \(0\!-\!1\), \(1\!-\!2\), \((n-2)\!-\!(n-1)\), and \((n-1)\!-\!n\), distinct for \(n\ge4\). Each first geodesic edge from \(x\) has color \(0\), and each second has color \(1\), so \(R(x)=B_1(x)\). Its palette label is empty. Since a target dominates \(n+1\) vertices, counting yields the bound.

For equality, let \(H\) be the \(r\times n\) matrix over \(\mathbb F_2\) containing each nonzero \(r\)-vector exactly once as a column, and take \(D=\ker H\). A nonzero syndrome \(Hx\) identifies a unique column \(H_i\), so flipping coordinate \(i\) puts \(x\) in \(D\). A zero syndrome already means \(x\in D\). Thus \(D\) dominates and has size \(2^{n-r}=2^n/(n+1)\). Each row has \(2^{r-1}\) ones, so \(H\mathbf1=0\) and \(D\) is antipodally invariant. \(\square\)

For \(n\ge5\) the lower bound exceeds \(n\). It applies to a universal fixed physical-target palette. The adaptive reduction above is governed by the actual coloring. Fixed palette restriction guarantees nonempty labels and sound extraction; preservation of every original intersection is the stronger property established by maximal-neighborhood compression.

## Genuine reachable sets with robust convex overlap

Identify cube vertices with subsets of \([n]\), and write \(\bar A=\{\bar S:S\in A\}\). A downset contains every subset of each of its elements.

**Theorem (exact downset realization).** Let \(A\) be a downset containing \(\varnothing\) and all singletons, with \(A\cap\bar A=\varnothing\). It occurs as the exact \(R(0)\) of an antipodally odd coloring whose edges at \(0\) all have color \(0\) iff \(d_H(A,\bar A)\ge2\).

**Proof.** In such a coloring every nonempty monochromatic path from \(0\) has color \(0\). An upward edge from \(U\in A\) to \(V\notin A\) must have color \(1\), since otherwise a geodesic to \(U\) extends to \(V\). If \(A,\bar A\) have adjacent vertices, downset closure forces their edge upward from \(A\) into \(\bar A\). Its antipodal edge also goes upward from \(A\) into \(\bar A\), forcing both colors to be \(1\), contrary to oddness.

Conversely, color every edge internal to \(A\) by \(0\), and every upward edge leaving \(A\) by \(1\). Their antipodes prescribe color \(1\) internally to \(\bar A\) and color \(0\) on upward edges entering \(\bar A\). Disjointness and the absence of edges between \(A,\bar A\) make these prescriptions consistent. Complete the remaining antipodal orbits with opposite colors. Every element of \(A\) is reached by an increasing path inside the downset, and no increasing color-\(0\) path can exit. All first edges have color \(0\), so color \(1\) reaches only the empty root. Hence \(R(0)=A\). \(\square\)

**Corollary (full-dimensional false convex coincidence in \(Q_{14}\)).** An antipodally odd edge coloring exists with
\[
R(0)\cap R(\mathbf1)=\varnothing,\qquad
[3/7,4/7]^{14}\subseteq
\operatorname{conv}R(0)\cap\operatorname{conv}R(\mathbf1).
\]

**Proof.** Split the coordinates into seven pairs \(B_p=\{2p-1,2p\}\). On the seven points take the lines
\[
123,\quad145,\quad167,\quad246,\quad257,\quad347,\quad356.
\]
Every two lines intersect and every point lies on three lines. Put \(D_L=\bigcup_{p\in L}B_p\), \(M_L=[14]\setminus D_L\), and
\[
A=\bigcup_L 2^{M_L}.
\]
Every singleton belongs to \(A\). If \(U\in A\) and \(V\in\bar A\), some line \(L\) has \(U\cap D_L=\varnothing\), while some line \(K\) has \(D_K\subseteq V\). Their common point supplies two coordinates absent from \(U\) and present in \(V\). Thus \(d_H(A,\bar A)\ge2\), and the realization theorem gives \(R(0)=A\), \(R(\mathbf1)=\bar A\).

Each coordinate belongs to exactly four of the seven \(M_L\), so their average is \((4/7)\mathbf1\). The convex hull of a downset is coordinatewise downward closed in the nonnegative orthant: if a coordinate of a generating vertex is \(1\), replacing it by \(0\) stays in the downset, and distributing these replacements across a convex combination produces any smaller coordinate. Consequently \([0,4/7]^{14}\subseteq\operatorname{conv}A\). Complementation gives \([3/7,1]^{14}\subseteq\operatorname{conv}\bar A\), proving the asserted overlap. In particular,
\[
\frac{0+\sum_L\mathbf1_{M_L}}8=\tfrac12\mathbf1
\]
expresses the center as the average of eight actual reachable vertices. \(\square\)

The common convex box contains a neighborhood of radius \(1/14\) in the maximum norm around the center. Thus even a convex coincidence with positive margin can occur without literal overlap at those roots. The exact simplicial label complex and its domination folds retain target membership throughout.

## Transfer to ordered three-face colors

Return to the active NORI coloring \(c(F,\pi)\), with \(c(\bar F,\operatorname{rev}\pi)=1-c(F,\pi)\). Ordinary reversal of a directed branch reverses its coordinate orders on the same physical faces; its window colors are therefore additional data. A compatible connector uses forward reachability and directed co-reachability.

**Proposition (two-window seam).** Let directed geodesics \(A:x\to z\) and \(B:z\to\bar x\) have lengths \(a,b\ge3\). Suppose their internal ordered-three-face words are respectively constant \(q,r\). Write their final two and first two directions as \((a_{a-1},a_a)\) and \((b_1,b_2)\). Let \(u,v\) be the colors of the actual ordered faces at the junction with direction orders
\[
(a_{a-1},a_a,b_1),\qquad(a_a,b_1,b_2).
\]
Then the full word is
\[
q^{a-2}\,u\,v\,r^{b-2}.
\]
It has at most one change iff \(u=v=q\) when \(q=r\), or iff
\[
(u,v)\in\{(q,q),(q,r),(r,r)\}
\]
when \(q\ne r\).

**Proof.** The branch supports are complementary because their endpoint pairs are \((x,z)\) and \((z,\bar x)\), so concatenation is a full geodesic. Exactly two three-edge windows cross the junction; they are the displayed ordered faces and have the exterior bits of \(z\). All other windows lie inside one branch. The binary word comparison gives the conditions. \(\square\)

The compression theorems above apply to the symmetric uncolored relation in the undirected edge case. A transfer to ordered three-face colors must construct a compatible directed relation or state complex that retains boundary direction memory and satisfies the seam condition. Establishing a topological forcing theorem for the reduced edge reachability core, and then a seam-compatible NORI lift, are the outstanding dimension-independent obligations.

For the ordered-three-face conjecture, the dimension-six forcing certificate also retains its exterior-bit extension obligation: higher-dimensional restrictions must realize both identical-face and antipodal-reversal comparisons with all fixed exterior coordinates. The conjecture in general dimension remains open.

## Reversed-terminal monochromatic reachability: an exact grand-conjecture reduction

For \(n\ge5\), fix a root \(x\), ordered distinct terminal directions \(J=(a,b)\), and \(D=[n]\setminus\{a,b\}\). Let \(\mathcal R_J(x)\) consist of nonempty supports \(U\subseteq D\) for which some **monochromatic ordered-three-face geodesic** from \(x\) has direction word
\[
(u_1,\ldots,u_k,a,b),\qquad\{u_1,\ldots,u_k\}=U.
\]
We deliberately forget the witness color, but retain the ordered terminal directions and the fact that the witness is a genuine geodesic.

**Theorem (exact reversed-two-tail extraction).** A full antipodal geodesic with at most one ordered-three-face color change exists if and only if
\[
\exists\,x,a,b,\ \varnothing\ne U\subsetneq D:
\qquad
U\in\mathcal R_{(a,b)}(x),\qquad
D\setminus U\in\mathcal R_{(b,a)}(x).
\tag{*}
\]

**Proof.** Let \(A\) and \(B\) be monochromatic witnesses with direction orders \((u_1,\ldots,u_k,a,b)\) and \((v_1,\ldots,v_m,b,a)\), with the supports of the \(u_i\) and \(v_j\) partitioning \(D\). The antipodal reversal of \(B\) has word \((a,b,v_m,\ldots,v_1)\); its initial vertex is
\[
\overline{x\oplus\chi_{D\setminus U}\oplus e_a\oplus e_b}
=x\oplus\chi_U,
\]
the vertex reached by the \(U\)-prefix of \(A\). Following that prefix by this reversal gives a full geodesic. Its first \(k\) ordered three-face windows are exactly those of \(A\), and its last \(m\) exactly those of reversed \(B\); since \(k+m=n-2\), no uncontrolled junction window exists. The two blocks are monochromatic (in possibly different colors), so at most one change occurs. Conversely, cut a good full geodesic between its monochromatic window blocks. Its prefix ending with the two shared directions \((a,b)\), and the antipodal reversal of its suffix ending with \((b,a)\), yield the two members of (*) rooted at the original start. A completely monochromatic full path permits any nontrivial interior cut. \(\square\)

This theorem replaces an inadequate arbitrary common-target picture by an **exact, dimension-independent** collision between *different* reversed-tail reachability families at the **same root**. Its proof also shows why ordered \(k\)-face windows require \(k-1\) terminal directions in the certificate.

### A faithful topological carrier is not yet a forcing theorem

A monochromatic witness \((u_1,\ldots,u_k,a,b)\) may drop an initial block of moves and slide its root forward; the remaining suffix is still monochromatic and retains its terminal pair and absolute endpoint. In root/support coordinates \(y_i=x_i\oplus U_i\), these certified slides occupy different *crossing diagonals* according to the conserved endpoint bit. Therefore a geometric crossing between root charts is not a certified intersection of witnesses, and independent slides need not preserve their common root.

The full-geodesic chamber complex is an \(n\)-dimensional closed pseudomanifold whose antipodal action fixes the midpoint of each antipodal endpoint edge. The two-moving-endpoint complex triangulates an \(n\)-torus. Neither geometry by itself meets the free-action or boundary hypotheses of a desired Borsuk–Ulam/Sperner/Tucker theorem. Two further obstructions preclude easy substitutions: the uncolored edge-reachability nerve need not fill every cube square, and an antipodally odd edge coloring may have \(|R(x)|<2^{n-1}\) for every root while still admitting a monochromatic antipodal geodesic. The labels must therefore preserve *actual monotone path incidence*, not just cardinalities or convex combinations.

### A second connector with a binary obstruction

Fix an \((n-2)\)-direction set \(U\), omitted directions \(a,b\), and a projected root \(r\in Q_U\). For \(i\in U\), define the **cap bit** \(A_i(r)\) as the color of the actual ordered face with free directions \((a,b,i)\) and exterior \(U\)-coordinates prescribed by \(r\). It is independent of the fixed values of \(a,b\). Form the four-facet **cap-memory graph** on \(U\), connecting first and last directions \(i,j\) of any monochromatic \(U\)-spanning geodesic in the four parallel facets based at projected root \(r\). Under the hypothesis of *no* good full geodesic, the proved first- and last-cap comparisons for a monochromatic core of color \(q\) imply
\[
q=A_i(r)=1\oplus A_j(r).
\]
Hence this graph would have to be bipartite. **An odd cycle in the actually witnessed graph forces grand closure.** Neither this theorem nor (*) currently ensures that the needed compatible connectors exist.

The open problem is to construct a dimension-independent equivariant fixed-point/connector carrier whose verified boundary and incidence conditions force either a same-root complementary pair in (*) or a nonbipartite four-facet cap-memory graph. A balanced simplex of abstract bit strings, a crossing of different endpoint sheets, or a zero of an interpolated map is not yet such an extraction. Thus the grand conjecture remains open beyond the established finite dimensions, but its most promising topological routes now have rigorous, explicit completion obligations.
