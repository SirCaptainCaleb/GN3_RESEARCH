# A trapped four-five plateau locks at least eight labels against one common long-path interior

## Statement

Let H be a boundary tournament and let X|Y|P be a spanning three-cover minimizing quadratic potential within a trapped connected pairwise-repartition component, with |X|=4, |Y|=5, and P=(p_1,...,p_a) of order a>=7. Put W=X union Y and M=(p_2,...,p_{a-1}). Then at least eight distinct vertices w in W are noninsertable into the displayed path M. More precisely, for each such w there exists a Hamiltonian four-set A subset W containing w, with Hamiltonian five-set complement B=W-A, such that for C=A-{w} the five-set C union {p_1,p_a} is Hamiltonian while M union {w} is non-Hamiltonian.

## Body

By balanced9_multiplicity36_01, H[W] has at least thirty-six distinct balanced 4|5 partitions A|B. Each yields an equal-Phi state A|B|P in the same trapped component.

Fix one such partition and any w in A. Since a>=7 and A|B|P is Phi-minimal, neither A union {p_1} nor A union {p_a} can be Hamiltonian: either endpoint extension would repartition A|P with orders (4,a) to (5,a-1), changing Phi by 10-2a<0. Apply two_bad_five_extensions_all_opposite01 to the four-set A and exterior labels p_1,p_a. It gives that C union {p_1,p_a} is Hamiltonian for C=A-{w}, for every w in A.

If M union {w} were Hamiltonian, then [C union {p_1,p_a}] | [M union {w}] would be a legal pairwise repartition of A|P with orders (5,a-1), again giving the strict change 10-2a<0. Thus M union {w} is non-Hamiltonian, so w is noninsertable into the displayed path M. Therefore every label lying in the four-side of any one of the at least thirty-six balanced partitions is noninsertable into M and carries the asserted endpoint-pair five-support.

Finally, thirty-six distinct four-subsets cannot all be contained in a seven-element subset of W, because binom(7,4)=35. Hence the union of these four-sides contains at least eight distinct vertices of W. Those eight vertices have the claimed simultaneous common-interior lock.
