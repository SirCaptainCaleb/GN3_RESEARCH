# Every six vertices admit a span-two bad order

**Summary:** Every six-vertex set in a boundary tournament has an ordering whose first three status bits are 001 or 011.

## Statement

For every six distinct vertices of a boundary tournament, there is an ordering a,b,c,d,e,f whose first three status bits are 001 or 011.

## Body

Suppose no ordering of six fixed vertices has first-three pattern (001) or (011). Then for every five distinct (a,b,c,d,e),
[
h(c,d,e)=1Longrightarrow h(a,b,c)=1.
]
Choose a non-tight ordered triple (h(0,1,2)=0). Boundary antisymmetry gives (h(2,1,0)=1). Applying the implication repeatedly,
[
h(2,1,0)Rightarrow h(3,4,2)Rightarrow h(5,0,3)Rightarrow h(2,4,5)Rightarrow h(0,1,2),
]
contradiction.

## Metadata

- ID: every_six_vertices_admit_a_span_two_bad_order
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
