# Four Hamiltonian vertex deletions force order disagreement in every non-Hamiltonian set

## Statement

Let K be a finite non-Hamiltonian boundary tournament, and let D be a set of at least four vertices such that K-d is Hamiltonian for every d in D. For each d in D choose an arbitrary Hamilton tight path P_d on K-d. Then some two paths P_d,P_e order two common vertices differently. Consequently the path-intersection calculus yields a reversed common ordered edge, a tight triple reversing an ordered edge at an intersection, or a vertex-simple tight cycle.

## Body

# Proof

Assume for contradiction that every pair P_d,P_e induces the same relative order on their common vertices.

Define a binary order on V(K). For distinct u,v choose d in D-{u,v}, possible because |D|>=4, and declare u<v exactly when u precedes v on P_d. This is well-defined: any second choice e in D-{u,v} gives the same comparison by the assumed pairwise compatibility.

For any three distinct u,v,w, choose d in D-{u,v,w}, again possible because |D|>=4. The three pairwise comparisons among u,v,w then agree with their order on the linear path P_d. Hence the global binary relation is transitive on every triple and therefore is a total linear order on V(K).

Write this order as v_0<...<v_{m-1}. Fix any three consecutive vertices v_i,v_{i+1},v_{i+2}. Choose d in D-{v_i,v_{i+1},v_{i+2}}. Since P_d induces the global relative order on all vertices except d, and the chosen three are consecutive in the global order, they are also consecutive on P_d. Therefore (v_i,v_{i+1},v_{i+2}) is tight.

This holds for every i, so (v_0,...,v_{m-1}) is a Hamilton tight path of K, contradicting the assumption that K is non-Hamiltonian. Thus some pair P_d,P_e has genuine relative-order disagreement. The standard path-intersection conclusion gives the stated reversed-edge / reversing-triple / tight-cycle witness. ∎
