# Toolkit migration — Every ten-vertex boundary tournament has a two-cover

Preserved from the retired Toolkit Limbo object [[ten_vertex_boundary_tournaments_have_two_cover]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 1,
    "created_at": "2026-10-05T01:15:06.026416+00:00",
    "updated_at": "2026-10-05T01:16:05.768513+00:00",
    "archived_at": null,
    "original_id": "ten_vertex_boundary_tournaments_have_two_cover",
    "audit_status": "passed",
    "math_version": 1,
    "toolkit_type": "lemma",
    "refutation_status": "unrefuted",
    "author_session_ids": [
        141
    ],
    "audited_math_version": 1
}

## Simplified statement

Every boundary tournament on ten vertices can be partitioned into two Hamiltonian five-vertex supports.

## Statement

Let H be a boundary tournament on exactly ten vertices. Then pc(H)<=2. In fact, H has two complementary Hamiltonian five-subsets.

## Body

By [[smallset01]], every six-vertex set contains at least four Hamiltonian five-subsets. Let G be the number of Hamiltonian five-subsets of V(H). Count incidences (F,S) with |F|=5, |S|=6, F subset S, and H[F] Hamiltonian. Each of the C(10,6)=210 six-sets contributes at least four incidences, while each Hamiltonian five-set is contained in exactly five six-sets. Hence 5G>=4*C(10,6)=840, so G>=168. The 252 five-subsets of a ten-set split into 126 complementary pairs {F,V-F}. If no complementary pair were both Hamiltonian, at most one member of each pair would be counted, giving G<=126, contradiction. Therefore some complementary five-sets are both Hamiltonian. Choosing Hamilton paths on them gives a spanning two-cover.

## Direct premises at migration

[
    {
        "premise_id": "smallset01",
        "premise_kind": "toolkit",
        "premise_title": "Small-order Hamiltonicity and structure",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": false
    }
]

## Direct consumers at migration

[
    {
        "consumer_id": "every_terminal_local_witness_support_is_two_coverable",
        "consumer_kind": "toolkit",
        "consumer_title": "Every terminal local-witness support is two-coverable",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "consumer_toolkit_limbo": true
    }
]

## Supersession records at migration

[]

## Retained passed-version snapshot at migration

null
