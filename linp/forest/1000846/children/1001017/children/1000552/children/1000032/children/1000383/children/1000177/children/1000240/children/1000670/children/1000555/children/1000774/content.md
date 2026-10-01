# The q,(q+1)^3 equality pattern forces tail-terminal or cross-splice obstructions

## Statement

Let e_1 have rank q and e_2,e_4 rank q+1, all potential-charged ascending nonspecial edges at common terminal v. Relative to any longest e_4-path and canonical entrance rail for e_1, either the entrance x_2 is absent and the opposite terminal u_2 lies in the final q-1 precursor tail, or x_2 is present and the natural low-rail/high-tail splice is necessarily cross-blocked. In particular, in a q,(q+1)^3 obstruction, each of the two nonchosen high competitors satisfies one of these two explicit obstruction modes against any chosen high edge.

## Body

Let e_1={x_1,v,u_1} be a potential-charged ascending nonspecial edge of rank q, and let e_2={x_2,v,u_2}, e_4={x_4,v,u_4} be potential-charged ascending nonspecial edges of rank q+1, all sharing the charged terminal v.

Choose:
- a longest (q+1)-edge path P_4 ending in e_4 with physical last vertex v;
- a canonical (q-1)-edge entrance path Q_1 ending at x_1 such that Q_1,e_1 is a longest q-edge path ending in e_1.

Then exactly the following obstruction alternative is forced.

(A) If x_2 is absent from P_4, apply the terminal tail-blocker lemma c0798e59ef02 to e_2 against the snake-incoming edge e_4 at v. Since phi(e_2)=phi(e_4)=q+1, e_2 must meet one of the final q-1 precursor edges before e_4. The only non-v vertices of e_2 are x_2,u_2, and x_2 is absent; hence u_2 lies in that final precursor tail.

(B) Suppose x_2 lies on P_4. Consider the natural splice from the certified uncrossed-splice lemma 5945d7d896b0:
  Q_1,e_1,e_4
followed by the reverse P_4-tail down to x_2.
If this were a linear path, 5945d7d896b0 would imply
  2 phi(e_2) >= phi(e_1)+phi(e_4)+2,
that is
  2(q+1) >= q+(q+1)+2 = 2q+3,
which is impossible.
Therefore whenever x_2 lies on P_4, the natural splice is cross-blocked by an additional forbidden intersection.

Thus in the rank pattern q,(q+1),(q+1), every intermediate high edge e_2 relative to a chosen high edge e_4 and low entrance rail Q_1 is either terminal-tail blocked (its opposite terminal u_2 lies in the final q-1 precursor tail of P_4) or the natural low/high splice is explicitly cross-blocked.

In a q,(q+1)^3 obstruction, choosing one high edge as e_4 applies this dichotomy independently to each of the other two high competitors.
