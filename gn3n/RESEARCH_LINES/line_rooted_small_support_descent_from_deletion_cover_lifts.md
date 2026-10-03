# Rooted small-support descent from deletion-cover lifts

**Summary:** Deletion-cover singleton lifts can be converted into bounded Hamiltonian supports carrying the deleted label; long neighboring paths force further descent or a small classified endpoint-core obstruction.

## Statement

Starting from a deletion cover H-x=P|Q in a minimum counterexample, track pairwise repartitions that keep x inside a bounded Hamiltonian support. The initial singleton lift strictly descends to a rooted three-path; interaction with long neighboring paths then produces rooted four- or five-supports, nonincreasing transport, or sharply positioned endpoint-core obstructions.

## Body

## Rooted descent through bounded supports


Let (H) be a minimum counterexample and let
[
H-x=Pmid Q
]
be a deletion cover. The singleton lift (Pmid Qmid{x}) lies in the three-cover repartition graph. Write
[
Phi(R_1mid R_2mid R_3)=|R_1|^2+|R_2|^2+|R_3|^2.
]

### 1. Descent from the singleton lift

By [[toolkit_lift_strictly_descends_to_a_rooted_three_vertex_component]], one pairwise repartition strictly decreases (Phi) and places the deleted label (x) in a Hamiltonian three-support (T). Thus every deletion-cover component contains a state in which the distinguished label lies in a bounded nontrivial support.

Let (Tmid C) be two displayed components with (|T|=3) and (C=(c_1,ldots,c_m)). If (mge6), [[three_vertex_component_long_neighbor_rotation01]] gives a strict decrease. At (m=5), direct Hamiltonian enlargement to order four is still strict, while failure of both endpoint enlargements forces the neutral rotation
[
3mid5longrightarrow5mid3.
]

### 2. Quadratic-minimal states with a three-support

Suppose a spanning three-cover is (Phi)-minimal in its repartition component and has a component of order three. By [[toolkit_a_phi_minimum_containing_a_three_path_has_order_at_most_thirteen]], its size multiset is one of
[
{3,3,5},qquad {3,4,4},qquad {3,4,5},qquad {3,5,5}.
]

For a (3mid4) pair, [[toolkit_34_pair_gives_a_neutral_endpoint_swap_or_a_controlled_52_detour]] gives either the neutral swap (3mid4	o4mid3) or a controlled (5mid2) detour. For a (3mid5) pair, [[toolkit_minimal_35_pair_forces_a_complementary_matching_block_four_set]] produces a complementary non-Hamiltonian matching-block four-set. Its local order is sharpened by [[toolkit_gives_an_interior_end_edge_reversal_or_a_central_sandwich]] to an interior end-edge reversal or a central sandwich. Two neutral (3mid5) rotations perform the two-for-two support exchange of [[toolkit_35_rotations_perform_a_controlled_two_for_two_support_exchange]].

The four size profiles have the following global consequences.

- In profile (3mid3mid5), [[toolkit_minimal_335_state_forces_a_cross_side_hamiltonian_five_support]] gives a Hamiltonian five-support meeting both three-sides and the interior triple of the five-side.
- In profile (3mid4mid4), [[toolkit_a_neutral_swap_an_order_disagreement_or_a_common_terminal_pair]] gives a neutral swap, an order disagreement, or a common terminal pair for two controlled Hamiltonian five-paths.
- In profile (3mid4mid5), [[toolkit_phi_minimal_345_state_has_a_nontrivial_neutral_reconfiguration]] gives a nontrivial equal-(Phi) reconfiguration.
- In profile (3mid5mid5), [[minimal_355_profile_has_a_neutral_cycle01]] shows that the three-side has distinct neutral rotations with both five-sides. Hence the equal-(Phi) state graph has minimum degree at least two and contains a nontrivial cycle.

Thus every (Phi)-minimal state containing a three-support carries a bounded support, an order disturbance, or explicit neutral recurrence.

### 3. Rooted four-supports

Let (X) be a Hamiltonian four-support containing the distinguished root, and let (C) be a disjoint tight path of order at least six. By [[four_path_long_pair_escape01]], one of the following occurs:

1. (Xmid C) admits a two-path repartition with strictly smaller quadratic contribution;
2. the endpoint six-set (Xcup{c_1,c_m}) is non-Hamiltonian and Hamiltonian five-vertex deletions exhibit an order disagreement;
3. (m=6), the endpoint six-set is Hamiltonian, and there is a neutral rooted migration
[
4mid6longrightarrow6mid4.
]

Consequently, at a quadratic minimum, a rooted four-support beside a path of order at least seven forces an order disagreement.

### 4. Rooted five-supports

Let (X) be a Hamiltonian five-support containing the root and let (C=(c_1,ldots,c_m)), (mge6). If one endpoint extends (X), then
[
5mid mlongrightarrow6mid(m-1),
]
with quadratic change (12-2m). This is neutral for (m=6) and strict for (mge7).

Assume neither endpoint extends (X). By [[five_side_endpoint_core_m6_01]] and [[toolkit_common_endpoint_core_or_a_two_pair_root_exchange_split]], either a common endpoint-replacement core preserves the root or the non-root vertices of (X) split into two endpoint-specific pairs. In the exceptional split, [[toolkit_forces_four_core_disturbance_or_an_outer_hamiltonian_sixset]] yields a four-core order disagreement, a Hamiltonian four-set, a positioned core reversal, or a Hamiltonian six-set.

Hence failure of numerical descent at support order five already produces a bounded order-theoretic obstruction or a rooted six-support.

### 5. Rooted six-supports

Let (X) be a proper Hamiltonian six-support containing the root, and write the non-Hamiltonian complement as
[
H-X=Pmid Q.
]
By [[rooted_six_support_transfer_or_comparison_disturbance01]], there is a non-root label (din X) such that (X-d) remains Hamiltonian and ((Pcup Q)+d) has path-cover number two. Comparing a two-cover of ((Pcup Q)+d) with the displayed partition
[
Pmid Qmid{d}
]
gives one of three outcomes:

1. (d) attaches to exactly one old support, producing a root-preserving one-label pairwise transfer;
2. one old support is split into two comparison blocks, yielding a split displayed edge or separated blocks;
3. a comparison edge joins (P) directly to (Q).

Thus rooted descent from a deletion-cover lift remains controlled through support order six. The possible outcomes are strict quadratic descent, explicit neutral recurrence, order disagreement or reversal, a bounded Hamiltonian core, or a comparison-cover disturbance.


## From bounded supports to defect compression


### Prescribed-vertex reduction of a six-support

Let (U) be a proper Hamiltonian six-support whose complement is non-Hamiltonian of path-cover number two. By A Hamiltonian six-support reduces to a five-support retaining any prescribed vertex, for every prescribed vertex (ain U) there is a Hamiltonian five-subset (Fsubset U), (ain F), such that (H-F) is again non-Hamiltonian with path-cover number two.

Thus a positioned Hamiltonian six-set need not be treated as a terminal object. Any distinguished vertex carried by it can be retained while the set is reduced from order six to order five.

In particular, the neutral (4mid6	o6mid4) migration from A four-path beside a path of order at least six descends, disagrees, or makes the unique neutral migration produces a Hamiltonian six-set containing both displayed endpoints of the old six-path. Prescribing either endpoint yields a Hamiltonian five-support containing that endpoint with two-coverable complement.

The same reduction applies to the Hamiltonian outer six-set from The root-exchange split forces four-core disturbance or an outer Hamiltonian six-set whenever a displayed extender vertex is to be retained.


### Six-support comparisons reduce to path disturbance

The comparison alternatives in A rooted six-support yields a one-label transfer or a path disturbance reduce to a dichotomy. With one interclass edge, the removable label attaches to exactly one old complementary path and produces a root-preserving one-label pairwise transfer. With at least two interclass edges, the block-count identity forces one old support to occur in at least two comparison blocks. Hence either a displayed inherited edge is split between the two comparison paths, or one comparison path leaves that support through a nonempty exterior segment and later returns.

Thus the six-support stage has only two essential outputs:
[
	ext{one-label transfer}qquad	ext{or}qquad	ext{path disturbance}.
]

### The four-support size constraint

The same local machinery gives a global size restriction. By A quadratic minimum containing a four-support is small or has an order disagreement, if a quadratic-minimal state contains a component of order four, then either it already belongs to the classified order-three regime, an order disagreement is present, or every component order lies in ({4,5,6}). In the last case the entire counterexample has order at most eighteen.

Hence, before any defect-line argument is used, the rooted descent has already compressed the low-support regime into:
- the classified order-three profiles;
- an explicit order disagreement;
- or one of six bounded size profiles with orders between four and six.

The bounded four-support analysis below now classifies all six profiles with component orders in \(\{4,5,6\}\). The profiles \(4|4|5\), \(4|5|5\), and \(4|4|4\) have forced neutral recurrence, while each of \(4|4|6\), \(4|5|6\), and \(4|6|6\) either exposes an order disagreement or has forced neutral recurrence. Thus no bounded four-support size profile remains as an unstructured residue.


## Route lemmas consolidated from the Toolkit

### A four-path beside a path of order at least six descends, disagrees, or makes the unique neutral migration

**Statement.** Let H be a boundary tournament, let X be a tight path on four vertices, and let P=(p_1,...,p_m) be a vertex-disjoint tight path of order m>=6. Regard X|P as a two-path cover of its union. Then at least one of the following holds: (1) V(X) union V(P) has a two-path cover with strictly smaller quadratic potential than 4^2+m^2; (2) with U=V(X) union {p_1,p_m}, the six-set H[U] is non-Hamiltonian and Hamilton paths on two distinct deletions U-{x}, x in V(X), have order disagreement; (3) m=6, H[U] is Hamiltonian, and U | (p_2,p_3,p_4,p_5) is a Phi-neutral 6|4 repartition of X|P. Thus outcome (3) is the only non-descending, non-disagreement possibility.

If H[V(X) union {p_1}] or H[V(X) union {p_m}] is Hamiltonian, move that endpoint from P into X and leave the inherited path on the other m-1 vertices of P. This changes the pair sizes from (4,m) to (5,m-1), with new Phi minus old Phi equal to 10-2m<0 for m>=6, giving outcome (1). Assume both endpoint five-sets are non-Hamiltonian. Apply the four-of-six theorem in smallset01 to U=V(X) union {p_1,p_m}. The deletions U-{p_1}=V(X) union {p_m} and U-{p_m}=V(X) union {p_1} are non-Hamiltonian, so all four deletions U-{x}, x in V(X), are Hamiltonian. If H[U] is non-Hamiltonian, astra004fourgooddisagree gives order disagreement between Hamilton paths on two of these deletions, giving (2). If H[U] is Hamiltonian, put M=(p_2,...,p_{m-1}); then U|M is a legal two-path cover of V(X) union V(P). Its potential change is 6^2+(m-2)^2-[4^2+m^2]=24-4m. This is strictly negative for m>=7, giving (1), and is zero exactly when m=6, giving (3).

### A five-side beside a path of order at least six gives nonincreasing transport or a common endpoint core

**Statement.** Let H be a boundary tournament and let X|P|Q be a spanning three-cover, where X is a tight path of order five and P=(p_1,...,p_m) has m>=6. Then either one endpoint transfer from P into X gives a legal spanning three-cover whose quadratic potential changes by 12-2m (neutral for m=6 and strictly decreasing for m>=7), or there exists x in V(X) such that both five-sets (V(X)-{x}) union {p_1} and (V(X)-{x}) union {p_m} are Hamiltonian.

If H[V(X) union {p_1}] is Hamiltonian, replace X|P by a Hamilton path on X union {p_1} together with the inherited path P-p_1. The size pair changes from (5,m) to (6,m-1), with Delta Phi=36+(m-1)^2-(25+m^2)=12-2m, which is zero for m=6 and negative for m>=7. The same applies to p_m. Hence if no such nonincreasing endpoint transfer exists, both six-sets S_1=V(X) union {p_1} and S_m=V(X) union {p_m} are non-Hamiltonian. By the four-of-six theorem, each has at least four Hamiltonian five-vertex deletions. Deleting the endpoint p_i leaves X, which is Hamiltonian, so for each endpoint at least three vertices x in X yield a Hamiltonian replacement (X-{x}) union {p_i}. The two good-label subsets of X each have size at least three, hence intersect because |X|=5. Any common x gives the asserted four-core. No extremality or minimum-counterexample hypothesis is used.

### Prescribed-pair mixed four-supports exist in every exterior three-set

**Statement.** Let A,B be disjoint vertex sets in an arbitrary boundary tournament, with |A|=a>=2 and |B|=b>=3. For every prescribed pair T subset A and every three-set D subset B, there is a pair E subset D such that T union E is Hamiltonian. At least binom(a,2)[binom(floor(b/2),2)+binom(ceil(b/2),2)] distinct Hamiltonian four-supports have exactly two vertices in A and two in B. Every five-set with two vertices in A and three in B has at least two Hamiltonian four-subsets, all meeting both sides. Consequently a bipartition with both sides of order at least two and total order at least five cannot exclude all mixed Hamiltonian four-supports. In a minimum counterexample, each of these four-supports has a non-Hamiltonian complement of path-cover number two.

Fix T={u,v} subset A. Partition B into C_+={z:(u,z,v) is tight} and C_-={z:(v,z,u) is tight}. The certified fixed-pair orientation-class theorem bd3c8d17ca06 makes every pair within either class complete T to a Hamiltonian four-support. Every three-set D subset B has two vertices in one class, giving the prescribed-pair claim without assumptions on paths, insertion, endpoint extensions, or potential. If |C_+|=c and |C_-|=b-c, there are at least binom(c,2)+binom(b-c,2) such supports. Moving one vertex from a class at least two larger than the other decreases this sum, so its minimum occurs at the two balanced class sizes floor(b/2),ceil(b/2). Supports arising from different T have different intersections with A and are distinct, giving the displayed bound. For S=T union D, smallset01 Section 7 gives at least two Hamiltonian four-subsets whether S is Hamiltonian or not. Every four-subset of this 2+3 split meets both A and B. If both sides have at least two vertices and total size at least five, exchange A,B if necessary to choose a 2+3 split; a mixed Hamiltonian four-support follows. The complement assertion is mincex01. Applied to X|P|Q with |X|=4 and |P|>=5, take B to be the displayed interior M of P. For every prescribed X-pair and every three consecutive vertices of M, a Hamiltonian four-support contains that pair and two of those three interior vertices. This is available before the endpoint package or insertion analysis. Therefore the broad no-mixed-support residue used by four_side_endpoint_lock_gap_network01, its cycle-or-monotone successor, and short_gap_forces_reverse_triples01 is empty in their intended four-label setting. The latter theorem gives no live restriction there. This does not produce a same-pair-union repartition: the complementary two-cover supplied by minimality can rearrange the third original path. The remaining useful question must couple these prescribed-pair support families with actual complement path orders and legal attachment data, rather than analyze a nonexistent no-mixed-support branch.

