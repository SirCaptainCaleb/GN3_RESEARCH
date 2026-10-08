# The five-coordinate connector seed reduces its induced gluing problem to one endpoint bit

## Composition

(none yet)

## Development

Continue with a minimum shortcut-free split B->z->A->x and a directed triangle u->v->w->u inside A. By §344, S0=(u,x,z,v,w) and S1=(w,v,z,x,u) have words 000 and 111. For any good order P of B, every B-vertex dominates every coordinate of A union {x,z}, so the left/right extension bits are independent of the exposed seed coordinate. Appending or prepending S0/S1 therefore has a one-bit interface. If the B-word is monochromatic, one seed color always gives a NOR-good concatenation. If it is bichromatic, endpoint concatenation succeeds exactly when the extension bit matches the adjacent phase color. SCOPE: these orders use B union {x,z,u,v,w}. They are spanning only when A={u,v,w}; for larger A they are proper-subinstance relative-splicing data. In the |A|=3 case an interior insertion at the B switch eliminates the remaining blocked endpoint residue.
