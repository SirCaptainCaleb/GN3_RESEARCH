# Toolkit migration — A three-side singleton lift reaches a positioned five-support by two nonincreasing pairwise repartitions

Preserved from the retired Toolkit Limbo object [[threeside_bounded_endpoint_five_repartition01]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 2,
    "created_at": "2026-09-29T22:48:48.45512+00:00",
    "updated_at": "2026-10-03T15:39:36.649056+00:00",
    "archived_at": "2026-10-03T15:39:36.649056+00:00",
    "original_id": "threeside_bounded_endpoint_five_repartition01",
    "audit_status": "unaudited",
    "math_version": 1,
    "toolkit_type": "other",
    "refutation_status": "unrefuted",
    "author_session_ids": [
    ],
    "audited_math_version": null
}

## Simplified statement

A three-side singleton lift reaches a positioned five-support by two nonincreasing pairwise repartitions.

## Statement

Let C=P|(x)|Q be a spanning three-cover of a boundary tournament, with |P|=3 and Q=(q_0,...,q_{m-1}), m>=5. Put X=V(P) union {x}. For every prescribed pair Z={z,zprime} subset X, at least one of F_z={z,q_0,q_1,q_2,q_3}, F_zprime={zprime,q_0,q_1,q_2,q_3}, and F_Z={z,zprime,q_0,q_1,q_2} is Hamiltonian. A Hamiltonian F_z or F_zprime yields a spanning three-cover with component orders (5,3,m-4), whose complement paths have supports X-{z} or X-{zprime}, and {q_4,...,q_{m-1}}. A Hamiltonian F_Z yields a spanning three-cover with orders (5,2,m-3), whose complement paths have supports X-Z and {q_3,...,q_{m-1}}. Thus at most eight vertices near the chosen endpoint are rearranged, and the remaining Q-segment is retained in its displayed order. Relative to C, the quadratic-potential changes are respectively 40-8m and 28-6m. Both are strictly negative for m>=6; at m=5 the first is zero and the second is negative. The analogous result holds at the other endpoint, retaining the displayed prefix of Q. In a minimum-counterexample deletion cover with |P|=3, m>=7, so both branches are strict. The new cover is reachable from C by at most two pairwise repartitions, each nonincreasing in quadratic potential. The first repartitions P|(x) into component orders (1,3) in a one-label branch, or into (2,2) in the two-label branch; the second repartitions the selected singleton or pair with Q, keeping the other short path unchanged. Therefore for m>=6 this is strict descent within the same pairwise-repartition component.

## Body

Fix Z={z,zprime}. Let U=Z union {q_0,q_1,q_2,q_3}, a six-set. The three listed five-supports are U-{zprime}, U-{z}, and U-{q_3}. They are distinct. By the four-of-six theorem in smallset01, at most two five-subsets of U are non-Hamiltonian. Hence at least one listed support is Hamiltonian. This does not require X or the four-vertex Q-window to be Hamiltonian, and does not use endpoint constraints or cyclic rotation of tight triples. If F_z is Hamiltonian, choose a Hamilton path on it. The three-set X-{z} has a tight Hamilton path: on any three-set a boundary tournament contains a tight ordering by its reversal-pair axiom. Pair these two paths with the displayed suffix (q_4,...,q_{m-1}), which is nonempty for m>=5. Their supports partition V(C), so they form a spanning three-cover. The F_zprime branch is identical. If F_Z is Hamiltonian, X-Z is a two-set and hence a tight path in either order; pair it with a Hamilton path on F_Z and the displayed suffix (q_3,...,q_{m-1}). Again the supports are disjoint and spanning. These are actual repartitions of the original three-cover, with explicit complementary paths, rather than arbitrary complement covers from minimality. In the first branch only X and the first four vertices of Q change path assignments; in the second only X and the first three change assignments. The original potential is 3^2+1^2+m^2=m^2+10. The two new potentials are 5^2+3^2+(m-4)^2 and 5^2+2^2+(m-3)^2, giving the stated differences. For the other endpoint use U=Z union the last four displayed Q-vertices, and take the third candidate by deleting the earliest of these four. The inherited complement is then the displayed prefix, so no reversal of a tight path is invoked. In a minimum counterexample, mincex01 gives order greater than ten, and n=m+4 implies m>=7. This is a replacement for the proposed endpoint alternating-five-window route in threeside_consecutive_fivewindows01: it gives a positioned five-support and inherited complementary two-cover, while it does not assert that all four two-label five-windows are Hamiltonian. The new cover is reachable by at most two legal pairwise repartitions, with no increase of quadratic potential at either step. In the F_z branch, repartition P|(x), on its four-vertex union X, into (z)|R where R is a Hamilton path on X-{z}. Such a three-vertex Hamilton path always exists. This first step preserves the component orders 1,3 and is neutral; omit it if z=x. Now repartition (z)|Q into a Hamilton path on F_z and the displayed suffix (q_4,...,q_{m-1}), leaving R unchanged. Its potential change is 40-8m. The F_zprime branch is identical. In the F_Z branch, first repartition P|(x) into the two two-vertex paths on Z and X-Z. This decreases potential by 2, since 2^2+2^2-(3^2+1^2)=-2. Next repartition the two-path on Z together with Q into a Hamilton path on F_Z and the displayed suffix (q_3,...,q_{m-1}), leaving the other two-path unchanged. This step changes potential by 30-6m, which is nonpositive for m>=5. The combined change is 28-6m. Thus at m=5 each step is still nonincreasing, and the F_Z route is strict in its first step. For m>=6 either branch yields a strict pairwise-reachable decrease, without changing any long-path vertices beyond the first four. All states remain in the original pairwise-repartition component. The omitted singleton label may change or disappear as a singleton during these legal moves; keeping that label omitted throughout is not asserted. A two-cover is not produced.

## Direct premises at migration

[]

## Direct consumers at migration

[]

## Supersession records at migration

[]

## Retained passed-version snapshot at migration

null
