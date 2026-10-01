# Three same-core star supports exceed the sharp-shell longest order

## Statement

Work in the sharp half-order shell |V(H)|=2lambda+1, and let C be an ordered tight path of order lambda-2. Let e,a,b,c be four distinct vertices outside C. Suppose the three Hamiltonian lambda-supports
V(C) union {e,a},
V(C) union {e,b},
V(C) union {e,c}
admit Hamilton orders with the same ordered interior C, with e occupying one fixed endpoint side in all three orders and a,b,c occupying the opposite endpoint side.

Then H has a tight path of order lambda+1, contradicting maximality of lambda.

Consequently no all-clean five-label shell can contain three same-parity supports forming an active-pair star {e,a},{e,b},{e,c} with the inherited clean orders.

## Body

Reverse all three displayed orders simultaneously if necessary so that the common orders are
(e,C,a), (e,C,b), (e,C,c).
Then (e,C) is tight, and each of (C,a),(C,b),(C,c) is tight.

Apply e425e6ca5fe0 to the tight core C, using a,b as two right extenders and e as a left extender. It gives a Hamilton tight path on
V(C) union {e,a,b}.
Its order is
(lambda-2)+3=lambda+1,
contradicting the definition of lambda as the maximum tight-path order.

The opposite orientation is symmetric.
