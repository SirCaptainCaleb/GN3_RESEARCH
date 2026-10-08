# One-exception endpoint enlargements have contractible outward loci — preserved pre-item development

## Development

## A one-exception endpoint enlargement is contractible

This strengthens [[moving_the_fixed_following_vertex_fills_a_protected_terminal_pair_locus]] from a null-homotopy of the old inclusion to contractibility of the entire enlarged outward locus.

Let H be a permutahedral face with one distinguished free block T=B union {z}, where B is nonempty. Other blocks contribute neutral factors. Let D be the subcomplex consisting of all faces of H whose chamber vertices belong to a prescribed allowed set. Thus membership of a face in D is determined by all its vertices, as for H intersect X_{r+1}.

Assume every chamber whose last label in the distinguished block belongs to B is allowed. No assumption is imposed on chambers ending that block in z. Let C be the subcomplex consisting of faces all of whose chambers end that block in B.

**Theorem.** D strongly deformation retracts onto C. Consequently D is nonempty and contractible.

**Proof.** The prescribed-endpoint-subset theorem makes C nonempty and contractible. It is contained in D by hypothesis.

For a nonempty face G of D, inspect the last block of its ordered partition inside T. If this is the singleton {z}, let A be the immediately preceding block inside T and define N(G) by merging A|{z}. Such A exists since B is nonempty. Otherwise put N(G)=G. Leave all neutral factors unchanged.

First, N(G) is a face of D containing G. Only the merge case needs proof. A chamber of N(G) ending in z belongs to G and is allowed. Every other chamber ends in A subset B and is allowed by hypothesis. The definition of D by its chamber vertices therefore puts the whole convex face N(G) in D.

Second, N is order preserving. Suppose G is a subface of G'. If G does not end in the singleton block {z}, then G' cannot end in that singleton either, so N(G)=G is a subface of N(G')=G'. If both end in singleton {z}, their preceding blocks refine one another, and merging with z preserves refinement. In the remaining case, G ends in singleton {z} while the last block U of G' contains z and another label. The immediately preceding block A of G lies inside U. Merging A with z is therefore still a refinement of G', so N(G) is a subface of N(G')=G'.

Now set K(G)=N(G) intersect C. This is nonempty and contractible: in the last block U of N(G), it restricts the final label to the nonempty subset U intersect B, and the remaining factors are permutahedral faces. It is also nested, since N is order preserving. If G lies in C, then N(G)=G and K(G)=G.

Construct a continuous map f from the barycentric subdivision of D into C by induction over face-chain simplices, carried by K(G_max). On the subdivision of C prescribe f to be the canonical identity map. This relative prescription is carried, since K(G)=G for G in C. Nonemptiness starts the induction and contractibility extends every boundary map. Thus f restricts to the identity on C.

Identify the subdivision with D. On every chain simplex with largest face G, both the identity and f lie in the convex face N(G). Their straight-line homotopy therefore stays in D. These homotopies agree on overlaps and fix C pointwise. The resulting homotopy from the identity to f is a strong deformation retraction onto C. Since C is contractible, so is D. QED.

### Positive-word application

Use the separated-window model of [[moving_the_fixed_following_vertex_fills_a_protected_terminal_pair_locus]]. B occupies positions 1 through k, z is next, and fixed suffix labels z_1,z_2,... follow. Merge B|{z} to obtain H. Assume n>=2k+9,
h(z,z_1,z_2)=1,
h(u,z_1,z_2)=0 for u in B,
and every consecutive suffix status starting at (z_1,z_2,z_3) is zero.

The statuses at the selected left span-two start and thereafter have form
t, alpha, delta, 0, 0, ...,
where delta is one exactly when the distinguished block ends in z. Every strictly inward span-two word ends in zero; every strictly inward alternating window has a terminal string of zeros. The reflected window is all zero. Thus H is protected. When the last label belongs to B, delta=0 and both selected-depth occurrences are absent. Hence all such chambers are outward.

The theorem applies to D=H intersect X_{r+1}. It proves this whole enlarged outward locus contractible, independently of the original terminal-pair relation on B and independently of whether the original outward locus is empty, disconnected, or circular. The assumption that the original outward locus is nonempty, needed for speaking of its old inclusion, is not needed for this stronger conclusion.

This is an elevation of the existing enlargement argument, not a proof that its exit-status hypotheses are forced in every separator face.
