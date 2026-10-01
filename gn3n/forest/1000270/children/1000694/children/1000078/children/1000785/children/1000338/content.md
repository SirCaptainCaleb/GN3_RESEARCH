# A nonescaping anchored four-window upgrades to a Hamiltonian five-window

## Statement

Let H be a minimum counterexample of order at least fifteen and let W be a Hamiltonian four-set such that H-W is non-Hamiltonian with path-cover number two. Then at least one of the following holds: (1) the anchored three-cover admits a strict quadratic-potential descent; (2) explicit relative-order disagreement occurs; or (3) H contains a Hamiltonian five-set S such that H-S is non-Hamiltonian with path-cover number two. Thus bounded four-window migration is not a separate neutral frontier: outside descent and order disagreement it amplifies to a Hamiltonian five-window.

## Body

Apply 7edbab77ddf9. Its first two alternatives are exactly (1) and (2). Otherwise there is a five-set S containing at least two anchored Hamiltonian four-windows with three-vertex intersection, and either H[S] is Hamiltonian or at least four of the five four-subsets of S are Hamiltonian anchored four-windows. Suppose the latter occurs while H[S] is non-Hamiltonian. Then S has at least four Hamiltonian vertex deletions. By the certified four-good-deletion theorem astra004fourgooddisagree, arbitrary Hamilton paths on four such deletions cannot all induce the same relative order on their common vertices; explicit relative-order disagreement follows, giving (2). Therefore, outside (2), H[S] must be Hamiltonian. Since S is proper, minimum-counterexample minimality gives path-cover number at most two for H-S. If H-S were Hamiltonian, a Hamilton path on S together with one on H-S would two-cover H, impossible. Hence H-S is non-Hamiltonian with path-cover number two, giving (3).
