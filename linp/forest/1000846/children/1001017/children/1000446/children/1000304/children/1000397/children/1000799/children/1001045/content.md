# Separation of successive contacts with a nonspecial edge

## Statement

Let f be a nonspecial edge of a linear 3-graph with φ(f)=q and unique entrance vertex x. Let P=(e_1,...,e_p) be a path not using f. Suppose u,w are distinct vertices of f such that u occurs on P before w, and no vertex of f occurs on the intervening part of P. Let i be the last index of an edge of P containing u before the first later occurrence of w, and let j>i be the first index of an edge containing w. If w=x, then j-i<=q-1. If w is one of the other two vertices of f, then j-i<=q-2.

## Body

Proof. By the choice of i and j, none of e_{i+1},...,e_{j-1} meets f, and e_j meets f only in w. Therefore (e_{i+1},...,e_j,f) is a linear path of length j-i+1 with last edge f and entrance vertex w. If w=x, its length is at most q=φ(f), so j-i<=q-1. If w is one of the other two vertices of f, then a q-edge path with last edge f entering through w would give a longest path with an entrance different from the unique entrance x, contradicting nonspecialness. Hence the displayed path has length at most q-1, and j-i<=q-2.