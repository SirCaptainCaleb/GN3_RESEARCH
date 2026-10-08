# Interior insertion forbids 010 in the zero phase and 101 in the one phase

## Metadata

- ID: interior_insertion_forbids_010_in_the_zero_phase_and_101_in_the_one_phase
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 290
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Interior insertion forbids 010 in the zero phase and 101 in the one phase

Let
\[
O=(v_1,\ldots,v_m)
\]
be a good deletion order omitting \(x\), with normalized word
\[
0^p1^q.
\]
Define the insertion scan
\[
s_i=\alpha(x,v_i,v_{i+1}),
\qquad 1\le i\le m-1.
\]

Insert \(x\) between \(v_i\) and \(v_{i+1}\). The only new ternary windows are
\[
(v_{i-1},v_i,x),\qquad
(v_i,x,v_{i+1}),\qquad
(x,v_{i+1},v_{i+2}),
\]
with endpoint clipping.

By cyclic invariance and alternation their colors are
\[
\boxed{s_{i-1},\ 1-s_i,\ s_{i+1}.}
\]

Every other window is an unchanged window of \(O\).

### Zero-phase exclusion

Suppose the insertion lies strictly inside the 0-phase, so the two old windows replaced by the insertion and the surrounding target windows all have desired color \(0\).

If
\[
(s_{i-1},s_i,s_{i+1})=(0,1,0),
\]
then the three new colors are
\[
0,0,0.
\]
Hence the entire full order still has word \(0^*1^*\), giving a spanning NOR-good order.

Therefore a minimum counterexample satisfies:
\[
\boxed{\text{no scan pattern }010\text{ can be centered at an interior zero-phase insertion position}.}
\]

### One-phase exclusion

Dually, for an insertion strictly inside the 1-phase, the desired three new colors are all \(1\).

If
\[
(s_{i-1},s_i,s_{i+1})=(1,0,1),
\]
then the new colors are
\[
1,1,1,
\]
so the full order is again one-change.

Hence:
\[
\boxed{\text{no scan pattern }101\text{ can be centered at an interior one-phase insertion position}.}
\]

### Block consequence

Inside the zero phase, every internal 1-run of the insertion scan has length at least two. Inside the one phase, every internal 0-run has length at least two.

Combined with the endpoint forcing
\[
s_1=1,\qquad s_{m-1}=0
\]
from §287, the arbitrary insertion scan is therefore constrained to move from an initial 1-state to a terminal 0-state without isolated 1s on the zero side or isolated 0s on the one side.

This is a purely full-order obstruction: no flatness or curvature assumption is used.

## Frontier

- Development version when composed: None
- Development version now: 1
