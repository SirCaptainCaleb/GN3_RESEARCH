# Packet reversal realizes opposite physical roots with the descent certificate intact

## Metadata

- ID: packet_reversal_realizes_opposite_physical_roots_with_the_descent_certificate_intact
- Parent Section: directed_nor_union_closed_bridge
- Position: 229
- Row version: 2
- Development version: 2
- Composition version: 1
- Composition stale: False

## Composition

Reversing a consecutive (r+1)-coordinate packet whose two r-windows have labels 10 preserves the word 10 and sends its actual window-slide root to its negative. It preserves full support and stays within a common tied-block cell when the packet lies there. Only r−1 crossing windows on either side need a collar check. This replaces the impossible persistence of that same root on an adjacent-swap edge by an explicit packet move; a global improvement still needs the collar conditions.

## Development

Combination of Article I's full-support interval-reversal calculus and Article II's physical window-slide roots.

Let π contain a consecutive packet W=(a_0,...,a_r), r≥2, with h(a_0,...,a_{r−1})=1 and h(a_1,...,a_r)=0. This is an actual 10 window descent with root ρ=e_{a_0}−e_{a_r}. Reverse precisely these r+1 consecutive coordinates and leave all other coordinates in their existing positions.

The two internal windows of the reversed packet have labels
h(a_r,...,a_1)=1−h(a_1,...,a_r)=1,
h(a_{r−1},...,a_0)=1−h(a_0,...,a_{r−1})=0.
Thus the same 10 descent survives and its physical root becomes −ρ. This is an explicit full-support root-reversal move. If W is contained in one tied block of an ordered-partition cell, both orders refine the same cell.

Only the r−1 windows crossing the left end and the r−1 crossing the right end can alter outside the packet; all other statuses stay fixed. The original 10 packet is preserved as an ordered status word. In ternary arity this leaves exactly the familiar two-status collar on either side.

This gives a certificate-preserving replacement for the proposed adjacent-swap extraction. A window-slide root has endpoints r positions apart, whereas an adjacent-swap edge makes them one position apart, so the same root certificate cannot persist there for r≥2. Packet reversal realizes opposite roots while retaining their actual descent.

The remaining condition is the explicit collar audit: a legal global descent, good-order improvement, or port-preserving connector move needs the changed crossing windows to satisfy its stated target. Root reversal itself preserves the internal defect. The useful common abstraction is therefore a rooted ordered packet with an exposed collar, rather than a root vector alone.
