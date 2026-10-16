# Alon–Pokrovskiy–Sudakov: near-spanning rainbow cycles and expander absorption (2017)

**Summary:** A proper edge coloring of a complete graph has a rainbow cycle missing only O(N^(3/4)) vertices. The proof uses rainbow path-forest exchanges plus a sparse-color random expander.

## Statement

For every sufficiently large N, every properly edge-colored complete graph K_N has a rainbow cycle of length at least N-24N^(3/4) (Theorem 1.2 of Alon, Pokrovskiy, Sudakov, Israel J. Math. 222 (2017)).

## Body

# Alon–Pokrovskiy–Sudakov: rainbow cycles in properly edge-colored complete graphs

**Bibliographic source.** Noga Alon, Alexey Pokrovskiy, Benny Sudakov, “Random subgraphs of properly edge-coloured complete graphs and long rainbow cycles,” *Israel Journal of Mathematics* **222** (2017), 317–331. DOI: 10.1007/s11856-017-1592-x. Preprint arXiv:1608.07028. Public full text: https://web.math.princeton.edu/~nalon/PDFS/rainbowalhc3.pdf .

**Definitions.** An edge coloring of a graph is proper if adjacent edges receive different labels. A rainbow cycle or path has pairwise distinct edge labels.

**Theorem 1.2 (published).** For all sufficiently large integers N, every properly edge-colored complete graph K_N contains a rainbow cycle of at least N-24N^(3/4) edges. Deleting one edge yields a vertex-simple rainbow path with at least N-24N^(3/4)-1 edges. The number N denotes the number of vertices of the complete graph, not its degree or the logarithm of its vertex count.

**Theorem 1.3 (random-label subgraph expansion).** If each color class of a proper edge coloring of K_N is independently retained with probability p<=1/2, then with high probability every vertex has degree (1-o(1))Np, and each pair of disjoint vertex subsets A,B of cardinalities much larger than (log N/p)^2 has at least (1-o(1))p|A||B| retained crossing edges. This yields an expander using relatively few colors.

**Lemma 3.1 (rainbow path-forest exchange).** If a properly edge-colored graph G on N vertices has minimum degree at least (1-delta)N, and parameters gamma,delta satisfy delta>=gamma and 3gamma delta-gamma^2/2>1/N, then G contains a rainbow vertex-disjoint path forest with at most gamma N components and at least (1-4delta)N edges. The proof maximizes forest size under a component cap and performs an alternating sequence of edge exchanges that retains one occurrence of each edge color and preserves the path-forest condition.

**Proof architecture.** Split colors into a dense bulk and a sparse random connecting reserve. The bulk supports a near-spanning rainbow path forest through the exchange lemma; the sparse reserve has robust expansion between large vertex sets, and its fresh-colored edges merge path components into a long rainbow cycle. Crucially both minimum degree close to the complete-graph order and inter-set expansion are available. The theorem is not asserted for all properly edge-colored sparse graphs.

**Hypercube application boundary.** For Q_n on 2^n vertices, the direction labeling i of each cube edge is a proper edge coloring with n colors, each direction class a perfect matching. A rainbow cube path is necessarily a direction-simple cube geodesic. However the published theorem applies to K_N and not the n-regular Q_n; putting N=2^n into the rainbow-cycle bound cannot imply any n-o(n) rainbow geodesic in Q_n. Moreover retaining random direction classes of Q_n yields a disjoint union of axis-aligned smaller cubes, so the sparse-color expander ingredient fails maximally in this setting. An adaptation must replace this expansion and additionally select a common binary edge color, because proper direction labeling does not control an independent red/blue coloring.

**Useful methodological transfer.** The alternating exchange in the proof of Lemma 3.1 is a candidate mechanism for minimizing missing direction labels in a family of monochromatic cube paths. The special cube cycle parity can help: any set of cube edges with distinct direction labels is acyclic, since every cycle uses every cube direction an even number of times. Nonetheless such a set may be a large matching instead of one path, so connecting the pieces while respecting edge colors and labels remains the obstacle. This note distinguishes the published theorem from proposed NORI transfers.

## Metadata

- ID: literature_alon_pokrovskiy_sudakov_long_rainbow_cycles_2017
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
