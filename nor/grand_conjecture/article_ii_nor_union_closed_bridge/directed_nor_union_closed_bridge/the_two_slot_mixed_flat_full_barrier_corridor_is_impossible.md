# The two-slot mixed flat-full barrier corridor is impossible

## Composition

(none yet)

## Development


Work in the doubly extremal threshold state of the coboundary-flat ternary sector. Suppose the target switch is flat and the nearest unresolved full-curvature boundary lies exactly two transition slots to the right.

Normalize six consecutive coordinates as 0,1,2,3,4,5, with local status word

A, B, B, A,
where B=1-A.

Thus {0,1,2,3} is the flat target-switch tetrahedron and {2,3,4,5} is the fully-curved boundary tetrahedron. The two middle B-windows are target-compatible; the final A-window is the first mismatch beyond the maximal band.

Flatness of {0,1,2,3} gives

alpha(0,1,3)=A.

Alternation gives

alpha(1,3,2)=1-alpha(1,2,3)=A

and

alpha(3,2,4)=1-alpha(2,3,4)=A.

Full curvature of {2,3,4,5}, whose consecutive statuses are B,A, gives

alpha(2,4,5)=B.

Now perform the endpoint-repair adjacent swap

(0,1,2,3,4,5) -> (0,1,3,2,4,5).

The four affected ternary windows have colors

A, A, A, B.

Hence move the proposed threshold cut from the original first transition to the surviving final transition. Every affected window now matches the shifted one-change target.

Because the swapped coordinates are the interior pair 2,3, an adjacent ternary swap affects exactly these four displayed windows; all windows outside the six-coordinate packet are unchanged. Therefore every previously matched exterior window remains matched, and the formerly mismatching final local window becomes matched.

The target-compatible band strictly increases, contradicting its global maximality.

Thus the distance-two mixed flat/full corridor is impossible.

Combined with the one-slot and three-slot exclusions and the doubly-extremal localization theorem, this yields:

In every doubly-extremal bad threshold state of the coboundary-flat ternary sector, the tetrahedron carrying the target switch is itself fully curved.

So after flat combing and secondary extremality, the terminal obstruction is all-curvature at the switch; no flat target-switch corridor survives.
