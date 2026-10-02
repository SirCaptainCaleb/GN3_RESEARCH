# Every full two-label path-cover-two square has a top-cover normal form

**Summary:** Every full two-label path-cover-two square has a top-cover normal form.

## Statement

Let G be a boundary tournament and let d,e be distinct vertices of G. Suppose G, G-d, G-e, and G-{d,e} are all non-Hamiltonian and have path-cover number two. Then at least one of the following holds. (1) Some two-cover F of G has both d and e as displayed endpoints; deleting either or both gives two-covers of the three lower square states. (2) One of d,e is internal in every two-cover of G. (3) Two two-covers of G have different unordered support partitions. (4) Two Hamilton paths on one common component support of two covers of G order some common pair differently.

## Body

The proof is the top-state argument of square_topcover_normal01 with its unused ambient-core hypothesis removed. If some two-cover F of G has both d and e as displayed endpoints, neither d nor e can form a singleton component because G-e or G-d is non-Hamiltonian, and {d,e} cannot itself be a component because G-{d,e} is non-Hamiltonian. Hence deleting d, e, or both from their displayed endpoint positions preserves two nonempty tight paths and yields outcome (1). Now assume no two-cover has both labels as endpoints. Every two-cover therefore has at least one of d,e internal. If one label is internal in every two-cover, outcome (2) holds. Otherwise choose F with d an endpoint, hence e internal, and F' with e an endpoint, hence d internal. If their unordered support partitions differ, outcome (3) holds. If the support partitions agree, look at the common support class containing d. Its Hamilton path in F has d at an endpoint, while its Hamilton path in F' has d internal. The two linear orders are different, so some common pair occurs in opposite relative order, giving outcome (4). No Hamiltonian core, minimum-counterexample hypothesis, or ambient complement is used.

## Metadata

- ID: pc2_square_topcover_normal01
- Kind: toolkit
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
