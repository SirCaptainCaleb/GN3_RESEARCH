# Opposite long-span orientations expose an outward commuting square — preserved pre-item development

## Development

## Opposite long-span orientations expose an outward commuting square

Fix a protected face F at a reflected positive span-two depth r, with left and right determining windows I_L and I_R. Assume their starts satisfy b-a>=8, so the windows are separated as in [[separated_protected_determining_windows_force_a_persistent_witness_or_same_face_escape]].

Let L(pi),R(pi) in {0,1} record the left and right depth-r occurrences in a chamber pi of F.

Assume F contains an ordinary left-only chamber and an ordinary right-only chamber:
[
L=1,R=0
qquad	ext{and}qquad
L=0,R=1.
]

The block-separation proof of the persistent-orientation theorem gives an ordered-block boundary between I_L and I_R. Hence F factors, for the purpose of these two indicators, into independent prefix and suffix block-order choices:
[
L=L(	ext{prefix}),qquad R=R(	ext{suffix}).
]

Choose a chamber-graph path in the prefix factor from the prefix of the left-only chamber to the prefix of the right-only chamber. Along this path L changes from 1 to 0, so there is an adjacent prefix pair p_1,p_0 with
[
L(p_1)=1,qquad L(p_0)=0.
]
Similarly choose an adjacent suffix pair q_0,q_1 with
[
R(q_0)=0,qquad R(q_1)=1.
]

The two adjacent transpositions act in the separated window factors, so they commute. The four product chambers
[
p_1q_0,quad p_1q_1,quad p_0q_0,quad p_0q_1
]
therefore span a commuting Coxeter square in F. Their occurrence states are respectively
[
(1,0),quad(1,1),quad(0,0),quad(0,1).
]

Because F is protected, the chamber p_0q_0 has no closer witness. Since it has neither depth-r occurrence, it lies at strictly greater witness depth.

Thus every protected long-span face containing both ordinary orientations contains a rank-two square of the form
[
oxed{	ext{left-only};-;	ext{double};-;	ext{right-only}
quad	ext{with an outward fourth corner}.}
]

This sharpens the earlier same-face escape theorem in the case relevant to separator compatibility.

### Separator consequence

The double corner may be assigned either available orientation. If it is assigned the left sign, the only opposite-sign boundary edge of this square is the double-to-right-only edge; the outward corner is adjacent to the right-only endpoint across the commuting generator. If the double corner is assigned the right sign, the symmetric statement holds for the left-only edge.

Hence a conflict between left and right persistent choices in a long separated face is not an unbounded terminal-surgery event. It is a rank-two bypass already containing an outward chamber. The actual remaining compatibility issue is global: organize these square bypasses coherently across overlapping protected faces and antipodal components.

This result uses only block independence and chamber-graph connectivity; no two-cover theorem, minimum-counterexample argument, or direct computation is used.
