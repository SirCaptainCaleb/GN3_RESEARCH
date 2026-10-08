# Repair parity equals mobile switch winding parity — preserved pre-item development

## Development

## Repair parity equals mobile-switch winding parity

Work in the coboundary-flat pure-orientation sector. Consider a repair path along which one distinguished transition is transported without annihilation. Lift its transition position from the cyclic status circle of length m to the integers.

Each endpoint repair moves the distinguished switch by signed distance
[
d_jin{pm2,pm3}.
]
Let
[
lambda_j=
egin{cases}
0,& |d_j|=2,\
1,& |d_j|=3.
end{cases}
]

Modulo 2,
[
d_jequivlambda_j.
]
Hence along any repair path,
[
sum_j d_j
equiv
sum_jlambda_j
pmod2.
	ag{1}
]

Subsection 133 proves that the global distance-two chord parity J2 changes by exactly lambda_j on each repair:
[
Delta J_2=lambda_j.
]
Therefore if the repair path returns to the same full repair state,
[
sum_jlambda_jequiv0pmod2.
	ag{2}
]

Suppose the distinguished switch returns to the same cyclic slot after winding w times around the transition circle. On the integer lift,
[
sum_j d_j=wm.
]
Combining with (1)-(2) gives
[
oxed{wmequiv0pmod2.}
]

### Consequence

If the status-circle length m is odd, every closed repair loop transporting one mobile switch has even winding number. In particular, an odd-winding equality loop is impossible.

This gives a direct interface with the switch-prism / Tucker connector program. A topological carrier that forces a repair path from a state to an antipodal or reversal-related state with odd winding cannot be trapped inside a closed minimum-variation repair component; somewhere along the path one must leave the pure transport graph, which means switch annihilation, variation decrease, or a nonrepair transition.

For even m the parity obstruction vanishes, so a stronger integer or mod-4 winding invariant would be required.
