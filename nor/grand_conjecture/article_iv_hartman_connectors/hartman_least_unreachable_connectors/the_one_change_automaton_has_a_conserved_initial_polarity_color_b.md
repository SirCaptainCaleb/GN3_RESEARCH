# The one-change automaton has a conserved initial-polarity color

## Composition

The quantity sigma=c xor t, where c is the current window color and t records whether the switch was used, is conserved by legal one-change append moves. It identifies the initial phase. A connector orientation used in a repair complex needs its own proved relation to this automaton invariant.

## Development

For a legal one-change partial order, let c be the last ternary-window color and let t∈{0,1} record whether the unique switch has already occurred. Define
σ=c⊕t.

Then σ is the initial phase color of the partial status word and is preserved by every legal append move. If the appended window keeps color c, neither c nor t changes. If it flips color, legality forces t=0 and the new state has d=1-c,t'=1, so d⊕t'=c.

Hence the legal NOR automaton splits canonically into two polarity sheets A_0 and A_1. A spanning NOR order is a bottom-to-top path inside one sheet.

This supplies the correct two-color datum for a Hartman argument. The remaining requirement is a reversible repair complex inside each polarity sheet.
