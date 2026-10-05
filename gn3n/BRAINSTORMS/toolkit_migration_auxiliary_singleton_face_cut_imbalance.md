# Toolkit migration — Auxiliary singleton faces reduce to tournament cut imbalance

Preserved from the retired Toolkit Limbo object [[auxiliary_singleton_face_cut_imbalance]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 1,
    "created_at": "2026-10-04T21:00:32.758506+00:00",
    "updated_at": "2026-10-04T21:00:32.758506+00:00",
    "archived_at": null,
    "original_id": "auxiliary_singleton_face_cut_imbalance",
    "audit_status": "unaudited",
    "math_version": 1,
    "toolkit_type": "lemma",
    "refutation_status": "unrefuted",
    "author_session_ids": [
        141
    ],
    "audited_math_version": null
}

## Simplified statement

In the auxiliary extension, averaging statuses over the face L|{r}|R kills every coordinate except the three windows at r; the outer two are forced +1 and -1, while the middle average is exactly the normalized directed-cut imbalance of L|R in the local tournament at r. For odd |V(H)| some nontrivial L makes the middle average zero.

## Statement

Let H^+ be the auxiliary-vertex extension with distinguished vertex r, let L|R partition V(H) into nonempty sets, and let F=L|{r}|R be the corresponding permutahedron face. Averaging the sign status vector over all chamber orders of F gives zero away from the three status positions adjacent to r. The left outer coordinate is +1, the right outer coordinate is -1, and the middle coordinate equals (|L||R|)^{-1} times the directed cut imbalance of L|R in the tournament T_r defined by u -> w iff (u,r,w) is tight. If |V(H)| is odd, T_r has a nonempty proper balanced cut, so this middle average can be chosen to be zero.

## Body

# Auxiliary singleton faces reduce to tournament cut imbalance

Let `H^+` be the auxiliary extension used for one-change exactification, with distinguished auxiliary vertex `r`. Let `L|R` be a partition of the original vertex set into two nonempty parts and consider the permutahedron face

`F=L|{r}|R`.

Write `ell=|L|`, so `r` occupies position `ell+1` in every chamber order of `F`. By [[permutahedron_face_status_localization]], the average sign status vector over the chambers of `F` can be nonzero only in the three windows beginning at positions `ell-1,ell,ell+1`.

The auxiliary construction forces every triple `(u,v,r)` with original vertices `u,v` to be tight, so the averaged coordinate at `ell-1` is `+1`. It forces every triple `(r,v,w)` with original vertices `v,w` to be non-tight, so the averaged coordinate at `ell+1` is `-1`.

For the middle window, every chamber contributes a triple `(u,r,w)` where `u` is the final vertex of the `L` order and `w` is the first vertex of the `R` order. Under the uniform chamber distribution every pair `(u,w) in L x R` occurs equally often. Define the local tournament `T_r` on the original vertices by

`u ->_{T_r} w` iff `(u,r,w)` is tight,

and let `sigma_r(u,w)=+1` for an arc `u -> w` and `-1` otherwise. Then the middle averaged coordinate is

`(1/(|L||R|)) sum_{u in L,w in R} sigma_r(u,w)`.

The numerator is the directed cut imbalance of `L|R` in `T_r`. If `b(u)=d^+_{T_r}(u)-d^-_{T_r}(u)`, internal arcs cancel and

`sum_{u in L,w in R} sigma_r(u,w)=sum_{u in L} b(u)`.

Thus the entire averaged status geometry of `F` is controlled by one ordinary tournament cut imbalance.

## Odd-order balanced-cut corollary

Assume the original vertex set has odd order `n`. Then every imbalance `b(u)` of the `n`-vertex tournament `T_r` is even. Divide all imbalances by two, obtaining integers `a(u)` with total sum zero and `|a(u)|<=(n-1)/2`.

Suppose no nonempty proper subset has sum zero. Then the full sequence is a minimal zero-sum sequence. For any minimal zero-sum sequence of nonzero integers, if `p` is its largest positive term and `q` the largest absolute value of a negative term, its length is at most `p+q`. Indeed, reorder the terms greedily, always choosing a term of sign opposite to the current partial sum. Every proper partial sum is nonzero and lies between `-(q-1)` and `p` (with the extreme `p` possible only at the first step); minimality makes the proper partial sums distinct, giving the stated bound.

Here `p+q<=n-1`, contradicting the length `n`. Hence some nonempty proper `L` has `sum_{u in L}b(u)=0`. For that cut the face average is

`0,...,0,+1,0,-1,0,...,0`.

This is an averaged directed one-change pattern obtained without any counterexample or minimality hypothesis.

## Direct premises at migration

[
    {
        "premise_id": "boundary_tournaments_as_oriented_transition_systems",
        "premise_kind": "toolkit",
        "premise_title": "Boundary tournaments as oriented transition systems",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": true
    },
    {
        "premise_id": "permutahedron_face_status_localization",
        "premise_kind": "toolkit",
        "premise_title": "Status averages localize at permutahedron face boundaries",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": true
    }
]

## Direct consumers at migration

[]

## Supersession records at migration

[]

## Retained passed-version snapshot at migration

null
