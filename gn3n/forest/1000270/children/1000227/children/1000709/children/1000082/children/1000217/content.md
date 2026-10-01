# Large minimum deletion side excludes complements of order at most six

## Statement

Let H be a minimum counterexample and let mu be the minimum smaller-component order among all exact two-covers of all one-vertex deletions. If mu>=6, then no tight path of H has a non-Hamiltonian complement of order 4, 5, or 6.

## Body

# Large minimum deletion side excludes complements of order at most six

Let H be a minimum counterexample, and let

mu = min_y min_{A|B exact two-cover of H-y} min{|A|,|B|}.

Assume mu>=6.

We claim that no tight path P of H can have a non-Hamiltonian complement F of order 4, 5, or 6.

Suppose such P and F exist. In each of the three possible orders, there is a vertex z in F for which F-{z} is Hamiltonian:

- if |F|=4, every three-vertex boundary tournament is Hamiltonian;
- if |F|=5, the non-Hamiltonian five-set theorem gives at least four Hamiltonian four-vertex deletions;
- if |F|=6, the four-of-six theorem gives at least four Hamiltonian five-vertex deletions.

Choose such z. Then P and a Hamilton path on F-{z} are vertex-disjoint tight paths whose supports partition V(H)-{z}. Hence they form a two-path cover of H-z.

Because H is a minimum counterexample, H-z is non-Hamiltonian; otherwise a Hamilton path of H-z together with the singleton (z) would two-cover H. Therefore the displayed cover is exact.

Its smaller component has order at most |F|-1<=5, contradicting mu>=6.

Thus every non-Hamiltonian complement of a tight path has order at least seven whenever mu>=6. ∎

## Consequence for a trapped one-defect state

By the one-defect/deletion-cover equivalence, a minimum D=1 state has deficient-support size delta=mu+1. Therefore any trapped minimum one-defect state with mu>=6 automatically lies outside the codimension-four, five-complement, and six-complement frontiers. Any maximin or transport reduction in such a trapped state must land at complement order at least seven.
