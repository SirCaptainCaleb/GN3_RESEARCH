# Potential four satisfies the potential-oriented local bound

## Statement

If phi(v)=4, then v is terminal for at most three potential-charged ascending nonspecial edges e={x,v,u} with phi(u)>=4.

## Body

Assume four such edges exist.

By the p=4 rank-pattern reduction and 07e1382b03d2, the mixed pattern (3,4,4,4) is impossible. Hence all four charged edges have rank four.

Fix a longest path
P=(g_1,g_2,g_3,f_4)
ending in one of them f_4 with last vertex v. Use the notation of 49c24605109f:
g_1={L,M,R}, g_2={R,S,T}, g_3={T,U,V},
where V is the entrance of f_4.

The three-pattern normal form 49c24605109f leaves only patterns (A),(B),(C). Pattern (A) is impossible by aa608665fcba. It remains to exclude (B),(C).

In both remaining patterns, U is a visible entrance of a rank-four ascending edge, so
phi(U)=3.

Pattern (B).
Here R is also a visible entrance. Let
h={R,v,c}
be its charged edge. We claim c is outside V(P).

The edge h already meets g_1 and g_2 at R, so by linearity c lies in neither g_1 nor g_2. It cannot equal T, because then h and g_2 would share R,T. It cannot equal U, because U is the entrance of another charged edge through v, and two edges through v cannot share U. It cannot equal V or the third vertex of f_4, because h and f_4 already share v. Thus c is absent from P.

Now
g_1,h,f_4,g_3
is a four-edge linear path. Consecutive intersections are R,v,V. The nonconsecutive pairs are disjoint: g_1 is disjoint from f_4,g_3; h is disjoint from g_3 because c is outside P and R,v are absent from g_3. Since the last edge g_3 meets its predecessor at V, U can be chosen as the last vertex. Hence phi(U)>=4, contradicting phi(U)=3.

Pattern (C).
Here R is the witness of the unique edge h={a,v,R} whose entrance a is absent from P. Thus a is outside V(P). Again
g_1,h,f_4,g_3
is a four-edge linear path with consecutive intersections R,v,V and all nonconsecutive pairs disjoint. It ends at U, giving phi(U)>=4, again contradicting phi(U)=3.

All pure rank-four patterns are impossible. Together with the mixed-case theorem, four charged edges cannot occur when phi(v)=4.
