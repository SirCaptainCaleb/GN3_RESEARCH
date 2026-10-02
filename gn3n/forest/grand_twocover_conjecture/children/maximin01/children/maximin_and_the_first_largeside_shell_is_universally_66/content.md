# Minimum deletion side controls maximin, and the first large-side shell is universally 6|6

## Statement


Let H be a minimum counterexample. Let mu be the minimum smaller-component order among exact two-covers of one-vertex deletions, and rho the maximum minimum-component order among spanning exact three-path covers. Then rho>=min{4,mu-2}. Hence mu>=6 implies rho>=4. Moreover mu>=6 forces |V(H)|>=13; if |V(H)|=13, then mu=6, every exact two-cover of every vertex deletion has orders 6,6, the maximum tight-path order is exactly six, every seven-vertex induced subtournament is non-Hamiltonian, and rho=4.


## Body


# Minimum deletion side controls maximin, and the first large-side shell is universally 6|6

Let H be a minimum counterexample. Define
mu=min_x min_{P|Q exact cover of H-x} min{|P|,|Q|}
and let rho be the maximum, over spanning exact three-path covers, of the minimum component order.

## From a minimum deletion side to a balanced three-cover

Choose
H-x=P|Q
with |P|,|Q|>=mu, and write
P=(p_0,...,p_m), Q=(q_0,...,q_s).
Both components have order at least three.

Consider the canonical spanning order P,x,Q. Its two outer join centers are defective. If the middle triple (p_m,x,q_0) is also non-tight, defect-span reversal gives the tight five-path
F=(q_1,q_0,x,p_m,p_{m-1}).
The inherited paths
P^-=(p_0,...,p_{m-2}), Q^+=(q_2,...,q_s)
are nonempty, so
P^- | F | Q^+
is a spanning three-cover with orders
|P|-2, 5, |Q|-2.
Thus
rho>=min{5,mu-2}>=min{4,mu-2}.

Suppose instead (p_m,x,q_0) is tight and put
Z={p_{m-1},p_m,x,q_0,q_1}.
If H[Z] is Hamiltonian, a Hamilton path on Z with P^- and Q^+ gives the same bound.

If H[Z] is non-Hamiltonian, a non-Hamiltonian five-vertex boundary tournament has at most one non-Hamiltonian four-vertex induced subtournament. Therefore at least one of
Z-{p_{m-1}}={p_m,x,q_0,q_1}
and
Z-{q_1}={p_{m-1},p_m,x,q_0}
is Hamiltonian.

In the first case,
(p_0,...,p_{m-1}) | F | (q_2,...,q_s)
has component orders |P|-1,4,|Q|-2. In the second,
(p_0,...,p_{m-2}) | F | (q_1,...,q_s)
has orders |P|-2,4,|Q|-1. Hence in all cases
rho>=min{4,mu-2}.                                             (1)

In particular mu>=6 implies rho>=4, while rho=3 forces mu<=5.

## The first large-minimum-side shell

Assume mu>=6. Every exact two-cover of every H-x has both component orders at least mu, so
|V(H)|-1>=2mu>=12.
Hence
|V(H)|>=13.

Now suppose |V(H)|=13. Every deletion cover has total order twelve and each side has order at least six. Therefore every exact deletion cover has order multiset
{6,6},
and mu=6.

Such a cover contains a tight path of order six, so the global maximum tight-path order L(H)>=6.

On the other hand, when mu>=6 the large-minimum-side complement theorem excludes a tight path whose non-Hamiltonian complement has order 4,5,or6. In a minimum counterexample the complement of every proper tight path is non-Hamiltonian, since a Hamiltonian complement would combine with the path to two-cover H. Thus H has no tight path of order 7,8,or9. A path of order at least ten is also impossible because every tight path in a minimum counterexample leaves at least four vertices. Therefore
L(H)=6.

Consequently no seven-vertex induced subtournament is Hamiltonian.

Finally (1) gives rho>=4. A thirteen-vertex tournament cannot have a spanning three-cover all of whose components have order at least five, since that would require at least fifteen vertices. Hence rho<=4 and
rho=4.

Thus the first possible shell with minimum deletion side at least six is completely rigid: order thirteen, universal 6|6 deletion covers, global longest-path order six, no Hamiltonian seven-set, and maximin exactly four.
