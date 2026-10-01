# Equitable three-cover size profiles are absolute quadratic minima

## Statement

Let C=P_1|P_2|P_3 be a three-cover of an n-vertex boundary tournament. If max_i |P_i|-min_i |P_i|<=1, then Phi(C)=sum_i |P_i|^2 is minimum among all triples of positive integers with sum n, hence among all spanning three-covers of H. In particular C is Phi-minimal in every connected component of the pairwise-repartition graph containing it. Moreover its minimum component order is floor(n/3), so the existence of such a cover forces the maximin minimum-component parameter rho to equal floor(n/3).

## Body

For positive integers s_1+s_2+s_3=n, if some s_i>=s_j+2 then replacing (s_i,s_j) by (s_i-1,s_j+1) changes the sum of squares by -2(s_i-s_j)+2<0. Iterating this purely numerical balancing step terminates exactly at triples whose largest and smallest entries differ by at most one. Therefore those and only those triples minimize the sum of squares at fixed total n. The first conclusion follows for any three-cover with such a size profile. Its minimum component order is floor(n/3). Since no three positive integers with sum n can all be at least floor(n/3)+1, the maximin parameter rho is at most floor(n/3), while C attains that value.