### A blocked center in a four-core extension star forces a complete outer-pair six-set or positioned disturbance

**Statement.** Let H be a boundary tournament, let C be a four-vertex set, let r_0,r_1,...,r_k be distinct vertices outside C with k>=2, and for each i choose a Hamilton path P_i on C union {r_i}. Suppose C union {r_0,r_i} is non-Hamiltonian for every i=1,...,k. Then at least one of the following holds: (1) two chosen paths P_i,P_j have relative-order disagreement on C; (2) H contains a Hamiltonian four-set inside C union {r_0,...,r_k}; (3) for some distinct i,j and c in C, a tight triple on {r_i,c,r_j} reverses a displayed root-core edge of P_i or P_j; (4) for every two distinct leaves r_i,r_j with 1<=i<j<=k, the six-set C union {r_i,r_j} is Hamiltonian.

Assume none of outcomes (1)-(3) occurs. Fix distinct leaves r_i,r_j. Apply three_fourcore_extensions_sync01 to the three Hamiltonian five-extensions C union {r_0}, C union {r_i}, C union {r_j}, with the already chosen Hamilton paths P_0,P_i,P_j. The order-disagreement, Hamiltonian-four-set, and root-core-reversal outcomes of the synchronizer are excluded by assumption. Hence its Hamiltonian six-set outcome occurs for some pair among {r_0,r_i,r_j}. By hypothesis both center-leaf unions C union {r_0,r_i} and C union {r_0,r_j} are non-Hamiltonian. Therefore the only possible pair is {r_i,r_j}, and C union {r_i,r_j} is Hamiltonian. Since i,j were arbitrary distinct leaves, every leaf pair gives a Hamiltonian six-set.

### A two-vertex middle path forces an endpoint-reversal pattern

**Statement.** Let H be a boundary tournament with pc(H)>=3. Let A=(a_1,...,a_r), C=(c_1,...,c_s) be tight paths with r,s>=2, and let u,v be distinct vertices outside A union C such that A|(u,v)|C is a spanning three-cover. Put L={z in {u,v} : (a_{r-1},a_r,z) is tight} and R={z in {u,v} : (z,c_1,c_2) is tight}. Then there are no distinct z,w in {u,v} with z in L and w in R. Hence exactly one of the following holds: (i) L is empty, so both (u,a_r,a_{r-1}) and (v,a_r,a_{r-1}) are tight; (ii) R is empty, so both (c_2,c_1,u) and (c_2,c_1,v) are tight; (iii) L=R={z} for some z in {u,v}, and for the other vertex w both (w,a_r,a_{r-1}) and (c_2,c_1,w) are tight.

Let A=(a_1,...,a_r) and C=(c_1,...,c_s), where r,s>=2, and suppose A|(u,v)|C is a spanning three-cover of a boundary tournament H with pc(H)>=3.

Define L={z in {u,v} : (a_{r-1},a_r,z) is tight} and R={z in {u,v} : (z,c_1,c_2) is tight}.

No two distinct middle vertices can attach to opposite sides. Indeed, if u is in L and v is in R, then (a_1,...,a_r,u) and (v,c_1,...,c_s) are vertex-disjoint tight paths whose supports partition V(H), giving a two-cover, contrary to pc(H)>=3. Hence u in L implies v notin R, and v in L implies u notin R.

If L is empty, boundary antisymmetry gives (u,a_r,a_{r-1}) and (v,a_r,a_{r-1}) tight. If R is empty, boundary antisymmetry gives (c_2,c_1,u) and (c_2,c_1,v) tight.

Assume both L and R are nonempty. Choose z in L and let w be the other vertex. The cross-attachment exclusion forces w notin R, so R={z}. Interchanging left and right gives L={z}. Hence w lies in neither L nor R, and boundary antisymmetry gives both (w,a_r,a_{r-1}) and (c_2,c_1,w) tight.

Thus a two-vertex middle component in a spanning three-cover forces one of three endpoint patterns: two reverse triples through the left exposed edge; two reverse triples through the right exposed edge; or one middle vertex attaches at both exposed ends while its mate reverses both exposed end edges.

### A one-sided tight join across a two-vertex middle forces the adjacent inner reversal

**Statement.** Let H be a boundary tournament with pc(H)>=3. Let A=(a_1,...,a_r) and C=(c_1,...,c_s) be tight paths with r,s>=2, and let u,v be the remaining two vertices. Consider the spanning ordering A,u,v,C. If (a_{r-1},a_r,u) is tight while (v,c_1,c_2) is non-tight, then (a_r,u,v) is non-tight and therefore (v,u,a_r) is tight. If (a_{r-1},a_r,u) is non-tight while (v,c_1,c_2) is tight, then (u,v,c_1) is non-tight and therefore (c_1,v,u) is tight. Consequently, in the mixed case L=R={z} of toolkit_a_two_vertex_middle_path_forces_an_endpoint_reversal_pattern, writing w for the other middle vertex, both (w,z,a_r) and (c_1,z,w) are tight.

Let pi=A,u,v,C. All defect centers of pi lie among the four consecutive centers at the two joins and the two middle positions. Number these local centers 1,2,3,4 from left to right. Center 1 corresponds to (a_{r-1},a_r,u), center 2 to (a_r,u,v), center 3 to (u,v,c_1), and center 4 to (v,c_1,c_2).

Suppose center 1 is tight and center 4 is non-tight. If center 2 were also tight, then every defect center of pi would lie among centers 3 and 4. Those are consecutive, so the defect-line matching number would be at most one. By the defect-line identity, pi would split into at most two tight paths, contradicting pc(H)>=3. Therefore center 2 is non-tight. Boundary antisymmetry then gives (v,u,a_r) tight.

The symmetric argument applies when center 1 is non-tight and center 4 is tight. If center 3 were tight, all defects would lie among centers 1 and 2, again giving defect-line matching number at most one. Hence center 3 is non-tight, and boundary antisymmetry gives (c_1,v,u) tight.

Now apply this to the mixed alternative L=R={z} from toolkit_a_two_vertex_middle_path_forces_an_endpoint_reversal_pattern. Let w be the other middle vertex. In the ordering A,z,w,C, the left outer join is tight and the right outer join is non-tight, so (w,z,a_r) is tight. In the ordering A,w,z,C, the left outer join is non-tight and the right outer join is tight, so (c_1,z,w) is tight.

Thus the mixed endpoint-attachment pattern is not merely an attachment/reversal classification: it forces two additional inner reverse triples, one pointing back into A and one pointing back into C.

### A mixed two-vertex middle forces an endpoint-rooted Hamiltonian four-set

**Statement.** Let H be a minimum counterexample and let A|(z,w)|C be a spanning three-cover in the mixed attachment case, with r=|A|, s=|C| at least two. Put a=a_{r-1}, b=a_r, c=c_1, d=c_2. Then either L={a,b,z,w} is Hamiltonian, in which case repartitioning A|(z,w) gives the same-component cover (a_1,...,a_{r-2})|L|C; or R={z,w,c,d} is Hamiltonian, symmetrically giving a same-component repartition; or both L,R are non-Hamiltonian, in which case (a,z,w,c) is a tight Hamiltonian four-path. In the third case its complement has path-cover number two by minimality, but no same-component pairwise-repartition claim is made.

The mixed-case lemmas give tight triples (a,b,z), (w,b,a), (w,z,b) on L={a,b,z,w}, and (z,c,d), (d,c,w), (c,z,w) on R={z,w,c,d}.

If L is Hamiltonian, then L together with the inherited prefix (a_1,...,a_{r-2}) partitions A union {z,w} into two tight paths (with the empty prefix omitted when r=2). Hence replacing A|(z,w) by these paths is a legal pairwise repartition, while C is unchanged. The symmetric statement holds if R is Hamiltonian.

Assume both L and R are non-Hamiltonian. By the non-Hamiltonian four-set matching-block classification, each is edge-orderable with its three opposite-edge matchings in consecutive blocks. On L the known triples give bw<ab<bz and wz<bz. With opposite-edge matchings {bw,az}, {ab,wz}, {bz,aw}, the block order is forced to be {bw,az}<{ab,wz}<{bz,aw}. Hence az<wz, so (a,z,w) is tight.

On R the known triples give zc<cd<cw and zc<zw. With opposite-edge matchings {zc,dw}, {cd,zw}, {cw,zd}, the block order is forced in that order. Hence zw<cw, so (z,w,c) is tight. Therefore (a,z,w,c) is a tight Hamiltonian four-path.

This cross support is proper, so minimum-counterexample calculus gives path-cover number two on its complement. However, it uses vertices from A, the middle component, and C simultaneously. Thus its existence alone does not certify that the resulting three-cover lies in the original pairwise-repartition component. The precise residue is therefore the double-non-Hamiltonian local case together with this forced cross four-path.

### A mixed two-vertex middle forces strict quadratic descent

**Statement.** Let H be a minimum counterexample and let A|(z,w)|C be a spanning three-cover with |A|=r, |C|=s, r,s>=2. Assume the mixed attachment case of toolkit_a_two_vertex_middle_path_forces_an_endpoint_reversal_pattern: one middle vertex z attaches to both exposed ends and the other vertex w reverses both. Then a single pairwise repartition strictly decreases Phi=sum |P_i|^2.

Put a=a_{r-1}, b=a_r, c=c_1, d=c_2. Since H is a minimum counterexample, n=|V(H)|>10. Hence r+s=n-2>8, so at least one of r,s is at least five. By symmetry suppose r>=5.

Consider the local four-set L={a,b,z,w} on the union of the components A and (z,w).

If L is Hamiltonian, choose a Hamilton path on L. The inherited prefix A_0=(a_1,...,a_{r-2}) is tight. Therefore A|(z,w) can be pairwise repartitioned as A_0|L, with the empty prefix omitted when necessary. The two affected component orders change from (r,2) to (r-2,4). The potential change is

(r-2)^2+4^2-r^2-2^2 = 16-4r < 0

because r>=5.

Assume L is non-Hamiltonian. The mixed-case inner-reversal lemma supplies the tight triples (a,b,z), (w,b,a), and (w,z,b). By the non-Hamiltonian four-set matching-block classification, the opposite-edge matchings {bw,az}, {ab,wz}, {bz,aw} occur as consecutive blocks. The known inequalities bw<ab<bz force this block order. Hence bw<wz, so (b,w,z) is tight.

Thus A|(z,w) can be pairwise repartitioned as

(a_1,...,a_{r-1}) | (b,w,z).

The affected orders change from (r,2) to (r-1,3), and the potential change is

(r-1)^2+3^2-r^2-2^2 = 6-2r < 0.

Therefore the side of order at least five always yields a strict one-step quadratic descent, regardless of whether its local four-set is Hamiltonian. The argument is symmetric when s>=5. Since one of r,s is at least five, every mixed two-vertex attachment state strictly descends.

### A quadratic-minimal two-vertex middle has a doubled same-side reversal

**Statement.** Let H be a minimum counterexample and let A|(u,v)|C be a spanning three-cover with |A|,|C|>=2. Assume this cover is Phi-minimal in its pairwise-repartition component. Then either both (u,a_r,a_{r-1}) and (v,a_r,a_{r-1}) are tight, or both (c_2,c_1,u) and (c_2,c_1,v) are tight (or both conclusions hold).

For the two middle vertices define L={z in {u,v}:(a_{r-1},a_r,z) is tight} and R={z in {u,v}:(z,c_1,c_2) is tight}. The two-vertex middle classification gives three possibilities: L is empty, R is empty, or L=R={z} for one middle vertex z. In the third, mixed case, toolkit_a_mixed_two_vertex_middle_forces_strict_quadratic_descent gives a one-step pairwise repartition with strictly smaller Phi, contradicting Phi-minimality. Hence L is empty or R is empty. If L is empty, boundary antisymmetry gives both reverse triples (u,a_r,a_{r-1}) and (v,a_r,a_{r-1}); if R is empty, it gives both (c_2,c_1,u) and (c_2,c_1,v).

### Any two-vertex component beside a path of order at least four strictly descends

**Statement.** Let H be any boundary tournament and let U|C be two components of a path cover, where |U|=2 and C=(c_1,...,c_s) is a tight path with s>=4. Then U union V(C) has a two-path cover with component orders 3 and s-1. Consequently the quadratic potential changes by (3^2+(s-1)^2)-(2^2+s^2)=6-2s<0. Therefore every spanning three-cover of a minimum counterexample that contains a component of order two admits a strict pairwise Phi-decrease.

Write U={u,v} and C=(c_1,...,c_s). By boundary antisymmetry, exactly one of (u,c_1,v) and (v,c_1,u) is tight. Thus the three-set {u,v,c_1} has a tight Hamiltonian path T of order three. The inherited suffix C'=(c_2,...,c_s) is a tight path of order s-1. Hence T|C' is a two-cover of U union V(C), obtained by a legal pairwise repartition of the two displayed components.

The affected component orders change from (2,s) to (3,s-1), so

Delta Phi = 3^2+(s-1)^2-2^2-s^2 = 6-2s,

which is strictly negative for s>=4.

Now let H be a minimum counterexample and let a spanning three-cover contain a two-vertex component. Since |V(H)|>10, the other two component orders sum to more than eight, so at least one is at least five. Pairing the two-vertex component with that path gives the strict descent above. Thus no Phi-minimal three-cover of a minimum counterexample has a component of order two. This argument does not require the two-vertex component to sit between two nontrivial paths, so it also applies to singleton lifts of profile 1|2|m.

### Quadratic-minimal three-covers have no components of order one or two

**Statement.** Let H be a minimum counterexample and let P_1|P_2|P_3 be a spanning three-cover that minimizes Phi=sum |P_i|^2 in its pairwise-repartition component. Then |P_i|>=3 for each i.

Suppose first that one component is a singleton (x). Since |V(H)|>10, among the other two components one has order s>=5, say C=(c_1,...,c_s). The pair (x,c_1) is a tight path of order two by definition, while (c_2,...,c_s) is the inherited suffix of C. Thus the pairwise repartition

(x)|C  ->  (x,c_1)|(c_2,...,c_s)

changes the affected component orders from (1,s) to (2,s-1). Its potential change is

2^2+(s-1)^2-1^2-s^2 = 4-2s < 0,

contradicting Phi-minimality.

Suppose instead that one component has order two. The other two component orders sum to more than eight, so one has order at least five. The general two-vertex balancing lemma repartitions (2,s) to (3,s-1), with potential change 6-2s<0. Again this contradicts Phi-minimality.

Therefore every component of a Phi-minimal spanning three-cover has order at least three.

### A three-vertex component beside a path of order at least six strictly descends

