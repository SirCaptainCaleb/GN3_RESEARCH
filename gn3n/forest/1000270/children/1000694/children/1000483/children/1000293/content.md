# An anti-diagonal pivot chain forces linearly many distinct c-free mixed triples

## Statement

Let H-c=A|B with A=(u_0,...,u_m), B=(v_0,...,v_s), and suppose pivot-pivot cross-swap clauses are available at L>=2 consecutive cells (i-t,j+t), t=0,...,L-1, along one valid anti-diagonal. Then H contains at least L-1 distinct tight c-free mixed triples, one forced by each adjacent cell overlap. Each such triple contains two consecutive vertices of one displayed path and one vertex of the other displayed path. Thus a long anti-diagonal family of pivot obstructions forces linear mixed-triple density across the fixed A|B support cut.

## Body

For each adjacent pair of cells (i-t,j+t) and (i-t-1,j+t+1), c55cbbc019d8 forces at least one tight triple from four c-free side alternatives. Call that four-element candidate set S_t. Its members respectively use: the B-edge v_{j+t-1}v_{j+t} with u_{i-t+1}; the A-edge u_{i-t+1}u_{i-t+2} with v_{j+t}; the A-edge u_{i-t-2}u_{i-t-1} with v_{j+t+2}; or the B-edge v_{j+t+2}v_{j+t+3} with u_{i-t-1}. Candidate sets for distinct overlap indices are disjoint. For equal candidate types the displayed consecutive edge determines the overlap index. Comparing the two A-edge types, equality of their A-edges would shift the overlap index by three, but then the accompanying B-vertex indices differ by one; the same argument applies to the two B-edge types. Types with different numbers of A- and B-vertices cannot coincide. Thus the S_t are pairwise disjoint as vertex triples. Selecting one forced tight member from each S_t gives L-1 distinct c-free mixed triples.
