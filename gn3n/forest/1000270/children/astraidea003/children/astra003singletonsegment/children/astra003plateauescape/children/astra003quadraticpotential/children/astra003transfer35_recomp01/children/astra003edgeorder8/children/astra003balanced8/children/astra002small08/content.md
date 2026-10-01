# The balanced two-cover conjecture holds through order eight

## Statement

Every boundary tournament on n<=8 vertices has a spanning two-path cover whose component orders are floor(n/2) and ceil(n/2).

## Body


For (2le nle6), the balanced partition sizes are at most three on each side whenever (nle6), except for the harmless (4|3) case first appearing at (n=7). Every vertex set of order one or two is a tight path support, and every three-vertex boundary tournament has a tight Hamilton path. Hence the balanced two-cover statement is immediate for (nle6).

For (n=8), the statement is exactly astra003balanced8: every eight-vertex boundary tournament has an exact (4|4) cover.

It remains to treat (n=7). Let (H) be any seven-vertex boundary tournament. Adjoin a new vertex (z) and orient all new reversal pairs involving (z) arbitrarily, obtaining an eight-vertex boundary tournament (H'). By astra003balanced8, (H') has a (4|4) cover with supports (A,B). Exactly one of these supports contains (z); say (zin A). Then
[
|A-{z}|=3,qquad |B|=4.
]
The four-set (B) remains Hamiltonian in (H), while the three-set (A-{z}) is automatically Hamiltonian in every boundary tournament. Thus (H) has a balanced (3|4) two-cover.

Therefore every boundary tournament of order at most eight has a balanced two-cover.
