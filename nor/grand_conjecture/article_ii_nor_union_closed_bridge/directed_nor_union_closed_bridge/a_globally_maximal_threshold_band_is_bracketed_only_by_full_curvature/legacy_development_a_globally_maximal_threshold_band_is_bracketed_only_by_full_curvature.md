# A globally maximal threshold band is bracketed only by full curvature — preserved pre-item development

## Development

## A globally maximal threshold band is bracketed only by full curvature

Work in the coboundary-flat pure-orientation sector. For every full coordinate order pi, switch cut k, and polarity eta, define
[
B(pi,k,eta)
]
to be the length of the maximal contiguous interval of window ranks containing the cut on which the actual status word agrees exactly with the one-change threshold target.

Assume NOR fails. Choose a bad switch state maximizing B over all orders, cuts, and polarities.

### Proposition 1: the matched band cannot stop immediately at the cut

Suppose, for example, the first unmatched window on the left is exactly the last pre-switch window k, while window k+1 on the post-switch side is matched. Then the target changes from eta at k to 1-eta at k+1. Since window k is wrong,
[
w_k=1-eta=w_{k+1}.
]
Move the proposed cut one rank to the left. Only the target at rank k changes, from eta to 1-eta, so window k becomes matched and every previously matched window remains matched. This strictly increases B, contradiction.

The right-side analogue is identical.

Hence every unresolved boundary of the maximal matched band lies strictly inside one constant-color side of the target.

### Proposition 2: every unresolved boundary tetrahedron is fully curved

Let j be the nearest mismatch immediately to the left of the maximal matched band. Since j and j+1 lie on the same threshold side, their target color is a common value eta. We have
[
w_j=1-eta,qquad w_{j+1}=eta,
]
so they form an actual transition.

If the supporting tetrahedron were flat, the outward combing repair of subsection 148 would change the local wrong,right pair to right,right while affecting only windows farther to the left. Every already matched window would remain matched and rank j would join the central band. Thus B would strictly increase, contradiction.

Therefore the left boundary transition is fully curved. The same argument applies to the right boundary.

### Maximal-band normal form

Every globally B-maximal bad switch state has a target-compatible central band containing the proposed switch, and each existing unresolved boundary of that band is a fully-curved tetrahedron.

Thus in the coboundary-flat sector all mobile flat repair dynamics can be removed from the terminal analysis. The only obstruction to enlarging a globally maximal compatible band is a curvature barrier.

A closure proof may therefore focus purely on crossing one or two fully-curved barriers. The unique-predecessor and double-full five-set lemmas are exactly the local tools relevant to this normal form.
