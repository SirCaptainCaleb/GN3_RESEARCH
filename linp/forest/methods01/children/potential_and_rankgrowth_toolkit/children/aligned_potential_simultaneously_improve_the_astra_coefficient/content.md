# Rank-gap mass and aligned potential simultaneously improve the Astra coefficient

## Statement

Let H be a finite linear r-uniform hypergraph, r>=3. For each nonisolated vertex v let p_v=phi(v), let t(v) count ascending nonspecial edges terminal at v, and when t(v)>0 let q(v) be their maximum rank. Let V_0={v:t(v)>0 and q(v)=p_v}, S_0=sum_{v in V_0}p_v, and G=sum_{v:t(v)>0,q(v)<p_v}(p_v-q(v)). Put S=sum_v p_v and c_r=1-(2r-1)/(8r(r-1)). Then
m <= c_r S - (2r-1)/(8r(r-1)) S_0 - (6r-7)/(8r(r-1)) G + O_r(n_+).
For r=3 this is m <= (43/48)S-(5/48)S_0-(11/48)G+O(n_+). Hence any asymptotic extremizer for the Astra coefficient with S/n_+ tending to infinity must satisfy both S_0=o(S) and G=o(S).

## Body

Set alpha=(6r-7)/8 and lambda=(2r-3)/4. Choose the global endpoint paths as in 3b170b2ae6 on aligned vertices and arbitrarily elsewhere, and let X_v be the resulting excess contact multiplicity. If v is aligned, 3b170b2ae6 gives t(v)-X_v <= lambda p_v+O_r(1)=alpha p_v-(alpha-lambda)p_v+O_r(1). If v is active but misaligned, the fixed-entrance theorem applied at a maximum-rank ascending terminal edge gives t(v)-X_v<=t(v)<=alpha q(v)+O_r(1)=alpha p_v-alpha(p_v-q(v))+O_r(1). If t(v)=0 then t(v)-X_v<=0. Summing and using alpha-lambda=(2r-1)/8 yields
(r-1)A-X <= alpha S -(2r-1)S_0/8-alpha G+O_r(n_+).
Since X>=0, A-X <= ((r-1)A-X)/(r-1). The contact-multiplicity identity gives rm <= (r-1)S-(r-2)n_+ +(C-X), and C<=A, hence
m <= [(r-1)+alpha/(r-1)]S/r -(2r-1)S_0/[8r(r-1)]-alpha G/[r(r-1)]+O_r(n_+).
The first coefficient is c_r, while alpha/[r(r-1)]=(6r-7)/[8r(r-1)]. The extremal consequence follows because both correction terms are nonnegative.