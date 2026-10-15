# Three-matroid Hamiltonian galleries and bounded-cost block reversal

# Three-matroid Hamiltonian galleries and bounded-cost block reversal

Let \(n\ge4\) and let \(b(a,v,c)\in\{0,1\}\) be a reversal-odd boundary 3-tournament:
\[
b(c,v,a)=1-b(a,v,c)
\]
for pairwise distinct letters. For an injective word \(P=(v_1,\ldots,v_m)\), write its triple-color sequence \(c_P(i)=b(v_i,v_{i+1},v_{i+2})\), and let \(\mathrm{sw}(P)=\sum_{i=1}^{m-3}\mathbf1_{\{c_P(i)\ne c_P(i+1)\}}\).

**Theorem 1 (Hamiltonian words as three-matroid common independent sets).** Let \(A=\{(u,v):u,v\in[n],u\ne v\}\) be the directed arcs of the complete graph. On this common ground set define the graphic matroid \(M_{\rm gr}\) of \(K_n\), treating both directions of an undirected edge as parallel elements; the indegree partition matroid \(M_{\rm in}\), allowing at most one arc entering each vertex; and the outdegree partition matroid \(M_{\rm out}\), allowing at most one arc leaving each vertex. The common independent sets of cardinality \(n-1\) are precisely the directed Hamiltonian paths:
\[
\boxed{\{B\subseteq A:|B|=n-1,\ B\in\mathcal I(M_{\rm gr})\cap\mathcal I(M_{\rm in})\cap\mathcal I(M_{\rm out})\}.}
\tag{1}
\]

*Proof.* A graphic-independent set of \(n-1\) arcs has an underlying spanning tree in \(K_n\). The two partition matroid bounds give each vertex total degree at most two. Every degree-two spanning tree is an undirected Hamiltonian path. Its internal vertices each have one incoming and one outgoing arc, ensuring a consistently directed Hamiltonian path. Conversely such a path satisfies all three conditions. \(\square\)

**Proposition 2 (a single matroid does not encode the paths).** For every \(n\ge4\), the undirected edge sets of Hamiltonian paths of \(K_n\) do not form the bases of any matroid on \(E(K_n)\).

*Proof.* Let \(P=(0,1,2,3,\ldots,n-1)\) and \(Q=(0,2,1,3,\ldots,n-1)\). The differences between their edge sets are
\[
E(P)\setminus E(Q)=\{\{0,1\},\{2,3\}\},\quad
E(Q)\setminus E(P)=\{\{0,2\},\{1,3\}\}.
\]
Remove \(e=\{0,1\}\) from \(P\). Adding \(\{0,2\}\) gives degree three at vertex 2 and is not a path. Adding \(\{1,3\}\) creates triangle \(1,2,3,1\) and leaves vertex 0 isolated. No element of \(E(Q)\setminus E(P)\) provides the required basis exchange, so the axiom fails. \(\square\)

**Theorem 3 (uniformly bounded cost for nonlocal block reversal).** For any injective word \(P=(v_1,\ldots,v_m)\), \(m\ge4\), and any \(1\le a<b\le m\), let \(P^{[a,b]}\) be obtained by reversing the contiguous block \(v_a,\ldots,v_b\). Then
\[
\boxed{\bigl|\mathrm{sw}(P^{[a,b]})-\mathrm{sw}(P)\bigr|\le6.}
\tag{2}
\]
The bound is independent of \(m\) and the number of reversed vertices. For Hamiltonian words the operation preserves all three matroid independence conditions from Theorem 1, and modifies at most two edges of the underlying undirected Hamiltonian spanning tree.

*Proof.* Every triple window fully inside the reversed block becomes, after reindexing, the reversal of its corresponding former triple. Reversal-oddness complements every such color while reversing their order. Comparing consecutive triple colors strictly within this block therefore yields the same number of changes before and after reversal. Triple windows fully outside the block are unchanged. Only windows crossing its boundaries can change nontrivially: their possible start indices are \(a-2,a-1\) on the left and \(b-1,b\) on the right. Each pair of boundary-crossing windows belongs to at most three switch comparisons; every other comparison is either unchanged or belongs to the reversed-and-complemented interior, where the total is preserved. Thus no more than six switch indicators can change, proving (2).

Reversing a block preserves the vertex set and injectivity of the word, so the resulting Hamiltonian path is again a common independent set of cardinality \(n-1\). At the undirected graph level, every interior edge of the reversed block remains present. Only the two external boundary edges, if present, are replaced:
\[
\{v_{a-1},v_a\}\mapsto\{v_{a-1},v_b\},\qquad
\{v_b,v_{b+1}\}\mapsto\{v_a,v_{b+1}\}.
\]
Thus at most two graphic-basis edges change. \(\square\)

**Proposition 4 (the constant six is sharp).** For \(n=14\), consider
\[
P=(0,1,2,3,4,5,6,7,8,9,10,11,12,13)
\]
and the block reversal of positions 8 through 11 (one-based),
\[
P'=(0,1,2,3,4,5,6,10,9,8,7,11,12,13).
\]
The following triple-color words are simultaneously realizable by a reversal-odd tournament:
\[
c_P=011000000000,\qquad c_{P'}=011001011010.
\tag{3}
\]
Every triple reversal-orbit occurring in both words receives consistent complementary labels upon orientation reversal; assign colors on all other triple orbits freely. The two words have switch counts two and eight. Hence equality is achieved in (2). \(\square\)

**Corollary 5 (connected nonlocal gallery with bounded edge and cost changes).** The graph of directed Hamiltonian paths joined by contiguous-block reversals is connected. Any two such words can be joined by at most \(n-1\) reversals, each changing at most two underlying graphic-basis edges and at most six color switches.

*Proof.* Reversing an adjacent pair swaps two consecutive symbols, and adjacent transpositions generate all permutations. For the quantitative bound, repeatedly locate the desired next symbol of a target word and reverse the block from its current position to the current target position, fixing one additional prefix symbol at each step. At most \(n-1\) reversals suffice. Apply Theorem 3 to each operation. \(\square\)

**Implications and limitations.** This is an admissibility-preserving *nonlocal* exchange on Hamiltonian paths, with a dimension-independent cost Lipschitz constant. It differs from formal binary hexagon reductions or signed-incidence lattice generation because every intermediate object is a connected, resource-simple directed path. The theorem does not guarantee a descending reversal from each nonoptimal Hamiltonian path; it gives no universal upper bound on the minimum switch count. Arbitrary antipodally odd cube-edge colorings do not acquire the same block-reversal property on proper coordinate subcubes: complementarity is imposed only by the full antipodal involution. A future shared theorem needs the analogous globally legal move in each model, not an unqualified transfer of this tournament-specific operation.

A prospective approach is to combine the nonlocal reversal graph with cut-connectivity constraints and a low-cost witness principle. The difficult remaining step is to prove that this connected family must contain a path with a long constant-color run, rather than merely controlling how much one move can change the cost.
