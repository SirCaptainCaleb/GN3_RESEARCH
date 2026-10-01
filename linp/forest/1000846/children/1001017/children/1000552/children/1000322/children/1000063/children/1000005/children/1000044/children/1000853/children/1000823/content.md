# Class-III nonspecial edges have rank at least four

## Statement

In a 12-vertex 5-regular linear triple system, every nonspecial edge has edge rank at least four. Consequently, in Class III of the n<=12 strict-threshold reduction, a hypothetical nonspecial edge has rank exactly 4 or 5.

## Body

Let e={x,y,z} be nonspecial, with unique entrance x and terminal vertices y,z.

Delete the two terminal vertices y,z and all incident edges. Because H is linear, the only edge through x that contains y or z is e itself: any second edge through x and y (or x and z) would repeat a vertex pair. Hence x has degree
d_{H-{y,z}}(x)=4.

Choose a longest linear path Q in H-{y,z} ending at x, of length s. Apply the certified terminal-degree bound to Q at its last vertex x:
d_{H-{y,z}}(x) <= 2s-1.
Since d(x)=4, this gives
4 <= 2s-1,
so s>=3.

Take the final three edges of an x-ending path of length at least three (or simply a three-edge x-ending prefix oriented toward x). This is a three-edge linear path R ending at x and avoiding y,z. Appending e at x gives a four-edge linear path R,e ending in e through the entrance x. Therefore
phi(e)>=4.

In Class III the global maximum path length is 5, so every nonspecial edge has rank 4 or 5.
