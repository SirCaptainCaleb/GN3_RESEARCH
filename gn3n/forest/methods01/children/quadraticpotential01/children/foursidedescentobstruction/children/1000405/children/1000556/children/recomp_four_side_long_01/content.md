# Each long side of a four-side Phi-minimum yields a Hamiltonian four/five-set, order disagreement, a short interval path, or a reverse triple

## Statement

Let H be a minimum counterexample and let X|P|Q be a spanning three-cover that is Phi-minimal in its connected pairwise-repartition component, where X=(x_0,x_1,x_2,x_3) and |P|,|Q|>=6. Fix one long component R=(r_0,...,r_{m-1}) and let M=(r_1,...,r_{m-2}). Then at least one of the following holds: (1) H contains a Hamiltonian induced set of order four or five; (2) two tight paths order the common pair x_0,x_3 oppositely; (3) there are indices 1<=i<j<=m-3 with 2<=j-i<=4 such that (x_0,r_{i+1},...,r_j,x_3) is a tight path; (4) for such an attempted interval replacement, at least one applicable triple among (x_1,x_0,r_i), (r_{j+1},x_3,x_2), (x_0,r_1,r_0) when i=1, and (r_{m-1},r_{m-2},x_3) when j=m-3 is tight.

## Body

Apply 7af43d05be78 to the chosen long component R. Its first alternative gives outcome (1), and its second gives outcome (2). Otherwise it gives a tight path C=(x_0,r_{i+1},...,r_j,x_3) through an interval of the displayed middle path M, containing at least two vertices of R. If this path is oriented from x_3 to x_0, it orders the common pair x_0,x_3 oppositely from X and gives outcome (2). Thus assume it is oriented from x_0 to x_3 and put k=j-i>=2. In the construction underlying 7af43d05be78, this interval-path case comes from the two alternative-2 insertion gaps for x_0 and x_3, so the four tight prefix/suffix paths required by 8eabe59de572 hold. Apply 8eabe59de572. Either k<=4, giving outcome (3), or one of the explicit reverse triples listed in outcome (4) is tight.
