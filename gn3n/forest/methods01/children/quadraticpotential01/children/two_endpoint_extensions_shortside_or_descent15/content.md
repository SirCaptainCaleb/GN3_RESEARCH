# Two Hamiltonian endpoint extensions force descent or a common short side

## Statement

Let H be a boundary tournament of order n>=15 and let D|P|Q be a spanning three-cover with |D|=4 and D Hamiltonian. Let d,e be distinct vertices outside D such that D union {d} and D union {e} are Hamiltonian. Suppose d and e are displayed endpoints of the two-cover P|Q of H-D. Then either one legal pairwise repartition strictly decreases quadratic potential, or d and e are the two displayed endpoints of the same one of P,Q and that path has order at most five. In the latter case the other displayed path has order at least six. If n>=18, the other path has order at least nine.

## Body

Write p=|P| and q=|Q|, so p+q=n-4>=11. Suppose first that d and e lie on different displayed paths; say d is an endpoint of P and e an endpoint of Q. Because D union {d} is Hamiltonian and P-d is the inherited endpoint truncation, replacing D|P by (D union {d})|(P-d) is a legal pairwise repartition. Its quadratic-potential change is 5^2+(p-1)^2-[4^2+p^2]=10-2p, which is strictly negative whenever p>=6. The analogous e-transfer has change 10-2q. Since p+q>=11, at least one of p,q is at least six, so one of these two legal transfers strictly decreases quadratic potential.

Now suppose d and e lie on the same displayed path, say P. Since they are distinct displayed endpoints, they are the two opposite endpoints of P. If p>=6, transfer d into D exactly as above to obtain a strict decrease. Therefore absence of strict descent forces p<=5. Then q=n-4-p>=n-9, so q>=6 for n>=15 and q>=9 for n>=18. This proves the claim.
