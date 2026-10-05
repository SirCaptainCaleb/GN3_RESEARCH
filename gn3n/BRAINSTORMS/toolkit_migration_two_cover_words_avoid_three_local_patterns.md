# Toolkit migration — Two-cover status words avoid three local patterns

Preserved from the retired Toolkit Limbo object [[two_cover_words_avoid_three_local_patterns]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 1,
    "created_at": "2026-10-04T21:39:34.646436+00:00",
    "updated_at": "2026-10-04T23:33:01.57561+00:00",
    "archived_at": null,
    "original_id": "two_cover_words_avoid_three_local_patterns",
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

A binary status word satisfies the exact two-cover condition q<=p+1 iff it contains none of 001, 011, or 0101 as a consecutive subword. Equivalently, every bad word has a local witness on at most four consecutive status positions.

## Statement

Let epsilon_1...epsilon_m be a binary status word, with p the first 0 and q the last 1 using the usual conventions. Then q<=p+1 iff the word avoids the consecutive patterns 001, 011, and 0101. Equivalently, if q>=p+2, there is a minimal inversion pair i<j with epsilon_i=0, epsilon_j=1 and j-i>=2; its span is 2 or 3, yielding 001/011 or 0101.

## Body

# Two-cover status words avoid three local patterns

Let

`epsilon_1...epsilon_m`

be a binary status word. Put `p` for the first zero and `q` for the last one, with the usual endpoint conventions. The exact inversion-window criterion says that the corresponding spanning order yields a two-cover exactly when

`q<=p+1`.

This condition has a purely local forbidden-pattern form.

## Proposition

The following are equivalent:

1. `q<=p+1`;
2. there are no indices `i<j` with `epsilon_i=0`, `epsilon_j=1`, and `j-i>=2`;
3. the word contains none of the consecutive subwords

`001`, `011`, `0101`.

**Proof.** The equivalence of (1) and (2) is immediate from the definitions of the first zero and last one.

Assume (2) fails and choose an inversion pair `i<j` with `epsilon_i=0`, `epsilon_j=1`, `j-i>=2` having minimum span.

If `j-i=2`, the three-position subword is either `001` or `011`.

Suppose `j-i>=3`. Minimality implies that every position `k` with `i<k<=j-2` must have `epsilon_k=1`, since a zero there would give the shorter inversion `(k,j)`. Likewise every `k` with `i+2<=k<j` must have `epsilon_k=0`, since a one there would give the shorter inversion `(i,k)`. If `j-i>=4`, these two ranges overlap, a contradiction. Hence `j-i=3`. The two interior bits are then forced to be `1,0`, so the four-position subword is `0101`.

Conversely each of `001`, `011`, and `0101` visibly contains a zero followed at distance at least two by a one, so (2) fails. ∎

Thus badness of a spanning order is always witnessed on at most four consecutive status positions, equivalently on at most six consecutive vertices of the order.

Under reversal-complement, `001` and `011` are exchanged, while `0101` is fixed. This local symmetry is useful for antipodal labeling arguments.

## Direct premises at migration

[
    {
        "premise_id": "spanning_orders_and_defect_helly",
        "premise_kind": "section",
        "premise_title": "Spanning orders and defect Helly theory",
        "compatibility_status": "optimistic",
        "premise_math_version": 10,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": false
    }
]

## Direct consumers at migration

[
    {
        "consumer_id": "dual_polarity_witness_reduction",
        "consumer_kind": "toolkit",
        "consumer_title": "Dual-polarity witness reduction",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "consumer_toolkit_limbo": true
    },
    {
        "consumer_id": "local_bad_patterns_label_a_fixed_path",
        "consumer_kind": "toolkit",
        "consumer_title": "Local bad patterns label a fixed path",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 2,
        "consumer_toolkit_limbo": true
    },
    {
        "consumer_id": "local_witness_carriers_have_a_protected_central_band",
        "consumer_kind": "toolkit",
        "consumer_title": "Local-witness carriers have a protected central band",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "consumer_toolkit_limbo": true
    },
    {
        "consumer_id": "local_witness_topology_and_the_finite_terminal_theorem",
        "consumer_kind": "section",
        "consumer_title": "Local-witness topology and the finite terminal theorem",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "consumer_toolkit_limbo": false
    },
    {
        "consumer_id": "protected_good_band_forces_thin_face_blocks",
        "consumer_kind": "toolkit",
        "consumer_title": "A protected good band forces thin face blocks",
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
