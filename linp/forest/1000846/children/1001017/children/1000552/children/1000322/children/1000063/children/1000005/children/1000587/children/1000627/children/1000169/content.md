# Two-hole alternate witnesses have exact alternating blocker defects

## Statement

For an alternate (ell-2)-edge wrong-entrance witness Q in a spanning top-rank core, the two opposite endpoint double-blocker systems are edge-disjoint matchings on W=V(Q)\h_1. Each endpoint has at most two single blockers because Q misses exactly two vertices. Writing U_r for unused blocker vertices and p for the number of alternating path components, one has U_r-S_r=2((ell-2)-d(r)) and S_u+S_v+U_u+U_v=2p.

## Body

Let Q=(h_1,...,h_s) with s=\ell-2 be one of the alternate wrong-entrance witnesses from 8e4a8307bc49, ending in e. Let u,v be the two free vertices of h_1 at the opposite end, and put
  W=V(Q)\setminus h_1,
so |W|=2s-2=2\ell-6. Let O=V(H)\setminus V(Q), so |O|=2.

For r in {u,v}, every edge f != h_1 through r must meet W. Indeed, linearity forbids f from using either other vertex of h_1, and if f avoided W then f would meet Q only at r; prepending f to Q would give an (\ell-1)-edge path ending in e through Q's entrance, which is different from the unique entrance of e in H.

Classify edges f != h_1 through r as single blockers if |(f\{r})∩W|=1 and double blockers if that number is 2. Let S_r,B_r be their numbers. Because O has only two vertices and distinct edges through r have disjoint non-r pairs, every single blocker uses a distinct vertex of O, so
  S_r<=2.

The double-blocker pairs form a matching M_r on W. The two matchings M_u,M_v are edge-disjoint: if the same pair {a,b} belonged to both, the corresponding hyperedges {u,a,b} and {v,a,b} would share two vertices.

Let U_r be the number of vertices of W unused by M_r and by the W-contact of any single blocker through r. Then
  2s-2-2B_r=S_r+U_r.
Also
  d_H(r)=1+S_r+B_r.
Eliminating B_r gives the exact defect identity
  U_r-S_r=2(s-d_H(r)).

Let p be the number of path components in the alternating union M_u∪M_v, isolated unmatched vertices counted as path components. Since M_u,M_v are matchings,
  p=|W|-(B_u+B_v).
Substituting the two defect equations yields
  S_u+S_v+U_u+U_v=2p.

Thus every alternate near-spanning witness supplied by the induction carries the same alternating path-cycle structure as a longest nonspecial witness, but with two additional restrictions:
(1) there are only two outside vertices, hence S_u,S_v<=2;
(2) the witness entrance is already a forbidden/wrong entrance for a full-length path, so every clean extension is prohibited.

In particular the obstruction is rotation-rich whenever the endpoint degrees are substantially below s; open alternating-chain endpoints are measured exactly by the signed degree defects.
