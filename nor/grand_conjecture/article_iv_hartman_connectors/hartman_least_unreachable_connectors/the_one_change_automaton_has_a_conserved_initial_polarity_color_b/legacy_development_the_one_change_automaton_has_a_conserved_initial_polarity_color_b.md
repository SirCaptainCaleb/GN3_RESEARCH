# The one-change automaton has a conserved initial-polarity color — preserved pre-item development

## Composition

(none yet)

## Development

For a legal one-change partial order, let c be the last ternary-window color and let t∈{0,1} record whether the unique switch has already occurred. Define
σ=c⊕t.

Then σ is the initial phase color of the partial status word and is preserved by every legal append move. If the appended window keeps color c, neither c nor t changes. If it flips color, legality forces t=0 and the new state has d=1-c,t'=1, so d⊕t'=c.

Hence the legal NOR automaton splits canonically into two polarity sheets A_0 and A_1. A spanning NOR order is a bottom-to-top path inside one sheet.

This supplies the correct two-color datum for a Hartman argument. The remaining requirement is a reversible repair complex inside each polarity sheet.
