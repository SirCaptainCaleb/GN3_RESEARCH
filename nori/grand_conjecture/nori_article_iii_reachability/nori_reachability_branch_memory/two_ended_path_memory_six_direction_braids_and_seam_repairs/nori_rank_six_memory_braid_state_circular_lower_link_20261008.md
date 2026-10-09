# Two middle-swap geodesics merge into a memory state with circular lower link

# First genuine topology from history compression: a rank-six memory-state link is a circle

Retain the exact NORI two-ended boundary-memory state B(P)=(oriented endpoints, first two and last two directions, first/last ordered-three-face colors, clipped change count), and its directed cover graph under one-direction extensions at either endpoint. Let n=6 for concreteness and choose a valid antipodal-reversal-odd coloring in which the two geodesics
P=(1,2,3,4,5,6), P'=(1,2,4,3,5,6)
starting at 000000 both have all four ordered three-window colors zero. Such a coloring exists because their prescribed ordered-face objects have no opposite-reversal conflict. They then represent one monochromatic rank-six boundary-memory state b with precisely these two full path histories (the four visible head/tail directions fix the two missing directions as the unordered set {3,4}). Every lower-rank state is history-unique because the memory quotient is injective through rank five.

Define the lower-link complex L_b as the simplicial complex of increasing chains of boundary-memory states that occur as successive actual contiguous subsegments of a representative path in b (equivalently, chains of exact two-ended Markov extensions terminating at b).

**Theorem (a noncontractible rank-six lower link).** L_b has the homotopy type of S^1, and
H_1(L_b;F2) = F2, while its reduced homology in other degrees vanishes.

Proof. Let L_P and L_P' denote the order complexes of proper oriented contiguous subsegments of the two directed paths. Each is contractible: split proper intervals into subintervals of the initial five-edge path and terminal five-edge path; these subposets and their intersection each have a maximum, so the two-cone union is contractible. Since lower-rank memory states are unique, L_b=L_P union L_P'.

The two full paths differ only in the order of the middle directions 3,4. Their physical vertex sequences agree at positions 0,1,2 and 4,5,6; the vertex at position 3 differs. No nontrivial contiguous directed subsegment can cross from position <=2 to position >=4 and be shared, because it would include the differing middle vertex. Therefore the common lower-interval poset decomposes into the disjoint union of:
(a) all contiguous subsegments of their common prefix at positions 0,1,2, with maximum the two-edge prefix (1,2);
(b) all contiguous subsegments of their common suffix at positions 4,5,6, with maximum the two-edge suffix (5,6).
Each component is contractible, and the intersection is exactly two connected components, hence homotopy equivalent to S^0.

Now L_P and L_P' are contractible CW subcomplexes with intersection homotopy equivalent to S^0. Their union is the homotopy pushout of two maps S^0 to points, which is the suspension Sigma S^0 = S^1. Alternatively the reduced Mayer–Vietoris sequence gives H_1(L_b;F2) =~ H_0(L_P intersect L_P';F2)=F2, with all higher reduced homology zero; van Kampen yields pi_1(L_b)=Z, so the homotopy type is S^1. QED.

**Topological meaning.** Attaching a vertex corresponding to b cones off an S^1 link; its relative cellular effect is a two-dimensional filling, unlike an uncompressed full-path vertex whose lower link is contractible and whose attachment changes no homotopy. Antipodal complemented reversal Theta exchanges b with a distinct corresponding full-rank state and carries its circular lower link equivariantly to the partner's. Thus exact boundary-memory compression introduces a PAIR of true two-dimensional relative attachment obstructions starting at rank six. These circles arise from actual, jointly realizable geodesic histories and remain compatible with all ordered-three-face colors; they are not false coordinatewise intersections.

**Precise limit.** This is an explicit nontrivial LOCAL link in a valid NORI coloring, NOT proof that the global memory-state complex has high antipodal index, NOT proof that the corresponding circle survives in global homology, and NOT a proof of the grand conjecture. The new research route is to study how these rank-six braid-link circles connect and cancel across full-rank and near-full-rank memory states, and whether their equivariant relative obstruction forces an accepting geodesic in every coloring. That is the first tangible higher-dimensional topology produced by the honest reachable-target labels.
