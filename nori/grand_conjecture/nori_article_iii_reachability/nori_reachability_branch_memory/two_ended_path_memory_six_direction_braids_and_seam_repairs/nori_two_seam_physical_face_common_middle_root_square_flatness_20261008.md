# Both ordered-three-face splice windows are literally root-invariant on exactly the square of their two common middle directions

# Exact common-middle root square of a two-window NORI geodesic splice

Let c be ANY physical ordered-three-face coloring, and fix a genuine full direction-distinct geodesic word p=(p1,...,pn) with a cut after \ell directions, where 2<=\ell<=n−2. Write the two last prefix directions u=p_(ell−1),v=p_ell and the first two suffix directions w=p_(ell+1),t=p_(ell+2), all pairwise distinct. For any cube root x, set S={p1,...,p_ell}, y=x XOR S, and define its TWO physical crossing-window faces
  L_x=( F(y;{u,v,w}), (u,v,w) ),
  R_x=( F(y;{v,w,t}), (v,w,t) ).
These are exactly the ordered faces of the two windows straddling the cut in the full geodesic rooted at x.

**THEOREM (literal two-seam cubical flatness, and sharp dimension).** For ANY translation mask A⊆{v,w} and x'=x XOR A, the two ordered physical faces are literally IDENTICAL:
  L_(x')=L_x, R_(x')=R_x.
Consequently their ordered colors are identical for all FOUR physical roots x, x XOR v, x XOR w, x XOR v XOR w. In other words the two-seam color pair is constant on the full physical 2-cube whose free coordinate directions are exactly {v,w}, for ANY NORI coloring and even without antipodal oddness.

Conversely, suppose A⊆[n] is such that translating x by each individual direction a∈A leaves BOTH ordered physical face OBJECTS unchanged (not merely their colors, which may coincidentally be constant). Then A⊆{v,w}. Thus the two-dimensional root square above is the MAXIMAL full physical coordinate face on which BOTH crossing window objects stay literally fixed. This is sharp in every dimension and every direction order.

**Proof.** A physical ordered face F(y;U) is the cube face with free directions U and all other coordinate bits fixed to y outside U. Translating the starting root x by direction a changes the cut vertex y by the same direction a, so F(y;U) is unchanged iff a∈U. For the left and right crossing faces their free direction sets are U_L={u,v,w} and U_R={v,w,t}. Their intersection is EXACTLY {v,w}, since p has pairwise distinct directions. Hence BOTH faces remain unchanged precisely under flips in span{v,w}; in particular all four root-square vertices have the same two physical objects and colors. Any additional direction lies outside at least one free set, so changing its root bit changes that ordered physical face object, establishing sharpness. QED.

**JOINT CONNECTION WITH MULTIROOT TUCKER.** The root-square near-midpoint Tucker theorem nori_multiroot_near_midpoint_tucker_common_cut_root_square_20261008 supplies, for ANY preassigned physical two-coordinate root square, two packets of eight total actual full endpoint-opposed paths with a common near-middle support cut S (n>=11). To take advantage of THIS theorem's exact two-seam flatness, one must show that some packet's selected cross-splice has the two shared middle seam directions (v,w) EQUAL TO the two free directions of the preassigned root square. That self-consistent alignment is NOT supplied by Tucker merely from common S. More generally, the eight packet paths can have different last prefix and first suffix directions, so their two seam objects need not be identical across the square. Establishing this boundary-memory/root-square alignment, and then synchronizing monochromatic branches or reducing the switch count, is a precisely formulated missing combinatorial forcing lemma.

**STATUS.** This is a genuine physical cubical flatness theorem of the two crossing windows, not an unrestricted NORI closure theorem. It sharply identifies the maximal root-square dimension available for *literal* simultaneous seam invariance (two), explaining why a four-root packet is natural in ordered-three-face NORI.
