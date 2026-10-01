# Endpoint covers of a longest path force double crossing or disagreement

## Statement

Let H be a boundary tournament with pc(H)>2 and let A=(a_0,...,a_m), m>=3, be a globally longest tight path, with U=V(H)-V(A). Choose arbitrary exact two-covers of H-a_0 and H-a_m. Then either one of these covers has at least two ordinary edges crossing the cut between the surviving vertices of A and U, or the two endpoint probes expose explicit support/order disagreement. More precisely, if both endpoint covers have exactly one cut crossing, maximality of A forces the attached U-block in each cover to be a singleton. If the two singleton labels differ, the induced exact two-covers u|(U-u) and v|(U-v) have different support partitions; if the labels agree, the two-sided endpoint-replacement theorem on A together with that common exterior vertex forces relative-order disagreement. Thus a globally longest path has no featureless one-crossing endpoint branch.

## Body

# Endpoint covers of a longest path force double crossing or disagreement

Let H be a boundary tournament with pc(H)>2. Let
A=(a_0,a_1,...,a_m),  m>=3,
be a globally longest tight path, of order lambda=m+1, and put
U=V(H)-V(A).

Choose arbitrary exact two-covers
G_0 of H-a_0
and
G_m of H-a_m.

For either endpoint deletion, the surviving lambda-1 vertices of A form a Hamiltonian set, and A itself is Hamiltonian. The crossing-forced lemma therefore says that every exact two-cover of the endpoint deletion has at least one ordinary edge between the surviving A-vertices and U.

Suppose one of G_0,G_m has at least two such crossing edges. This is the first conclusion.

It remains to assume that both covers have exactly one crossing edge.

Cut the unique crossing edge of G_0. The unique-crossing block count gives exactly one path block B_0 on all lambda-1 surviving vertices A-{a_0}, and exactly two nonempty path blocks in U. One of those U-blocks is joined to B_0 in the mixed component of G_0; call it R_0.

The mixed component has order
(lambda-1)+|R_0|.
Because A is globally longest, every tight path has order at most lambda. Hence |R_0|<=1. Since R_0 is nonempty, R_0={u} is a singleton.

Thus G_0 consists of

- a Hamilton path L on (A-{a_0}) union {u}, and
- a Hamilton path S on U-{u}.

No assumption on the order of L is needed.

The same argument at a_m gives a vertex v in U such that G_m consists of

- a Hamilton path R on (A-{a_m}) union {v}, and
- a Hamilton path T on U-{v}.

Equivalently, cutting the unique crossing edges produces exact two-covers of H[U]
(u)|(U-{u})
and
(v)|(U-{v}).

If u!=v, these two exact U-covers have different unordered support partitions. The exact-cover disagreement theorem therefore gives reciprocal support-crossing edges inside U.

Assume u=v. Put X=V(A) and y=u. Since A is globally longest, H[X union {y}] is non-Hamiltonian. But we have

- the Hamilton path A on X;
- the Hamilton path L on (X-{a_0}) union {y}; and
- the Hamilton path R on (X-{a_m}) union {y}.

The two-sided endpoint-replacement theorem applies and forces two of A,L,R to disagree on the relative order of common vertices. The path-intersection theorem then yields a reversed common edge, a reversing tight triple, or a vertex-simple tight cycle.

Therefore arbitrary endpoint probes of a globally longest path have only two outcomes:

1. one endpoint deletion cover has at least two ordinary crossings between the surviving longest-path vertices and the complement; or
2. the two endpoint probes expose explicit support or relative-order disagreement.

In particular there is no one-crossing/no-disagreement endpoint branch at all. ∎
