# A whole ascending chord localizes its opposite terminal to the far end of every avoiding rail

## Statement

Let e={x,v,u} be an ascending nonspecial edge of rank r with unique entrance x, so phi(x)=r-1. Let Q=(g_1,...,g_L) be a linear path avoiding v and containing both x and u. Assume x and u do not lie on a common Q-edge (automatic when e is not an edge of Q by linearity).

If x occurs before u along Q, let b be the last index of a Q-edge containing u. Then
L-b+1 <= r-2
in the convention that the reversed suffix g_L,...,g_b has L-b+1 edges and ends at u.
Symmetrically, if u occurs before x and a is the first index of a Q-edge containing u, then
a <= r-2.

Equivalently: delete u from the path-order picture and take the Q-side from u toward the endpoint that does not contain x. That side has at most r-2 edges. Thus for every whole contact pair {x,u} of an external ascending edge on a canonical source rail, the opposite terminal u is forced into an (r-2)-edge end-zone on the side opposite its entrance x.

## Body

Suppose x occurs before u. Consider the reversed suffix
g_L,g_{L-1},...,g_b,
where g_b is the last Q-edge containing u. This is a linear path ending at u, and by the order assumption none of its vertices is x except possibly u itself, which is distinct from x.

Append e after g_b in the reversed orientation. Since Q avoids v and e meets Q only at x and u, while x is absent from the chosen suffix, e meets the suffix exactly at u. Hence
g_L,g_{L-1},...,g_b,e
is a linear path ending at x. Its length is
(L-b+1)+1.
Because phi(x)=r-1,
(L-b+1)+1 <= r-1,
so
L-b+1 <= r-2.

The case u before x is identical using the forward prefix ending at u and then e. The final reformulation is exactly the statement that the side of Q incident with u and avoiding x has length at most r-2.