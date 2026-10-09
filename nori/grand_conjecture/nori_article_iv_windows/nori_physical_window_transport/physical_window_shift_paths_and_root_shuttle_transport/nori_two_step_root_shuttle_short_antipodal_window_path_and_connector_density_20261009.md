# Two-step physical root shuttles give length ≤2n antipodal window transport and amplified connector density

# Two-step movable-root shuttles halve the antipodal window transport length

Let n>=5 and fix a distinguished direction i. Write W_z(a,i,b) for the ACTUAL physical ordered 3-face through vertex z with ordered free directions (a,i,b). Its physical identity depends only on the bits of z outside {a,i,b}. Let H_i denote the genuine four-edge window-shift graph retaining i in the two middle directions, as in Item nori_certified_square_complex_connected_antipodal_one_class_20261008.

**Lemma (exact two-step exterior-bit shuttle).** For distinct a,b,d,i,k, the two edges
 W_z(a,i,b) -- W_z(i,b,k) -- W_(z xor k)(d,i,b)
are genuine physical consecutive-window-shift edges of H_i. The first edge has full direction word (a,i,b,k), the second has (d,i,b,k) read backward. Their intermediate ordered physical face is literally the SAME because k belongs to its free triple, and its outside fixed bits coincide. More generally choose an arbitrary representative of the initial face differing in free coordinates, and the endpoint d-face can have its newly fixed a-bit freely selected. Replacing z xor k by z gives an equally valid two-step move that swaps the outer direction a→d without toggling k. Interchanging a,d reverses the construction.

**THEOREM (short antipodal path, all dimensions).** For each actual ordered window v=W_z(a,i,b), there exists an EVEN H_i path from v to its actual antipodal reversal tau v=W_(bar z)(b,i,a) of length at most
 L_n = 2n-2 if n is EVEN, and L_n=2n if n is ODD.
This path involves genuine physical ordered-face windows at every step; no abstract identification of distinct root charts is used.

**Proof.** Choose one buffer direction d outside {a,b,i}; let K=[n]\{a,b,i,d}, of size m=n-4>=1. Starting with W_z(a,i,b), process every k in K exactly once by the above two-edge shuttle, alternately replacing the left outer direction a by d and d by a, and toggling the exterior bit k. This costs precisely 2m window-shift edges. While d is free, its eventual exterior fixed bit on returning to a can be selected arbitrarily through the hub representative at the intermediate face: the intermediate (i,b,k) face has d as a fixed coordinate when the left outer is a, but after the a→d move, d is free, and can be set before the d→a move. Choose this d-bit to be the COMPLEMENT of its initial value on the last d→a transition. The original a-bit is free at both the initial and final a-middle windows and poses no constraint. The original exterior bits k∈K have each been toggled exactly once; the b and i free bits are irrelevant to the physical ordered face.

If m is even, the outer direction returns to a after 2m edges; the resulting physical face has the same free triple and order (a,i,b), with EVERY exterior bit in K∪{d} complemented. If m is odd, the outer direction is d; use one additional two-edge no-flip shuttle d→a with helper k_0∈K. This leaves the already flipped k_0 exterior bit unchanged and lets us choose the final d-bit as above. The exterior bits are now all complemented. Finally, at this fixed physical hub, swap the two outer free directions by three two-edge SAME-HUB direction replacements
 (a,i,b) -> (h,i,b) -> (h,i,a) -> (b,i,a),
where h is a third direction distinct from a,b,i; each arrow is a two-edge genuine window-shift path with a helper direction distinct from the four involved directions, possible because n>=5. This six-edge operation does not change the exterior bit assignment of the original {a,b,i} face. Hence we reach tau v with length
 2(n-4)+6 = 2n-2 if n even,
 2(n-4)+2+6 = 2n if n odd.
The length is even. QED.

**Quantitative corollary (strengthens Item nori_equivariant_window_shift_short_antipodal_path_many_middle_connectors_20261009).** Under active NORI oddness, write N_i for the number of DISTINCT monochromatic certified window-shift edges having i in their middle pair. Antipodal reversal pairs the two directional edge-orbits, so their good-edge counts agree, N_L=N_R. Let E0=2^(n-2)(n-1)(n-2)(n-3) be the exact number of edges in EACH oriented H_i orbit. For any path P of the above length L<=L_n, every translated-and-coordinate-permuted (fixing i) copy gP joins a face to its antipodal reversed mate in EVEN steps; because its endpoint colors are opposite, gP has at least ONE equal-color adjacent window pair. Orbit averaging yields
 1 <= E_g[# good edges on gP] = L*N_L/E0.
Consequently
  N_L=N_R >= ceil(E0/L_n),
  N_i >= 2*ceil(2^(n-2)(n-1)(n-2)(n-3)/L_n).
In particular n=5 gives N_i>=40, n=6 gives N_i>=192, n=7 gives N_i>=550. These are exponentially many actual monochromatic directed four-edge connectors per direction, with balanced i-middle orientations.

**Global forcing gap.** The two-step shuttles give exact coordinatewise physical root transport using ONE shared intermediate actual ordered face and a linear-length equivariant antipodal connector. This improves the previous 4n-6 path-length bound and its per-coordinate counting certificate. Nonetheless translated short paths may choose different good edges. The result gives a concrete local cross-root transition chart, but does NOT imply that these monochromatic connectors globally synchronize into one reversed-two-tail support collision or a full one-switch geodesic. The missing gluing theorem must relate edges selected from DIFFERENT translated shuttles while retaining full terminal two-direction and monochromatic run memory.
