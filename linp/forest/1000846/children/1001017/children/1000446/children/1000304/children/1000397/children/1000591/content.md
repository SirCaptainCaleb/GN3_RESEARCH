# Four ascending edges can share one last vertex

## Statement

There exists a linear 3-graph with four ascending nonspecial edges having the same last vertex. Hence both the conjecture Δ(T^up)<=3 and the compensated inequality a(v)<=3+h(v) are false.

## Body

Construction. Let Q=(E_1,...,E_{21}) be a 3-uniform linear path with E_i={a_{i-1},b_i,a_i}, where the listed vertices are otherwise distinct. Let v=b_{21}. Add three edges F_{11}={b_{11},v,c_{11}}, F_{17}={b_{17},v,c_{17}}, and F_{20}={b_{20},v,c_{20}}, with c_{11},c_{17},c_{20} new. The hypergraph is linear. Its intersection graph is the path E_1...E_{21}, together with F_{11},F_{17},F_{20}; the four vertices E_{21},F_{11},F_{17},F_{20} form a clique, and each F_j has one additional neighbor E_j. By direct inspection of induced paths, the unique longest-path predecessors of E_{21},F_{11},F_{17},F_{20} are respectively E_{20},E_{11},E_{17},E_{20}, and the corresponding values of φ are 21,12,18,21. The associated entrance vertices are a_{20},b_{11},b_{17},b_{20}. Their φ-values are 20,11,17,20, respectively: prefixes E_1,...,E_{20}, E_1,...,E_{11}, E_1,...,E_{17}, E_1,...,E_{20} witness these values, while any competing induced path through the clique must omit the attachment point of the target and is shorter. Therefore all four target edges are nonspecial and ascending. Each has v as a last vertex of a longest path. Moreover these are the only nonspecial edges at v that matter for the compensated conjecture and none satisfies φ(x)>2(φ(e)-1), so h(v)=0 while a(v)=4. Thus both local conjectures fail.
