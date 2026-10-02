# Opposite endpoint covers in the sharp half-order shell are position-locked odd weaves or force bridge disagreement

## Statement


Let H be a minimum counterexample in the sharp half-order shell |V(H)|=2lambda+1, and let A=(a_0,...,a_{lambda-1}) be globally longest. For any exact cover of either endpoint deletion, either there is relative-order disagreement among surviving A-vertices or a tight triple reversing an ordered edge of A, or every surviving a_i occurs at its original position i in its component. In this neutral case the two components are positionwise complementary across the A|U cut and the crossing number is 1+2 times the number of ownership changes, hence odd. If arbitrary exact covers are chosen at both endpoints and neither already has ordered disagreement, then a_{lambda-1} is terminal in the left cover and a_0 is initial in the right cover; endpoint-state trichotomy excludes both internal restoration and clean omission swap, so the two induced covers of H-{a_0,a_{lambda-1}} exhibit bridge disagreement, yielding support crossing or explicit order disagreement.


## Body


# Opposite endpoint covers in the sharp half-order shell are position-locked odd weaves or force bridge disagreement

Let H be a minimum counterexample in the sharp half-order shell
|V(H)|=2lambda+1,
where lambda is the maximum tight-path order. Let
A=(a_0,...,a_{lambda-1})
be globally longest and put U=V(H)-V(A).

## Position locking at one endpoint

Take any exact two-cover T of H-a_0. Both components have order lambda.

If two surviving A-vertices occurring in one T-component appear in a different relative order from A, path-intersection calculus gives the standard reversed-edge, reversing-triple, or tight-cycle witness. Assume no such disagreement.

Let a_i, 1<=i<=lambda-1, occur at position p in its component C=(c_0,...,c_{lambda-1}). If p<i, let z=c_{p+1}. By inherited A-order, the A-prefix through a_{i-1} is disjoint from the C-suffix beginning a_i,z. All triples in
(a_0,...,a_i,z,c_{p+2},...,c_{lambda-1})
are inherited from A or C except possibly (a_{i-1},a_i,z). If this triple were tight, the displayed path would have order lambda+(i-p)>lambda. Hence it is non-tight and
(z,a_i,a_{i-1})
is tight, explicitly reversing the ordered edge (a_{i-1},a_i).

Similarly, if p>i, with y=c_{p-1}, the only unchecked triple in
(c_0,...,y,a_i,a_{i+1},...,a_{lambda-1})
is (y,a_i,a_{i+1}). Tightness would again create a path longer than lambda, so
(a_{i+1},a_i,y)
is tight and reverses an A-edge.

Therefore, absent relative-order disagreement or an explicit reversing triple,
p=i
for every surviving a_i.

Hence neither T-component has an A-vertex at position 0, while for each position i>=1 exactly one component contains a_i and the other contains a U-vertex. Let x_i indicate which component owns a_i. Between positions 0 and 1 exactly one component crosses the A|U cut. At every later step both components cross exactly when ownership changes. Thus the total crossing number is
t=1+2 |{i in {1,...,lambda-2}: x_i != x_{i+1}}|.
It is odd. The one-crossing case is the constant ownership word; every nonconstant neutral state has at least three crossings.

The symmetric right-end statement holds for H-a_{lambda-1}: absent disagreement, each surviving a_i occurs at position i, both terminal positions lie in U, and the crossing count is odd.

## Opposite neutral endpoint covers force bridge disagreement

Choose arbitrary exact covers T_L of H-a_0 and T_R of H-a_{lambda-1}. Suppose neither has relative-order disagreement or a reversing triple against A.

Position locking makes a_{lambda-1} the terminal endpoint of its component in T_L and a_0 the initial endpoint of its component in T_R.

Apply the endpoint-state trichotomy to T_L with omitted vertex x=a_0, endpoint y=a_{lambda-1}, and choose C_y=T_R as the exact cover of H-y.

The internal-restoration branch is impossible because x=a_0 is an endpoint, not an internal vertex, of T_R.

Suppose the clean omission-swap branch held. Delete y from T_L, obtaining an ordered exact two-cover T_y of H-{a_0,a_{lambda-1}}. Restoring y recovers T_L at the terminal end of its component. Clean swap would require restoring x=a_0 in T_R at the same end of the same ordered component of T_y. Thus a_0 would be terminal in its T_R-component. But position locking makes it initial. Exact deletion-cover components have order at least three, so the two endpoints are distinct. Contradiction.

Therefore only bridge disagreement remains: deleting a_0 from T_R gives a different ordered exact two-cover of the common two-deletion graph from the cover obtained by deleting a_{lambda-1} from T_L. The exact-cover disagreement theorem gives either support-partition crossing or, on a common support, a reversed common edge, reversing tight triple, or vertex-simple tight cycle.

Thus opposite endpoint covers cannot both remain featurelessly order-neutral. Neutral endpoint states are rigid odd weaves, and comparing the two ends necessarily exports a concrete bridge disagreement.
