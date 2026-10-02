# A connector between consecutive exterior corridor vertices already forces order disagreement or a reversed splice junction

## Statement

Let A be a globally longest tight path of order lambda and C a tight A-order-preserving path of order lambda-1 that agrees with A outside one common-vertex gap. Put O=V(A)-V(C) and E=V(C)-V(A). Let x,y be consecutive vertices of the E-block in the displayed order of C. Suppose the paired-noninsertion connector outcome gives a tight path D=(x,a_i,...,a_j,y), after possibly interchanging x,y, where a_i,...,a_j form a nonempty A-interval containing at least two vertices. Then either C and D have order disagreement on common vertices, or one of the at most two new triples needed to splice D in place of the edge xy of C is non-tight; hence boundary antisymmetry gives an explicit reversed tight triple at that splice junction.

## Body

Because the one-gap normal form puts every vertex of O inside the unique discrepancy gap, every A-vertex outside O lies on C. The vertices x,y are consecutive in the E-block and therefore adjacent in the displayed path C.

First suppose the A-interval a_i,...,a_j used by D contains some vertex z of A cap C. Since x and y lie in the unique discrepancy gap while z is a common A-vertex, z occurs in C either before both x,y or after both x,y. In D, however, x<z<y after orienting D from x to y. Thus D and C order the common pair x,z or z,y differently, giving order disagreement.

It remains that every interior A-vertex of D lies in O. Hence the interior of D is disjoint from C. Replace the adjacent pair x,y in the displayed sequence C by the whole path D. All old consecutive triples remain unchanged, and all internal consecutive triples of D are tight. The only potentially new triples are the left junction (p,x,a_i), when x has predecessor p in C, and the right junction (a_j,y,q), when y has successor q in C.

If every existing junction triple were tight, the splice would be a tight path. Since the connector outcome from a8c9883902b1 uses at least two A-vertices, the splice has order at least |C|+2=lambda+1, contradicting global maximality of A. Therefore at least one existing junction triple is non-tight. Boundary antisymmetry supplies its reversed tight triple, namely (a_i,x,p) or (q,y,a_j). This is the stated bounded reverse-junction witness.