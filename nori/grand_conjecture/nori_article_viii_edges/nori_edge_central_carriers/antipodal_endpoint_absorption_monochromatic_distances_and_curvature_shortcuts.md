# Antipodal endpoint absorption, monochromatic distances, and curvature shortcuts

# Antipodal endpoint absorption and curvature-sensitive shortening

Let \(n\ge3\) and let \(c\) be an arbitrary coloring of the undirected edges of \(Q_n\) by \(0,1\), satisfying \(c(\bar e)=1-c(e)\). A *monochromatic antipodal path* joins \(x\) to \(\bar x=x+\mathbf1\) with all edges of one color. Write \(d_a(u,v)\) for the graph distance in the color-\(a\) subgraph, with value \(+\infty\) when the vertices are disconnected, and set \(d_*(u,v)=\min\{d_0(u,v),d_1(u,v)\}\). The 2026 Wu--Yang monochromatic antipodal path theorem guarantees that at least one such path exists. All shortening statements below are independent of that existence theorem.

## 1. Antipodal two-color path absorption

**Theorem 1 (antipodal endpoint absorption).** Let \(P=P_1P_2\) be a monochromatic color-\(a\) path from \(x\) to \(\bar x\), with the two consecutive segments meeting at \(z\), of lengths \(p\) and \(q\). If \(Q\) is a monochromatic path of either color from \(z\) to \(\bar x\) with length \(s<q\), then there is a monochromatic color-\(a\) antipodal path of length at most \(p+s<p+q\). The same conclusion holds if \(Q\) goes from \(x\) to \(z\) with length \(s<p\), giving length at most \(q+s\). The conclusion does not assume that the new root equals \(x\).

**Proof.** If the first replacement path \(Q\) has color \(a\), concatenate \(P_1\) and \(Q\) to obtain a color-\(a\) walk \(x\to\bar x\). If \(Q\) has color \(1-a\), its antipodal translate \(\bar Q\) is a color-\(a\) path from \(\bar z\) to \(x\), since the antipodal image of \(Q:z\to\bar x\) has endpoints \(\bar z\to x\). Concatenating \(\bar Q\) with \(P_1:x\to z\) yields a color-\(a\) walk from \(\bar z\) to \(z\), of length \(s+p\). In either case, remove closed subwalks when necessary to obtain a color-\(a\) path of no greater length. The prefix version follows on reversing \(P\), or by applying the same argument to the opposite end. \(\square\)

**Corollary 2 (two-color endpoint rigidity).** Let \(P=(v_0,\ldots,v_L)\) be a shortest monochromatic antipodal path over all roots and both colors. Then for every \(0\le t\le L\),
\[
\boxed{d_*(v_0,v_t)=t,\qquad d_*(v_t,v_L)=L-t.}
\tag{1}
\]
In particular every prefix and suffix of \(P\) is a shortest path between its endpoints simultaneously in its own color and relative to the better of the two monochromatic path distances.

**Proof.** The indicated portions of \(P\) establish the upper inequalities. A strict lower inequality would provide a shorter monochromatic connecting path of one of the two colors, contradicting Theorem 1. \(\square\)

**Corollary 3 (terminal-ear deletion in any defect).** If a monochromatic antipodal path ends with a consecutive three-edge direction word \((i,j,i)\), where \(i\ne j\), then it admits a strictly shorter monochromatic antipodal path, of length smaller by at least two. The same holds for an initial \((i,j,i)\).

**Proof.** The beginning and end of the three-edge suffix differ only in dimension \(j\). The single edge joining them is monochromatic in one of the two colors, has length one, and replaces a suffix of length three by Theorem 1. Reversal handles the prefix. \(\square\)

More generally, if a terminal subpath of length \(q>1\) begins at a vertex adjacent to the endpoint, the entire path can be shortened by at least \(q-1\). Consequently a globally shortest monochromatic antipodal path has no vertex adjacent to either endpoint except the neighboring vertex along the path itself.

## 2. Curvature of short endpoint shortcuts

