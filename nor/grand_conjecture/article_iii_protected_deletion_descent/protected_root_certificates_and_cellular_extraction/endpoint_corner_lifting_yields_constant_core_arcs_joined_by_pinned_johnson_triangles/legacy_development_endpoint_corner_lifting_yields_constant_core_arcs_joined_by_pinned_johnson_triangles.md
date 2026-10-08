# Endpoint corner lifting yields constant-core arcs joined by pinned Johnson triangles — preserved pre-item development

## Composition

(none yet)

## Development

## Audit and replacement: the endpoint corner lift is a backward-copy move, yielding a constant-core arc decomposition

### Audit of Subsections 108 and 111

For consecutive endpoint cuts
C_i={x_i,a_i},
C_i^+={x_{i+1},a_i},
C_{i+1}={x_{i+1},a_{i+1}},
the missing Johnson-square corner is
M_i={x_i,a_{i+1}}.

Realizing M_i by an endpoint/deletion witness for the SAME physical root x_i->x_{i+1} changes the partner on edge i from a_i to a_{i+1}. Thus the direct operation supplied by the square-lift target of Subsection 93 is

a_i <- a_{i+1}.

It COPIES the next partner backward. It does not by itself swap the pair (a_i,a_{i+1}) to (a_{i+1},a_i), because that would additionally require the successor cut C_i^+={x_{i+1},a_i} to be attained as an endpoint witness for edge i+1.

Therefore Subsection 108 is valid only under its explicitly stronger two-witness SWAP-lift hypothesis. The synchronization step imported from 108 into Subsection 111 is correspondingly stronger than the present missing-corner theorem. The later uniform-offset transport inside §111 does use only the copy lift, but its initial reduction to a synchronized offset is not yet supplied by §93.

The sign correction in §108 remains valid independently:
D_i=e_{a_{i+1}}-e_{a_i}; for a synchronized shift a_i=x_{i+r}, one has D_i=-rho_{i+r}.

### The correct copy-lift dynamics

Assume the following witness-preserving CORNER-LIFT property, exactly matching §93:

For any i with a_{i+1} notin {x_i,x_{i+1}}, either
1. there is a legal endpoint/deletion witness for edge x_i->x_{i+1} with partner a_{i+1}, so a_i may be replaced by a_{i+1}; or
2. the local surgery gives a full-support one-change order or a strictly improved protected witness.

The condition a_{i+1}!=x_{i+1} is already part of the endpoint witness at i+1. Hence the only new degeneracy is
a_{i+1}=x_i.
That is exactly the Johnson-triangle case where the missing corner would be {x_i,x_i}.

Suppose no solve/improvement occurs, so every nondegenerate copy move is realizable.

### Partner changes behave like movable domain walls

Let
m(a)=#{i : a_i != a_{i+1}}
be the cyclic number of partner changes.

If a_i!=a_{i+1} and the copy move at i is nondegenerate, replace a_i by a_{i+1}. The change at boundary i disappears. At boundary i-1, at most one change is created. Hence m never increases.

In block language, if a maximal constant block with value a begins at edge s, then copying a backward replaces the partner on edge s-1 by a. This moves the start of the a-block one step backward while leaving the physical root cycle unchanged. Repeating either:
- eliminates the preceding partner block, strictly lowering m; or
- reaches a degenerate edge where a=x_{s-1}.

Choose an unresolved witness-realized partner assignment minimizing m. Subject to that, push every block backward as far as possible by corner lifts.

### External partners force an exact constant-core cycle

Let S={x_0,...,x_{k-1}} be the physical-cycle support.

If some partner value a lies outside S, then a is never equal to any x_i. Hence its block has no degenerate stopping edge. It can be copied backward through every preceding block.

In an m-minimal unresolved assignment this is possible only if m=0, because otherwise the a-block would eventually eliminate another block and lower m.

Thus all partners are equal to the same exterior coordinate a. Then
C_i={x_i,a},
C_i^+={x_{i+1},a}=C_{i+1}
for every i.

So any endpoint cycle with an exterior partner collapses, under corner lifting, to an EXACT realized constant-core Johnson cycle.

Therefore a genuinely unresolved corner-lift-minimal cycle has every partner inside the physical support S.

### Internal partners give pinned constant-core arcs

Now let a=x_t be an internal partner value.

The copy move that would extend its block backward onto edge i is degenerate exactly when x_t=x_i. Thus a backward-maximal x_t-block must begin at edge
s=t+1
(mod k), because the preceding edge is t and cannot carry partner x_t.

Equivalently, at every partner-change boundary
a_{s-1} != a_s,
the NEW partner is forced to be
a_s=x_{s-1}.

Also, one internal partner value cannot occur in two disjoint maximal blocks after this normalization: both blocks would have to begin at the same unique edge t+1.

Hence the normalized partner word partitions the physical cycle into constant-partner arcs
I_1,...,I_r
with distinct cores, and if I_j begins at edge s_j then its core is exactly
x_{s_j-1}.

Inside each arc the Johnson chronology is exact:
if i and i+1 lie in the same arc, a_i=a_{i+1}=a and
C_i^+={x_{i+1},a}=C_{i+1}.

All cut defects are concentrated at the arc boundaries.

At a boundary beginning at s, the defect is pinned by
a_s=x_{s-1};
the chronological cut geometry on the three consecutive physical coordinates
x_{s-1},x_s,x_{s+1}
is a degenerate Johnson triangle rather than a missing square.

### Endpoint-color consequence at every pinned boundary

For the endpoint witness omitting x_s, its partner is a_s=x_{s-1} and its physical successor is x_{s+1}. Write its beginning as
(x_{s-1},b_s,x_{s+1},...).

Prepending x_s gives the established fully-curved endpoint 10 barrier
(x_s,x_{s-1},b_s,x_{s+1}).

Failure of the last-pair repair forces
alpha(x_s,x_{s-1},x_{s+1})=0.
By alternation,
alpha(x_{s-1},x_s,x_{s+1})=1.

Thus every partner-change boundary certifies that the corresponding consecutive triple of the physical cycle has color 1.

If every arc has length one, every edge is a boundary, so the physical cycle order is monochromatic and the Hamiltonian case closes exactly as in §111. More generally the unresolved endpoint cycle is now a concatenation of exact constant-core arcs joined only at pinned endpoint triangles.

### Correct live endpoint frontier

Under the actual §93 corner-lift theorem, arbitrary partner-defect circulation reduces to the following much smaller object:

- exterior-core case: exact constant-core Johnson cycle;
- internal-core case: finitely many exact constant-core arcs;
- the only remaining incompatibilities are degenerate Johnson triangles at arc boundaries, each carrying an actual fully-curved endpoint witness and the forced physical triple color 1.

This is the appropriate next target for local extraction. It avoids the stronger unproved swap-lift assumption and replaces arbitrary partner alignment by a one-dimensional domain-wall problem with explicit pinned boundary geometry.
