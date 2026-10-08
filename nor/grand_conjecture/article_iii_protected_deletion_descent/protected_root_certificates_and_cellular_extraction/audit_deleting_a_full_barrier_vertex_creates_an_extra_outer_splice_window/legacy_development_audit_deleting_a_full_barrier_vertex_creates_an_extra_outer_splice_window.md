# Audit deleting a full-barrier vertex creates an extra outer splice window — preserved pre-item development

Root §136 correctly identifies the local off-face of a fully-curved 10 tetrahedron, but its deletion-shadow conclusion omits one changed outer window.

Let an actual order contain
(...,r,u,v,w,z,t,...)
and suppose the consecutive barrier windows are
alpha(u,v,w)=1,
alpha(v,w,z)=0.
For a fully-curved 10 tetrahedron,
alpha(u,v,z)=0
and
alpha(u,w,z)=1.

Delete the third barrier coordinate w.

The old ternary windows involving w are THREE windows, not two:
alpha(u,v,w),
alpha(v,w,z),
alpha(w,z,t)
when the right exterior coordinate t exists.

After deletion they are replaced by TWO windows:
alpha(u,v,z)=0,
alpha(v,z,t).

Thus the full-curvature identity controls the first replacement window, but it says nothing by itself about the new outer splice
alpha(v,z,t)
relative to the old exterior value
alpha(w,z,t).

Therefore deleting w does NOT in general leave every outside target status unchanged. A new right-boundary defect may be created.

The zero-shadow statement is valid only in one of the following situations:
1. z is at the global right endpoint, so no exterior window exists;
2. alpha(v,z,t) is independently proved to equal the required target value;
3. the resulting outer splice is explicitly included in a subsequent protected transport argument.

Applied to the long stopped endpoint prefix of roots §§133/135, a terminal full barrier is near the LEFT end and normally has exterior coordinates to its right. Hence §136 does not yet produce a target-compatible two-omission shadow there.

This audit does not affect root §135. The adjacent swaps in §135 were computed with all four changed ternary window ranks, including the outer-left spill, and its exact three-barrier classification remains valid.

The correct exchange problem after a terminal full barrier therefore retains one additional outer splice bit. Any omission-exchange theorem must control that bit rather than treating the suffix as frozen.
