# Every six vertices admit a span-two bad order

**Summary:** On every six-vertex set in a boundary tournament, some ordering has status pattern 001 or 011 on three consecutive status positions.

## Statement

For every six distinct vertices of a boundary tournament, there is an ordering a,b,c,d,e,f whose first three status bits are 001 or 011.

## Body

Suppose no ordering of six fixed vertices has first-three pattern 001 or 011. Then for every five distinct a,b,c,d,e, h(c,d,e)=1 implies h(a,b,c)=1. Choose a non-tight ordered triple (0,1,2); boundary antisymmetry gives h(2,1,0)=1. Applying the implication four times gives h(2,1,0)=>h(3,4,2)=>h(5,0,3)=>h(2,4,5)=>h(0,1,2), contradiction. Hence some ordering has a zero at the first status and a one at the third, with the middle bit arbitrary, i.e. 001 or 011.

## Metadata

- ID: every_six_vertices_admit_a_span_two_bad_order
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: passed
- Refutation: unrefuted
- Toolkit status: Limbo
