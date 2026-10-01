# Weighted potential-cut inequality for the exact-density layer

## Statement

Let ell>=4, d=floor(2ell/3), and let H be a vertex-minimal exact-density obstruction to S_ell as in a05c50b3ab96. Let w_1,...,w_{ell-1} be arbitrary nonnegative weights and put W(r)=sum_{t=1}^r w_t. Then
sum_{e in E(H)} W(phi(e)) - sum_{e ascending} w_{phi(e)}
<= d sum_{v in V(H)} W(phi(v))
   - sum_{t: emptyset != V_t != V(H)} w_t,
where V_t={v:phi(v)>=t}.

## Body

For every t with V_t a proper nonempty subset, a05c50b3ab96 gives
  M_{>=t}-A_t <= d|V_t|-1,
where M_{>=t}=|{e:phi(e)>=t}| and A_t is the number of ascending edges of rank exactly t.

If V_t=V(H), then trivially
  M_{>=t}-A_t <= |E(H)|=d|V(H)|=d|V_t|.
If V_t is empty then all three quantities vanish.

Multiply the level-t inequality by w_t>=0 and sum over t=1,...,ell-1.

On the edge side,
sum_t w_t M_{>=t}
 = sum_e sum_{t<=phi(e)}w_t
 = sum_e W(phi(e)).
Also
sum_t w_t A_t
 = sum_{e ascending} w_{phi(e)}.

On the vertex side,
sum_t w_t |V_t|
 = sum_v sum_{t<=phi(v)}w_t
 = sum_v W(phi(v)).

Every proper nonempty level contributes the additional strict term -w_t. Therefore
sum_e W(phi(e)) - sum_{e ascending}w_{phi(e)}
<= d sum_v W(phi(v))
   - sum_{t: emptyset != V_t != V(H)}w_t.

No monotonicity of the weights is required; only nonnegativity.

Thus every choice of threshold weights gives a valid dual constraint on an exact-density minimal obstruction. Choosing w_t=1 recovers the first-moment potential inequality. Choosing increasing weights emphasizes top-rank edge mass; sharply localized weights recover individual potential cuts.
