# A laminar two-for-two fractional replacement must contain the whole union

## Statement

Let A,B,C,D be subsets of a finite set with A and B overlapping and incomparable. If 1_C+1_D >= 1_A+1_B coordinatewise and {C,D} is laminar, then A intersect B is contained in C intersect D and A union B is contained in C union D. Consequently C and D intersect, so after relabeling C subseteq D, and then A union B subseteq D. In particular, if C,D are required to lie inside A union B, then D=A union B. Thus a same-mass equal-weight two-for-two local fractional replacement of crossing supports by a laminar pair requires the larger replacement support to contain the entire old union.

## Body

The coordinatewise inequality is read vertex by vertex. If v lies in A intersect B, then the right-hand side has value 2 at v. Since each of 1_C and 1_D is at most 1, both must equal 1 there. Hence A intersect B is contained in C intersect D.

If v lies in A union B, then the right-hand side is at least 1 at v, so at least one of C,D contains v. Hence A union B is contained in C union D.

Because A and B overlap, A intersect B is nonempty, so C intersect D is nonempty. Laminarity of {C,D} therefore forces one to contain the other; relabel so C subseteq D. Then C union D=D, and the preceding inclusion gives A union B subseteq D.

If both replacement supports are required to be subsets of A union B, it follows that D=A union B.

Applied to the proposed fractional-path transformation, this shows that the standard equal-epsilon move which decreases two crossing path supports and increases two laminar replacement supports cannot be justified purely by coordinatewise incidence unless one replacement is a tight-path support containing the entire union. Therefore the route cannot rely on a generic two-for-two set-cover replacement template; it needs either a Hamiltonian-union theorem, available slack elsewhere in the fractional solution, more than two replacements, or a genuinely nonlocal transformation.