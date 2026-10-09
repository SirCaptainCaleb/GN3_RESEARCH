# NORI partial geodesics are antipodal crosspolytope signed-face flags; extension deletes signed unused coordinates

# The active NORI problem as a signed CROSSPOLYTOPE FLAG-ERASURE problem with a canonical antipodal residual face

Let C_n=conv{±e_1,...,±e_n}⊂R^n be the n-dimensional crosspolytope and ∂C_n≅S^(n−1) its centrally antipodal simplicial boundary. Let P be an actual partial directed cube geodesic with root x, used direction support W, unused support D=[n]\W, and endpoint y=x XOR W. Define signed-unused vector
  eta(P)_i=0 for i in W, eta(P)_i=(1−2x_i) for i in D.
This is the exact root/complement-endpoint signed vector of
nori_root_complement_endpoint_swap_signed_unused_tucker_high_index_exact_extraction_20261008.

**THEOREM 1 (literal crosspolytope face correspondence).** For a partial path with D nonempty, associate the proper NONEMPTY simplicial face
  F(P)=conv{eta_i(P)e_i:i in D}⊆∂C_n.
Every nonempty face of ∂C_n arises as F(P) from SOME partial cube geodesic (indeed from some choice of starting cube root x and some order of the complementary used directions W), so the binary 2n-bit root/complement-endpoint geometry realizes the FULL face lattice of the canonical antipodal crosspolytope sphere.

Proof: A face of C_n is exactly a collection of signed coordinate basis vertices containing at most one from each antipodal pair {e_i,-e_i}; its ternary label determines an unused set D and its root exterior bits x_D. Assign the remaining root bits arbitrarily and traverse the used set W in any direction order. Conversely eta(P) has one signed vertex per unused direction, so it determines precisely such a face. QED.

**THEOREM 2 (legal extension is face deletion; NORI reversal is central antipodality).** If a partial directed geodesic with used W is extended by one fresh unused direction i, then its signed-unused vector eta loses the single nonzero i-coordinate while keeping all other signed unused coordinates fixed. Thus the crosspolytope face of the longer path is a CODIMENSION-ONE FACE of the preceding F(P) whenever |D|>=2. At the final extension (|D|=1), the last signed vertex is erased and the resulting formal support is the EMPTY FACE, corresponding to the physical full antipodal endpoint condition b=a. Under actual physical antipodal complement plus reversal of the path, eta↦-eta and
  F(ΘP)=−F(P),
the genuine CENTRAL antipodal action on ∂C_n. This holds with no condition on the exterior face colors; the active NORI law merely ensures that the monochromatic or at-most-one-switch path predicate is Θ-invariant.

**THEOREM 3 (full direction orders are MAXIMAL DESCENDING SIGNED FLAGS).** Every starting cube root x determines an initial facet of ∂C_n,
  F_x=conv{(1−2x_i)e_i:i=1,...,n}.
Every n-direction full geodesic rooted at x with direction permutation pi=(p1,...,pn) determines the complete maximal descending face flag
  F_x = F_0 ⊃ F_1 ⊃ ... ⊃ F_(n−1) ⊃ F_n=empty,
where F_j is obtained by deleting the signed basis vertices for the first j directions p1,...,pj. Conversely each such signed facet plus complete deletion order uniquely specifies a rooted full cube geodesic and hence ALL its physical ordered-three-face window objects. Thus this is a bijective FACE-POSIT / GEODESIC representation, not an abstract model that forgets the original physical path.

**Topological and physical memory warning.** The intermediate signed face F_j alone does NOT specify the physically colored ordered-three-face window: it forgets the order in which preceding coordinates were traversed and the original signs of USED root coordinates. The FULL signed flag retains that data. Consequently admissibility of successive three-direction deletion windows (and keeping at most one color change) is a constraint on genuinely DECORATED FLAG CHAINS, not merely on a path through the undirected crosspolytope 1-skeleton. Building a high-index certified complex of admissible partial flags whose topological boundary is ∂C_n is the meaningful Tucker/Hex direction.

**Sharp closure target.** The unrestricted NORI grand conjecture is equivalent to the statement that every active coloring of these physically instantiated ordered-three-deletion windows, with antipodal reversal oddness on original physical three-faces, has SOME full signed facet-erasure flag whose entire window-color word changes at most once. A hypothetical counterexample produces a Θ-invariant collection of <=1-switch PARTIAL flags stopping STRICTLY before the empty face, living over the antipodal ∂C_n signed-support sphere. Any topological completion/existence theorem must preserve the full flag's physical face color provenance and the literal final empty-face certificate. The conditional index-n criterion of the root/complement-endpoint theorem provides one precise way to force that final certified flag.

**Novel relevance.** This crosspolytope geometry uses genuine antipodally odd signed UNUSED coordinates, unlike the invariant USED-support labels which blocked earlier naive cubical Tucker attempts. It also encodes the user's 2n-bit root+position idea in a standard, high-index simplicial sphere while cleanly exposing the still-missing physical memory coherence; it is not claimed to solve grand NORI by itself.
