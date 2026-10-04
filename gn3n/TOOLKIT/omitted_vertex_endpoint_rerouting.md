# Endpoint rerouting at an omitted vertex

**Summary:** If a vertex omitted from a two-path cover cannot be absorbed at either displayed end, boundary antisymmetry forces a four-vertex tight path crossing the two exposed ends and consuming one terminal edge.

## Statement

Let H be a boundary tournament with pc(H)>2, let x be a vertex, and let P|Q be a two-path cover of H-x. If P=(...,a0,a1) and Q=(...,b0,b1) have at least two vertices each, then (x,a1,a0) and (x,b1,b0) are tight. Exactly one of (a1,x,b1) and (b1,x,a1) is tight; consequently one of (a1,x,b1,b0) and (b1,x,a1,a0) is a tight four-vertex path.

## Body

# Endpoint rerouting at an omitted vertex

Let `H` be a boundary tournament with `pc(H)>2`, let `x` be a vertex, and let

`P | Q`

be a two-path cover of `H-x`. Suppose the displayed terminal portions are

`... a_0,a_1` and `... b_0,b_1`.

Because appending `x` to `P` would otherwise give a spanning two-path cover of `H`, `(a_0,a_1,x)` is not tight. Boundary antisymmetry therefore gives `(x,a_1,a_0)` tight. Similarly `(x,b_1,b_0)` is tight.

Exactly one of `(a_1,x,b_1)` and `(b_1,x,a_1)` is tight. In the first case

`(a_1,x,b_1,b_0)`

is a tight path; in the second case

`(b_1,x,a_1,a_0)`

is a tight path.

Thus failure to absorb the omitted vertex directly at either displayed path end forces a local rerouting across the two exposed ends: the omitted vertex joins the two current endpoints and the resulting four-vertex path incorporates the terminal edge of one of the old paths. The point of the lemma is the local move itself; by itself it does not produce a spanning two-cover.

## Metadata

- ID: omitted_vertex_endpoint_rerouting
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Toolkit status: Limbo
