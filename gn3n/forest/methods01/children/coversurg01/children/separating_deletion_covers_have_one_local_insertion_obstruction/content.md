# Compatible separating deletion covers have one local insertion obstruction

## Statement

Let H be a boundary tournament and let s,t be distinct vertices for which H has no two-cover separating s and t. Let x,y be distinct vertices outside {s,t}. Suppose F_x is a two-cover of H-x separating s,t, F_y is a two-cover of H-y separating s,t, and F_x,F_y are compatible on V(H)-{x,y}. Then their common pair-state data have two ordered support classes P,Q with s and t in different classes. The omitted labels x and y restore to the same common class, and their insertion slots in that common order are identical or adjacent. If the slots are adjacent with common order L,z,R and F_y=(L,x,z,R)|Q, F_x=(L,z,y,R)|Q, then (x,z,y) is non-tight and (y,z,x) is tight.

## Body

Compatibility on the common domain gives two ordered support classes P,Q, because both deletion covers have two components and both separate the surviving vertices s,t. In particular s and t lie in different common classes.

In F_x the surviving omitted label y is inserted into exactly one common class; in F_y the label x is inserted into exactly one common class.

If x and y restore to different common classes, augment each common class by the label that belongs to it, using the path order inherited from the corresponding deletion cover. These two paths cover H. Since s and t belong to different common classes, the resulting two-cover separates s,t, contradiction. Hence both labels restore to the same common class, say P.

If their insertion slots in P differ by at least two, insert both labels into P at their respective slots. No consecutive triple contains both inserted labels. Every consecutive triple is inherited from one of F_x,F_y or from the common order away from the two insertion sites. Together with Q this gives a two-cover of H that still separates s and t, contradiction. Thus the two slots are equal or adjacent.

In the adjacent-slot case write the common order as P=L,z,R with
F_y=(L,x,z,R)|Q and F_x=(L,z,y,R)|Q.
All consecutive triples of (L,x,z,y,R) are certified by F_x or F_y except possibly (x,z,y). If this triple were tight, that path together with Q would separate s and t in a two-cover of H. Therefore (x,z,y) is non-tight. Boundary antisymmetry gives (y,z,x) tight.

Thus compatibility of two separating deletion covers is confined to one same-support insertion obstruction, with no hypothesis that H itself lacks all two-covers.