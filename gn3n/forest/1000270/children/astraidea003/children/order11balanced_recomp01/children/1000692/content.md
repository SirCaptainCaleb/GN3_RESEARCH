# Order eleven reduces the merge problem to three finite longest-path obstruction types

## Statement

Let H be a hypothetical order-eleven minimum counterexample and let lambda be its maximum tight-path order. Then lambda is 5, 6, or 7. If lambda=5, every equitable 5|5|1 deletion state exposes an internal crossing or relative-order disagreement. If lambda=6, the codimension-five endpoint normalization yields either at least two Hamiltonian-side/complement crossings, explicit relative-order disagreement, or an endpoint-exchanged tight six-path with non-Hamiltonian five-complement. If lambda=7, the codimension-four structure yields, on the four-vertex complement together with four distinguished path vertices, an exact two-cover of type 4|4 or 6|2; together with the three internal path vertices this is an explicit 4|4|3 or 6|2|3 spanning obstruction state.

## Body

# Finite longest-path obstruction menu at order eleven

Let H be a hypothetical minimum counterexample of order eleven and let λ be the maximum order of a tight path.

The certified half-order theorem gives λ≥ceil((11-1)/2)=5. The minimum-counterexample calculus says every tight path leaves at least four vertices, so λ≤7. Hence

λ∈{5,6,7}.

## λ=5

There is no tight six-path. This is exactly the ordinary extremal (5,5,1) branch of the certified order-eleven stress test 2ac31d8f3bb6. Its internal non-clean deletion theorem says that in every exact equitable state H-x=P|Q, at least one of the two five-components has an internal good deletion that is not the same-slot clean replacement. The internal-deletion localization theorem therefore produces either an ordinary crossing between inherited path pieces or relative-order disagreement with the inherited five-path order.

Thus λ=5 gives explicit crossing/order complexity directly.

## λ=6

Let Y be a globally longest tight six-path and let F=V(H)-V(Y), so |F|=5. The complement F is non-Hamiltonian, since otherwise Y together with a Hamilton path on F would two-cover H.

Because H is a minimum grand counterexample, it is also minimum among counterexamples admitting a Hamiltonian side with a five-vertex complement: any smaller counterexample to that restricted statement would itself be a smaller grand counterexample. Therefore the certified codimension-five module codim5_01 applies to Y|F.

Its final endpoint normalization gives one of three outcomes:

1. an endpoint-deletion exact two-cover has at least two ordinary edges crossing between the surviving Hamiltonian-side vertices and F;
2. an endpoint-deletion comparison exposes relative-order disagreement, hence a reversed common edge, reversing tight triple, or vertex-simple tight cycle; or
3. there are distinct ell,r∈F such that replacing the two ends of Y by ell,r produces another tight six-path
   (ell,y_1,y_2,y_3,y_4,r)
   whose complementary five-set is non-Hamiltonian.

Thus the neutral λ=6 residue is not arbitrary recurrence: it is an exact two-end support exchange preserving the 6+5 longest-path shell.

## λ=7

Let Y=(x_0,...,x_6) be a globally longest seven-path and S=V(H)-V(Y), |S|=4. Again S is non-Hamiltonian, or S|Y would be a spanning two-cover.

Apply the certified codimension-four module codim4_01. In its minimal-Hamiltonian-side reduction the minimal side must be all of Y: if a proper nonempty Hamiltonian Z⊊Y still had pc(H[S∪Z])>2, that proper induced subtournament would be a smaller grand counterexample. Hence the module applies with Hamiltonian side order seven.

Its eight-vertex endpoint/complement proposition, with L=x_0, u=x_1, v=x_5, R=x_6 and internal path N=(x_2,x_3,x_4), gives an exact two-cover of

S∪{L,u,v,R}

of one of the following forms:

- 4|4; or
- 6|2.

Adding the disjoint tight three-path N gives an explicit spanning three-cover of H of type 4|4|3 or 6|2|3, with the first eight vertices governed by the rigid matching-block endpoint structure of codim4_01.

Therefore every hypothetical order-eleven counterexample lies in one of three finite obstruction families. Combined with the global Astra connectivity of the three-cover state space, the remaining task is purely to consume these crossings/order disagreements/endpoint-exchange kernels into an actual two-component merge or defect span at most two.
