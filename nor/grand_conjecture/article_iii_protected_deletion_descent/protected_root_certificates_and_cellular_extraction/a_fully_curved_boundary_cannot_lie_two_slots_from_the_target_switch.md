# Audit: endpoint relocation does not enlarge the width-two compatible band

## Composition

(none yet)

## Development

## Audit correction

The endpoint-relocation argument in the previous development does NOT prove that a width-two full-full corridor is impossible.

Keep the local notation
A,B,B,A
on six consecutive coordinates (0,1,2,3,4,5), with B=1-A, and assume the right B->A boundary on {2,3,4,5} is fully curved. Then indeed
alpha(2,4,5)=B,
and if t=alpha(1,2,4), relocating coordinate 3 to a remote global endpoint changes the local corridor to
A,t,B.
If t=B one keeps the cut; if t=A one shifts the cut one rank right. In either case the displayed local windows are target-compatible.

The error was the claim that this strictly enlarges the target-compatible band. Removing coordinate 3 from the corridor also removes one ternary window rank. If the next unchanged exterior window is mismatching, that exterior mismatch shifts inward by one rank. Consequently the number of matched windows in the maximal band can remain exactly the same as before.

Thus relocation is a legitimate transport of the boundary obstruction, not a strict band-length improvement.

This is consistent with the independently proved barrier-reflection gadget: width-two full-full corridors have exact transport structure, but no monotone potential has yet been established for repeated reflections/relocations.

Safe retained fact: the fully-curved B->A boundary has a canonical B-shadow alpha(2,4,5)=B, so moving its second coordinate away removes that particular barrier without creating any new defect inside the shortened local packet. Any global use must account for the rank compression and the new first exterior window.

No width-two exclusion is claimed.
