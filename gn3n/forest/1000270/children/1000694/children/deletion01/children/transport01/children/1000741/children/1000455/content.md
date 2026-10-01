# Two two-crossing endpoint covers force order disagreement or a longest-support square

## Statement

Let H be a minimum counterexample in the sharp half-order shell |V(H)|=2lambda+1 with lambda>=6, let A=(a_0,...,a_{lambda-1}) be globally longest, and put U=V(H)-V(A). Choose deletion covers of H-a_0 and H-a_{lambda-1}, each having exactly two ordinary crossings across the surviving-A | U cut. Then either the endpoint data expose explicit order disagreement, or the two covers are singleton internal exchanges using distinct labels u,v in U and S=(V(A)-{a_0,a_{lambda-1}}) union {u,v} is Hamiltonian. In the latter case A, A-a_0+u, S, and A-a_{lambda-1}+v form a four-cycle in the Johnson graph on Hamiltonian lambda-supports, and V(H)-S is non-Hamiltonian with path-cover number exactly two.

## Body

Apply 4cd0c6fd1e31 to the cover of H-a_0. If it is in the crosswise four-block case, that theorem already yields explicit order disagreement with A. Otherwise c8d4f2197a61 gives the singleton internal-exchange form
L | (U-{u}),
where L is Hamiltonian on (V(A)-{a_0}) union {u}.

For the cover of H-a_{lambda-1}, the block-count classification of c8d4f2197a61 applies directly with B=A-{a_{lambda-1}}: its proof uses only that B is Hamiltonian, U is non-Hamiltonian with path-cover number two, both cover components have order at most lambda, and there are exactly two B-U crossings. Thus this cover is either crosswise or has singleton internal-exchange form
R | (U-{v}),
where R is Hamiltonian on (V(A)-{a_{lambda-1}}) union {v}.

It remains to show directly, without reversing A, that a crosswise terminal-end cover exposes order disagreement. Consider one crosswise component C and its nonempty A-block B_C. If its A-vertices already occur in a different relative order from A, we are done. Otherwise write k for the least A-index in B_C and j for the greatest. Since a_{lambda-1} is omitted, j<=lambda-2.

If B_C occurs last in C, then C ends at a_j. Let y be the predecessor of a_j in C. Appending the inherited suffix (a_{j+1},...,a_{lambda-1}) would make a path longer than lambda if (y,a_j,a_{j+1}) were tight. Hence (a_{j+1},a_j,y) is tight, reversing the ordered edge (a_j,a_{j+1}) of A. Thus an inherited-order A-block occurring last always gives order disagreement.

If B_C occurs first in C and k>0, then C begins at a_k. Let z be the next vertex of C. Prepending the inherited prefix (a_0,...,a_{k-1}) would make a path longer than lambda if (a_{k-1},a_k,z) were tight. Hence (z,a_k,a_{k-1}) is tight, reversing the ordered edge (a_{k-1},a_k). Thus an inherited-order A-block can occur first without disagreement only when k=0.

Therefore, if a terminal-end crosswise cover exposed no order disagreement, both of its disjoint A-blocks would have to occur first and both would have to contain a_0, impossible. Thus every crosswise terminal-end cover also exposes order disagreement.

We may now assume both endpoint covers are singleton internal exchanges, namely L | (U-{u}) for H-a_0 and R | (U-{v}) for H-a_{lambda-1}. If either L or R fails to preserve the inherited relative order of its common A-vertices, we again have order disagreement. Hence assume both preserve the A-order.

Suppose first that u=v. Since A is globally longest, A union {u} is non-Hamiltonian. The two-sided endpoint-replacement theorem in insert01 applies to A and the common exterior label u. It forces order disagreement among A,L,R. The A-L and A-R comparisons are order-preserving by assumption, so the remaining L-R comparison supplies explicit order disagreement.

We may therefore assume u!=v. Apply a69b11eefede to A,L,R. Since lambda>=6, the set
S=(V(A)-{a_0,a_{lambda-1}}) union {u,v}
has a Hamilton tight path.

Put
A_L=(V(A)-{a_0}) union {u},
A_R=(V(A)-{a_{lambda-1}}) union {v}.
Then A,A_L,S,A_R are four Hamiltonian lambda-subsets and consecutive sets differ by one exchange:
A -> A_L exchanges a_0 for u,
A_L -> S exchanges a_{lambda-1} for v,
S -> A_R exchanges u for a_0,
A_R -> A exchanges v for a_{lambda-1}.
Hence they form a four-cycle in the Johnson graph.

Finally let
T=V(H)-S=U-{u,v}+{a_0,a_{lambda-1}}.
If T were Hamiltonian, Hamilton paths on S and T would form a spanning two-cover of H, impossible. Thus T is non-Hamiltonian. Since T is a proper induced subtournament of the minimum counterexample, mincex01 gives pc(T)<=2. Therefore pc(T)=2.

So the paired two-crossing endpoint branch has only two outcomes: explicit order disagreement, or a commuting square of longest Hamiltonian supports whose opposite complement is non-Hamiltonian and has path-cover number exactly two. ∎
