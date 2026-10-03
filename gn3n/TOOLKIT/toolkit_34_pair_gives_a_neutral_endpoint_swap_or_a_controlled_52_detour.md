# A 3|4 pair gives a neutral endpoint swap or a controlled 5|2 detour

**Summary:** For a tight 3-path T beside a tight 4-path C, either one endpoint of C Hamiltonian-extends T, giving an equal-Phi 3|4 to 4|3 repartition, or both endpoint extensions are non-Hamiltonian and the two-bad-four-extension theorem gives a 5|2 repartition whose 5-path has both endpoints in T.

## Statement

Let H be a boundary tournament and let T|C be two components of a path cover, with |T|=3 and C=(c_1,c_2,c_3,c_4). Then either (i) T union {c_1} or T union {c_4} is Hamiltonian, yielding a pairwise repartition with orders (4,3) and no change in quadratic potential, or (ii) both endpoint four-extensions are non-Hamiltonian, in which case there is a pairwise repartition with orders (5,2), where the 5-path has vertex set V(T) union {c_1,c_4} and both its endpoints lie in V(T), while the 2-path is (c_2,c_3).

## Body

If T union {c_1} is Hamiltonian, let K be a Hamilton path on that four-set. Then K|(c_2,c_3,c_4) is a two-cover of V(T) union V(C), with orders (4,3). The same holds using c_4 and the inherited prefix (c_1,c_2,c_3). Since 4^2+3^2=3^2+4^2, this is Phi-neutral.

Assume both T union {c_1} and T union {c_4} are non-Hamiltonian. Apply the controlled two-bad-four-extensions lemma in localextend01 to the tight three-path T and exterior vertices c_1,c_4. It produces a Hamiltonian five-path K on V(T) union {c_1,c_4}, with both endpoints in V(T). The complementary pair (c_2,c_3) is a tight path of order two. Hence K|(c_2,c_3) is a legal pairwise repartition of T|C with orders (5,2).

Thus every 3|4 pair has exactly the useful local menu: neutral endpoint swap, or controlled 5|2 detour with the two-path equal to the displayed interior edge of C.

## Metadata

- ID: toolkit_34_pair_gives_a_neutral_endpoint_swap_or_a_controlled_52_detour
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
