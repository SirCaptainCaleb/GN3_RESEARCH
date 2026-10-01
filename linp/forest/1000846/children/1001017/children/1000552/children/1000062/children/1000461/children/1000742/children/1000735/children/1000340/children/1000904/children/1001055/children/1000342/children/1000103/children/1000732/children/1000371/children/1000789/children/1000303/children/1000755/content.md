# Near 43/48, five-eighths switching mass survives without endpoint lenses

## Statement

Let (H_j) be a sequence of finite linear 3-uniform hypergraphs. For H_j write
  S_j=sum_v phi(v),  m_j=|E(H_j)|,  n_j^+=|{v:d(v)>0}|.
Assume
  S_j/n_j^+ -> infinity
and
  m_j >= (43/48)S_j-o(S_j).

Choose the maximum endpoint paths and local deficits eta_v from a57007500001. Then
  sum_v eta_v=o(S_j).
Moreover all but o(S_j) vertex-rank mass lies on active misaligned vertices v for which the maximum edge rank q(v) of an ascending nonspecial edge terminal at v satisfies q(v)<phi(v).

For each such vertex choose one maximum-rank ascending terminal anchor and a longest anchor path. Let s(v) be the number of anchor-double / maximum-path-single switching edges supplied by 411fc64479d2. Then
  sum_v s(v) >= (5/8-o(1))S_j.

Thus every asymptotic 43/48 near-extremizer carries center-indexed switching-edge mass of order 5S/8. No endpoint-lens conclusion is asserted or needed.

## Body

For each H=H_j use the exact identity of a57007500001. Its main local term is
  4p-2+beta(p),
with beta(p)=floor((11p-16)/8) in the stable range, while the omitted bounded-rank corrections are O(1) per nonisolated vertex. Therefore
  6m <= (43/8)S-sum_v eta_v+O(n_+),
because every other defect term in the exact identity is nonnegative. The hypotheses
  m >= (43/48)S-o(S)
and n_+=o(S) imply
  sum_v eta_v=o(S).                                    (1)

Vertices of bounded rank contribute O(n_+)=o(S), so ranks below the stable range may be discarded.

If t(v)=0, then
  eta_v=beta(p)+D_v>=beta(p)=(11/8)p-O(1).
Thus (1) implies that inactive vertices carry only o(S) total vertex-rank mass.

If v is active and aligned, q(v)=p. By 411fc64479d2,
  eta_v>=beta(p)-ceil((3p-4)/4)=(5/8)p-O(1).
Again (1) implies that aligned vertices carry only o(S) total vertex-rank mass.

Hence, writing the sum over active misaligned vertices,
  S_mis=S-o(S).                                        (2)

Fix such a vertex v with p=phi(v), and let q=q(v)<p. Choose a rank-q ascending terminal anchor and a q-edge longest anchor path. The lens-free local theorem 411fc64479d2 gives
  s(v)>=beta(p)-eta_v-a(q),
where a(q)=ceil((3q-4)/4).
Since q<=p-1 and a is increasing,
  s(v)>=beta(p)-a(p-1)-eta_v
      =(5/8)p-O(1)-eta_v.                              (3)

Summing (3) over active misaligned vertices and using (1), (2), and n_+=o(S) gives
  sum_v s(v)
  >=(5/8)S_mis-sum_v eta_v-O(n_+)
  =(5/8-o(1))S.

This is exactly the quantitative switching-mass portion of the former switching/lens stability theorem. The failed automatic endpoint-lens conversion is nowhere used.
