# Distance-three entrance rails meet at the intervening cycle terminal

## Statement

Retain the entrance-rail lens-free flat gap-one terminal cycle
  e_i={x_i,t_i,t_{i+1}}
and canonical entrance rails R_i from 315871ed0c8b.

Then for every i,
  t_{i+2} belongs to V(R_i) intersect V(R_{i+3}).

Moreover, in the lens-free residual this is the unique common vertex:
  V(R_i) intersect V(R_{i+3})={t_{i+2}}.
Consequently t_{i+2} is an internal aligned joint of R_i and R_{i+3} at one common index h_i, and
  h_i <= p-4.

In particular, if the flat terminal cycle has length five, all five entrance rails are pairwise intersecting and every pair intersects uniquely: adjacent pairs meet at the anonymous aligned joints y_i from 960a5153b900, while nonadjacent pairs meet at the labeled cycle terminals supplied above.

## Body

By 315871ed0c8b, on R_i the forward adjacent cycle edge e_{i+1} is an exact single blocker with
  e_{i+1} intersect V(R_i)={t_{i+2}}.
Hence t_{i+2} lies on R_i.

Apply the same lemma to R_{i+3}. Its backward adjacent edge is e_{(i+3)-1}=e_{i+2}, and
  e_{i+2} intersect V(R_{i+3})={t_{(i+3)-1}}={t_{i+2}}.
Hence t_{i+2} also lies on R_{i+3}.

If R_i and R_{i+3} had a second common vertex, two equal-length maximum endpoint rails would contain an elementary balanced lens, contrary to the lens-free residual. Thus their only common vertex is t_{i+2}. The universal unique-intersection alignment theorem 5854d853a44b now makes t_{i+2} a joint at the same index h_i on both rails.

Finally, 315871ed0c8b already places the first R_i-edge containing t_{i+2} at index at most p-4. Since t_{i+2} is an internal joint at level h_i, its first occurrence is edge h_i, so h_i<=p-4.

For a cycle of length five, any two rail indices differ by 1,2,3, or4 modulo five. Differences 1 and4 are adjacent and covered by 960a5153b900; differences 2 and3 are distance three in one orientation and are covered by the present statement. Hence every rail pair intersects uniquely.
