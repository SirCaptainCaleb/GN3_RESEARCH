# Every endpoint-cycle junction either closes locally or has a shortcut-separating two-cut — preserved pre-item development

## Every endpoint-cycle junction either closes locally or has a shortcut-separating two-cut

Work in a minimum counterexample.

For each coordinate x, choose a NOR-good deletion order
O_x=(a,b,y,...)
on V minus {x}. Normalize its one-change word to 0^p1^q. Prepending x gives
F_x=(x,a,b,y,...).
If alpha(x,a,b)=0, F_x is already one-change, impossible. Hence alpha(x,a,b)=1 and the first packet has transition 1->0.

If the tetrahedron {x,a,b,y} were flat, flatness gives alpha(x,b,y)=0. Swapping the first pair gives
(a,x,b,y,...)
with first two statuses 0,0 and every later window equal to the old deletion witness from b onward. This is a spanning one-change order, impossible.

Therefore the first endpoint transition is fully curved. It supplies the protected endpoint root
x->y
with certified cut {x,a}.

Choose one such outgoing endpoint root from every coordinate. A finite functional digraph contains a directed cycle. Consider consecutive cycle roots
x->y, y->z,
and write the first packet as (x,a,b,y).

By the fully-curved K2,2 theorem, the first packet realizes all four roots from source pair {x,a} to target pair {b,y}. In particular it realizes
a->y.

If a=z, this is the opposite root z->y to the next cycle root y->z. Their two four-coordinate packets share y,z, so their union contains at most six coordinates. The existing pure ternary opposite-root overlap theorem below six active coordinates supplies a one-change weave. Hence NOR closes.

Therefore in a counterexample
a != z.

Since the certified cut of x->y is exactly {x,a}, and z is distinct from x and a, the same cut separates x from z:
x in {x,a}, z notin {x,a}.

Thus every surviving endpoint-cycle junction has a canonical shortcut certificate for the two-step chord x->z.

### Consequence

A shortest endpoint-root cycle in a counterexample has no alternating size-two cut junction. Every adjacent two-edge segment
x->y->z
comes equipped with the existing cut {x,a} certifying the shortcut direction x->z.

The remaining endpoint-cycle closure problem is therefore only physical shortcut realization: turn this already-certified two-step chord into an admissible endpoint/protected root, or obtain a spanning one-change order / strict witness improvement. The irreducible alternating-cut branch is eliminated locally.
