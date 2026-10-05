# Toolkit migration — Two bad extensions of a Hamiltonian five-set yield a six-set with four positioned good deletions

Preserved from the retired Toolkit Limbo object [[five_side_two_bad_endpoint_sixpackage01]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 2,
    "created_at": "2026-09-29T20:44:01.323016+00:00",
    "updated_at": "2026-10-03T15:39:36.649056+00:00",
    "archived_at": "2026-10-03T15:39:36.649056+00:00",
    "original_id": "five_side_two_bad_endpoint_sixpackage01",
    "audit_status": "unaudited",
    "math_version": 1,
    "toolkit_type": "other",
    "refutation_status": "unrefuted",
    "author_session_ids": [
    ],
    "audited_math_version": null
}

## Simplified statement

Two bad extensions of a Hamiltonian five-set yield a six-set with four positioned good deletions.

## Statement

Let H be a boundary tournament, let X be a Hamiltonian five-vertex set, and let e,f be distinct vertices outside X. Suppose X union {e} and X union {f} are non-Hamiltonian. Then there exist distinct x,z_1,z_2 in X such that, for U=(X-{x}) union {e,f}, each of U-{e}, U-{f}, U-{z_1}, and U-{z_2} is Hamiltonian. In particular U has four explicitly positioned Hamiltonian one-vertex deletions: both exterior labels e,f and two labels inherited from X.

## Body

Apply 41a89ea9eacf. It gives x in X such that both (X-{x}) union {e} and (X-{x}) union {f} are Hamiltonian, and at least two distinct vertices z_1,z_2 in X-{x} such that (X-{x,z_i}) union {e,f} is Hamiltonian for i=1,2. Put U=(X-{x}) union {e,f}. Then U-{f}=(X-{x}) union {e} and U-{e}=(X-{x}) union {f} are Hamiltonian, while U-{z_i}=(X-{x,z_i}) union {e,f} is Hamiltonian for i=1,2. The four deletion labels e,f,z_1,z_2 are distinct. No minimum-counterexample, path-cover, or extremality hypothesis is used.

## Direct premises at migration

[]

## Direct consumers at migration

[]

## Supersession records at migration

[]

## Retained passed-version snapshot at migration

null
