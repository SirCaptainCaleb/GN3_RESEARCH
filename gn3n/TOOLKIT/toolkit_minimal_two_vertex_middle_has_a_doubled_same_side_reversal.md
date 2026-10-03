# A quadratic-minimal two-vertex middle has a doubled same-side reversal

**Summary:** In a minimum counterexample, if A|(u,v)|C is a spanning three-cover with a two-vertex middle component and is quadratic-potential minimal in its pairwise-repartition component, then both middle vertices reverse the left exposed edge of A or both reverse the right exposed edge of C.

## Statement

Let H be a minimum counterexample and let A|(u,v)|C be a spanning three-cover with |A|,|C|>=2. Assume this cover is Phi-minimal in its pairwise-repartition component. Then either both (u,a_r,a_{r-1}) and (v,a_r,a_{r-1}) are tight, or both (c_2,c_1,u) and (c_2,c_1,v) are tight (or both conclusions hold).

## Body

For the two middle vertices define L={z in {u,v}:(a_{r-1},a_r,z) is tight} and R={z in {u,v}:(z,c_1,c_2) is tight}. The two-vertex middle classification gives three possibilities: L is empty, R is empty, or L=R={z} for one middle vertex z. In the third, mixed case, toolkit_a_mixed_two_vertex_middle_forces_strict_quadratic_descent gives a one-step pairwise repartition with strictly smaller Phi, contradicting Phi-minimality. Hence L is empty or R is empty. If L is empty, boundary antisymmetry gives both reverse triples (u,a_r,a_{r-1}) and (v,a_r,a_{r-1}); if R is empty, it gives both (c_2,c_1,u) and (c_2,c_1,v).

## Metadata

- ID: toolkit_minimal_two_vertex_middle_has_a_doubled_same_side_reversal
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
