# Two individually insertable vertices either insert together or localize to three consecutive gaps

## Statement

Let B=(b_1,...,b_m) be a tight path and let x,y be distinct vertices outside B. For z in {x,y}, let I_z be the nonempty set of insertion positions in {0,...,m} at which inserting z into the displayed order of B gives a tight path. Then either there exist i in I_x and j in I_y with |i-j|>=2, in which case inserting x and y simultaneously at those two positions gives a tight path on V(B) union {x,y}; or I_x union I_y is contained in three consecutive insertion positions. Thus failure of simultaneous separated insertion forces all successful insertions of both exterior vertices into one bounded common window.

## Body

Suppose first that i in I_x and j in I_y satisfy i<j-1. Insert x after the first i old vertices of B and y after the first j old vertices. Because the two insertion positions are separated by at least one whole old edge, every consecutive triple in the resulting order is either a consecutive triple of B, a triple appearing in the x-only insertion at position i, or a triple appearing in the y-only insertion at position j. All such triples are tight, so the simultaneous insertion is a tight path. The case j<i-1 is symmetric. Now assume no such pair exists. Then |i-j|<=1 for every i in I_x and j in I_y. Let r be the minimum and s the maximum of I_x union I_y. If r and s belong to different insertion sets then s-r<=1. If they belong to the same insertion set, choose any position t from the other nonempty insertion set. The cross-distance condition gives t-r<=1 and s-t<=1, hence s-r<=2. Therefore I_x union I_y is contained in the three consecutive positions r,r+1,r+2 (with missing positions allowed).
