# Union-closed tournament neighborhoods force transitivity

## Metadata

- ID: union_closed_tournament_neighborhoods_force_transitivity
- Parent Section: directed_nor_union_closed_bridge
- Position: 5
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

A finite tournament's out-neighborhood family is union-closed if and only if the tournament is transitive, equivalently its neighborhoods are nested. For a->b, closure forces their union to be N+(a): a third representative c would beat a, putting a in a union that excludes a. Thus the proposed local union-closed intermediary coincides with local transitivity. Independent transitive center orders remain broader than global scalar edge orders: three distinguished edges can impose a cyclic comparison, and the construction extends to arbitrary ground sets.

## Development

## Union-closed tournament neighborhoods are precisely the transitive case

Let T be a finite tournament, and let N+(a)={b:a->b}. The family {N+(a):a in V(T)} is union-closed if and only if T is transitive; equivalently these neighborhoods are nested.

### Proof
Suppose the family is union-closed and a->b. Put U=N+(a) union N+(b)=N+(c). The vertex a is absent from U, while b belongs to U. Thus c cannot be b. If c is distinct from a,b, then c is absent from its own neighborhood and hence from U. It follows that c->a and c->b. But c->a puts a in N+(c)=U, a contradiction. Therefore c=a and N+(b) is contained in N+(a).

A directed triangle a->b->d->a would give d in N+(b) but d not in N+(a), a contradiction. Hence T has no directed triangle and is transitive. Alternatively the strict neighborhood containments along arcs directly give an acyclic orientation. Conversely, in a transitive tournament the out-neighborhoods are suffixes of one total order, so their unions are again out-neighborhoods. This includes the empty and one-vertex cases.

### NOR interpretation
For a reversal-antisymmetric ternary coordinate label h, set a-> in T_b c if h(a,b,c)=0. Then E_b(a)=N+_{T_b}(a). Requiring the family {E_b(a):a != b} to be union-closed is equivalent to requiring T_b to be transitive. It does not weaken local nestedness. The proposed interpolation nested local neighborhoods < union-closed local neighborhoods therefore collapses at this step.

Local transitivity nevertheless need not come from one global ordering of unordered edges. On three distinguished vertices a,b,c prescribe
h(a,b,c)=h(b,c,a)=h(c,a,b)=0
and give reversed triples color 1. Every center tournament has only two vertices and is transitive. A representing edge order would require
lambda(ab)<lambda(bc)<lambda(ca)<lambda(ab),
which is impossible.

This obstruction extends to any larger ground set: at each distinguished center put its two distinguished incident edges first, in the cyclicly prescribed order; put all remaining incident edges afterwards, ordered by one fixed injective weight on nondistinguished edges. At other centers use that fixed weight order. Define h by the local comparisons. Every center tournament is transitive and reversal antisymmetry holds, but the same three-edge cycle prevents global representation.

Thus three separate conditions must be distinguished: global edge-order representability; transitivity (equivalently union closure) of local center neighborhoods; union closure of fixed-tail feasible supports. The latter is a condition on entire witness paths and is not established by the neighborhood theorem. No NOR closure for the whole locally transitive class is asserted.
