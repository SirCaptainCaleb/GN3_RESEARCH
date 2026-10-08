# Exact audited shore-switch absorption and the parity-drop frontier — preserved pre-item development

## Composition

(none yet)

## Development

Let P_B=(b_1,…,b_r) be a good opposite-shore order with normalized word
0^p1^q, p,q≥1.
Choose switching bits σ_i making P_B a directed Hamiltonian path in a switching-equivalent shore tournament and put
e_i=σ_i⊕σ_{i+1}.

Insert the five-block at the unique shore switch. The zero orientation produces the exact full status word
W_0=0^{p-1}, e_p, 0^5, e_{p+2}, 1^{q-1},
while the reversed one orientation gives
W_1=0^{p-1}, e_p, 1^5, e_{p+2}, 1^{q-1}.

For (p,q)≠(1,1), both orientations fail exactly in the single parity state
(e_p,e_{p+2})=(1,0).
If p=q=1, one orientation always closes, including this nominal parity-drop state.

Therefore the entire phase-alignment problem has collapsed to persistence of one local parity drop across a nonminimal shore switch.

This is the current Hartman frontier: build the reversible repair component of good B-orders and prove that the state (1,0) cannot remain trapped throughout that component. Any reachable order changing either bit is immediately absorbed by one orientation of the monochromatic five-block.
