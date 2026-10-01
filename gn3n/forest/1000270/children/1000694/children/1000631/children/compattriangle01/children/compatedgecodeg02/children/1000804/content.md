# Two common compatibility neighbors force an order-reversal separator

## Statement

Let F_a,F_b be compatible deletion covers in a boundary tournament with pc(H)>2, and suppose their compatibility-graph edge ab has two distinct common neighbors c,d. Then c,d are the two vertices flanking the common insertion slot of a and b in the common restored support. The covers F_c and F_d induce the same support partition and agree on the relative order of every pair of common vertices except possibly a,b. If F_c and F_d are incompatible, they order a and b oppositely. Consequently, when c,d are incompatible, every compatibility path from c to d contains a or b; equivalently c and d lie in different components of G-{a,b}.

## Body

# Proof

Fix the compatible pair F_a,F_b. By the compatible-pair localization, on H-{a,b} they have common ordered supports P|Q, both omitted labels restore to one support P, and their insertion slots in P are equal or adjacent.

Because ab has two distinct common compatibility neighbors c,d, the adjacent-slot case is impossible: compatedgecodeg02 shows that an adjacent-slot edge has at most one common neighbor. Thus a and b have one common insertion slot s in P. The same lemma shows that c and d must be exactly the two vertices of P flanking s. In particular s is internal. Orient the displayed order of P so that c immediately precedes d.

In F_a, the surviving label b is inserted at s, so locally the order is c,b,d. In F_b the local order is c,a,d.

Now use the compatibility triangle a,b,c. Its common-gap localization says that after deleting a,b,c, the three labels a,b,c restore into one common gap. Since d remains and the displayed orders above place a and b immediately before d after c is deleted, this common gap is the gap immediately before d. Thus in F_c the two surviving labels a,b occur together in that gap before d, in one of the two possible orders.

Similarly the compatibility triangle a,b,d shows that, after deleting a,b,d, the labels a,b,d share the common gap immediately after c. Hence in F_d the surviving labels a,b occur together in that gap after c.

Delete c and d as well. The restrictions of F_c and F_d to the remaining vertices have the same two supports and the same base order: compatibility of each with F_a fixes the position and order of b relative to every other common vertex, while compatibility of each with F_b fixes the position and order of a relative to every other common vertex. Therefore the only relative-order comparison on which F_c and F_d can differ is the comparison a versus b. It follows that F_c,F_d are compatible exactly when they order a,b the same way; if they are incompatible, they order a,b oppositely.

Finally suppose c=x_0,x_1,...,x_t=d is a compatibility path avoiding a and b. Every F_{x_i} contains both a and b. Compatibility of consecutive covers preserves both the common support containing a,b and their relative order. Hence the relative order of a,b is constant along the path, contradicting the opposite orders forced in F_c and F_d when those two covers are incompatible. Therefore every compatibility path from c to d meets {a,b}.
