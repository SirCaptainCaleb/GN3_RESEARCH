# Two neutral 3|5 rotations perform a controlled two-for-two support exchange

**Summary:** At a Phi-minimal 3|5 state T|C, two successive neutral endpoint rotations replace the 3-side T={t1,t2,w} by a 3-path on {w,c1,c5} and the 5-side C=(c1,...,c5) by a 5-path on {t1,t2,c2,c3,c4}, for suitable t1,t2 in T. Thus the neutral dynamics exchange two 3-side vertices with the two displayed endpoints of the 5-side while retaining one 3-side vertex.

## Statement

Let H be a minimum counterexample and let T|C be two components of a Phi-minimal spanning three-cover, where |T|=3 and C=(c_1,c_2,c_3,c_4,c_5). Then there exist distinct t_1,t_2,w in V(T) and a sequence of two equal-Phi pairwise repartitions, staying in the same repartition component, which transforms the displayed pair into U|L where U is a tight 3-path on {w,c_1,c_5} and L is a tight 5-path on {t_1,t_2,c_2,c_3,c_4}.

## Body

Because the state is Phi-minimal, three_vertex_component_long_neighbor_rotation01 implies that T union {c_1} and T union {c_5} are both non-Hamiltonian. Apply the controlled two-bad-four-extensions lemma from localextend01 to the tight three-path T and the exterior vertices c_1,c_5. It yields a Hamiltonian five-path K on

V(T) union {c_1,c_5}

whose two endpoints both lie in V(T). Let those endpoints be t_1,t_2 and write w for the third vertex of T. The complementary interior path

C^o=(c_2,c_3,c_4)

is tight, so replacing T|C by K|C^o is a legal pairwise repartition of profile 3|5 -> 5|3. Its Phi change is zero.

The new state is therefore also Phi-minimal. View the displayed pair now as C^o|K, with C^o the 3-side and K the 5-side. At a Phi-minimum, neither endpoint of K can Hamiltonian-extend C^o, because such an extension would give the strict 3|5 -> 4|4 descent. Thus C^o union {t_1} and C^o union {t_2} are both non-Hamiltonian.

Apply the same controlled two-bad-four-extensions lemma again, now to the tight three-path C^o and exterior vertices t_1,t_2. It gives a Hamiltonian five-path L on

{c_2,c_3,c_4,t_1,t_2}

whose endpoints lie in {c_2,c_3,c_4}. The complementary path in K is its interior after deleting the endpoints t_1,t_2 of K. Since K has vertex set {t_1,t_2,w,c_1,c_5} and endpoints t_1,t_2, this interior is a tight three-path U with vertex set

{w,c_1,c_5}.

Hence the second equal-Phi pairwise repartition changes C^o|K to L|U. Overall, two neutral rotations exchange the pair {t_1,t_2} from the old 3-side with the endpoint pair {c_1,c_5} of the old 5-side, while the vertex w remains on the 3-side and the interior triple {c_2,c_3,c_4} moves to the 5-side.

## Metadata

- ID: toolkit_35_rotations_perform_a_controlled_two_for_two_support_exchange
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
