# A paired terminal inside its source endpoint lens spends the remaining edge rank

## Statement

Let e={x,v,u} be an ascending nonspecial edge of rank r, with unique entrance x, so phi(x)=r-1. Let S be a maximum (r-1)-edge path ending at x that avoids u and v. Let Q be another maximum endpoint path containing x, and let z,x bound a clean balanced endpoint lens between S and Q, with both lens sides of length t.

Assume u lies in the interior of the Q-side from z to x, and assume the Q-subpath from z to u avoids v. Let a be the number of Q-edges from z to u along that side (choosing the occurrence that precedes x). Then
  t+a+1 <= r.
Equivalently,
  a <= r-t-1.

Thus if an endpoint lens at the entrance of an ascending edge uses almost all of the source rank, its paired terminal cannot lie deep inside a v-avoiding host side: it is forced into the first r-t-1 edges from the far lens boundary z.

## Body

The S-side from z to x and the Q-side from z to x are internally vertex-disjoint by cleanliness. Since S avoids u and v, and e={x,v,u}, the edge e meets the S-side only at x. Because u lies strictly between z and x on the Q-side, the Q-subpath from u back to z avoids x; by hypothesis it also avoids v.

Hence the following is a linear cycle:
  S[z,x], e, Q[u,z].
Its length is
  t+1+a.

The edge e is nonspecial. By f2925a904b8e, every nonspecial edge on a linear cycle has edge rank at least the cycle length. Therefore
  r=phi(e) >= t+a+1,
which rearranges to
  a<=r-t-1.