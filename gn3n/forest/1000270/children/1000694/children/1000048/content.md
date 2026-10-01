# Compatibility edges lift to one-move adjacency of deletion singleton states

## Statement

Let H be a boundary tournament with pc(H)>2. Let F_a be a two-cover of H-a and F_b a two-cover of H-b, and suppose F_a,F_b are compatible on V(H)-{a,b}. Then their spanning singleton lifts F_a|{a} and F_b|{b} are adjacent by one legal pairwise repartition in the graph of spanning covers with at most three components. Consequently every connected set of labels in a compatibility graph of chosen deletion covers has all of its singleton lifts in one component of that pairwise-repartition graph.

## Body

Let
W=V(H)-{a,b}.
Compatibility of F_a and F_b gives two common ordered support classes on W. By the compatible-pair theorem in d43a7c9e2f61, since pc(H)>2 the omitted labels a and b must restore into the same common class; restoration into different classes would itself give a spanning two-cover of H.

Call that common ordered class P and call the unchanged other class Q. Thus, at the support-and-order level,
F_a=P_b | Q,
F_b=P_a | Q,
where P_b is the tight path obtained by inserting b into P in F_a, and P_a is the tight path obtained by inserting a into P in F_b. The precise insertion slots may be equal or adjacent; nothing further is needed.

Consider the singleton lift of F_a:
P_b | Q | {a}.
Repartition the pair P_b | {a}, whose union is V(P) union {a,b}, as
P_a | {b}.
This is a legal pairwise repartition: P_a is a tight path because it is a component of F_b, {b} is a one-vertex tight path, the two new supports are disjoint, and together they cover exactly the same pair union.

The unchanged component Q remains fixed, so this single pairwise repartition produces
P_a | Q | {b},
which is exactly the singleton lift of F_b.

Therefore a compatibility edge between deletion covers lifts to an edge between their singleton-lift states. Along any path in the compatibility graph, these one-move lifts concatenate, so all singleton lifts indexed by one compatibility component lie in one component of the pairwise-repartition graph. ∎
