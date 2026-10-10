# Physical end rotations transfer singleton switches and force opposite-color caps under maximality

# Exact physical endpoint rotations and forced opposite cap colors at singleton phases

**Lemma (head rotation).** Let P be a genuine k-edge direction-distinct cube geodesic, k>=4, rooted at x with direction word p_1,...,p_k and ordered-three-face window color word w_1,...,w_(k-2). Put y=x symmetric_difference {p_1,...,p_k}. The head-rotated path H(P) starts at x symmetric_difference {p_1} and traverses
(p_2,...,p_k,p_1).
It is a genuine geodesic on the same direction support, and its exact physical window-color word is
(w_2,...,w_(k-2), a),
where a is the actual color of the final face window of orientation (p_(k-1),p_k,p_1) through y. Thus the first k-3 window certificates are literally inherited (with their true physical root bits), and only ONE new cap value is introduced.

**Lemma (tail rotation).** The tail-rotated path T(P), rooted at x symmetric_difference {p_k}, traverses
(p_k,p_1,...,p_(k-1))
and has window-color word
(b,w_1,...,w_(k-3)),
where b is the actual color of its initial oriented triple (p_k,p_1,p_2) through x. Again every retained window is the SAME physical ordered face as before.

**Proof.** H(P) first follows exactly the original P's suffix of edges after its first edge, from the original first intermediate vertex to y; all its internal ordered-three-face windows coincide physically with old windows 2,...,k-2. Its one remaining edge flips the original first direction, which is unused by that suffix, so the resulting path is geodesic, and its last triple is the stated physical cap. The tail argument follows the original P prefix after first flipping its final direction into x, so old windows 1,...,k-3 are retained literally. Both moves require neither coordinate-only coloring nor antipodal oddness.

**Corollary (forced boundary-switch transfer at global maximality).** Suppose P has globally maximum length k<n among ALL geodesics with <=1 window-color change, and its word is q^s r^t with q!=r and s,t>=1. If s=1 then H(P) is necessarily good, and its new cap a equals q: otherwise H(P) would be r-monochromatic, so extending it by ANY missing direction would create a longer good geodesic. Thus its exact word is r^t q and its unique switch is now at the LAST adjacency. Dually, if t=1 then T(P) is good, b=r, and its exact word is r q^s, with the unique switch at the FIRST adjacency. In both cases the move preserves length and support, transports the cube root by one actual edge, and preserves all retained physical face certificates.

**Application and limitation.** The near-spanning isolated-transposition construction does not isolate its core against these directed end-relocations: when its first phase is singleton, the head rotation is automatically good under every coloring. This is a genuine root-coupled exchange and an exact secondary cap equation available for extremal path families. It preserves support size; extracting an unused direction still requires global coordination of the transported caps and the two-sided extension walls.
