# Periodic exchange strands and resource capacity

Let \(M=\bigoplus_{j=1}^{t}U_{r_j,m_j}\) be a loopless partition matroid decomposed into its connected matroid components, with \(1\le r_j<m_j\) or \(r_j=m_j=1\) (singleton coloops). Let its component ground sets be \(E_j\), and put \(r=\sum_jr_j\), \(N=\sum_jm_j\). A **resource-simple sliding-window gallery** of order \(m\) is an injective word \(w_1,\ldots,w_m\), \(m\ge r\), such that every consecutive length-\(r\) set \(B_i=\{w_i,\ldots,w_{i+r-1}\}\) is a basis. Its exchanged basis arcs are \(B_i\to B_{i+1}\).

**Theorem (periodic component strands).** A word of distinct ground elements with a basis as its initial length-\(r\) window is a resource-simple sliding-window gallery if and only if
\[
\boxed{w_i\text{ and }w_{i+r}\text{ belong to the same connected component of }M}
\quad(1\le i\le m-r).\tag{1}
\]
Thus every gallery decomposes into \(r\) strands indexed by positions modulo \(r\); each strand stays inside one connected component. Conversely every such component schedule can be realized by choosing distinct elements in the prescribed components, subject only to their cardinalities.

*Proof.* The \(i\)-th basis window contains \(r_j\) elements of block \(E_j\) for every \(j\). The next window deletes \(w_i\) and inserts \(w_{i+r}\). Since all block counts must be preserved, both belong to the same block. This proves necessity. Conversely, if the entering and departing elements always belong to the same block, each transition preserves the block counts \(r_j\). By induction every length-\(r\) window is a basis, proving sufficiency. Distinctness gives a resource-simple gallery. \(\square\)

**Theorem (resource-capacity formula).** Fix a nonnegative integer \(q\), the proposed number of successive basis exchanges, and write
\[
q=ar+s,\qquad a\ge0,\quad 0\le s<r.
\]
A resource-simple sliding-window gallery with \(q\) exchanges (word order \(r+q\)) exists if and only if both
\[
\boxed{m_j\ge(a+1)r_j\text{ for every }j,}\tag{2}
\]
and
\[
\boxed{\sum_{j=1}^{t}\min\{r_j,m_j-(a+1)r_j\}\ge s.}\tag{3}
\]
In particular, these conditions compute the maximum uncolored resource-simple gallery length for every partition matroid in all ranks.

*Proof.* Choose the initial length-\(r\) block schedule with \(r_j\) positions labeled \(j\). By (1) the block schedule repeats with period \(r\). In the first \(r+q=(a+1)r+s\) positions, each block \(j\) occurs \((a+1)r_j+t_j\) times, where \(t_j\) is the number of labels \(j\) among the first \(s\) positions of the initial period. We have \(0\le t_j\le r_j\), \(\sum_jt_j=s\). Distinct resources can be chosen if and only if \((a+1)r_j+t_j\le m_j\) for each \(j\). Such integers \(t_j\) exist precisely under (2) and (3). Indeed, (3) says the available nonnegative prefix capacities \(\min\{r_j,m_j-(a+1)r_j\}\) can be allocated to total \(s\); after choosing the \(t_j\), arrange the first \(s\) positions accordingly, fill the remaining \(r-s\) positions to reach initial counts \(r_j\), and populate the strands by distinct resources. \(\square\)

**Corollary (criterion for a full-resource word).** A resource-simple sliding-window gallery using every nonloop element of \(M\) exists if and only if, writing \(h=\lfloor N/r\rfloor\),
\[
\boxed{h r_j\le m_j\le(h+1)r_j\quad\text{for every }j.}\tag{4}
\]
*Proof.* Apply (2)--(3) with \(q=N-r=(h-1)r+(N-hr)\). The excess capacities \(u_j=m_j-h r_j\) sum to \(s=N-hr<r\). Feasibility requires \(u_j\ge0\) and \(\sum\min(r_j,u_j)\ge\sum u_j\), equivalently \(0\le u_j\le r_j\). \(\square\)

**Canonical cases.** For \(M=\bigoplus_{i=1}^nU_{1,2}\), one strand corresponds to each parallel pair and contains at most two elements. Consequently any maximal uncolored gallery has length \(2n\): its first \(n\) entries choose one representative from each pair, and its final \(n\) entries are the corresponding mates in the same order. The basis windows form a coordinate-distinct antipodal cube geodesic. For \(M=U_{2,n}\), all positions share one component; every injective word of length at least two is a gallery, giving ordinary vertex-simple tight paths of a boundary 3-tournament. More generally, for \(M=U_{r,n}\) the same one-component rule gives vertex-simple length-\(r\) window galleries.

**Geometric implication.** The periodic component-strand rule is a common intrinsic gallery geometry underlying both canonical models. Its capacity theorem separates **combinatorial admissibility** (which positions and resources may occur) from the **color feasibility** treated by terminal-set tournament growth. In particular, full-resource uncolored galleries exist for both models; their color existence problems have qualitatively different strength. The all-dimensional mixed example \(Q_k\square K_3\) constructed in the associated obstruction note satisfies (4), while its deck-odd reversal-odd coloring prohibits positive galleries of \(r\) exchanges. This proves that the periodicity and capacity axioms alone cannot supply the desired colored diameter bound.
