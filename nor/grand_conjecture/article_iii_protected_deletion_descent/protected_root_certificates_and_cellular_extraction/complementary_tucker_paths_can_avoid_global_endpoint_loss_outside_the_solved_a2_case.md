# Complementary Tucker paths can avoid global endpoint loss outside the solved A2 case

## Composition

(none yet)

## Development

## Complementary Tucker paths can avoid global endpoint loss outside the solved A2 case

Work in one product cell of the switch-prism / permutahedral refinement carrying complementary signed-middle labels +b and -b.

A signed-middle label exists only when b is the middle coordinate of a ternary window, so in both complementary endpoint states the physical coordinate b is NOT at either global endpoint of the coordinate order.

The arbitrary-cell extraction theorem follows a chamber-graph path between these two states. Its only unresolved purely combinatorial event class was that b might move to a global endpoint and temporarily lose its centered window.

That event can be avoided by path choice except in the already local A2 case.

### Chamber graph inside one Coxeter block

Let the Coxeter block containing b occupy a fixed contiguous interval of positions. Refinements of the face vary the order inside this block by adjacent transpositions.

If the block interval does not meet a global endpoint, b can never become a global endpoint and there is nothing to prove.

Suppose the block meets a global endpoint.

The relevant combinatorial statement is:

> In S_m with adjacent-transposition edges, the induced graph on permutations in which a distinguished symbol b is not in position 1 or m is connected for m>=4.

If only one of the two positions is forbidden, the analogous graph is connected already for m>=3.

### Proof for two forbidden endpoints

Take m>=4.

First move b by adjacent swaps to position 2; this never puts b in position 1.

Adjacent swaps not involving b freely permute the suffix positions 3,...,m.

It remains to show that the symbol in position 1 can be exchanged with a suffix symbol without sending b to an endpoint.

With local order

(A,b,C,D,...)

perform

(A,b,C,D,...)
 -> (A,C,b,D,...)
 -> (C,A,b,D,...)
 -> (C,b,A,D,...).

The three swaps are legal chamber edges, b visits only positions 2 and 3, and the net effect exchanges A and C while returning b to position 2.

Together with arbitrary suffix swaps, these moves generate all permutations of the non-b symbols while keeping b internal. Moving b among positions 2,...,m-1 then connects every allowed permutation.

Thus the induced internal-b graph is connected.

### The exceptional size-three block

For m=3 with both endpoints forbidden, b must stay in the unique middle position. The two possible orders of the other coordinates are disconnected if paths are required to keep b internal.

But this is exactly an A2 Coxeter block. The honest side-balanced A2 / A3 local extraction results already treat complementary same-middle states in this bounded carrier directly; no long arbitrary-cell path through an endpoint is required.

### Tucker consequence

Given a complementary product cell with labels +b and -b:

- if the b-block has size at least four, choose a chamber path between the two labeled states that keeps b away from every global endpoint;
- if the block does not touch a global endpoint, endpoint loss is impossible automatically;
- if the only obstruction is a size-three endpoint-touching block, invoke the existing A2 local extraction.

Vertical cut moves do not change the physical position of b and therefore preserve the endpoint-avoidance property.

Hence the global-endpoint equality event in root §81 is not an essential termination class for complementary Tucker extraction.

### Updated frontier

Along an endpoint-avoiding path, the first disappearance/side-change event for the b-centered violation is one of:

1. vertical cut change: E strictly decreases;
2. same-side bubble: E decreases or fixed-cut Q increases;
3. switch-crossing move: a phase-compatible repair;
4. neighbor replacement: E decreases or fixed-cut Q increases.

Therefore, at FIXED cut, every non-strict interior event is already terminated by (E,-Q).

The remaining global issue is compatibility when a switch-crossing repair changes the effective cut / phase state, not physical endpoint loss of b.
