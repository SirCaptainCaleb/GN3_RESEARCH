# Trapped quadratic minima are fully size-balanced from order eleven through fifteen

## Statement

Let H be a boundary tournament of order n with 11<=n<=15, and let A|B|C be a spanning three-cover minimizing quadratic potential within a connected pairwise-repartition component containing no cover with at most two components. Then, after sorting component orders decreasingly, the profile is uniquely determined by n: n=11 gives 4|4|3; n=12 gives 4|4|4; n=13 gives 5|4|4; n=14 gives 5|5|4; n=15 gives 5|5|5.

## Body

Let a>=b>=c be the three component orders.

By astra003minside_recomp01, since n>=11 every component has order at least three. If c=3, the certified local theorem threeside_trapped_order_le11 gives n<=11 and a,b<=4. Hence at n=11 the only possibility is 4|4|3, while for n>=12 we have c>=4.

For n=12, a+b+c=12 with c>=4 forces a=b=c=4.

For n=13, c>=4 forces the unique sorted profile 5|4|4.

For n=14, c>=4 leaves profiles 6|4|4 and 5|5|4. The first is impossible: the 6|4 pair has total order ten, and the certified universal order-ten theorem in extremal01 repartitions that pair as 5|5. This changes its quadratic contribution from 36+16=52 to 25+25=50, contradicting componentwise Phi-minimality. Thus only 5|5|4 remains.

For n=15, c>=4 leaves profiles 7|4|4, 6|5|4, and 5|5|5. The profile 6|5|4 is impossible because the 6|4 pair again has total order ten and rebalances to 5|5 with strict Phi decrease two. The profile 7|4|4 is impossible by the certified theorem 7f0190e9e532: any two four-vertex paths beside a path of order at least six admit a two-move strict quadratic descent in the same pairwise-repartition component. Hence only 5|5|5 remains.

Thus every trapped componentwise Phi-minimum in this entire order range is forced to the displayed balanced profile.
