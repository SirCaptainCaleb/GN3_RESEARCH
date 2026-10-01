# Laminar fractional path covers of mass at most two round immediately

## Statement

Let F be any finite family of subsets of a finite vertex set V, and let (x_S)_{S in F} be a feasible fractional cover: x_S>=0 and sum_{S contains v} x_S>=1 for every v. Suppose the family {S:x_S>0} of positive-weight members is laminar and sum_S x_S<=2. Then at most two inclusion-maximal positive-weight members exist, and their union is V. Consequently, when F is the family of tight-path supports of a boundary tournament, those maximal members give a spanning path cover with at most two components.

## Body

Let L={S in F:x_S>0}, assumed laminar. Every vertex v lies in at least one member of L because its covering sum is at least one. Hence v lies in an inclusion-maximal member of L, so the maximal members cover V.

Distinct inclusion-maximal members of a laminar family are disjoint. Let the distinct maximal members be M_1,...,M_t, and choose one vertex v_i in M_i for each i.

Every member S of L containing v_i is contained in M_i: if S contains v_i, then S intersects M_i, so laminarity gives S subseteq M_i or M_i subseteq S; maximality of M_i excludes the second alternative unless S=M_i. Thus

sum_{S contains v_i} x_S >= 1

by fractional-cover feasibility.

For different i, the families {S in L:v_i in S} are disjoint. Indeed, a member carrying positive weight and containing both v_i and v_j would intersect the two disjoint maximal members M_i,M_j and, by the preceding containment argument, would have to be contained in both, impossible. Therefore

t <= sum_{i=1}^t sum_{S contains v_i} x_S
  <= sum_{S in F} x_S
  <= 2.

Thus t<=2. Since the maximal positive-weight members cover V, one or two members of F already cover V. If F consists of tight-path supports, choose a tight path on each maximal member to obtain a spanning path cover with at most two components.

No optimality or extremality assumption is needed. The argument also permits the empty set to belong to F with positive weight, since it belongs to none of the charged families. Therefore the laminar-rounding part of the brainstorm is completely general; all substantive difficulty lies in producing a laminar feasible fractional cover of mass at most two.