**Statement.** Let H be a boundary tournament and let T|C be two components of a path cover, where T is a tight path of order three and C=(c_1,...,c_s) is a tight path with s>=5. If either T union {c_1} or T union {c_s} is Hamiltonian, there is a pairwise repartition with orders (4,s-1) and Delta Phi=8-2s<0. If both four-sets are non-Hamiltonian, then T union {c_1,c_s} is Hamiltonian and there is a pairwise repartition with orders (5,s-2) and Delta Phi=20-4s. Consequently no Phi-minimal three-cover contains component orders 3 and s>=6. For s=5, every Phi-minimal such pair has both endpoint four-extensions non-Hamiltonian and admits an equal-Phi 3|5 to 5|3 rotation.

Let
\[
T=(t_1,t_2,t_3),\qquad C=(c_1,\ldots,c_s),
\qquad s\ge5.
\]

Suppose first that
\[
H[T\cup\{c_1\}]
\]
is Hamiltonian. Let \(K\) be a Hamilton path on this four-set. Then
\[
K\mid(c_2,\ldots,c_s)
\]
is a two-cover of \(T\cup V(C)\), so replacing the displayed pair \(T\mid C\) gives a legal pairwise repartition with component orders
\[
(3,s)\longrightarrow(4,s-1).
\]
The change in the two affected square terms is
\[
4^2+(s-1)^2-3^2-s^2=8-2s<0.
\]
The same argument applies if \(T\cup\{c_s\}\) is Hamiltonian, using the inherited prefix \((c_1,\ldots,c_{s-1})\).

Assume therefore that both endpoint extensions
\[
T\cup\{c_1\},
\qquad
T\cup\{c_s\}
\]
are non-Hamiltonian. The two-bad-four-extensions lemma in [[localextend01]] applies to the tight three-path \(T\) and the exterior vertices \(c_1,c_s\). It yields a Hamiltonian five-path on
\[
T\cup\{c_1,c_s\}.
\]
Together with the inherited interior path
\[
(c_2,\ldots,c_{s-1}),
\]
this gives a pairwise repartition
\[
(3,s)\longrightarrow(5,s-2).
\]
Its potential change is
\[
5^2+(s-2)^2-3^2-s^2=20-4s.
\]

If \(s\ge6\), this quantity is strictly negative. Hence a \(\Phi\)-minimal three-cover cannot contain a 3-vertex component beside a component of order at least six.

When \(s=5\), direct Hamiltonian enlargement to order four still gives the strict change \(8-2s=-2\), so at a \(\Phi\)-minimum both endpoint four-extensions must be non-Hamiltonian. The preceding five-path construction then gives
\[
(3,5)\longrightarrow(5,3)
\]
with zero change in \(\Phi\). Thus the boundary case is an explicit neutral endpoint rotation.

### Every deletion-cover singleton lift strictly descends to a rooted three-vertex component

**Statement.** Let H be a minimum counterexample and H-x=P|Q a deletion cover. Then one of P,Q has order r>=4. If R=(r_1,...,r_r) is such a component, the singleton lift P|Q|{x} admits one pairwise repartition replacing R|{x} by a tight three-vertex path on {x,r_1,r_2} and the inherited tail (r_3,...,r_r). The quadratic potential decreases by 4(r-3).

Let H be a minimum counterexample and let
H-x=P|Q
be a deletion cover. Its singleton lift is
P|Q|{x}.

First, |V(H)|>=8. For |V(H)|<=6, partition V(H) into two sets of order at most three; every set of order at most three has a Hamilton tight path. For |V(H)|=7, choose any five-set S. If S is Hamiltonian, deleting an endpoint of a Hamilton order leaves a Hamiltonian four-set. If S is non-Hamiltonian, the five-set small-order theorem gives a Hamiltonian four-subset of S. In either case H has a Hamiltonian four-set whose complementary three-set is Hamiltonian, yielding a two-cover. Thus a minimum counterexample has order at least eight.

Since |P|+|Q|=|V(H)|-1>=7, at least one of P,Q has order r>=4. Let
R=(r_1,...,r_r)
be such a path.

By boundary antisymmetry, exactly one of
(x,r_1,r_2)
and
(r_2,r_1,x)
is tight. Let T be the resulting tight path on {x,r_1,r_2}. The inherited tail
R'=(r_3,...,r_r)
is also a nonempty tight path. Hence
R|{x}
may be replaced in one pairwise repartition by
T|R'.

Only the component orders r and 1 change, becoming 3 and r-2. Therefore
Phi_new-Phi_old
=9+(r-2)^2-r^2-1
=12-4r
=-4(r-3)<0.

Thus every deletion-cover singleton lift admits a one-step strict quadratic descent to a three-cover in which the deleted label x lies in a three-vertex component together with two consecutive vertices taken from an endpoint of one displayed deletion-cover path. The terminal pair (r_{r-1},r_r) gives the symmetric construction.

### A Phi-minimum containing a three-path has order at most thirteen

**Statement.** Let H be a minimum counterexample and let C be a spanning three-cover minimizing Phi in its pairwise-repartition component. If one component of C has order three, then |V(H)|<=13. More precisely, the size multiset of C is one of {3,3,5}, {3,4,4}, {3,4,5}, {3,5,5}.

By toolkit_minimal_three_covers_have_no_components_of_order_one_or_two, every component of C has order at least three. Let one component T have order three. By three_vertex_component_long_neighbor_rotation01, T cannot sit beside a path of order at least six in a Phi-minimal state. Therefore each of the other two components has order at most five.

Hence |V(H)|<=3+5+5=13. On the other hand mincex01 gives |V(H)|>10. Writing the other two component orders as 3<=a<=b<=5 and requiring 3+a+b>10 leaves exactly

(3,3,5), (3,4,4), (3,4,5), (3,5,5).

Thus every Phi-minimal state of order at least fourteen has all three component orders at least four, and the entire three-component residue is confined to these four bounded profiles.

### A rooted five-side has a root-preserving common endpoint core or a two-pair root-exchange split

**Statement.** Let X be a Hamiltonian five-set with distinguished root x, and let a,b be vertices outside X such that X∪{a} and X∪{b} are non-Hamiltonian. For u∈{a,b}, let G_u={t∈X:(X-{t})∪{u} is Hamiltonian}. Then |G_a|,|G_b|≥3. Hence either some t≠x belongs to G_a∩G_b, giving a common Hamiltonian endpoint-replacement core that still contains x, or G_a∩G_b={x}, x∈G_a∩G_b, and the four non-root vertices split into two disjoint pairs G_a-{x} and G_b-{x}.

Let X be a Hamiltonian set of order five, let x in X be distinguished, and let a,b be vertices outside X. Assume X union {a} and X union {b} are both non-Hamiltonian.

For u in {a,b}, define
G_u={t in X : (X-{t}) union {u} is Hamiltonian}.

Consider the non-Hamiltonian six-set X union {u}. By the four-of-six theorem, at least four of its five-vertex deletions are Hamiltonian. Deleting u leaves X, which is Hamiltonian. Therefore at least three deletions by vertices t in X are Hamiltonian, and hence
|G_u|>=3.

If there is t in (G_a intersect G_b)-{x}, then both
(X-{t}) union {a}
and
(X-{t}) union {b}
are Hamiltonian and their common four-vertex core X-{t} still contains the distinguished root x. This is the root-preserving alternative.

Assume no such non-root t exists. Then
(G_a-{x}) intersect (G_b-{x})=emptyset.
Since X-{x} has four vertices, the lower bounds |G_a|,|G_b|>=3 force x to belong to both G_a and G_b: otherwise one of G_a-{x},G_b-{x} would have size at least three while the other has size at least two, impossible for disjoint subsets of a four-set.

Thus each of G_a-{x} and G_b-{x} has size at least two. They are disjoint subsets of the four-set X-{x}, so each has size exactly two and together they partition X-{x}. Consequently
G_a intersect G_b={x},
G_a={x} union A,
G_b={x} union B,
where A,B are disjoint two-sets with A union B=X-{x}.

Hence failure of a root-preserving common endpoint core has a unique form: the root x is the unique common removable label, and the remaining four labels split into two endpoint-specific exchange pairs.

### A Phi-minimal 3|5 pair forces a complementary matching-block four-set

**Statement.** Let H be a minimum counterexample and let a Phi-minimal spanning three-cover contain components T|C with |T|=3 and C=(c_1,c_2,c_3,c_4,c_5). Then there exists a two-set E subset V(T) such that S={c_1,c_5} union E is Hamiltonian. If w is the unique vertex of T-E, then F={w,c_2,c_3,c_4} is non-Hamiltonian. Therefore F is edge-orderable and its three opposite-edge perfect matchings occur as three consecutive blocks.

Apply prescribed_pair_mixed_four_supports01 with the prescribed pair {c_1,c_5} and the exterior three-set V(T). It gives a two-set E subset V(T) such that

S={c_1,c_5} union E

is Hamiltonian. Let w be the remaining vertex of T, and put

F={w,c_2,c_3,c_4}.

The sets S and F are complementary inside V(T) union V(C). If F were Hamiltonian, then S|F would be a two-cover of that union with component orders (4,4). Replacing the displayed pair T|C would therefore be a legal pairwise repartition

(3,5) -> (4,4).

Its quadratic-potential change is

4^2+4^2-3^2-5^2 = 32-34 = -2,

contradicting Phi-minimality. Hence F is non-Hamiltonian.

By smallset01, every non-Hamiltonian four-set is edge-orderable and its six ordinary edges occur in three consecutive opposite-edge matching blocks. Thus every Phi-minimal 3|5 pair carries a canonical local matching-block obstruction on one remaining 3-core vertex together with the three interior vertices of the displayed 5-path.

### The root-exchange split forces four-core disturbance or an outer Hamiltonian six-set

**Statement.** Let C be a four-set and x,a,b distinct exterior vertices. Suppose C∪{x}, C∪{a}, C∪{b} are Hamiltonian while C∪{x,a} and C∪{x,b} are non-Hamiltonian. Then at least one of the following holds: two chosen Hamilton orders on the three five-sets disagree on the relative order of C; there is a Hamiltonian four-set inside C∪{x,a,b}; a tight triple through one vertex of C reverses a displayed core edge between two extenders; or C∪{a,b} is Hamiltonian.

Let C be a four-vertex set and let x,a,b be distinct vertices outside C. Assume
C union {x},
C union {a},
C union {b}
are Hamiltonian, while
C union {x,a}
and
C union {x,b}
are non-Hamiltonian.

Choose Hamilton paths P_x,P_a,P_b on the three Hamiltonian five-sets. Apply the blocked four-core extension-star theorem with center r_0=x and leaves r_1=a,r_2=b. Its center-leaf non-Hamiltonicity hypotheses are exactly the two displayed assumptions.

The theorem gives at least one of four outcomes:

1. two of P_x,P_a,P_b have a relative-order disagreement on C;
2. there is a Hamiltonian four-set contained in C union {x,a,b};
3. for two extenders among x,a,b and some c in C, a tight triple through c reverses a displayed core edge of one of the chosen five-paths;
4. the outer-pair six-set C union {a,b} is Hamiltonian.

In particular, apply this to the exceptional branch of the rooted-five endpoint refinement. There X is a Hamiltonian five-set with root x, C=X-{x}, and a,b are the two exterior endpoints. Failure of a root-preserving common removable label forces x to be the unique common removable label, so both C union {a} and C union {b} are Hamiltonian; the original X=C union {x} is Hamiltonian, while the bad endpoint-extension hypothesis gives non-Hamiltonicity of C union {x,a}=X union {a} and C union {x,b}=X union {b}. Hence the exceptional root-loss branch always yields one of the four outcomes above.

### The 3|5 matching-block residue gives an interior end-edge reversal or a central sandwich

**Statement.** Let H be a minimum counterexample and let T|C be components of a Phi-minimal three-cover with |T|=3 and C=(c_1,...,c_5). Let w in T be chosen so that F={w,c_2,c_3,c_4} is the non-Hamiltonian matching-block four-set given by toolkit_minimal_35_pair_forces_a_complementary_matching_block_four_set. Then one of the following holds: (i) (w,c_3,c_2) is tight; (ii) (c_4,c_3,w) is tight; (iii) both (c_2,c_3,w) and (w,c_3,c_4) are tight.

Because F is a non-Hamiltonian four-set, smallset01 gives an edge order in which the three opposite-edge perfect matchings are consecutive blocks. Write

e_1=c_2c_3,  e_2=c_3c_4.

Since (c_2,c_3,c_4) is tight, e_1<e_2. The opposite-edge matching containing e_1 is

M_1={c_2c_3,wc_4},

and the matching containing e_2 is

M_2={c_3c_4,wc_2}.

Thus the matching blocks satisfy M_1<M_2. The third block is

M_3={c_2c_4,wc_3}.

There are exactly three possible block orders compatible with M_1<M_2.

If M_3<M_1<M_2, then wc_3<c_2c_3, so (w,c_3,c_2) is tight. This reverses the displayed edge (c_2,c_3).

If M_1<M_2<M_3, then c_3c_4<wc_3, so (c_4,c_3,w) is tight. This reverses the displayed edge (c_3,c_4).

If M_1<M_3<M_2, then c_2c_3<wc_3<c_3c_4. Hence both (c_2,c_3,w) and (w,c_3,c_4) are tight.

Therefore every Phi-minimal 3|5 pair yields an explicit interior end-edge reversal unless the unique middle-block sandwich configuration occurs.

### Two neutral 3|5 rotations perform a controlled two-for-two support exchange

**Statement.** Let H be a minimum counterexample and let T|C be two components of a Phi-minimal spanning three-cover, where |T|=3 and C=(c_1,c_2,c_3,c_4,c_5). Then there exist distinct t_1,t_2,w in V(T) and a sequence of two equal-Phi pairwise repartitions, staying in the same repartition component, which transforms the displayed pair into U|L where U is a tight 3-path on {w,c_1,c_5} and L is a tight 5-path on {t_1,t_2,c_2,c_3,c_4}.

Because the state is Phi-minimal, three_vertex_component_long_neighbor_rotation01 implies that T union {c_1} and T union {c_5} are both non-Hamiltonian. Apply the controlled two-bad-four-extensions lemma from localextend01 to the tight three-path T and the exterior vertices c_1,c_5. It yields a Hamiltonian five-path K on

V(T) union {c_1,c_5}

whose two endpoints both lie in V(T). Let those endpoints be t_1,t_2 and write w for the third vertex of T. The complementary interior path

C^o=(c_2,c_3,c_4)

is tight, so replacing T|C by K|C^o is a legal pairwise repartition of profile 3|5 -> 5|3. Its Phi change is zero.

The new state is therefore also Phi-minimal. View the displayed pair now as C^o|K, with C^o the 3-side and K the 5-side. At a Phi-minimum, neither endpoint of K can Hamiltonian-extend C^o, because such an extension would give the strict 3|5 -> 4|4 descent. Thus C^o union {t_1} and C^o union {t_2} are both non-Hamiltonian.

Apply the same controlled two-bad-four-extensions lemma again, now to the tight three-path C^o and exterior vertices t_1,t_2. It gives a Hamiltonian five-path L on

