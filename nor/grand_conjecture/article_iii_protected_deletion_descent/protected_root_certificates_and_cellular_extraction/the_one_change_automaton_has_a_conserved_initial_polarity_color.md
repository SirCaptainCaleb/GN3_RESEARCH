# The one-change automaton has a conserved initial-polarity color

## Composition

(none yet)

## Development

## The one-change automaton has a conserved initial-polarity color

Use the exact continuation state from the ordered-tail formulation. After at least one ternary window has been read, a legal partial order carries state
[
(S;a,b,c,t),
]
where (cin{0,1}) is the last window color and (tin{0,1}) is the number of color changes already used.

Define
[
sigma:=coplus t.
]

Then (sigma) is exactly the initial color of the partial status word.

Indeed, if (t=0), no change has occurred and the entire word has color (c), so (sigma=c). If (t=1), the word has changed exactly once and its initial color is (1-c), so again (sigma=coplus1).

Now append a new coordinate (x), producing new window color
[
d=alpha(a,b,x).
]

A legal append has two possibilities.

1. If (d=c), then (t) is unchanged and
[
sigma'=doplus t=coplus t=sigma.
]

2. If (d
e c), legality requires (t=0), and the new switch count is (t'=1). Since (d=1-c),
[
sigma'=doplus1=(1-c)oplus1=c=sigma.
]

Therefore every legal extension preserves (sigma).

### Consequence

The exact one-change continuation graph splits canonically into two polarity sheets
[
mathcal A_0,qquad mathcal A_1,
]
and every spanning NOR-good order is a bottom-to-top path entirely inside one sheet.

This gives the correct two-color object for a Hartman-style connector argument. The directed prefix graph itself is not yet suitable for least-unreachable labels, because directed target reachability is only monotone under extension, not constant along adjacent states. A Hartman implementation therefore needs a reversible cell/repair graph inside one polarity sheet (or a reversible enlargement preserving (sigma)) so that boundary-target reachability becomes a genuine component invariant.
