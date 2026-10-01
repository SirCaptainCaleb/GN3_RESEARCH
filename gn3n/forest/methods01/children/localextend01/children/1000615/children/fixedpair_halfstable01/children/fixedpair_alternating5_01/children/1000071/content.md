# Every prescribed pair supports a full three-label path-cover-two deletion cube

## Statement

Let H be a minimum counterexample and let L,R be any two distinct vertices. Then there exist distinct x,y,z outside {L,R} such that, with T={x,y,z} and G=H-{L,R}, every induced subtournament G-S for S subseteq T is non-Hamiltonian with path-cover number two.

Moreover {L,R,x,y,z} is Hamiltonian, with an explicit tight order of one of the forms
(y,L,x,R,z) or (y,R,x,L,z).

Thus every prescribed pair in a minimum counterexample has a three-label Boolean deletion cube of eight non-Hamiltonian path-cover-two states on its complement, together with a Hamiltonian alternating five-support on the five removed labels.

## Body

Apply fixedpair_alternating5_01 to the prescribed pair L,R. It supplies distinct x,y,z outside {L,R}, with T={x,y,z}, such that one of
(y,L,x,R,z), (y,R,x,L,z)
is a tight Hamilton path.

Writing G=H-{L,R}, that theorem also states that G itself, every G-t for t in T, and every G-{s,t} for distinct s,t in T are non-Hamiltonian with path-cover number two.

It remains only the three-label deletion G-T. But G-T is exactly
H-{L,R,x,y,z},
the complement of the displayed Hamiltonian five-set. Since this five-set is proper in a minimum counterexample, its complement cannot be Hamiltonian, or the two complementary Hamilton paths would form a spanning two-cover of H. By minimum-counterexample calculus its path-cover number is at most two, hence exactly two.

These are precisely all eight subsets S of the three-element set T. No additional orientation or compatibility choice is required.
