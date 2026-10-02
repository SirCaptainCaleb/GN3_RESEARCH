# A late common-terminal blocker on a 4445 high-terminal path forces the low entrance into the center

## Statement

In the 4445 triangle setting, let f_b={b,v,u_b} with phi(f_b)=4 and phi(b)=3. Let
  R=(r_1,...,r_5)
be a five-edge path ending at u_b.

If v∈r_4, then b∈V(R). More precisely,
  b is either the private vertex of r_3 or the joint r_2∩r_3.
In particular b∉r_4.

## Body

Assume v∈r_4.

Suppose first that b∉V(R). Because R ends at u_b, the vertex u_b is private to r_5 and in particular u_b∉r_4. Since f_b also contains u_b, linearity gives f_b∩r_5={u_b}. The vertex v cannot be the joint r_4∩r_5, because then f_b and r_5 would share both v and u_b.

Nor can v=r_3∩r_4. Indeed, under b∉V(R), the sequence
  r_1,r_2,r_3,f_b
is a four-edge linear path: f_b meets r_3 at v, while its other vertices b,u_b are absent from r_1∪r_2∪r_3. This path ends in f_b through the terminal v, contradicting that the nonspecial rank-four edge f_b has unique rank-four entrance b.

Hence v is private to r_4. Therefore f_b meets R exactly in the two vertices v∈r_4 and u_b∈r_5. Apply the j=p-1 case of the certified two-contact rotation lemma a51a7f9cff95. It yields the five-edge linear path
  (r_1,r_2,r_3,r_4,f_b).
This path ends in f_b, contradicting phi(f_b)=4. Therefore b∈V(R).

Now use phi(b)=3 and the position-sensitive path-potential lemma 8b1790d79d74 on the five-edge path R. A private occurrence in r_i gives
  phi(b)>=max{i,6-i},
so with phi(b)=3 the only possible private position is i=3. A joint occurrence r_i∩r_{i+1} gives
  phi(b)>=max{i,5-i},
so the only possible joint indices are i=2,3.

The possibility b=r_3∩r_4 is excluded because v∈r_4 and then r_4 and f_b would share both b and v, violating linearity. Hence b is either private in r_3 or b=r_2∩r_3.