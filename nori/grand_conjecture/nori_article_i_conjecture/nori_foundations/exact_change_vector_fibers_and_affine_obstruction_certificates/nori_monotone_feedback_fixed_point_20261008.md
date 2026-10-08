# Monotone feedback blocks force one-change geodesics

# Monotone feedback produces one-change geodesics

Let c be a binary coloring of ordered three-faces of Q_n, n>=4, with or without antipodal-reversal oddness. Fix a direction order p=(p_1,...,p_n). Write x_i for the initial bit in direction p_i, w_i(x) for window i's color, s=n-3, and d_i=w_i XOR w_{i+1}. A geodesic is good when at most one d_i equals 1.

## A finite Boolean fixed-point lemma

A Boolean function is unate in a variable if, with all other variables fixed, it is always nondecreasing in that variable or always nonincreasing. For a map f:{0,1}^m -> {0,1}^m whose coordinates are unate, draw i -> j when f_i depends on z_j. Give this edge sign + if the dependence is nondecreasing and - if it is nonincreasing; omit absent dependencies. Suppose every directed cycle has positive sign product. Then f has a fixed point.

Proof. Process strongly connected components of the dependency graph in reverse topological order, so all dependencies outside the current component have already been fixed. Restrictions retain the assigned signs and can only delete edges.

Within any strongly connected component C, the signs admit a coordinate-complement gauge. Indeed, choose a root r. Define eta_j as the sign product along a directed path from r to j. A directed return path from j to r exists. Appending the same return path to two root-to-j paths shows that their products agree, because every closed directed walk has positive product: decompose it into directed cycles. Thus eta_j is well-defined, and every edge i -> j has sign eta_i eta_j.

Set z_i=y_i when eta_i=+ and z_i=1-y_i when eta_i=-. Apply the same coordinate complements to the output f_i. The transformed block map T is nondecreasing in every input, since an edge's transformed sign is eta_i times its old sign times eta_j, which is +. Starting with y^(0)=0, iterate y^(t+1)=T(y^(t)). The first inequality is automatic, and monotonicity inductively gives y^(t)<=y^(t+1). At most |C| strict increases occur, so the sequence becomes stationary. Undoing the gauge gives a fixed point on C. For singleton components with no loop the output is constant and the same argument applies. Solving all components proves the lemma. QED.

## Theorem: monotone influence blocks

Choose J subset of [s] and an injection phi:J -> [n]. Put z_i=x_{phi(i)}. Suppose toggling z_i always complements d_i, for each i in J. Hence
  d_i(z,y)=z_i XOR f_i(z_{J minus {i}},y),
where y denotes the nonpivot initial bits and f_i is independent of z_i.

Draw i -> j, i!=j, when f_i depends on z_j, and let C range over the strongly connected components of this graph. Assume that, for every C and every fixed assignment of all initial bits outside z_C, the internal map (f_i)_{i in C} is unate in its internal variables and its signed dependency graph has no negative directed cycle. Then there is an initial vertex with d_i=0 for every i in J. In particular this order admits a geodesic with at most s-|J| color changes; it is good if |J|>=n-4, and monochromatic if J=[s].

Proof. Fix the nonpivot bits arbitrarily and process components C in reverse topological order. Every outside pivot affecting an equation in C belongs to an already solved component. Upstream pivots have no effect on the current block and may be assigned provisional values. The finite Boolean fixed-point lemma applied to the resulting internal map produces z_C=f_C(z_C), equivalent to d_i=0 for i in C. Subsequent upstream assignments leave these equations unchanged. After all components are processed, every controlled difference vanishes. Only s-|J| differences remain uncontrolled. QED.

Only the feedback dependencies within a component require unateness. Dependencies between distinct components may be arbitrary nonlinear functions.

## Corollary: negative cycles bound the remaining changes

Fix the nonpivot initial bits. Suppose the residual functions f_i are unate in all pivot variables, with signed dependency graph G. Let F subset of J meet every negative directed cycle of G. Then this order has a geodesic with at most
  s-|J|+|F|
changes.

Proof. Fix the pivots in F arbitrarily and discard their target equations. The remaining signed graph has no negative directed cycle; restrictions preserve unateness and edge signs. Apply the fixed-point lemma to the remaining residual map. The seams outside J and those in F account for the displayed bound. QED.

Thus when every seam has a distinct uniform pivot, a set of at most one seam meeting all negative directed cycles suffices for one-change closure. Positive feedback cycles can be retained.

## A face-valid nonlinear example beyond almost-complete surjectivity

Take n=9 and p=(1,2,3,4,5,6,7,8,9). Prescribe the seven window colors as functions of initial bits by
  w=(x_8, x_7 XOR x_5 x_6, x_8, x_1 XOR x_9,
     x_2 XOR x_9, x_1 XOR x_9, x_3).
Multiplication denotes Boolean AND. Each function is independent of the three free starting bits in its window. It therefore specifies an ordered-three-face color: when translating to fixed face bits, preceding directions have already been toggled.

The seven ordered triples are distinct and no one is the reverse of another. Assign their antipodal reversed partners the complementary colors and assign all remaining antipodal-reversal pairs arbitrarily. This extends the prescription to a full NORI coloring.

Its six differences are
  d_1=d_2=x_8 XOR x_7 XOR x_5 x_6,
  d_3=x_8 XOR x_1 XOR x_9,
  d_4=d_5=x_1 XOR x_2,
  d_6=x_1 XOR x_9 XOR x_3.
Use pivots
  (z_1,z_2,z_3,z_4,z_5,z_6)=(x_8,x_7,x_9,x_1,x_2,x_3).
The feedback components are {1,2}, {4,5}, {3}, and {6}. In {1,2}, after outside bits are fixed, both residual dependences are increasing if x_5 x_6=0 and decreasing if x_5 x_6=1. Their two-cycle is positive in either case. The component {4,5} has an increasing two-cycle. Singleton blocks have no internal dependence. The theorem therefore supplies a monochromatic geodesic.

Explicitly, choose x_1,x_8,x_4,x_5,x_6 freely, and set
  x_7=x_8 XOR x_5 x_6,
  x_2=x_1,
  x_9=x_8 XOR x_1,
  x_3=x_8.
All seven colors then equal x_8. There are exactly 32 monochromatic starts.

For any prescribed d satisfying d_1=d_2 and d_4=d_5, choose those same five free bits and solve the four displayed independent difference equations for x_7,x_2,x_9,x_3. Hence precisely 16 change vectors occur, each at 32 starts. Of these, exactly 0,e_3,e_6 have weight at most one, giving exactly 96 good starts.

Every choice of five among the six controlled seam outputs contains a duplicated pair. Such a five-output map is never surjective. Consequently the earlier acyclic or bijective-block certificates controlling at least n-4=5 seams cannot certify this specified order. The monotone fixed-point criterion controls all six seams despite the two nonbijective feedback components. The nonlinear term also places the complete starting-bit change map outside the affine theorem's hypotheses. An exhaustive check of the 512 starts confirmed the analytic counts; the argument above proves them.

## Scope and remaining obligation

The theorem is a full-dimensional sufficient condition, independent of antipodal symmetry. It does not prove that every NORI coloring admits such a direction order and pivot system. A counterexample must defeat this monotone-block criterion for every order and every almost-complete uniform-pivot matching. Failure of the criterion can occur either because uniform pivots are unavailable or because internal feedback has incompatible signs or genuinely nonunate dependence. Establishing a global order-selection theorem, or controlling these failures by face symmetry, remains necessary for the grand conjecture.
