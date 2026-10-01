# Weighted bad-load truncation by edge potential

## Statement


Let H be P_ell-free with incidence matrix N. For any nonincreasing weights 1>=g_1>=...>=g_{ell-1}>=0, define G=sum_e g_{phi(e)}, Q(v)=sum_{e nonspecial, entrance(e)=v} g_{phi(e)}, E_L^g=sum_v(Q(v)-L)_+, and S_g=g_1+2sum_{t=2}^{ell-1}g_t. Then
  G <= ((S_g+L+2)/3) rank_R(N)+E_L^g
    <= ((S_g+L+2)/3)n+E_L^g.
The unweighted bad-load truncation inequality is the specialization g_t=1.


## Body


Give each special edge e weight g_{phi(e)}. Give a nonspecial edge e with entrance v weight
  g_{phi(e)} min(1,L/Q(v)),
with the zero convention when Q(v)=0. The total assigned weight is W=G-E_L^g.

Fix a vertex x. Incoming snake incidences of rank t contribute at most g_t each. If c_t counts them and C_q=sum_{t<=q}c_t, the cumulative snake-rank bound gives C_q<=2q-1. Since g_t is nonincreasing, summation by parts yields
  sum_t g_t c_t <= g_1+2sum_{t=2}^{ell-1}g_t=S_g.
Nonspecial edges whose entrance is x contribute at most L. Hence every weighted vertex degree is at most S_g+L. The weighted incidence-rank inequality gives
  W <= ((S_g+L+2)/3)rank_R(N),
and rank_R(N)<=n, proving the theorem.

If g_t=1, then G=m, S_g=2ell-3, Q(v)=q(v), and E_L^g=sum_v(q(v)-L)_+. Equivalently
  m <= ((2ell-1+L)/3)n + E_L.
Thus the earlier bad-load truncation is exactly the constant-weight case, while the weighted form permits distribution-sensitive charging by phi(e).
