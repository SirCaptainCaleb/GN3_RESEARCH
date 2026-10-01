# Reciprocal stretch bound for ascending edges

## Statement

Let H be a finite linear 3-graph on n vertices. For each ascending nonspecial edge e={x,u,v}, write q(e)=phi(e) and p(e)=min{phi(u),phi(v)}. Then q(e)>=2, q(e)<=p(e)<=2q(e)-2, and sum_e (1/(q(e)-1)-1/p(e)) <= 5n/4.

## Body

For t>=2 let R_t be the potential-threshold terminal graph from 1f65fa538544. If uv is an edge of R_t arising from an ascending nonspecial hyperedge e={x,u,v} of rank q=phi(e), then phi(x)=q-1<t, hence q<=t. Also t<=min{phi(u),phi(v)}. The terminal-potential bound a7b7670e955a gives phi(u),phi(v)<=2q-2<=2t-2. Thus every nonisolated vertex of R_t has potential in [t,2t-2].

Each R_t is properly edge-colored and contains no rainbow path of t edges. For t=2 this makes R_2 a matching, so |E(R_2)|<=|V_2|/2. For t>=3, the Ergemlidze-Gyori-Methuku rainbow-path bound e4fb292edb26 gives |E(R_t)|<((9t+5)/7)|V_t|, where V_t={v:t<=phi(v)<=2t-2}.

An ascending edge e of rank q and lower terminal potential p appears in R_t exactly for q<=t<=p. Therefore
sum_e (1/(q(e)-1)-1/p(e))
 = sum_{t>=2} |E(R_t)|/[t(t-1)].
Put c_2=1/2 and c_t=(9t+5)/7 for t>=3. The preceding edge bounds give
sum_{t>=2}|E(R_t)|/[t(t-1)]
 <= sum_v S_{phi(v)},
where
S_p=sum_{t=ceil((p+2)/2)}^p c_t/[t(t-1)].
Now S_2=1/4, S_3=16/21, and S_4=5/4. For t>=3,
c_t/[t(t-1)]=2/(t-1)-5/(7t)=:f(t),
a positive decreasing function. For even p=2r>=4,
S_{2r}=sum_{t=r+1}^{2r}f(t)
and
S_{2r+2}-S_{2r}=f(2r+1)+f(2r+2)-f(r+1)
=-(19r+14)/(14r(r+1)(2r+1))<0.
For odd p=2r+1>=5,
S_{2r+1}=S_{2r}+f(2r+1)-f(r+1)<S_{2r}.
Hence S_p<=S_4=5/4 for every p, proving the bound.

The coarser estimate <=2n follows already from the elementary degeneracy bound |E(R_t)|<=(2t-2)|V_t| and is retained here as an intermediate step rather than a separate tree node.
