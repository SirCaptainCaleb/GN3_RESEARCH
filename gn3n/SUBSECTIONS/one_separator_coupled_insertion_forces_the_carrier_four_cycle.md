# One-separator coupled insertion forces a directed local four-cycle

## Metadata

- ID: one_separator_coupled_insertion_forces_the_carrier_four_cycle
- Parent Section: article_vii_synthesis_and_exact_frontier
- Position: 49
- Row version: 2
- Development version: 2
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Let B=(b_1,...,b_m) be a tight path, let x,y be outside B, and assume neither x nor y can be inserted individually into any slot of the inherited order of B. Suppose nevertheless that for some i with 1<=i<=m-2 the order

(...,b_i,x,b_{i+1},y,b_{i+2},...)

is tight and preserves the order of all vertices of B.

Then in the local tournament at the separator b_{i+1}, the four vertices b_i,b_{i+2},x,y contain the directed cycle

b_i -> b_{i+2} -> x -> y -> b_i.

Proof. Since B is tight, h(b_i,b_{i+1},b_{i+2})=1, so b_i -> b_{i+2} in the local tournament at b_{i+1}. The coupled order is tight, in particular h(b_i,x,b_{i+1})=1, h(x,b_{i+1},y)=1, and h(b_{i+1},y,b_{i+2})=1.

Insert x alone between b_i and b_{i+1}. The left junctions required for that insertion are already certified by the coupled order, including h(b_i,x,b_{i+1})=1. Since the one-vertex insertion fails, the remaining right junction must fail:
h(x,b_{i+1},b_{i+2})=0.
Boundary antisymmetry gives h(b_{i+2},b_{i+1},x)=1, hence b_{i+2}->x.

Similarly, insert y alone between b_{i+1} and b_{i+2}. The middle and right junctions are certified by the coupled order. Since that insertion fails, the left junction must fail:
h(b_i,b_{i+1},y)=0.
Thus h(y,b_{i+1},b_i)=1, hence y->b_i. Finally h(x,b_{i+1},y)=1 gives x->y. These four arcs form the stated directed cycle. ∎

For a genuine minimum deletion pair {x,y}, minimum-pair nonaugmentability supplies the individual noninsertability hypothesis on each inherited path. Thus any successful one-separator coupled absorption preserving an inherited path order produces this four-label directed local pattern.

This directed cycle is not the terminal-pair carrier C4. Here all arcs have one fixed middle label b_{i+1}, so boundary antisymmetry makes the reverse arc complementary; the carrier C4 instead lives in a mutual ordered-pair graph and requires both directions of each cycle edge to be admissible. The result therefore supplies a bounded four-label local-tournament normal form, not a topological loop identification. Any transfer from this normal form to the carrier obstruction requires an additional theorem.

## Frontier

- Development version when composed: None
- Development version now: 2