{c_2,c_3,c_4,t_1,t_2}

whose endpoints lie in {c_2,c_3,c_4}. The complementary path in K is its interior after deleting the endpoints t_1,t_2 of K. Since K has vertex set {t_1,t_2,w,c_1,c_5} and endpoints t_1,t_2, this interior is a tight three-path U with vertex set

{w,c_1,c_5}.

Hence the second equal-Phi pairwise repartition changes C^o|K to L|U. Overall, two neutral rotations exchange the pair {t_1,t_2} from the old 3-side with the endpoint pair {c_1,c_5} of the old 5-side, while the vertex w remains on the 3-side and the interior triple {c_2,c_3,c_4} moves to the 5-side.

### A 3|4 pair gives a neutral endpoint swap or a controlled 5|2 detour

**Statement.** Let H be a boundary tournament and let T|C be two components of a path cover, with |T|=3 and C=(c_1,c_2,c_3,c_4). Then either (i) T union {c_1} or T union {c_4} is Hamiltonian, yielding a pairwise repartition with orders (4,3) and no change in quadratic potential, or (ii) both endpoint four-extensions are non-Hamiltonian, in which case there is a pairwise repartition with orders (5,2), where the 5-path has vertex set V(T) union {c_1,c_4} and both its endpoints lie in V(T), while the 2-path is (c_2,c_3).

If T union {c_1} is Hamiltonian, let K be a Hamilton path on that four-set. Then K|(c_2,c_3,c_4) is a two-cover of V(T) union V(C), with orders (4,3). The same holds using c_4 and the inherited prefix (c_1,c_2,c_3). Since 4^2+3^2=3^2+4^2, this is Phi-neutral.

Assume both T union {c_1} and T union {c_4} are non-Hamiltonian. Apply the controlled two-bad-four-extensions lemma in localextend01 to the tight three-path T and exterior vertices c_1,c_4. It produces a Hamiltonian five-path K on V(T) union {c_1,c_4}, with both endpoints in V(T). The complementary pair (c_2,c_3) is a tight path of order two. Hence K|(c_2,c_3) is a legal pairwise repartition of T|C with orders (5,2).

Thus every 3|4 pair has exactly the useful local menu: neutral endpoint swap, or controlled 5|2 detour with the two-path equal to the displayed interior edge of C.

### A Phi-minimal 3|3|5 state forces a cross-side Hamiltonian five-support

**Statement.** Let H be a minimum counterexample and let T_1|T_2|C be a Phi-minimal spanning three-cover with |T_1|=|T_2|=3 and C=(c_1,c_2,c_3,c_4,c_5). Then there exist w_i in V(T_i), i=1,2, such that each four-set {w_i,c_2,c_3,c_4} is non-Hamiltonian, while the five-set K={w_1,w_2,c_2,c_3,c_4} is Hamiltonian. Consequently H-K is non-Hamiltonian and has path-cover number two.

Apply toolkit_minimal_35_pair_forces_a_complementary_matching_block_four_set first to T_1|C and then to T_2|C. This gives vertices w_1 in T_1 and w_2 in T_2 such that

F_i={w_i,c_2,c_3,c_4}

is non-Hamiltonian for i=1,2. The three-set

I={c_2,c_3,c_4}

is a tight path, since it is an inherited contiguous subpath of C.

Thus F_1=I union {w_1} and F_2=I union {w_2} are two non-Hamiltonian four-extensions of the same tight three-path I. Apply the controlled two-bad-four-extensions lemma in localextend01. It yields a Hamiltonian five-path on

K=I union {w_1,w_2}={w_1,w_2,c_2,c_3,c_4},

with both endpoints lying in I.

The set K is proper. By minimum-counterexample calculus, H-K has path-cover number at most two. It cannot be Hamiltonian, because a Hamilton path on H-K together with the Hamilton path on K would give a two-cover of H. Hence pc(H-K)=2.

So the two local 3|5 obstructions cannot remain independent: in profile 3|3|5 they synchronize on the common interior triple and force a proper Hamiltonian five-support meeting both 3-sides, with two-coverable complement.

### Every Phi-minimal 3|4|5 state has a nontrivial neutral reconfiguration

**Statement.** Let H be a minimum counterexample and let T|C|D be a Phi-minimal spanning three-cover with |T|=3, |C|=4, |D|=5. Then there is a nontrivial sequence of at most two pairwise repartitions ending at another three-cover of the same size multiset {3,4,5} and the same quadratic potential.

Apply toolkit_34_pair_gives_a_neutral_endpoint_swap_or_a_controlled_52_detour to T|C.

In the first outcome, one endpoint of C Hamiltonian-extends T. Replacing T|C by the corresponding 4|3 cover is a one-step nontrivial pairwise repartition with no change in Phi. The third component D is unchanged, so the full size multiset remains {3,4,5}.

In the second outcome, both endpoint extensions are non-Hamiltonian and T|C repartitions as K|E with |K|=5 and |E|=2, where E is the displayed interior edge of C. The first move changes the affected square sum from 3^2+4^2=25 to 5^2+2^2=29, an increase of 4.

Now pair E with the untouched 5-path D=(d_1,...,d_5). The general two-vertex balancing lemma gives a repartition of E|D with component orders 3 and 4: explicitly, E union {d_1} has a tight Hamiltonian 3-path and (d_2,...,d_5) is tight. This changes the affected square sum from 2^2+5^2=29 to 3^2+4^2=25, a decrease of 4.

Thus the two-step route

3|4|5 -> 5|2|5 -> 5|3|4

returns exactly to the original value of Phi and to the same size multiset {3,4,5}. Since the intermediate and final covers are obtained by legal pairwise repartitions, they lie in the same component of the repartition graph.

Therefore every Phi-minimal 3|4|5 state has an explicit neutral recurrence: a one-step endpoint swap or a controlled two-step detour through a temporary two-vertex component.

### A Phi-minimal 3|4|4 state has a neutral swap, an order disagreement, or a common terminal pair

**Statement.** Let H be a minimum counterexample and let T|A|B be a Phi-minimal spanning three-cover with |T|=3 and |A|=|B|=4, where A=(a_1,a_2,a_3,a_4) and B=(b_1,b_2,b_3,b_4). Then at least one of the following holds: (i) T|A or T|B admits a Phi-neutral 3|4 to 4|3 endpoint swap; (ii) there are Hamiltonian five-paths K_A on V(T) union {a_1,a_4} and K_B on V(T) union {b_1,b_4} whose restrictions to V(T) have different relative orders; (iii) there is a fixed two-set E subset V(T) such that both K_A and K_B can be chosen with endpoint set exactly E.

Apply toolkit_34_pair_gives_a_neutral_endpoint_swap_or_a_controlled_52_detour to T|A and T|B.

If either pair is in the neutral endpoint-swap outcome, we have (i). Assume neither is. Then both endpoint extensions are non-Hamiltonian on each side. The controlled two-bad-four-extensions lemma yields a Hamiltonian five-path K_A on V(T) union {a_1,a_4} with both endpoints in V(T), and similarly a Hamiltonian five-path K_B on V(T) union {b_1,b_4} with both endpoints in V(T). Let E_A,E_B be their two-element endpoint sets inside V(T).

If E_A is not equal to E_B, then the restrictions of K_A and K_B to the common three-set V(T) have different relative orders. Indeed, because both global endpoints of each K lie in T, those two endpoints are exactly the first and last vertices of T in the restricted order. Distinct endpoint pairs therefore give distinct extremal pairs, so the restricted total orders cannot agree. This is outcome (ii). The standard order-disagreement machinery then turns such a pair into a tight reversal.

If E_A=E_B, put E=E_A. Then both forced Hamiltonian five-paths use the same two vertices of T as their global endpoints, giving outcome (iii).

Thus the only 3|4|4 state that avoids both a neutral endpoint swap and an order disagreement is a common-terminal-pair configuration: the two locked 4-sides synchronize on the same pair of endpoints in the 3-side.

### A rooted six-support yields a one-label transfer or a path disturbance

**Statement.** Let H be a minimum counterexample, let X be a proper Hamiltonian six-set with distinguished root x, and let H-X=P|Q. Then there exists d in X-{x} such that X-d is Hamiltonian and (P union Q)+d has path-cover number two. For any two-cover R|S of (P union Q)+d, relative to P|Q|{d}, either (1) there is exactly one interclass edge, necessarily joining d to one of P,Q, and hence a root-preserving pairwise repartition (X-d)|(P+d)|Q or its symmetric analogue; or (2) one of P,Q occurs in at least two comparison blocks, and therefore either an inherited displayed edge of that support has endpoints in different comparison paths, or one comparison path leaves that support through a nonempty exterior segment and later returns.

Choose a Hamilton path on X and an endpoint d distinct from the root. By [[ham6goodsquare01]], X-d is Hamiltonian and K+d is non-Hamiltonian with path-cover number two, where K=V(P) union V(Q). Fix a two-cover R|S of K+d. Decompose R,S into maximal blocks contained in P,Q,{d}. If b_P,b_Q are the block counts of the two old supports and t is the number of interclass edges, then t=b_P+b_Q-1. If t=1, then b_P=b_Q=1. The unique interclass edge cannot join P to Q, because then P union Q would be Hamiltonian and, together with X, would two-cover H. Thus d joins exactly one old support and gives the stated root-preserving pairwise transfer. Suppose t>=2. Then b_P+b_Q=t+1>=3, so one old support, say P, has at least two comparison blocks. If vertices of P occur in both R and S, some consecutive pair in the displayed Hamilton order of P lies in different comparison paths, giving a split inherited edge. Otherwise all P-vertices lie in one comparison path, but at least two maximal P-blocks occur there; a nonempty block of another displayed class lies between two consecutive P-blocks, so that comparison path leaves P through exterior vertices and later returns. Thus every non-transfer comparison is already a path disturbance.

### Every quadratic-minimal 3|5|5 profile lies on a nontrivial neutral cycle

**Statement.** Let H be a minimum counterexample and let T|A|B be a Phi-minimal spanning three-cover with |T|=3 and |A|=|B|=5. Then T|A admits a nontrivial equal-Phi repartition of orders 5|3, and independently T|B admits another such repartition. The two resulting three-covers are distinct and still have profile 3|5|5. Consequently, in the graph of Phi-minimal 3|5|5 covers in the same pairwise-repartition component, every vertex has degree at least two; in particular every connected component contains a cycle of length at least three.

Write A=(a1,a2,a3,a4,a5). If T union {a1} or T union {a5} were Hamiltonian, then T|A would repartition from orders (3,5) to (4,4), changing the quadratic contribution by 16+16-9-25=-2, contradicting Phi-minimality. Hence both endpoint four-extensions are non-Hamiltonian. By A three-vertex component beside a path of order at least six strictly descends, T union {a1,a5} is Hamiltonian and (a2,a3,a4) is an inherited tight path, so T|A has a nontrivial neutral repartition (3,5)->(5,3). The same argument with B gives a second neutral neighbor. The two neighbors are distinct because in the first the new 3-side is contained in A, while in the second it is contained in B, and A,B are disjoint. Every equal-Phi neighbor is again Phi-minimal in the same repartition component. Therefore every vertex of the finite graph of Phi-minimal 3|5|5 states has at least two distinct neighbors. Every finite graph of minimum degree at least two contains a cycle; because the repartition graph is simple, the cycle has length at least three.

### A Hamiltonian six-support reduces to a five-support retaining any prescribed vertex

**Statement.** Let H be a minimum counterexample, let U be a proper Hamiltonian six-vertex set, and suppose K=H-U is non-Hamiltonian with path-cover number two. For every prescribed vertex a in U, there exists d in U-{a} such that U-{d} is Hamiltonian, contains a, and H-(U-{d})=K+d is non-Hamiltonian with path-cover number two.

Fix a Hamilton path on U. At least one endpoint differs from the prescribed vertex a; call it d. Deleting d leaves an inherited Hamilton path on U-{d}. By [[ham6goodsquare01]], adjoining either Hamilton-path endpoint to K gives a non-Hamiltonian induced subtournament of path-cover number two. Thus K+d has path-cover number two and U-{d} retains a.

### A quadratic minimum containing a four-support is small or has an order disagreement

**Statement.** Let H be a minimum counterexample and let C=P_1|P_2|P_3 be Phi-minimal in its pairwise-repartition component. Suppose some component has order four. Then at least one of the following holds: (1) C has a component of order three, hence |V(H)|<=13 and its size multiset is one of {3,3,5},{3,4,4},{3,4,5},{3,5,5}; (2) for the four-component X and some other displayed path P, the endpoint six-set of four_path_long_pair_escape01 has Hamiltonian five-vertex deletions with an order disagreement; (3) every component order belongs to {4,5,6}, so |V(H)|<=18 and the size multiset is one of {4,4,4},{4,4,5},{4,4,6},{4,5,5},{4,5,6},{4,6,6}.

Let X be a displayed component of order four. If another component has order three, A Phi-minimum containing a three-path has order at most thirteen gives outcome (1). Assume therefore that the other two component orders are at least four. Let P be either of them, of order m. If m>=7, apply A four-path beside a path of order at least six descends, disagrees, or makes the unique neutral migration to X|P. Its strict-descent alternative contradicts Phi-minimality, and its neutral migration occurs only when m=6. Therefore the only possible outcome for m>=7 is the order-disagreement alternative. Hence, if no such disagreement occurs, both components other than X have order at most six. Since they have order at least four, every component order lies in {4,5,6}. The six displayed multisets and the bound |V(H)|<=18 follow immediately.

## Toolkit Limbo placement audit: route-local results


### Every proper tight path induces a path-cover-two endpoint square on its complement

**Statement.** Let H be a minimum counterexample and let P=(p_0,...,p_m), m>=2, be a proper tight path. Put K=H-V(P). Then each of
K, K+{p_0}, K+{p_m}, and K+{p_0,p_m}
is non-Hamiltonian with path-cover number two.

Equivalently, the complement of every proper tight path of order at least three carries a full two-label path-cover-two square indexed by the two displayed endpoints of P.

The set V(P) is a proper Hamiltonian support, so minimum-counterexample calculus gives pc(K)=2 and K is non-Hamiltonian.

The complement of K+{p_0} is the inherited tight suffix (p_1,...,p_m). If K+{p_0} were Hamiltonian, a Hamilton path on it together with that suffix would two-cover H. Thus K+{p_0} is non-Hamiltonian; since it is proper, minimality gives path-cover number two. The argument for K+{p_m} is symmetric, using the inherited prefix (p_0,...,p_{m-1}).

Finally, the complement of K+{p_0,p_m} is the inherited middle path (p_1,...,p_{m-1}); when m=2 this is a singleton, which is still a tight path. Again Hamiltonicity of K+{p_0,p_m} would combine with that complementary path to two-cover H. Hence it is non-Hamiltonian and, by minimality, has path-cover number two.

