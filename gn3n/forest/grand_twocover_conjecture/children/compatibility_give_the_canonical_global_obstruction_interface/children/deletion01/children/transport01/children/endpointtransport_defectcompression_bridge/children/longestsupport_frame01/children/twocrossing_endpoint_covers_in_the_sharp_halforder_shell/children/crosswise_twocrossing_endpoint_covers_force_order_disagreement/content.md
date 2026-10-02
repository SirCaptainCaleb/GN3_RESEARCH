# Crosswise two-crossing endpoint covers force order disagreement

## Statement

Let H be a minimum counterexample with |V(H)|=2lambda+1 and maximum tight-path order lambda. Let A=(a_0,...,a_{lambda-1}) be a globally longest path, U=V(H)-V(A), and let T be an exact two-cover of H-a_0 having exactly two ordinary edges across (A-{a_0})|U. Then either T is the singleton internal-exchange shape of c8d4f2197a61, or its crosswise four-block shape exposes explicit relative-order disagreement with A: a reversed common edge, a tight triple reversing an ordered edge of A, or a vertex-simple tight cycle. Thus the crosswise equality shape cannot remain order-compatible with the original longest path.

## Body

# Crosswise two-crossing endpoint covers force order disagreement

Let H be a minimum counterexample with |V(H)|=2 lambda+1, where lambda is the maximum tight-path order. Let

A=(a_0,...,a_{lambda-1})

be globally longest and put U=V(H)-V(A). Let T be an exact two-cover of H-a_0 with exactly two ordinary edges across (A-{a_0})|U.

By c8d4f2197a61, either T is the singleton internal-exchange shape

(B_1,u,B_2) | (U-{u}),

or T is crosswise: its two components C_1,C_2 each consist of one nonempty A-block and one nonempty U-block joined by their unique crossing edge. Both components have order exactly lambda.

Assume T is crosswise. Fix one component C and let B_C be its A-block. If its A-vertices occur in a different relative order from A, pathcalc01 already gives a reversed common edge, reversing tight triple, or vertex-simple tight cycle. Hence suppose B_C preserves the inherited A-order.

Write k for the least A-index in B_C and j for the greatest. Since a_0 is omitted, k>=1.

If B_C comes first in C, then C begins at a_k. Write z for the next vertex of C. If k=1, tightness of (a_0,a_1,z) would make (a_0,C) a tight path of order lambda+1, impossible. Hence (z,a_1,a_0) is tight and reverses the ordered edge (a_0,a_1) of A.

If k>=2, prepend the inherited prefix (a_0,...,a_{k-1}) to C. The prefix is disjoint from C by minimality of k. Every consecutive triple is inherited from A or C except possibly (a_{k-1},a_k,z). If that triple were tight, the concatenation would have order lambda+k>lambda. Therefore (z,a_k,a_{k-1}) is tight, reversing the ordered edge (a_{k-1},a_k).

Thus an inherited-order A-block occurring first always gives explicit order disagreement.

Now suppose B_C comes last in C. Then C ends at a_j; let y be its predecessor in C. If j<lambda-1, append the inherited suffix (a_{j+1},...,a_{lambda-1}). Every new triple is inherited except possibly (y,a_j,a_{j+1}). If it were tight, the resulting path would be longer than lambda. Hence (a_{j+1},a_j,y) is tight, reversing the ordered edge (a_j,a_{j+1}). Therefore an inherited-order A-block can occur last without disagreement only if j=lambda-1.

Finally suppose the whole crosswise cover exposes no order disagreement. Neither A-block can occur first, so both occur last. Each must then end at a_{lambda-1}. But the two A-blocks are disjoint and partition A-{a_0}, so they cannot both contain a_{lambda-1}. Contradiction.

Hence every crosswise exact-two-crossing endpoint cover exposes explicit relative-order disagreement with A. Combined with c8d4f2197a61, every exact two-crossing endpoint cover is either the singleton internal exchange or supplies ordered reversal/cycle data against the original longest path. ∎

## Route consequence

The exact-two-crossing endpoint branch is no longer a support-only residue in the general sharp half-order shell. The only featureless two-crossing residue is the singleton internal exchange.