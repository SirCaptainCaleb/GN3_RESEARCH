# Rooted seven-set Hamiltonian shell graph

## Statement

Let W=A disjoint-union {r} be a seven-vertex boundary tournament with |A|=6. Define a graph G on A by joining distinct a,b when H[{r} union (A-{a,b})] is Hamiltonian. Then delta(G)>=3 and e(G)>=9. Consequently G has a Hamilton cycle and a perfect matching.

## Body

# Rooted seven-set Hamiltonian shell graph

Let W=A disjoint-union {r} be a seven-vertex boundary tournament with |A|=6. Define a graph G on A by joining distinct vertices a,b exactly when the five-set

{r} union (A-{a,b})

is Hamiltonian.

Then

delta(G)>=3

and therefore e(G)>=9. Moreover G has a Hamilton cycle and, by taking alternate cycle edges, a perfect matching.

## Proof

Fix a in A and consider the six-set

U=W-{a}={r} union (A-{a}).

By the four-of-six theorem, at least four of the six five-vertex deletions of U are Hamiltonian.

One of these six deletions is obtained by deleting r, giving the five-set A-{a}. Whether or not that set is Hamiltonian, at least three of the remaining five deletions must be Hamiltonian.

For b in A-{a}, deleting b from U gives exactly

{r} union (A-{a,b}).

Thus at least three vertices b are adjacent to a in G. Since a was arbitrary, delta(G)>=3.

The handshake lemma gives

e(G)>=6*3/2=9.

Finally G has six vertices and minimum degree at least 6/2. Dirac's theorem gives a Hamilton cycle. The alternating edges of that six-cycle form a perfect matching. ∎

The lemma is deliberately root-agnostic: it is a direct shell consequence of four-of-six and can replace any use of the older rooted seven-set assertion embedded in the stale extremal omnibus.
