# Double crossing needs only local internality except in the adjacent equality case

## Statement

Let G be a boundary tournament, let F=P|Q be one displayed two-cover, and let x,y be distinct vertices internal in their displayed F-components. Assume G-{x,y} has a two-cover. If x,y lie on different components of F, or lie nonconsecutively on the same component, then deleting them leaves four nonempty inherited path fragments and every two-cover of G-{x,y} contains at least two ordinary edges joining different fragments. No internality hypothesis concerning any other top two-cover is required. If x,y are consecutive on one component and are additionally internal in every two-cover of G, then every lower two-cover has a cross-class edge, and any lower cover with exactly one such edge must directly join the left and right inherited fragments while leaving the opposite top component intact.

## Body

In the different-component case, deleting the two displayed internal vertices cuts the two top paths into four nonempty inherited fragments. In the same-component nonconsecutive case, writing P=(A,x,M,y,B) leaves A,M,B,Q, again four nonempty fragments. Any two paths covering four nonempty fragment classes have at least 4-2=2 transitions between classes. This counting uses only internality in the single chosen display F.

For consecutive x,y, write P=(A,x,y,B). Three nonempty classes A,B,Q remain, so every lower two-cover has at least one cross-class edge. If exactly one occurs, each class appears in one contiguous block. A merge A-Q would leave B alone and allow restoration of the inherited path (x,y,B), producing a top two-cover with x exposed; similarly B-Q would expose y. Under universal internality both are impossible, so the unique merge is A-B and Q remains intact. Thus global universal internality is needed only for this final equality classification, not for the double-crossing alternatives.