## Canonical

ascending edge: A nonspecial edge e with entrance x such that φ(x)=φ(e)-1.
  Note: LINP-defined term. The adjective is permitted because it names a recurring mathematical class; use only with this definition.

color-terminal collision: Let v_0v_1...v_k be a terminal-pair path with parent hyperedges E_i={x_i,v_{i-1},v_i}, where x_i is the unique entrance of E_i. A color-terminal collision is an equality x_i=v_j with j not in {i-1,i}; equivalently, an entrance label of one parent edge is a nonincident vertex of the terminal-pair path.
  Note: Use the full term “color-terminal collision” in durable mathematics. Bare “collision” is permitted only after this meaning has been fixed unambiguously in the local discussion. On the certified nondecreasing-edge-rank rainbow paths of c9a012c1b82e, every color-terminal collision is backward: j<=i-2.

contact: Let e be a hyperedge and let X be a specified path, path segment, edge set, or vertex set. A contact of e with X is a vertex in e∩V(X). If a vertex z∈e is explicitly excluded, an off-z contact of e with X is a vertex in (e\{z})∩V(X). The contact multiplicity is the cardinality of the specified intersection.
  Note: Always say what meets what: e.g. “an e-contact with P”, “the unique off-v contact of e with the precursor P\g_p”, or write the intersection explicitly. Bare “contact” is allowed only when both the edge and the comparison path/region have been fixed unambiguously in the immediately preceding sentence. Do not use “contact” to mean an edge-edge intersection unless the two edges are explicitly named.

core: For a real threshold d, the >d-core of a hypergraph H is the subhypergraph obtained by repeatedly deleting a vertex whose current degree is at most d, together with all incident edges, until the hypergraph is empty or every remaining vertex has degree greater than d. Equivalently, it is the unique maximal induced subhypergraph of H having minimum degree greater than d.
  Note: Use only with an explicit threshold, as in “the >d-core”, unless d has already been fixed unambiguously. Do not use bare “the core” with an unstated threshold. In a minimal-counterexample proof of |E(H)|<=d|V(H)|, the counterexample equals its >d-core.

entrance: For an edge e, an entrance is a vertex x in e that is the entrance label for every longest linear path whose last edge is e, when such a vertex exists.
  Note: For the nonspecial edges used in LINP, the entrance is path-independent. Use entrance label for the path-relative notion.

entrance label: Let P be a longest linear path whose last edge is e, and let f be its penultimate edge. By linearity, f∩e is a single vertex; this vertex is the entrance label of P into e.
  Note: Path-relative notion. This matches the certified longest-path/intersection-graph formulation.

intersection graph: The graph whose vertices are the edges of G, with two vertices adjacent exactly when the corresponding hyperedges intersect.
  Note: Use for the graph denoted L(G) in the paper/pathmaker discussion.

linear r-graph: An r-uniform hypergraph in which any two distinct edges intersect in at most one vertex.
  Note: Canonical terminology used throughout linear_paths.tex.

potential [alias -> rank]: Legacy LINP prose synonym for the rank φ(v) when applied to a vertex.
  Note: Normalize durable mathematics to rank of v. Do not introduce potential as a parallel technical quantity.

rank: Typed shorthand for the canonical quantities φ(v) and φ(e): the rank of a vertex v is φ(v), the length of a longest linear path whose last vertex is v; the rank of an edge e is φ(e), the length of a longest linear path whose last edge is e.
  Note: Use bare rank only when the object being ranked is unambiguous; otherwise write rank of v or rank of e.

snake digraph: For an r-graph G, the r-digraph D on V(G) such that (e,v) is an edge of D exactly when φ(e,v)=φ(e).
  Note: Exact named construction from linear_paths.tex.

special edge: An edge e of G that contributes r edges to the snake digraph.
  Note: Exact named notion from linear_paths.tex.

terminal at an edge: A vertex v is terminal at an edge e iff φ(e,v)=φ(e).
  Note: LINP canonical definition. Use the exact rank equality as the definition; do not replace it by an informal path-existence paraphrase.

φ(e): The length of a longest path with last edge e.
  Note: Exact snake-digraph notation from linear_paths.tex; equivalently max_{v in e} φ(e,v).

φ(e,v): The length of a maximum path in G with last edge e and last vertex v.
  Note: Exact snake-digraph notation from linear_paths.tex (LaTeX source uses \\varphi via the macro \\mpl).

φ(v): The length of a longest path with last vertex v.
  Note: Exact snake-digraph notation from linear_paths.tex.

## Prohibited

anchor [prohibited]: 
  Note: Do not use anchor as project shorthand. State the common path, vertex, edge, or reference object explicitly.

cells [prohibited]: 
  Note: Do not use cells as unexplained project shorthand. Name the partition classes, index pairs, table entries, or other objects directly.

charge [prohibited]: 
  Note: Do not use charge as bookkeeping jargon unless a future canonical definition is added. State the counted contribution or inequality directly.

chord-geometry [prohibited]: 
  Note: Do not use chord-geometry. State the relevant intersections, edge positions, or path configuration directly.

clean [prohibited]: 
  Note: Do not use clean as a technical modifier. State the condition directly.

lens [prohibited]: 
  Note: Do not use lens as project shorthand. State the relevant pair of paths, intersections, or endpoint configuration directly.

p-center [prohibited]: 
  Note: Do not use p-center. Name the vertex v and write p=φ(v) when that rank is relevant.

paid [prohibited]: 
  Note: Do not use paid/unpaid bookkeeping language. State which certificate, contribution, or inequality is present.

physical [prohibited]: 
  Note: Proof-process disambiguator with no mathematical content. Rewrite using last vertex, last edge, final vertex, final edge, or explicit ordinary language as appropriate.

slack [prohibited]: 
  Note: Do not introduce slack as an undefined LINP quantity. State the difference or inequality explicitly; add a canonical definition first if a recurring quantity genuinely needs a name.

switching [prohibited]: 
  Note: Do not use switching as generic project shorthand. Name the family of replacement edges or the specific transformation being performed.

terminal path [prohibited]: 
  Note: Do not use terminal path as a technical term. Use the already defined path notion and state the relevant terminal vertices or terminal-at-an-edge property explicitly.

terminal-singleness [prohibited]: 
  Note: Do not use terminal-singleness. State the terminal-single condition explicitly, including the path or incidence to which it applies.
