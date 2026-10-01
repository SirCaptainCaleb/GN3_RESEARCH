# The exact-two-good-core six-set has a three-pattern Hamiltonian four-overlap normal form

## Statement

In the setting of astra003canonicalfarsix, suppose exactly two core vertices d,e in D are good deletions, so the full good-deletion set is G={a,b,d,e}. Then at least one of the following holds: (i) U-{d,e} is Hamiltonian; (ii) U-{a,b}=D is Hamiltonian; or (iii), after possibly interchanging d,e, both U-{a,d} and U-{b,e} are Hamiltonian. Thus the sparse boundary case reduces to a core pair, a far pair, or a crossed pair of Hamiltonian four-overlaps.

## Body

On the four good deletion labels G={a,b,d,e}, form the ordinary graph J in which distinct g,h are adjacent exactly when U-{g,h} is Hamiltonian. The prescribed Hamiltonian K4-overlap theorem in extremal01 says that for every prescribed g in G there exists h in G-{g} with U-{g,h} Hamiltonian. Hence J has minimum degree at least one. If de is an edge, conclusion (i) holds. If ab is an edge, conclusion (ii) holds. Assume neither de nor ab is an edge. Then every edge of J joins one vertex of {a,b} to one vertex of {d,e}; thus J is bipartite across this 2+2 partition. Since J has no isolated vertices, Hall's condition is automatic for a 2-by-2 bipartite graph, so J has a perfect matching. After interchanging d,e if needed, its two matching edges are ad and be. These mean exactly that U-{a,d} and U-{b,e} are Hamiltonian, giving conclusion (iii).
