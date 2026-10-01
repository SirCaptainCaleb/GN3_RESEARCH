# Every boundary tournament of order at least seven has five-vertex order disagreement

## Statement

Let H be a boundary tournament of order n>=7. Then H contains two Hamiltonian four-paths whose union has at most five vertices and whose common vertices occur in different relative orders. In particular every boundary tournament of order at least seven has nonvacuous relative-order disagreement supported on at most five vertices.

## Body

Fix any two distinct vertices a,b. For every vertex y outside {a,b}, boundary antisymmetry says exactly one of (b,y,a) and (a,y,b) is tight. Thus the n-2 exterior vertices split into two orientation classes. Since n>=7, one class contains at least three vertices. After possibly interchanging a and b, choose distinct y,z,w with (b,y,a),(b,z,a),(b,w,a) all tight.

Orient the ordinary complete graph on {y,z,w} by p->q exactly when (p,b,q) is tight. Boundary antisymmetry makes this a tournament. Every tournament on three vertices has a vertex with one incoming and one outgoing incident arc, so after relabelling we may assume y->z and z->w. Hence (y,b,z) and (z,b,w) are tight.

Therefore R=(y,b,z,a) and S=(z,b,w,a) are Hamiltonian four-paths. Their common vertices include z,b,a; in R the vertex b precedes z, while in S the vertex z precedes b. Thus R and S have order disagreement on the common pair {b,z}. Their union is contained in {a,b,y,z,w}, proving the theorem.