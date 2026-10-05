# Toolkit migration — A two-vertex middle path forces an endpoint-reversal pattern

Preserved from the retired Toolkit Limbo object [[toolkit_a_two_vertex_middle_path_forces_an_endpoint_reversal_pattern]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 2,
    "created_at": "2026-10-03T04:10:33.074793+00:00",
    "updated_at": "2026-10-03T14:43:12.126335+00:00",
    "archived_at": "2026-10-03T14:43:12.126335+00:00",
    "original_id": "toolkit_a_two_vertex_middle_path_forces_an_endpoint_reversal_pattern",
    "audit_status": "unaudited",
    "math_version": 1,
    "toolkit_type": "other",
    "refutation_status": "unrefuted",
    "author_session_ids": [
        52
    ],
    "audited_math_version": null
}

## Simplified statement

In any spanning three-cover A|(u,v)|C of a boundary tournament with path-cover number at least three, the two middle vertices cannot attach crosswise to the exposed ends of A and C. Consequently either both reverse the same exposed end edge, or one vertex attaches to both sides while the other reverses both exposed end edges.

## Statement

Let H be a boundary tournament with pc(H)>=3. Let A=(a_1,...,a_r), C=(c_1,...,c_s) be tight paths with r,s>=2, and let u,v be distinct vertices outside A union C such that A|(u,v)|C is a spanning three-cover. Put L={z in {u,v} : (a_{r-1},a_r,z) is tight} and R={z in {u,v} : (z,c_1,c_2) is tight}. Then there are no distinct z,w in {u,v} with z in L and w in R. Hence exactly one of the following holds: (i) L is empty, so both (u,a_r,a_{r-1}) and (v,a_r,a_{r-1}) are tight; (ii) R is empty, so both (c_2,c_1,u) and (c_2,c_1,v) are tight; (iii) L=R={z} for some z in {u,v}, and for the other vertex w both (w,a_r,a_{r-1}) and (c_2,c_1,w) are tight.

## Body

Let A=(a_1,...,a_r) and C=(c_1,...,c_s), where r,s>=2, and suppose A|(u,v)|C is a spanning three-cover of a boundary tournament H with pc(H)>=3.

Define L={z in {u,v} : (a_{r-1},a_r,z) is tight} and R={z in {u,v} : (z,c_1,c_2) is tight}.

No two distinct middle vertices can attach to opposite sides. Indeed, if u is in L and v is in R, then (a_1,...,a_r,u) and (v,c_1,...,c_s) are vertex-disjoint tight paths whose supports partition V(H), giving a two-cover, contrary to pc(H)>=3. Hence u in L implies v notin R, and v in L implies u notin R.

If L is empty, boundary antisymmetry gives (u,a_r,a_{r-1}) and (v,a_r,a_{r-1}) tight. If R is empty, boundary antisymmetry gives (c_2,c_1,u) and (c_2,c_1,v) tight.

Assume both L and R are nonempty. Choose z in L and let w be the other vertex. The cross-attachment exclusion forces w notin R, so R={z}. Interchanging left and right gives L={z}. Hence w lies in neither L nor R, and boundary antisymmetry gives both (w,a_r,a_{r-1}) and (c_2,c_1,w) tight.

Thus a two-vertex middle component in a spanning three-cover forces one of three endpoint patterns: two reverse triples through the left exposed edge; two reverse triples through the right exposed edge; or one middle vertex attaches at both exposed ends while its mate reverses both exposed end edges.

## Direct premises at migration

[]

## Direct consumers at migration

[
    {
        "consumer_id": "toolkit_a_mixed_two_vertex_middle_forces_strict_quadratic_descent",
        "consumer_kind": "toolkit",
        "consumer_title": "A mixed two-vertex middle forces strict quadratic descent",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "consumer_toolkit_limbo": true
    },
    {
        "consumer_id": "toolkit_across_a_two_vertex_middle_forces_the_adjacent_inner_reversal",
        "consumer_kind": "toolkit",
        "consumer_title": "A one-sided tight join across a two-vertex middle forces the adjacent inner reversal",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "consumer_toolkit_limbo": true
    },
    {
        "consumer_id": "toolkit_minimal_two_vertex_middle_has_a_doubled_same_side_reversal",
        "consumer_kind": "toolkit",
        "consumer_title": "A quadratic-minimal two-vertex middle has a doubled same-side reversal",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "consumer_toolkit_limbo": true
    },
    {
        "consumer_id": "toolkit_vertex_middle_forces_an_endpoint_rooted_hamiltonian_four_set",
        "consumer_kind": "toolkit",
        "consumer_title": "A mixed two-vertex middle forces an endpoint-rooted Hamiltonian four-set",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 2,
        "consumer_toolkit_limbo": true
    }
]

## Supersession records at migration

[]

## Retained passed-version snapshot at migration

null
