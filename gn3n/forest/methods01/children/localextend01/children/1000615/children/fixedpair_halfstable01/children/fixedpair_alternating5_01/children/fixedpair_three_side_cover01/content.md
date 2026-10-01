# Every prescribed pair lies on a three-side with path-cover-two complement

## Statement

Let H be a minimum counterexample and let L,R be any two distinct vertices. Then there exists x outside {L,R} such that one of (L,x,R) and (R,x,L) is a tight three-vertex path and H-{L,R,x} is non-Hamiltonian with path-cover number two. Consequently H has a spanning three-path cover whose three-vertex component contains the prescribed pair {L,R}.

## Body

Apply fixedpair_alternating5_01 to L,R. It gives distinct x,y,z outside {L,R} such that either (y,L,x,R,z) or (y,R,x,L,z) is a tight path. Hence respectively (L,x,R) or (R,x,L) is a tight three-vertex subpath. Writing G=H-{L,R} and T={x,y,z}, the same theorem states that G-x=H-{L,R,x} is non-Hamiltonian with path-cover number two. Choosing any two-cover P|Q of H-{L,R,x}, the tight triple on {L,x,R} together with P|Q is a spanning three-path cover of H whose three-vertex component contains the prescribed pair.
