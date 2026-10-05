# Toolkit migration — A hard four-side lock against a seven-path uses the four interior gaps in reverse order

Preserved from the retired Toolkit Limbo object [[four_side_gap_order7_reverse01]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 4,
    "created_at": "2026-09-29T22:16:17.739731+00:00",
    "updated_at": "2026-10-03T15:39:36.649056+00:00",
    "archived_at": "2026-10-03T15:39:36.649056+00:00",
    "original_id": "four_side_gap_order7_reverse01",
    "audit_status": "unaudited",
    "math_version": 1,
    "toolkit_type": "other",
    "refutation_status": "unrefuted",
    "author_session_ids": [
    ],
    "audited_math_version": null
}

## Simplified statement

A hard four-side lock against a seven-path uses the four interior gaps in reverse order.

## Statement

Assume outcome (3) of four_side_endpoint_lock_gap_network01 with X=(x_0,x_1,x_2,x_3) and a host path P of order seven, so its interior M=(b_1,...,b_5) has exactly four displayed gaps. Let g_i be the second-type obstruction gap of x_i in M. Then (g_0,g_1,g_2,g_3)=(4,3,2,1). Thus the four-side order and the obstruction-gap order are reverses.

## Body

The hard gap-network outcome assigns the four vertices x_i to four distinct gaps of M, hence {g_0,g_1,g_2,g_3}={1,2,3,4}. First note that whenever g_i>g_{i+1}, the drop is exactly one. Indeed this adjacent X-pair is an inversion, so four_side_gap_inversion_double_seam_reversal01 gives both tight triples (b_{g_{i+1}+1},x_{i+1},x_i) and (x_{i+1},x_i,b_{g_i}). If g_i>=g_{i+1}+2, the two b-vertices are distinct and these triples concatenate to the mixed Hamiltonian four-path (b_{g_{i+1}+1},x_{i+1},x_i,b_{g_i}), contradicting the defining absence of mixed Hamiltonian four/five-supports in the hard gap branch. Hence g_i=g_{i+1}+1. Next use short_gap_forces_reverse_triples01 on the displayed tight triples (x_0,x_1,x_2) and (x_1,x_2,x_3). If g_2>g_0, then g_2-g_0>=3, so necessarily (g_0,g_2)=(1,4). The remaining values are {2,3}; since g_2=4>g_3 and x_2,x_3 are adjacent, the preceding drop-one rule forces g_3=3 and g_1=2. But then g_3>g_1 with difference one, contradicting short_gap_forces_reverse_triples01 applied to (x_1,x_2,x_3). Therefore g_2<g_0. Symmetrically, if g_3>g_1 then (g_1,g_3)=(1,4); the adjacent inversion g_0>g_1 forces g_0=2 and hence g_2=3, contradicting the short-gap theorem on (x_0,x_1,x_2). Thus g_3<g_1 as well. Now if g_0<g_1, then g_1>g_2 and the distinct intermediate value g_0 lies strictly between them, so g_1-g_2>=2, contradicting the drop-one rule. Hence g_0>g_1 and g_0=g_1+1. If g_1<g_2, then g_0>g_2>g_1, contradicting g_0=g_1+1; hence g_1>g_2 and g_1=g_2+1. Finally g_3<g_1; if g_2<g_3 then g_2<g_3<g_1=g_2+1, impossible. Hence g_2>g_3 and g_2=g_3+1. The four distinct values are therefore 4,3,2,1 in order.

## Direct premises at migration

[]

## Direct consumers at migration

[]

## Supersession records at migration

[
    {
        "new_id": "mixed_two_by_three_hamiltonian_four01",
        "old_id": "four_side_gap_order7_reverse01",
        "reason": "The order-seven gap pattern is a specialization of an impossible hard branch; a mixed Hamiltonian four-set exists before gap-order analysis is needed.",
        "created_at": "2026-10-03T04:05:43.438094+00:00",
        "session_id": 48
    }
]

## Retained passed-version snapshot at migration

null
