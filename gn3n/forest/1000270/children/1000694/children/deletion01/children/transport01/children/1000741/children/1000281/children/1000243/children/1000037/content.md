# Two bad endpoints over a six-side share three four-cores and force six-support migration or order disagreement

## Statement


Let H be a boundary tournament and let C=X|P|Q be a spanning three-cover minimizing Phi within its connected pairwise-repartition component, where X is a Hamiltonian path of order six. Let e,f be distinct displayed endpoints of components of C other than X, and assume the component containing each of e,f has order at least eight. The two endpoints may belong to the same component.

Then there are at least three unordered pairs {a,b} subset V(X) such that, with D=V(X)-{a,b}, both five-sets D union {e} and D union {f} are Hamiltonian. For each such pair, putting S=D union {e,f}, either S is Hamiltonian or H[S] contains explicit relative-order disagreement among Hamiltonian vertex-deletion paths. Consequently, if no order disagreement occurs, at least three distinct two-for-two replacements of X by {e,f} produce Hamiltonian six-sets.


## Body


Fix one endpoint e, lying on a displayed path R of order m>=8. If X union {e} were Hamiltonian, replacing X|R by (X union {e}) | (R-e) would change the pair of component orders
6,m -> 7,m-1.
The potential change is
7^2+(m-1)^2-[6^2+m^2]=14-2m<0,
contradicting local Phi-minimality. Hence the seven-set W_e=V(X) union {e} is non-Hamiltonian. The same holds for f.

Apply the rooted seven-set shell theorem 84ac56baf953 to W_e with root e and six-vertex shell V(X). Define G_e on V(X) by joining a,b exactly when
{e} union (V(X)-{a,b})
is Hamiltonian. Then delta(G_e)>=3, so e(G_e)>=9. Define G_f analogously; again e(G_f)>=9.

There are only binom(6,2)=15 pairs in V(X), hence
|E(G_e) intersect E(G_f)| >= 9+9-15 = 3.
Thus at least three pairs {a,b} have the asserted common-core property.

Fix one such pair and write D=V(X)-{a,b}. Then D union {e} and D union {f} are Hamiltonian five-sets. Put S=D union {e,f}, a six-set. If S is Hamiltonian, we have the first outcome. Suppose S is non-Hamiltonian. By the four-of-six theorem in smallset01, S has at least four Hamiltonian vertex deletions. Apply astra004fourgooddisagree to any four of them. The chosen Hamilton deletion paths cannot all induce the same order on common vertices, so a pair has relative-order disagreement; pathcalc01 then yields the standard reversed-edge, reversing-triple, or tight-cycle witness.

This argument applies independently to every common shell edge. Therefore absent order disagreement all common shell edges give Hamiltonian six-set replacements, and there are at least three of them.
