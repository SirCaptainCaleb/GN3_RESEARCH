# At the odd central boundary a unique non-double rank-q edge cannot use D or E

## Statement

Let q>=4, let v have p=phi(v)=2q-3, and fix a maximum p-edge path
   P=(g_1,...,g_p)
ending at v. Use
   A=g_{q-3}∩g_{q-2},
   B=private(g_{q-2}),
   C=g_{q-2}∩g_{q-1},
   D=private(g_{q-1}),
   E=g_{q-1}∩g_q.
Assume four assigned potential-charged ascending edges of ranks in {q,q+1} are all single-contact on P, exactly one has rank q, and all contacts lie in A,...,E (as ensured by the F,G exclusions).

Then the rank-q contact cannot be D or E. Hence in every surviving one-low four-single state the rank-q contact is C.

## Body

A rank-q single contact at D or E cannot be terminal-only by a01ddfa76dc8, so in either case it is the visible unique entrance of the rank-q edge.

First suppose the low entrance is E. Then phi(E)=q-1. Since E=g_{q-1}∩g_q is a clean joint entrance, eac2e3da3eea forbids every other single-contact edge whose first-contact cell is q-2. Both
   B=private(g_{q-2})
and
   C=g_{q-2}∩g_{q-1}
have first-contact cell q-2. Thus B,C are unavailable. Besides E only A,D remain among A,...,E, so three further high single contacts cannot be placed. Contradiction.

Now suppose the low entrance is D=private(g_{q-1}); write its edge f_D={D,v,u_D}. Then phi(D)=q-1.

If B is occupied, let h_B be its star edge. Since both incidences are single-contact,
   g_1,...,g_{q-2},h_B,f_D
is linear: the prefix meets h_B only at B, h_B∩f_D={v}, and the omitted edge g_{q-1} removes the D-contact from the inherited path. The sequence has (q-2)+2=q edges and ends in f_D through v. Since f_D has rank q and unique entrance D, this is a longest f_D-path through the wrong entrance v, contradiction.

If B is unoccupied, the three high contacts must occupy A,C,E. In particular C is occupied; let h_C be its star edge. Again
   g_1,...,g_{q-2},h_C,f_D
is linear: h_C meets the prefix only at C on g_{q-2}, and h_C∩f_D={v}. It has q edges and ends in f_D through v, the same contradiction.

Therefore neither D nor E can carry the unique rank-q contact. Since the rank-q witness window at p=2q-3 is {C,D,E}, only C remains.
