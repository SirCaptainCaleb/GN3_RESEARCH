# Any two-vertex component beside a path of order at least four strictly descends

**Summary:** In any boundary tournament, a path cover containing components of orders 2 and s>=4 admits a pairwise repartition to orders 3 and s-1. Hence quadratic potential drops by 2s-6. In particular, every three-cover of a minimum counterexample containing a two-vertex component has a strict Phi-decreasing move.

## Statement

Let H be any boundary tournament and let U|C be two components of a path cover, where |U|=2 and C=(c_1,...,c_s) is a tight path with s>=4. Then U union V(C) has a two-path cover with component orders 3 and s-1. Consequently the quadratic potential changes by (3^2+(s-1)^2)-(2^2+s^2)=6-2s<0. Therefore every spanning three-cover of a minimum counterexample that contains a component of order two admits a strict pairwise Phi-decrease.

## Body

Write U={u,v} and C=(c_1,...,c_s). By boundary antisymmetry, exactly one of (u,c_1,v) and (v,c_1,u) is tight. Thus the three-set {u,v,c_1} has a tight Hamiltonian path T of order three. The inherited suffix C'=(c_2,...,c_s) is a tight path of order s-1. Hence T|C' is a two-cover of U union V(C), obtained by a legal pairwise repartition of the two displayed components.

The affected component orders change from (2,s) to (3,s-1), so

Delta Phi = 3^2+(s-1)^2-2^2-s^2 = 6-2s,

which is strictly negative for s>=4.

Now let H be a minimum counterexample and let a spanning three-cover contain a two-vertex component. Since |V(H)|>10, the other two component orders sum to more than eight, so at least one is at least five. Pairing the two-vertex component with that path gives the strict descent above. Thus no Phi-minimal three-cover of a minimum counterexample has a component of order two. This argument does not require the two-vertex component to sit between two nontrivial paths, so it also applies to singleton lifts of profile 1|2|m.

## Metadata

- ID: toolkit_two_vertex_middle_component_forces_strict_quadratic_descent
- Kind: toolkit
- Version: 2
- Math version: 2
- Audit: unaudited
- Refutation: unrefuted
