# Edge-collision forcing and sharp linear gallery separation at paired roots

- Stable ID: note_nori_paired_gallery_separation_r11435
- Author: unspecified; session provenance retained
- Primary home: subsection:dihedral_full_path_symmetry_and_the_root_gluing_obstruction
- Labels: NORI1, ordinary-facets, paired-root, edge-collision, rooted-splicing, Kendall-distance, sharp, unrestricted, critical-repair, geodesic-order
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11435_4
- Updated session: session_nori_r11435_4
- Disposition: none
- Successor: none

## Related references

- note:note_nori_linear_reverse_order_gluing_obstruction_r11435

## Research note

# Sharp edge-collision forcing and linear gallery separation for paired ordinary-cube geodesics

Let f be ANY binary undirected-edge coloring of Q_m, m>=2, without antipodal constraints. At a fixed root x let P_pi have direction order pi and color word 0^k1^(m-k) (rising), and P_sigma have direction order sigma and word 1^ell0^(m-ell) (falling). Write S_pi(r) for its first r directions, pred_pi(i) for directions preceding i, and d_KT for inversion distance.

**FORCING THEOREM.** A monochromatic full geodesic from x exists if either (a) the two witnesses share an undirected edge, or (b) they have a common rank-r vertex for some min(k,ell)<=r<=max(k,ell).

Proof. An edge shared by two rooted full geodesics has the same preceding direction set on both. If it is color zero, concatenate the zero prefix of the rising path through the edge with the zero suffix of the falling path after it; if it is color one, concatenate the one prefix of the falling path with the one suffix of the rising path. The disjoint supports of the prefix and suffix partition all directions. For (b), equal rank-r vertices mean S_pi(r)=S_sigma(r). If k<=r<=ell, splice the falling one-prefix to the rising one-suffix. If ell<=r<=k, splice the rising zero-prefix to the falling zero-suffix. Each concatenation is a monochromatic full geodesic.

**SHARP DIMENSION-UNIFORM ORDER SEPARATION.** If no monochromatic full geodesic begins at x, then 1<=k,ell<=m-1 and all rising/falling witness pairs from x satisfy:

(i) pred_pi(i)!=pred_sigma(i) for every direction i; equivalently the inversion graph of pi and sigma has no isolated vertex.

(ii) S_pi(r)!=S_sigma(r) for each r in I=[min(k,ell),max(k,ell)] and also r=1,m-1.

(iii) d_KT(pi,sigma) >= max(ceil(m/2), |{1,m-1} union I|) >= max(ceil(m/2),|k-ell|+1).

Proof. If pred_i were equal the paths would use the same i-edge, contradicting (a). An inversion between two orders is a pair of directions whose relative positions change; pred_pi(i) and pred_sigma(i) differ iff i is incident to an inversion. Thus their inversion graph covers all m vertices and has at least ceil(m/2) edges. Condition (ii) follows from the vertex forcing statement; equality at first or penultimate prefix ranks would share the first or last edge. A single adjacent order swap modifies a prefix set at only its own rank. To differ at every rank in the displayed set therefore takes at least that many swaps. QED.

**SHARPNESS EVEN WHEN MONOCHROMATIC GEODESICS ARE GLOBALLY ABSENT.** For every m>=2, define an ordinary edge coloring with direction 0 constantly zero, direction 1 constantly one. Therefore no full geodesic from any root is monochromatic. At root 0 choose rising order pi and falling order sigma with d_KT=ceil(m/2):

For even m, partition remaining directions into pairs (a,b). Put f_a=1+x_b+q(x), f_b=x_a (mod2), where q(x)=x_0(1+x_1). Take pi=(0,1, each pair a,b) and sigma=(1,0, each pair b,a), using the same block order. Both traverse initial directions before the other blocks, hence q=0; pi has word 0 1^(m-1), sigma has 1 0^(m-1), and the orders differ by one adjacent inversion in each of the m/2 pairs including (0,1).

For odd m>=5, use pairs as above except for one last triple (a,b,c), with rules f_a=1+x_b+q, f_b=x_a, f_c=x_a; put (a,b,c) in pi and (b,c,a) in sigma. The triple contributes words 111 and 000 and two inversions. Total distance is (m+1)/2. For m=3 put f_2=x_0 x_1, pi=(0,1,2), sigma=(1,2,0), giving words 011,100 and two inversions. For m=2 the two constant rules and opposite orders suffice.

All direction rules ignore their own bit. For m>=4, the q term joins both initial directions to every other pair/triple, so the undirected influence graph is connected; for m=3 the rule x_0 x_1 connects all dimensions. Thus the leading gallery-distance bound cannot be increased, even in connected examples for every m>=3.

**APPLICATION TO CRITICAL PAIRED-ROOT REPAIRS.** Suppose f has no paired root, but changing a one-colored edge e to zero gives f_e with a paired root x. If f_e has no monochromatic full geodesic from x (the nonmonochromatic alternative of Article XV's singleton repair dichotomy), then EVERY opposite orientation witness pair at x is edge-disjoint, with inversion distance at least ceil(m/2). This yields an unconditional all-dimensional geometric separation for this branch of the repair classification.

**LIMITATION.** This does not eliminate the one-sided favorable root in a hypothetical NORI1 good/bad orbit transition. That configuration's lower-facet ordinary coloring has no paired roots. The theorem is an incidence-sensitive forcing tool and a sharp limitation on short gallery transport, not a proof of NORI1.

Independent exhaustive Q3 audit over all 4096 ordinary edge colorings and all eight roots checked 8064 eligible rising/falling witness pairs with no monochromatic root path. Constructive sharpness independently checked for m=2,...,15. Verifier: paired_gallery_separation.py; full manuscript: paired_gallery_separation.md.
