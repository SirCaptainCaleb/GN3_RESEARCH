# Every order-eleven triple has at least seven balanced complements, all blocked on both sides

## Statement

Let H be a hypothetical order-eleven minimum counterexample. For every three-set X subseteq V(H), the eight-vertex complement H-X has at least seven distinct Hamiltonian 4|4 partitions P|Q. Every corresponding spanning three-cover X|P|Q lies in the unique connected pairwise-repartition component containing all spanning three-covers, and for every one of these partitions both seven-sets X union P and X union Q are non-Hamiltonian.

## Body

Fix X. By balanced8_multiplicity7_01, H-X has at least seven Hamiltonian 4|4 partitions P|Q. Since every three-set is Hamiltonian, each gives a spanning three-cover X|P|Q. The certified order-eleven connectivity theorem astra003order11connected places every spanning three-cover in the same pairwise-repartition component.

For any one of the balanced complements P|Q, if X union P were Hamiltonian then a Hamilton path on X union P together with a Hamilton path on Q would give a spanning two-cover of H, contradiction. Thus X union P is non-Hamiltonian, and symmetrically X union Q is non-Hamiltonian. This holds for all at least seven partitions. Hence every prescribed triple carries at least seven distinct two-sided no-merge barriers.