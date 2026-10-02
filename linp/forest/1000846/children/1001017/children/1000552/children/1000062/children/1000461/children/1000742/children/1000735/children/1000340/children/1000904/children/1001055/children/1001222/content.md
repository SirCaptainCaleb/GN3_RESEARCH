# Near-saturated gap-one vertices force a five-eighths switching matching

## Statement

Let v have p=phi(v)=q+1 with q>=4, let T be the ascending nonspecial edges terminal at v with maximum rank q, and let delta=gamma(q)-(t(v)-X_v^T), gamma(q)=floor((11q-5)/8), where X_v^T is excess contact multiplicity of T on a chosen maximum p-path P. For every rank-q anchor path Q ending at v, at least gamma(q)-ceil((3q-4)/4)-delta=(5/8)q-O(1)-delta members of T are double on Q but single on P. Their disjoint non-v pairs form a matching in the anchor precursor crossing from vertices retained by P to vertices omitted by P; hence both sides of this cut have that size.

## Body

Near equality in the fixed-entrance bound forces at least floor(5q/8)-r double contacts on every rank-q anchor, because the non-double members have capacity at most ceil((3q-4)/4). More generally, if T has size t then the number d_Q(T) of anchor-double members is at least t-ceil((3q-4)/4). Any maximum p-path P must meet every rank-at-most-q member of T away from v. Among the anchor-double edges, those that are also double on P contribute at least one unit to X_v^T, so at least d_Q(T)-X_v^T remain single on P. Substituting delta=(gamma(q)-t)+X_v^T gives the displayed five-eighths lower bound. For each such edge both non-v vertices lie in the anchor precursor, while exactly one lies on P; linearity makes these pairs disjoint, producing the crossing matching.