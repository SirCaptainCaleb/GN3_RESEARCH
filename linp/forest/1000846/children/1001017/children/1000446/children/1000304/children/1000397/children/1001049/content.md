# High-rank competitors contain the whole ascending edge

## Statement

Let e={x,v,y} be an ascending nonspecial edge of rank q with unique entrance x, so a(x)=q-1 and v,y are terminal. Let f be a snake-incoming edge at v of rank p>=2q-1, and let P be any longest p-edge path ending in f at physical terminal v. Then P contains all three vertices x,y,v of e. More precisely, y occurs among the final q-2 precursor edges before f, and x occurs earlier on P.

## Body

Proof. By the rank-gap terminal-blocker lemma df09b68b76e5, because p>=2q-1 the forced intersection of e with the final q-2 precursor edges of P cannot occur at the low-rank entrance x, so it occurs at y. Let r_j be the first edge of P containing y. Since some occurrence of y lies among the final q-2 precursor edges, the first occurrence index j is at least p-q+1 (if y is shared by two consecutive path edges, the first occurrence can be one edge earlier than the forced tail occurrence). Hence j>=q because p>=2q-1. The prefix r_1,...,r_j can be ordered to end physically at y: if y is private in r_j this is immediate, and if y=r_j cap r_{j+1} then y is a terminal vertex of the prefix ending in r_j. Suppose x did not occur on this prefix. The terminal vertex v occurs only in the final edge f of P, hence is also absent from the prefix. Therefore the prefix meets e only at y, so appending e through y gives a linear path of length j+1>=q+1 ending in e, contradicting phi(e)=q. Thus x occurs earlier on P. Finally v lies in the last edge f and no earlier edge because P ends physically at v. Hence P contains x,y,v as claimed.
