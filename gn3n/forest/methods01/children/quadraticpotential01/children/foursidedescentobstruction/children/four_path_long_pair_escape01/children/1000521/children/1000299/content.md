# From order seventeen onward a global quadratic minimum has no four-vertex component unless order disagreement already occurs

## Statement

Let H be a minimum counterexample of order n>=17 and let C=X|P|Q be a spanning three-cover minimizing Phi among all spanning three-covers. If H contains no explicit relative-order disagreement of the type produced by a25b748fb338, then every component of C has order at least five. Equivalently, a globally Phi-minimal three-cover with a four-vertex component forces such order disagreement when n>=17.

## Body

By the certified global minimum-side theorem, every component of C has order at least four. Suppose |X|=4 and write |P|=p>=q=|Q|>=4. Since p+q=n-4>=13, we have p>=7. Apply a25b748fb338 to X|P|Q. Because C is globally Phi-minimal, its strict-descent alternative is impossible. Therefore the explicit order-disagreement alternative must occur. This already proves the statement directly. For the boundary mechanism behind the threshold, note that if p=6 then the Hamiltonian-six branch in the proof of a25b748fb338 merely swaps the size pair 4|6 to 6|4 with equal Phi, moving the four-side to the inherited middle four-path. If the untouched third component had order at least seven, applying a25b748fb338 again to that new four-side and the third component would force strict descent or order disagreement. Hence an order-neutral Phi-minimal four-side plateau can only have both other component orders at most six, so its total order is at most 16.