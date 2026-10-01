# A shortest backward collision closes a genuine linear cycle

## Statement

Let v_0v_1...v_k be a rainbow terminal-pair path of ascending nonspecial edges
E_s={x_s,v_{s-1},v_s}
with nondecreasing edge ranks. Suppose at least one color-terminal collision occurs, and choose x_i=v_j with minimum span i-j.

Then i-j>=3, the terminal subpath
E_{j+1},E_{j+2},...,E_{i-1}
is strong-rainbow and lifts to a linear hypergraph path, and
E_{j+1},E_{j+2},...,E_{i-1},E_i
is a linear cycle of length i-j.

Consequently, if r_i=phi(E_i), then
i-j <= r_i.

## Body

First i-j cannot equal 2. If i=j+2, then E_{j+1} contains the terminal pair {v_j,v_{j+1}}, while E_i=E_{j+2} contains v_j=x_i and the terminal v_{i-1}=v_{j+1}; the two distinct hyperedges would share two vertices, contradicting linearity. Hence i-j>=3.

Consider the terminal subpath P=E_{j+1},...,E_{i-1}. Its graph-edge colors are distinct because the ambient terminal path is rainbow. Suppose P were not strong-rainbow. Then for some s in {j+1,...,i-1}, its color x_s would equal a nonincident terminal vertex v_t of P, with j<=t<=i-1. By c9a012c1b82e every color-terminal collision points backward, so t<=s-2. Therefore x_s=v_t is a collision of span s-t. Since s<=i-1 and t>=j,
s-t <= (i-1)-j < i-j,
contradicting the minimality of x_i=v_j. Thus P is strong-rainbow, and by 8924e63f61db it lifts in the displayed order to a linear hypergraph path.

Now add E_i. It meets the first edge E_{j+1} at v_j=x_i and the last edge E_{i-1} at v_{i-1}. These vertices are distinct because i-j>=3. It has no other intersection with the lifted path. Indeed its third vertex v_i is not a terminal vertex of P, and cannot be an entrance color of an edge of P by the backward-collision lemma; an extra occurrence of v_j as an entrance color inside P would be a shorter collision; and v_{i-1} cannot occur as an earlier entrance color because color-terminal collisions cannot point forward. Hence the displayed edges form a linear cycle of length i-j.

Finally E_i is nonspecial, so f2925a904b8e gives that the length of any linear cycle containing E_i is at most phi(E_i)=r_i. Therefore i-j<=r_i.
