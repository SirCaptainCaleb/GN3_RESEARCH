# Low-support-cut two-cover comparisons have rigid quadratic normal forms

## Statement

Let F=P|Q and G=A|B be two two-covers of the same vertex set, with displayed orders on P,Q and |P|=p>=q=|Q|. Call a consecutive pair of vertices of P or Q a support cut if its two vertices lie in different component supports of G, and let kappa be the total number of such support cuts.

If the unordered support partitions of F and G differ, then kappa>=1. When kappa<=2, the support change is completely classified.

(1) If kappa=1, one displayed path is split once and the other is monochromatic for the G-support partition. Thus G is obtained supportwise by moving one nonempty terminal block of one F-component into the other. If the donor and recipient have orders a and b and the transferred block has order t, then
Phi(G)-Phi(F)=2t(t-(a-b)).
Hence an equal-Phi one-cut move exists only from the larger component to the smaller one, with t equal to the component-size gap.

(2) If kappa=2 and both cuts lie on P, write P=L M R with L,M,R nonempty and m=|M|. The two ends L,R have one G-color and M the other. If Q has the color of M, then the G-support orders are p-m and q+m and
Phi(G)-Phi(F)=2m(m-(p-q)).
If Q has the color of L,R, then the G-support orders are m and p+q-m and
Phi(G)-Phi(F)=2(m-p)(m-q).
The symmetric formulas hold when both cuts lie on Q.

(3) If kappa=2 with one cut on each of P,Q, then each G-support is the union of one terminal block of P and one terminal block of Q. If one G-support has order s, then
Phi(G)-Phi(F)=2(s-p)(s-q).
In particular, equality of Phi holds exactly when s is p or q; equivalently, the move exchanges terminal blocks of P and Q of equal order.

Consequently, for equal-Phi comparisons with |p-q|<=1, every support-incompatible comparison with fewer than three support cuts is one of the following explicit neutral moves: if p=q, an exchange of equal-order terminal blocks; if p=q+1, either a terminal singleton transfer from P to Q, an internal singleton transfer from P to Q obtained by cutting on both sides of that singleton, or an exchange of equal-order terminal blocks. Therefore any other support disagreement in a near-balanced equal-Phi pair has at least three support cuts.

## Body

Color every vertex of P union Q by the G-component support A or B containing it. The support-cut count kappa is exactly the number of color changes along the displayed orders P and Q.

If the F- and G-support partitions differ, at least one displayed path is not monochromatic, so kappa>=1.

Suppose kappa=1. Exactly one of P,Q changes color, and it changes once. Thus, after possibly exchanging the names of P,Q and reversing which terminal block is called the transferred block, one path is L T and the other path lies entirely in the same G-support as L. Supportwise, G is obtained by moving the terminal block T of order t from a donor of order a to a recipient of order b. The changed pair of component orders is
(a,b) -> (a-t,b+t),
so
Phi(G)-Phi(F)
=(a-t)^2+(b+t)^2-a^2-b^2
=2t(t-(a-b)).
The equal-Phi claim follows immediately.

Now suppose kappa=2 and both cuts lie on P. The binary color word on P has exactly two changes, so
P=L M R
with L,M,R nonempty, L and R of one color, and M of the other. The path Q is monochromatic.

If Q has the color of M, the new support orders are p-m and q+m, where m=|M|. Therefore
Phi(G)-Phi(F)
=(p-m)^2+(q+m)^2-p^2-q^2
=2m(m-(p-q)).

If Q has the color of L,R, the new support orders are m and p+q-m. With n=p+q,
Phi(G)-Phi(F)
=m^2+(n-m)^2-p^2-q^2
=2(m-p)(m-q).
The case of two cuts on Q is symmetric.

Finally suppose there is one cut on each of P,Q. Write
P=P_1 P_2,  Q=Q_1 Q_2
with all four blocks nonempty. Since each displayed path changes color once, every G-support contains one P-block and one Q-block. Let one support have order s. Since the total order is n=p+q, the other support has order n-s, and
Phi(G)-Phi(F)
=s^2+(n-s)^2-p^2-q^2
=2(s-p)(s-q).
Thus Phi is unchanged exactly when s=p or s=q. If, for example, the chosen support is P_1 union Q_1 and s=p, then |Q_1|=|P_2|; if s=q, then |P_1|=|Q_2|. The other possible pairing is identical after swapping one terminal block choice. Hence every equal-Phi two-cut comparison with one cut on each path exchanges terminal blocks of equal order.

For the near-balanced corollary, first take p=q. The one-cut equality condition would require a transferred block of order zero, impossible. In the two-cuts-on-one-path case, the first formula requires m=0 and the second requires m=p=q, impossible because the middle block is proper. Hence only the equal-order terminal-block exchange remains.

Now take p=q+1. A one-cut equal-Phi move transfers exactly one terminal vertex from P to Q. For two cuts on P, the first same-path formula gives equality only at m=1, which is an internal singleton transfer. The second same-path formula would require m=q, leaving |L|+|R|=1 although both L and R are nonempty, impossible. Two cuts on Q cannot be neutral by the symmetric formulas. The one-cut-on-each-path case is exactly the equal-order terminal-block exchange already proved.

Thus, after these explicit neutral moves are removed, every support-incompatible equal-Phi comparison with size gap at most one has at least three displayed support cuts.
