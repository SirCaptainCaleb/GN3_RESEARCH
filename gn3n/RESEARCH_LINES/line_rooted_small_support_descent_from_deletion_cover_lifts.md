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

## Metadata

- ID: line_rooted_small_support_descent_from_deletion_cover_lifts
- Kind: line
- Version: 12
- Math version: 8
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Chunk 1 — crystallized, version 7: Rooted descent through bounded supports
- Chunk 2 — HOT, version 6: From bounded supports to defect compression
