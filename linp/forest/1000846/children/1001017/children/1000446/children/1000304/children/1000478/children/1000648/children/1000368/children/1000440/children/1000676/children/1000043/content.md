# The p=5 pattern 4445 contains a canonical low-high terminal triangle

## Statement

In the p=5 charged pattern (4,4,4,5), with notation from 9a7eac176b49, let
  f_b={b,v,u_b},
  f_c={c,v,u_c}
be the two rank-four charged edges whose forced entrances are
  b=private(g3),
  c=g3∩g4.
Then
  (f_b,g3,f_c)
is a linear 3-cycle with joints b,c,v.

Moreover
  phi(b)=phi(c)=3,
while the opposite terminals satisfy
  phi(u_b)>=5,
  phi(u_c)>=5.
Thus every 4445 obstruction contains a canonical triangle with two low-potential entrance joints and two high-potential outer terminals.

## Body

By 9a7eac176b49, b and c are the unique entrances of two distinct rank-four charged ascending edges through v. Write these edges
  f_b={b,v,u_b},
  f_c={c,v,u_c}.
Because they are charged at v,
  phi(u_b)>=phi(v)=5
and
  phi(u_c)>=5.
Because they are ascending of rank four,
  phi(b)=phi(c)=3.

Now g3 contains b and c. The edge f_b meets g3 at b. It cannot meet g3 at any second vertex, by linearity. Likewise f_c meets g3 exactly at c.

The two charged edges f_b and f_c both contain v and are distinct, so by linearity
  f_b∩f_c={v}.
The three pairwise intersections are therefore
  f_b∩g3={b},
  g3∩f_c={c},
  f_c∩f_b={v},
and b,c,v are distinct.

Hence f_b,g3,f_c form a linear 3-cycle.

This cycle is potential-polarized: its two entrance joints b,c have potential exactly three, whereas the free outer terminals u_b,u_c on the two charged edges have potential at least five.