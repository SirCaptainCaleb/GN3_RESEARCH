# A flat gap-one top edge forces a balanced elementary lens

## Statement

In the setup of 0b1c38ec6184, one may choose the forced two-path overlap so that some elementary lens is balanced. If x lies on a terminal maximum path P_v (or P_u), then the elementary lens adjacent to x between the maximum entrance rail R and that terminal path has equal side lengths. If x lies on neither terminal path, then the two equal-length maximum terminal paths P_u,P_v share u and v and contain a balanced elementary lens. Hence every flat rank-(p-1) edge between potential-p terminals forces a balanced lens to which the no-piercing theorem applies.

## Body

First suppose x lies on P_v. By 0b1c38ec6184, R and P_v have a second common vertex. Choose y so that x,y are consecutive common vertices along the two paths and the resulting cell is a clean elementary lens. Let a be the number of R-edges on the y-to-x suffix and b the number of P_v-edges on the y-to-x segment. Replacing that suffix of R by the P_v segment gives a linear path ending at x of length (p-2)-a+b, so maximality phi(x)=p-2 gives b<=a. Replacing the P_v segment by the R suffix gives a linear path ending at v of length p-b+a, so maximality phi(v)=p gives a<=b. Thus a=b. The P_u case is identical. Now suppose x lies on neither terminal path. Then P_v contains u and P_u contains v. The two paths are both maximum of length p and share at least u,v. Choose an elementary lens between consecutive common vertices. If the lens is internal to both, balance follows from 390e818020e1. If it is an endpoint cell, exchanging its two sides produces endpoint paths whose endpoints are among u,v, both of potential p; the two maximality inequalities again give equality of side lengths. Thus a balanced elementary lens exists in all cases.
