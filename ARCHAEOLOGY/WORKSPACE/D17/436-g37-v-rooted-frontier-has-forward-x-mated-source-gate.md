# D17.436 — Every v-rooted sharp first-loss augmenter has a forward X-mated source gate

**Workspace:** D17
**State:** audited PASS
**Canonical result:** `A7C3/RESULTS/USABLE/ACTIVE/R1038.md`
**Key:** `g37-v-rooted-frontier-forward-x-mated-source-gate`

## Statement
In the v-rooted sharp first-loss cell, let `C_*` be the unique augmenter, let `r` be the first index with positive prefix ledger, and retain

`tau(F)=3`, `tau(J)=1`, `w(C_*)=2`.

Then the X|B transition counts on `C_*` are either `(2F,0J)` or `(3F,1J)`. In either case at least one of the two X-mated source gates from D17.435/R1037 occurs strictly after the v-transition along `C_*`. Any source gate occurring before v must be neutralized by the unique J-transition before the first-positive v-pivot.

## Proof
Let `n_F,n_J` count F-selected and J-selected X|B transitions on `C_*`. Since `w(C_*)=2`,

`n_F-n_J=2`.

The global totals give `n_F<=3`, `n_J<=1`, so only `(2,0)` and `(3,1)` are possible.

By R1037 the three F-transitions are exactly the unique v-B transition and the two X-mated endpoint gates of the internal three-spoke source block.

If `(n_F,n_J)=(2,0)`, no J-transition occurs on `C_*`. Because the v-transition is the first positive prefix pivot, no F-transition can precede it. Hence the other F-transition on `C_*` is a source gate strictly after v.

If `(n_F,n_J)=(3,1)`, all three F-transitions and the unique J-transition lie on `C_*`. Were both source gates before v, their total `+2` contribution could be offset by at most the unique J contribution `-1`, forcing a positive proper prefix before r. This contradicts first-positive minimality. Hence at least one source gate lies strictly after v.

Likewise, any source gate before v must be J-neutralized; otherwise its `+1` contribution would itself create a positive prefix before r.

No physical-success or global-closure conclusion is asserted.
