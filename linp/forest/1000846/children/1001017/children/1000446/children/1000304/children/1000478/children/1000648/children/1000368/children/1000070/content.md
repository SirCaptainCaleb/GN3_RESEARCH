# Low-potential cases of the potential-oriented local bound are humanly reduced

## Statement

Let v have p=phi(v). For potential-charged ascending nonspecial edges e={x,v,u} with phi(u)>=p: if p<=3, at most three such edges exist. If p=4 and four such edges exist, then at most one has rank 3; equivalently the ordered rank pattern is either (3,4,4,4) or (4,4,4,4).

## Body

By the certified central-window packing theorem 6959dc2c0376, for Q in [ceil((p+2)/2),p], the number C_Q(v) of charged ascending nonspecial edges at v of rank at most Q satisfies |C_Q(v)|<=4Q-2p-3. Also every charged edge has rank q between ceil((p+2)/2) and p by a7b7670e955a.

If p=1 or p=2 there are no admissible ascending charged edges of positive rank except trivially fewer than four. If p=3, every charged edge has rank q in {3}; taking Q=3 gives |C_3(v)|<=12-6-3=3. Thus the conjectured local bound holds at every vertex of potential at most 3.

Now let p=4. Every charged edge has rank q in {3,4}. Taking Q=3 gives |C_3(v)|<=12-8-3=1. Hence among any four charged edges, at most one can have rank 3. Therefore a four-edge counterexample at p=4, if one exists, must have ordered ranks (3,4,4,4) or (4,4,4,4).

This replaces the computational evidence in the entire p<=3 regime and isolates the first unresolved potential p=4 to a top-rank multiplicity problem.
