# Affine F3 joint-sum obstruction for spanning paths

## Statement

Let H be the affine Steiner triple system AG(d,3) on F_3^d, d>=2. If H has a spanning linear path, with joint set J, then sum_{x in J} x=0 in F_3^d. In particular AG(2,3) contains no spanning 4-edge linear path, giving a short algebraic proof of the affine-plane P4 obstruction.

## Body

Every affine line of AG(d,3) has the form {x-a,x,x+a}, whose three point-vectors sum to 3x=0 in F_3^d. Sum the point-vectors over all edges of a hypothetical spanning path. Every nonjoint vertex is counted once and every joint twice. Since the path spans all of F_3^d, this sum equals sum_{v in V}v + sum_{j in J}j. The sum of all vectors of F_3^d is 0, while the sum over each path edge is 0, so sum_{j in J}j=0.

For d=2 the system has 9 points and a spanning path would have 4 edges and exactly 3 joints. Three distinct points of F_3^2 sum to 0 if and only if they are an affine line. Hence the three joints lie on one line L. But every pair of consecutive joints determines the internal path edge joining them, so that edge must be L and therefore contains the third joint as well. An internal edge of a linear 4-edge path contains exactly its two consecutive joints and one nonjoint vertex, contradiction.