# Vertex charge and density deficit obey an exact deletion recurrence

## Statement

If |E(H)|=d|V(H)|-r and q_v:=3d-d_H(v), then sum_v q_v=3r. Deleting a vertex w produces new deficit r_prime=r+2d-q_w. Thus at equality, deleting charge K creates deficit 2d-K, and the target charge 2d is exactly the threshold for deletion not to worsen the deficit.

## Body

Fix ell and d=floor(2ell/3). Let H be an n-vertex linear triple system with
  |E(H)|=dn-r,
where r>=0 is the edge deficit from the conjectural d n bound.

Define the deficit charge of a vertex v by
  q_v=3d-d_H(v).

Then degree summation gives
  sum_v q_v
   =3dn-sum_v d_H(v)
   =3dn-3|E(H)|
   =3r.                                             (1)

Thus equality r=0 is exactly the zero-sum charge case. In that case q_v agrees with the leave charge k_v of 588537713840, since d_H(v)=3d-k_v.

Now delete a vertex w. Put
  H'=H-w,
  n'=n-1,
and define r' by
  |E(H')|=dn'-r'.

Since deleting w removes d_H(w)=3d-q_w edges,
  |E(H')|
   =dn-r-(3d-q_w)
   =d(n-1)-[r+2d-q_w].
Therefore
  r'=r+2d-q_w.                                     (2)

Equivalently,
  q_w=2d+r-r'.                                     (3)

So vertex charge is exactly the amount by which deletion improves the naive deficit increase of 2d. At equality r=0, deleting a charge-K vertex creates deficit
  r'=2d-K.

The equality target d_H(w)<=d is q_w>=2d, which by (2) is exactly the condition that deleting w does not increase the deficit:
  r'<=r.
At equality it means r'=0.

More generally, charge amplification and deficit reduction are the same operation viewed in dual coordinates. Any strengthened induction theorem controlling low-degree vertices at deficit r can be fed back through (2) to amplify charges at smaller deficit.
