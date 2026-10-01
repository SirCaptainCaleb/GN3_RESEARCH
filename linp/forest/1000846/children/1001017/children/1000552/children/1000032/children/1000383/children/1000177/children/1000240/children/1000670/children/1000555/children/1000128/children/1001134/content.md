# Rank-ordered source rails force linear distinguished overlap

## Statement

Let e_1,...,e_k be distinct ascending nonspecial edges terminal at a common vertex v, ordered so that
r_1<=...<=r_k,
where r_i=phi(e_i). Write e_i={x_i,v,u_i}, with x_i the unique entrance, and choose a canonical maximum source rail R_j ending at x_j for every j.

Fix integers h,m>=1 with h+m<=k, and choose any m indices
j_1,...,j_m > h.
For each chosen rail R_j and each coordinate i<=h, the rail meets {x_i,u_i}. Consequently some pair of the m chosen rails has at least
h * floor((m-1)^2/4) / C(m,2)
common distinguished vertices from the disjoint pairs {x_i,u_i}, i<=h.
In particular this is at least
h (m-2)/(2(m-1))
for m>=2, and is h/2-O(h/m).

Taking the last m=k-h rails and h=floor(k/2), some two source rails share at least
k/4-O(1)
distinct distinguished vertices. Thus a common-terminal family of k ascending edges necessarily contains a pair of maximum source rails with linear overlap.

## Body

By 1c8aac8aa4dd, every chosen rail R_j with j>h meets every earlier edge e_i, i<=h. Since R_j avoids v, this meeting uses x_i or u_i (possibly both).

For each chosen rail and coordinate i, choose one symbol in {X,U}: choose X if x_i lies on the rail, and otherwise choose U; the latter is available because the rail meets e_i. This gives m binary words of length h.

At a fixed coordinate i, suppose a of the m words choose X and m-a choose U. The number of agreeing pairs at this coordinate is
C(a,2)+C(m-a,2),
whose minimum over integers a is floor((m-1)^2/4). Summing over the h coordinates, the total number of coordinate agreements over all C(m,2) rail pairs is at least
h floor((m-1)^2/4).
Hence some pair agrees in at least the displayed average number of coordinates.

Every agreement produces a common distinguished vertex of the two rails. Vertices coming from different coordinates are distinct: if i!=i', then the non-v pairs e_i minus {v} and e_i' minus {v} are disjoint by linearity, since e_i and e_i' already share v. Thus the number of agreements is a genuine lower bound on the number of distinct common vertices.

For the final assertion choose h=floor(k/2) and m=k-h. Then m and h differ by at most one, and the displayed lower bound is k/4-O(1).
