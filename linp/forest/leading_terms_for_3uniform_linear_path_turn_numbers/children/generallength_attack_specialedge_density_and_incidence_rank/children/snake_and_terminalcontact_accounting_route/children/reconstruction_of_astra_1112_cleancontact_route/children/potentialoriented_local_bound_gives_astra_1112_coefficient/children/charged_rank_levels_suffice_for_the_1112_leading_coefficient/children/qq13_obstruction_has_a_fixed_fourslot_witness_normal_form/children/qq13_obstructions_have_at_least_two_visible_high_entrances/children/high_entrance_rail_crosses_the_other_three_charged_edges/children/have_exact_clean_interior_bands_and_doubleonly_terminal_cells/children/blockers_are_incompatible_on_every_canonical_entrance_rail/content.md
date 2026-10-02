# Distance-two single blockers are incompatible on every canonical entrance rail

## Statement

Let h={y,v,z} be an ascending nonspecial edge of rank Q>=3 with unique entrance y, and let R=(r_1,...,r_{Q-1}) be a canonical entrance path ending at y and avoiding v,z, so R,h is a longest Q-edge path ending in h.

Let f_1,f_2 be distinct edges through v, neither equal h. Suppose each f_i meets V(R) in exactly one vertex, private to r_{a_i}. Then |a_1-a_2|!=2.

## Body

Assume a_2=a_1+2 and write a=a_1.

Consider
  r_1,...,r_a,f_1,f_2,r_{a+2},r_{a+3},...,r_{Q-1}.

The omitted edge r_{a+1} separates the inherited prefix and suffix. Each f_i has exactly one R-contact, private in its indicated edge, and f_1,f_2 are distinct edges through v, so f_1∩f_2={v}. Since the canonical rail R avoids the terminal v of h, v is outside R. Hence the displayed sequence is linear.

Its length is
  a+2+[(Q-1)-(a+2)+1]=Q.

Its last edge is r_{Q-1}. The entrance y is a last vertex there and cannot lie in either f_i, because each f_i already shares v with h and linearity would forbid also sharing y with h.

Thus phi(y)>=Q. But h is ascending of rank Q, so phi(y)=Q-1, contradiction.