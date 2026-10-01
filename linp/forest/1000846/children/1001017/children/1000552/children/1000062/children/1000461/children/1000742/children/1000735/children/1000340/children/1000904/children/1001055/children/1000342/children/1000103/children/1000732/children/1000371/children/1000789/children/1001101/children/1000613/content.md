# Lens-free flat terminal incidences are paid by local defect

## Statement

For each nonisolated vertex w let eta_w be the local defect from a57007500001. Let C be any set of distinct ordered terminal incidences (h,w) such that h is an ascending nonspecial edge terminal at w and
  phi(h)=phi(w)=p_w.

Then
  |C| <= 4 sum_w eta_w + O(n_+).

More precisely, restricting to p_w>=8,
  |C| <= 4 sum_w eta_w.

Thus in a 43/48 near-extremal sequence, the total number of rank-tight ascending terminal incidences is o(S).

## Body

Fix w with p=phi(w)>=8. If C contains an incidence (h,w), then h is an ascending nonspecial edge of rank p terminal at w. Hence w is active aligned: the maximum rank q(w) of an ascending nonspecial edge terminal at w satisfies
  p<=q(w)<=phi(w)=p.

Let t(w) be the number of ascending nonspecial edges terminal at w. The number of C-incidences ending at w is at most t(w). The exact fixed-entrance bound gives
  t(w)<=gamma(p),
where gamma(p)=floor((11p-5)/8).

By the aligned conclusion of the lens-free dense switching theorem f3588b3a3bc7,
  eta_w>=beta(p)-ceil((3p-4)/4).
For p>=8 one has
  gamma(p)<=4[beta(p)-ceil((3p-4)/4)].
Indeed direct substitution handles p=8,9,10; for p>=11,
  gamma(p)<=11p/8
and
  beta(p)-ceil((3p-4)/4)>=(5p-24)/8,
while 11p<=4(5p-24) for p>=11.
Therefore
  t(w)<=4eta_w.

Summing over p_w>=8 gives the exact displayed bound. Vertices with p_w<8 support only O(1) ascending terminal incidences each, contributing O(n_+).

No switching rotation, endpoint-lens, or flat-output premise is used.