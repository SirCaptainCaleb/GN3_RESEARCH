# At p=2q-3 a four-single rank-pair obstruction cannot occupy the right-private slot

## Statement

Let p=phi(v)=2q-3 with q>=4, and fix a maximum path
   P=(g_1,...,g_p)
ending physically at v. Use the seven-slot notation
   A=g_{q-3}∩g_{q-2},
   B=private(g_{q-2}),
   C=g_{q-2}∩g_{q-1},
   D=private(g_{q-1}),
   E=g_{q-1}∩g_q,
   F=private(g_q),
   G=g_q∩g_{q+1}.

Suppose four assigned potential-charged ascending edges of ranks in {q,q+1} are all single-contact relative to P.

Then F cannot be occupied.

Combined with 8d1adea102fe, neither F nor G can be occupied; hence every four-single obstruction at p=2q-3 is confined to the five slots A,B,C,D,E.

## Body

Suppose F is occupied. By a01ddfa76dc8, terminal-only rank-(q+1) single contacts cannot occupy F, and rank-q edges have no witness at F. Hence F is the visible unique entrance of a rank-(q+1) edge h_F, so
   phi(F)=q.

Because F is a clean private entrance on g_q, the mixed private-hole lemma 08f894b8cb5e forbids any other private single contact two path positions earlier. Thus B=private(g_{q-2}) is unoccupied.

The other three contacts therefore occupy three of the four slots A,C,D,E. Every three-element subset of {A,C,D,E} contains either {A,D} or {C,E}.

First suppose A,D are occupied, with corresponding single-contact star edges h_A,h_D through v. Then
   g_1,...,g_{q-3},h_A,h_D,g_{q-1},g_q
is linear. Indeed h_A meets the retained prefix only at A, h_D meets the suffix only at D, h_A∩h_D={v}, and the omitted edge g_{q-2} separates the two inherited path pieces. Its length is
   (q-3)+2+2=q+1.
The final edge is g_q and F is private to g_q, so F is a physical last vertex. Hence phi(F)>=q+1, contradicting phi(F)=q.

Now suppose C,E are occupied, with corresponding single-contact star edges h_C,h_E. Then
   g_1,...,g_{q-2},h_C,h_E,g_q
is linear: the omitted edge g_{q-1} separates the prefix from g_q, while h_C and h_E use their sole P-contacts C and E respectively and meet each other at v. Its length is
   (q-2)+2+1=q+1,
and again it ends physically at the private vertex F of g_q. Thus phi(F)>=q+1, the same contradiction.

Therefore F cannot be occupied. The exclusion of G is 8d1adea102fe, so all four contacts lie in A,...,E.
