# Sublinear rotation-endpoint reuse would lower the r=3 coefficient to 19/24

## Statement

Let (H_j) be a sequence of finite linear 3-uniform hypergraphs, with
S_j=sum_v phi(v) and n_j^+ the number of nonisolated vertices, and assume S_j/n_j^+ tends to infinity.

For each active misaligned vertex v choose the maximum path, switching family, and rotation-endpoint set R(v) supplied by b032348c1a8a and 5f8d96bf566a. Suppose the maximum reuse multiplicity
M_j=max_w |{v:w in R(v)}|
satisfies
M_j n_j^+=o(S_j).

Then
|E(H_j)| <= (19/24+o(1)) S_j.

In particular, an absolute bound on rotation-endpoint reuse would improve the present 43/48 leading coefficient to 19/24 in the large-potential regime.

## Body

Write p_v=phi(v) and eta_v for the local defect in a57007500001, and put eta=sum_v eta_v. Vertices of bounded potential contribute only O(n_j^+), so all displayed local estimates below may absorb O(1) per vertex.

Partition the nonisolated vertices into inactive vertices, active aligned vertices q(v)=p_v, and active misaligned vertices q(v)<p_v.

For an inactive vertex,
eta_v>=beta(p_v)=(11/8)p_v-O(1),
so in particular
p_v <= (8/5)eta_v+O(1).

For an active aligned vertex, b032348c1a8a gives
eta_v>=beta(p_v)-ceil((3p_v-4)/4)
       =(5/8)p_v-O(1),
and hence again
p_v <= (8/5)eta_v+O(1).

Now let v be active misaligned. The same theorem gives a switching family of size
s(v)>=beta(p_v)-eta_v-a(q(v)),
where a(q)=ceil((3q-4)/4). Since q(v)<=p_v-1,
s(v)>=(5/8)p_v-eta_v-O(1).
Applying the single-blocker rotation packet theorem 5f8d96bf566a,
|R(v)|>=s(v)/2-O(1).
Therefore
(5/8)p_v <= eta_v+2|R(v)|+O(1),
or
p_v <= (8/5)eta_v+(16/5)|R(v)|+O(1).

Summing the three vertex classes yields
S_j <= (8/5)eta+(16/5)sum_v |R(v)|+O(n_j^+).
By the reuse hypothesis,
sum_v |R(v)| <= M_j n_j^+=o(S_j),
and n_j^+=o(S_j). Hence
eta >= (5/8)S_j-o(S_j).

Finally the exact defect identity in a57007500001 gives
6m <= (43/8)S_j-eta+O(n_j^+).
Substituting the preceding bound,
6m <= (43/8-5/8)S_j+o(S_j)
    = (19/4)S_j+o(S_j),
and division by six gives
m <= (19/24+o(1))S_j.

Thus the remaining reuse problem is quantitatively high leverage: any endpoint-reuse bound small compared with the average endpoint potential S_j/n_j^+ already forces a fixed leading improvement.
