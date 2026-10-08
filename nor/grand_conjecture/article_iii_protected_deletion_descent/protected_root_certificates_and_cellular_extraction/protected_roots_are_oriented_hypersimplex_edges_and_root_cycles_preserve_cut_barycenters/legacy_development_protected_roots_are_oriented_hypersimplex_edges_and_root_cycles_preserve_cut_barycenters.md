# Protected roots are oriented hypersimplex edges and root cycles preserve cut barycenters — preserved pre-item development

## Development

## Protected roots are oriented hypersimplex edges and root cycles preserve cut barycenters

Fix a normalized first-phase size p. For every p-cut C define its centered cut vector

z_C = 1_C - (p/n) 1

in the type-A space W. The vectors z_C are exactly the vertices of the centered hypersimplex Delta(n,p).

Let a protected root state have

rho=e_a-e_c,

with a in C and c outside C. Its canonical Johnson successor is

C'=(C minus {a}) union {c}.

Then

z_C-z_C' = 1_C-1_C' = e_a-e_c = rho.

Thus a faithful protected root is literally an oriented edge C' -> C of the centered hypersimplex. The side sign records which threshold boundary produced that oriented edge.

### Root circulations are barycenter-preserving cut displacements

Suppose protected roots rho_i form a physical positive cycle with equal coefficients, as happens on a simple directed coordinate cycle. Let C_i be their protected cuts and C_i' their forced Johnson successors. Since

z_{C_i'}=z_{C_i}-rho_i,

summing around the physical cycle gives

sum_i z_{C_i'} = sum_i z_{C_i}

because sum_i rho_i=0.

Hence the physical root circulation is exactly a mass-preserving displacement of hypersimplex vertices.

In the Hamiltonian regular-cut design from root §55, every coordinate belongs to exactly p of the n cuts, so

sum_i z_{C_i}=0.

Therefore also

sum_i z_{C_i'}=0.

Both the attained protected cuts and their forced successor cuts have the hypersimplex center as their equal-weight barycenter.

### Relation to cut defect

The defect vector from root §52 compares the next attained cut with the forced successor:

D_i = 1_{C_{i-1}}-1_{C_i'} = z_{C_{i-1}}-z_{C_i'}.

Thus D_i is literally the chord in the centered hypersimplex from the forced successor C_i' to the next attained protected cut C_{i-1}. Zero defect means the root edge lands exactly on the next attained cut. Positive defect is geometric failure of edge concatenation.

The total defect circulation

sum_i D_i=0

is therefore a closed polygonal correction to the mass-preserving hypersimplex edge displacement.

### Topological relevance

This identifies a natural polytope for fixed-point methods. Hairy-ball topology acts on the permutahedron of coordinate orders; protected extraction acts on the hypersimplex of first-phase cuts. The canonical root map is the bridge between them: a terminal barrier produces a hypersimplex edge.

A Sperner/Brouwer formulation should therefore label cells by protected p-cuts, not by individual coordinates. A successful face-respecting cut labeling would force a convexly compatible packet by the polytopal Sperner theorem, while the root identities above convert compatibility into Johnson-edge/cut-defect information.

This does not yet construct the required face-respecting labeling.
