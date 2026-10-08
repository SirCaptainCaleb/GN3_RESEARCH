# Two-hole cage around a near-spanning ternary tight path

## Composition

If a counterexample has a monochromatic path on all but two vertices, endpoint blocking forces both hole-pair orders and both exposed ends. The two corresponding full cyclic orders have the same four-change word with two singleton opposite-color runs. The hypothesis that such a near-spanning monochromatic path exists is essential and is not proved for every counterexample.

## Development

## Two-hole cage around a near-spanning tight path

Work in the directed ternary sector, with h(c,b,a)=1-h(a,b,c). Assume h is a counterexample on V. Let P=(v_1,...,v_m), m=|V|-2, be a color-sigma tight path, and let the omitted vertices be x,y.

### Proposition
The omitted vertices satisfy
h(x,v_1,v_2)=h(y,v_1,v_2)=1-sigma,
h(v_{m-1},v_m,x)=h(v_{m-1},v_m,y)=1-sigma,
h(x,y,v_1)=h(y,x,v_1)=sigma,
and
h(v_m,x,y)=h(v_m,y,x)=sigma.

Consequently the cyclic orders
C_xy=(x,y,v_1,...,v_m) and C_yx=(y,x,v_1,...,v_m)
have the same cyclic status word
sigma, 1-sigma, sigma^(m-2), 1-sigma, sigma.
Thus each has four color changes, with two singleton (1-sigma)-runs.

### Proof
Consider (x,P), an order of V\{y}. Its new first color cannot be sigma: otherwise (x,P) is monochromatic on |V|-1 vertices, and prepending y would give a spanning word with at most one change. Hence h(x,v_1,v_2)=1-sigma, and symmetrically h(y,v_1,v_2)=1-sigma.

Therefore (x,P) is a one-change deletion order with initial color 1-sigma and final color sigma. Endpoint blocking for the omitted vertex y gives h(y,x,v_1)=sigma and h(v_{m-1},v_m,y)=1-sigma. Interchanging x,y gives h(x,y,v_1)=sigma and h(v_{m-1},v_m,x)=1-sigma.

Now (P,x) is a one-change deletion order of V\{y}, with final color 1-sigma. Endpoint blocking when y is appended gives h(v_m,x,y)=sigma. Interchanging x,y gives h(v_m,y,x)=sigma.

Reading the cyclic triples of C_xy yields sigma,1-sigma, then all internal colors of P (all sigma), then 1-sigma,sigma. The same calculation holds for C_yx. QED.

### Corollary
Any counterexample containing a monochromatic tight path on all but two vertices contains a minimum-variation four-change cyclic order with two isolated opposite-color statuses. Swapping the two omitted vertices preserves the entire cyclic status word.

For |V|=6 this is the opposite-window-coherent pattern sigma,(1-sigma),sigma,sigma,(1-sigma),sigma.

### Significance
The two holes are blocked at both ends, while both orders of the hole pair are forced to have color sigma against the exposed one-coordinate ends. This gives a rigid interface between maximum tight paths and the deletion-root-cycle route. No claim is made that every minimum counterexample contains such a path.
