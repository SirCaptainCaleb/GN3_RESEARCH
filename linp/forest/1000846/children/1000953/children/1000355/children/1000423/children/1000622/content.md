# Two endpoint-chord normal forms for an order-six rainbow-path counterexample

## Statement

Let K_{6,6} have a proper 6-edge-coloring and contain no rainbow P_6. If P=x_0y_0x_1y_1x_2y_2 is a rainbow P_5 whose five edge colors are distinct and alpha is the missing color, then exactly one of two configurations holds: (I) x_0y_2 has color alpha; or (II) both x_0y_1 and x_1y_2 have color alpha.

## Body

Because the coloring is proper and uses six colors on the 6-regular graph K_{6,6}, every color class is a perfect matching.

Let alpha be the unique color absent from P. Consider the alpha-edge incident with the endpoint x_0. If its other endpoint were one of the three right-side vertices outside P, that alpha-edge could be prepended to P, producing a rainbow P_6. Hence the alpha-mate of x_0 lies among y_0,y_1,y_2. It is not y_0, because x_0y_0 is the first edge of P and has one of the five used colors. Therefore the alpha-mate of x_0 is y_1 or y_2.

Similarly, the alpha-edge incident with the endpoint y_2 cannot come from one of the three left-side vertices outside P, or it could be appended to P. Its left endpoint lies among x_0,x_1,x_2, and it is not x_2 because x_2y_2 is the last used-color edge of P. Thus the alpha-mate of y_2 is x_0 or x_1.

Since the alpha-edges form a matching, if x_0 is matched to y_2 then both endpoint requirements are met by the single chord x_0y_2, giving (I). Otherwise x_0 is matched to y_1; then y_2 cannot also be matched to x_0, so its only remaining possibility is x_1, giving (II).

No third configuration is possible. In case (I), P together with x_0y_2 is a rainbow 6-cycle using all six colors. In case (II), the missing color appears on the two forced chords x_0y_1 and x_1y_2.