No path reversal or cyclic invariance is used.



### Two bad endpoint extensions of a four-path give a two-path repartition or interior noninsertability

**Statement.** Let H be a boundary tournament, let W be a tight path on four vertices, write V(W)=D union {w} with |D|=3, and let Q=(f,q_1,...,q_{q-2},g) be a vertex-disjoint tight path of order q>=3. Suppose H[D union {f}] and H[D union {g}] are non-Hamiltonian. Put M=(q_1,...,q_{q-2}) and F=D union {f,g}. Then H[F] is Hamiltonian. Moreover either H[V(M) union {w}] is Hamiltonian, in which case F | (V(M) union {w}) is a two-path cover of V(W) union V(Q) whose quadratic potential differs from that of W|Q by 10-2q, or H[V(M) union {w}] is non-Hamiltonian, in which case w is noninsertable into every position of the inherited path M.

Choose any tight Hamilton order on the three-set D. Since D union {f} and D union {g} are both non-Hamiltonian, the certified two-bad-four-extensions lemma in localextend01 gives a Hamilton path on F=D union {f,g}. The supports F and V(M) union {w} are disjoint and partition V(W) union V(Q). If H[V(M) union {w}] is Hamiltonian, these two Hamilton paths give a two-path repartition of W|Q. Its component orders change from (4,q) to (5,q-1), so the quadratic-potential change is 25+(q-1)^2-16-q^2=10-2q. If H[V(M) union {w}] is non-Hamiltonian, inserting w into the inherited tight path M at any position would Hamiltonize that support, a contradiction. Hence w is noninsertable into M. No ambient third path, spanningness, extremality, or minimum-counterexample hypothesis is used.



### Local non-Hamiltonian interfaces force opposite-extremal matching blocks

**Statement.** Let H be a boundary tournament. Let S=(u,s_1,s_2,v) be a tight four-path, and let r_i,r_{i+1},r_j,r_{j+1} be vertices outside S (not necessarily all distinct except as required by the displayed four-sets below). Suppose (r_{i+1},u,r_i) and (r_{j+1},v,r_j) are tight. Assume the five-sets {r_i,u,s_1,s_2,v} and {u,s_1,s_2,v,r_{j+1}} are non-Hamiltonian, and the four-sets A={s_1,u,r_i,r_{i+1}} and B={s_2,v,r_j,r_{j+1}} are non-Hamiltonian. Then A and B are edge-orderable matching-block four-sets. In A, the opposite-edge matching {u r_i, s_1 r_{i+1}} is the highest block; in B, {v r_{j+1}, s_2 r_j} is the lowest block. Consequently (u,s_1,r_{i+1}), (u,r_{i+1},s_1), (r_i,s_1,r_{i+1}), (r_i,r_{i+1},s_1), (s_2,r_j,v), (r_j,s_2,v), (s_2,r_j,r_{j+1}), and (r_j,s_2,r_{j+1}) are tight.

Because (u,s_1,s_2) and (s_1,s_2,v) are tight, if (r_i,u,s_1) were tight then (r_i,u,s_1,s_2,v) would be a Hamilton tight path on the first displayed five-set, contrary to its assumed non-Hamiltonicity. Hence boundary antisymmetry gives (s_1,u,r_i) tight. Symmetrically, if (s_2,v,r_{j+1}) were tight then (u,s_1,s_2,v,r_{j+1}) would Hamiltonize the second displayed five-set, so (r_{j+1},v,s_2) is tight.

The four-sets A and B are non-Hamiltonian by hypothesis. The small-set matching-block classification therefore represents each by an edge order whose three opposite-edge perfect matchings form strict blocks.

For A define M_0={u r_i,s_1 r_{i+1}}, M_1={u s_1,r_i r_{i+1}}, M_2={u r_{i+1},r_i s_1}. Tightness of (s_1,u,r_i) means u s_1<u r_i, hence M_1<M_0. Tightness of (r_{i+1},u,r_i) means u r_{i+1}<u r_i, hence M_2<M_0. Thus M_0 is the highest block. Comparing every edge in M_1 and M_2 with the appropriate edge in M_0 gives the four asserted A-side tight triples.

For B define N_0={v r_{j+1},s_2 r_j}, N_1={v s_2,r_j r_{j+1}}, N_2={v r_j,s_2 r_{j+1}}. Tightness of (r_{j+1},v,s_2) gives v r_{j+1}<v s_2, hence N_0<N_1. Tightness of (r_{j+1},v,r_j) gives v r_{j+1}<v r_j, hence N_0<N_2. Thus N_0 is the lowest block, and the four asserted B-side triples follow. No minimum-counterexample, path-cover, ambient-order, or extremality hypothesis is used.



### A prescribed-pair six-set has a Hamiltonian, singleton-extension, overlap, or fixed-pair matching outcome

**Statement.** Let H be a minimum counterexample, let X be a proper Hamiltonian five-set with H-X non-Hamiltonian of path-cover number two, fix x in X, and fix distinct p,q outside X. Put A=X-{x} and S=A union {p,q}. Then at least one of the following holds: (1) S is Hamiltonian, with H-S non-Hamiltonian of path-cover number two; (2) at least one of A union {p}, A union {q} is Hamiltonian, hence one of p,q is a Hamiltonian-deletion label of S; (3) S is non-Hamiltonian, both A union {p} and A union {q} are non-Hamiltonian, and the Hamiltonian two-deletion graph J on A has adjacent edges, yielding the overlap-amplification conclusion of ad81548d4f9f; (4) S is non-Hamiltonian, both singleton extensions are non-Hamiltonian, and J is a perfect matching. In outcome (4), the two matching edges are exactly the two fixed-pair orientation classes of A relative to p,q, every cross pair gives a non-Hamiltonian four-set, and every cross cell carries the complete opposite-orientation hook rectangle of fixedpair_perfect_matching_hooks01.
In outcome (3), the union of the two overlapping Hamiltonian four-sets is itself Hamiltonian. In outcome (4), A is a non-Hamiltonian matching-block K4, and all eight four-sets (A-{a}) union {p} and (A-{a}) union {q}, a in A, are Hamiltonian. In particular, if A is Hamiltonian, outcome (4) is impossible.

If S is Hamiltonian, (1) holds and minimum-counterexample calculus gives the complement conclusion. Assume S is non-Hamiltonian. If A union {p}=S-{q} or A union {q}=S-{p} is Hamiltonian, then (2) holds. Hence assume both are non-Hamiltonian. Apply two_bad_five_extensions_all_opposite01 to the four-set A and exterior labels p,q. It gives that (A-{a}) union {p,q}=S-{a} is Hamiltonian for every a in A. Since S-{p}=A union {q} and S-{q}=A union {p} are non-Hamiltonian by assumption, the Hamiltonian-deletion set D of S is exactly A. Apply ad81548d4f9f to S. Its good two-deletion graph J on D=A either has adjacent edges, giving (3), or is a perfect matching. In the perfect-matching case apply fixedpair_perfect_matching_orientation01 and fixedpair_perfect_matching_hooks01 with fixed pair p,q and four-set A. They identify the matching edges with the two 2-vertex fixed-pair orientation classes and give the complete hook rectangle on every cross cell, proving (4).

Strengthening and earlier use. Apply bad_six_deletion_matching_fourcore01 to the six-set S in outcomes (3) and (4), where D=A. Adjacent edges de,df in the deletion graph give four-sets S-{d,e}, S-{d,f} with union S-{d}; this union is Hamiltonian because d belongs to D. If the graph is a perfect matching, the same theorem forces A to be a non-Hamiltonian matching-block K4 and makes all eight four-sets (A-{a})+{p}, (A-{a})+{q} Hamiltonian. Thus a Hamiltonian core A eliminates the matching outcome immediately, without deriving the orientation partition or hook rectangle. These conclusions use only the six-set and its deletion graph; the original five-support and its complement do not enter this local step.



### A Hamiltonian five-side admits prescribed-pair two-for-two support switches

**Statement.** Let H be a minimum counterexample, let X be a proper Hamiltonian five-vertex set, and suppose H-X is non-Hamiltonian with path-cover number two. Fix any x in X and any two distinct vertices p,q outside X. Then for at least two distinct vertices d in X-{x}, the five-set U_d=(X-{x,d}) union {p,q} is Hamiltonian. For every such d, H-U_d is non-Hamiltonian with path-cover number two. Consequently, if H-X=P|Q is any displayed two-cover, one may prescribe one vertex p of P and one vertex q of Q and move both simultaneously into a new Hamiltonian five-side while forcing any prescribed x in X out of the five-side.

Put A=X-{x}, so |A|=4, and put S={p,q}. The sets A and S are disjoint. Apply twofourhamdeletions01 to S and A. It gives at least two vertices d in A such that S union (A-{d})=(X-{x,d}) union {p,q} is Hamiltonian. Call this support U_d. Since X is proper and H is a minimum counterexample, |V(H)|>10; in particular each five-set U_d is proper. Minimum-counterexample calculus gives pc(H-U_d)<=2. If H-U_d were Hamiltonian, then a Hamilton path on U_d together with one on H-U_d would form a spanning two-cover of H, impossible. Hence H-U_d is non-Hamiltonian with path-cover number exactly two. The final sentence is the specialization when p and q are chosen from the two displayed components of H-X.



### Every four-side carries four endpoint-pair transport probes

**Statement.** Let H be a minimum counterexample and let X|P|Q be a spanning three-cover with |X|=4 and P=(p_1,...,p_m), m>=5. Put M=(p_2,...,p_{m-1}). Then either there is a legal pairwise repartition of X|P with nonincreasing quadratic potential, or the following holds simultaneously for every t in X. Define F_t=(X-{t}) union {p_1,p_m} and L_t=V(M) union {t}. If F_t is Hamiltonian, then L_t is non-Hamiltonian with path-cover number two. If F_t is non-Hamiltonian, then there is a set D_t subseteq F_t of at least four labels such that F_t-{d} is Hamiltonian and L_t union {d} is non-Hamiltonian with path-cover number two for every d in D_t. Any nonincreasing repartition produced by a Hamiltonian F_t|L_t has size change (4,m)->(5,m-1) and potential change 10-2m, neutral at m=5 and strict for m>=6; any repartition produced from a good deletion d in a non-Hamiltonian F_t preserves the size pair {4,m} and is neutral.

Fix t in X and write F=F_t, L=L_t. The sets F and L are disjoint and partition V(X) union V(P), with |F|=5 and |L|=m-1. If F is Hamiltonian and L is Hamiltonian, F|L is a legal pairwise repartition of X|P; its potential change is 25+(m-1)^2-(16+m^2)=10-2m<=0 for m>=5. Therefore, if no nonincreasing repartition exists, Hamiltonicity of F forces L to be non-Hamiltonian, and minimum-counterexample calculus gives pc(L)=2. Now suppose F is non-Hamiltonian. The five-vertex small-set theorem gives a set D of at least four labels d in F for which F-{d} is Hamiltonian. For each such d, the complementary support in X union P is L+d, of order m. If any L+d were Hamiltonian, (F-{d})|(L+d) would be a legal pairwise repartition of X|P preserving the component sizes {4,m}, hence preserving Phi. Therefore absence of a nonincreasing repartition forces every L+d to be non-Hamiltonian; minimum-counterexample calculus gives pc(L+d)=2. This argument is independent of t, so it holds simultaneously for all four choices t in X.



### A three-side singleton lift reaches a positioned five-support by two nonincreasing pairwise repartitions

**Statement.** Let C=P|(x)|Q be a spanning three-cover of a boundary tournament, with |P|=3 and Q=(q_0,...,q_{m-1}), m>=5. Put X=V(P) union {x}. For every prescribed pair Z={z,zprime} subset X, at least one of F_z={z,q_0,q_1,q_2,q_3}, F_zprime={zprime,q_0,q_1,q_2,q_3}, and F_Z={z,zprime,q_0,q_1,q_2} is Hamiltonian. A Hamiltonian F_z or F_zprime yields a spanning three-cover with component orders (5,3,m-4), whose complement paths have supports X-{z} or X-{zprime}, and {q_4,...,q_{m-1}}. A Hamiltonian F_Z yields a spanning three-cover with orders (5,2,m-3), whose complement paths have supports X-Z and {q_3,...,q_{m-1}}. Thus at most eight vertices near the chosen endpoint are rearranged, and the remaining Q-segment is retained in its displayed order. Relative to C, the quadratic-potential changes are respectively 40-8m and 28-6m. Both are strictly negative for m>=6; at m=5 the first is zero and the second is negative. The analogous result holds at the other endpoint, retaining the displayed prefix of Q. In a minimum-counterexample deletion cover with |P|=3, m>=7, so both branches are strict. The new cover is reachable from C by at most two pairwise repartitions, each nonincreasing in quadratic potential. The first repartitions P|(x) into component orders (1,3) in a one-label branch, or into (2,2) in the two-label branch; the second repartitions the selected singleton or pair with Q, keeping the other short path unchanged. Therefore for m>=6 this is strict descent within the same pairwise-repartition component.

Fix Z={z,zprime}. Let U=Z union {q_0,q_1,q_2,q_3}, a six-set. The three listed five-supports are U-{zprime}, U-{z}, and U-{q_3}. They are distinct. By the four-of-six theorem in smallset01, at most two five-subsets of U are non-Hamiltonian. Hence at least one listed support is Hamiltonian. This does not require X or the four-vertex Q-window to be Hamiltonian, and does not use endpoint constraints or cyclic rotation of tight triples. If F_z is Hamiltonian, choose a Hamilton path on it. The three-set X-{z} has a tight Hamilton path: on any three-set a boundary tournament contains a tight ordering by its reversal-pair axiom. Pair these two paths with the displayed suffix (q_4,...,q_{m-1}), which is nonempty for m>=5. Their supports partition V(C), so they form a spanning three-cover. The F_zprime branch is identical. If F_Z is Hamiltonian, X-Z is a two-set and hence a tight path in either order; pair it with a Hamilton path on F_Z and the displayed suffix (q_3,...,q_{m-1}). Again the supports are disjoint and spanning. These are actual repartitions of the original three-cover, with explicit complementary paths, rather than arbitrary complement covers from minimality. In the first branch only X and the first four vertices of Q change path assignments; in the second only X and the first three change assignments. The original potential is 3^2+1^2+m^2=m^2+10. The two new potentials are 5^2+3^2+(m-4)^2 and 5^2+2^2+(m-3)^2, giving the stated differences. For the other endpoint use U=Z union the last four displayed Q-vertices, and take the third candidate by deleting the earliest of these four. The inherited complement is then the displayed prefix, so no reversal of a tight path is invoked. In a minimum counterexample, mincex01 gives order greater than ten, and n=m+4 implies m>=7. This is a replacement for the proposed endpoint alternating-five-window route in threeside_consecutive_fivewindows01: it gives a positioned five-support and inherited complementary two-cover, while it does not assert that all four two-label five-windows are Hamiltonian. The new cover is reachable by at most two legal pairwise repartitions, with no increase of quadratic potential at either step. In the F_z branch, repartition P|(x), on its four-vertex union X, into (z)|R where R is a Hamilton path on X-{z}. Such a three-vertex Hamilton path always exists. This first step preserves the component orders 1,3 and is neutral; omit it if z=x. Now repartition (z)|Q into a Hamilton path on F_z and the displayed suffix (q_4,...,q_{m-1}), leaving R unchanged. Its potential change is 40-8m. The F_zprime branch is identical. In the F_Z branch, first repartition P|(x) into the two two-vertex paths on Z and X-Z. This decreases potential by 2, since 2^2+2^2-(3^2+1^2)=-2. Next repartition the two-path on Z together with Q into a Hamilton path on F_Z and the displayed suffix (q_3,...,q_{m-1}), leaving the other two-path unchanged. This step changes potential by 30-6m, which is nonpositive for m>=5. The combined change is 28-6m. Thus at m=5 each step is still nonincreasing, and the F_Z route is strict in its first step. For m>=6 either branch yields a strict pairwise-reachable decrease, without changing any long-path vertices beyond the first four. All states remain in the original pairwise-repartition component. The omitted singleton label may change or disappear as a singleton during these legal moves; keeping that label omitted throughout is not asserted. A two-cover is not produced.



