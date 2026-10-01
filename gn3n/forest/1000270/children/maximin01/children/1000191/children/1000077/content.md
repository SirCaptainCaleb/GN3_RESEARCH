# The near-end deletions of every 5|4|4 cover are three-crossed, with only three equality geometries

## Statement

Let H be a minimum counterexample in the order-thirteen mu=6 shell and let A|B|C be a spanning 5|4|4 three-cover, A=(a_0,...,a_4). For i=1 and i=3, every exact 6|6 cover of H-a_i has at least three ordinary edges crossing the inherited four-part partition. For i=1, write the inherited class orders as L_1,R_3,B_4,C_4. If equality t=3 holds, exactly one of R,B,C is split and, up to swapping B,C and the cover components, the five block sizes have exactly one of three forms: (I) R=R_1 sqcup R_2 with (B_4+R_2)|(C_4+L_1+R_1); (II) B=B_2 sqcup B'_2 with (C_4+B_2)|(R_3+L_1+B'_2); or (III) B=B_3 sqcup B_1 with (R_3+B_3)|(C_4+L_1+B_1). The i=3 case is symmetric. Otherwise t>=4.

## Body

# The near-end deletions of every 5|4|4 cover are three-crossed, with only three equality geometries

Work in the order-thirteen mu=6 shell. Let
A=(a_0,a_1,a_2,a_3,a_4) | B | C
be a spanning three-cover with orders 5,4,4.

Fix i=1 or i=3 and let T be any exact two-cover of H-a_i. The universal order-thirteen shell makes both T-components have order six. Put
L=A[0,i-1],  R=A[i+1,4].
The inherited classes L,R,B,C are all nonempty, with orders
1,3,4,4
for i=1 and
3,1,4,4
for i=3.

Cut every ordinary T-edge whose endpoints lie in different inherited classes. If b_X is the number of resulting nonempty T-blocks inside class X and t is the number of cut edges, the path-forest transition identity gives
t=sum_X b_X-2.

If any inherited class splits, then sum_X b_X>=5 and hence t>=3.

Suppose instead no class splits. Then all four b_X equal one and t=2. Contracting the four monochromatic blocks gives a forest of two paths with two edges. A 3+1 component-block split would leave a one-block T-component of order at most four, impossible because both T-components have order six. Thus the blocks would have to pair 2+2. But no pair of the orders {1,3,4,4} sums to six: the possible sums are 4,5,7,8. Contradiction. Therefore
t>=3
for both i=1 and i=3.

Now fix i=1 and assume equality t=3. The transition identity gives
sum_X b_X=5.
Exactly one inherited class has two blocks and the other three have one. The singleton class L cannot split, so the split class is R,B, or C.

After contraction there are five blocks and three forest edges. The two component block-counts cannot be 1+4, since a one-block component has order at most four; hence they are 2+3. Therefore one pair of blocks must have total order six, with the remaining three blocks also totaling six.

If R splits, its order three must split 1+2. The block orders are 1,1,2,4,4. The only two-block sum six is 2+4. Thus, up to swapping B,C,
(I)  R=R_1 sqcup R_2, |R_1|=1, |R_2|=2,
and the cover components have block-size form
(B_4+R_2) | (C_4+L_1+R_1).

If B splits 2+2, the block orders are 1,3,2,2,4. Again the only two-block sum six is 2+4. Hence
(II) B=B_2 sqcup B'_2,
with
(C_4+B_2) | (R_3+L_1+B'_2).

If B splits 1+3, the block orders are 1,3,1,3,4. The only two-block sum six is 3+3. Hence
(III) B=B_3 sqcup B_1,
with
(R_3+B_3) | (C_4+L_1+B_1).

These are all positive splittings of B; splitting C is symmetric. The case i=3 follows by reversing A.

Thus every near-end internal deletion of a 5|4|4 cover is universally at least three-crossed, and equality is confined to three explicit five-block geometries.
