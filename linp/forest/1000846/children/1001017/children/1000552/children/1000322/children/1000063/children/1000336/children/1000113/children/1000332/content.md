# Refuted: consecutive private single blockers need not force an extension

## Statement

Refuted. Consecutive private single blockers can occur on a longest endpoint path; the explicit counterexample 2712f65b5d5e has a longest 3-edge x-ending path with such blockers in consecutive private slots p_2,p_3.

## Body

The proposed splice was invalid because reversing the prefix does not eliminate all inherited path intersections. In the counterexample 2712f65b5d5e, the attempted longer route leaves an old consecutive-path intersection as a nonconsecutive chord. Retain this object only as a fence: private-slot single blockers need not form an independent set along the cell chain, and any multi-blocker splice must explicitly track inherited path intersections.
