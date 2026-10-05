# Toolkit migration — Endpoint-rooted overlap carries the original transport menu plus four simultaneous endpoint probes

Preserved from the retired Toolkit Limbo object [[endpoint_overlap_allfour_elevated01]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 2,
    "created_at": "2026-09-29T21:54:32.609417+00:00",
    "updated_at": "2026-10-03T15:39:36.649056+00:00",
    "archived_at": "2026-10-03T15:39:36.649056+00:00",
    "original_id": "endpoint_overlap_allfour_elevated01",
    "audit_status": "unaudited",
    "math_version": 1,
    "toolkit_type": "other",
    "refutation_status": "unrefuted",
    "author_session_ids": [
    ],
    "audited_math_version": null
}

## Simplified statement

Endpoint-rooted overlap carries the original transport menu plus four simultaneous endpoint probes.

## Statement

Let H be a minimum counterexample and let X|P|Q be a spanning three-cover, where X is a Hamiltonian four-path and P=(p_1,...,p_m) has m>=6. Put M=(p_2,...,p_{m-1}). Suppose distinct x,y,z in X, with t the fourth vertex, satisfy that W={p_1,p_m,x,y} and W'={p_1,p_m,x,z} are Hamiltonian. Then the complete endpoint-overlap transport menu of four_side_endpoint_overlap_transport_recomp01 holds: strict quadratic descent, or a neutral same-order replacement by a Hamiltonian four-subset of F={p_1,p_m,x,y,z}, or F Hamiltonian with L=M+{t} non-Hamiltonian pc2, or F non-Hamiltonian with at least four good deletions d for which L+d is non-Hamiltonian pc2. In addition, independently of which of those alternatives occurs, either some legal pairwise repartition of X|P has nonincreasing quadratic potential, or for every s in X the endpoint-pair probe F_s=(X-{s}) union {p_1,p_m}, L_s=M union {s} satisfies: if F_s is Hamiltonian then L_s is non-Hamiltonian pc2, while if F_s is non-Hamiltonian then at least four labels d in F_s have F_s-{d} Hamiltonian and L_s+d non-Hamiltonian pc2. Thus the overlap witness is only one distinguished member of a four-probe family.

## Body

The first asserted menu is exactly four_side_endpoint_overlap_transport_recomp01. Apply four_side_universal_endpoint_probe01 to the same four-side X and path P. It gives the independent second dichotomy: either a nonincreasing pairwise repartition exists, or the stated pc2 residual/star conclusion holds simultaneously for all four choices s in X. Combining the two conclusions gives the theorem. Since m>=6, every (4,m)->(5,m-1) move among the universal probes is strict; same-size probe moves are neutral. No further assumptions are introduced.

## Direct premises at migration

[]

## Direct consumers at migration

[]

## Supersession records at migration

[]

## Retained passed-version snapshot at migration

null
