# Toolkit migration — A quadratic-minimal two-vertex middle has a doubled same-side reversal

Preserved from the retired Toolkit Limbo object [[toolkit_minimal_two_vertex_middle_has_a_doubled_same_side_reversal]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 2,
    "created_at": "2026-10-03T04:20:05.802128+00:00",
    "updated_at": "2026-10-03T14:43:12.126335+00:00",
    "archived_at": "2026-10-03T14:43:12.126335+00:00",
    "original_id": "toolkit_minimal_two_vertex_middle_has_a_doubled_same_side_reversal",
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

In a minimum counterexample, if A|(u,v)|C is a spanning three-cover with a two-vertex middle component and is quadratic-potential minimal in its pairwise-repartition component, then both middle vertices reverse the left exposed edge of A or both reverse the right exposed edge of C.

## Statement

Let H be a minimum counterexample and let A|(u,v)|C be a spanning three-cover with |A|,|C|>=2. Assume this cover is Phi-minimal in its pairwise-repartition component. Then either both (u,a_r,a_{r-1}) and (v,a_r,a_{r-1}) are tight, or both (c_2,c_1,u) and (c_2,c_1,v) are tight (or both conclusions hold).

## Body

For the two middle vertices define L={z in {u,v}:(a_{r-1},a_r,z) is tight} and R={z in {u,v}:(z,c_1,c_2) is tight}. The two-vertex middle classification gives three possibilities: L is empty, R is empty, or L=R={z} for one middle vertex z. In the third, mixed case, toolkit_a_mixed_two_vertex_middle_forces_strict_quadratic_descent gives a one-step pairwise repartition with strictly smaller Phi, contradicting Phi-minimality. Hence L is empty or R is empty. If L is empty, boundary antisymmetry gives both reverse triples (u,a_r,a_{r-1}) and (v,a_r,a_{r-1}); if R is empty, it gives both (c_2,c_1,u) and (c_2,c_1,v).

## Direct premises at migration

[
    {
        "premise_id": "toolkit_a_mixed_two_vertex_middle_forces_strict_quadratic_descent",
        "premise_kind": "toolkit",
        "premise_title": "A mixed two-vertex middle forces strict quadratic descent",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": true
    },
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

[]

## Supersession records at migration

[
    {
        "new_id": "toolkit_two_vertex_middle_component_forces_strict_quadratic_descent",
        "old_id": "toolkit_minimal_two_vertex_middle_has_a_doubled_same_side_reversal",
        "reason": "Phi-minimal states cannot contain any two-vertex component at all.",
        "created_at": "2026-10-03T04:26:22.015476+00:00",
        "session_id": 52
    }
]

## Retained passed-version snapshot at migration

null
