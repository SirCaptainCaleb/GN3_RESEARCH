# Augment exchange walks only with globally coupled obstruction transitions

## Statement

Proposal: replace the success-only splice graph by a mixed transition system whose successful transitions are checked endpoint-to-cut splices and whose failure states are bounded insertion-obstruction windows. A failure window is not itself an exchange edge. A legal obstruction transition must use information coupling two displayed paths, for example a tight triple meeting both paths or comparison with a second deletion cover. The first target is: from the two obstruction windows attached to a deletion singleton, either construct one checked repartition/merge, or force an order-disagreement witness that enters endpoint transport.

## Body

The success-only graph has an isolated deletion singleton, while every such singleton carries one bounded failed-insertion window on each deletion path. A separate local-independence fence shows that those two windows can be prescribed independently under local boundary-tournament constraints, so no Hall theorem can be obtained merely by adjoining the windows as formal neighbors. This leaves one precise redesign: every non-success transition must be justified by cross-path or global deletion-state information. A useful first lemma would take the two windows sharing the omitted label x and one additional globally forced cross-path relation, and return either a verified pairwise repartition, a direct two-cover, or an explicit order disagreement. Only after such a lemma exists is an alternating-walk/Hall formulation mathematically meaningful.
