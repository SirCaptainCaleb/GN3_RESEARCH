# Forbidden target-size covers force noninsertability

## Statement

Let H be a boundary tournament, let x be a vertex, and let P|Q be a two-cover of H-x with displayed path orders. If H has no two-cover with component-order multiset {|P|+1,|Q|}, then x is noninsertable into the displayed path P. Symmetrically, if H has no two-cover with component-order multiset {|P|,|Q|+1}, then x is noninsertable into Q.

## Body

If x could be inserted into the displayed tight path P, the resulting path P+x together with the unchanged path Q would be a two-cover of H with component orders |P|+1 and |Q|, contradicting the stated forbidden size multiset. The argument for Q is identical.

This is the exact local mechanism behind the parity-specific noninsertability lemma astra002paritybarrier01. No minimal-counterexample assumption is required. For a boundary tournament of odd order 2k+1 with no balanced two-cover, any k|k deletion cover makes x noninsertable into both components. For even order 2k, any k|(k-1) deletion cover makes x noninsertable into the smaller component.
