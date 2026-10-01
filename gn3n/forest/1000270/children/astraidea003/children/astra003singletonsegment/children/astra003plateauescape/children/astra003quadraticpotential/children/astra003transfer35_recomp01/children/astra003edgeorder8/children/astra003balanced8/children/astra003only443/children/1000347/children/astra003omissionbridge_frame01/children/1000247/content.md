# The order-eleven Astra component has at least seven omission labels

## Statement

Let K be a trapped Astra-003 component on eleven vertices containing a 4|4|3 state. Let S be the set of labels that occur as the singleton in some reachable 5|5|1 state. Then |S|>=7. If |S|=7 and T=V(H)-S, then in every reachable 5|5|1 state P|Q|(x), x in S, each of P,Q contains exactly three vertices of S and two vertices of T; in each non-Hamiltonian six-set P union {x} and Q union {x}, the four Hamiltonian five-deletions are exactly x and the three S-labels on that side, while the two T-labels are the two bad deletions.

## Body

# Seven omission labels and the equality shell

By the universal 4|4|3-to-5|5|1 bridge, K contains at least one equitable omission state

P|Q|(x),

with |P|=|Q|=5.

Let S be the set of vertex labels that occur as the singleton of some 5|5|1 state in K.

The certified order-eleven omission-graph theorem says that from every state P|Q|(x) there are at least three distinct reversible omission swaps through P and at least three through Q. Thus there are distinct labels

p_1,p_2,p_3 in P,  q_1,q_2,q_3 in Q

such that K also contains omission states with singleton labels p_i and q_j. These six labels are distinct from one another and from x. Therefore |S|>=7.

Now suppose |S|=7 and put T=V(H)-S, so |T|=4. Fix any reachable omission state P|Q|(x). The omission theorem supplies at least three singleton-swap labels from P and at least three from Q, all belonging to S-{x}. Since S-{x} has exactly six elements and P,Q are disjoint, each side contains exactly three vertices of S and hence exactly two vertices of T.

Consider the non-Hamiltonian six-set

R_P=V(P) union {x}.

Deleting x leaves the Hamiltonian five-set P. The four-of-six theorem gives at least four Hamiltonian five-deletions of R_P. Every t in P intersection T must be a bad deletion: if R_P-{t} were Hamiltonian, then replacing P|(x) by (R_P-{t})|(t) would be a legal omission swap producing singleton label t, contradicting t notin S.

There are exactly two such T-labels. Hence the remaining three vertices of P, all in S, must all be good deletions, and the good-deletion set is exactly

{x} union (P intersection S).

Thus R_P has exactly four good five-deletions and exactly two bad ones, namely P intersection T. The same argument applies to R_Q=V(Q) union {x}.

Therefore the minimal seven-label omission shell is rigid: every 5|5|1 state splits the four excluded labels 2+2 across its two five-sides, and on each side those two excluded labels are precisely the bad deletions of the corresponding six-set.
