# Refuted: opposite-end 2/3 degree bound for longest paths ending in a nonspecial edge

## Statement

Refuted, even after weakening 'every longest path' to 'there exists a longest path'. The explicit counterexample 1d151c5db254 has global maximum path length L=6 and a maximum-rank nonspecial edge with exactly one longest path ending at it; both free opposite-end vertices have degree 5>4=floor(2(L+1)/3).

## Body

The originally proposed opposite-end bound is false. Counterexample 1d151c5db254 has 13 vertices, 19 edges, global maximum path length L=6, and a globally maximum-rank nonspecial edge e={0,3,8} with unique entrance 3. It has exactly one longest path ending at e, namely (1,6,7)-(4,7,10)-(4,5,11)-(9,11,12)-(2,3,9)-e. The first two edges intersect in 7, so the two free opposite-end vertices are 1 and 6; both have degree 5, exceeding floor(2(L+1)/3)=4. Thus neither the universal nor existential opposite-end formulation is valid. Retain this object only as a fence. The safe-rotation lemma fc1f69f1f481 remains valid, but safe endpoint mobility alone does not force a low-degree state.
