# Every Class-II system is all-special

## Statement

Every 12-vertex 4-regular linear triple system with no five-edge linear path is all-special.

## Body

Assume H is 12-vertex, 4-regular and P_5-free, and suppose e={x,y,z} is nonspecial with unique entrance x.

First, phi(e)>=3. Delete the two terminal vertices y,z. By linearity, among the four edges through x only e contains y or z, so x has degree three in H-{y,z}. If s is the maximum length of a path ending at x in this deletion, the certified terminal-degree bound gives
3<=2s-1,
hence s>=2. Appending e to a two-edge x-ending path avoiding y,z gives a three-edge path ending in e. Thus phi(e)>=3.

The global maximum path length in Class II is four, so phi(e) is 3 or 4.

The rank-four case is impossible by 8f5bb725421d. It remains to exclude rank three.

Assume phi(e)=3 and choose a longest path
P=(g_1,g_2,e)
ending in e through x. Write
g_1={a,b,r},  g_2={r,c,x},  e={x,y,z}.

By d04b5b1b6d44, the six edges through y,z other than e determine two edge-disjoint perfect matchings M_y,M_z on the six-set
S=V(H)\(V(g_1)∪{x,y,z}),
and M_y∪M_z is one alternating C_6. Relabel the cycle vertices s_1,...,s_6 cyclically so c=s_1 and
M_y={{s_1,s_2},{s_3,s_4},{s_5,s_6}},
M_z={{s_2,s_3},{s_4,s_5},{s_6,s_1}}.

The vertices y,z are already saturated at degree four. The vertex c=s_1 has degree three among the known edges: g_2 and the unique y- and z-terminal edges whose matching pairs contain s_1. The entrance x has degree two among the known edges: e and g_2.

Now consider any remaining edge f through a. Besides g_1, exactly three such edges exist. Because f and g_1 already meet at a, linearity forbids f from containing b or r. It cannot contain y or z because those vertices are saturated.

Suppose f avoids both c and x. Then its two vertices other than a lie in S\{s_1}; write them u,v.

Consider the two y-terminal edges whose matching pairs avoid s_1, namely the edges on {s_3,s_4} and {s_5,s_6}. If {u,v} missed one of those two pairs, call the corresponding terminal edge Y. Then
f,g_1,g_2,e,Y
would be a five-edge linear path:
f is disjoint from g_2 because it avoids c=s_1,x,r;
f is disjoint from e because it avoids x,y,z;
f is disjoint from Y by choice;
g_1 is disjoint from e and from every terminal edge by d04b5b1b6d44;
and g_2 is disjoint from Y because Y's pair avoids c.
This contradicts P_5-freeness.

Therefore {u,v} meets both {s_3,s_4} and {s_5,s_6}.

Apply the identical argument to the two z-terminal matching pairs avoiding s_1, namely {s_2,s_3} and {s_4,s_5}. Thus {u,v} also meets both of those pairs.

A two-element set satisfying all four requirements is uniquely
{u,v}={s_3,s_5}.
Indeed the y-conditions require one element from {s_3,s_4} and one from {s_5,s_6}; checking the four possibilities against the z-conditions leaves only {s_3,s_5}.

Hence an edge through a that avoids {c,x} is uniquely forced to be
{a,s_3,s_5}.
The same reasoning applies to b: an edge through b avoiding {c,x} would have to be
{b,s_3,s_5}.
But these two possible edges cannot both occur, since they would share the pair {s_3,s_5}. Therefore among the six distinct remaining edges incident with a or b (three through each), at most one avoids {c,x}. At least five of them contain c or x.

On the other hand, c has current degree three and therefore residual degree one, while x has current degree two and residual degree two. Moreover no edge can contain both c and x because the pair {c,x} already lies in g_2. Thus at most
1+2=3
remaining edges can contain c or x.

This contradicts the required five. Therefore rank-three nonspecial edges do not exist either.

All possible nonspecial ranks have been excluded, so every edge of H is special.