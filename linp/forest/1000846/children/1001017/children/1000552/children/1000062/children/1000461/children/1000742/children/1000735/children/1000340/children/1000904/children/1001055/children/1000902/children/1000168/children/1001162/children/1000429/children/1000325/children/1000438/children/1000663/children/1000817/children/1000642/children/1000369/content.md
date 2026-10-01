# A genuine balanced lens has length at least two

## Statement

Let H be a simple linear hypergraph. Let Q and R be linear paths having a genuine clean balanced lens between distinct boundary vertices a,b, with Q-side and R-side internally vertex-disjoint and distinct. If the common side length is t, then t>=2.

Consequently, every balanced endpoint lens supplied by b35b0fd4e4cd that has genuinely distinct host and auxiliary sides uses at least two host edges and at least two auxiliary edges.

## Body

Suppose t=1. Then the Q-side of the lens consists of one hyperedge e_Q containing both boundary vertices a,b, and the R-side consists of one hyperedge e_R containing both a,b. Because the lens is genuine, its two sides are distinct, so e_Q!=e_R. But then the two distinct hyperedges e_Q,e_R intersect in the two vertices a,b, contradicting linearity. Therefore t cannot equal one. Since a genuine lens is nonempty, t>=2.

The endpoint-lens consequence is immediate because b35b0fd4e4cd produces a clean balanced elementary lens with distinct sides whenever the two maximum endpoint paths do not simply coincide along the relevant terminal segment.