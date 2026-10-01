# At the odd boundary a one-low four-single obstruction pins the low witness to C

## Statement

Let p=phi(v)=2q-3 with q>=4, and fix a maximum path
   P=(g_1,...,g_p)
ending physically at v. Use
   A=g_{q-3}∩g_{q-2},
   B=private(g_{q-2}),
   C=g_{q-2}∩g_{q-1},
   D=private(g_{q-1}),
   E=g_{q-1}∩g_q.

Assume four assigned charged ascending nonspecial edges are all single-contact on P and have rank pattern
   q,(q+1),(q+1),(q+1).
By 8d1adea102fe and f378e6022301 their witnesses all lie in A,B,C,D,E.

Then the sole rank-q edge has witness C. In particular its witness cannot be D or E.

Thus every remaining one-low all-single obstruction has a central low edge whose sole P-contact is C; C may be either its visible entrance or its opposite terminal.

## Body

A rank-q witness at p=2q-3 lies in C,D,E by 220a14637b5f. By a01ddfa76dc8 a terminal-only rank-q witness can occur only at C. Hence a low witness at D or E is necessarily the unique entrance of the low edge, and its opposite terminal is absent from P.

Suppose first the low entrance is
   D=private(g_{q-1}).
Then
   R=(g_1,...,g_{q-1})
is a canonical (q-1)-edge entrance rail for the low rank-q edge: it ends physically at D and avoids both terminals of the low edge.

If a high edge had sole P-contact
   B=private(g_{q-2}),
then it would meet R in exactly one private contact on rail edge r_{q-2}. This contradicts c448268039f5, which confines such one-rank-higher single private contacts to positions at most q-3. Thus B is unoccupied.

The low edge occupies D and the other three high contacts must therefore occupy A,C,E. Let h_A,h_E be the star edges at A,E. Then
   g_1,...,g_{q-3},h_A,h_E,g_{q-1}
is linear: the omitted g_{q-2} separates the inherited path pieces, h_A and h_E meet at v, and each has exactly its displayed P-contact. The path has
   (q-3)+2+1=q
edges and ends physically at the private vertex D of g_{q-1}. Hence
   phi(D)>=q,
contradicting phi(D)=q-1.

Now suppose the low entrance is
   E=g_{q-1}∩g_q.
Again R=(g_1,...,g_{q-1}) is a canonical (q-1)-edge low entrance rail, now ending physically at E because g_q is omitted.

By c448268039f5, a high edge meeting R in exactly one private contact can only do so on rail edges r_j with j<=q-3. Therefore neither
   B=private(g_{q-2})
nor
   D=private(g_{q-1})
can be occupied by a high single contact.

But the low edge already occupies E, and after the global F,G exclusions only A,B,C,D remain for the three high witnesses. Deleting B,D leaves only A,C, fewer than three distinct slots. Contradiction.

Therefore the sole rank-q witness must be C.
