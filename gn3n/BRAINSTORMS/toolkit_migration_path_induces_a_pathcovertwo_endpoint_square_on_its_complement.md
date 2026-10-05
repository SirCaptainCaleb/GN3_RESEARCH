# Toolkit migration — Every proper tight path induces a path-cover-two endpoint square on its complement

Preserved from the retired Toolkit Limbo object [[path_induces_a_pathcovertwo_endpoint_square_on_its_complement]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 2,
    "created_at": "2026-09-28T21:13:53.505047+00:00",
    "updated_at": "2026-10-03T15:39:36.649056+00:00",
    "archived_at": "2026-10-03T15:39:36.649056+00:00",
    "original_id": "path_induces_a_pathcovertwo_endpoint_square_on_its_complement",
    "audit_status": "unaudited",
    "math_version": 1,
    "toolkit_type": "other",
    "refutation_status": "unrefuted",
    "author_session_ids": [
    ],
    "audited_math_version": null
}

## Simplified statement

Every proper tight path induces a path-cover-two endpoint square on its complement

## Statement

Let H be a minimum counterexample and let P=(p_0,...,p_m), m>=2, be a proper tight path. Put K=H-V(P). Then each of
K, K+{p_0}, K+{p_m}, and K+{p_0,p_m}
is non-Hamiltonian with path-cover number two.

Equivalently, the complement of every proper tight path of order at least three carries a full two-label path-cover-two square indexed by the two displayed endpoints of P.

## Body

The set V(P) is a proper Hamiltonian support, so minimum-counterexample calculus gives pc(K)=2 and K is non-Hamiltonian.

The complement of K+{p_0} is the inherited tight suffix (p_1,...,p_m). If K+{p_0} were Hamiltonian, a Hamilton path on it together with that suffix would two-cover H. Thus K+{p_0} is non-Hamiltonian; since it is proper, minimality gives path-cover number two. The argument for K+{p_m} is symmetric, using the inherited prefix (p_0,...,p_{m-1}).

Finally, the complement of K+{p_0,p_m} is the inherited middle path (p_1,...,p_{m-1}); when m=2 this is a singleton, which is still a tight path. Again Hamiltonicity of K+{p_0,p_m} would combine with that complementary path to two-cover H. Hence it is non-Hamiltonian and, by minimality, has path-cover number two.

No path reversal or cyclic invariance is used.

## Direct premises at migration

[]

## Direct consumers at migration

[]

## Supersession records at migration

[]

## Retained passed-version snapshot at migration

null
