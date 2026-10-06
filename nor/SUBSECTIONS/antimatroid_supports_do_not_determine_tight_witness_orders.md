# Antimatroid supports do not determine tight witness orders

## Metadata

- ID: antimatroid_supports_do_not_determine_tight_witness_orders
- Parent Section: higher_memory_norine_geodesics
- Position: 46
- Row version: 2
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

Two reversal-antisymmetric ternary colorings can have the same antimatroid support family F_{0,(u,v)}=2^{ {a,b} } but disjoint maximal-support tight witness orders. In both, set h(a,u,v)=h(b,u,v)=0. In one, set h(a,b,u)=0,h(b,a,u)=1; in the other interchange those colors. Complete reverses complementarily. The full-support witnesses are respectively (a,b,u,v) and (b,a,u,v).

Thus a feasible-support chain need not lift through front extensions of the chosen witness, and the antimatroid basic-word language need not coincide with the tight witness language. Sections 41 and 44's set-family structure remains valid, but gluing needs control of exposed ordered tuples and actual witness orders.

Any spanning conclusion must also account for vertices outside the local support plus terminal tuple. An abundant coordinate in a support family supplies a counting statement, with a further witness-preserving step needed to reach NOR closure.

## Development

## Antimatroid supports do not determine tight witness orders

The support arguments in sections 41 and 44 are valid as statements about feasible sets. Their use in NOR still requires a separate theorem about witness orders. The following example makes the distinction explicit.

### Proposition
There are two reversal-antisymmetric ternary colorings with the same feasible-support family F_{0,(u,v)}=2^{ {a,b} }, but with disjoint sets of color-0 tight witness orders for the maximal support {a,b}.

### Proof
In both colorings set
h(a,u,v)=h(b,u,v)=0.
In the first coloring set
h(a,b,u)=0, h(b,a,u)=1.
In the second coloring set
h(a,b,u)=1, h(b,a,u)=0.
Assign all reversed triples complementary colors and complete other reversal-orbits arbitrarily. These prescriptions are consistent: (a,b,u) and (b,a,u) are not reverses.

In both colorings the empty support and both singleton supports are feasible. The full support {a,b} is feasible in the first coloring via (a,b,u,v), and in the second via (b,a,u,v). Hence both feasible-support families are the full Boolean family, an antimatroid.

The only two witness orders for {a,b} ending in the prescribed terminal tuple are (a,b,u,v) and (b,a,u,v). Precisely the first is 0-tight in coloring one, and precisely the second in coloring two. Thus their maximal-support witness languages are disjoint.

In particular the feasible chain
emptyset, {a}, {a,b}
does not necessarily lift by successive front extension of its existing witness (a,u,v): prepending b is invalid in the first coloring, even though {a,b} is feasible through another order. The usual antimatroid basic-word language of the support family therefore contains words that the tight-path witness language does not. Square.

### Consequence for the current research
Accessibility and local square completion control supports. They do not supply permission to prepend a specified new vertex to a specified tight witness. A theorem synchronizing witnesses or changing their exposed (r-1)-tuples is still needed before an antimatroid argument yields a NOR exchange.

For a minimal top-missing support square, the antimatroid side restrictions in section 44 may therefore be useful, but the combinatorial information needed for gluing includes the actual witness orders and their exposed tuples. The example does not refute section 44's set-family proposition.

Also, a one-change order found on the square's support plus the terminal tuple need not span the ambient NOR ground set. Any closure or descent must account for all remaining vertices. This is the same ambient-set issue identified in the audit of tail truncation.

### Relation to Frankl
An abundant coordinate in an antimatroid support family concerns how many supports contain the coordinate. It does not by itself constrain the orders realizing those supports. Turning abundance into a spanning NOR construction therefore requires an additional witness-preserving mechanism. The present example isolates that requirement without using any additional edge-order assumptions.
