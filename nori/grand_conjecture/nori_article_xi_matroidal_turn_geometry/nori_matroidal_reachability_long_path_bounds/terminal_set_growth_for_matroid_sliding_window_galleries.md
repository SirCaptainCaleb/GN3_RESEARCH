# Terminal-set growth for matroid sliding-window galleries

Let \(M\) be a finite matroid of rank \(r\ge1\) on a ground set \(E\), with \(N=|E|\). Write \(\mathcal B(M)\) for its bases and \(\mathcal I_{r-1}(M)\) for its independent \((r-1)\)-sets. For each \(1\le j\le N-r\), choose an arbitrary binary coloring \(\beta_j\) of the oriented edges of the basis-exchange graph, satisfying
\[
\beta_j(B',B)=1-\beta_j(B,B')\qquad(B,B'\text{ adjacent}).\tag{1}
\]
A **sliding-window gallery** of order \(m\) is an injective word \(v_1,\ldots,v_m\), \(m\ge r\), for which each consecutive \(r\)-set
\[
B_i=\{v_i,\ldots,v_{i+r-1}\},\qquad1\le i\le m-r+1,
\]
is a basis. The gallery is **positive** if \(\beta_i(B_i,B_{i+1})=1\) for \(1\le i\le m-r\). The stage colorings \(\beta_i\) may vary independently.

**Theorem (terminal-set growth).** Let \(L\) be the maximum order of a positive sliding-window gallery. Then
\[
\boxed{|\mathcal B(M)|\le|\mathcal I_{r-1}(M)|(L-r+1)^2,\qquad
L\ge r-1+\sqrt{\frac{|\mathcal B(M)|}{|\mathcal I_{r-1}(M)|}}.}\tag{2}
\]
The conclusion requires neither representability nor simplicity nor an edge ordering.

*Proof.* Every basis supports a gallery of order \(r\), with no colored transitions. For each basis \(B\), let \(\ell(B)\) be the maximum order of a positive gallery terminating with the \(r\)-set \(B\). Choose such a gallery with final word \(x,s_1,\ldots,s_{r-1}\), and assign \(B\) to the independent set \(S=\{s_1,\ldots,s_{r-1}\}\). 

Fix an independent \((r-1)\)-set \(S\), an integer \(s\in\{r,\ldots,L\}\), and put
\[
U_{S,s}=\{x\notin S:S\cup\{x\}\text{ was assigned to }S,\ \ell(S\cup\{x\})=s\},\qquad q=|U_{S,s}|.
\]
If \(s=N\), then \(q\le N-r+1\le 2(s-r)+1\), so (3) follows immediately. Suppose henceforth that \(s<N\). The bases \(S\cup\{x\}\), \(x\in U_{S,s}\), form a complete exchange clique. Equation (1) makes \(\beta_{s-r+1}\) a tournament on this clique. Choose \(x\) having at least \((q-1)/2\) outgoing comparisons of color one. The selected \(s\)-element gallery for \(S\cup\{x\}\) ends in \(x,s_1,\ldots,s_{r-1}\). If an outgoing neighbor \(y\in U_{S,s}\) did not already occur in the gallery, appending \(y\) would preserve distinctness, add the valid basis window \(S\cup\{y\}\), and fulfill the prescribed positive stage comparison. This would give \(\ell(S\cup\{y\})\ge s+1\), a contradiction. Thus all favorable neighbors occur among the earlier \(s-r\) vertices, and
\[
(q-1)/2\le s-r,\qquad |U_{S,s}|\le2(s-r)+1.\tag{3}
\]
The number of bases assigned to \(S\) is at most
\[
\sum_{s=r}^{L}(2(s-r)+1)=(L-r+1)^2.
\]
Summing over all \(S\in\mathcal I_{r-1}(M)\) gives (2). \(\square\)

**Corollary 1 (uniform matroids of every rank).** For \(1\le r<n\), every reversal-odd coloring of oriented exchanges of \(U_{r,n}\) admits a positive injective sliding-window gallery with
\[
\boxed{L\ge r-1+\sqrt{\frac{n-r+1}{r}}.}\tag{4}
\]
The assertion remains valid for independently chosen reversal-odd colorings at every stage.

*Proof.* In \(U_{r,n}\), all \(r\)-sets are bases and all \((r-1)\)-sets are independent, so
\[
|\mathcal B|/|\mathcal I_{r-1}|=\binom nr/\binom n{r-1}=(n-r+1)/r.
\]
Apply (2). \(\square\)

When \(r=2\), \(S=\{b\}\) and the oriented exchange \(S\cup\{a\}\to S\cup\{c\}\) is the ordered triple \((a,b,c)\). Thus (4) is \(L\ge1+\sqrt{(n-1)/2}\), recovering the Devine--Milans terminal-pair theorem for every ordinary reversal-odd boundary 3-tournament. Its stage-dependent version recovers the layered terminal-pair extension in Article VII. For every fixed \(r\), (4) is a square-root lower bound with distinct original resources. The complete exchange clique above a codimension-one independent set is the shared local mechanism.

**Corollary 2 (cubical specialization and its limitation).** Let \(M_n=\bigoplus_{i=1}^nU_{1,2}\), so its basis graph is \(Q_n\). Designate one element in each parallel pair as zero, and let \(\varepsilon(B)\) count the other selected elements modulo two. For an arbitrary undirected-edge coloring \(c\) of \(Q_n\), define the stage-dependent oriented coloring
\[
\boxed{\beta_j(B,B')=c(\{B,B'\})+\varepsilon(B)+(j-1)\pmod2.}\tag{5}
\]
Every positive sliding-window gallery for (5) induces a monochromatic cube geodesic, using \(m-n\) different directions if the gallery has order \(m\).

