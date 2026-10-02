# Pure-high odd-boundary four-single states force terminal central joints and loss-one witnesses

## Statement

At p=2q-3, if four assigned 0-1-1 rank-(q+1) edges are all single-contact on one maximum v-path, their contacts occupy four of A,B,C,D,E. Whenever E is occupied it is terminal-only; whenever A and C are both occupied, C is terminal-only. Thus every state has a terminal-only central joint. If B or D is the omitted slot, then both C and E are terminal-only, and g_1,...,g_{q-2},h_C,h_E is an exact q-edge wrong-entrance path into a rank-(q+1) edge.

## Body


Let v have
  p=phi(v)=2q-3, q>=4,
and let
  P=(g_1,...,g_p)
be a maximum path ending physically at v.

Suppose four assigned 0-1-1 ascending nonspecial edges through v all have rank q+1 and are single-contact on P. By the F,G exclusions, their four distinct contacts occupy four of the five slots
  A=g_{q-3} cap g_{q-2},
  B=private(g_{q-2}),
  C=g_{q-2} cap g_{q-1},
  D=private(g_{q-1}),
  E=g_{q-1} cap g_q.

Call a contact X-type if it is the unique entrance of its edge and U-type if it is the opposite-terminal contact (so the entrance is absent from P).

Claim 1: if E is occupied, then E is U-type.
Indeed if E were an entrance, the clean-joint hole rule eac2e3da3eea would forbid every other single contact whose first-contact cell is q-2. Both B and C have first-contact cell q-2. Thus B and C would both be unavailable, leaving only A,D,E, fewer than four slots, contradiction.

Claim 2: if A and C are both occupied, then C is U-type.
If C were an entrance, eac2e3da3eea applied to the clean joint C=g_{q-2} cap g_{q-1} would forbid a single contact with first-contact cell q-3. The occupied slot A has first-contact cell q-3, contradiction.

Consequences by the missing slot:
- missing A: B,C,D,E occupied, with E U-type;
- missing B: A,C,D,E occupied, with C and E both U-type;
- missing C: A,B,D,E occupied, with E U-type;
- missing D: A,B,C,E occupied, with C and E both U-type;
- missing E: A,B,C,D occupied, with C U-type.

Thus every pure-high four-single state has at least one terminal-only central-joint contact; the missing-B and missing-D states have the adjacent pair C,E both terminal-only.

Now suppose C and E are both U-type, with corresponding rank-(q+1) edges h_C,h_E. Their entrances are absent from P. The sequence
  g_1,...,g_{q-2}, h_C, h_E
is linear: the prefix meets h_C only at C on its last edge g_{q-2}; h_C and h_E meet at v; h_E has no precursor contact other than E, which lies only in omitted g_{q-1},g_q. It has
  (q-2)+2=q
edges and ends in h_E through terminal v.
Since h_E has rank q+1 and unique entrance off P, this is an exact loss-one wrong-entrance witness for h_E.

Hence the two patterns missing B or D reduce to a canonical loss-one state, with two additional rank-(q+1) 0-1-1 edges still available as blockers/augmenters.
