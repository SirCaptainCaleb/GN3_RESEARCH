# Lexicographically maximal reachable three-covers confine pairwise repartition sizes

## Statement

Fix a spanning three-path cover A|B|C with a=|A|>=b=|B|>=c=|C| that is lexicographically maximal among all three-covers reachable from it by Astra's pairwise repartition moves, assuming no reachable two-cover exists. Then every exact two-cover of A union B has both component orders in [b,a], every exact two-cover of B union C has both component orders in [c,b], and every exact two-cover of A union C has both component orders in [c,a]. Moreover, an A union C repartition with a component of order a must have component orders a,c.

## Body

# Reachable lexicographic confinement

Assume the pairwise-repartition move system of Astra's conjecture, and suppose the reachable class under consideration contains no cover with at most two components. Choose a reachable three-cover A|B|C whose decreasing component-order triple (a,b,c), a>=b>=c, is lexicographically maximal.

Consider any exact two-cover X|Y of H[V(A) union V(B)], and write x=max{|X|,|Y|}, y=min{|X|,|Y|}. Replacing A|B by X|Y is one legal move, so X|Y|C is reachable. Lexicographic maximality forbids x>a. Since x+y=a+b, we get y>=b. Also x>=b and y<=a, so both new orders lie in [b,a].

Now consider an exact two-cover X|Y of H[V(B) union V(C)]. If x>b, then in the reachable cover A|X|Y either x>a, increasing the first coordinate, or x<=a, in which case the first coordinate remains a and the second becomes x>b. Both contradict lexicographic maximality. Hence x<=b. Since x+y=b+c, we obtain y>=c, so both new orders lie in [c,b].

Finally, for an exact two-cover of H[V(A) union V(C)], lexicographic maximality again forbids x>a; from x+y=a+c this gives y>=c, hence both orders lie in [c,a]. If x=a then y=c.

Thus a terminal obstruction to Astra's reconfiguration conjecture may be normalized to a three-cover whose adjacent pair-unions are size-rigid: repartitioning A union B cannot move mass outside [b,a], and repartitioning B union C cannot move mass outside [c,b]. In particular, if a=b then every exact two-cover of A union B has orders a,a; if b=c then every exact two-cover of B union C has orders b,b. This isolates exact equality plateaux as the natural residue for further structural attack.