# Equal-cover endpoint probes force order disagreement, reciprocal crossing, or a leave-and-return excursion

## Statement

Under the hypotheses of c460f924ee3e, arbitrary exact two-covers of the two displayed endpoints of A force at least one of three scale-free disturbances: (i) relative-order disagreement with an inherited displayed path; (ii) an ordinary edge of an inherited displayed path whose endpoints lie in different components of one endpoint deletion cover; or (iii) within one deletion-cover component, a leave-and-return excursion from an inherited path class through a nonempty segment of other classes and back to the same inherited class.

## Body

By c460f924ee3e, either relative-order disagreement already occurs, giving (i), or one endpoint deletion cover splits an inherited path class R into at least two maximal monochromatic blocks. Apply split_dich to R and that deletion cover. If R meets two deletion-cover components, split_dich gives an ordinary inherited edge crossing their support partition, outcome (ii). If all of R lies in one deletion-cover component, split_dich gives a leave-and-return excursion, outcome (iii). These alternatives are independent of the common component order.
