# Ascending flow gives a levelwise charge-to-superlevel growth inequality

## Statement

For L_p={v:phi(v)=p} and V_{p+1}={u:phi(u)>=p+1}, one has 2 sum_{v in L_p} max(0,d_H(v)-2p+1) <= (2p-1)|V_{p+1}|. At exact density d_H(v)=3d-k_v, this becomes 2 sum_{L_p} max(0,3d-k_v-2p+1) <= (2p-1)|V_{p+1}|. Thus low-potential negative charge forces quantitative growth of higher potential superlevels.

## Body

Let H be a finite linear 3-graph. For p>=1 define
  L_p={v:phi(v)=p},
  V_{p+1}={u:phi(u)>=p+1}.

For v∈L_p, the certified incident low-rank count says that at most
  2p-1
incident edges have rank at most p. Every remaining incident edge has rank p+1 and, by the one-step incidence-rank characterization, is an ascending nonspecial edge with unique entrance v. Hence if c_p(v) is the number of rank-(p+1) ascending edges sourced at v,
  c_p(v) >= max{0,d_H(v)-(2p-1)}.                  (1)

Each such source edge has two terminal vertices, and each terminal has endpoint potential at least p+1. Therefore the edges sourced from L_p contribute
  2 sum_{v∈L_p} c_p(v)
terminal incidences into V_{p+1}.

Fix u∈V_{p+1}. Every one of these incoming edges is nonspecial, terminal at u, and has rank exactly p+1. The certified cumulative nonspecial-terminal bound 0e550ff0eadd, applied with q=p+1, gives at most
  2(p+1)-3=2p-1
nonspecial terminal edges of rank at most p+1 at u. Hence u receives at most 2p-1 of the above terminal incidences.

Summing over u∈V_{p+1},
  2 sum_{v∈L_p} c_p(v)
  <= (2p-1)|V_{p+1}|.
Combining with (1),
  2 sum_{v∈L_p} max{0,d_H(v)-2p+1}
  <= (2p-1)|V_{p+1}|.                              (2)

At exact density, write d_H(v)=3d-k_v. Then
  2 sum_{v∈L_p} max{0,3d-k_v-2p+1}
  <= (2p-1)|V_{p+1}|.                              (3)

Thus negative charge in a low potential layer quantitatively forces population in higher potential layers. Formula (3) is a levelwise reproduction/absorption inequality for the ascending DAG.
