# An explicit antipodally odd labeling localizes every balanced ridge to one direction

# The balanced-ridge theorem can be supported on one arbitrary root-slide coordinate

Fix \(n\ge2\) and an arbitrary coordinate \(j\in[n]\). Define an odd vertex labeling
\[
\ell_j(x)=\big((-1)^{x_i}\big)_{i\in[n]\setminus\{j\}}\in\mathbb R^{n-1}.
\]
Indeed \(\ell_j(\bar x)=-\ell_j(x)\).

**Theorem (one-coordinate localization).** For an \((n-1)\)-edge cube geodesic ridge \(R\), one has
\[
0\in\operatorname{conv}\{\ell_j(v):v\in R\}
\quad\Longleftrightarrow\quad
\text{the unique UNUSED coordinate of \(R\) is \(j\)}.
\]
Thus all balanced root-slide ridges of this labeling are supported on the edges of the folded-cube root graph in direction \(j\). Their root-pair graph has no component larger than two vertices. This localization persists at the level of *eligible directions* under sufficiently small generic odd perturbations of the labels.

**Proof.** Let \(k\) be the unused coordinate. If \(k\ne j\), the \(k\)-th component of \(\ell_j(v)\) is constant, either \(+1\) or \(-1\), over every \(v\in R\), so zero cannot lie in their convex hull. If \(k=j\), the endpoints \(u,v\) of \(R\) differ on precisely all coordinates outside \(j\), hence \(\ell_j(v)=-\ell_j(u)\). Their image segment contains the origin, proving balancedness. Every ridge with unused coordinate \(j\) is shared between root pairs \(e_x=\{x,\bar x\}\) and \(e_{x\oplus e_j}\), and the fixed-direction edges \(e_x e_{x\oplus e_j}\) form a perfect matching of the folded n-cube. For a perturbation with all coordinate deviations less than one in absolute value, ridges missing \(k\ne j\) retain their strictly constant-sign \(k\)-th component; arbitrary sufficiently small generic equivariant perturbations therefore retain the claimed directional exclusion. \(\square\)

**Consequence for the fixed-point project.** Dimension-\((n-1)\) Borsuk–Ulam zeros and odd-degree parity at every root do not, by themselves, imply traversal of more than ONE root-change coordinate or long-distance collective repair. A coloring-dependent label must supply substantial new constraints on which coordinate directions can carry balanced ridges. Combined with the valid exterior-parity coloring whose good roots can be Hamming distance roughly \(n/2\) from a prescribed root, this shows why bare root-slide parity alone cannot produce the geodesic witness. One should seek a *multi-coordinate* obstruction, or constraints tying \(\ell\) to actual colored directed reachability, rather than interpreting the odd-degree graph itself as a long global connector.
