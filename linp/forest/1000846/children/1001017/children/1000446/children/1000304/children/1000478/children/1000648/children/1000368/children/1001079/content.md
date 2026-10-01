# Certified low-potential case of the potential-oriented local bound

## Statement

If v has endpoint potential p=phi(v)<=3, then v is terminal for at most three potential-charged ascending nonspecial edges e={x,v,u} with phi(u)>=p.

## Body

Use the certified cumulative terminal-incidence bound 0e550ff0eadd: for every vertex v and every integer 2<=q<=phi(v), the number of nonspecial edges e for which v is terminal and phi(e)<=q is at most 2q-3.

For p=phi(v)=1 there is no nonspecial edge of rank at most p: rank-one edges are special.

For p=2, every charged ascending edge e at v has phi(e)<=p=2 (the standard two-point-transversal/appendability argument for a charged edge gives q<=p). Applying 0e550ff0eadd with q=2 gives at most 1 such nonspecial terminal edge.

For p=3, every charged ascending edge likewise has rank at most 3. Applying 0e550ff0eadd with q=3 gives at most
2*3-3=3
nonspecial terminal edges in total. The charged ascending edges form a subfamily, so there are at most three.

Thus the potential-oriented local bound is fully proved for phi(v)<=3 without any central-window packing estimate. This argument is independent of the disputed 4Q-2p-3 packing count and remains valid under the corrected packing ranges.