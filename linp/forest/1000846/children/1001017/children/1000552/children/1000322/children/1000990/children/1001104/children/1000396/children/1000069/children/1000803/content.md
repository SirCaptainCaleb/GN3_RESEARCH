# Quadratic potential flow becomes an exact charge-potential covariance lower bound

## Statement

With leave charges k_v=(d_U(v)-s)/2 and centered endpoint potentials a_v=phi(v)-d, every exact-density equality obstruction satisfies
  2 sum_v a_v k_v >= n(7d+2)-(6d-1)sum_v a_v-6sum_v a_v^2.
Hence whenever the right side is positive, the obstruction has quantitatively positive covariance between leave charge and endpoint potential.

## Body

Let H be an exact-density equality obstruction with
  |E(H)|=dn,
leave charges
  k_v=(d_U(v)-s)/2,
so that
  d_H(v)=3d-k_v
and
  sum_v k_v=0.

Let
  a_v=phi(v)-d.

The quadratic degree-potential inequality 6d45cc8708c2 states
  sum_v [6phi(v)^2-phi(v)-2(phi(v)+1)d_H(v)-2] >=0.

Substitute
  phi(v)=d+a_v,
  d_H(v)=3d-k_v.
For one vertex the summand becomes
  6(d+a)^2-(d+a)-2(d+a+1)(3d-k)-2
= 6a^2+(6d-1)a-7d-2+2(d+a+1)k.

Summing and using sum_v k_v=0 removes the constant 2(d+1)k term:
  0 <= 6sum_v a_v^2
       +(6d-1)sum_v a_v
       -n(7d+2)
       +2sum_v a_vk_v.

Equivalently,
  2sum_v a_vk_v
  >= n(7d+2)
     -(6d-1)sum_v a_v
     -6sum_v a_v^2.                                (1)

Thus the exact-density obstruction requires positive charge-potential covariance whenever the right side of (1) is positive. In particular, sufficiently small centered-potential first and second moments force positive leave charge to correlate with above-d potential and negative leave charge with below-d potential.

This is consistent with 588537713840, which independently forces every negative-charge vertex below the global top potential and to emit ascending flow. Formula (1) gives the exact quantitative covariance consequence of the quadratic degree-potential inequality.
