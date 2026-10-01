# Above order fourteen anchored four-windows yield descent, order disagreement, or a Hamiltonian five-set

## Statement

Let H be a minimum counterexample of order n>=15, let W be a Hamiltonian four-vertex set, and let H-W=P|Q be a two-cover. Then at least one of the following holds: (1) W|P|Q admits a spanning three-cover of strictly smaller quadratic potential; (2) H contains explicit order disagreement between tight Hamilton paths on overlapping induced supports; (3) H contains a proper Hamiltonian five-vertex induced set S whose complement is non-Hamiltonian with path-cover number two.

## Body

Apply the certified cross-endpoint dichotomy 27a05b61e8c3.

In the checkerboard branch, because n>=15 at least one of P,Q has order at least six. The certified theorem 92c86d754e08 gives an explicit strict Phi-decreasing endpoint transfer. This is (1).

Now take the shared-endpoint branch. By 064902822993 there is a six-set U such that either U is non-Hamiltonian and Hamiltonian deletion paths of U exhibit order disagreement, giving (2), or U is Hamiltonian.

Assume U is Hamiltonian. Apply sharedendpointmigration_recomp01. In its first outcome there is a Hamiltonian four-set W' with |W intersect W'|=3; minimum-counterexample calculus gives H-W' non-Hamiltonian with path-cover number two. In its second outcome there are two Hamiltonian four-sets W_1,W_2, each with non-Hamiltonian path-cover-two complement and |W_1 intersect W_2|=3. Thus in either case we obtain two distinct Hamiltonian four-sets A,B whose complements are non-Hamiltonian with path-cover number two and |A intersect B|=3.

Put S=A union B, so |S|=5. Apply the certified overlap theorem d9a4b66724d2. If H[S] is Hamiltonian, then S is proper and minimum-counterexample calculus gives a non-Hamiltonian complement of path-cover number two, giving (3). Otherwise at least four of the five four-subsets S-{s} are Hamiltonian. Since H[S] is non-Hamiltonian, apply astra004fourgooddisagree to four such deletion labels and arbitrary Hamilton paths on their deletions. It forces order disagreement between two of those Hamilton paths, giving (2).

These cases prove the stated trichotomy.
