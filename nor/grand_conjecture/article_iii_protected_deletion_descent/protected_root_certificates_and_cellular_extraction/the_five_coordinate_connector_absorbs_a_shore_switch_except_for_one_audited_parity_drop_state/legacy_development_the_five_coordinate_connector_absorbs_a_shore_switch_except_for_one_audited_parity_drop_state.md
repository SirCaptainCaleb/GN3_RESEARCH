# The five-coordinate connector absorbs a shore switch except for one audited parity-drop state — preserved pre-item development

## Development

## Exact audited switch absorption by the minimum-shore connector block

Continue from §344. Let
[
C_0=(u,x,z,v,w)
]
be the monochromatic connector block with ternary word
[
000,
]
where (u,v,win A) form the directed shore triangle
[
u	o v	o w	o u
]
in the switching-normalized representative
[
B	o z	o A	o x.
]
Its reversal
[
C_1=(w,v,z,x,u)
]
has ternary word (111).

Let
[
P_B=(b_1,ldots,b_r)
]
be a NOR-good order of the opposite shore (B), normalized so that
[
c(P_B)=0^p1^q,qquad p,qge1.
]
Choose switching bits (sigma_i=sigma(b_i)) relative to the split-normalized tournament so that (P_B) is a directed Hamiltonian path in the switched representative. Put
[
e_i=sigma_ioplussigma_{i+1}.
]

Insert the connector block in the coordinate gap
[
b_{p+1}mid b_{p+2},
]
so the two old switch-straddling windows (c_p=0) and (c_{p+1}=1) disappear.

### Boundary-bit audit

Give every vertex of (C_0) (or (C_1)) one common switching bit (lambda). This leaves the internal tournament on the connector block unchanged.

Because every (B)-vertex dominates every connector vertex in the split-normalized tournament, and because the switched edge (b_i	o b_{i+1}) is directed, the left outer crossing satisfies
[
alpha(b_p,b_{p+1},c_1)
=
sigma_poplussigma_{p+1}
=
e_p.
]

Similarly the right outer crossing is
[
alpha(c_5,b_{p+2},b_{p+3})
=
sigma_{p+2}oplussigma_{p+3}
=
e_{p+2}.
]

For the zero block (C_0=(u,x,z,v,w)), its first and last ordered pairs are tournament-forward:
[
u	o x,qquad v	o w.
]
Hence the two immediate block-boundary windows are both (0). Together with the internal (000), the complete replacement packet is
[
oxed{e_p,;0,0,0,0,0,;e_{p+2}}.
]

For the reversed block (C_1=(w,v,z,x,u)), the first and last ordered pairs are tournament-backward:
[
w
ot	o v,qquad x
ot	o u.
]
Hence both immediate boundary windows are (1), and the replacement packet is
[
oxed{e_p,;1,1,1,1,1,;e_{p+2}}.
]

Thus the full two candidate words are exactly
[
W_0=
0^{p-1}, e_p, 0^5, e_{p+2}, 1^{q-1},
]
and
[
W_1=
0^{p-1}, e_p, 1^5, e_{p+2}, 1^{q-1}.
]

### Classification

If ((p,q)
e(1,1)), then:

- (W_0) is NOR-good whenever (e_p=0);
- (W_1) is NOR-good whenever (e_{p+2}=1).

Conversely, when at least one exterior phase remains, (e_p=1) makes (W_0) contain the forced pattern (0	o1	o0) on the left whenever a left zero remains, or forces a later return to the nonempty right one-phase when the left phase has length one. Symmetrically, (e_{p+2}=0) makes (W_1) contain the corresponding second change.

Therefore, for every nonminimal bichromatic shore word,
[
oxed{
	ext{both connector orientations fail}
iff
(e_p,e_{p+2})=(1,0).
}
]

### Minimal shore word

If
[
p=q=1,
]
there are no unchanged status windows on either side. Then
[
W_0=e_p,0^5,e_{p+2},qquad
W_1=e_p,1^5,e_{p+2}.
]
For every one of the four pairs ((e_p,e_{p+2})), at least one of these two words has at most one change. In particular the nominal parity-drop state ((1,0)) also closes.

Hence a shore whose internal word is exactly (01) is always absorbed by one orientation of the five-coordinate connector.

### Theorem

The minimum-shore five-coordinate connector absorbs the unique internal switch of any good opposite-shore order, except possibly in the single audited state
[
oxed{
c(P_B)=0^p1^q,quad (p,q)
e(1,1),quad
(e_p,e_{p+2})=(1,0).
}
]

This is the exact finite phase-alignment residue.

### Hartman interpretation

All higher endpoint data have disappeared. The remaining obstruction is one local parity drop across the shore switch.

Thus a reversible-reachability argument need only show that the state
[
(1,0)
]
cannot persist throughout the repair component of good (B)-orders. Any reachable order changing either bit is immediately absorbed by (C_0) or (C_1), while the shortest bichromatic word (01) closes even in the parity-drop state.

This supplies a concrete smallest-unreachable target for the Hartman program: the first repair that escapes the parity-drop class.
