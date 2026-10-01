# At p=2q-3 a four-single rank-pair obstruction cannot occupy the right-private slot

## Statement

Under the p=2q-3 four-single rank-pair hypotheses with q>=4, the private right slot F=private(g_q) cannot be occupied. Since F is a clean rank-(q+1) entrance it empties B; splitting on the label/occupancy of E, the remaining star contacts always contain one of the bridge pairs {A,C}, {A,D}, or {C,E}, each producing a (q+1)-edge path ending at F and contradicting phi(F)=q. Together with the G-slot elimination, every four-single obstruction is confined to A,B,C,D,E.

## Body

Retain the seven-slot notation A,...,G at p=2q-3, q>=4, and suppose four assigned charged edges of ranks in {q,q+1} are all single-contact on P.

By 8d1adea102fe, G is unoccupied. Suppose F=private(g_q) is occupied. Since F cannot be terminal-only, it is the unique entrance of a rank-(q+1) edge and phi(F)=q.

By 08f894b8cb5e, the clean private entrance F forbids a private single contact two positions earlier, so B=private(g_{q-2}) is unoccupied.

Thus the other three contacts occupy three of A,C,D,E.

Case 1: E is unoccupied.
Then A,C,D are all occupied. Let h_A,h_C be the star edges whose sole P-contacts are A,C. As in the G-slot elimination,
  g_1,...,g_{q-3},h_A,h_C,g_{q-1},g_q
is a linear (q+1)-edge path. Its final predecessor g_{q-1} meets g_q at E, so the private vertex F is a last vertex. Hence phi(F)>=q+1, contradiction.

Case 2: E is occupied as a visible entrance.
Then the clean-joint hole lemma eac2e3da3eea forbids every single contact with first-contact cell q-2, hence C is unoccupied (B already is). Therefore A,D are the other occupied slots.

Let h_A,h_D be their star edges. Then
  g_1,...,g_{q-3},h_A,h_D,g_{q-1},g_q
is linear: h_A bridges from A, h_D bridges to the private D-contact, and g_{q-2} is omitted. It has q+1 edges and ends at F, contradiction.

Case 3: E is occupied terminal-only.
Choose the remaining two occupied slots from A,C,D.

- If A,C are occupied, Case 1's h_A,h_C bridge gives the contradiction.
- If A,D are occupied, Case 2's h_A,h_D bridge gives the contradiction.
- If C,D are occupied, use h_C and h_E instead:
    g_1,...,g_{q-2},h_C,h_E,g_q.
  Here h_C meets the prefix at C, h_C and h_E meet at v, h_E meets g_q at E, and g_{q-1} is omitted, so the sequence is linear. Its length is
    (q-2)+3=q+1.
  Since the predecessor h_E meets g_q at E, F is a last vertex, again contradicting phi(F)=q.

All cases are impossible. Hence F is unoccupied.

Together with 8d1adea102fe, every four-single rank-pair obstruction at p=2q-3 is confined to the five slots A,B,C,D,E.
