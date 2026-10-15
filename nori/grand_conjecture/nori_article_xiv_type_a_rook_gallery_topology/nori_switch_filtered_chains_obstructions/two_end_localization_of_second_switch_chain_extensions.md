# Two-end localization of second-switch chain extensions

# Two-end localization via an equivariant acyclic carrier

Continue the dimension-simple second-switch construction of Article XIV. Let \(n\ge4\), and assume hypothetically that every full rooted antipodal geodesic has at least two switches. Each type-\(B_n\) chamber \(g=(x,\pi)\) receives
\[
L(g)=(-1)^{w_1(g)}e_{s_2(g)}
\in \partial\mathcal O,\qquad
\partial\mathcal O\cong S^{n-3},
\tag{1}
\]
where \(\mathcal O=\operatorname{conv}\{\pm e_2,\ldots,\pm e_{n-1}\}\). The labeling is antipodally odd, and adjacent chambers have nonopposite labels; hence it extends linearly along the dual Coxeter 1-skeleton.

Write \(s_0\) for the generator flipping the sign of the first dimension, and \(s_i\) (\(1\le i<n\)) for exchanging dimensions in positions \(i,i+1\). A dual Coxeter cell \(D=gW_J\) is indexed by a parabolic coset with \(J\subseteq\{0,\ldots,n-1\}\), and its vertices are the chambers in that coset.

**Theorem 1 (fixed-terminal-edge hemisphere).** Let \(\mathcal P\) be any family of complete rooted geodesics such that every member traverses the same undirected edge in its **final** step. If each word has at least two switches, the labels (1) of all members lie in one closed hemisphere of the target crosspolytope sphere. Specifically, if the common final-edge color is \(b\), then
\[
L(\mathcal P)\subseteq
H_b:=\partial\mathcal O\cap
\{z:(-1)^b z_{n-1}\ge0\}.
\tag{2}
\]
This hemisphere is a closed \((n-3)\)-ball. Any boundary map built from these labels and carried inside \(H_b\) admits a filling within the same hemisphere.

*Proof.* A label with second-switch index \(r<n-1\) has zero component along \(e_{n-1}\). If the second switch is at \(r=n-1\), then the full path has two switches and therefore \(w_1=w_n=b\), giving label \((-1)^b e_{n-1}\). Thus no label has the excluded opposite sign of the last axis. The crosspolytope boundary is the union of two closed hemispherical balls cut out by the last-axis hyperplane, and each is contractible. \(\square\)

**Theorem 2 (equivariant acyclic carrier on two-end-stable parabolic cells).** Let \(X_{\mathrm{good}}\) be the union of the closed dual Coxeter cells \(D=gW_J\) satisfying at least one of
\[
1\notin J,\qquad\text{or}\qquad 0\notin J\text{ and }n-1\notin J.
\tag{3}
\]
This is an antipodally invariant subcomplex containing the entire dual 1-skeleton. Under the same hypothetical assumption, the signed second-switch map on its vertices and dual edges extends to an antipodally equivariant continuous map
\[
F_{\mathrm{good}}:X_{\mathrm{good}}\longrightarrow S^{n-3}.
\tag{4}
\]
More precisely the extension admits a family of contractible target carriers, nested under inclusion of source cells, and therefore induces an equivariant augmentation-preserving chain map on the cellular chains of \(X_{\mathrm{good}}\).

*Proof.* If \(1\notin J\), all generators in \(J\) preserve the same initial undirected cube edge: \(s_0\) interchanges its endpoints, and the swaps \(s_i\) for \(i\ge2\) preserve both root and first dimension. Hence the first color bit \(a\) is fixed over the cell, and all its second-switch labels lie in the simplex
\[
\Delta_a=\operatorname{conv}\{(-1)^a e_2,\ldots,(-1)^a e_{n-1}\}
\subset\partial\mathcal O.
\tag{5}
\]

If \(0,n-1\notin J\), then the root and the last dimension are fixed throughout the cell. All permutations in this parabolic coset merely rearrange the first \(n-1\) dimensions, so the endpoint just before the last step is also fixed. Hence its last undirected edge, with color \(b\), is common to every chamber in the cell. Theorem 1 supplies the contractible carrier \(H_b\).

We now choose carriers compatible with **all** face inclusions, including intersections of these two classes of cells. For a cell with only the first-edge invariance, choose \(\Delta_a\). For a cell with last-edge invariance but no first-edge invariance, choose \(H_b\). For a cell with both invariances, choose \(\Delta_a\) if \(a=b\), and otherwise choose the face
\[
\Delta_a'=\operatorname{conv}
\{(-1)^a e_2,\ldots,(-1)^a e_{n-2}\}.
\tag{6}
\]
When \(a\ne b\), no vertex label on that cell can use \(e_{n-1}\), since a second switch at \(n-1\) would force \(w_1=w_n\). Therefore every vertex label lies in the selected carrier. All selected carriers are nonempty and contractible.

Let \(D'\) be a face of \(D\). Fixedness of either terminal edge on \(D\) is inherited by \(D'\), with the same bit. If \(D\) has a first-edge carrier, the carrier of \(D'\) is equal to it or one of its faces. If \(D\) has a last-edge hemisphere, the carrier of \(D'\) is either the same hemisphere or a first-color simplex lying inside it; the exclusion in (6) is precisely what guarantees this inclusion when the two endpoint bits differ. Hence the carriers are nested under face inclusion.

The antipodal involution complements first-edge and last-edge colors, and sends every selected carrier to its negative, so the carrier assignment is equivariant. On 0-cells the vertex labels lie in their assigned carriers; on 1-cells their nonopposite endpoint labels span target edges lying in those carriers. Inductively extend an attaching sphere over each higher-dimensional dual cell inside its contractible carrier, choosing representatives of free antipodal cell pairs and translating the extensions by the antipodal map. This constructs (4), with its prescribed 1-skeleton values. Passing to induced cellular chains, or working directly with compatible singular chains inside the carriers, produces an equivariant augmentation-preserving chain map. \(\square\)

**Corollary 3 (where the remaining obstruction can live).** The complement of \(X_{\mathrm{good}}\) among the dual Coxeter cells consists only of cells whose parabolic type \(J\) satisfies
\[
\boxed{1\in J\quad\text{and}\quad(0\in J\ \text{or}\ n-1\in J).}
\tag{7}
\]
In particular, the entire root-preserving parabolic complex that permutes the first \(n-1\) dimensions while fixing the last edge admits the extension of Theorem 2. The rank-two \(s_1,s_2\) braid hexagons are a special case of this last-edge filling, whereas the commuting square \(\{s_1,s_3\}\) in \(B_4\) is outside it, because \(s_3=s_{n-1}\) changes the last edge.

**Research significance and limits.** Wu and Yang's chain-level argument requires a globally equivariant chain map into a sphere of smaller dimension. Theorem 2 constructs a topologically and chain-theoretically valid part of such a map for the unrestricted dimension-simple cube-geodesic flags. The remaining cells must be filled compatibly with the already fixed boundary chains, while retaining the required rank-sensitive coloring relations. It is not legitimate simply to cone them in arbitrary target hemispheres: some have opposite labels and no common fixed first or last edge. The central proof obligation has therefore been localized simultaneously to an **initial exchange** and one of the **two ends of the complete path**. The theorem does not by itself prove NORI1 or settle the corresponding boundary-tournament one-switch conjecture.
