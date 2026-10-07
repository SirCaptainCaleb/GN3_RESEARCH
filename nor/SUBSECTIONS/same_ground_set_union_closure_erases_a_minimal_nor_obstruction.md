# Same-ground-set union closure erases a minimal NOR obstruction

## Metadata

- ID: same_ground_set_union_closure_erases_a_minimal_nor_obstruction
- Parent Section: directed_nor_union_closed_bridge
- Position: 32
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development


## Same-ground-set union closure erases a minimal NOR obstruction

Let U be a minimal local fixed-tail obstruction, so its feasible-support family on U is H = 2^U minus {U}.

### Proposition
If K is union-closed and H subseteq K subseteq 2^U, then K=2^U.

### Proof
Choose distinct a,b in U. Both U minus {a} and U minus {b} lie in H. Their union is U, so union closure forces U into K. Hence K contains every subset of U.

### Consequence
The union-closure hull of H is the full Boolean cube. Every coordinate then occurs in exactly half the sets, so Frankl's heavy-element conclusion yields no distinguished coordinate and no witness-order information. The completion has repaired the obstruction only by inserting the very top support whose feasibility NOR still needs to prove.

Likewise, the complementary family 2^U minus {emptyset} is union-closed and every coordinate is automatically heavy. That heaviness is forced by the Boolean shape and does not encode the missing witness.

Therefore a genuine NOR-to-Frankl reduction cannot merely close feasible supports under union on the same ground set. It must retain witness-order information, for example through extra coordinates or state, so that a heavy element decodes to a synchronizable extension, splice, or terminating recentering move.


## Frontier

- Development version when composed: None
- Development version now: 1
