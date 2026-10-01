# A U_11 color-terminal collision has exact blockers except at explicit boundary cases

## Statement

Let v_0v_1...v_k be a rainbow terminal-pair path whose parent hyperedges E_s={x_s,v_{s-1},v_s} are ascending nonspecial edges in U_11, with nondecreasing edge ranks r_s=phi(E_s). Suppose x_i=v_j is a color-terminal collision, and let P_{x_i}=(g_1,...,g_p) be the chosen maximum path ending at x_i used for the source incidence of E_i, where p=phi(x_i)=r_i-1 and h=g_p.

For either parent edge F incident with v_j (F=E_{j+1}, and also F=E_j when j>=1), put s=phi(F). Then

(1) ceil((r_i+1)/2) <= s <= r_i-1.

(2) If F!=h, then there is a unique vertex c_F!=x_i with
    F intersect V(P_{x_i})={x_i,c_F}.

(3) If moreover s<p, and a_F,b_F are the first and last path-edge indices containing c_F, then
    a_F<=s-1,
    b_F>=r_i-s+1,
with the stronger a_F<=s-2 when c_F is the opposite terminal of F rather than its unique entrance.

At most one of the two adjacent parent edges can equal h. Hence every interior color-terminal collision has at least one genuine exact off-x_i contact on P_{x_i}; if neither adjacent parent edge is h, both exact contacts exist and are distinct.

## Body

Because E_i is ascending with unique entrance x_i,
  p=phi(x_i)=r_i-1.
At the collision x_i=v_j, the certified backward-collision lemma c9a012c1b82e gives
  phi(v_j)=r_i-1=p
and, for every parent edge F incident with v_j,
  s=phi(F)<=r_i-1=p.

Since v_j=x_i is a terminal of F, the certified terminal-rank bound a7b7670e955a gives
  phi(x_i)<=2s-2.
Thus
  r_i-1<=2s-2,
so
  s>=ceil((r_i+1)/2).
This proves (1) without any contact-multiplicity convention.

Now assume F!=h. Because F belongs to U_11 and x_i is a terminal of F, its terminal contact multiplicity on P_{x_i} is one. For a non-last incident edge this is the actual cardinality
  |(F minus {x_i}) intersect (V(P_{x_i}) minus h)|=1.
Let c_F be that unique vertex. Since F and h both contain x_i, linearity forbids either other vertex of F from lying in h. Therefore
  F intersect V(P_{x_i})={x_i,c_F},
proving (2).

If in addition s<p, the hypotheses of 49080cbf1371 apply to F at terminal x_i on the maximum p-edge path P_{x_i}. Hence
  a_F<=s-1,
  b_F>=p-s+2=r_i-s+1,
with the stronger a_F<=s-2 when c_F is the opposite terminal of F. This proves (3).

Finally, E_j and E_{j+1} are distinct parent edges, so at most one can equal the single last edge h. When both are different from h, their exact contacts are distinct because the two parent edges already meet at x_i and linearity forbids a second common vertex. The final assertions follow.
