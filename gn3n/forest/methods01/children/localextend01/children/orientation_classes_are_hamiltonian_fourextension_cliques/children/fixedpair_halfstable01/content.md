# Every fixed pair has a large family of one- and two-label path-cover-two deletions

## Statement

Let H be a minimum counterexample on n vertices and let L,R be distinct vertices. Then there is a set C contained in V(H)-{L,R} with |C| at least ceil((n-2)/2) such that, writing G=H-{L,R}, the induced subtournaments G, G-y for every y in C, and G-{y,z} for every two distinct y,z in C are all non-Hamiltonian with path-cover number two.

## Body

Partition V(H)-{L,R} into C_+={y:(L,y,R) is tight} and C_-={y:(R,y,L) is tight}. By bd3c8d17ca06, any two distinct vertices y,z in the same class make {L,R,y,z} Hamiltonian. Choose C to be the larger class, so |C|>=ceil((n-2)/2). Put G=H-{L,R}. The two-vertex set {L,R} is itself a tight path, so G cannot be Hamiltonian: otherwise a Hamilton path on G together with the two-vertex path on {L,R} would form a spanning two-cover of H. Since G is a proper induced subtournament of the minimum counterexample, its path-cover number is exactly two. Now fix y in C. The three-set {L,R,y} is Hamiltonian, so G-y cannot be Hamiltonian, or complementary Hamilton paths would two-cover H. Minimality again gives path-cover number two. Finally, for distinct y,z in C, bd3c8d17ca06 makes {L,R,y,z} Hamiltonian. Therefore G-{y,z} is non-Hamiltonian for the same complementary-cover reason, and minimality gives path-cover number two. Thus the chosen orientation class C supplies the asserted simultaneous one- and two-label deletion stability.