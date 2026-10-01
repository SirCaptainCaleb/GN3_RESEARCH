# Terminal-only singleton ranks two positions apart sum to at least the host potential plus five

## Statement

Let P=(g_1,...,g_p) be a maximum p-edge path ending at v, and let e_1,e_2,e_3 be three ascending nonspecial terminal-only singleton edges through v whose unique contacts occur in this order along P. Write r_i=phi(e_i). Then r_1+r_3>=p+5. Consequently, if all three ranks are at most q, three terminal-only singleton contacts require p<=2q-5.

## Body

Let j_2,l_2 be the first and last path-edge indices containing the unique contact vertex of e_2, so l_2<=j_2+1. Apply the reversed terminal-only inequality f0c177137b7f to e_1 before e_2: l_2>=p-r_1+3. Apply the forward terminal-only inequality df8ad4c65be0 to e_2 before e_3: j_2<=r_3-3. Hence p-r_1+3<=l_2<=j_2+1<=r_3-2, which rearranges to r_1+r_3>=p+5. If r_1,r_3<=q, then p+5<=2q.
