# Toolkit migration — A one-sided tight join across a two-vertex middle forces the adjacent inner reversal

Preserved from the retired Toolkit Limbo object [[toolkit_across_a_two_vertex_middle_forces_the_adjacent_inner_reversal]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 2,
    "created_at": "2026-10-03T04:14:30.964722+00:00",
    "updated_at": "2026-10-03T14:43:12.126335+00:00",
    "archived_at": "2026-10-03T14:43:12.126335+00:00",
    "original_id": "toolkit_across_a_two_vertex_middle_forces_the_adjacent_inner_reversal",
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

For a spanning ordering A,u,v,C in a boundary tournament with path-cover number at least three, if the left outer join is tight and the right outer join is non-tight, then (a_r,u,v) must be non-tight, hence (v,u,a_r) is tight. Symmetrically, if the left outer join is non-tight and the right outer join is tight, then (v,u,c_1) must be non-tight, hence (c_1,u,v) is tight.

## Statement

Let H be a boundary tournament with pc(H)>=3. Let A=(a_1,...,a_r) and C=(c_1,...,c_s) be tight paths with r,s>=2, and let u,v be the remaining two vertices. Consider the spanning ordering A,u,v,C. If (a_{r-1},a_r,u) is tight while (v,c_1,c_2) is non-tight, then (a_r,u,v) is non-tight and therefore (v,u,a_r) is tight. If (a_{r-1},a_r,u) is non-tight while (v,c_1,c_2) is tight, then (u,v,c_1) is non-tight and therefore (c_1,v,u) is tight. Consequently, in the mixed case L=R={z} of toolkit_a_two_vertex_middle_path_forces_an_endpoint_reversal_pattern, writing w for the other middle vertex, both (w,z,a_r) and (c_1,z,w) are tight.

## Body

Let pi=A,u,v,C. All defect centers of pi lie among the four consecutive centers at the two joins and the two middle positions. Number these local centers 1,2,3,4 from left to right. Center 1 corresponds to (a_{r-1},a_r,u), center 2 to (a_r,u,v), center 3 to (u,v,c_1), and center 4 to (v,c_1,c_2).

Suppose center 1 is tight and center 4 is non-tight. If center 2 were also tight, then every defect center of pi would lie among centers 3 and 4. Those are consecutive, so the defect-line matching number would be at most one. By the defect-line identity, pi would split into at most two tight paths, contradicting pc(H)>=3. Therefore center 2 is non-tight. Boundary antisymmetry then gives (v,u,a_r) tight.

The symmetric argument applies when center 1 is non-tight and center 4 is tight. If center 3 were tight, all defects would lie among centers 1 and 2, again giving defect-line matching number at most one. Hence center 3 is non-tight, and boundary antisymmetry gives (c_1,v,u) tight.

Now apply this to the mixed alternative L=R={z} from toolkit_a_two_vertex_middle_path_forces_an_endpoint_reversal_pattern. Let w be the other middle vertex. In the ordering A,z,w,C, the left outer join is tight and the right outer join is non-tight, so (w,z,a_r) is tight. In the ordering A,w,z,C, the left outer join is non-tight and the right outer join is tight, so (c_1,z,w) is tight.

Thus the mixed endpoint-attachment pattern is not merely an attachment/reversal classification: it forces two additional inner reverse triples, one pointing back into A and one pointing back into C.

## Direct premises at migration

[
    {
        "premise_id": "toolkit_a_two_vertex_middle_path_forces_an_endpoint_reversal_pattern",
        "premise_kind": "toolkit",
        "premise_title": "A two-vertex middle path forces an endpoint-reversal pattern",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": true
    }
]

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
