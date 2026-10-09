# Contiguous good-path flags retain only window-graph topology; higher information requires shared-window identifications

# Contiguous extension flags have only window-graph topology

Let window size r>=1 and n>=r+1. A path predicate is hereditary under taking contiguous subpaths and invariant under physical antipodal reversal Theta. For NORI take the predicate "at most one ordered-window color change"; every path of length r and r+1 is then admitted.

Consider either:
(a) actual rooted admitted geodesic paths, or
(b) their complete ordered PHYSICAL window sequences, identifying exactly the root translations preserving all physical windows.
Order the objects by contiguous subpath/subsequence inclusion. Let P_good be the resulting finite poset, and take its order complex. Theta acts on it simplicially and preserves ranks (path lengths).

THEOREM. Removing all objects of length k>=r+2, in decreasing length, gives an equivariant homotopy equivalence to the rank-r/r+1 order complex. In version (b), this is the barycentric subdivision of the full actual physical window-shift graph H. Hence for the <=1-switch predicate its equivariant homotopy type is independent of the coloring. Its cohomological antipodal index is at most one.

PROOF. At the removal of a maximal admitted path P of length k>=r+2, all of its proper subpaths of length >=r remain, by heredity. Its lower link is the order complex of proper contiguous edge intervals of P of length >=r. This link is the union of:
 L_left = all subpaths of the prefix of length k-1,
 L_right = all subpaths of the suffix of length k-1.
Each is a cone, with its full prefix or suffix as maximum. Their intersection is the cone of all subpaths of the common middle interval of length k-2>=r. Thus the lower link is contractible. Attaching the cone at P along this contractible link changes no homotopy type; equivalently one may remove P.

Remove vertices in Theta pairs. They have the same rank, are distinct, and are incomparable, so their stars meet only in the retained complex. Choose the two relative homotopies as Theta-images. This gives equivariant homotopy equivalences throughout. Exact physical-window identification in version (b) preserves the interval-poset description: distinct positions of one geodesic have distinct direction sets, and its contiguous window strings specify the same fixed physical subpath fiber. At the end, length-r objects are windows and length-(r+1) objects subdivide edges joining two consecutive windows. All such objects are admitted for the <=1-switch predicate. QED.

The involution on the flag complex is free even when full good paths exist: an invariant chain would have an invariant vertex at each of its distinct ranks, whereas reversal of a direction-distinct path of length >=2 has no fixed ordered path. This observation is consistent with the low-index conclusion.

RELATION TO THE STATIC-BOX THEOREM. The exact physical-box nerve isolates all paths of length >=2r in root/used-support components. Adding only contiguous extension flags supplies connections, but their long-path cones are homotopically redundant by the theorem above. To retain higher-dimensional path information, a carrier must also identify common physical windows or other certified data ACROSS DIFFERENT path orders. Such identifications have potentially noncontractible fibers and cannot be replaced by the interval poset.

This is a structural restriction on carrier design. It does not assert that a larger order-exchange carrier cannot force NORI closure.
