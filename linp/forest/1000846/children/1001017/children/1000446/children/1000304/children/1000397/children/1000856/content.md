# Terminal tail-blocker lemma

## Statement

Let e and f be distinct edges of a linear 3-uniform hypergraph sharing a vertex v. Assume e is nonspecial of rank q=phi(e), that v is a terminal vertex of e, and that f is a snake-incoming edge at v with phi(f)>=q-1. Then for every longest path P ending in f at v, the edge e meets at least one of the q-2 edges immediately preceding f in the final (q-1)-edge suffix of P. Equivalently, e cannot be disjoint from the precursor part of any (q-1)-edge suffix ending in f at v.

## Body

Proof. Let P be a longest path ending in f at terminal vertex v, of length p=phi(f)>=q-1. Take the final q-1 edges of P; they form a linear path Q of length q-1 ending in f at v. Suppose e is disjoint from every edge of Q except for the common vertex v in f. Then appending e to Q gives a q-edge linear path ending in e and entering e through v. Since phi(e)=q, this is a longest path ending in e with entrance label v. But v is already a terminal vertex of the nonspecial edge e, so its unique longest-path entrance label is a different vertex of e. Hence e would have at least two longest-path entrance labels and would be special, a contradiction. Therefore e must meet the precursor Q\{f}, which consists exactly of the q-2 edges immediately preceding f in the chosen suffix. The assertion holds for every longest terminal-v path into f.
