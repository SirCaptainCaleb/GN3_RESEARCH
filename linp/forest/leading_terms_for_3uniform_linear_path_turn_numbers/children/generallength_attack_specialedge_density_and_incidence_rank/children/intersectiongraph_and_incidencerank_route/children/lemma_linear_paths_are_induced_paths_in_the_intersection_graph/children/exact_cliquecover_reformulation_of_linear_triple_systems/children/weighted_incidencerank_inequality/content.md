# Weighted incidence-rank inequality

## Statement

Let H be a linear 3-uniform hypergraph with incidence matrix N. Assign weights 0<=w_e<=1 to its edges, let W=sum_e w_e, and let d_w(v)=sum_{e contains v} w_e. If d_w(v)<=D for every vertex v, then rank_R(N) >= 3W/(D+2). Consequently W <= (D+2)|V(H)|/3.

## Body

Proof. Let R=diag(w_e) and Q=R^{1/2}N^T N R^{1/2}. Then Q is positive semidefinite and rank Q<=rank N. Since every edge has size 3, tr Q=3W. By linearity, Q_ee=3w_e, while for e!=f the entry Q_ef is sqrt(w_e w_f) exactly when e and f intersect. Hence tr(Q^2)=9 sum_e w_e^2 + 2 sum_{e<f, e intersect f} w_e w_f. Also sum_v d_w(v)^2 = 3 sum_e w_e^2 + 2 sum_{e<f, e intersect f} w_e w_f, since each intersecting pair has a unique common vertex. Therefore tr(Q^2)=6 sum_e w_e^2 + sum_v d_w(v)^2. Because 0<=w_e<=1, sum_e w_e^2<=W; because d_w(v)<=D, sum_v d_w(v)^2<=D sum_v d_w(v)=3DW. Thus tr(Q^2)<=3(D+2)W. For a positive semidefinite matrix, rank Q >= (tr Q)^2/tr(Q^2), so rank N >= 3W/(D+2). Finally rank N<=|V(H)|.