# The three-isolated-defect case is an exact cube of singleton transfers

## Statement

Let H be a boundary tournament with pc(H)>2 and let a minimum-span cyclic defect certificate Gamma have run type {1,1,1}. Then its eight cyclic-interval three-covers are naturally indexed by {0,1}^3, one bit choosing an endpoint of each isolated defect edge. Two covers differing in one bit differ by moving exactly one vertex from one of the two path components adjacent to that defect edge to the other, with the third component unchanged. Consequently, if one of the eight covers minimizes Phi over this cube, then at each of its three defect edges the donor side for the available bit-flip has order at most one larger than the recipient side.

## Body

Because Gamma is the disjoint union of three isolated edges, every minimum vertex cover of Gamma consists of exactly one endpoint from each defect edge, giving 2^3=8 cut sets. By the cyclic-interval cover construction, each cut set gives a spanning three-cover by the three cyclic intervals between its selected cut positions. Flipping one coordinate replaces the selected endpoint of one defect edge by the other endpoint. These two cut positions are consecutive on the cyclic order, while the other two cuts are fixed. Hence one of the two adjacent cyclic intervals gains exactly the single vertex between the old and new cut, the other loses exactly that vertex, and the third interval is unchanged. Thus every cube edge is a legal singleton transfer. If the affected component orders are d (donor) and r (recipient), the Phi change is (d-1)^2+(r+1)^2-d^2-r^2=2(r-d+1). At a Phi-minimum on the eight-state cube this is nonnegative for every available coordinate flip, so d<=r+1 at each defect edge.
