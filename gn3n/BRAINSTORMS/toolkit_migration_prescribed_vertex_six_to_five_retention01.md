# Toolkit migration — A Hamiltonian six-support reduces to a five-support retaining any prescribed vertex

Preserved from the retired Toolkit Limbo object [[prescribed_vertex_six_to_five_retention01]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 2,
    "created_at": "2026-10-03T05:01:11.235053+00:00",
    "updated_at": "2026-10-03T14:43:12.126335+00:00",
    "archived_at": "2026-10-03T14:43:12.126335+00:00",
    "original_id": "prescribed_vertex_six_to_five_retention01",
    "audit_status": "unaudited",
    "math_version": 1,
    "toolkit_type": "other",
    "refutation_status": "unrefuted",
    "author_session_ids": [
        48
    ],
    "audited_math_version": null
}

## Simplified statement

A proper Hamiltonian six-set with two-coverable complement can be reduced to a Hamiltonian five-set retaining any prescribed vertex, while its new complement remains non-Hamiltonian of path-cover number two.

## Statement

Let H be a minimum counterexample, let U be a proper Hamiltonian six-vertex set, and suppose K=H-U is non-Hamiltonian with path-cover number two. For every prescribed vertex a in U, there exists d in U-{a} such that U-{d} is Hamiltonian, contains a, and H-(U-{d})=K+d is non-Hamiltonian with path-cover number two.

## Body

Fix a Hamilton path on U. At least one endpoint differs from the prescribed vertex a; call it d. Deleting d leaves an inherited Hamilton path on U-{d}. By [[ham6goodsquare01]], adjoining either Hamilton-path endpoint to K gives a non-Hamiltonian induced subtournament of path-cover number two. Thus K+d has path-cover number two and U-{d} retains a.

## Direct premises at migration

[
    {
        "premise_id": "ham6goodsquare01",
        "premise_kind": "toolkit",
        "premise_title": "Every Hamiltonian six-set with two-coverable complement contains a full two-label square",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": false
    }
]

## Direct consumers at migration

[]

## Supersession records at migration

[]

## Retained passed-version snapshot at migration

null
