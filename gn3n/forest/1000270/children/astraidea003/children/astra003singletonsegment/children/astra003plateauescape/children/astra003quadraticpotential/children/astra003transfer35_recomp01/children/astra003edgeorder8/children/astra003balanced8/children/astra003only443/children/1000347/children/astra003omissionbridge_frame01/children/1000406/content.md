# Every equitable 5|5|1 state returns to 4|4|3 in two moves

## Statement

Assume the balanced order-eight theorem astra003balanced8. Let H be an eleven-vertex boundary tournament and let P|Q|(x) be a spanning 5|5|1 cover. Then two legal Astra-003 moves transform it into a 4|4|3 cover: first repartition P union {x} arbitrarily as 3|3, then apply the balanced order-eight theorem to one resulting 3-side together with Q to repartition their eight-vertex union as 4|4.

## Body

# A two-move return from 5|5|1 to 4|4|3

Assume the balanced order-eight theorem: every eight-vertex boundary tournament has an exact Hamiltonian 4|4 cover.

Start from a spanning state

P|Q|(x)

with |P|=|Q|=5.

The six-vertex set V(P) union {x} can be partitioned arbitrarily into two three-sets A,B. Every three-vertex boundary tournament has a tight Hamilton path, so A|B is a 3|3 two-path cover of this six-set. Replacing P|(x) by A|B is one legal Astra-003 move. We obtain

A|B|Q

with component orders 3,3,5.

Now the union V(B) union V(Q) has order eight. By astra003balanced8 it has an exact 4|4 cover R|S. Replacing B|Q by R|S is a second legal Astra-003 move, producing

A|R|S

with component orders 3,4,4.

Therefore every equitable omission state lies within two Astra moves of the quadratic-bottom 4|4|3 surface. Combined with the certified-direction bridge 4|4|3 -> 5|5|1, the two order-eleven state surfaces lie in the same connected components whenever astra003balanced8 is available.
