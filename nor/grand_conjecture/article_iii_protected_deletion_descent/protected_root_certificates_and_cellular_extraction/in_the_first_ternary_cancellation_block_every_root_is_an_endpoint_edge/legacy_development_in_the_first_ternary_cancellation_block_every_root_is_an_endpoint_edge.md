# In the first ternary cancellation block every root is an endpoint edge — preserved pre-item development

## Composition

(none yet)

## Development

## In the first ternary cancellation block every root is an endpoint edge

By the block-coorientation theorem, a positive physical window-slide dependence in ternary arity cannot be supported in a Coxeter block of size at most 3. The first possible block has size 4, an A3 permutohedral block.

Fix such a block B occupying four consecutive chamber positions. For ternary arity r=3, any actual window-slide root whose endpoints both lie in B joins positions exactly three apart. Hence its endpoints are necessarily the first and last coordinates of B in the carrying chamber.

Therefore every internal physical root in the A3 block has the form

rho(pi)=e_{first_B(pi)}-e_{last_B(pi)}.

The two middle coordinates of the block do not enter the root label.

### Endpoint-digraph reduction

Take any positive dependence of internal block roots. Orient the physical edge from the last endpoint to the first endpoint, as in the circulation convention. The dependence is exactly a positive circulation on the directed graph whose vertices are the four physical coordinates of B.

A support-minimal positive dependence is therefore a directed simple endpoint cycle of length 2, 3, or 4. After rescaling, all coefficients on that cycle are equal.

Thus the first genuine ternary root-extraction problem is finite in structure without any SAT/MILP classification:

- length 2: two chambers carry opposite endpoint roots e_a-e_b and e_b-e_a;
- length 3: three endpoint roots form a directed triangle;
- length 4: all four coordinates form a directed endpoint cycle.

### Geometry of the two-cycle

To reverse a and b from first/last to last/first while keeping the same four-position block requires at least five adjacent transpositions. For example

(a,c,d,b) -> (b,c,d,a)

has inversion distance five, and five is minimal because a must move three places right and b three places left with their mutual crossing counted once.

This exactly matches the short-path coorientation theorem: every ternary chamber path of at most four walls is zero-free, while an opposite-root pair first becomes geometrically possible at wall-distance five inside A3.

### Extraction target

The ternary carrier problem may now be attacked cycle-by-cycle in this A3 endpoint graph. For a shortest positive carrier, choose a shortest chamber path realizing one endpoint-cycle edge transition. The first non-cooriented geometry is forced to traverse essentially the full four-coordinate block, so any successful local bridge theorem need only understand how the two middle coordinates mediate an endpoint reversal.

This is substantially smaller than an arbitrary Coxeter-block extraction problem and is compatible with the existing distance-two/three repair packets and antipodal two-exit analysis.
