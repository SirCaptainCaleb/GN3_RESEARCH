# Flat transfers carry a one-edge blocker memory into the next longest witness

## Statement

Let e={x,y,z} and f be equal-rank q nonspecial edges arising in a flat transfer e to f through their common terminal y, with e ascending and unique entrance x. Then every q-edge longest path P ending in f with last vertex y has, among the final q-2 precursor edges before f, a vertex from {x,z}. Equivalently the previous edge e must reappear in the tail of every such next-state witness through one of its two nonshared vertices.

## Body

The edges e and f share y, and y is terminal for both by 321866bdcbef. The edge f is snake-incoming at y with phi(f)=q>=q-1. Apply the certified terminal tail-blocker lemma c0798e59ef02 to e as the rank-q nonspecial edge terminal at y and f as the competing incoming edge. Every longest path ending in f at y must have e meet one of the final q-2 precursor edges. Since e cap f={y} by linearity and y occurs only in the last edge f of such a path, the additional contact lies in e minus {y}={x,z}.