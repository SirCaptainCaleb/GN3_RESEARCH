# Quadratic-maximal relocation states force reversed interfaces on every size-gap-one pair

## Statement

In a trapped contiguous-block relocation component, let A|B|C maximize Phi and let X=(x_1,...,x_p), Y=(y_1,...,y_q) be displayed blocks with p>q>=2. For the unordered pair {X,Y}, either one of the two ordered interfaces is double non-tight, or both endpoints x_1,x_p of the larger block admit legal transfers into the smaller block, each producing size pair (p-1,q+1). If p=q+1, the latter alternative is impossible: the two transfer triples combine to a tight path (x_p,Y,x_1), and repartitioning as X^o | (x_p,Y,x_1) raises Phi, contradicting maximality. Hence every size-gap-one block pair has a double-non-tight orientation and therefore its forced reversed four-path interface. Also a trapped quadratic-maximal state cannot contain two blocks of order two, because their reversed interface Hamiltonizes their union and merges them.

## Body

Quadratic maximality applied to X|Y says the interface is double non-tight or has the unique single-tight slide moving x_p from X to Y. Permute whole blocks and apply the same statement to Y|X. If that orientation is not double non-tight, its unique slide moves x_1 from X to Y. Thus absence of a double-failure orientation gives transfers of both endpoints. The change of Phi for either single transfer is 2(q-p)+2.

Now let p=q+1. If both transfers exist, the tight triples at the two ends of Y concatenate with the displayed order of Y to give (x_p,y_1,...,y_q,x_1). The inherited middle X^o=(x_2,...,x_{p-1}) is nonempty. Moving x_1 past Y gives a legal three-block state X^o | (x_p,Y,x_1) | Z whose size-pair change is (p,q)->(p-2,q+2); its Phi change is 4(q-p+2)=4, contradicting maximality. Thus one orientation must be double non-tight.

Finally, if two blocks both have order two, the equal-size maximality rule makes their ordered interface double non-tight. Boundary antisymmetry yields the reversed four-vertex path on their entire union, merging them and contradicting trappedness. Hence at most one block has order two.
