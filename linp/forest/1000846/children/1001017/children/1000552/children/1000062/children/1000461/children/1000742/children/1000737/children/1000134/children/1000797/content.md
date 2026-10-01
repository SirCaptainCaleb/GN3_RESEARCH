# One exceptional entrance supports at most four Type-A ladder vertices

## Statement

Assume every vertex has endpoint potential at least three. Let L be the set of Type-A vertices that fall in the LADDER alternative of 1e24a8fe7b2a.

For each v∈L, let e_v be its unique rank-two nonspecial terminal edge and let x_v be the unique entrance of e_v. Then x_v is non-Type-A.

For every fixed exceptional vertex x,
  |{v∈L:x_v=x}|<=4.
Consequently, if E is the non-Type-A vertex set,
  |L|<=4|E|.

## Body

By 1e24a8fe7b2a, every ladder vertex v has a unique rank-two nonspecial terminal edge e_v whose entrance x_v is non-Type-A.

Fix an exceptional vertex x and put a=phi(x)>=3. Any rank-two nonspecial edge e with unique entrance x is nonascending: if it were ascending, then
  phi(x)=phi(e)-1=1,
contrary to a>=3.

Apply the certified joint snake-incidence and blocker budget ca5f7dc68b1a at x. For every such rank-two nonascending edge,
  w_x(e)=ceil(a/(2-1))-1=a-1.
If r_x is the number of rank-two nonspecial edges with unique entrance x, the budget gives
  r_x(a-1)
  <= |I(x)| + sum_{f∈B^-(x)}w_x(f)
  <=2a-1.
Since a>=3,
  r_x<=floor((2a-1)/(a-1))=2.

Each rank-two hyperedge has exactly two terminal vertices. Hence at most two ladder vertices can choose the same rank-two edge e as their bottom edge. Therefore
  |{v∈L:x_v=x}|<=2r_x<=4.

Summing over exceptional entrances x∈E gives
  |L|<=4|E|.