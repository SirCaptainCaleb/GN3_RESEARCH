# Boundary tournaments as oriented transition systems

**Summary:** A boundary 3-tournament is equivalently a family of ordinary tournaments centered at vertices; tight paths are exactly compatible paths in the resulting oriented transition system.

## Statement

For each vertex v define T_v on V\{v} by u→_{T_v}w iff (u,v,w) is tight. Then each T_v is a tournament, the family {T_v} determines H, and (v_1,...,v_k) is tight iff v_{i-1}→_{T_{v_i}}v_{i+1} for every internal i.

## Body

For each vertex (v) of a boundary (3)-tournament (H), define an ordinary tournament (T_v) on (V(H)setminus{v}) by
[
u	o_{T_v} w iff (u,v,w)	ext{ is tight}.
]
Boundary antisymmetry makes (T_v) a tournament, and conversely any family ({T_v}) defines a boundary tournament in this way.

A vertex sequence
[
(v_1,ldots,v_k)
]
is a tight path exactly when
[
v_{i-1}	o_{T_{v_i}}v_{i+1}
]
for every internal index (i). Thus a boundary tournament is an oriented transition system on (K_n): at each vertex, every pair of incident edges has exactly one allowed traversal orientation.

## Metadata

- ID: boundary_tournaments_as_oriented_transition_systems
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
