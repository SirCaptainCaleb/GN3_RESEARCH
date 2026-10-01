# Ascending terminal graph need not be a pseudoforest

## Statement

The terminal-pair graph formed only from ascending edges can have cycle rank greater than one in a connected component; in particular the pseudoforest strengthening is false.

## Body

Structured counterexample from the three-center one-factorization family. Take N=12 base vertices, three centers c_0,c_1,c_2, and three edge-disjoint perfect matchings M_0,M_1,M_2 of K_12. Use triples {c_i,u,v} for uv in M_i. Exact path/entrance computation classifies all 18 triples as ascending. Their terminal-pair graph is M_0 union M_1 union M_2, a 3-regular graph on 12 vertices; in the tested cyclic factorization it is connected, so its cycle rank is 18-12+1=7. Thus even the ascending terminal graph can contain many independent cycles. This does not obstruct an O(n) edge bound: the same example has exactly 3N/2 ascending edges and motivates the weaker terminal-degree-at-most-3 conjecture.
