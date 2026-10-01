# Strict pair-union balance improvement is equivalent to balanced refinement on every two-coverable tournament

## Statement

The following are equivalent for finite boundary tournaments. (i) Whenever A|B is a spanning two-cover with ||A|-|B||>=2, the same tournament has a spanning two-cover R|S with strictly smaller component-order imbalance. (ii) Every boundary tournament that admits at least one spanning two-cover admits a balanced spanning two-cover, with component orders floor(n/2),ceil(n/2). Consequently ff2977cf5c23, viewed as a theorem about an arbitrary pair-union in isolation, is exactly the balanced-refinement problem on the class of already two-coverable boundary tournaments.

## Body

Assume (i), and let K be any boundary tournament admitting a spanning two-cover. Start from any such cover A_0|B_0 and let d_0=||A_0|-|B_0||. If d_0<=1, the cover is balanced. Otherwise (i) gives a second spanning two-cover with strictly smaller nonnegative integer imbalance. Repeating whenever the current imbalance is at least two gives a strictly decreasing sequence of nonnegative integers, so the process terminates. The parity of the imbalance of any two-cover equals |V(K)| modulo two, since if the component orders are r,s then |r-s| is congruent to r+s=|V(K)| mod 2. Therefore the smallest possible terminal imbalance is 0 when |V(K)| is even and 1 when it is odd. The terminal cover is balanced.

Conversely assume (ii), and let A,B be vertex-disjoint tight paths with |A|>=|B|+2. Put K=H[V(A) union V(B)]. The displayed paths A|B form a spanning two-cover of K. By (ii), K has a balanced spanning two-cover R|S. Its imbalance is 0 or 1, which is strictly smaller than |A|-|B|>=2. Thus (i) holds.

Hence the local strict-improvement statement is equivalent to balanced refinement for every already two-coverable boundary tournament. In particular, a proof of ff2977cf5c23 that uses only the induced pair-union and its displayed two-cover, with no information from an ambient third component or ambient minimum counterexample, would establish this full balanced-refinement theorem. For the grand two-cover project, this is a strategic fence: to obtain a weaker theorem tailored to a trapped three-cover, one should exploit the third component or other ambient minimum-counterexample constraints rather than expect a purely pair-internal argument.
