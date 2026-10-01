# Fixed-hole one-contact chords either bridge or collapse to one two-edge window

## Statement

For a path P ending at x and an outside fixed hole b with at least three one-contact external b-chords, either two chords satisfy the corrected bridge criterion, or all contacts other than x lie in two consecutive path edges. Consequently, in the canonical loss-one two-cycle the fixed-hole escape problem reduces to: an edge disjoint from the rotated path, a corrected two-chord bridge, or a single two-edge contact window containing all non-x one-contact chords.

## Body

Let F be at least three one-contact external b-edges and for f in F let alpha(f),beta(f) be the first and last path-edge indices containing its contact w_f. Distinct b-edges have distinct contacts, so at most one contact is x. Let r=min alpha(f), and choose g with w_g≠x maximizing beta(g). If beta(g)>=r+2, choose f with alpha(f)=r. Then f≠g because a path vertex lies in at most two consecutive path edges, so alpha(f)+2<=beta(g); the corrected two-chord bridge applies.

Otherwise beta(g)<=r+1. Every non-x contact h has alpha(h)>=r and beta(h)<=r+1, hence w_h lies in p_r union p_{r+1}. This proves the bridge-or-window dichotomy.

In the canonical loss-one two-cycle, the fixed-hole surplus gives either an edge through b disjoint from the rotated state P_1 or at least three one-contact external b-edges. In the latter case apply the dichotomy above. Thus exactly the three residual geometries stated remain: a disjoint edge, a bridge producing a longer x-ending path, or concentration of every non-x external contact in one two-edge window.
