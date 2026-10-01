# Gap-three rotation position gives a quantitative hole-potential floor

## Statement

In the lexicographically maximal two-hole state of a7e06ef01132, suppose a gap-three rotation of 387e8e7dba7c occurs with k=i+3 on an s-edge wrong-entrance path Q=(p_1,...,p_s). Then both current holes a,b satisfy
  phi(a),phi(b) >= max{i, s-i-2}.

Hence a gap-three rotation whose cut lies within r cells of either end forces both hole potentials to be at least s-r-2.

## Body

The gap-three rotation replaces the two path edges p_{i+1},p_{i+2} by the two hole edges f,g and imports the old holes a,b. Since the path length is unchanged, exactly two old path vertices become the new holes a',b'. Every ejected vertex lies in V(p_{i+1}∪p_{i+2}).

We use the position-sensitive part of 8b1790d79d74. For any vertex v lying on p_j, regardless of whether v is private or one of the adjacent joints,
  phi(v)>=max{j-1,s-j}.
Indeed this is immediate from the three cases in 8b1790d79d74.

For j=i+1 this gives
  phi(v)>=max{i,s-i-1},
and for j=i+2 it gives
  phi(v)>=max{i+1,s-i-2}.
Both quantities are at least max{i,s-i-2}. Therefore
  phi(a'),phi(b')>=max{i,s-i-2}.

By lexicographic maximality of the old hole-potential pair, as in a7e06ef01132, its smaller coordinate cannot be below the smaller coordinate of the new pair. Hence both old holes have potential at least max{i,s-i-2}.

If the cut is within r cells of the left end, i<=r, the displayed lower bound is at least s-r-2. If it is within r cells of the right end, s-i-2<=r implies i>=s-r-2, giving the same conclusion.