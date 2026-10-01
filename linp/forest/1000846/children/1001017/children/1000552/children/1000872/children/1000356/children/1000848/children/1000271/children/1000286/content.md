# Every source-clean rail in a two-rank 0-1-1 block crosses every foreign edge

## Statement

Let e_i={x_i,v,u_i} be 0-1-1 ascending nonspecial edges through common assigned terminal v, with ranks in {q,q+1}. For each i let Q_i be the chosen maximum clean source path ending at x_i. Then for every i!=j, e_j meets Q_i. Otherwise Q_i,e_i,e_j either exceeds phi(e_j) or is a longest e_j-path through the wrong terminal v. Hence a four-edge block creates twelve forced foreign contacts, each using x_j or u_j.

## Body

Let e_i={x_i,v,u_i}, i=1,...,k, be distinct 0-1-1 ascending nonspecial edges through a common terminal v, all assigned to v. Assume their ranks belong to {q,q+1}.

For each i, because the source incidence is clean, choose the globally fixed maximum endpoint path
  Q_i
ending at x_i. Since e_i is ascending,
  |Q_i|=phi(x_i)=phi(e_i)-1.
Because mu_{x_i}(e_i)=0 and e_i cannot be the last edge of Q_i, the two terminals v,u_i are absent from V(Q_i). Indeed if one lay in the final edge of Q_i, that edge and e_i would share x_i and that terminal, violating linearity.

Claim: for every i!=j,
  e_j meets V(Q_i).

Suppose not. Then
  Q_i,e_i,e_j
is linear: Q_i ends at x_i and avoids the terminals v,u_i of e_i; e_i and e_j meet exactly at v; e_j is disjoint from Q_i by assumption.

Its length is
  phi(e_i)+1.

If phi(e_i)=q+1, this length is q+2, exceeding phi(e_j)<=q+1.

If phi(e_i)=q, the length is q+1. If phi(e_j)=q it again exceeds the rank. If phi(e_j)=q+1, it is a longest path ending in e_j but enters e_j through the common terminal v, contradicting that e_j is nonspecial with unique entrance x_j.

Therefore every foreign edge e_j intersects every source-clean rail Q_i.

Since Q_i avoids v, each such contact uses one of the two non-v vertices {x_j,u_j} of e_j.

Thus any four-edge 0-1-1 violation in two consecutive ranks creates twelve forced directed incidences:
for each ordered pair i!=j, Q_i contains x_j or u_j (or both).
