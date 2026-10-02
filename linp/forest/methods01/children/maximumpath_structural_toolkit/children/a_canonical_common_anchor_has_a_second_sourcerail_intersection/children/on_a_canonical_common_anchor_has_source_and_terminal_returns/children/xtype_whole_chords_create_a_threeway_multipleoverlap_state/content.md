# Reciprocal X-type whole chords create a three-way multiple-overlap state

## Statement

Retain the common-anchor setup of eb7f3a1e87e0. Let
  e={x,v,u}
be terminal-single on the chosen maximum path P_u ending at u, and suppose its reciprocal contact type at u is X, i.e. x lies on P_u and v does not.

Let S_x be a canonical maximum source rail ending at x and R the canonical common anchor precursor containing x and u.

Then every pair among the three maximum endpoint paths
  R, S_x, P_u
has at least two common vertices:
  |R intersect S_x|>=2,
  |R intersect P_u|>=2,
  |S_x intersect P_u|>=2.

More specifically R∩P_u contains both x and u. Thus reciprocal X-type whole chords manufacture a three-way multiple-overlap state on maximum endpoint paths, with one side carrying the distinguished pair {x,u}.

## Body

The first two inequalities are supplied by eb7f3a1e87e0. In reciprocal type X, terminal-singleness at u says x is the unique off-u e-contact on P_u, so x∈V(P_u). Since both x and u lie on R, the pair {x,u} lies in V(R)∩V(P_u).

It remains to show |V(S_x)∩V(P_u)|>=2. Both are maximum endpoint paths, ending at the distinct vertices x and u. They share x because x lies on P_u and is the endpoint of S_x. If x were their unique common vertex, the unique-intersection theorem 5854d853a44b would force x to be an internal joint of S_x, contradicting that x is the last vertex of S_x. Hence there is a second common vertex.

No paid-cell geometry is used.