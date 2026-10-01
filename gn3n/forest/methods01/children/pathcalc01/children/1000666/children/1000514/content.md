# Three-block plateaux have free cut slides or a forced reversed tight four-path

## Statement

Let an ordering pi be partitioned as three nonempty contiguous tight paths A|B|C. Any permutation of the three whole blocks is reachable by contiguous block relocations while keeping c<=3. Moreover, for any adjacent tight blocks X=(x_1,...,x_p) and Y=(y_1,...,y_q) with p,q>=2, exactly one of the following local alternatives holds at their interface: (i) both join triples are tight, so XY is one tight path and the three-block state immediately reduces to at most two paths; (ii) exactly one join triple is tight, and the cut can be slid by one vertex across the interface while retaining two tight blocks; (iii) both join triples are non-tight, and (y_2,y_1,x_p,x_{p-1}) is a tight four-vertex path. This local trichotomy does not imply that repeated cut slides terminate; slides can reverse one another, so an additional global invariant is required for a no-trapping argument.

## Body

First, relocating one whole block past another never changes its internal order. Since A,B,C are individually tight, after any permutation they still form three contiguous tight subpaths. Hence every whole-block permutation stays in the sublevel set c<=3.

Now fix adjacent tight blocks X,Y of orders at least two. The only new triples needed for their concatenation XY are
T_L=(x_{p-1},x_p,y_1)
and
T_R=(x_p,y_1,y_2).
All other consecutive triples are inherited from X or Y.

If both T_L and T_R are tight, then XY is tight, giving alternative (i).

Suppose T_L is tight and T_R is non-tight. Then X'=(x_1,...,x_p,y_1) is tight, while Y'=(y_2,...,y_q) is an inherited tight path (or a singleton when q=2). Thus the same vertex ordering admits the cut shifted one step to the right, giving alternative (ii). If instead T_L is non-tight and T_R is tight, then X'=(x_1,...,x_{p-1}) and Y'=(x_p,y_1,...,y_q) are tight, so the cut shifts one step left.

Finally suppose both T_L and T_R are non-tight. Boundary antisymmetry gives the tight reverses
(y_1,x_p,x_{p-1})
and
(y_2,y_1,x_p).
These are exactly the two consecutive triples of
(y_2,y_1,x_p,x_{p-1}),
so this four-vertex sequence is a tight path, proving alternative (iii).

The trichotomy is purely local. It does not by itself imply termination under repeated cut slides: after a one-step slide, the only available slide at the new interface may be the reverse move. Thus a global Astra-006 descent still requires an additional monotone invariant or a nonlocal relocation argument. ∎