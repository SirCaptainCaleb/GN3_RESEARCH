# Endpoint rerouting at an omitted vertex

**Summary:** If an omitted vertex cannot be absorbed at either displayed end of a two-path cover, boundary antisymmetry forces a tight four-vertex rerouting path across the two exposed ends.

## Statement

Let pc(H)>2 and let P|Q cover H-x. If P=(...,a0,a1) and Q=(...,b0,b1), then (x,a1,a0) and (x,b1,b0) are tight, and one of (a1,x,b1,b0), (b1,x,a1,a0) is a tight four-path.

## Body

Let (P|Q) be a two-path cover of (H-x), with displayed terminal portions
[
ldots,a_0,a_1,qquad ldots,b_0,b_1.
]
Since (x) cannot be appended to (P) without producing a spanning two-cover,
[
(a_0,a_1,x)
]
is non-tight, hence by boundary antisymmetry ((x,a_1,a_0)) is tight. Similarly ((x,b_1,b_0)) is tight.

Exactly one of ((a_1,x,b_1)) and ((b_1,x,a_1)) is tight. In the first case
[
(a_1,x,b_1,b_0)
]
is a tight path; in the second,
[
(b_1,x,a_1,a_0)
]
is a tight path.

## Metadata

- ID: omitted_vertex_endpoint_rerouting
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
