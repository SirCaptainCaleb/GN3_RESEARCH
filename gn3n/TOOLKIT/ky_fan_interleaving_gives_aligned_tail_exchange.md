# Ky Fan interleaving gives an aligned tail exchange

**Summary:** For an equal-side one-hole cover, the interleaved prescribed order P1,Q1,...,Pr,Qr,x makes any Ky Fan alternating-role cover an equal-size aligned tail exchange of the old supports.

## Statement

Let H-x=P|Q with P={p_1,...,p_r}, Q={q_1,...,q_r}, and suppose the Ky Fan alternating-role alternative applies. Prescribe the order p_1,q_1,...,p_r,q_r,x. If the resulting hole is p_j, then up to swapping the two new supports they are {p_i:i<j} union {q_i:i>=j} and {q_i:i<j} union {p_i:i>j} union {x}. If the hole is q_j, the cut is after j; if the hole is x, the supports are P,Q.

## Body

The graph-theoretic path orders of the new cover are not specified here; only its two support sets are. Since n=2r+1, deleting one hole leaves 2r labels, so the alternating signs occur r times each. In the prescribed interleaving, before the deleted position the parity classes are the old P and Q labels, while after the deletion every subsequent parity flips. Thus deleting p_j gives the two displayed tail-exchange supports; deleting q_j gives A={p_i:i<=j} union {q_i:i>j} and B={q_i:i<j} union {p_i:i>j} union {x}; deleting the final label x leaves the original parity classes P and Q. This converts the Ky Fan conclusion into an explicit aligned support exchange.

## Metadata

- ID: ky_fan_interleaving_gives_aligned_tail_exchange
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: passed
- Refutation: unrefuted
- Toolkit status: Limbo
