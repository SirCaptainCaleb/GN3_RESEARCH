# Potential cuts have an exact three-minus-one incidence count

## Statement

Let H be a finite linear 3-graph and, for t>=1, put V_t={v:phi(v)>=t}. Let M_{>=t} be the number of edges of rank at least t and A_t the number of ascending nonspecial edges of rank exactly t. Then the number I_t of incidences (v,e) with v in V_t and phi(e)>=t is exactly\nI_t=3M_{>=t}-A_t.\n\nIf t>=2, then for every v in V_t,\n#{e contains v: phi(e)>=t} >= d_H(v)-(2t-3),\nwith the right side interpreted as zero if negative. Hence, for t>=2,\nsum_{v in V_t} max{0,d_H(v)-2t+3}\n<=3M_{>=t}-A_t.

## Body

By the potential-cut classification 321022a601f7, every edge e of rank q>t lies wholly inside V_t. Every rank-t edge also lies wholly in V_t unless it is ascending nonspecial; in that exceptional case its unique entrance has potential t-1 and lies outside V_t, while its two terminal vertices lie inside V_t.\n\nTherefore, for every t>=1, each rank-at-least-t edge contributes three incidences to V_t, except each of the A_t ascending rank-t boundary edges, which contributes exactly two. Thus\nI_t=3(M_{>=t}-A_t)+2A_t\n   =3M_{>=t}-A_t.\n\nAssume now t>=2 and fix v in V_t. The certified incident low-rank bound e766796773d9 applied with q=t-1 shows that at most\n2(t-1)-1=2t-3\nincident edges have rank at most t-1. Hence at least\nd_H(v)-(2t-3)\nincident edges have rank at least t, whenever this quantity is positive.\n\nSumming over v in V_t gives the asserted lower bound on I_t for t>=2.