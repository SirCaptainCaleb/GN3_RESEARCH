# Low-φ nonspecial edges force larger-φ adjacency

## Statement

Let H be a linear 3-graph with minimum degree δ. For t>=1 let B_t be the nonspecial edges e with φ(e)=t, and let M_{>t}=|{f:φ(f)>t}|. Then 2(δ-2t+1)_+ |B_t| <= 3(2t-1) M_{>t}.

## Body

Fix e∈B_t. Since e is nonspecial, exactly two vertices x,y of e are last vertices of longest t-edge paths ending with e. At either such vertex x, the cumulative low-φ incidence bound gives at most 2t-1 incident edges f with φ(f)<=t. Hence at least (δ-2t+1)_+ incident edges through x have φ(f)>t. The corresponding sets for x and y are disjoint by linearity. Thus the number of triples (e,v,f), where e∈B_t, v is one of the two snake vertices of e, f contains v, and φ(f)>t, is at least 2(δ-2t+1)_+|B_t|. Conversely, fix f with φ(f)>t. At each v∈f, every e∈B_t counted through v gives a snake incidence (e,v) with φ(e,v)=t. By the cumulative snake bound, at most 2t-1 such e occur at v. Thus f is counted at most 3(2t-1) times.