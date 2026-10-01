# Doubled rotation packets halve the endpoint-congestion penalty

## Statement

Let (H_j) be a sequence of finite linear 3-graphs with
  S_j=sum_v phi(v),
  n_j^+=number of nonisolated vertices,
and S_j/n_j^+ tending to infinity.

For every active misaligned vertex v, choose the switching family and the doubled rotation-endpoint packet R(v) supplied by b032348c1a8a and 465568d6d8dc. Let
  M_j=max_w |{v:w in R(v)}|.
Then
  |E(H_j)|
  <= (19/24)S_j + (M_j/6)n_j^+ + o(S_j).

More generally the pointwise maximum may be replaced by any aggregate bound
  sum_v |R(v)| <= K_j n_j^+,
giving
  |E(H_j)| <= (19/24)S_j + (K_j/6)n_j^+ + o(S_j).

Thus any estimate
  K_j < (5/8-o(1)) S_j/n_j^+
already yields a strict asymptotic improvement over 43/48; sublinear congestion K_j=o(S_j/n_j^+) recovers 19/24.

## Body

Let p_v=phi(v) and eta_v be the exact local defect of a57007500001.

Inactive and active aligned vertices obey
  p_v <= (8/5)eta_v+O(1)
as in e233684ca13b.

For an active misaligned vertex, b032348c1a8a gives a switching family of size
  s(v)>=(5/8)p_v-eta_v-O(1).
By 465568d6d8dc the doubled endpoint packet satisfies
  |R(v)|>=s(v)-O(1).
Hence
  (5/8)p_v <= eta_v+|R(v)|+O(1),
or
  p_v <= (8/5)eta_v+(8/5)|R(v)|+O(1).

Summing all vertices,
  S_j <= (8/5)eta+(8/5)sum_v|R(v)|+O(n_j^+).
Under sum_v|R(v)|<=K_j n_j^+,
  eta >= (5/8)S_j-K_j n_j^+-O(n_j^+).

The exact defect identity gives
  6m <= (43/8)S_j-eta+O(n_j^+).
Substitution yields
  6m <= (19/4)S_j+K_j n_j^+ + O(n_j^+),
and division by six proves the displayed estimate. Taking K_j=M_j gives the pointwise-reuse form.

Finally 43/48-19/24=5/48. The congestion error K_j n_j^+/(6S_j) is strictly below 5/48 precisely when
  K_j < (5/8) S_j/n_j^+
up to lower-order terms.