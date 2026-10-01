# Human counterexample to the 368-extension search around the 11,11,17,17 gadget

## Statement

The finite-search statement bce2e76b5733 is false. In the base configuration e56c6d0fce1a, adjoining G={v,a_13,c_4} with c_4 new gives five ascending nonspecial edges E_17,F_1,F_2,F_3,G with common last vertex v and ordered ranks (11,11,14,17,17).

## Body

Start from the certified configuration e56c6d0fce1a:
E_i={a_{i-1},b_i,a_i}, 1<=i<=17, v=b_17,
F_1={v,a_10,c_1}, F_2={v,b_16,c_2}, F_3={v,b_15,b_10}.
Adjoin the edge
G={v,a_13,c_4},
where c_4 is new.

This is linear: G meets E_13 and E_14 in the single vertex a_13, meets each of E_17,F_1,F_2,F_3 in the single vertex v, and is disjoint from every other old edge.

We verify G first. In the intersection graph, the new vertex G is adjacent exactly to E_13,E_14 and to the four-clique C={E_17,F_1,F_2,F_3}.

Any induced path ending at G through a_13 cannot contain a member of C earlier, because every member of C is adjacent to G. Also it cannot use both E_13 and E_14 before G, because E_13,E_14,G form a triangle. Hence the longest a_13-entrance path is
E_1,E_2,...,E_13,G,
of length 14.

Any induced path ending at G through v has a penultimate edge in C. Its precursor must avoid E_13,E_14 and all other members of C. For penultimate F_1 or F_3 the longest precursor has length 11, namely the old E_1,...,E_10,F_i route; for F_2 or E_17 the deletion of E_13,E_14 leaves only a short right-hand segment. Thus every v-entrance path has length at most 12. Therefore phi(G)=14 and its unique longest-path entrance is a_13.

Now phi(a_13)=13. The old path E_1,...,E_13 ends at a_13 with a_13 as a last vertex, so phi(a_13)>=13. A path ending at a_13 with a_13 as a last vertex and using G cannot have G earlier and then end in E_13 or E_14, because G is adjacent to both of those last-edge candidates and would create a chord unless it were penultimate; if it were penultimate, the entrance into the last edge would be a_13, so a_13 would not be a last vertex. If the last edge is G, the path must enter G through v, and we just bounded such paths by 12. Thus G creates no a_13-ending path longer than the old ones. In the old graph, direct inspection of the path-plus-clique structure shows that the longest a_13-ending path has length 13: E_1,...,E_13 has length 13, while the only useful detour through F_3 gives E_1,...,E_10,F_3,E_15,E_14, also length 13, and the other clique edges give shorter routes. Hence phi(a_13)=13=phi(G)-1. So G is ascending nonspecial, with v one of its two terminal vertices.

It remains to show that the four old distinguished edges remain ascending.

First, their edge ranks and unique entrance labels do not change. Any new induced path ending at one of h in C and using G must have G immediately before h, since G is adjacent to h. The edge before G must then be E_13 or E_14; no other member of C can occur earlier because C is a clique and is also complete to G.

For h=F_1, the final edge also sees E_10,E_11, so the longest G-containing route has length far below 11 (at most the short segment E_12,E_13,G,F_1).
For h=F_3, the analogous bound uses its contacts E_10,E_15 and is again below 11.
For h=F_2 or E_17, the longest G-containing route is
E_1,...,E_13,G,h,
of length 15.
Thus no G-containing path reaches the old ranks 11,11,17,17. Consequently the ranks and unique entrances remain exactly
F_1: rank 11, entrance a_10;
F_3: rank 11, entrance b_10;
F_2: rank 17, entrance b_16;
E_17: rank 17, entrance a_16.

Finally, the endpoint potentials of these four entrance vertices also remain 10,10,16,16.

For a_10, any G-containing path ending at a_10 has last edge E_10,E_11, or F_1. If the last edge is F_1 then G must be penultimate and the route has length at most 5. If the last edge is E_10 or E_11, a route through G can reach the left side only through E_13 or E_14; allowing one clique predecessor before G gives length at most 8. Hence no new path beats the old value phi(a_10)=10.

The same argument for b_10, whose incident old edges are E_10 and F_3, gives no G-containing endpoint path of length 10, so phi(b_10)=10.

For a_16, the last edge is E_16 or E_17. A G-containing path ending at a_16 has length at most 16. The extremal new possibility is
E_1,...,E_13,G,F_2,E_16,
which has length 16. Thus phi(a_16)=16.

For b_16, the last edge is E_16 or F_2. Again every G-containing route has length at most 16; for example
E_1,...,E_13,G,E_17,E_16
has length 16, and no longer route is possible because any occurrence of G forces all other neighbors of G off the nonconsecutive part of the path. Hence phi(b_16)=16.

Therefore all four old edges remain ascending nonspecial and G is a fifth ascending nonspecial edge with the same last vertex v. Their ordered edge ranks are
11,11,14,17,17.

This directly contradicts the stated exhaustive conclusion of bce2e76b5733. It does not refute the five-edge deficit-doubling conjecture 6cca826aad42, because 2*q_4=34 >= 29=q_1+q_5+1.