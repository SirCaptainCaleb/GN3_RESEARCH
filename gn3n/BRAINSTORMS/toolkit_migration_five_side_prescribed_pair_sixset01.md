# Toolkit migration — Prescribed-pair five-side switches synchronize on a six-vertex transport set

Preserved from the retired Toolkit Limbo object [[five_side_prescribed_pair_sixset01]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 3,
    "created_at": "2026-09-29T21:13:29.250327+00:00",
    "updated_at": "2026-10-03T15:39:36.649056+00:00",
    "archived_at": "2026-10-03T15:39:36.649056+00:00",
    "original_id": "five_side_prescribed_pair_sixset01",
    "audit_status": "unaudited",
    "math_version": 1,
    "toolkit_type": "other",
    "refutation_status": "unrefuted",
    "author_session_ids": [
    ],
    "audited_math_version": null
}

## Simplified statement

Let H be a minimum counterexample, let X be a proper Hamiltonian five-set with H-X non-Hamiltonian of path-cover number two, fix x in X, and fix distinct p,q outside X. Put S=(X-{x}) union {p,q}. Then either S is Hamiltonian and H-S is non-Hamiltonian with path-cover number two, or S is non-Hamiltonian and has at least four vertices d for which S-{d} is Hamiltonian. In the latter case, writing L=H-S, every such L+d is non-Hamiltonian with path-cover number two; moreover the Hamiltonian two-deletion graph on those good deletion labels has minimum degree at least one, and every edge de gives L+d+e non-Hamiltonian with path-cover number two. In particular, if p,q are prescribed vertices from two complementary paths, the resulting six-set is positioned on both chosen complementary vertices while excluding the prescribed old five-side vertex x.

## Statement

Let H be a minimum counterexample, let X be a proper Hamiltonian five-set with H-X non-Hamiltonian of path-cover number two, fix x in X, and fix distinct p,q outside X. Put S=(X-{x}) union {p,q}. Then either S is Hamiltonian and H-S is non-Hamiltonian with path-cover number two, or S is non-Hamiltonian and has at least four vertices d for which S-{d} is Hamiltonian. In the latter case, writing L=H-S, every such L+d is non-Hamiltonian with path-cover number two; moreover the Hamiltonian two-deletion graph on those good deletion labels has minimum degree at least one, and every edge de gives L+d+e non-Hamiltonian with path-cover number two. In particular, if p,q are prescribed vertices from two complementary paths, the resulting six-set is positioned on both chosen complementary vertices while excluding the prescribed old five-side vertex x.

## Body

By five_side_prescribed_pair_switch01 there are at least two distinct d1,d2 in X-{x} such that S-{d1} and S-{d2} are Hamiltonian five-sets. Let K=S-{d1,d2}; then K union {d1}=S-{d2} and K union {d2}=S-{d1} are Hamiltonian. Apply 944fd93bda46 to the common four-core K and labels d1,d2. If S is Hamiltonian, its complement is non-Hamiltonian with path-cover number two by minimum-counterexample calculus. Otherwise 944fd93bda46 gives a Hamiltonian-deletion set D of size at least four containing d1,d2, with every L+d, d in D, non-Hamiltonian of path-cover number two, and a graph J on D of minimum degree at least one whose edge de certifies that L+d+e is non-Hamiltonian of path-cover number two. This is exactly the stated transport set.

## Direct premises at migration

[]

## Direct consumers at migration

[]

## Supersession records at migration

[]

## Retained passed-version snapshot at migration

null
