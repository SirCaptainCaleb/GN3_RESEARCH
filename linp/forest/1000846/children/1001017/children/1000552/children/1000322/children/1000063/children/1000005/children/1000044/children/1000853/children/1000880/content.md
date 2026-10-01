# Contact-gap restrictions for a rank-four nonspecial edge against a P5

## Statement

Let Q=(g_1,...,g_5) be a five-edge linear path and let e={x,y,z} be an edge outside Q such that z is absent from Q while x,y lie on Q. Suppose e is nonspecial of rank four with unique entrance x. Record at each path edge whether it contains x (X), contains y (Y), or is disjoint from e (0). Then the X-positions and Y-positions are disjoint blocks of length one or two; every 0-run adjacent to a contact has length at most two; and every 0-run adjacent to a Y-position has length at most one.

## Body

Because H is linear, no path edge can contain both x and y. Since Q is a linear path, the path edges containing a fixed vertex form either one edge or two consecutive edges. Hence the X-positions form a block of length one or two, the Y-positions form a disjoint block of length one or two, and all remaining positions are 0.

Now let g_k be a contact edge, and suppose immediately on one side of g_k there are d consecutive 0-edges before the next contact or the end of Q. Traversing those d edges toward g_k and then appending e gives a linear path of length d+2 ending in e through the label carried by g_k.

Since phi(e)=4, this forces d+2<=4, so every such 0-run has length at most two.

If g_k is a Y-position, then the displayed path enters e through the terminal vertex y rather than through the unique entrance x. A four-edge path of this form would be a longest path ending in e with the wrong entrance. Therefore in the Y-case d+2<=3, so every 0-run adjacent to a Y-position has length at most one.

These are necessary contact-gap restrictions on every spanning P5 avoiding z. They do not assert that Q itself contains a rank-four witness for e: the rank-four witness may use other hyperedges.
