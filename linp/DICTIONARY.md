## ambiguous

anchor: 
cells: 
charge: 
chord-geometry: 
clean: 
lens: 
p-center: 
paid: 
slack: 
switching: 
terminal path: 
terminal-singleness: 

## canonical

a(v) [alias -> φ(v)]: Legacy/newer LINP notation for the maximum length of a linear path with last vertex v.
  Note: Normalize durable mathematics back to the paper notation φ(v).
ascending edge: A nonspecial edge e with unique entrance vertex x such that φ(x)=φ(e)-1.
  Note: LINP-defined term. The adjective is permitted because it names a recurring mathematical class; use only with this definition.
color-terminal collision: Let v_0v_1...v_k be a terminal-pair path with parent hyperedges E_i={x_i,v_{i-1},v_i}, where x_i is the unique entrance of E_i. A color-terminal collision is an equality x_i=v_j with j not in {i-1,i}; equivalently, an entrance label of one parent edge is a nonincident vertex of the terminal-pair path.
  Note: Use the full term “color-terminal collision” in durable mathematics. Bare “collision” is permitted only after this meaning has been fixed unambiguously in the local discussion. On the certified nondecreasing-edge-rank rainbow paths of c9a012c1b82e, every color-terminal collision is backward: j<=i-2.
contact: Let e be a hyperedge and let X be a specified path, path segment, edge set, or vertex set. A contact of e with X is a vertex in e∩V(X). If a vertex z∈e is explicitly excluded, an off-z contact of e with X is a vertex in (e\{z})∩V(X). The contact multiplicity is the cardinality of the specified intersection.
  Note: Always say what meets what: e.g. “an e-contact with P”, “the unique off-v contact of e with the precursor P\g_p”, or write the intersection explicitly. Bare “contact” is allowed only when both the edge and the comparison path/region have been fixed unambiguously in the immediately preceding sentence. Do not use “contact” to mean an edge-edge intersection unless the two edges are explicitly named.
core: For a real threshold d, the >d-core of a hypergraph H is the subhypergraph obtained by repeatedly deleting a vertex whose current degree is at most d, together with all incident edges, until the hypergraph is empty or every remaining vertex has degree greater than d. Equivalently, it is the unique maximal induced subhypergraph of H having minimum degree greater than d.
  Note: Use only with an explicit threshold, as in “the >d-core”, unless d has already been fixed unambiguously. Do not use bare “the core” with an unstated threshold. In a minimal-counterexample proof of |E(H)|<=d|V(H)|, the counterexample equals its >d-core.
edge rank: For a hyperedge e, its edge rank is φ(e), the length of a longest linear path whose last edge is e.
  Note: Official LINP terminology. When context is clear, "rank of e" may be used for φ(e).
endpoint potential [alias -> vertex rank]: Legacy LINP prose synonym for the vertex rank φ(v).
  Note: Prefer “vertex rank” or “rank of v”.
entrance: For a nonspecial edge whose unique entrance has been established, the entrance is that unique entrance vertex. When referring instead to the first vertex of a particular path ending in the edge without asserting path-independence, use entrance label.
  Note: Canonical LINP term. Bare entrance is permitted when the edge is fixed and nonspecial; use entrance label for the path-relative notion.
entrance label: Let P be a longest linear path whose last edge is e, and let f be its penultimate edge. By linearity, f∩e is a single vertex; this vertex is the entrance label of P into e.
  Note: Path-relative notion. This matches the certified longest-path/intersection-graph formulation.
exact contact: Let e be a hyperedge, P a specified path, and z in e a distinguished vertex already known to lie on P. A vertex c!=z is an exact off-z contact of e with P when the full intersection is known exactly:
e intersect V(P)={z,c}.
More generally, “exact contact” may be used only when the surrounding statement explicitly determines the complete relevant edge-path intersection, not merely the existence of a contact.
  Note: Prefer an explicit intersection equality whenever space permits. In the U_11 color-terminal-collision setting, saying that c_F is the exact contact of F with R_i means F∩V(R_i)={x_i,c_F}. Do not use “exact contact” when only c_F∈F∩V(R_i) is known.
intersection graph: The graph whose vertices are the edges of G, with two vertices adjacent exactly when the corresponding hyperedges intersect.
  Note: Use for the graph denoted L(G) in the paper/pathmaker discussion.
last edge: For an ordered hypergraph path, the final hyperedge in its edge sequence.
  Note: Paper terminology; prefer over project-local terminal-edge jargon.
last vertex: For an ordered hypergraph path, the final vertex.
  Note: Paper terminology; prefer over physical endpoint language.
linear r-graph: An r-uniform hypergraph in which any two distinct edges intersect in at most one vertex.
  Note: Canonical terminology used throughout linear_paths.tex.
potential [alias -> vertex rank]: Legacy LINP prose synonym for vertex rank φ(v) when applied to a vertex.
  Note: Normalize durable mathematics to “rank” / “vertex rank”. Do not introduce “potential” as a parallel technical quantity.
rank: Typed shorthand for the canonical quantities φ(v) and φ(e): the rank of a vertex v is φ(v), the length of a longest linear path whose last vertex is v; the rank of an edge e is φ(e), the length of a longest linear path whose last edge is e.
  Note: Use bare “rank” only when the object being ranked is unambiguous. Prefer “vertex rank” or “edge rank” when both types are in play.
snake digraph: For an r-graph G, the r-digraph D on V(G) such that (e,v) is an edge of D exactly when φ(e,v)=φ(e).
  Note: Exact named construction from linear_paths.tex.
special edge: An edge e of G that contributes r edges to the snake digraph.
  Note: Exact named notion from linear_paths.tex.
strong-rainbow: A rainbow terminal-pair path E_i={x_i,v_{i-1},v_i} is strong-rainbow when no entrance label x_i is equal to any terminal-path vertex v_j.
  Note: Use only for terminal-pair paths after the ambient rainbow condition (distinct entrance labels) has been stated. Equivalently, the path has no color-terminal collision.
terminal at an edge: A vertex v is terminal at an edge e iff φ(e,v)=φ(e).
  Note: LINP canonical definition. Use the exact rank equality as the definition; do not replace it by an informal path-existence paraphrase.
unique entrance: For a nonspecial edge e with φ(e)≥2, its unique entrance is the vertex x∈e that is the entrance label for every longest linear path whose last edge is e.
  Note: Equivalent certified characterization: e is nonspecial exactly when all longest paths ending in e have the same entrance label. The other two vertices of a 3-edge are terminal at e.
vertex rank: For a vertex v, its vertex rank is φ(v), the length of a longest linear path whose last vertex is v.
  Note: Official LINP terminology. When context is clear, "rank of v" may be used for φ(v).
φ(e): The length of a longest path with last edge e.
  Note: Exact snake-digraph notation from linear_paths.tex; equivalently max_{v in e} φ(e,v).
φ(e,v): The length of a maximum path in G with last edge e and last vertex v.
  Note: Exact snake-digraph notation from linear_paths.tex (LaTeX source uses \\varphi via the macro \\mpl).
φ(v): The length of a longest path with last vertex v.
  Note: Exact snake-digraph notation from linear_paths.tex.

## prohibited

physical [prohibited; use last vertex]: 
  Note: Proof-process disambiguator with no mathematical content. Rewrite using last vertex, last edge, or explicit ordinary language as appropriate.
