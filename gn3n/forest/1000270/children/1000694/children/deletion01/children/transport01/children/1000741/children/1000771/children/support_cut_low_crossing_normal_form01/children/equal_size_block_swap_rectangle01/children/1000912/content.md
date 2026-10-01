# Equal-size low-cut swaps yield transport or a five-side escape

## Statement

Let H be a minimum counterexample. Suppose two displayed equal-size two-covers F=P|Q and G=A|B of the same support are support-incompatible, have equal quadratic potential, and G has fewer than three support cuts along P,Q. Then either the reverse support-cut count is at least three, there is order disagreement on a common block, or the two covers form a four-block switch rectangle.

In the switch-rectangle case there are nonempty tight blocks L,X,Y,R with P=(L,X), Q=(Y,R), with the G-supports L union Y and X union R, |L|=|R| and |X|=|Y|. Choose the equivalent description whose exchanged block has order s=min(|X|,|L|).

If s>=2, the displayed joins splice to produce two positioned Hamiltonian supports on three of the four blocks; in a minimum counterexample each has non-Hamiltonian path-cover-two complement.

If s=1, let x,y be the swapped singleton labels. Then there are at least two Hamiltonian five-sets containing {x,y}, each with non-Hamiltonian path-cover-two complement. If |V(H)|>=18, every such five-side state has a complementary path of order at least seven and therefore satisfies the five_side_arbitrary_escape01 trichotomy: strict quadratic-potential descent, neutral endpoint/support exchange, or a displayed-edge reversal.

Thus the equal-size low-cut equal-Phi branch reduces to reverse support complexity, order disagreement, an explicit positioned Hamiltonian support, or—above order seventeen—the standard five-side escape trichotomy.

## Body

The low-cut normal form gives the equal-order terminal-block exchange. Counting cuts in the reverse direction shows that either there are at least three reverse cuts or each G-component contains exactly one reverse cut. If a common block changes its inherited order, this is the order-disagreement outcome. Otherwise the four blocks have the switch-rectangle form
P=(L,X), Q=(Y,R),
with G ordered as one of (L,Y),(Y,L) and independently one of (X,R),(R,X), and with |L|=|R|, |X|=|Y|.

Describe the same support switch using the smaller of the exchanged pairs, so s=min(|X|,|L|). When s>=2, all four blocks have order at least two. The middle block in each relevant splice has length at least two, so the two neighboring displayed joins overlap safely: the first G-component gives either (L,Y,R) or (Y,L,X), while the second gives either (L,X,R) or (Y,R,X). Each is a tight three-block path. In a minimum counterexample each such proper Hamiltonian support has non-Hamiltonian path-cover-two complement by minimum-counterexample calculus.

Now let s=1 and write x,y for the swapped singleton labels. Since a minimum counterexample has order greater than ten, choose any four further vertices distinct from x,y and let U be the resulting six-set. Apply sixset_prescribed_pair_menu01 to U with prescribed pair {x,y}. It gives at least two distinct deletions among the other four vertices for which the remaining five-set is Hamiltonian and still contains x,y. Each such five-set is proper, so minimum-counterexample calculus gives a non-Hamiltonian complement of path-cover number exactly two.

Finally, when n>=18, any two-cover of such a five-set complement has total order n-5>=13, so one component has order at least seven. Applying five_side_arbitrary_escape01 gives strict descent, a neutral support exchange, or a displayed-edge reversal.

Thus the equal-size low-cut equal-Phi branch reduces directly to reverse support complexity, order disagreement, positioned Hamiltonian support, or a five-side escape, without any flank-size assumption in the singleton case.