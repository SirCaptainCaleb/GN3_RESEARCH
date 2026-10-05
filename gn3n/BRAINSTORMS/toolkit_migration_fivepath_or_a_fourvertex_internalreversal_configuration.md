# Toolkit migration — A longest path has a bi-endpoint five-path or a four-vertex internal-reversal configuration

Preserved from the retired Toolkit Limbo object [[fivepath_or_a_fourvertex_internalreversal_configuration]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 2,
    "created_at": "2026-09-28T21:58:37.023398+00:00",
    "updated_at": "2026-10-03T15:39:36.649056+00:00",
    "archived_at": "2026-10-03T15:39:36.649056+00:00",
    "original_id": "fivepath_or_a_fourvertex_internalreversal_configuration",
    "audit_status": "unaudited",
    "math_version": 1,
    "toolkit_type": "other",
    "refutation_status": "unrefuted",
    "author_session_ids": [
    ],
    "audited_math_version": null
}

## Simplified statement

A longest path has a bi-endpoint five-path or a four-vertex internal-reversal configuration.

## Statement

Let H be a minimum counterexample and let A=(a_0,...,a_{lambda-1}) be any globally longest tight path. Then at least one of the following holds.

(1) There is y outside A such that
(a_1,a_0,y,a_{lambda-1},a_{lambda-2})
is a tight five-vertex path.

(2) There are distinct exterior vertices w,y,z such that
(w,a_{lambda-1},y,a_0)
is a tight four-vertex path and
(y,a_{lambda-1},z)
reverses its internal displayed edge a_{lambda-1}y. Consequently the four-set {w,a_{lambda-1},y,z} is one of the three certified internal-reversal four-vertex configurations of 53005a4e0315: Hamiltonian, exceptional cyclic non-Hamiltonian, or matching-block non-Hamiltonian.

Thus if no five-path in (1) exists, the exterior vertices force an internal displayed-edge reversal on a four-vertex path, and 53005a4e0315 classifies the resulting four-set.

## Body

Put L=a_0, R=a_{lambda-1}, and U=V(H)-V(A). By minimum-counterexample calculus, |U|>=4. The certified longest-path theorem bcfa72bc175f gives, for every y in U,
(a_1,L,y) and (y,R,a_{lambda-2})
tight.

If (L,y,R) is tight for some y, then the three consecutive triples of
(a_1,L,y,R,a_{lambda-2})
are exactly
(a_1,L,y), (L,y,R), (y,R,a_{lambda-2}),
so outcome (1) holds.

Assume therefore that (L,y,R) is non-tight for every y in U. Boundary antisymmetry then gives
(R,y,L)
tight for every y in U.

Define an ordinary tournament T on U by
p -> q  iff  (p,R,q) is tight.
For each distinct p,q exactly one of (p,R,q),(q,R,p) is tight, so T is indeed a tournament.

Since |U|>=4, T contains a vertex y having both an in-neighbor w and an out-neighbor z. Otherwise every vertex would have indegree zero or outdegree zero; a tournament has at most one source and at most one sink, forcing |U|<=2.

Thus
(w,R,y) and (y,R,z)
are tight. The preceding universal relation also gives (R,y,L) tight. Hence
(w,R,y,L)
is a tight four-path, and the tight triple
(y,R,z)
reverses its internal edge R y.

Apply the certified internal reversed-edge theorem 53005a4e0315. It gives precisely outcome (2).

No cyclic rotation and no path reversal is used.

## Direct premises at migration

[]

## Direct consumers at migration

[]

## Supersession records at migration

[]

## Retained passed-version snapshot at migration

null
