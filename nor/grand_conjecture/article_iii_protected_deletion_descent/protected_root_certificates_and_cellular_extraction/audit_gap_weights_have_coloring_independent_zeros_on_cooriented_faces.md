# Audit: gap weights have coloring-independent zeros on cooriented faces

## Composition

The gap-weighted fields of §23 have a coloring-independent common zero locus. For n>=5 its minimum braid-face codimension is ceil((n-3)/5), attained with disjoint doubleton ties. Physical window-slide roots on those faces are strictly cooriented. Thus the valid even-n two-frame obstruction may be exhausted by zeros built into the weights; it does not itself supply a positive physical-root dependence. A relative obstruction or a carrier retaining nonvanishing actual root coefficients is needed.

## Development

## Audit: gap weights have coloring-independent zeros on cooriented faces

This audits root §23. Its continuity, oddness, open-chamber independence, and even-n Stiefel--Whitney calculation remain valid. The existence of a wall degeneracy, however, is already forced by the weights independently of the coloring. It does not establish a positive physical window-slide root dependence.

### Universal zero locus

Use §23's notation: m=n-3 transition positions and
\[
I_i=[\max(1,i-1),\min(n-1,i+3)]\cap\mathbb Z,\qquad
\omega_i=\prod_{s\in I_i}\delta_s.
\]
Let
\[
Z_{\rm wt}=\{x\in S(W):\omega_i(x)=0\text{ for every }1\le i\le m\}.
\]
For every coloring, both weighted middle-root fields vanish on this set.

In particular, every two-level point belongs to it for n>=4: only one adjacent gap is positive, whereas every I_i has at least three elements. Such centered, normalized two-level points exist on the free antipodal sphere. Thus the assertion that a wall dependence exists is true for every coloring and every n>=4 without any characteristic-class argument.

### Sharp codimension and disjoint ties

For n>=5, the least codimension of a braid face whose relative interior lies in Z_wt is
\[
k=\lceil(n-3)/5\rceil.
\]
Indeed, its zero gaps must hit all m intervals I_i. Each gap index s lies in at most five intervals, so at least k gaps must vanish.

For attainment, write m=5(k-1)+t with 1<=t<=5. Set gaps at indices 4,9,...,5(k-1)-1 equal to zero (this list is empty if k=1). For the final zero gap use s=m when t=1, and s=m-1 when 2<=t<=5. All remaining gaps are strictly positive. The first k-1 selected indices cover transition positions 1 through 5(k-1). The last selected index covers the remaining t positions. All selected indices are valid indices in 1,...,n-1, and no two are adjacent. Centering and normalizing such a coordinate vector preserves its ties and strict inequalities.

Hence a minimum-codimension universal zero occurs on a face with only doubleton and singleton blocks. In even orders n=6 and n=8, one doubleton wall already suffices.

### Why these zeros cannot certify physical root cancellation

More generally, let an ordered-partition face have all block sizes at most r. Assign each coordinate the midpoint of the ranks occupied by its block, and let L(e_a-e_b) be midpoint(b)-midpoint(a). For an actual length-r window-slide root, a occurs exactly r ranks before b in its carrying refinement. The endpoints cannot belong to the same block, whose rank diameter is at most r-1. Their blocks are distinct and ordered, so L(e_a-e_b)>0. This one functional separates all physical slide roots over every refinement of the face.

Consequently the doubleton faces constructed above are strictly cooriented for ternary physical slide roots. They contain no positive dependence of those roots, although both weighted middle-root fields vanish identically there.

The distinction is essential: §23 labels shared middle pairs and kills terms using gap products; physical slide roots label dropped and entering coordinates. A vanished weighted field need not transfer to a Radon zero of physical roots.

### Correction and remaining obligation

The characteristic-class obstruction remains a correct general obstruction to a global odd two-frame in even n. For these particular fields, its dependence may lie entirely in Z_wt. The forced-degeneracy statement therefore supplies no additional coloring-sensitive extraction information by itself. This does not refute NOR or the characteristic-class calculation.

A useful topological replacement must retain actual root coefficients on cooriented small-block faces, or prove a relative obstruction forcing dependence outside the universal zero locus. Dividing by a vanishing gap weight is not a repair without a proof of continuous, compatible extension. The following face-carrier construction supplies a zero-free model on every small-block face, but does not yet force a zero globally.
