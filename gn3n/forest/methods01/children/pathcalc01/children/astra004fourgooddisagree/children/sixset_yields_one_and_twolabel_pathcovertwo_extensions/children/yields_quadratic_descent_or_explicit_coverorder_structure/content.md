# From order fifteen a non-Hamiltonian six-set yields quadratic descent or explicit cover/order structure

## Statement

Let H be a minimum counterexample of order n>=15 and let K be a non-Hamiltonian six-set. Choose distinct Hamiltonian deletions d,e of K such that D=K-{d,e} is Hamiltonian. Put L=H-K, let F=P|Q be any two-cover of H[L union {d,e}], and consider the spanning three-cover C=D|P|Q. Then at least one of the following holds:

(1) the connected component of C in the pairwise-repartition graph contains a three-cover with strictly smaller quadratic potential;

(2) for some x in {d,e}, deleting x from the displayed F-component containing it gives a three-cover of H[L union ({d,e}-{x})], and a two-cover of that induced subtournament contains an ordinary path edge joining two distinct paths of this three-cover;

(3) explicit order disagreement occurs.

When n=15, two additional conclusions are allowed: a deletion cover has at least two ordinary path edges joining different classes of a displayed 5|5|5 three-cover, or two displayed endpoints are noninsertable into the same displayed opposite path as in 5ec926f6e4fc.

## Body

By d2205c472e75, H[L union {d}], H[L union {e}], and H[L union {d,e}] are all non-Hamiltonian with path-cover number two. If C is not Phi-minimal in its connected pairwise-repartition component, the first conclusion already holds. Hence assume C is Phi-minimal in that component.

Fix x in {d,e}, and let y be the other label. Consider the displayed F-component containing x. If x is internal, deleting x splits that component into two nonempty contiguous tight subpaths; together with the unchanged other F-component they form a displayed three-path cover of H[L union {y}]. Since H[L union {y}] has path-cover number two, the component-drop comparison in coversurg01 implies that every two-cover of H[L union {y}] contains an ordinary edge joining two distinct components of this displayed three-cover. Thus such an ordinary edge exists. Hence, if no such edge exists for either deletion, both d and e are displayed endpoints of their F-components. Neither can be a singleton component, since deleting it would leave a Hamilton path on the corresponding one-label state H[L union {y}], contradicting its non-Hamiltonicity.

Because D union {d}=K-e and D union {e}=K-d are Hamiltonian, moving either endpoint label from its F-component into D is a legal pairwise repartition from C. If the component containing d has order p, this move changes the affected orders from 4,p to 5,p-1, so Delta Phi=25+(p-1)^2-[16+p^2]=10-2p. Phi-minimality gives p<=5. The component containing e likewise has order at most five.

If d and e lie in different F-components, both component orders are at most five, while their sum is |L|+2=n-4>=11, impossible. Thus d and e lie in the same component P of order p<=5. Let q be the order of the other component Q. Then p+q=n-4, so q>=6.

If q>=7, a25b748fb338 applied to D|Q|P gives either a legal strict Phi decrease or explicit order disagreement. The former contradicts Phi-minimality of C, so order disagreement follows. This handles every n>=16, and n=15 whenever p<=4.

It remains only n=15 with p=5 and q=6, so Phi(C)=4^2+5^2+6^2=77. Let Phi_* be the global minimum over all spanning three-covers of H. The minimum possible value for three positive integer orders summing to 15 is 75, attained only by 5|5|5, and the next possible value is 77, attained by 4|5|6. Since Phi_*<=77, either Phi_*=75 or Phi_*=77. If Phi_*=77, a globally Phi-minimal cover has a four-side, and global_four_side_order15 gives explicit order disagreement. If Phi_*=75, 5ec926f6e4fc applied to a global 5|5|5 cover gives either at least two ordinary three-part crossings, two displayed endpoints noninsertable into the same displayed opposite path, with the alternatives of a8c9883902b1, or explicit order disagreement. Thus the order-fifteen boundary also enters the configurations listed in the statement. No assumption on Hamiltonicity of the outside core L is used.