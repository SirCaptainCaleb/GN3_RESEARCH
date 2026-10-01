# Every inclusion-minimal backward collision is a nonspecial cycle with one unit of rank slack

## Statement

Let v_0v_1...v_k be a rainbow terminal-pair path of ascending nonspecial edges
E_s={x_s,v_{s-1},v_s}
with nondecreasing edge ranks r_s.

Call a backward color-terminal collision interval [j,i], meaning x_i=v_j, inclusion-minimal if there is no other collision x_h=v_l with j<=l<h<=i such that [l,h] is a proper subinterval of [j,i].

If [j,i] is inclusion-minimal and c=i-j, then:
(1) c>=3;
(2) E_{j+1},...,E_{i-1} is strong-rainbow;
(3) E_{j+1},...,E_i is a linear cycle of length c;
(4) every edge on this cycle has rank at least c;
(5) r_i>=c+1.

## Body

The proof of (1)--(3) is the minimum-span argument localized to the interval [j,i].

First c cannot equal 2: E_{j+1} and E_i=E_{j+2} would both contain v_j and v_{j+1}, contradicting linearity.

Consider the terminal subpath E_{j+1},...,E_{i-1}. If it were not strong-rainbow, some color x_h with j+1<=h<=i-1 would equal a nonincident terminal vertex v_l of this subpath. By c9a012c1b82e the collision points backward, so l<=h-2, and because v_l lies on this subpath we have j<=l. Hence [l,h] is a proper collision subinterval of [j,i], contrary to inclusion-minimality. Thus the subpath is strong-rainbow and lifts to a linear hypergraph path by 8924e63f61db.

Adding E_i closes this path at v_j=x_i and v_{i-1}. There are no further intersections. The third vertex v_i is not a terminal vertex of the interior path; it cannot be an interior entrance color because that would be a forward color-terminal collision. Likewise an interior entrance equal to v_j would give a proper collision subinterval [j,h], and an interior entrance equal to v_{i-1} would point forward. Therefore E_{j+1},...,E_i is a linear cycle of length c.

All its edges are ascending nonspecial. By f2925a904b8e every nonspecial edge on a c-edge linear cycle has rank at least c. In particular r_{j+1}>=c. On the other hand c9a012c1b82e applied to x_i=v_j gives r_{j+1}<=r_i-1. Hence r_i>=c+1.
