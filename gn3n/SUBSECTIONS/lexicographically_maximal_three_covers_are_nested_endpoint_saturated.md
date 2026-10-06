# Lexicographically maximal three-covers are nested endpoint-saturated

## Metadata

- ID: lexicographically_maximal_three_covers_are_nested_endpoint_saturated
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 192
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Lexicographically maximal three-covers have nested endpoint saturation

Let H be a minimum-order counterexample.

Choose a spanning three-cover
A | B | C
whose sorted component-size triple
(|A|,|B|,|C|)
with |A|>=|B|>=|C| is lexicographically maximal among all spanning three-covers of H.

Write displayed Hamilton orders
A=(a_1,...,a_r), B=(b_1,...,b_s), C=(c_1,...,c_t).

1. A is a globally largest proper Hamiltonian support.

For any proper Hamiltonian support K, minimum-counterexample calculus gives pc(H-K)=2. Hence K appears as one component of a spanning three-cover, so |K|<=|A| by lexicographic maximality.

2. Endpoints of B and C cannot enlarge A.

Let z be a displayed endpoint of B or C. If A+z were Hamiltonian and the old component containing z had another vertex, deleting the endpoint z leaves an inherited tight path, and moving z into A yields a three-cover with largest component |A|+1, contradiction. If that old component were the singleton {z}, then A+z together with the remaining component would two-cover H.

Thus A+z is non-Hamiltonian. Endpoint insertion fails at both ends of A, so
h(a_2,a_1,z)=1 and h(z,a_r,a_{r-1})=1.

3. Endpoints of C cannot enlarge B.

Let z be an endpoint of C. If B+z were Hamiltonian and C-z nonempty, then
A | (B+z) | (C-z)
has a lexicographically larger sorted profile: the largest component remains at least |A| and the second component is at least |B|+1. If C={z}, then A | (B+z) is a two-cover. Both are impossible.

Thus B+z is non-Hamiltonian, and
h(b_2,b_1,z)=1 and h(z,b_s,b_{s-1})=1.

Hence each endpoint z of C simultaneously reverses all four displayed end edges of A and B:
h(a_2,a_1,z)=h(z,a_r,a_{r-1})=h(b_2,b_1,z)=h(z,b_s,b_{s-1})=1.

So a lexicographically maximal spanning three-cover is nested endpoint-saturated: the smallest path is trapped outside both larger paths, while the middle and smallest paths are trapped outside the largest.

No small-order bound, cyclic rotation, path reversal, or computation is used.
