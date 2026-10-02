# Single-contact path rotations bound total contact-potential drop

## Statement

Let H be a finite linear 3-graph, phi its endpoint potential, and P=(g_1,...,g_p) a maximum path ending at v. Let E_v be a family of distinct edges e through v, different from the last edge of P, each meeting V(P) exactly in {v,z_e}. Then
sum_{e in E_v} (p-phi(z_e))_+ <= 12p.
In particular, for ascending edges e={x,v,u} of rank r<p that are terminal-single on P: entrance contacts contribute p-r <= p-phi(x), and opposite-terminal contacts contribute (p-phi(u))_+. The bound holds for any subfamily of these contacts.

## Body

All lengths count hyperedges. For a vertex z on P, let a(z) and b(z) be the first and last indices of host edges containing z. Then b(z)<=a(z)+1. The z_e are distinct: two edges already share v, so another common vertex would violate linearity.

Partition the contacts into six classes, by parity of a(z), and by one of three slots for contacts with the same first index. Each host edge has at most three vertices, so three slots suffice. In each class the first indices are distinct and differ by at least two. Write consecutive contacts z_j,z_i in increasing first-index order, with a_i>=a_j+2.

Concatenate the P-prefix through g_{a_j}, ending at z_j; edge e_j from z_j to v; and the reversed P-suffix beginning with g_{b_i} and ending at z_i. Its length is a_j+1+(p-b_i+1)=p+a_j-b_i+2. This is a linear path: the prefix and suffix have disjoint host-edge blocks separated by at least one edge; e_j meets P only at z_j and v, and its third vertex is outside P. The last endpoint z_i is a free vertex of the final suffix edge after reversal. Therefore phi(z_i)>=p+a_j-b_i+2, and
(p-phi(z_i))_+ <= a_i-a_j.
The first contact in a class contributes at most p. The remaining contributions telescope to at most p. Hence each class contributes at most 2p and six classes at most 12p. Empty classes cause no issue.

For an ascending edge with entrance x, phi(x)=r-1, so p-r <= (p-phi(x))_+ when r<p. For an opposite-terminal contact z=u the displayed term is exactly (p-phi(u))_+. No cycle bound, payment allocation, or independence between source paths is used.