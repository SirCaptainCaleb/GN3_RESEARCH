# Every pure-high odd-boundary four-single state is an exact loss-one wrong-entrance state

## Statement

At p=2q-3, any four assigned 0-1-1 rank-(q+1) edges that are all single-contact on a maximum v-path necessarily yield a q-edge path ending in one of those rank-(q+1) edges through terminal v rather than its unique entrance. Thus every pure-high four-single obstruction is canonically a loss-one wrong-entrance state.

## Body


Retain the setting of e581db151e69:
  p=2q-3,
  P=(g_1,...,g_p)
ends physically at v, and four assigned 0-1-1 rank-(q+1) edges are all single-contact on P. Their contacts occupy four of
  A=g_{q-3} cap g_{q-2},
  B=private(g_{q-2}),
  C=g_{q-2} cap g_{q-1},
  D=private(g_{q-1}),
  E=g_{q-1} cap g_q.

We claim that every such state contains an exact q-edge wrong-entrance witness into one of the four high edges.

Case 1: E is occupied.
By e581db151e69, E is terminal-only. Let h_E be its edge. Since four of five slots are occupied, at least one of B,C is occupied; let Y be such an occupied slot and h_Y its edge.

Then
  g_1,...,g_{q-2}, h_Y, h_E
is linear. The prefix meets h_Y only at Y: both B and C lie in g_{q-2}, while each assigned edge is single-contact on P. The two star edges h_Y,h_E meet exactly at v. The sole P-contact E of h_E lies only in omitted g_{q-1},g_q. Thus there are no nonconsecutive intersections.

The path has
  (q-2)+2=q
edges and ends in h_E through terminal v. Since h_E has rank q+1 and unique entrance off P, this is an exact loss-one wrong-entrance witness.

Case 2: E is omitted.
Then the occupied set is A,B,C,D. By e581db151e69, because A and C are both occupied, C is terminal-only. Let h_C be the C-edge and h_D the D-edge.

Again
  g_1,...,g_{q-2}, h_C, h_D
is linear: the prefix meets h_C only at C, h_C and h_D meet at v, and the sole P-contact D of h_D lies on omitted g_{q-1}. This is a q-edge path ending in rank-(q+1) edge h_D through terminal v.

Hence every pure-high four-single odd-boundary state produces a canonical loss-one wrong-entrance path.
