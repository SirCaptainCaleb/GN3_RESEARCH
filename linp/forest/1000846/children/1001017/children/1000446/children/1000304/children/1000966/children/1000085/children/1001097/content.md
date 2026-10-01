# Nonspecial edges on a linear cycle have rank at least the cycle length

## Statement

Let C=(E_1,...,E_c) be a linear cycle of length c>=3 in a linear 3-graph. If E_i is nonspecial, then phi(E_i)>=c. Consequently, if every edge of C is nonspecial, min_i phi(E_i)>=c.

## Body

Fix a nonspecial cycle edge E=E_i. Deleting either one of the two cycle neighbors of E breaks the cycle into a linear path of c-1 edges ending in E. Thus phi(E)>=c-1. If phi(E)=c-1, these two (c-1)-edge paths are both longest paths ending in E, and they enter E through its two distinct cycle joints. That gives two distinct entrance labels for longest paths ending in E, contradicting nonspeciality. Therefore phi(E)>=c.