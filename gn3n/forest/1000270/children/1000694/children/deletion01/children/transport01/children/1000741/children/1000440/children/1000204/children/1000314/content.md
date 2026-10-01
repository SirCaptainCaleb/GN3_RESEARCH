# Each anchor-neighborhood compatibility component is a consecutive run on one anchor path

## Statement

Fix an anchor deletion cover F_d=P|Q and let S be labels whose chosen deletion covers are compatible with F_d. In the full-compatibility graph induced by S, every connected component with at least two vertices lies entirely on one of P,Q and consists of a consecutive run of vertices in that displayed anchor order. More precisely, if a component on P contains p_i and p_j with i<j, then it contains every p_t for i<=t<=j and its edges are exactly the consecutive pairs along that run. Hence the component has j-i+1 vertices and is a path; in particular anchor-neighborhood compatibility has no cycles.

## Body

The certified theorem 47d4a615286a says that every compatibility edge yz inside N(F_d) joins two labels lying on the same anchor component and consecutive in the displayed anchor order. Therefore the induced compatibility graph on S is a subgraph of the ordinary adjacency graph of the full displayed paths P and Q. Let C be a connected component containing p_i and p_j with i<j. Any graph path in C from p_i to p_j can move only between consecutive anchor positions, so it must visit p_{i+1},...,p_{j-1}; all those labels belong to S. Moreover connectivity forces each consecutive edge p_t p_{t+1} along the interval to be present. Thus C is exactly the path on the consecutive run p_i,...,p_j. The same holds on Q. This strengthens the earlier bounded-step formulation: the step size is exactly one whenever an edge exists.