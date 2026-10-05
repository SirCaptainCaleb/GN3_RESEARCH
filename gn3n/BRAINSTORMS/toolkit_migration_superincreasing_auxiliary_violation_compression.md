# Toolkit migration — Superincreasing compression of auxiliary violations

Preserved from the retired Toolkit Limbo object [[superincreasing_auxiliary_violation_compression]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 1,
    "created_at": "2026-10-04T23:30:46.419849+00:00",
    "updated_at": "2026-10-04T23:30:46.419849+00:00",
    "archived_at": null,
    "original_id": "superincreasing_auxiliary_violation_compression",
    "audit_status": "unaudited",
    "math_version": 1,
    "toolkit_type": "lemma",
    "refutation_status": "unrefuted",
    "author_session_ids": [
        139
    ],
    "audited_math_version": null
}

## Simplified statement

Compress all exact auxiliary violations to one odd scalar, freeing enough dimensions to reduce zero carriers to three prescribed macrocomponents.

## Statement

The {-1,0,1}-valued exact auxiliary violation coordinates can be compressed by superincreasing weights to one odd scalar whose chamber zeros are exactly directed one-change orders. Spending the freed dimensions on relative-order gauges for a forest with three components forces a Borsuk-Ulam zero carrier to have at most three ordered macro-blocks.

## Body

# Superincreasing compression of auxiliary violations

Let H^+ be the auxiliary extension and let
F_d(pi)=x_d(pi)-y_d(pi)+g(pi)x_d(pi)y_d(pi)
be the odd exact violation coordinates from [[auxiliary_violation_vector_has_exact_chamber_zeros]], so each F_d lies in {-1,0,1}, reversal negates every coordinate, and all F_d vanish exactly on directed one-change orders.

Choose positive weights
W_1>W_2+...+W_D,
W_2>W_3+...+W_D,
...
for example W_d=3^{D-d}. Define
E(pi)=sum_d W_d F_d(pi).

Then E(pi^rev)=-E(pi), and
E(pi)=0 iff F_d(pi)=0 for every d.
Indeed, if d_0 is the least index with F_{d_0} nonzero, then the leading term W_{d_0}F_{d_0} has larger absolute value than the sum of all later terms. Thus the sign of E is the sign of the nearest nonzero violation coordinate, and E has exactly the desired chamber zeros.

This compresses the full exact violation vector to one real coordinate without losing chamber-level exactness. Convex zeros become weaker, but the released dimensions can be spent on independent antipodal gauges.

In particular, let H^+ have N=n+1 vertices, so its centered permutahedron boundary is S^{n-1}. Let T be a forest on V(H^+) with n-2 edges, hence exactly three connected components. For each forest edge ab let
g_ab(pi)=+1 if a precedes b and -1 otherwise.
The direct-sum chamber label
Lambda_T(pi)=(E(pi),(g_ab(pi))_{ab in E(T)})
takes values in R^{n-1} and is odd. Its barycentric face-average extension therefore has a zero.

At any zero carrier face C with the usual strictly positive chamber weights, every forest edge has both relative-order signs in the weighted balance. If its endpoints lay in distinct ordered blocks of C, their relative order would be fixed and the corresponding gauge could not average to zero. Hence every connected component of T lies wholly inside one block of C. Consequently C has at most three ordered blocks.

Thus the exact directed-one-change obstruction admits a dimension-tight reduction to three prescribed macrocomponents. Choosing one component to be {r} identifies the remaining problem with an odd scalar nearest-violation function on the boundary of the three-macrocomponent permutahedron. Along a fixed macro-order path that moves {r} from first to last, the scalar starts strictly negative and ends strictly positive under the counterexample hypothesis, so some singleton-r macrostate or adjacent two-block coarsening carries a scalar zero. This last scalar zero is not by itself a two-cover certificate; its value is the reduction of arbitrary carrier geometry to three moving chunks.

## Direct premises at migration

[
    {
        "premise_id": "antipodal_reachability_and_neutral_corridor",
        "premise_kind": "section",
        "premise_title": "Antipodal reachability and the neutral corridor",
        "compatibility_status": "confirmed",
        "premise_math_version": 4,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": false
    },
    {
        "premise_id": "auxiliary_violation_vector_has_exact_chamber_zeros",
        "premise_kind": "toolkit",
        "premise_title": "An odd auxiliary violation vector with one-change chamber zeros",
        "compatibility_status": "confirmed",
        "premise_math_version": 2,
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