For distinct dimensions \(i,j\) define the square curvature
\[
\kappa_{ij}(u)
=c_i(u)+c_j(u+e_i)+c_i(u+e_j)+c_j(u)\pmod2.
\tag{2}
\]
It is the parity of the four edge colors around the square with diagonal endpoints \(u,u+e_i+e_j\).

**Lemma 4 (curved squares provide monochromatic diagonals).** If \(\kappa_{ij}(u)=1\), then precisely one of the two length-two geodesics from \(u\) to \(u+e_i+e_j\) is monochromatic.

**Proof.** The indicators that the orders \(i,j\) and \(j,i\) change color are
\[
s_1=c_i(u)+c_j(u+e_i),\qquad
s_2=c_j(u)+c_i(u+e_j)
\quad(\bmod2).
\]
Their sum is \(\kappa_{ij}(u)\). When it equals one, precisely one \(s_k\) vanishes, which is equivalent to monochromaticity of the corresponding two-edge path. \(\square\)

**Theorem 5 (curvature exclusion along shortest antipodal paths).** If \(P=(v_0,\ldots,v_L)\) is a globally shortest monochromatic antipodal path and \(v_t=v_0+e_i+e_j\) for distinct dimensions \(i,j\), with \(t>2\), then
\[
\boxed{
c_i(v_0)\ne c_j(v_0+e_i),\qquad
c_j(v_0)\ne c_i(v_0+e_j),\qquad
\kappa_{ij}(v_0)=0.
}
\tag{3}
\]
The analogous assertion holds when \(v_t\) is at Hamming distance two from \(v_L\) but the terminal path segment has length greater than two. In particular, nonzero curvature on the corresponding square supplies an explicit strictly shorter monochromatic antipodal path by Theorem 1.

**Proof.** If either of the two length-two geodesics from \(v_0\) to \(v_t\) were monochromatic, its length two would contradict (1), since \(t>2\). Thus both are mixed, giving the first two inequalities. Their indicator sum is the square curvature, so it vanishes. Reversal proves the terminal version. \(\square\)

For a shortest path of length \(n+2\), a terminal three-edge ear \((i,j,i)\) therefore forces a full monochromatic antipodal geodesic in the original coloring: Theorem 1 produces an antipodal monochromatic path of length at most \(n\), while Hamming distance forces its length to equal \(n\). The same argument applies when a length-four prefix or suffix revisits a square diagonal at Hamming distance two and the square has curvature one.

## 3. A global two-color distance inequality

**Proposition 6 (min-plus antipodal absorption).** If \(L_{\min}(c)\) denotes the minimum length of a monochromatic antipodal path in \(c\), then for every \(x,z\in Q_n\),
\[
\boxed{
L_{\min}(c)\le d_*(x,z)+d_*(z,\bar x)
}
\tag{4}
\]
whenever both distances are finite. Moreover,
\[
\boxed{
L_{\min}(c)=\min_{x,z}\bigl(d_*(x,z)+d_*(z,\bar x)\bigr).
}
\tag{5}
\]

**Proof.** Choose monochromatic shortest paths for the two terms in (4). If their colors agree, concatenate them directly. If they disagree, antipodally translate the path of the opposite color and concatenate as in Theorem 1, now without requiring a pre-existing monochromatic antipodal path. The resulting monochromatic antipodal walk has length equal to the sum of the two distances, and removing loops gives (4). For equality in (5), take any globally shortest monochromatic antipodal path and set \(z\) equal to one of its vertices. Corollary 2 makes the two terms sum to its length. \(\square\)

Since \(\operatorname{dist}_{Q_n}(x,z)+\operatorname{dist}_{Q_n}(z,\bar x)=n\) for every \(z\), formula (5) isolates the accumulated excess of monochromatic path distance over Hamming distance. Theorem 5 gives a curvature-sensitive sufficient condition for reducing this excess in the original coloring.

These theorems supply a dimension-uniform path-shortening operation and constraints on globally shortest witnesses. A proof that every positive-excess minimizer contains an admissible monochromatic endpoint shortcut would establish the full-geodesic NORI1 statement; that remaining assertion is not proved here.
