# Lexicographic maxima confine pairwise repartition sizes

## Statement

Let A|B|C be a spanning three-cover of a boundary tournament, with a=|A|>=b=|B|>=c=|C|. In the graph of spanning three-covers connected by pairwise repartitions using two-component covers of the selected pair-union, suppose A|B|C has lexicographically maximal decreasing component-order triple in its connected component. Then every two-component cover of H[V(A) union V(B)] has both component orders in [b,a]; every two-component cover of H[V(B) union V(C)] has both component orders in [c,b]; and every two-component cover of H[V(A) union V(C)] has both component orders in [c,a]. In the last case, if one new component has order a, the other has order c.

## Body

For a two-component cover X|Y of A union B, write x=max(|X|,|Y|) and y=min(|X|,|Y|). Replacing A|B by X|Y gives an adjacent three-cover. Lexicographic maximality forbids x>a. Since x+y=a+b, this gives y>=b, while x>=b and y<=a. Hence both orders lie in [b,a].

For a two-component cover X|Y of B union C, if x>b then after replacement the sorted triple either has first coordinate larger than a (if x>a), or first coordinate a and second coordinate larger than b (if x<=a). Both contradict lexicographic maximality. Hence x<=b, and x+y=b+c gives y>=c.

For a two-component cover X|Y of A union C, maximality forbids x>a. Since x+y=a+c, this gives y>=c, so both orders lie in [c,a]. If x=a then y=c.

The qualification “two-component” is essential because project terminology uses “two-cover” for at most two paths. If a selected pair-union is Hamiltonian, replacing those two components by one path gives a spanning two-cover of H rather than another three-cover in the move graph; that is a direct escape, not an equal-level state constrained by lexicographic maximality.

The proof uses only reachability by pairwise repartitions and lexicographic maximality. It does not use the absence of a reachable two-cover, a minimum-counterexample hypothesis, fixed component orders, or orientation structure. This is the general core of repartlex01.
