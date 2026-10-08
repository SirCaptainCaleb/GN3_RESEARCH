# Transitive center tournaments can fail support union closure at a sink — preserved pre-item development

## Composition

(none yet)

## Development

## Local transitivity does not imply support union closure, even at a sink tail

The neighborhood theorem and the support-coverage theorem leave a precise gap: do transitive center tournaments force union closure of the support family at a local sink? The answer is no.

### Proposition
On every ground set V={u,v,a,b} union R there is a reversal-antisymmetric ternary coordinate coloring with all center tournaments transitive and v a sink in T_u, but F_{0,(u,v)} is not union-closed.

### Construction and proof
Specify a strict total order on V\setminus{x} for each center x, and put h(p,x,q)=0 if p precedes q in that center order. Define h=1 otherwise. This automatically gives h(q,x,p)=1-h(p,x,q), and each T_x is transitive.

At center u choose the order
a < b < (the vertices of R in any fixed order) < v.
At center a put u before b, with the other vertices placed arbitrarily. At center b put u before a, with the other vertices placed arbitrarily. At all other centers choose any total order.

Then h(a,u,v)=h(b,u,v)=0, so the singleton supports {a},{b} are feasible at tail (u,v). But h(a,b,u)=1 because u precedes a at center b, and h(b,a,u)=1 because u precedes b at center a. The only possible witnesses on support {a,b} are (a,b,u,v) and (b,a,u,v); both fail their first window. Hence {a,b} is infeasible, although both singletons and the empty set are feasible. This is a top-missing support square with empty base.

The construction retains v as a sink of T_u and retains transitivity at every center for arbitrary R. Thus the gap is structural and persists under adding coordinates.

### Meaning
Even at the most favorable terminal pair, where every singleton outside the tail is feasible, local neighborhood union closure does not supply support union closure. The obstruction already resides in comparisons at the two different centers a and b. It is not a failure to choose the sink correctly.

This does not refute directed NOR for the locally transitive class, and it does not refute the general conjecture. It refutes only the implication from local transitivity to support union closure, including the attempted sink-tail specialization. A proof for that class needs exchanges between terminal states or a direct spanning construction; applying antimatroid frequency or coverage at one tail cannot establish the missing premise.
