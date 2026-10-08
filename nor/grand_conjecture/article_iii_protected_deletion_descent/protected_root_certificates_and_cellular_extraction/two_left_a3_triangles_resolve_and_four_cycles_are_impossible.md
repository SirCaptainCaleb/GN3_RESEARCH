# Two-left A3 triangles resolve and four-cycles are impossible

## Composition

(none yet)

## Development

Consider canonical protected roots in one ternary A3 block whose protected cut meets the block in two coordinates. Flatness forces the four face bits into one of the two alternating patterns 1010 or 0101. For a directed triangle a to b to c to a, the 0101 pattern forces all three edges to use the same omitted fourth coordinate d. Their good deletion witnesses then force alpha(c,a,e)=alpha(a,b,e)=alpha(b,c,e)=0 for the first exterior coordinate e; the flat identity on {a,b,c,e} is violated, so this pattern is impossible. In the 1010 pattern the three witnesses instead force the five-coordinate order (d,a,b,c,e) to have word 010, and both bounding transition tetrahedra are fully curved. The two one-sided monotone resolutions therefore reduce the triangle to a global one-change state or a protected-root handoff by threshold-band combing. For a directed four-cycle a to b to c to d to a, the 1010 pattern gives two opposite cycle witnesses whose right attachments force both alpha(d,b,e)=0 and alpha(b,d,e)=0, impossible by alternation. The 0101 pattern similarly forces both alpha(c,a,e)=0 and alpha(a,c,e)=0. Thus no two-left directed four-cycle exists. Combining this with the two-left two-cycle splice/ejection theorem, no protected A3 circuit is a closed four-coordinate obstruction: every A3 circuit either closes, improves the deletion profile, or emits a protected root leaving the A3 block.
