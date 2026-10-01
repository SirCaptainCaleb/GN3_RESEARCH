# Central longest-path deletions are disturbed from at least one endpoint except for two labels

## Statement

Let H be a minimum counterexample and A=(a_0,...,a_{lambda-1}) a globally longest tight path. Put sigma=2lambda-(|V(H)|-1), choose two-covers G_0 of H-a_0 and G_1 of H-a_{lambda-1}, and assume neither endpoint comparison already gives relative-order disagreement among surviving A-vertices or a tight triple reversing an ordered edge of A. For every index sigma<i<lambda-sigma-1 and every chosen two-cover F_i of H-a_i, relative to each endpoint anchor F_i either joins two inherited pieces, disagrees with an inherited path order, or is the clean same-slot replacement by the omitted endpoint. At most two central labels can be in the clean same-slot branch relative to both endpoint anchors. Hence, for M=max{0,lambda-2sigma-2}, at least max{0,M-2} chosen central deletion covers expose an inherited-piece crossing or order disagreement from at least one end. Moreover every central a_i is internal in the relevant component of each neutral endpoint cover, and every two-cover of the corresponding double deletion crosses the three nonempty inherited pieces.

## Body

Positional lag bounds the shift of a surviving a_i in an order-neutral endpoint deletion cover by the component deficit d<=sigma. Thus sigma<i<lambda-sigma-1 places a_i strictly inside its component. Deleting it produces three nonempty inherited path pieces, and the two-deletion endpoint trichotomy forces every two-cover of the double deletion to cross that three-part partition.

Apply the internal-deletion trichotomy to an arbitrary F_i. From the left endpoint, the only alternatives are: an ordinary edge of F_i joins two inherited pieces; F_i disagrees in relative order with an inherited path; or F_i replaces a_i by a_0 in the same slot while leaving the remaining ordered support data unchanged. The right endpoint gives the symmetric trichotomy.

Restrict G_0-a_{lambda-1} and G_1-a_0 to W=V(H)-{a_0,a_{lambda-1}}. The certified opposite-end comparison says these ordered covers are not identical; choose a pair {u,v} whose component-membership or relative-order state differs. If F_i is a clean same-slot replacement from both ends, then after deleting a_i its ordered restriction agrees with both endpoint restrictions. Unless a_i is u or v, the disagreeing pair survives, contradiction. Hence at most two central labels are clean from both ends. Every other central F_i therefore exposes a crossing or order disagreement from at least one anchor, giving the stated count.
