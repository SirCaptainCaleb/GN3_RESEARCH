# A double triple-gate C4 braid forces a cross-gate blocker

## Statement

Retain the double triple-gate branch of b6bdb78029f5. Let A be the common same-index joint of Q_0,Q_1,Q_3 at index a, and B the common same-index joint of Q_2,Q_1,Q_3 at index b. Then a≠b. If a<b, the other diagonal Q_0,Q_2 has a common vertex lying on the Q_0 suffix strictly after A and on the Q_2 prefix at or before B. If b<a, symmetrically Q_0,Q_2 has a common vertex lying on the Q_0 prefix at or before A and on the Q_2 suffix strictly after B. Thus the other diagonal must cross the interval between the two triple gates.

## Body

The vertices A and B are distinct. They cannot have the same joint index on Q_1, because a fixed pair of consecutive edges of a linear path has only one intersection vertex. Hence a≠b. Suppose a<b. Write Q_0=(e_1,...,e_r), Q_2=(f_1,...,f_s), and Q_1=(h_1,...,h_t). By the triple-gate conclusion, A=e_a∩e_{a+1}=h_a∩h_{a+1} and B=f_b∩f_{b+1}=h_b∩h_{b+1}. Since Q_2 meets Q_1 uniquely at B and Q_0 meets Q_1 uniquely at A, the sequence f_1,...,f_b, h_b,h_{b-1},...,h_{a+1}, e_{a+1},...,e_r is linear except possibly for intersections between the initial Q_2 prefix and the final Q_0 suffix. If those two pieces were disjoint, this would be a linear path ending at the last vertex of Q_0. Its length would be b+(b-a)+(r-a)=r+2(b-a)>r=phi(x_0), contradicting maximality of Q_0. Therefore the Q_2 prefix through f_b meets the Q_0 suffix beginning with e_{a+1}. This gives the required common vertex. If b<a, use instead e_1,...,e_a, h_a,h_{a-1},...,h_{b+1}, f_{b+1},...,f_s. Its length is a+(a-b)+(s-b)=s+2(a-b)>s, so maximality of Q_2 forces an intersection between the Q_0 prefix through e_a and the Q_2 suffix beginning with f_{b+1}.
