# Crossing deletion covers close by ordered overlap and a contiguous complementary intersection — preserved pre-item development

## Composition

(none yet)

## Development

## Crossing deletion covers close by an ordered overlap and a contiguous complementary intersection

Let a,b be distinct vertices of a boundary tournament H. Let
F_a=P|Q cover H-a,
F_b=R|S cover H-b.
Name the paths so b belongs to P and a belongs to R.

Put D=V(P) intersection V(R) and C=V(Q) intersection V(S). Suppose D is nonempty and the displayed orders have the form
P=(U,D), R=(D,W),
with exactly the same displayed order on D, and |D|>=2.
Suppose also that C is empty or occurs as one contiguous subpath in at least one of Q,S.

Then H has a spanning two-cover:
(U,D,W) | C.

Proof. Since D is the entire support intersection, U,D,W are disjoint. Every consecutive triple of (U,D,W) is inherited from P or R: the overlap contains at least two vertices, so no triple uses both a vertex strictly before D and a vertex strictly after D. Thus the merged path is tight.

The two missing labels have been restored: b belongs to P and a to R, hence both belong to the merged path. For every other label, being outside P union R is equivalent to belonging to both Q and S. Therefore its complement is exactly C. A contiguous subpath of a tight path is tight. The displayed paths are disjoint and cover H.

If |D|=1, write D=(d). Both U and W are nonempty because they contain b and a, respectively. The displayed merged path is tight exactly when the additional junction triple (last U,d,first W) is tight; this is not an equivalence for the existence of arbitrary two-covers. Its failure gives the explicit boundary flip (first W,d,last U) tight; it does not refute unrestricted two-coverability.

No agreement of the full support partitions is assumed. All four common-domain intersection cells can be large: P intersection R=D, P intersection S=U-{b}, Q intersection R=W-{a}, and Q intersection S=C. Thus the theorem applies to crossing, highly dissimilar covers, retaining the actual local orders that permit a closing splice.

In a no-two-cover state, every pair of deletion covers therefore fails at least one of these geometric conditions: the two hole-containing paths do not meet in a common ordered terminal/initial block of length at least two, or the complementary intersection is fragmented in both remaining paths. This is a restriction on the actual dissimilar-cover interface, not a reduction to a bare bounded Hamiltonian support.

The theorem is a closing criterion rather than a claim that every pair admits this geometry. Its useful next application is to crossing covers selected to maximize an ordered overlap and minimize fragmentation of the complementary intersection. Neither extremal objective alone is asserted to enforce the criterion.
