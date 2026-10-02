# Flat-transfer joint classification and entrance-to-entrance path

## Statement


Let e->f be an equal-rank ascending terminal-clean transfer of rank q. Let y=e∩f be the source-shared joint on the transfer q-cycle and let b be the other cycle joint of f.

Then y is terminal for f. The joint b is the unique entrance x_f of f if and only if phi(b)=q-1; if b is instead the other terminal of f, then phi(b)>=q.

In the entrance-joint case b=x_f, the deficiency-two precursor R=(g_2,...,g_{q-1}) is a (q-2)-edge linear path whose two last vertices can be chosen as x_f and the entrance x_e of e. Moreover R avoids both terminals of e and both terminals of f.


## Body


The transfer-cycle construction already forces the shared joint y=e∩f to be terminal for f. No corresponding type is automatic for the opposite joint b.

Since f is ascending of rank q, its unique entrance has endpoint potential q-1. Conversely every terminal t of a rank-q edge has phi(t)>=q: take a q-edge longest path ending in f through its entrance and choose t as the final vertex of f. Hence b is the entrance exactly when phi(b)=q-1, while terminal type forces phi(b)>=q.

Assume now phi(b)=q-1, so b=x_f. In the transfer notation the deficiency-two precursor R=(g_2,...,g_{q-1}) has length q-2, ends at x_e, and has b as its opposite last vertex. Thus orienting R from b to x_e gives a path from x_f to x_e. The original entrance precursor for e avoids both terminals of e, hence so does R. The transfer edge f is clean relative to R except for b=x_f, so R contains no other vertex of f and therefore avoids both terminals of f.

The open labeled-overlap obstruction is deliberately not absorbed here; it remains the explicit proposal child that follows this proved structural step.
