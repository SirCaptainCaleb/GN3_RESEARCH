# The contiguous-path number is the vertex-cover number of the defect line

## Statement

Let pi=(v_1,...,v_n) be any vertex ordering and let D(pi) subset {2,...,n-1} be its defect centers. Form a graph L_pi on cut positions {1,...,n-1}, putting the edge {i-1,i} for every defect center i. Then
c(pi)=1+tau(L_pi)=1+nu(L_pi),
where tau is minimum vertex-cover number and nu maximum matching number. Equivalently, if the maximal runs of consecutive defect centers have lengths r_1,...,r_s, then
c(pi)=1+sum_j ceil(r_j/2).
In particular c(pi)=3 exactly when either the defects form one consecutive run of length three or four, or they form two separated runs each of length one or two. Thus every c=3 ordering has at most four defect centers.

## Body

A partition of pi into contiguous intervals is specified by a set C of cut positions, where j in C means cutting between v_j and v_{j+1}. A resulting interval is a tight path exactly when none of its internal consecutive triples is defective.

A defect centered at i survives inside one interval precisely when neither adjacent cut position i-1 nor i is chosen. Therefore all resulting intervals are tight exactly when C meets every pair {i-1,i} with i in D(pi). In other words C is a vertex cover of L_pi. A partition using |C| cuts has |C|+1 nonempty contiguous pieces, so
c(pi)=1+tau(L_pi).

The graph L_pi is a subgraph of the ordinary path on cut positions 1,...,n-1, hence is bipartite. By the path case of Konig's theorem, or directly by greedy matching, tau(L_pi)=nu(L_pi).

If a maximal run of defect centers has length r, its corresponding component of L_pi is a path with r edges, whose matching/vertex-cover number is ceil(r/2). Different runs give disjoint components, proving the sum formula.

Finally sum ceil(r_j/2)=2 has exactly two forms: one run with r=3 or 4, or two runs with each r in {1,2}. Hence at most four defect centers occur when c(pi)=3. ∎
