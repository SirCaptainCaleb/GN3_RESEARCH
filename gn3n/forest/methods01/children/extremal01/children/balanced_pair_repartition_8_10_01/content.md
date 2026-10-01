# Universal pair balancing at total orders eight and ten

## Statement

Let H be a boundary tournament and let A|B|C be any spanning three-cover. If |A|+|B|=8, then one legal pairwise repartition of A|B replaces their union by two Hamiltonian four-vertex paths. If |A|+|B|=10, then one legal pairwise repartition replaces their union by two Hamiltonian five-vertex paths. Consequently, for total order 8 the quadratic contribution |A|^2+|B|^2 strictly decreases unless {|A|,|B|}={4,4}, and for total order 10 it strictly decreases unless {|A|,|B|}={5,5}. In particular every 3|5 pair has an immediate 4|4 strict descent, and every 4|6 pair has an immediate 5|5 strict descent of exactly two.

## Body

The induced boundary tournament H[V(A) union V(B)] has order |A|+|B|. If this order is eight, apply balanced8_structural01 to partition the union into two Hamiltonian four-sets; choosing Hamilton paths on them gives a legal pairwise repartition, since the union V(A) union V(B) is unchanged and C is untouched. If the union has order ten, apply the certified order-ten result in extremal01 that every ten-vertex boundary tournament admits a partition into two Hamiltonian five-sets. This again gives a legal pairwise repartition preserving the pair union.\n\nFor fixed sum s, the sum of squares a^2+(s-a)^2 is uniquely minimized by the balanced split when s is even. Hence for s=8 every non-4|4 split strictly decreases to 4|4, and for s=10 every non-5|5 split strictly decreases to 5|5. Explicitly, 3^2+5^2-(4^2+4^2)=2 and 4^2+6^2-(5^2+5^2)=2.
