# Local span gauge localizes terminal tie-break sign flips — preserved pre-item development

## Composition

(none yet)

## Development

## Local span gauge

The external antipodal gauge is needed only when the selected unsigned witness edge is represented in both orientations, including the centered self-reflecting tie case. It can be replaced by a local odd tie-break.

Fix a total order on the vertices. If both orientations of selected edge (e) occur in chamber (pi), let (u_L,u_R) be the vertices at the leftmost and rightmost positions of the full determining span (I(pi,e)). Orient the tie by
[
g_I(pi,e)=+1 iff u_L<u_R.
]
Reversal exchanges the two endpoint positions of the span, so
[
g_I(pi^{m rev},e)=-g_I(pi,e).
]
Thus the witness labeling remains odd. Chambers having a unique intrinsic witness orientation are unchanged.

If an adjacent transposition is disjoint from (I), it leaves the two span-endpoint vertices unchanged and therefore cannot flip this tie-break. Hence no completely exterior generator can create a gauge-induced terminal sign flip.

Combining this with the intrinsic-orientation persistence argument gives: every terminal sign change is localized to the bounded determining span. Unique-orientation sign flips must alter the represented determining occurrence; tie-case sign flips must alter the local span gauge. Completely exterior Coxeter factors are sign-neutral and can be factored off.

This does not assert the false universal identity (ell(pi)=g(pi)e_r). The gauge is still used only in genuine tie cases; the change is that the tie-break itself is now local to the selected support.
