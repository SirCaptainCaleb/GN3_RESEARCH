# 43/48 near-extremizers carry five-eighths switching and lens mass

## Statement

Let (H_j) be a sequence of finite linear 3-uniform hypergraphs. For H_j write
  S_j=sum_v φ(v),  m_j=|E(H_j)|,  n_j^+=|{v:d(v)>0}|.
Assume
  S_j/n_j^+ -> infinity
and
  m_j >= (43/48)S_j-o(S_j).

Choose the maximum endpoint paths and local deficits eta_v from a57007500001. Then
  sum_v eta_v=o(S_j).
Moreover, all but o(S_j) endpoint-potential mass lies on active misaligned vertices v for which the maximum rank q(v) of an ascending nonspecial edge terminal at v satisfies q(v)<φ(v).

For each such vertex choose one maximum-rank ascending terminal anchor and its canonical longest anchor path. Let s(v) be the number of anchor-double / maximum-path-single switching edges supplied by b032348c1a8a. Then
  sum_v s(v) >= (5/8-o(1))S_j.
Consequently the chosen maximum endpoint paths collectively support at least (5/8-o(1))S_j distinct center-indexed balanced endpoint-lens states.

Thus every asymptotic 43/48 near-extremizer carries switching/lens mass of order 5S/8; any global argument forcing a fixed positive proportional loss in this mass improves the 43/48 leading coefficient.

## Body

For each H=H_j use the exact identity of a57007500001. Its main local term is
  4p-2+beta(p)
with beta(p)=floor((11p-16)/8) for p in the stable range, while the omitted small-p corrections are O(1) per nonisolated vertex. Hence
  6m <= (43/8)S-sum_v eta_v+O(n_+),
because every other defect in the exact identity is nonnegative. The hypotheses
  m >= (43/48)S-o(S)
and n_+=o(S) therefore imply
  sum_v eta_v=o(S).                                    (1)

Vertices with bounded potential contribute O(n_+)=o(S), so we may ignore p<8.

If t(v)=0, then by definition eta_v=beta(p)+D_v>=beta(p)=(11/8)p-O(1). Thus (1) implies that the total potential mass on inactive vertices is o(S).

If v is active and aligned, q(v)=p. By b032348c1a8a,
  eta_v>=beta(p)-ceil((3p-4)/4)=(5/8)p-O(1).
Again (1) implies that the aligned potential mass is o(S).

Therefore
  S_mis:=sum_{v active, q(v)<p_v}p_v=S-o(S).            (2)

Now fix an active misaligned vertex v with p=p_v>=8 and q=q(v). Choose a rank-q ascending terminal anchor and a q-edge longest anchor path. The theorem b032348c1a8a gives
  s(v)>=beta(p)-eta_v-a(q),
where a(q)=ceil((3q-4)/4).
Since q<=p-1 and a is increasing,
  s(v)>=beta(p)-a(p-1)-eta_v
      =(5/8)p-O(1)-eta_v.                              (3)

Sum (3) over all active misaligned vertices. Using (1), (2), and n_+=o(S),
  sum_v s(v)
  >=(5/8)S_mis-sum_v eta_v-O(n_+)
  =(5/8-o(1))S.

For each switching edge, b032348c1a8a supplies a balanced endpoint lens attached at its distinct retained vertex on the center's chosen maximum path. Distinct switchers at a fixed center give distinct retained vertices, so the same lower bound counts center-indexed balanced endpoint-lens states.

The conclusion is a stability reduction, not yet a coefficient improvement: a sequence can approach 43/48 only by supporting asymptotically five-eighths of its total endpoint-potential mass in these dense switching/lens configurations.
