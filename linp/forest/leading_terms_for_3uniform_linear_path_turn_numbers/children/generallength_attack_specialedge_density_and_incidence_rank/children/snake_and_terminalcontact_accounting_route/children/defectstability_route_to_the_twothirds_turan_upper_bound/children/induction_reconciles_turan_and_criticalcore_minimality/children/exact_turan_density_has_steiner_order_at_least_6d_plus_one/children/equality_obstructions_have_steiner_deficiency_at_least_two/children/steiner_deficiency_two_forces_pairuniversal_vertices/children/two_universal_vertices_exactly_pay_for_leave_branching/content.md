# At Steiner deficiency two, universal vertices exactly pay for leave branching

## Statement

In the s=2 equality layer the leave U is even of average degree two. If z is the number of leave-isolated vertices and n_{2j} the number of leave-degree 2j vertices, then z=sum_{j>=2}(j-1)n_{2j}. Thus pair-universal vertices of H exactly equal the total branching excess of the Eulerian leave. In particular z=1 forces one degree-4 branch vertex and all other nonisolated vertices degree 2; the exceptional leave component suppresses to a bouquet of two cycles.

## Body


Assume the exact-density equality layer has Steiner deficiency s=2:
  n=6d+3.
Let U be the uncovered-pair leave graph. Then every leave degree is even and
  sum_v d_U(v)=2n.

Write
  z=|{v:d_U(v)=0}|
and, for j>=2, let
  n_{2j}=|{v:d_U(v)=2j}|.
Vertices of leave degree two contribute zero deviation from the average 2. Summing
  d_U(v)-2
over all vertices gives zero, hence
  -2z + sum_{j>=2}(2j-2)n_{2j}=0.
Dividing by two,
  z = sum_{j>=2}(j-1)n_{2j}.                        (1)

Thus the number of pair-universal vertices of H (the isolated vertices of U) is exactly the total branching excess of the Eulerian leave above degree two.

Consequences.

(1) If z=1, then necessarily n_4=1 and n_{2j}=0 for j>=3. Hence U has exactly one isolated vertex, exactly one degree-four vertex, and every other vertex has degree two. The non-cycle exceptional component is therefore an Eulerian connected graph with one degree-four branch point; after suppressing degree-two vertices it is a bouquet of two loops (allowing the two cycles to share only the branch vertex), while all remaining nontrivial components are cycles.

(2) If z=2 and the branching is concentrated in one vertex, then that vertex has leave degree six and all remaining nonisolated vertices have degree two. After suppressing degree-two vertices the exceptional component is a bouquet of three loops.

More generally, (1) is an exact defect conservation law: every extra two units of leave degree above two require one additional pair-universal vertex somewhere else.

For ell≡0 mod3, 1ef6d03dc4e0 gives z>=2. For ell≡1,2 mod3 it gives z>=1. Thus the first surviving equality layer is globally a union of cycle-like leave components with branching complexity paid for exactly by universal vertices.
