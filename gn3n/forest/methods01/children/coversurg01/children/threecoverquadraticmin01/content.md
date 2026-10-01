# Quadratic minima are pairwise minimum-imbalance covers

## Statement

Let H be a boundary tournament. Form the graph whose vertices are spanning three-covers of H and where two vertices are adjacent when one is obtained from the other by replacing two components by a two-component cover of their union. For C=P_1|P_2|P_3 put Phi(C)=sum_i |P_i|^2. If C is Phi-minimal in its connected component, then for every pair i<j and every two-component cover R|S of H[V(P_i) union V(P_j)],
||R|-|S|| >= ||P_i|-|P_j||.
Thus each displayed pair P_i|P_j is a minimum-imbalance two-component cover of its union.

## Body

Replacing P_i|P_j by a two-component cover R|S is an edge of the three-cover repartition graph and leaves the third component unchanged. Phi-minimality therefore gives
|R|^2+|S|^2 >= |P_i|^2+|P_j|^2.
Both pairs have the same total order N. For x+y=N,
x^2+y^2=(N^2+(x-y)^2)/2,
so the preceding inequality is equivalent to
||R|-|S|| >= ||P_i|-|P_j||.

The qualification “two-component” matters because project terminology uses “two-cover” for a cover with at most two paths. If the selected union is Hamiltonian, replacing P_i|P_j by one path leaves a spanning two-cover of H rather than another vertex of the three-cover graph; that is a direct escape, not an equal-level repartition covered by this Phi-minimality comparison.

No trapping hypothesis, minimum-counterexample hypothesis, fixed order, or boundary-tournament orientation property is used beyond the existence of the relevant covers. This is the general core behind 9b1b920f0aab and astra003quadraticpotential; those nodes retain the Astra-003 application and its further consequences.