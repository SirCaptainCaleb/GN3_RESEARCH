# Potential four counterexamples saturate the five-slot central witness window

## Statement

Let v satisfy phi(v)=4, and let P=(g_1,g_2,g_3,g_4) be a maximum 4-edge path ending at v. For any family of four potential-charged ascending nonspecial edges through v, the path-relative witness construction assigns four distinct witnesses among the five central positions consisting of the private vertices of g_2,g_3 and the joints g_1∩g_2, g_2∩g_3, g_3∩g_4. Moreover any charged edge of rank 3 must use the unique witness g_2∩g_3. Thus in the rank pattern (3,4,4,4), the rank-3 edge is pinned to the middle joint and the three rank-4 edges occupy three distinct remaining central slots.

## Body

Apply the path-relative central-window proof 220a14637b5f with r=4.

For a charged ascending nonspecial edge e={x,v,u} of rank q, choose x as witness if x lies on P and otherwise choose u. Distinct charged edges have disjoint non-v pairs {x,u}, so their chosen witnesses are distinct.

For q=4, the proof localizes private witnesses to positions r-q+2 through q-1, namely private vertices of g_2 and g_3, and joint witnesses to positions r-q+1 through q-1, namely the three joints g_1∩g_2, g_2∩g_3, g_3∩g_4. Hence every rank-4 witness lies in this five-position set.

For q=3, the private interval is r-q+2=3 through q-1=2 and is empty, while the joint interval is r-q+1=2 through q-1=2. Therefore the only possible witness is the middle joint g_2∩g_3.

By 109414e163c7, any four-edge charged configuration at p=4 has rank pattern (3,4,4,4) or (4,4,4,4). Since the witnesses are distinct, four such edges occupy four distinct positions in the five-slot central window. In the first pattern, the rank-3 edge necessarily occupies g_2∩g_3 and the three rank-4 edges occupy three distinct positions among the other four.

One further linearity observation is useful: a charged edge distinct from g_4 cannot use g_3∩g_4 as a witness, because it already contains v∈g_4, and sharing the additional vertex g_3∩g_4 with g_4 would violate linearity. Thus the last-joint slot can only correspond to the path edge g_4 itself when g_4 belongs to the charged family.