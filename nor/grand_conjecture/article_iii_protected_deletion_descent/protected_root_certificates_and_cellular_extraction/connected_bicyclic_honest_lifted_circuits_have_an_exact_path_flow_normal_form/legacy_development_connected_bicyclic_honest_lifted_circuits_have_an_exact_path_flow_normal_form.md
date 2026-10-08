# Connected bicyclic honest-lifted circuits have an exact path-flow normal form — preserved pre-item development

## Development

## Exact flow normal form for connected bicyclic honest-lifted circuits

Work with a support-minimal positive dependence of honest ternary switch-prism labels
sum_{e in E} lambda_e (rho_e,s_e)=0, lambda_e>0,
where rho_e=e_u-e_v and s_e in {+1,-1}. Assume the physical support graph is connected and bicyclic, so by the preceding cycle-rank theorem its core is a figure-eight or a theta graph.

### Figure-eight

Let the two directed simple cycles be C_1,C_2, meeting only at the articulation vertex x. At every degree-two vertex, flow conservation forces the coefficients on the two incident cycle edges to agree. Hence lambda_e=a on C_1 and lambda_e=b on C_2 for constants a,b>0.

Put S_i=sum_{e in C_i}s_e. The scalar lifted equation becomes a S_1+b S_2=0. Support minimality forbids S_i=0, because then C_i alone is a proper positive lifted subdependence. Thus S_1,S_2 are nonzero and have opposite signs, and a:b=|S_2|:|S_1|.

### Theta graph

Let the branch vertices be x,y, with internally disjoint paths P_1,P_2,P_3. Since every support edge has positive circulation weight, each path is coherently directed. After exchanging names and reversing the whole picture if necessary, exactly two paths P_1,P_2 are directed from x to y, while P_3 is directed from y to x.

Flow conservation makes the coefficient constant on each path: lambda=a on P_1, lambda=b on P_2, lambda=c on P_3. At either branch vertex, c=a+b.

Write T_i=sum_{e in P_i}s_e. The lifted scalar equation is aT_1+bT_2+(a+b)T_3=0, equivalently a(T_1+T_3)+b(T_2+T_3)=0.

The two directed fundamental cycles are C_1=P_1 union P_3 and C_2=P_2 union P_3, with side imbalances S_1=T_1+T_3 and S_2=T_2+T_3. Support minimality forbids S_1=0 or S_2=0. Hence S_1,S_2 are nonzero and opposite, with a:b=|S_2|:|S_1| and c=a+b.

### Consequence

Every full-support connected bicyclic honest-lifted circuit is controlled by only two nonzero opposite-sign integer cycle imbalances. There are no free edge coefficients beyond the path-flow constants above.

This is the coefficient-level normal form for the remaining figure-eight/theta frontier. Any local surgery only has to track how it changes the relevant directed-cycle side sums; the positive circuit coefficients then update automatically.
