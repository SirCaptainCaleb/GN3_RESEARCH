# The one-split interior pivots reach the five-complement frontier or cross-core c-transport

## Statement

In the interior-pivot branch of compattogglecross33, put W={c,u_i,u_{i+1},v_j,v_{j+1}}. Then exactly the certified central-five-set dichotomy from transport01 applies: either W is Hamiltonian, in which case H-W is non-Hamiltonian of path-cover number two, or at least one of the reverse cross-core triples (v_{j+1},c,u_i) and (u_{i+1},c,v_j) is tight. Thus the one-split residue reaches either the five-complement frontier or an explicit cross-core transport of the common switching label c.

## Body

# Proof

The interior second-type pivots on the deletion cover

H-c = A | B

have gaps u_i|u_{i+1} and v_j|v_{j+1}. By the second-type pivot relations, failed insertion across those gaps gives the native reverse triples

(u_{i+1},c,u_i)
and
(v_{j+1},c,v_j)

tight.

Consider the central five-set

W={c,u_i,u_{i+1},v_j,v_{j+1}}.

The certified central-five-set closure theorem in transport01 says that if both forward cross-join triples

(u_i,c,v_{j+1})
and
(v_j,c,u_{i+1})

are tight, then H[W] is Hamiltonian.

If H[W] is Hamiltonian, W is a proper subset of the minimum counterexample H. Its complement H-W cannot be Hamiltonian, since two disjoint Hamilton paths on W and H-W would form a spanning two-cover. Minimality therefore gives pc(H-W)=2.

If W is not Hamiltonian, the two forward cross-joins cannot both be tight. Boundary antisymmetry then implies that at least one of their reverses

(v_{j+1},c,u_i),
(u_{i+1},c,v_j)

is tight.

Hence the interior one-split double-pivot branch reaches one of two explicit interfaces: a Hamiltonian five-set with non-Hamiltonian pc-two complement, or a cross-core tight triple transporting c between the two pivot neighborhoods.
