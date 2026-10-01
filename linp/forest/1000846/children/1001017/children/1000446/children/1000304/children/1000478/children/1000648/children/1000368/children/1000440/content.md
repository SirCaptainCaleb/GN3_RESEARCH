# Potential-five charged obstructions have four rank patterns

## Statement

Let phi(v)=5 and suppose four potential-charged ascending nonspecial edges through v exist. Then every such edge has rank 4 or 5, at most three have rank 4, and the ordered rank pattern is one of (4,4,4,5), (4,4,5,5), (4,5,5,5), (5,5,5,5). Moreover, in pattern (4,4,4,5), for any maximum five-edge path P=(g_1,g_2,g_3,g_4,e_5) ending in a rank-five charged edge e_5 at v, the three rank-four path-relative witnesses are exactly the three vertices of g_3: the joints g_2∩g_3, g_3∩g_4 and the private vertex of g_3.

## Body

For any charged ascending edge e of rank q at v, terminal potential satisfies phi(v)<=2q-2 by a7b7670e955a. With phi(v)=5 this gives q>=ceil(7/2)=4. Since v is terminal for e, q<=phi(v)=5. Thus q∈{4,5}.

Apply the certified central-window packing theorem 6959dc2c0376 with p=5 and Q=4. It gives
|C_4(v)| <= 4*4-2*5-3 = 3.
Hence at most three charged edges have rank four. With four edges total, at least one has rank five, giving exactly the four listed ordered patterns.

Now assume the pattern is (4,4,4,5), choose a maximum five-edge path
P=(g_1,g_2,g_3,g_4,e_5)
ending in a rank-five charged edge at terminal v, and apply the path-relative witness localization underlying 6959dc2c0376 to each rank-four charged edge.

For q=4 and p=5, a private witness can occur only in path-edge position
p-q+2=3 through q-1=3,
so the only private slot is the private vertex of g_3.
A joint witness can occur only at joint indices
p-q+1=2 through q-1=3,
so the only joint slots are g_2∩g_3 and g_3∩g_4.

Distinct charged edges have disjoint non-v pairs, hence their selected witnesses are distinct. There are three rank-four edges and exactly three allowed witness vertices. Therefore all three slots are occupied, i.e. the three rank-four witnesses are exactly the three vertices of g_3.
