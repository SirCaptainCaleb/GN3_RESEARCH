# Two crossing backward collisions either shortcut to a linear cycle or expose a further collision

## Statement

Let v_0v_1...v_k be a rainbow terminal-pair path of ascending nonspecial edges
E_s={x_s,v_{s-1},v_s}
with nondecreasing edge ranks. Suppose
x_i=v_j and x_h=v_l
are crossing backward collisions with
j<l<i<h.

Consider the edge sequence
C=
E_{j+1},E_{j+2},...,E_l,
E_h,E_{h-1},...,E_i.

Then one of the following holds.

(A) C is a linear cycle of length
L=(l-j)+(h-i+1).
Every edge of C has rank at least L, and r_i>=L+1.

(B) There is an additional backward collision x_b=v_a, distinct from the two displayed collisions, with either
j<=a<b<=l,
or
i<=a<b<=h,
or
j<=a<l<i<b<=h.
Thus failure of the crossing shortcut is witnessed in one of the two flanks or by another collision lying inside the crossing rectangle between the displayed chords.

## Body

The displayed sequence has the intended consecutive intersections:
the left terminal segment runs from v_j to v_l;
E_l meets E_h at x_h=v_l;
the reversed right terminal segment runs from E_h down to E_i using the joints v_{h-1},...,v_i;
and E_i meets E_{j+1} at x_i=v_j, closing the cycle.
All intended intersection vertices are distinct because the terminal graph path is simple and j<l<i<h.

If C is not a linear cycle, two nonconsecutive displayed hyperedges have an extra common vertex. Distinct terminal-pair edges on the original simple terminal path cannot create such an intersection through two terminal vertices, and rainbow colors exclude entrance-entrance coincidences. Hence an extra intersection is a color-terminal equality x_b=v_a.

By c9a012c1b82e every such equality points backward in the original index order, so a<=b-2. The displayed indices consist of the left block j+1,...,l and the right block i,...,h. Therefore an additional collision must have both endpoints in the left block, both in the right block, or terminal endpoint in the left block and colliding-edge index in the right block. These are exactly the three alternatives in (B). A collision with terminal endpoint on the right and colliding edge on the left would point forward and is impossible.

If no such additional collision exists, C is a linear cycle. Its length is
L=(l-j)+(h-i+1).
All displayed edges are ascending nonspecial, so f2925a904b8e gives rank at least L for each of them. In particular r_{j+1}>=L. The collision x_i=v_j gives r_{j+1}<=r_i-1 by c9a012c1b82e, hence r_i>=L+1.