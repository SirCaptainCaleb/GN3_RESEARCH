# Minimum-counterexample calculus

**Summary:** A minimum counterexample has path-cover number three, every proper induced subtournament has path-cover number at most two, and proper Hamiltonian supports have exact two-cover complements.

## Statement

If the grand two-cover conjecture fails and H is a counterexample of minimum order n, then pc(H)=3; every proper induced subtournament has path-cover number at most two; every proper Hamiltonian set has a complementary exact two-cover; deleting one or two vertices leaves an exact two-cover with no singleton component; every tight path or cycle leaves at least four vertices; and n>10.

## Body

# Minimum-counterexample calculus

Assume the grand two-cover conjecture is false and let H be a counterexample of minimum order n.

## Proper induced subtournaments and path complements

Every proper induced subtournament of H has path-cover number at most two, by minimality. For any vertex v, a two-cover of H-v together with the singleton (v) gives a three-cover of H. Since pc(H)>2, pc(H)=3.

Let S be a nonempty proper subset such that H[S] is Hamiltonian. Minimality gives pc(H-S)<=2. If H-S were Hamiltonian, a Hamilton path on S and one on V(H)-S would form a spanning two-cover. Therefore pc(H-S)=2.

Thus every proper tight path has an exact two-cover on its complement. In particular every tight path has order at most n-4: its complement is non-Hamiltonian, while every boundary tournament of order at most three is Hamiltonian. Opening a tight cycle at any ordinary cycle edge gives a tight path on the same support, so every tight cycle also has order at most n-4.

## One- and two-vertex deletions

For every vertex v, pc(H-v)=2. Every exact two-cover of H-v has both components nontrivial. Otherwise one component is a singleton (s), and the two-vertex path (v,s), together with the other component, two-covers H.

For distinct a,c, the two-vertex sequence (a,c) is a tight path, so the complement principle gives pc(H-{a,c})=2. Again every exact two-cover has both components nontrivial. If (s) were a singleton component, exactly one of (a,s,c) and (c,s,a) is tight; that three-path together with the other component would two-cover H.

## The order is greater than ten

The small-set structure theorem supplies two facts:

1. every six-set contains at least four Hamiltonian five-subsets;
2. a Hamiltonian five-set contains at most three non-Hamiltonian four-subsets, while a non-Hamiltonian five-set contains at most one.

Every boundary tournament of order at most six has a two-cover by splitting the vertices into sets of order at most three. For orders seven and eight, choose six vertices; one Hamiltonian five-subset has a complement of order at most three. Hence n>=9.

Suppose n=9. Let F5 be the Hamiltonian five-subsets and B4 the non-Hamiltonian four-subsets. Counting incidences between six-sets and Hamiltonian five-subsets gives 4|F5| >= 4 C(9,6), because each six-set contributes at least four and each five-set lies in four six-sets. Hence |F5|>=84.

The complement of every member of F5 lies in B4, otherwise complementary Hamilton paths would two-cover H. Thus |B4|>=|F5|.

Each bad four-set lies in five five-sets. Counting its incidences with five-sets and using fact 2 gives
5|B4| <= 3|F5| + (C(9,5)-|F5|) = 126 + 2|F5|.
Together with |B4|>=|F5| this gives |F5|<=42, contradiction.

Suppose n=10. Double-count pairs F subset U with |F|=5, |U|=6, and F Hamiltonian. Every six-set contributes at least four such F, and every five-set lies in five six-sets. If h5 is the number of Hamiltonian five-sets, then 5 h5 >= 4 C(10,6), so h5>=168.

But the 252 five-sets form 126 complementary pairs, and at most one member of each pair can be Hamiltonian. Hence h5<=126, contradiction.

Therefore n>10.

## Metadata

- ID: mincex01
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
