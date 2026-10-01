# Minimal equality obstructions are connected and top cycles have a two-contact first ear

## Statement

Let ell>=4, d=floor(2ell/3), and let H be a vertex-minimal counterexample to the exact-density equality assertion E_ell: |E(H)|=d|V(H)|, delta(H)>=d+1, and H contains a nonspecial edge. Then H is connected.

Moreover, in the minimum-potential equality branch, if C is one of the canonical linear ell-cycles supplied by 56fe77d0057c, there exists an edge f not in C meeting both V(C) and V(H)\V(C). Every such crossing edge meets C in exactly two vertices; in particular the first connection from C to the outside reservoir is a two-contact chord with one outside vertex.

## Body

Suppose H is disconnected, with components H_1,...,H_r. Since
sum_i |E(H_i)| = d sum_i |V(H_i)|,
some component H_i has density at least d.

Every component inherits minimum degree at least d+1.

If H_i contains a nonspecial edge, then H_i has fewer vertices than H, is P_ell-free, has density at least d, and minimum degree at least d+1. Thus it is a smaller counterexample to the strengthened equality-layer assertion, contradicting vertex-minimality.

If every edge of H_i is special, the certified all-special snake bound gives
|E(H_i)| <= ((2ell-3)/3)|V(H_i)|.
For ell>=4,
(2ell-3)/3 < floor(2ell/3)=d,
contradicting density at least d.

Hence H is connected.

Now assume the minimum-potential equality branch and let C be a canonical linear ell-cycle from 56fe77d0057c. Exact-density size separation gives |V(H)|>|V(C)|, but connectedness alone already implies that some edge f outside C meets both V(C) and its complement: take the first hyperedge leaving C along an edge-intersection walk from C to any outside vertex.

We claim f cannot meet C in exactly one vertex. Let w be its unique cycle contact. A linear ell-cycle has ell edges. Delete a cycle edge adjacent to the cycle edge containing w so that, in the remaining (ell-1)-edge cycle path, w occurs in the first edge and is a last vertex. If w is a joint, delete the other incident cycle edge; if w is private, delete either neighboring cycle edge. The resulting (ell-1)-edge path meets f only at w, and the other two vertices of f lie outside C. Appending/prepending f gives a linear P_ell, contradiction.

Thus every crossing edge has at least two cycle vertices. Since it also has an outside vertex and is 3-uniform, it has exactly two cycle contacts and one outside vertex.
