# Boundary tournaments as oriented transition systems

**Summary:** A boundary 3-tournament is equivalently a family of ordinary tournaments T_v on V\{v}; a tight path is exactly a path in K_n whose successive incident-edge transitions follow the corresponding local tournament orientations.

## Statement

For each vertex v of a boundary 3-tournament H, define an ordinary tournament T_v on V(H)\{v} by u ->_{T_v} w iff (u,v,w) is tight. Boundary antisymmetry makes T_v a tournament, and the family {T_v} determines H. A vertex sequence (v_1,...,v_k) is a tight path iff v_{i-1} ->_{T_{v_i}} v_{i+1} for every internal index i. Equivalently, H is an oriented transition system on K_n in which each vertex orients every pair of incident edges.

## Body

# Boundary tournaments as oriented transition systems

Let `H` be a boundary 3-tournament on vertex set `V`. For each `v in V`, define an ordinary tournament `T_v` on `V-{v}` by

`u ->_{T_v} w` iff `(u,v,w)` is tight.

For distinct `u,w`, the boundary flip of `(u,v,w)` is `(w,v,u)`. Hence exactly one of these two triples is tight, so exactly one of `u ->_{T_v} w` and `w ->_{T_v} u` holds. Thus `T_v` is an ordinary tournament.

Conversely, an arbitrary family of tournaments `{T_v:v in V}`, with `T_v` on `V-{v}`, defines a boundary 3-tournament by declaring `(u,v,w)` tight exactly when `u ->_{T_v} w`. Therefore boundary 3-tournaments are equivalent to families of local tournaments centered at the vertices.

Now let `P=(v_1,...,v_k)` be a sequence of distinct vertices. It is a tight path exactly when

`v_{i-1} ->_{T_{v_i}} v_{i+1}`

for every internal index `2<=i<=k-1`.

Equivalently, view `P` as an ordinary path in `K_V`. At every internal vertex `v_i`, the two incident path edges `{v_{i-1},v_i}` and `{v_i,v_{i+1}}` are traversed in the orientation prescribed by the local tournament `T_{v_i}` on the incident edges. Thus `H` is an oriented transition system on the complete graph: every pair of incident edges at a vertex receives exactly one allowed traversal direction.

In this language the two-cover problem asks whether every such oriented transition system on `K_n` has a spanning cover by at most two vertex-disjoint compatible paths.

## Metadata

- ID: boundary_tournaments_as_oriented_transition_systems
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Toolkit status: Limbo