### Endpoint-rooted overlap carries the original transport menu plus four simultaneous endpoint probes

**Statement.** Let H be a minimum counterexample and let X|P|Q be a spanning three-cover, where X is a Hamiltonian four-path and P=(p_1,...,p_m) has m>=6. Put M=(p_2,...,p_{m-1}). Suppose distinct x,y,z in X, with t the fourth vertex, satisfy that W={p_1,p_m,x,y} and W'={p_1,p_m,x,z} are Hamiltonian. Then the complete endpoint-overlap transport menu of four_side_endpoint_overlap_transport_recomp01 holds: strict quadratic descent, or a neutral same-order replacement by a Hamiltonian four-subset of F={p_1,p_m,x,y,z}, or F Hamiltonian with L=M+{t} non-Hamiltonian pc2, or F non-Hamiltonian with at least four good deletions d for which L+d is non-Hamiltonian pc2. In addition, independently of which of those alternatives occurs, either some legal pairwise repartition of X|P has nonincreasing quadratic potential, or for every s in X the endpoint-pair probe F_s=(X-{s}) union {p_1,p_m}, L_s=M union {s} satisfies: if F_s is Hamiltonian then L_s is non-Hamiltonian pc2, while if F_s is non-Hamiltonian then at least four labels d in F_s have F_s-{d} Hamiltonian and L_s+d non-Hamiltonian pc2. Thus the overlap witness is only one distinguished member of a four-probe family.

The first asserted menu is exactly four_side_endpoint_overlap_transport_recomp01. Apply four_side_universal_endpoint_probe01 to the same four-side X and path P. It gives the independent second dichotomy: either a nonincreasing pairwise repartition exists, or the stated pc2 residual/star conclusion holds simultaneously for all four choices s in X. Combining the two conclusions gives the theorem. Since m>=6, every (4,m)->(5,m-1) move among the universal probes is strict; same-size probe moves are neutral. No further assumptions are introduced.



### The unresolved four-side endpoint lock is a four-label second-type gap network

**Statement.** Let H be a minimum counterexample and let X|P|Q be a spanning three-cover with |X|=4 and P=(p_1,...,p_m), m>=5. Put M=(p_2,...,p_{m-1}). Then at least one of the following holds: (1) there is a legal pairwise repartition of X|P with component orders (5,m-1) and quadratic-potential change 10-2m<=0; (2) H contains a proper Hamiltonian induced set of order four or five meeting both X and V(M), with non-Hamiltonian path-cover-two complement; (3) m>=7 and each x in X has a second-type failed-insertion obstruction at a distinct displayed gap g(x) of M. In outcome (3), for every distinct x,y in X, if |g(x)-g(y)|=1 then the explicit adjacent-gap cross triple supplied by 36fccff06d48 is tight, while if |g(x)-g(y)|>=2 then x and y are joined by the tight interval path through the displayed subinterval of M between their obstruction gaps. Thus the sole unresolved branch is a complete four-label gap network, not a single connector.

Apply four_side_endpoint_lock_mixed_menu_m5_01. If its first or second outcome occurs we are done. Otherwise every vertex of X is noninsertable into the displayed interior path M, and assume no mixed Hamiltonian four/five-support exists. Apply insert01 to each x in X. A first-type obstruction would, by 0425e03e2aa3 exactly as in the predecessor proof, give either a mixed Hamiltonian four-set or a cyclic non-Hamiltonian four-set whose extension by another X-label is a mixed Hamiltonian five-set. Hence every x has a second-type obstruction at some displayed gap g(x). If two labels x,y had the same gap, the equal-gap case of 36fccff06d48 would give a mixed Hamiltonian four-set, contradiction. Thus the four gaps are distinct, so M has at least five vertices and m=|M|+2>=7. Now fix x!=y. If their gaps differ by at least two, the separated-gap case of 36fccff06d48 gives the stated tight interval connector. If their gaps are adjacent, that theorem gives either a mixed Hamiltonian five-set on x,y and three consecutive vertices of M, contradicting the absence of outcome (2), or its explicit adjacent-gap cross triple. Therefore the cross triple must occur. This proves the complete pairwise network.



### Short gaps force reversed endpoint triples without a minimum-counterexample hypothesis

**Statement.** Let B=(b_1,...,b_r) be a tight path in a boundary tournament H, and let L be a set of exterior vertices. Assign each x in L a distinct second-type obstruction gap g(x) in {1,...,r-1}. Assume that for adjacent assigned gaps i=g(u), i+1=g(w), the triple (u,b_{i+1},w) is tight. If no Hamiltonian four- or five-support meets both L and V(B), then for any distinct u,v,w in L with 0<g(w)-g(u)<=2, (w,v,u) is tight. Equivalently, every tight triple (u,v,w) on L with g(u)<g(w) has g(w)-g(u)>=3. In particular, for any displayed tight four-path (x_0,x_1,x_2,x_3) on L, each of g(x_2)-g(x_0) and g(x_3)-g(x_1) is either negative or at least three. If its label gaps are increasing, its second-neighbor gaps are at least three, its total span is at least four, and r>=6. These conclusions do not require a cycle claim, an endpoint-extension hypothesis, a cover, or global quadratic minimality.

Fix distinct u,v,w in L and let i=g(u)<g(w)=j. Suppose (u,v,w) is tight. If j=i+1, the assumed adjacent-gap cross triple gives the second tight path (u,b_{i+1},w). The parallel-middle four-path lemma in localextend01 therefore makes {u,v,w,b_{i+1}} Hamiltonian, contradicting the mixed-support exclusion. If j=i+2, the separated-gap case of 36fccff06d48 gives (u,b_{i+1},b_{i+2},w) tight. This four-vertex path and (u,v,w) are internally disjoint corridors with the same ordered endpoints. By 53d257fcf0a8 their five-vertex union is Hamiltonian, again a contradiction. Boundary antisymmetry now forces (w,v,u) whenever j-i is one or two. Apply this to the two consecutive triples of a displayed four-path for the stated inequalities. If its gaps increase, g(x_2)-g(x_0)>=3 and g(x_3)-g(x_1)>=3. Distinct integer gaps then give g(x_3)-g(x_0)>=4. Since assigned indices lie in {1,...,r-1}, r-2>=4 and r>=6. This is a direct local statement on arbitrary H. The second-type gap network in four_side_endpoint_lock_gap_network01 provides its assumptions in its unresolved branch. No step concatenates paths around a cycle or assumes the gap order agrees with a preexisting path order.



### A four-side beside a path of order at least six strictly descends or creates an adjacent opposite-end four-window fork

**Statement.** Let H be a boundary tournament, let X be a Hamiltonian four-vertex set, and let P=(p_1,...,p_m) be a vertex-disjoint tight path of order m>=6. Then either X|P admits a legal two-path repartition of V(X) union V(P) with strictly smaller quadratic contribution than 4^2+m^2, or there are distinct x,y,z in X such that {p_1,p_m,x,y} and {p_1,p_m,x,z} are both Hamiltonian four-sets. Thus the non-descent branch is a positioned adjacent fork of Hamiltonian four-windows sharing the three-core {p_1,p_m,x}; no neutral or generic-order-disagreement outcome is needed. If H is a minimum counterexample, each of the two forked four-sets has non-Hamiltonian path-cover-two complement.

If X union {p_1} is Hamiltonian, move p_1 from P into X and retain the inherited path (p_2,...,p_m). This changes the pair orders from (4,m) to (5,m-1), with new quadratic contribution minus old equal to 25+(m-1)^2-(16+m^2)=10-2m<0 for m>=6. The same argument applies if X union {p_m} is Hamiltonian. Hence assume both five-sets X union {p_1} and X union {p_m} are non-Hamiltonian. Apply two_bad_five_extensions_adjacent_four01 to the Hamiltonian four-set X and exterior vertices p_1,p_m. It yields distinct x,y,z in X such that {p_1,p_m,x,y} and {p_1,p_m,x,z} are Hamiltonian. They share exactly the three vertices {p_1,p_m,x}. This proves the dichotomy. In a minimum counterexample the forked four-sets are proper; their complements cannot be Hamiltonian, else either one together with its Hamilton path would two-cover H, while minimality gives path-cover number at most two. Therefore each complement is non-Hamiltonian of path-cover number exactly two.



### A five-side no-swap branch forces a two-sided endpoint lock on one long path

**Statement.** Let X|P|Q be a quadratic-potential-minimal trapped three-cover with |X|=5 and |P|,|Q|>=7. Then either an equal-potential support exchange exists as in astra003fiveswapobstruct, or there are x in V(X) and one of the two long paths R=(r_1,...,r_m) such that x cannot be inserted into any position of the displayed order of R. More strongly, writing e_i={r_i,r_{i+1}} and f_i={x,r_i} in the comparison digraph, the four endpoint constraints e_1->f_1, e_2->f_2, f_{m-1}->e_{m-2}, and f_m->e_{m-1} all hold. Hence insert01 supplies a bounded failed-insertion obstruction for x on the full displayed path R.


By astra003fivethreeendpoints, choose x in V(X), with D=V(X)-{x}, such that D union {e} is Hamiltonian for at least three of the four endpoints of P and Q. Apply astra003fiveswapobstruct to these synchronized endpoints.

If any corresponding support exchange exists, we are in the first alternative. Suppose therefore that none exists. Among at least three endpoints drawn from the two endpoint pairs of P and Q, two belong to the same path. Call that path
R=(r_1,...,r_m), m>=7.
Thus D union {r_1} and D union {r_m} are Hamiltonian, while both
(R-r_1) union {x}
and
(R-r_m) union {x}
are non-Hamiltonian; otherwise the corresponding same-size support exchange would exist.

