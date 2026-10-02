# Global nonspecial-edge path-length inequality

## Statement

Let H be a finite linear 3-graph with minimum degree δ and global maximum linear-path length L. If H contains a nonspecial edge, then 3δ<=2L+2. Equivalently L>=ceil((3δ-2)/2).

## Body

This is a minimum-degree-first reformulation of the dense all-special target. It is calibrated sharply by the known ell=6 equality obstruction d9ee4adc37d3, which has δ=4, global maximum path length L=5, and a nonspecial edge, giving 3δ=12=2L+2. If H is P_ell^(3)-free then L<=ell-1, so the conjecture implies 3δ<=2ell whenever a nonspecial edge exists. Therefore every P_ell-free linear 3-graph with δ>2ell/3 is all-special, exactly the dense minimum-degree all-special conjecture 020f694f8767. The advantage is that the statement no longer depends on choosing a particular nonspecial edge of maximum rank: it asks only that the existence of any nonspecial edge force a sufficiently long path somewhere in H.