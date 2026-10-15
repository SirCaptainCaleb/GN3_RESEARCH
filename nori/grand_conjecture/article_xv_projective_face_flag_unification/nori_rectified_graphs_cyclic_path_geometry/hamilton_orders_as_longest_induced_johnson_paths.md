# Hamilton orders as longest induced Johnson paths

# Hamilton orders as longest induced Johnson paths

**Theorem 1 (universal line-graph decoding).** Let \(G\) be any finite simple graph. Induced paths \(e_1,\ldots,e_m\) of \(m\) vertices in \(L(G)\) correspond precisely to vertex-simple paths of \(m\) edges in \(G\), with successive original edges \(e_1,\ldots,e_m\).

*Proof.* Successive edges of a vertex-simple path meet, while nonconsecutive ones are disjoint, so their line-graph vertices form an induced path. Conversely, let \(e_1,\ldots,e_m\) be an induced line-graph path. Each \(e_j\) meets its predecessor and successor at *different* endpoints, since otherwise \(e_{j-1},e_{j+1}\) would meet and form a forbidden chord. Hence the sequence of original edges is consistently traversable as a trail. Any repetition of an original vertex would make nonconsecutive trail edges incident, giving a chord in the line graph. Thus the original trail is vertex-simple. \(\square\)

**Corollary 2 (simplex Hamilton paths are maximum induced paths).** The graph of the rectified simplex \(\Delta(2,n)\) is \(J(n,2)=L(K_n)\). Its longest induced paths have \(n-1\) vertices, and all of them are
\[
\boxed{\{v_1,v_2\},\{v_2,v_3\},\ldots,\{v_{n-1},v_n\}}
\]
for Hamilton orders \(v_1,\ldots,v_n\) of the original simplex. An unrestricted reversal-odd boundary 3-tournament is an arbitrary orientation of the edges of \(J(n,2)\). Consequently its original one-switch conjecture is equivalent to the statement that **every orientation of the Johnson graph has a longest induced path whose directed-edge color word changes at most once**.

*Proof.* By Theorem 1, an induced path of \(m\) Johnson-graph vertices decodes to a simple path of \(m\) edges in \(K_n\), using \(m+1\le n\) vertices; hence \(m\le n-1\). Hamilton paths attain equality, and conversely equality forces Hamiltonicity. An oriented Johnson edge from \(\{a,h\}\) to \(\{h,c\}\) corresponds bijectively to the ordered triple \((a,h,c)\), with direction reversal encoding \(b(c,h,a)=1-b(a,h,c)\). \(\square\)

**Comparison with NORI1.** Every full cube geodesic is also a simple original graph path and hence gives an induced path in its rectified line graph. Its special completeness requirement is, more strongly, characterized by being a **shortest essential cycle** in the antipodal quotient, not by maximum induced-path length. These are intrinsic extremal graph descriptions of the two original complete-path families.

**Limitation.** Arbitrary orientations of all line graphs do not satisfy a one-switch theorem for maximum induced paths. For the original graph \(G=C_N\) with even \(N\ge8\), its line graph is \(C_N\). Alternate the clockwise directed-edge bits. Every maximum induced path uses \(N-1\) consecutive vertices and \(N-2\) edges, whose bits alternate in either traversal direction, forcing \(N-3>1\) switches. Thus the successful Johnson case would rely on additional complete exchange geometry, not merely being a line graph.
