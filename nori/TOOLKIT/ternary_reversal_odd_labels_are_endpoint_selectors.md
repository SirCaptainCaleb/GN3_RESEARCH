# Ternary reversal-odd labels are endpoint selectors; changes are inner/outer defects

**Summary:** For h(a,b,c), let color 0 select a and color 1 select c. Reversal keeps the same selected endpoint. Then 01 on a,b,c,d selects a,d (outer defect) and 10 selects c,b (inner defect). NOR asks for an order with no inner defects or no outer defects.

## Statement

A reversal-odd ternary binary label canonically selects one endpoint of every ordered two-edge path, independently of path reversal. On a four-vertex block, status 01 is exactly outer-endpoint selection and status 10 is exactly inner-endpoint selection. Thus a one-change spanning order is equivalently a Hamilton order avoiding one of the two defect types.

## Body


## Endpoint-selector form

Let h(a,b,c) be binary with h(c,b,a)=1-h(a,b,c).

For the unoriented two-edge path a-b-c define its selected endpoint by

s(a-b-c)=a if h(a,b,c)=0,
s(a-b-c)=c if h(a,b,c)=1.

This is independent of orientation: if the path is read backward as c-b-a, its color is complemented, so the same physical endpoint is selected.

Thus a directed ternary NOR coloring is equivalently a rule that, for every center b and unordered pair {a,c}, selects one of the two endpoints.

Equivalently, each center b carries a tournament on V minus {b}.

### Four-block dictionary

For a,b,c,d in this order, compare the selectors on a-b-c and b-c-d.

- status 00 selects a and b;
- status 01 selects a and d, the two outer vertices;
- status 10 selects c and b, the two inner vertices;
- status 11 selects c and d.

Call 01 an outer defect and 10 an inner defect.

A binary word has no 10 pattern exactly when it is 0*1*. It has no 01 pattern exactly when it is 1*0*. Therefore:

A spanning order satisfies directed ternary NOR if and only if it avoids all inner defects or avoids all outer defects on consecutive four-blocks.

A counterexample is equivalently an endpoint-selector system in which every Hamilton order contains at least one inner defect and at least one outer defect.

Both defect types are invariant under reversal of the Hamilton order, as required by the reversal-complement rule.

### Topological relevance

A ternary window is a consecutive-rank 2-face of the antipodal Coxeter sphere from the cube-to-simplex completion. The selector chooses one of the two endpoint coordinates of that face. Consecutive windows share an edge, and inner/outer defects describe the two possible directions in which those endpoint choices can cross the shared edge.

This gives a local formulation suited to connector/Sperner arguments: closure means finding a chamber whose selector flow never turns inward, or never turns outward.


## Metadata

- ID: ternary_reversal_odd_labels_are_endpoint_selectors
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
