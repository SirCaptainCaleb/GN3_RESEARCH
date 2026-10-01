# Lens-free 43/48 switching stability

## Statement

Let (H_j) be a sequence of finite linear 3-uniform hypergraphs. For H_j write
  S_j=sum_v phi(v),  m_j=|E(H_j)|,  n_j^+=|{v:d(v)>0}|.
Assume
  S_j/n_j^+ -> infinity
and
  m_j >= (43/48)S_j-o(S_j).

Choose the maximum endpoint paths and local deficits eta_v from a57007500001. Then
  sum_v eta_v=o(S_j).
Moreover, all but o(S_j) endpoint-potential mass lies on active misaligned vertices v for which the maximum edge rank q(v) of an ascending nonspecial edge terminal at v satisfies q(v)<phi(v).

For each such vertex choose one maximum-rank ascending terminal anchor and a longest anchor path. Let s(v) be the number of anchor-double / maximum-path-single switching edges supplied by the lens-free dense switching theorem f3588b3a3bc7. Then
  sum_v s(v) >= (5/8-o(1))S_j.

Thus every asymptotic 43/48 near-extremizer carries center-indexed switching mass of order 5S/8, with each local switching family a disjoint matching between retained and omitted vertices of one common anchor precursor.

## Body

Use the exact identity of a57007500001. Its main local term is
  4p-2+beta(p),
with beta(p)=floor((11p-16)/8) in the stable range; bounded-p corrections are O(1) per nonisolated vertex. Every remaining defect in that identity is nonnegative. Hence
  6m <= (43/8)S-sum_v eta_v+O(n_+).
The hypotheses
  m >= (43/48)S-o(S),
  n_+=o(S)
therefore imply
  sum_v eta_v=o(S).                                    (1)

Vertices of bounded potential contribute O(n_+)=o(S). If t(v)=0, then
  eta_v=beta(p)+D_v>=beta(p)=(11/8)p-O(1),
so (1) implies that inactive vertices carry o(S) potential mass.

If v is active aligned, q(v)=p. The aligned conclusion of f3588b3a3bc7 gives
  eta_v>=beta(p)-ceil((3p-4)/4)=(5/8)p-O(1).
Again (1) implies that aligned vertices carry o(S) potential mass. Therefore
  sum_{v active, q(v)<p_v} p_v = S-o(S).               (2)

At every active misaligned vertex v of potential p>=8, choose a maximum-rank ascending terminal anchor. The lens-free dense switching theorem f3588b3a3bc7 gives
  s(v)>=beta(p)-eta_v-a(q(v)),
where a(q)=ceil((3q-4)/4).
Since q(v)<=p-1 and a is increasing,
  s(v)>=beta(p)-a(p-1)-eta_v
      =(5/8)p-O(1)-eta_v.                              (3)

Summing (3) over active misaligned vertices and using (1), (2), and n_+=o(S) gives
  sum_v s(v)>=(5/8-o(1))S.

For each center, f3588b3a3bc7 additionally says these switching edges form a matching crossing the retained/omitted cut of the chosen anchor precursor. No endpoint-lens assertion is used.
