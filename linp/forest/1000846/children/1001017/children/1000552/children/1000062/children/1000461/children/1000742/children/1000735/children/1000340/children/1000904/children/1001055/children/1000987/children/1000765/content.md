# Near equality in the arbitrary-r fixed-entrance bound forces linear double-contact mass

## Statement

In the arbitrary-r fixed-entrance transfer, suppose |J_q(v)| is within t of the exact local maximum. Then the number of nonsingleton contact sets is at least floor(((r-1)(q-1)-alpha_r(q-3))/2)-t = ((2r-1)/8)q-O_r(1)-t. Moreover the total excess beyond doubles, u+sum_{j>=3}(j-2)n_j, is at most 2t+1. Hence all but O(t+1) of the forced nonsingleton contacts are genuine double contacts; quantitatively n_2>=((2r-1)/8)q-O_r(1)-3t.

## Body


Retain the arbitrary-r fixed-entrance setup of dcf886f98a51. Put
  M=(r-1)(q-1)
for the number of contact vertices in W, and let
  s_max=alpha_r(q-3)
be the exact maximum number of singleton contact sets allowed by the transfer.

For a given configuration write:
- s = number of singleton contact sets;
- n_j = number of contact sets of size j, 2<=j<=r-1;
- N = sum_{j>=2} n_j = total nonsingleton contact sets;
- u = number of unused W-vertices;
- E = u + sum_{j>=3}(j-2)n_j.

Then
  M = s + 2N + E,
and
  |J_q(v)| = 1+s+N
           = 1 + (M+s-E)/2.

Let
  J_max = 1+floor((M+s_max)/2),
the exact local upper bound.

Suppose
  |J_q(v)| >= J_max - t
for integer t>=0.

Since s<=s_max,
  N >= floor((M-s_max)/2)-t.                        (1)

Because
  s_max=((2r-3)/4)q+O_r(1)
and M=(r-1)q+O_r(1), this gives
  N >= ((2r-1)/8)q - O_r(1)-t.                     (2)

Let epsilon=(M+s_max) mod 2. Then
  (s_max-s)+E
   =2(J_max-|J_q(v)|)+epsilon
   <=2t+1.                                          (3)

Hence
  E<=2t+1.                                          (4)

Since
  E=u+sum_{j>=3}(j-2)n_j,
we obtain
  sum_{j>=3}n_j<=2t+1.
Therefore
  n_2 >= floor((M-s_max)/2)-3t-1.                  (5)

Thus all but O(t+1) of the linearly many nonsingleton contacts forced near equality are genuine double contacts.

For t=0, equality in the local fixed-entrance bound forces E<=1 (only parity can contribute), so there is no linear mass of unused vertices or contacts of size at least three, while
  n_2=((2r-1)/8)q+O_r(1).
