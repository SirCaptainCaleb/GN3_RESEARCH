# Every outermost root reduces to two six-coordinate collars joined by one good bridge — preserved pre-item development

## Every outermost root reduces to two six-coordinate collars joined by one good bridge

Continue from §251. Let a bad witness \(\pi\) have first and last change positions \(p<q\) and outermost root
\[
D(\pi)=e_{v_p}-e_{v_{q+3}}.
\]

When \(q-p\ge 7\), freeze the extreme four-coordinate collars
\[
L=(v_p,v_{p+1},v_{p+2},v_{p+3}),\qquad
R=(v_q,v_{q+1},v_{q+2},v_{q+3}),
\]
and replace the middle set
\[
S=\{v_{p+4},\ldots,v_{q-1}\}
\]
by a NOR-good order
\[
g(S)=(s_1,\ldots,s_m).
\]
As proved in §251, the first and last changes and therefore the exact outermost root remain unchanged.

### Two-collar normal form

Every ternary window of the resulting order belongs to one of three regions.

1. **Left endpoint packet.** Every window affected by the join \(L|g(S)\) uses only
\[
v_p,v_{p+1},v_{p+2},v_{p+3},s_1,s_2.
\]
Thus all left-side complexity beyond the fixed first change is contained in a packet of at most six physical coordinates.

2. **Good bridge.** Every window wholly inside \(g(S)\) belongs to a status word with at most one change.

3. **Right endpoint packet.** Every window affected by the join \(g(S)|R\) uses only
\[
s_{m-1},s_m,v_q,v_{q+1},v_{q+2},v_{q+3}.
\]
Hence all right-side complexity beyond the fixed last change is contained in another packet of at most six coordinates.

If the core has fewer than four coordinates, the two packets overlap and the entire active interval is already uniformly bounded.

### Theorem

Every outermost root in a minimum counterexample has a representative of the form
\[
\boxed{\text{six-coordinate collar}\;|\;\text{one-change proper bridge}\;|\;\text{six-coordinate collar}}
\]
with the same physical root, the same outside order, and the same extreme four-coordinate transition certificates.

Thus the phrase “at most nine changes” can be sharpened structurally: **all unbounded-length behavior is already NOR-good**. New realization difficulty can occur only at the two bounded joins attaching that good bridge to the frozen extreme collars.

### Relation to the current reconnection frontier

This normal form matches the existing local machinery:

- §238 shows ternary relative splicing needs only a three-coordinate collar to leave at most one exported bit;
- §226 resolves the rigid six-coordinate width-two residue to one exported bit or a double-full singleton;
- §246 resolves an isolated singleton by a curvature-free one-sided endpoint swap;
- threshold-band combing handles the exported flat side and terminates at a fully-curved protected barrier.

Accordingly, the remaining outermost-root realization theorem is a **two-collar attachment theorem**. There is no further long interior classification to perform.
