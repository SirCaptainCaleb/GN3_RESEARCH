# Summed potential cuts retain the exact induced-core density defects

## Statement

Let xi_t=|E(H[V_t])|-d|V_t|. For arbitrary nonnegative weights w_t supported on h<t<=L,
  sum_t w_t A_t
  >= sum_t w_t M_{>=t}
     -d sum_t w_t|V_t|
     -sum_t w_t xi_t.
In particular,
  A_{>h}
  >= sum_e(phi(e)-h)_+
     -d sum_v(phi(v)-h)
     -sum_{t=h+1}^L xi_t.
The previously claimed +(L-h) bonus is recovered only under the additional hypothesis xi_t<=-1 at every proper threshold.

## Body

Retain the notation of a05c50b3ab96. Let
  h=min_v phi(v),  L=max_v phi(v),
and for each h<t<=L put
  xi_t=|E(H[V_t])|-d|V_t|.

The repaired levelwise cut inequality is
  A_t >= M_{>=t}-d|V_t|-xi_t.                       (1)

Multiplying by arbitrary nonnegative weights w_t and summing gives
  sum_t w_t A_t
  >= sum_t w_t M_{>=t}
     -d sum_t w_t |V_t|
     -sum_t w_t xi_t.                               (2)

For unit weights on t=h+1,...,L, use the layer-cake identities
  sum_{t=h+1}^L M_{>=t}
    = sum_e (phi(e)-h)_+,
  sum_{t=h+1}^L |V_t|
    = sum_v (phi(v)-h),
and
  sum_{t=h+1}^L A_t=A_{>h}.
Thus
  A_{>h}
  >= sum_e (phi(e)-h)_+
     -d sum_v (phi(v)-h)
     -sum_{t=h+1}^L xi_t.                           (3)

This is the correct unconditional summed potential-cut inequality. If one separately proves xi_t<=-1 for every proper threshold, then (3) recovers the former +(L-h) bonus. Without such an induced-core deficit theorem, that bonus is not justified by vertex-minimality alone.

Special edges still require no separate correction: their rank mass appears in the first term and never in A_{>h}. Their effect is mediated through the actual superlevel core defects xi_t.
