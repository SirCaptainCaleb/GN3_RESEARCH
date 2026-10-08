# Antipodal braid exits preserve the entire outside order — preserved pre-item development

## Development


In the flat d=e=3 antipodal backtrack, subsection 221 gives the caged braid-hexagon on local coordinates a,b,x,y,c,d and its two protected exits

L=(x,a,b,y,c,d),
R=(a,b,x,c,d,y).

The important global bookkeeping is stronger than preservation of one boundary pair:

Each exit is obtained by permuting only the six displayed local coordinates. Every coordinate outside this packet remains in exactly the same relative order as in the original full order.

Moreover:

- L preserves the ordered right boundary pair (c,d) exactly. Therefore every ternary window strictly to the right of the packet is unchanged. The only possible new incompatibility is exported through the two left reconnection windows meeting the new first local coordinates x,a.

- R preserves the ordered left boundary pair (a,b) exactly. Therefore every ternary window strictly to the left of the packet is unchanged. The only possible new incompatibility is exported through the two right reconnection windows meeting the new final local coordinates d,y.

Thus neither exit changes the outside permutation data, resets the threshold phase, or introduces hidden disturbances on both sides. Each move is a genuinely one-sided protected transport.

The remaining antipodal-backtrack problem is therefore exactly a boundary-reconnection problem on the exported side. In the current strategy this should be analyzed by the g=1 reconnection case and the two exits: for each exit, prove that the two exported reconnection windows either already match the threshold and finish, or define a strictly improved protected state under the chosen boundary-descent potential.

No further local permutation inside the braid hexagon is needed; all six braid chambers are already caged.
