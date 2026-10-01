# Collision-adjacent double blockers are localized on the source-rail tail

## Statement

Retain the setting of fff2955f7084. Thus x_i=v_j is a backward collision for the rank-r_i edge E_i, and R_i is a canonical (r_i-1)-edge source rail ending at x_i.

Let F be either E_{j+1}, or E_j when j>=1, and put s=phi(F). Then F is not an edge of R_i. Among the vertices of F∩V(R_i) distinct from x_i, choose z closest to x_i along R_i, and let d be the number of R_i-edges in the segment from z to x_i.

Then
1 <= d <= s-1 <= r_i-2.

For F=E_j and F=E_{j+1}, the chosen vertices z are distinct. Hence an interior backward collision forces two distinct lower-rank blocker contacts into rank-controlled terminal segments of its source rail.

## Body

By fff2955f7084, F has a contact with R_i distinct from x_i, and s<=r_i-1.

First F cannot itself be an edge of R_i. Otherwise the initial segment of R_i ending in F gives a path ending in F, and if F is the last edge of R_i this path has length r_i-1>=s and ends through x_i. If the length exceeds s this contradicts the definition of s=phi(F); if it equals s, it is a longest F-path entering F through x_i. But F is nonspecial and its unique entrance is its rainbow color, distinct from the incident terminal x_i. If F occurs earlier on R_i, the suffix of R_i from F to x_i shows that R_i is not a path because F would then meet the later occurrence of x_i while x_i is the endpoint; equivalently, a path edge containing the endpoint x_i must be the last edge. Thus F is not an R_i-edge.

Choose z to be the F-contact distinct from x_i that is closest to x_i along R_i. By this choice, the open R_i-segment from z to x_i contains no further vertex of F. Therefore that segment together with F is a linear cycle of length d+1: F meets the segment exactly at z and x_i, while the segment is part of the linear path R_i.

Since F is ascending nonspecial of rank s, the certified cycle-rank bound f2925a904b8e gives
d+1<=s,
hence d<=s-1. Also d>=1. From fff2955f7084, s<=r_i-1, so d<=r_i-2.

Finally E_j and E_{j+1} already share x_i=v_j. By linearity they cannot share any second vertex, so their chosen non-x_i contacts on R_i are distinct.
