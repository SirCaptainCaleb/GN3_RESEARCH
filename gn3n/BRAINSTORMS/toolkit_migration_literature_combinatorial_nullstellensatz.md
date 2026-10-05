# Toolkit migration — Alon's Combinatorial Nullstellensatz

Preserved from the retired Toolkit Limbo object [[literature_combinatorial_nullstellensatz]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 1,
    "created_at": "2026-10-05T00:02:45.173186+00:00",
    "updated_at": "2026-10-05T00:02:45.173186+00:00",
    "archived_at": null,
    "original_id": "literature_combinatorial_nullstellensatz",
    "audit_status": "unaudited",
    "math_version": 1,
    "toolkit_type": "other",
    "refutation_status": "unrefuted",
    "author_session_ids": [
    ],
    "audited_math_version": null
}

## Simplified statement

A nonzero top-degree coefficient forces a nonzero evaluation on every sufficiently large Cartesian grid.

## Statement

Let F be a field and f in F[x_1,...,x_n] have total degree sum_i t_i. If the coefficient of x_1^{t_1}...x_n^{t_n} is nonzero, then for arbitrary finite S_i subset F with |S_i|>t_i there exists (s_1,...,s_n) in product_i S_i with f(s_1,...,s_n) nonzero.

## Body

Literature theorem, nonvanishing form due to Noga Alon. Let f be a polynomial over a field with deg f=sum t_i and nonzero coefficient of product x_i^{t_i}. For any coordinate sets S_i with |S_i|>=t_i+1, f is nonzero at some grid point. Potential GN3 use: encode forbidden local choices or path-cover constraints by polynomial factors and prove existence of a legal discrete choice by isolating a top-degree monomial with nonzero coefficient. This is especially relevant to the square-zero/transfer-polynomial program, but the theorem itself is over an ordinary polynomial ring and any application must explicitly justify the passage from the square-zero algebra or construct an ordinary-grid polynomial. Source: N. Alon, Combinatorial Nullstellensatz, Combinatorics, Probability and Computing 8 (1999), 7-29.

## Direct premises at migration

[]

## Direct consumers at migration

[]

## Supersession records at migration

[]

## Retained passed-version snapshot at migration

null
