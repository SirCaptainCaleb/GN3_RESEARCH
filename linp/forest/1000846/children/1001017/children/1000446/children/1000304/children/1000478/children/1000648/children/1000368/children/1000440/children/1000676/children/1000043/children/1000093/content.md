# The low joints in a 4445 triangle are universally pinned on high-terminal five-paths

## Statement

In the p=5 charged 4445 setting of 0b8e51bfe396, let
  f_b={b,v,u_b}, f_c={c,v,u_c},
with phi(f_b)=phi(f_c)=4, phi(b)=phi(c)=3, and phi(u_b),phi(u_c)>=5.

Let R=(r_1,...,r_5) be any five-edge linear path ending physically at u_b. Then f_b is not the last edge of R, and one of b,v occurs in r_3 union r_4. Moreover, if b occurs in r_3 union r_4, then b must be exactly the joint
  b=r_3∩r_4.
In particular b cannot be private to r_3 or r_4 and cannot be the joint r_4∩r_5.

The symmetric statement holds for c on every five-edge path ending physically at u_c.

## Body

Since phi(f_b)=4, no five-edge path can end in f_b. Thus R does not have f_b as its last edge.

Apply the terminal tail-blocker lemma b5ba2ebc7a66 to the nonspecial rank-four edge f_b and the five-edge path R ending at its terminal u_b. Since f_b is not last, one of its other two vertices b,v occurs among the final q-2=2 precursor edges before r_5, namely in r_3 union r_4.

Suppose b occurs in r_3 union r_4. We use the position-sensitive path-potential bound 8b1790d79d74 on the five-edge path R.

If b is private to r_3, then
  phi(b)>=max{3,5-3+1}=3;
this alone is compatible. But because b lies in the final-two-precursor tail and is not on r_4, the blocker contact with f_b is already completed at r_3. Then the suffix r_4,r_5 followed backwards through f_b?
