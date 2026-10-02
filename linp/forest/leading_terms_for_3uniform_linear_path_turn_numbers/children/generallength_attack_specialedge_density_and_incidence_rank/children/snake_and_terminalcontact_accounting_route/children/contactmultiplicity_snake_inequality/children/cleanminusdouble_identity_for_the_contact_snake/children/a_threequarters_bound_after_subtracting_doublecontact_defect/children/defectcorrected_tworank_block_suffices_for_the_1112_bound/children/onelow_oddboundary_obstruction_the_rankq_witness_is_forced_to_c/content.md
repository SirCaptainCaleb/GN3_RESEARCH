# In a source-clean one-low odd-boundary obstruction the rank-q witness is forced to C

## Statement

Let p=phi(v)=2q-3, q>=4. Choose maximum endpoint paths globally, and suppose four assigned source-clean ascending edges through v, of ranks in {q,q+1}, are all single-contact on P_v. Assume exactly one has rank q.

Using the five surviving slots
  A=g_{q-3}∩g_{q-2},
  B=private(g_{q-2}),
  C=g_{q-2}∩g_{q-1},
  D=private(g_{q-1}),
  E=g_{q-1}∩g_q,
the unique rank-q edge cannot have witness D or E.

Hence its witness is necessarily C. If C is entrance-visible then phi(C)=q-1; otherwise C is the unique possible terminal-only rank-q witness.

## Body

The rank-q witness window at p=2q-3 is exactly {C,D,E}, with terminal-only use possible only at C by a01ddfa76dc8.

Suppose first the low witness is E. Then E is necessarily the visible unique entrance of the rank-q edge. Since E is the clean joint
  g_{q-1}∩g_q,
the mixed clean-joint hole lemma eac2e3da3eea forbids every other single contact whose first-contact cell is q-2, in particular B and C. But four single contacts occupy four of the five slots A,B,C,D,E, so at most one slot is missing. They cannot omit both B and C. Contradiction.

Now suppose the low witness is D=private(g_{q-1}). Then D is the visible entrance, so phi(D)=q-1. Because the low edge is single on P_v, its opposite terminal is absent from P_v. Hence
  R=(g_1,...,g_{q-1})
is a canonical (q-1)-edge entrance rail ending physically at D and avoiding both terminals of the low edge.

If E is occupied by any of the three high edges, then relative to R the vertex E is private in the last rail edge g_{q-1}, and the high edge has exactly this one R-contact (its P_v-contact is unique). This contradicts c448268039f5, which forces every clean single-contact competitor through the common terminal on a canonical rank-q entrance rail into private positions j<=q-3.

Thus E must be the unique missing slot. The occupied set is then {A,B,C,D}. In particular A and C are occupied by high single-contact star edges h_A,h_C. The sequence
  g_1,...,g_{q-3}, h_A,h_C,g_{q-1}
is linear: g_{q-2} is omitted, h_A and h_C use their sole P_v contacts A,C, and meet each other only at v. It has
  (q-3)+2+1=q
edges and ends physically at the private vertex D of g_{q-1}. This gives phi(D)>=q, contradicting phi(D)=q-1.

Therefore neither D nor E can be the low witness. Only C remains.