# Every boundary tournament of order at least seven has a five-vertex reversal

**Summary:** Every boundary tournament of order at least seven has a five-vertex reversal

## Statement

Let H be a boundary tournament of order n>=7. Then there exist distinct vertices a,b,y,z,w such that R=(y,b,z,a) is a tight path and T=(z,b,w) is a tight triple. In particular T reverses the ordered edge (b,z) of R. Thus every boundary tournament of order at least seven contains a genuine reversing tight triple, with the reversing configuration supported on at most five vertices.

## Body

Fix distinct vertices a,b. For each vertex x outside {a,b}, boundary antisymmetry says exactly one of (b,x,a) and (a,x,b) is tight. Since n-2>=5, one of these two orientation classes contains at least three vertices. After interchanging a,b if necessary, choose distinct y,z,w with (b,y,a), (b,z,a), and (b,w,a) tight. Orient the ordinary complete graph on {y,z,w} by p->q exactly when (p,b,q) is tight. Boundary antisymmetry makes this a tournament. Every three-vertex tournament has a directed path of length two; relabel so y->z->w. Then (y,b,z) and (z,b,w) are tight. Together with (b,z,a), this makes R=(y,b,z,a) a tight path. The tight triple T=(z,b,w) traverses the adjacent pair {b,z} as z,b, while R traverses it as b,z. Hence T reverses the ordered edge (b,z) of R. All five displayed vertices are distinct.

## Metadata

- ID: tournament_of_order_at_least_seven_has_a_fivevertex_reversal
- Kind: toolkit
- Version: 2
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Toolkit status: Promoted
