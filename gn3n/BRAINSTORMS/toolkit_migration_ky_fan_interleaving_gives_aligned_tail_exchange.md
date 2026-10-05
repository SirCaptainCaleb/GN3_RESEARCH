# Toolkit migration — Ky Fan interleaving gives an aligned tail exchange

Preserved from the retired Toolkit Limbo object [[ky_fan_interleaving_gives_aligned_tail_exchange]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 1,
    "created_at": "2026-10-05T00:39:36.26512+00:00",
    "updated_at": "2026-10-05T00:42:14.228078+00:00",
    "archived_at": null,
    "original_id": "ky_fan_interleaving_gives_aligned_tail_exchange",
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

For an equal-side one-hole cover, the interleaved prescribed order P1,Q1,...,Pr,Qr,x makes any Ky Fan alternating-role cover an equal-size aligned tail exchange of the old supports.

## Statement

Let H-x=P|Q with P={p_1,...,p_r}, Q={q_1,...,q_r}, and suppose the Ky Fan alternating-role alternative applies. Prescribe the order p_1,q_1,...,p_r,q_r,x. If the resulting hole is p_j, then up to swapping the two new supports they are {p_i:i<j} union {q_i:i>=j} and {q_i:i<j} union {p_i:i>j} union {x}. If the hole is q_j, the cut is after j; if the hole is x, the supports are P,Q.

## Body

The graph-theoretic path orders of the new cover are not specified here; only its two support sets are. Since n=2r+1, deleting one hole leaves 2r labels, so the alternating signs occur r times each. In the prescribed interleaving, before the deleted position the parity classes are the old P and Q labels, while after the deletion every subsequent parity flips. Thus deleting p_j gives the two displayed tail-exchange supports; deleting q_j gives A={p_i:i<=j} union {q_i:i>j} and B={q_i:i<j} union {p_i:i>j} union {x}; deleting the final label x leaves the original parity classes P and Q. This converts the Ky Fan conclusion into an explicit aligned support exchange.

## Direct premises at migration

[]

## Direct consumers at migration

[]

## Supersession records at migration

[]

## Retained passed-version snapshot at migration

null
