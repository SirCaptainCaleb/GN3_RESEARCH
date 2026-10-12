# Two-switch lifting patterns for antipodal diagonal compression

- Stable ID: note_diagonal_compression_two_switch_lifting_patterns_20261012
- Author: unspecified; session provenance retained
- Primary home: subsection:antipodal_diagonal_compression_and_local_face_certificates
- Labels: compression, square_lifting, obstruction, switch_count
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6331_1
- Updated session: session_nori_r6331_1
- Disposition: none
- Successor: none

## Related references

- subsection:antipodal_diagonal_compression_and_local_face_certificates, exact version 1

## Research note

Let a compressed long path cross at x with word alpha h beta and two switches. At its exterior square write A=c(xx^a), B=c(xx^b), C=c(x^a x^{ab}), E=c(x^b x^{ab}). Assume h belongs to {A,B,C,E}. The two lifted words are alpha A C beta and alpha B E beta. Put z equal to the smaller of their switch counts. Then z<=4.

If alpha,beta are nonempty, let L be the last color of alpha, R the first color of beta, and t=[L!=h]+[h!=R]. The condition z>=4 has the following complete characterization:

1. For t=2, it never holds.
2. For t=1, it holds precisely when A=B=R and C=E=L.
3. For t=0, one has L=R=h, and it holds precisely when neither route is monochromatic in h: neither A=C=h nor B=E=h.

If beta is empty and alpha is nonempty, z>=4 holds precisely when L=h, A=B=1-h, C=E=h. If alpha is empty and beta is nonempty, it holds precisely when R=h, A=B=h, C=E=1-h.

Proof. Let k=sigma(alpha)+sigma(beta), so k=2-t when both portions are nonempty. The respective square-interface costs are
[L!=A]+[A!=C]+[C!=R]
and
[L!=B]+[B!=E]+[E!=R].
For t=2, k=0, and each interface costs at most three. For t=1, k=1 and L!=R; both interfaces must cost three, which gives the stated alternating comparisons A=B=R,C=E=L. For t=0, k=2 and L=R=h. Each interface has even cost, either zero or two, and zero occurs precisely for a monochromatic h-route. This proves the interior cases. With one portion empty, each interface has at most two comparisons. A compressed seam of one leaves k=1 and yields z<=3. A seam of zero leaves k=2 and forces both new comparisons to switch on each route; this gives the stated endpoint patterns.

For a selected a-edge h=A, the corresponding route replaces h by hC. This adds two switches precisely when C=1-h and beta is nonempty with first color h. For a selected a-edge h=E, the other route replaces h by Bh. This adds two switches precisely when B=1-h and alpha is nonempty with last color h. In the other cases that selected lift adds at most one. The corresponding b-edge statements follow by exchanging a,b.

Thus even a joining edge at the end of a compressed path can cost two switches: a selected far edge is expanded by inserting the missing edge before it, between two matching colors. For example, the compressed word 000 has zero switches and replacement of its final 0 by 10 gives 0010 with two. At a two-switch witness, replacement of the first 0 in 001100 by 01 gives 0101100 with four.

When z<=3, odd-change rotation in the original antipodally odd cube gives mu(c)<=2. The listed local patterns concern these two lifts and do not assert that the original cube has no other low-switch long geodesic. The full case analysis was independently checked on 6000 two-switch word/square configurations, allowing empty face portions.
