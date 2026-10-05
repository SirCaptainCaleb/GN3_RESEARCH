# Toolkit migration — Every four-side carries four endpoint-pair transport probes

Preserved from the retired Toolkit Limbo object [[four_side_universal_endpoint_probe01]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 2,
    "created_at": "2026-09-29T21:49:28.470274+00:00",
    "updated_at": "2026-10-03T15:39:36.649056+00:00",
    "archived_at": "2026-10-03T15:39:36.649056+00:00",
    "original_id": "four_side_universal_endpoint_probe01",
    "audit_status": "unaudited",
    "math_version": 1,
    "toolkit_type": "other",
    "refutation_status": "unrefuted",
    "author_session_ids": [
    ],
    "audited_math_version": null
}

## Simplified statement

Every four-side carries four endpoint-pair transport probes.

## Statement

Let H be a minimum counterexample and let X|P|Q be a spanning three-cover with |X|=4 and P=(p_1,...,p_m), m>=5. Put M=(p_2,...,p_{m-1}). Then either there is a legal pairwise repartition of X|P with nonincreasing quadratic potential, or the following holds simultaneously for every t in X. Define F_t=(X-{t}) union {p_1,p_m} and L_t=V(M) union {t}. If F_t is Hamiltonian, then L_t is non-Hamiltonian with path-cover number two. If F_t is non-Hamiltonian, then there is a set D_t subseteq F_t of at least four labels such that F_t-{d} is Hamiltonian and L_t union {d} is non-Hamiltonian with path-cover number two for every d in D_t. Any nonincreasing repartition produced by a Hamiltonian F_t|L_t has size change (4,m)->(5,m-1) and potential change 10-2m, neutral at m=5 and strict for m>=6; any repartition produced from a good deletion d in a non-Hamiltonian F_t preserves the size pair {4,m} and is neutral.

## Body

Fix t in X and write F=F_t, L=L_t. The sets F and L are disjoint and partition V(X) union V(P), with |F|=5 and |L|=m-1. If F is Hamiltonian and L is Hamiltonian, F|L is a legal pairwise repartition of X|P; its potential change is 25+(m-1)^2-(16+m^2)=10-2m<=0 for m>=5. Therefore, if no nonincreasing repartition exists, Hamiltonicity of F forces L to be non-Hamiltonian, and minimum-counterexample calculus gives pc(L)=2. Now suppose F is non-Hamiltonian. The five-vertex small-set theorem gives a set D of at least four labels d in F for which F-{d} is Hamiltonian. For each such d, the complementary support in X union P is L+d, of order m. If any L+d were Hamiltonian, (F-{d})|(L+d) would be a legal pairwise repartition of X|P preserving the component sizes {4,m}, hence preserving Phi. Therefore absence of a nonincreasing repartition forces every L+d to be non-Hamiltonian; minimum-counterexample calculus gives pc(L+d)=2. This argument is independent of t, so it holds simultaneously for all four choices t in X.

## Direct premises at migration

[]

## Direct consumers at migration

[]

## Supersession records at migration

[]

## Retained passed-version snapshot at migration

null
