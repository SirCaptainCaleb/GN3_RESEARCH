# A five-edge path chord excludes the potential-five pattern 4445

## Statement

Let H be a finite linear 3-graph and P=(g1,g2,g3,g4,g5) a five-edge linear path with last vertex v. Put a=g2∩g3 and c=g3∩g4. If H contains an edge f containing a and v, then φ(c)≥4. Consequently, at a vertex v with φ(v)=5, four potential-charged ascending nonspecial edges cannot have ordered ranks (4,4,4,5). The remaining four-edge rank patterns are (4,4,5,5), (4,5,5,5), and (5,5,5,5).

## Body

Write f={a,v,z}. Since P is linear, a and v lie in no common path edge, so f is distinct from every edge of P. Linearity gives f∩g2={a}, f∩g3={a}, and f∩g5={v}.

First suppose f∩g4 is empty. Then (g2,f,g5,g4) is a four-edge linear path: its consecutive intersections are a,v,d, where d=g4∩g5; its nonconsecutive pairs g2,g5 and g2,g4 are disjoint because P is linear, and f,g4 are disjoint by assumption. Its last edge g4 contains c, and c is not in g5. Thus c can be its last vertex, proving φ(c)≥4.

Now suppose f meets g4. Neither a nor v belongs to g4, so f∩g4={z}. In particular z belongs to g4. All three vertices a,v,z of f are absent from g1, since g1 is disjoint from g3,g4,g5. Hence (g1,g2,f,g4) is a four-edge linear path. Its consecutive intersections are g1∩g2,a,z; the nonconsecutive pairs g1,f, g1,g4, and g2,g4 are disjoint. Moreover c is not in f, since f and g3 already meet at a and a≠c. The path therefore has last vertex c, again proving φ(c)≥4.

For the consequence, assume the rank pattern (4,4,4,5). Choose a maximum five-edge path ending in the rank-five edge at v. The saturated witness conclusion of 6244cba591da supplies a rank-four charged edge f whose chosen witness is a=g2∩g3. Whether a is its entrance or its opposite terminal, f contains both a and v. The forced-entrance lemma 9a7eac176b49 gives φ(c)=3 for c=g3∩g4. The preceding elementary path construction gives φ(c)≥4, a contradiction. Thus (4,4,4,5) is impossible. Combining this exclusion with the rank-pattern reduction 6244cba591da leaves precisely the three stated candidate patterns.

The five-edge path lemma itself uses no edge-rank, specialness, maximality, or charging hypothesis. The rank-pattern corollary uses the exact current, pending versions of 6244cba591da and 9a7eac176b49; it is submitted for independent audit rather than claimed certified.
