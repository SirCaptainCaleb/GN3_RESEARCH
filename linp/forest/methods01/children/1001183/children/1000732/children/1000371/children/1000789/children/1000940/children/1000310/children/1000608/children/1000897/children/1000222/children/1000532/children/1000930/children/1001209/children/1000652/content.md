# Two nested backward collisions either shortcut to a linear cycle or contain a further collision

## Statement

Let v_0v_1...v_k be a rainbow terminal-pair path of ascending nonspecial edges
E_s={x_s,v_{s-1},v_s}
with nondecreasing edge ranks. Suppose
x_i=v_j and x_h=v_l
are nested backward collisions with
j<l<h<i.

Consider the shortcut edge sequence
C =
E_{j+1},E_{j+2},...,E_l,
E_h,
E_{h+1},E_{h+2},...,E_i.

Then exactly one of the following holds.

(A) C is a linear cycle, of length
L=(l-j)+1+(i-h)=i-j-(h-l)+1.
In this case every edge of C has rank at least L, and in particular r_i>=L+1.

(B) There is an additional backward color-terminal collision x_b=v_a, distinct from the two displayed collisions, whose interval [a,b] is contained in [j,l], or contained in [h,i], or satisfies
j<=a<l<h<b<=i.
In the last case [l,h] is properly contained in [a,b], which is properly contained in [j,i] unless an endpoint agrees with the outer collision.

Thus a nested pair that does not yield the shortcut cycle necessarily exposes a further collision in one of the two flanks or between the two nesting levels.

## Body

The displayed sequence is connected cyclically by the intended intersections:
E_l meets E_h at x_h=v_l;
E_h meets E_{h+1} at v_h;
consecutive edges in each retained terminal segment meet at their usual terminal-path joints; and E_i meets E_{j+1} at x_i=v_j.
These intended consecutive intersection vertices are distinct because the terminal graph path is simple and j<l<h<i.

Any failure of C to be a linear cycle must therefore come from an additional intersection between two nonconsecutive displayed edges. The original terminal-pair path is simple and the parent hypergraph is linear, so such an extra intersection cannot be a repeated terminal-path joint. Because the edge colors x_s are pairwise distinct, it also cannot be an entrance-entrance coincidence. Hence every extra intersection is an entrance x_b of one displayed edge equal to a terminal-path vertex v_a belonging to another displayed edge: a color-terminal collision.

By c9a012c1b82e every such collision points backward, so a<=b-2. Since the displayed edges come from the left retained block [j+1,l], the bridge edge h, and the right retained block [h+1,i], the collision interval must be of one of three types:
(i) both endpoints lie in the left block, giving [a,b] contained in [j,l];
(ii) both lie in the right block, giving [a,b] contained in [h,i];
(iii) the terminal endpoint lies on the left and the colliding edge lies on the right, giving a<l<h<b, hence an interval spanning the deleted inner block.
The designated collisions [j,i] and [l,h] account for the intended closure and bridge intersections, so any nonconsecutive extra intersection gives an additional collision as in (B). Conversely, if no such extra collision occurs, C is a linear cycle.

In case (A), C has L edges and every displayed edge is ascending nonspecial. By f2925a904b8e each has rank at least L. In particular r_{j+1}>=L. The outer collision x_i=v_j gives r_{j+1}<=r_i-1 by c9a012c1b82e, so r_i>=L+1.