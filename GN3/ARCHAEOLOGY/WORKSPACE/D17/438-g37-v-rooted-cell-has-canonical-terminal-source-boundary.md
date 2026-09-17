# The v-rooted hard cell has a canonical terminal X-mated source boundary

**Workspace:** D17
**State:** audited PASS_ADJUSTED
**Result:** `R1040`
**Key:** `g37-v-rooted-terminal-source-boundary`

## Certified statement

In the v-rooted hard cell, let `e_k` be the last old `F`-transition on the unique augmenter `C_*`. Then `k` lies strictly after the v-transition, `e_k` is one of the two X-mated source gates, and exchanging the terminal alternating suffix beginning at `e_k` into `J` yields a matching of the same cardinality as `J` with transition count at most two. If `t` is the source endpoint of `e_k`, the tight source trimer `(A,t,C)` remains graph-intrinsic, and R1037 supplies the adjacent old X-X mate and ordered three-spoke source ancestry.

No claim is made here that this matching-level boundary automatically launches the historical D17.425 wall consumer or is already a physical tight three-forest.

## Proof

R1037 shows that the old `F` transitions are exactly the unique v-B transition and the two X-mated source gates. R1038 shows that at least one source gate occurs strictly after the v-transition on `C_*`. Therefore the last old `F`-transition `e_k` occurs after v and is source-bearing; since both source gates are X-mated, `e_k` is X-mated.

For the terminal alternating exchange

`J' = J - {f_{k-1},...,f_{m-1}} + {e_k,...,e_m}`,

matching cardinality is preserved. With `chi` the X|B transition indicator,

`tau(J') = tau(J) - sum_{i=k-1}^{m-1} chi(f_i) + sum_{i=k}^{m} chi(e_i)`.

Because `k` is the last old `F`-transition,

`sum_{i=k}^{m} chi(e_i)=1`.

Since `tau(J)=1` and the removed-J sum is nonnegative,

`tau(J') <= 2`.

The source endpoint `t` of `e_k` retains the graph-intrinsic tight trimer `(A,t,C)`, while R1037 supplies the selected adjacent X-X mate.

## Audit adjustment

The pre-audit version invoked an unrecovered two-ended theorem behind D17.420 and concluded that D17.425 could launch from this boundary. The terminal-boundary estimate itself is direct and needs neither citation. The stronger consumer implication is not part of the audited theorem unless its additional physical-realization hypotheses are separately established.

Canonical result: `A7C3/RESULTS/USABLE/ACTIVE/R1040.md`.