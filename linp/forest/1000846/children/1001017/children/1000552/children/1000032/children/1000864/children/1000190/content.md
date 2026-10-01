# Clean entrance-only ascending terminal chords satisfy the three-halves path-slot bound

## Statement

Let P=(g_1,...,g_p) be a maximum p-edge linear path ending physically at v, with last edge h=g_p. Let X(P,v) be the set of ascending nonspecial edges e={x,v,u}, e!=h, for which v is a terminal and
  e∩(V(P)\h)={x},
where x is the unique entrance of e.

Then
  |X(P,v)| <= floor(3p/2).

More precisely, at most p-2 members of X(P,v) have entrance at a path joint outside h, while at most ceil(p/2)+1 have entrance in a path-private slot.

## Body

Distinct edges of X(P,v) have distinct entrances, since all contain v and H is linear.

The joints of P outside h are exactly
  g_i∩g_{i+1}, 1<=i<=p-2,
so at most p-2 members of X(P,v) can use joint entrances.

Now consider private entrances. Outside h there are p path-private vertices: two on g_1, and one on each g_i for 2<=i<=p-1. For each i let z_i be the number of private entrances of X(P,v) lying in g_i. Then
  z_1<=2,
  z_i<=1 for i>=2.
By c265aa8ded39, if z_j>0 then z_{j+2}=0 for every 1<=j<=p-3.

Split the indices 1,...,p-1 by parity. On each parity class the positive z_i form an independent set in a path. The even chain has unit weights and contributes at most the ceiling of half its number of positions. The odd chain also has unit weights except its first position, i=1, has weight at most two; choosing that first position can increase the ordinary independent-set bound by at most one. Consequently the total private contribution is at most
  ceil(p/2)+1.
(Equivalently, pair successive vertices on each parity chain, leaving at most one unpaired unit slot on each chain and one extra unit from the second private vertex of g_1.)

Hence
  |X(P,v)| <= (p-2)+(ceil(p/2)+1)
            = p-1+ceil(p/2).
If p is even this is 3p/2-1, while if p is odd it is (3p-1)/2=floor(3p/2). Thus in all cases
  |X(P,v)|<=floor(3p/2).
