# Hyperplane parity obstruction for spanning paths in binary projective STS

## Statement

Let d>=3 and let H be the Steiner triple system of lines of PG(d-1,2), on 2^d-1 points. If H has a spanning linear path, and J is the set of its joint vertices, then |J∩Pi| is even for every projective hyperplane Pi. Equivalently, representing points by nonzero vectors of F_2^d, the vector sum of J is 0.

## Body

A spanning linear path has ell=2^{d-1}-1 edges and therefore ell-1=2^{d-1}-2 joint vertices. Fix a hyperplane Pi. Let a be the number of path edges lying in Pi and j=|J∩Pi|. Every projective line either lies in Pi or meets Pi in exactly one point. Counting incidences of Pi-points with the path edges, every non-joint point is counted once and every joint twice, so the total is |Pi|+j=(2^{d-1}-1)+j=ell+j. On the other hand the a contained path edges contribute 3 each and the other ell-a path edges contribute 1 each, giving ell+2a. Hence j=2a is even.

Now identify the points with nonzero vectors in F_2^d. For every nonzero linear functional f, its kernel gives a hyperplane. Since |J| is even and |J∩ker(f)| is even, the number of j∈J with f(j)=1 is even. Thus f(sum_{j∈J}j)=0 for every f, forcing sum_{j∈J}j=0.