Let
L=(r_2,...,r_m),  R'=(r_1,...,r_{m-1})
be the inherited endpoint truncations. Since H[V(L) union {x}] and H[V(R') union {x}] are non-Hamiltonian, inserting x into every position of either displayed truncation fails.

We claim that inserting x into every position of the full displayed order R also fails.

- Insertion before r_1 is already the left-end insertion into R', hence fails.
- Insertion after r_m is already the right-end insertion into L, hence fails.
- Insertion between r_1 and r_2 requires, among its tight triples, the left-end triple needed to insert x before r_2 in L. That truncated insertion fails, so the full insertion fails.
- Insertion between r_{m-1} and r_m requires, among its tight triples, the terminal triple needed to insert x after r_{m-1} in R'. That truncated insertion fails, so the full insertion fails.
- Every insertion between r_i and r_{i+1} for 2<=i<=m-2 is an insertion position internal to both endpoint truncations, so it fails there and therefore in R.

Hence x is noninsertable in the full displayed path R.

The failed endpoint insertions also give explicit comparison arcs. Put
e_i={r_i,r_{i+1}}, 1<=i<=m-1,
and f_i={x,r_i}, 1<=i<=m.
Failure of the left-end insertion into R' gives e_1->f_1, and failure of the right-end insertion into R' gives f_{m-1}->e_{m-2}. Failure of the left-end insertion into L gives e_2->f_2, and failure of the right-end insertion into L gives f_m->e_{m-1}. Thus all four stated endpoint constraints hold simultaneously.

Finally, applying the failed-insertion theorem of insert01 to the full path R gives a bounded obstruction involving x and at most four consecutive vertices of R. The point is that this obstruction now sits inside a path carrying simultaneous two-sided endpoint constraints forced by one common five-side displacement.




### Inner facing four-windows have local two-move potential formulas

**Statement.** Let H be a boundary tournament, let P=(p_0,...,p_{p-1}) and Q=(q_0,...,q_{q-1}) be vertex-disjoint tight paths with p,q>=3, and let x lie outside both. Regard P|Q|{x} as a three-path cover of its union. If W_L={p_0,q_{q-1},x,p_1} is Hamiltonian, then two pairwise repartitions of this local cover produce W_L | (p_2,...,p_{p-1}) | (q_0,...,q_{q-2}), with quadratic-potential change 20-4p-2q. If W_R={p_0,q_{q-1},x,q_{q-2}} is Hamiltonian, two pairwise repartitions produce the symmetric local cover of component orders 4,p-1,q-2, with change 20-2p-4q.

For W_L, first repartition Q|{x} into the inherited path (q_0,...,q_{q-2}) and the two-vertex path (q_{q-1},x). Then repartition P together with that two-vertex path into the Hamiltonian four-set W_L and the inherited tail (p_2,...,p_{p-1}). Every vertex of V(P) union V(Q) union {x} appears exactly once, so both moves are legal pairwise repartitions of the local three-path cover. The component orders change from p,q,1 to 4,p-2,q-1, and the potential change is 16+(p-2)^2+(q-1)^2-(p^2+q^2+1)=20-4p-2q. The W_R case is symmetric: first split P|{x} as (p_1,...,p_{p-1}) | (p_0,x), then combine (p_0,x) with Q using W_R, leaving (q_0,...,q_{q-3}); the component orders are 4,p-1,q-2 and the change is 20-2p-4q. No ambient spanning hypothesis is used.



### Three noninsertable vertices on one path yield a four-vertex configuration or an interval path

**Statement.** Let B=(b_1,...,b_m) be a tight path in a boundary tournament, and let x,y,z be three distinct vertices outside B, each noninsertable into every position of the displayed order B. Then at least one of the following holds: (1) for one label w in {x,y,z}, a first-type failed-insertion window on w is either a Hamiltonian four-set or the cyclic non-Hamiltonian four-vertex configuration from smallset01, whose every one-vertex extension is Hamiltonian; (2) two labels have second-type obstructions at the same displayed gap, and together with that gap edge form a Hamiltonian four-set; (3) two labels have second-type obstruction gaps separated by at least one intervening gap, and are joined by a tight connector through the displayed interval between those gaps. In particular three noninsertable labels cannot produce only adjacent-gap cross residues.

Apply the failed-insertion normal form insert01 separately to x,y,z. If any label has alternative 1, apply 0425e03e2aa3 to its local four-vertex window. This gives outcome (1).

Assume therefore that all three labels have alternative 2. Let their obstruction gaps have indices i,j,k and sort them so i<=j<=k. If two indices coincide, the same-gap case of 36fccff06d48 gives a Hamiltonian four-set consisting of the two corresponding exterior labels and the two vertices of that displayed gap, yielding outcome (2). If all three indices are distinct, then i<j<k and k>=i+2. The separated-gap case of 36fccff06d48 applied to the labels at gaps i and k gives the tight connector from the first label through b_{i+1},...,b_k to the second, yielding outcome (3). These alternatives exhaust the failed-insertion normal forms.



### Three second-type insertion obstructions yield a Hamiltonian four-set or an interval path

**Statement.** Let B=(b_1,...,b_m) be a tight path in a boundary tournament, and let x,y,z be three distinct exterior vertices. Suppose alternative 2 of the failed-insertion normal form in insert01 holds for x,y,z at gaps b_i|b_{i+1}, b_j|b_{j+1}, b_k|b_{k+1}, respectively. Then either two of i,j,k are equal, in which case the corresponding two exterior labels together with that displayed edge form a Hamiltonian four-set, or two of the obstruction gaps differ by at least two, say r<s with s>=r+2, in which case the corresponding exterior labels are joined by a tight connector through the displayed interval (u,b_{r+1},...,b_s,v). Thus three second-type locks cannot all remain in the adjacent-gap cross-only residue.

Relabel x,y,z so that i<=j<=k. If two of i,j,k are equal, apply the same-gap case of 36fccff06d48 to those two labels. It gives a Hamiltonian four-set on the two labels and the two vertices of the common displayed gap.

Assume now that i,j,k are pairwise distinct. Then i<j<k, hence k>=i+2. Apply the separated-gap case of 36fccff06d48 to the labels at gaps i and k. It gives the tight connector consisting of the first exterior label, the displayed interval b_{i+1},...,b_k, and the second exterior label. These two cases are exhaustive. In particular the adjacent-gap cross alternative of the two-label spacing trichotomy cannot be the only structure across all three labels.



### A quadratic-minimal 4|5|m cover has a cyclic exchange or one of three insertion-obstruction outcomes

**Statement.** Let H be a boundary tournament and let C=X|Y|P minimize quadratic potential within its connected pairwise-repartition component, with |X|=4, |Y|=5, and P=(p_1,...,p_m) of order m>=7. Then at least one of the following holds. (1) C has a nontrivial equal-Phi cyclic support exchange of profile 4|5|m. (2) Some y in Y has a first-type failed-insertion window on P, whose associated four-set is either Hamiltonian or the cyclic non-Hamiltonian four-vertex configuration from smallset01, whose every one-vertex extension is Hamiltonian. (3) Two distinct labels y,z in Y have second-type obstruction at the same gap of P, and {y,z} together with that displayed gap edge is Hamiltonian. (4) Two distinct labels y,z in Y are joined by a tight connector (y,p_{r+1},...,p_s,z) through an interval of P with s>=r+2. Thus, once neutral cyclic exchange is excluded, the 4|5|m potential-minimizing cover reduces to a four-vertex configuration or a direct connector between two vertices of the five-side through the long path.

Apply local45_exchange_or_triplelock01. If its neutral cyclic-exchange alternative occurs, we have (1). Otherwise choose three distinct labels y_1,y_2,y_3 in Y that are noninsertable into every position of P.

Apply the failed-insertion normal form insert01 separately to these three labels. If some label has alternative 1, 0425e03e2aa3 gives exactly outcome (2).

Assume all three have alternative 2, at gap indices i,j,k. Sort the indices. If two are equal, the same-gap case of 36fccff06d48 yields outcome (3). If they are pairwise distinct, the smallest and largest differ by at least two, and the separated-gap case of 36fccff06d48 yields outcome (4). These cases exhaust the three locked labels.



### Componentwise four-side fork interior lock

**Statement.** Let H be a boundary tournament and W|P|Q a spanning three-cover minimizing quadratic potential in its connected pairwise-repartition component. Write W=D union {w}, |W|=4. Let Q=(f,q_1,...,q_{q-2},g) have order q>=5. If D union {f} and D union {g} are non-Hamiltonian, put M=(q_1,...,q_{q-2}). Then D union {f,g} is Hamiltonian. For q>=6, M union {w} is non-Hamiltonian, so w is noninsertable into the inherited path M. For q=5, either the same lock holds or W|Q has a legal Phi-neutral repartition of orders 5 and 4.

By the two-bad-four-extension lemma in localextend01, F=D union {f,g} is Hamiltonian. If M union {w} is Hamiltonian, then F and M union {w} partition V(W) union V(Q), so replacing W|Q by those two Hamiltonian paths is one legal pairwise repartition in the same connected component. The potential change is 5^2+(q-1)^2-(4^2+q^2)=10-2q. For q>=6 this is negative, contradicting componentwise minimality. Hence M union {w} is non-Hamiltonian, and any insertion of w into M would contradict that. For q=5 the same repartition has zero potential change, giving the stated neutral alternative. No global minimality hypothesis is used.



### Mutual deletion internality forces four endpoint windows or doubled reverse constraints

**Statement.** Let H be a minimum counterexample and let d,t be distinct vertices such that d is internal in every two-cover of H-t and t is internal in every two-cover of H-d. Let H-{d,t}=P|Q be any displayed two-cover, with P=(p_0,...,p_m) and Q=(q_0,...,q_s). Then |P|,|Q|>=3. At each of the four displayed ends, one has a Hamiltonian four-window with non-Hamiltonian path-cover-two complement or a doubled reverse constraint. More precisely: at the initial end of P, either {p_1,p_0,d,t} is Hamiltonian, or both (t,d,p_0) and (d,t,p_0) are tight; at the terminal end of P, either {d,t,p_m,p_{m-1}} is Hamiltonian, or both (p_m,t,d) and (p_m,d,t) are tight. The analogous two alternatives hold at the initial and terminal ends of Q.

Apply square_permanent_internal_hooks01 first to G=H-t with universally internal vertex d and the lower two-cover G-d=H-{d,t}=P|Q. It gives |P|,|Q|>=3 and the endpoint hooks (p_1,p_0,d), (d,p_m,p_{m-1}), (q_1,q_0,d), and (d,q_s,q_{s-1}). Apply the same theorem to G'=H-d with universally internal vertex t and the same lower cover G'-t=P|Q. This gives the parallel hooks (p_1,p_0,t), (t,p_m,p_{m-1}), (q_1,q_0,t), and (t,q_s,q_{s-1}).

Consider the initial end of P. If (p_0,d,t) is tight, then (p_1,p_0,d,t) is a tight Hamiltonian four-path, using the hook (p_1,p_0,d). If (p_0,t,d) is tight, then (p_1,p_0,t,d) is a tight Hamiltonian four-path. If neither is tight, boundary antisymmetry forces both reversals (t,d,p_0) and (d,t,p_0) to be tight. This proves the initial-end dichotomy.

At the terminal end, if (d,t,p_m) is tight then (d,t,p_m,p_{m-1}) is a tight Hamiltonian four-path using (t,p_m,p_{m-1}); if (t,d,p_m) is tight then (t,d,p_m,p_{m-1}) is tight using (d,p_m,p_{m-1}). If neither is tight, boundary antisymmetry gives both (p_m,t,d) and (p_m,d,t). The two Q-end statements are identical.

Whenever one of these four-sets is Hamiltonian, it is proper. Its complement cannot be Hamiltonian, since complementary Hamilton paths would two-cover H; minimum-counterexample calculus therefore gives path-cover number two.



### A non-Hamiltonian five-set has either a complete pc2 punctured cube or one Hamiltonian singleton exception

**Statement.** Let H be a minimum counterexample and let F be a non-Hamiltonian five-vertex set. Put K=H-F. Then exactly one of the following holds. (1) For every nonempty proper subset S of F, K union S is non-Hamiltonian with path-cover number two. (2) There is a unique vertex d0 in F such that F-{d0} is non-Hamiltonian and K union {d0} is Hamiltonian; for every other nonempty proper subset S of F, K union S is non-Hamiltonian with path-cover number two. In outcome (2), the proper Hamiltonian set K union {d0} has the non-Hamiltonian four-set F-{d0} as its complement, so the full codimension-four Hamiltonian-side structure theorem codim4_01 applies to this exceptional state. Thus the 30 nonempty proper extension states of K form either a complete pc2 punctured five-cube, or a pc2 punctured cube with one uniquely identified Hamiltonian singleton exception carrying the complete codimension-four complement structure.

By nonham_five_punctured_pc2_cube02, every extension K union S with 2<=|S|<=4 is non-Hamiltonian with path-cover number two, and at least four singleton extensions K+d are non-Hamiltonian with path-cover number two. The five-vertex small-set theorem gives at most one label d0 for which F-{d0} is non-Hamiltonian. If there is no such label, all five singleton extensions are pc2 and (1) holds.

Otherwise d0 is unique. The proper induced subtournament K+{d0} has path-cover number at most two by minimum-counterexample minimality. If it is non-Hamiltonian, it has path-cover number exactly two, so again all 30 nonempty proper extension states are pc2 and (1) holds. If it is Hamiltonian, then it is the unique singleton state not pc2, while all other 29 states are pc2 by the punctured-cube theorem, giving (2). Uniqueness of the exceptional singleton follows from uniqueness of the non-Hamiltonian four-deletion.

In outcome (2), K+{d0} and F-{d0} are complementary proper induced sets, the former Hamiltonian and the latter a non-Hamiltonian four-set. Therefore the hypotheses of codim4_01 hold with Hamiltonian side K+{d0} and four-vertex complement F-{d0}; every certified structural consequence in that codimension-four package is available at the unique exceptional singleton state.



### Four-label gap networks force a mixed four-set, an outer-edge reversal, or a spaced middle configuration

**Statement.** Let H be a minimum counterexample and let X=(x_0,x_1,x_2,x_3) be a Hamiltonian four-path in a spanning three-cover X|P|Q, where P=(p_1,...,p_m), m>=7, and M=(p_2,...,p_{m-1}). Suppose each x_i has a distinct second-type failed-insertion obstruction gap g_i in M and the complete gap-network connectors of four_side_endpoint_lock_gap_network01 are present. Then at least one of the following holds. (1) H contains a proper Hamiltonian four-set meeting both X and V(M), whose complement is non-Hamiltonian with path-cover number two. (2) A tight triple reverses one of the two outer displayed edges x_0x_1 or x_2x_3 of X. (3) For some gap index t, g_2=t, g_1=t+1, g_0<=t-3, and g_3>=t+4; if z is the unique M-vertex in the connector from x_2 to x_1, then both (z,x_2,x_1) and (x_2,x_1,z) are tight. In (3), m>=11. Consequently every hard gap-network configuration on a host path of order at most ten gives (1) or (2).

Write the four assigned obstruction gaps as
\[
g_i=g(x_i),\qquad 0\le i\le3.
\]
The complete gap-network hypothesis gives, for every pair of labels, either the adjacent-gap cross triple or the tight interval connector through the displayed subinterval of \(M\).

We first record the path-intersection consequence. Suppose \(i<j\) and
\[
g_j<g_i.
\]
Let \(C\) be the gap-network connector from \(x_j\) to \(x_i\), and let
\[
A=(x_i,\ldots,x_j)
\]
be the displayed \(X\)-subpath. Their only common vertices are \(x_i,x_j\), and these occur in opposite relative orders. The reversed-common-vertices lemma from the path-intersection calculus therefore gives either a tight triple reversing a boundary edge of \(A\), or a vertex-simple tight cycle on \(V(A)\cup V(C)\).

The cycle alternative yields conclusion (1). Indeed the cycle meets both \(X\) and \(M\). If it has at least four vertices, four consecutive vertices across a junction between its \(X\)-portion and its \(M\)-portion form a mixed Hamiltonian four-set. If it has three vertices, then \(A\) is a single displayed edge of \(X\). The cyclic triples place the unique \(M\)-vertex on both sides of that ordered edge, and one of the two displayed neighbors of the edge in the four-path \(X\) extends one of these triples to a mixed Hamiltonian four-path. In either case the resulting four-set is proper; minimum-counterexample calculus gives a non-Hamiltonian path-cover-two complement.

Thus, unless (1) holds, every inversion \(g_j<g_i\) forces a tight triple reversing one of the two boundary edges of the displayed subpath \(A\).

Assume henceforth that neither (1) nor (2) holds. Then
\[
g_0<g_1
\]
because an inversion of the adjacent pair \(x_0,x_1\) would reverse the outer edge \(x_0x_1\). Similarly
\[
g_2<g_3.
\]
The four gaps cannot occur in increasing order. To see this, suppose
\[
g_0<g_1<g_2<g_3.
\]
The second-type prefix for \(x_1\) contains
\[
(b_{g_1-1},b_{g_1},x_1).
\]
If \((b_{g_1},x_1,x_2)\) were tight, these vertices would contain a mixed Hamiltonian four-path; otherwise boundary reversal gives
\[
(x_2,x_1,b_{g_1})
\]
tight. Symmetrically, using the second-type suffix for \(x_2\), absence of a mixed Hamiltonian four-path gives
\[
(b_{g_2+1},x_2,x_1)
\]
tight. The latter two triples concatenate to a mixed Hamiltonian four-path, a contradiction. Hence
\[
g_1>g_2.
\]

Consider the connector
\[
C=(x_2,c_1,\ldots,c_k,x_1)
\]
supplied by the gap network. We claim that \(k=1\). The two junction triples with the displayed middle edge of \(X\) are
\[
(x_1,x_2,c_1),\qquad (c_k,x_1,x_2).
\]
If \(k\ge2\) and the first junction is tight, then
\[
(x_1,x_2,c_1,c_2)
\]
is a mixed Hamiltonian four-path. If the second junction is tight, then
\[
(c_{k-1},c_k,x_1,x_2)
\]
is such a path. If both junctions are non-tight, boundary reversal gives
\[
(c_1,x_2,x_1),\qquad(x_2,x_1,c_k)
\]
tight, and since \(c_1\ne c_k\),
\[
(c_1,x_2,x_1,c_k)
\]
is a mixed Hamiltonian four-path. All three possibilities contradict the exclusion of (1). Therefore \(k=1\).

Write the unique internal connector vertex as \(z\). If
\[
(x_1,x_2,z)
\]
were tight, then \((x_0,x_1,x_2,z)\) would be a mixed Hamiltonian four-path. Hence
\[
(z,x_2,x_1)
\]
is tight. Similarly, tightness of \((z,x_1,x_2)\) would make
\[
(z,x_1,x_2,x_3)
\]
a mixed Hamiltonian four-path, so
\[
(x_2,x_1,z)
\]
is tight. Thus the middle edge has reverse triples on both sides through the same vertex \(z\).

By the connector dichotomy in the gap-network theorem, a connector with exactly one internal vertex corresponds to adjacent obstruction gaps. Hence, for some integer \(t\),
\[
g_2=t,\qquad g_1=t+1.
\]
Since \(g_0<g_1\), distinctness of the gaps implies \(g_0<g_2\). Since \(g_2<g_3\), distinctness likewise implies \(g_1<g_3\).

Now apply the short-gap reversal theorem to the displayed tight triple
\[
(x_0,x_1,x_2).
\]
Because \(g_0<g_2\), its two endpoint gaps differ by at least three:
\[
g_2-g_0\ge3.
\]
Apply the same theorem to
\[
(x_1,x_2,x_3).
\]
Because \(g_1<g_3\),
\[
g_3-g_1\ge3.
\]
Consequently
\[
g_0\le t-3,qquad
g_2=t,qquad
g_1=t+1,qquad
g_3\ge t+4.
\]
This is conclusion (3).

Finally the displayed gaps of \(M=(p_2,\ldots,p_{m-1})\) are indexed by
\[
1,\ldots,m-3.
\]
Conclusion (3) gives \(g_3-g_0\ge7\), hence \(g_3\ge8\) and therefore
\[
m-3\ge8,
\qquad
m\ge11.
\]
Thus for \(m\le10\), only conclusions (1) and (2) are possible.



### The four-side endpoint package extends through the neutral order-five threshold

**Statement.** Let H be a boundary tournament and X|P|Q a spanning three-cover with |X|=4 and P=(p_1,...,p_m), m>=5. Put a=p_1, b=p_m, and M=(p_2,...,p_{m-1}). Then either there is a legal pairwise repartition of X|P with component orders (5,m-1), whose quadratic-potential change is 10-2m (strictly negative for m>=6 and zero for m=5), or both X union {a} and X union {b} are non-Hamiltonian and, for every t in X, F_t=(X-{t}) union {a,b} is Hamiltonian while L_t=V(M) union {t} is non-Hamiltonian. In the latter case there are distinct x,y,z in X such that {a,b,x,y} and {a,b,x,z} are Hamiltonian and their five-vertex union is Hamiltonian. In a minimum counterexample, every proper Hamiltonian support displayed has non-Hamiltonian path-cover-two complement and every L_t has path-cover number two.

The proof of four_side_four_five_supports_descent01 is unchanged except for keeping the potential difference rather than requiring it to be negative. If X+{a} or X+{b} is Hamiltonian, pair it with the inherited endpoint truncation of P; the component orders change from (4,m) to (5,m-1), with Delta Phi=25+(m-1)^2-16-m^2=10-2m, which is zero at m=5 and negative for m>=6. Otherwise both endpoint five-extensions are non-Hamiltonian. Apply two_bad_five_extensions_all_opposite01 to X,a,b to obtain all four Hamiltonian supports F_t. If some L_t=M+{t} is Hamiltonian, F_t|L_t gives the same legal (5,m-1) repartition and the same potential change. Hence absence of such a nonincreasing move forces all four L_t non-Hamiltonian. Apply two_bad_five_extensions_adjacent_four01 exactly as in the predecessor to obtain the two overlapping Hamiltonian four-sets whose union is one of the already-Hamiltonian F_t. The minimum-counterexample complement statements follow from mincex01.



### Prescribed-pair five-side switches synchronize on a six-vertex transport set

**Statement.** Let H be a minimum counterexample, let X be a proper Hamiltonian five-set with H-X non-Hamiltonian of path-cover number two, fix x in X, and fix distinct p,q outside X. Put S=(X-{x}) union {p,q}. Then either S is Hamiltonian and H-S is non-Hamiltonian with path-cover number two, or S is non-Hamiltonian and has at least four vertices d for which S-{d} is Hamiltonian. In the latter case, writing L=H-S, every such L+d is non-Hamiltonian with path-cover number two; moreover the Hamiltonian two-deletion graph on those good deletion labels has minimum degree at least one, and every edge de gives L+d+e non-Hamiltonian with path-cover number two. In particular, if p,q are prescribed vertices from two complementary paths, the resulting six-set is positioned on both chosen complementary vertices while excluding the prescribed old five-side vertex x.

By five_side_prescribed_pair_switch01 there are at least two distinct d1,d2 in X-{x} such that S-{d1} and S-{d2} are Hamiltonian five-sets. Let K=S-{d1,d2}; then K union {d1}=S-{d2} and K union {d2}=S-{d1} are Hamiltonian. Apply 944fd93bda46 to the common four-core K and labels d1,d2. If S is Hamiltonian, its complement is non-Hamiltonian with path-cover number two by minimum-counterexample calculus. Otherwise 944fd93bda46 gives a Hamiltonian-deletion set D of size at least four containing d1,d2, with every L+d, d in D, non-Hamiltonian of path-cover number two, and a graph J on D of minimum degree at least one whose edge de certifies that L+d+e is non-Hamiltonian of path-cover number two. This is exactly the stated transport set.

### Every four-by-five pair has a nontrivial neutral repartition

**Statement.** Let \(H\) be a boundary tournament, let \(X\) be a Hamiltonian four-set, and let \(P=(a,p_2,p_3,p_4,b)\) be a vertex-disjoint tight path of order five. Then \(H[X\cup V(P)]\) has a two-path cover with component orders \(4\) and \(5\) whose support partition differs from \(X\mid V(P)\). Consequently, whenever \(X\mid P\) occurs as two components of a three-cover, there is a nontrivial pairwise repartition preserving quadratic potential.

Apply the four-side endpoint package at \(m=5\). If its first alternative occurs, it already gives a legal repartition with orders \(5\mid4\), and the potential change is \(10-2m=0\).

Assume therefore that the endpoint-lock alternative occurs. Put
\[
M=\{p_2,p_3,p_4\}.
\]
For every \(t\in X\), the four-set
\[
L_t=M\cup\{t\}
\]
is non-Hamiltonian. The same endpoint package gives distinct \(x,y,z\in X\) such that
\[
A=\{a,b,x,y\},\qquad B=\{a,b,x,z\}
\]
are Hamiltonian. Let \(t\) be the fourth vertex of \(X\), so \(X=\{x,y,z,t\}\).

Consider the five-set complementary to \(A\) inside \(X\cup V(P)\):
\[
C=(X\cup V(P))-A=M\cup\{z,t\}.
\]
Both four-subsets \(M\cup\{z\}=L_z\) and \(M\cup\{t\}=L_t\) are non-Hamiltonian. By the five-set theorem in [[smallset01]], a non-Hamiltonian five-set has at most one non-Hamiltonian four-subset. Therefore \(C\) is Hamiltonian.

Thus \(A\mid C\) is a two-path cover of \(X\cup V(P)\) with orders \(4\mid5\). It is nontrivial because \(A\) contains the two vertices \(a,b\) from the old five-side, so \(A\ne X\). Hence the locked branch also yields a neutral pairwise repartition, and the two alternatives together prove the statement.

### Quadratic-minimal four-four-five and four-five-five states lie on neutral cycles

**Statement.** Let \(H\) be a minimum counterexample and let \(C\) be a spanning three-cover that is \(\Phi\)-minimal in its pairwise-repartition component. If the component-size multiset is \(\{4,4,5\}\) or \(\{4,5,5\}\), then \(C\) has at least two distinct nontrivial equal-\(\Phi\) pairwise-repartition neighbors. Consequently every connected component of the graph of \(\Phi\)-minimal covers of either profile contains a cycle of length at least three.

For profile \(4|4|5\), apply the preceding theorem separately to each four-side together with the unique five-side. This gives one neutral neighbor by repartitioning the first \(4|5\) pair and another by repartitioning the second. The two neighbors are distinct because the first move changes the support partition on one four-component and the five-component while leaving the other four-component fixed, whereas the second move leaves the first four-component fixed and changes the other pair.

For profile \(4|5|5\), apply the theorem separately to the four-side together with each of the two five-sides. Again the resulting neighbors are distinct: one leaves the first five-side fixed and the other leaves the second five-side fixed, while each move nontrivially changes the chosen \(4|5\) support partition.

Every equal-\(\Phi\) neighbor remains \(\Phi\)-minimal in the same repartition component and has the same size multiset. Hence every vertex in the finite graph of \(\Phi\)-minimal covers of either profile has degree at least two. Every finite simple graph of minimum degree at least two contains a cycle, and such a cycle has length at least three.


### All mixed bounded four-support profiles give disagreement or neutral recurrence

**Statement.** Let \(H\) be a minimum counterexample and let \(C\) be a spanning three-cover that is \(\Phi\)-minimal in its pairwise-repartition component. Suppose the component-size multiset is one of
\[
\{4,4,6\},\qquad \{4,5,6\},\qquad \{4,6,6\}.
\]
Then either some displayed \(4|6\) pair has an endpoint-six-set order disagreement, or \(C\) has at least two distinct nontrivial equal-\(\Phi\) pairwise-repartition neighbors. Consequently every connected component of the finite neutral-state graph on any one of these profiles either contains a state with such an order disagreement or contains a cycle of length at least three.

For a displayed \(4|6\) pair, apply **A four-path beside a path of order at least six descends, disagrees, or makes the unique neutral migration**. Its strict-descent outcome is impossible at a \(\Phi\)-minimum. Hence every displayed \(4|6\) pair either has the stated order disagreement or admits the nontrivial neutral migration
\[
4|6\longrightarrow 6|4.
\]

For profile \(4|4|6\), there are two displayed \(4|6\) pairs. If neither carries an order disagreement, neutral migration on either pair gives a neighbor. These two neighbors are distinct because the first move leaves the second four-component fixed while changing the first four-component and the six-component, whereas the second move leaves the first four-component fixed.

For profile \(4|6|6\), pair the unique four-component separately with each six-component. Again, absent an order disagreement, the two neutral migrations give distinct neighbors, one leaving each of the two six-components fixed in turn.

For profile \(4|5|6\), the theorem **Every four-by-five pair has a nontrivial neutral repartition** gives one neutral neighbor by repartitioning the \(4|5\) pair and leaving the six-component fixed. Apply the \(4|6\) theorem to the other pair. If its order-disagreement outcome occurs we are done; otherwise its neutral migration gives a second neighbor, this time leaving the five-component fixed. The two neighbors are distinct.

Every equal-\(\Phi\) neighbor remains \(\Phi\)-minimal and has the same size multiset. Thus, inside any connected component containing no order-disagreement state, every vertex has degree at least two. A finite simple graph of minimum degree at least two contains a cycle of length at least three.

Combining this with the neutral-cycle results for \(4|4|5\) and \(4|5|5\), the sole bounded four-support profile not yet reduced to recurrence or an explicit order disturbance is
\[
4|4|4.
\]


### Every eight-set has at least seven complementary Hamiltonian four-pairs

**Statement.** Let \(H\) be any boundary tournament and let \(U\subseteq V(H)\) have order eight. Among the \(35\) unordered complementary pairs
\[
\{A,U-A\},\qquad |A|=4,
\]
at least seven pairs have both \(A\) and \(U-A\) Hamiltonian. Consequently, if \(A|B\) is any displayed two-path cover of an eight-set with \(|A|=|B|=4\), then the same eight-set has at least six other \(4|4\) two-path covers. Every such replacement is a nontrivial \(\Phi\)-neutral pairwise repartition.

Let \(h\) be the number of Hamiltonian four-subsets of \(U\). By the density conclusion of [[smallset01]], every five-subset contains at least three Hamiltonian four-subsets, and therefore
\[
h\ge \frac35\binom84=42.
\]
Equivalently, this follows by counting incidences \((F,S)\) with \(F\) a Hamiltonian four-set, \(S\) a five-set, and \(F\subset S\): the \(56\) five-sets contribute at least \(3\cdot56=168\) incidences, while each four-set lies in exactly four five-sets.

Partition the \(70\) four-subsets of \(U\) into their \(35\) complementary pairs. Let \(p\) be the number of complementary pairs whose two members are both Hamiltonian, and let \(q\) be the number having exactly one Hamiltonian member. Then
\[
h=2p+q,\qquad p+q\le35.
\]
Hence
\[
h\le 35+p,
\]
so
\[
p\ge h-35\ge7.
\]

If \(A|B\) is already a displayed \(4|4\) cover of \(U\), then \(\{A,B\}\) is one of these complementary Hamiltonian pairs. At least six further complementary Hamiltonian pairs remain. Each supplies a different two-path cover of the same eight vertices with component orders \(4|4\), hence a nontrivial pairwise repartition with exactly the same quadratic contribution.

### Every four-four-four state has neutral degree at least eighteen

**Statement.** Let \(H\) be a boundary tournament and let \(C=A|B|D\) be a spanning three-cover with
\[
|A|=|B|=|D|=4.
\]
Then \(C\) has at least eighteen distinct nontrivial pairwise-repartition neighbors with the same component-size multiset \(4|4|4\) and the same quadratic potential. Consequently every connected component of the finite \(4|4|4\) repartition graph has minimum degree at least eighteen and contains a cycle.

Apply the preceding eight-set theorem first to \(A\cup B\). The displayed decomposition \(A|B\) has at least six alternative complementary Hamiltonian \(4|4\) decompositions. Replacing \(A|B\) by any one of them and leaving \(D\) fixed gives six distinct neutral neighbors.

Repeat on \(A\cup D\), leaving \(B\) fixed, and on \(B\cup D\), leaving \(A\) fixed. Each pair contributes at least six neighbors. The three families are disjoint. Indeed, a nontrivial repartition of \(A\cup B\) leaves \(D\) as a component but leaves neither \(A\) nor \(B\) as a component; similarly for the other two pairs. If a neighbor obtained from two different pair choices were the same cover, it would contain two of the original components, forcing the third component also to be the original remaining four-set and hence giving back \(C\), contrary to nontriviality.

Thus \(C\) has at least \(3\cdot6=18\) distinct neutral neighbors. The same statement holds at every \(4|4|4\) state, so the finite neutral-state graph has minimum degree at least eighteen. In particular it contains abundant neutral recurrence, not merely a single cycle.

Together with the \(4|4|5\), \(4|5|5\), and mixed order-six analyses above, this closes the entire bounded four-support profile list: every profile with component orders in \(\{4,5,6\}\) has forced neutral recurrence unless an explicit \(4|6\) order disagreement is already present.


## Metadata

- ID: line_rooted_small_support_descent_from_deletion_cover_lifts
- Kind: line
- Version: 18
- Math version: 14
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Chunk 1 — crystallized, version 7: Rooted descent through bounded supports
- Chunk 2 — HOT, version 12: From bounded supports to defect compression