*Proof.* Each basis window of length \(n\) chooses one element of every parallel pair. When the window shifts, its entering element must be the parallel mate of the departing element. The injective word therefore exchanges every pair at most once, so the basis windows trace a geodesic. Every basis exchange changes \(\varepsilon\) by one, giving \(\beta_j(B',B)=1-\beta_j(B,B')\). Along the gallery, \(\varepsilon(B_j)=\varepsilon(B_1)+(j-1)\), whence
\[
\beta_j(B_j,B_{j+1})=c(\{B_j,B_{j+1}\})+\varepsilon(B_1).
\]
Positivity makes the traversed cube edges monochromatic. \(\square\)

For this cubical matroid, however,
\[
\frac{|\mathcal B(M_n)|}{|\mathcal I_{n-1}(M_n)|}
=\frac{2^n}{n2^{n-1}}=\frac2n.\tag{6}
\]
Therefore (2) offers no guaranteed positive exchange beyond the initial basis window, whereas a full antipodal geodesic requires gallery order \(2n\). In contrast, the ratio for \(U_{2,n}\) is \((n-1)/2\). The terminal-set method gives a common witness predicate and proves the tournament square-root estimate, while (6) pinpoints its inability to force the spanning cubical witness. A unified spanning theorem must supply an additional global exchange or antipodal-splicing principle beyond the terminal-set tournament comparison.

**Corollary 3 (parallel-factor law for terminal capacity).** For a loopless partition matroid \(M=\bigoplus_{j=1}^tU_{r_j,m_j}\) with \(r_j\ge1\), the terminal-set ratio in (2) obeys
\[
\boxed{\frac{|\mathcal B(M)|}{|\mathcal I_{r-1}(M)|}
=\left(\sum_{j=1}^{t}\frac{r_j}{m_j-r_j+1}\right)^{-1}.}\tag{7}
\]
*Proof.* An independent \((r-1)\)-set is obtained by choosing \(r_j-1\) elements in one summand \(j\) and bases in all others. Therefore
\[
|\mathcal I_{r-1}(M)|
=\sum_j \binom{m_j}{r_j-1}\prod_{\ell\ne j}\binom{m_\ell}{r_\ell}.
\]
Divide by \(|\mathcal B(M)|=\prod_\ell\binom{m_\ell}{r_\ell}\), and use \(\binom{m_j}{r_j-1}/\binom{m_j}{r_j}=r_j/(m_j-r_j+1)\). \(\square\)

The reciprocal terminal capacity is additive under direct sums. Thus the uniform rank-two model has one large rank-one contraction fiber, producing a square-root gain, whereas the cubical model has \(n\) small contraction fibers whose reciprocal contributions add to \(n/2\). This formula expresses quantitatively why terminal-fiber growth by itself cannot recover the cube's full antipodal geodesic.
