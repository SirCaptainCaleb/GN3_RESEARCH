# Human classification of one-private-contact fifth edges around the 11,11,17,17 gadget

## Statement

In the 11,11,17,17 base configuration e56c6d0fce1a, no legal fifth edge G={v,b_j,c} with c new and b_j a single private precursor vertex can make G together with E_17,F_1,F_2,F_3 all ascending nonspecial with common last vertex v.

## Body

Use the notation of e56c6d0fce1a:
E_i={a_{i-1},b_i,a_i}, 1<=i<=17, v=b_17,
F_1={v,a_10,c_1}, F_2={v,b_16,c_2}, F_3={v,b_15,b_10}.
Let G={v,b_j,c} with c new. Linearity and the rule that the old precursor vertex is not already used off v exclude j=10,15,16; also j<=14 because the candidate old vertex lies in E_1 union ... union E_16 and b_17=v.

In the intersection graph, G is adjacent exactly to E_j and to the four-clique {E_17,F_1,F_2,F_3}.

We split by j.

1. j<=8.
Any induced path ending at G through the contact b_j must avoid the four-clique before its last edge, so its precursor lies in the ordinary path E_1...E_16. The maximum such length is obtained from the suffix E_16,...,E_j,G and equals 18-j. On the other hand
E_{j+1},E_{j+2},...,E_16,F_2,G
is an induced path of the same length 18-j and enters G through v. No induced path ending at G is longer: if the penultimate edge is E_j, the pure path bound just used applies; if the penultimate edge is one of the four clique edges, all other clique edges and E_j must be avoided, and the longest remaining component gives at most the same length. Thus G has two longest-path entrance labels b_j and v, so G is special.

2. j=9.
The path E_1,...,E_9,G shows that G can be entered through b_9. But the old edge F_1 ceases to be nonspecial:
E_1,...,E_10,F_1
is its old 11-edge longest path entering through a_10, while
E_1,...,E_9,G,F_1
is an 11-edge path entering through v.
Any new path ending at F_1 and containing G must have G immediately before F_1, and its precursor must avoid E_10,E_11 and the other clique edges; hence it has length at most 11. Therefore F_1 still has rank 11 but now has two longest entrance labels, so it is special.

3. j=11.
The two paths
E_1,...,E_11,G
and
E_1,...,E_10,F_1,G
both have length 12 and enter G through b_11 and v respectively. The same neighborhood deletion argument bounds every induced path ending G by 12. Hence G is special.

4. j=12 or 13.
For j>=11, every path ending G through v has length at most 12: the longest possible predecessor is F_1 or F_3, reached by E_1,...,E_10 and then followed by G. A path through b_j has maximum length j+1, realized by E_1,...,E_j,G. Hence for j=12,13, G has rank q=j+1 with unique entrance b_j.

However b_j has endpoint potential strictly larger than q-1. Indeed
E_1,...,E_10,F_3,E_15,E_14,...,E_j
is a linear path ending at b_j, of length 27-j: this is 15 for j=12 and 14 for j=13. Thus phi(b_j)>j=q-1, so G is not ascending.

5. j=14.
Here G has rank 15 and its longest paths through b_14 have length 15, while every v-entrance path has length at most 12. The obstruction is instead that E_17 stops being ascending. The new sequence
E_1,...,E_14,G,F_2,E_16
is a 17-edge linear path ending at a_16. Thus phi(a_16)>=17.

Meanwhile every new induced path ending at E_17 that uses G must have G immediately before E_17. Its precursor must then avoid E_16 and the other clique edges; because G's only nonclique contact is E_14, such a path has length at most
E_1,...,E_14,G,E_17,
namely 16. Therefore no G-containing path raises the edge rank of E_17 above its old value 17, and no new rank-17 entrance into E_17 is created. Its unique entrance remains a_16, but phi(a_16)>=17>16=phi(E_17)-1, so E_17 is no longer ascending.

These cases exhaust every legal one-private-contact candidate G={v,b_j,c}. Thus the one-private-precursor subfamily of the 368-extension search has a complete human explanation: either G is special, G is nonascending, an old low-rank edge becomes special, or the entrance potential of E_17 rises and destroys its ascendingness.