# Toolkit migration — A quadratic-minimal 4|5|m cover has a cyclic exchange or one of three insertion-obstruction outcomes

Preserved from the retired Toolkit Limbo object [[local45_locked_finite_menu01]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 2,
    "created_at": "2026-09-29T20:33:12.635251+00:00",
    "updated_at": "2026-10-03T15:39:36.649056+00:00",
    "archived_at": "2026-10-03T15:39:36.649056+00:00",
    "original_id": "local45_locked_finite_menu01",
    "audit_status": "unaudited",
    "math_version": 1,
    "toolkit_type": "other",
    "refutation_status": "unrefuted",
    "author_session_ids": [
    ],
    "audited_math_version": null
}

## Simplified statement

A quadratic-minimal 4|5|m cover has a cyclic exchange or one of three insertion-obstruction outcomes.

## Statement

Let H be a boundary tournament and let C=X|Y|P minimize quadratic potential within its connected pairwise-repartition component, with |X|=4, |Y|=5, and P=(p_1,...,p_m) of order m>=7. Then at least one of the following holds. (1) C has a nontrivial equal-Phi cyclic support exchange of profile 4|5|m. (2) Some y in Y has a first-type failed-insertion window on P, whose associated four-set is either Hamiltonian or the cyclic non-Hamiltonian four-vertex configuration from smallset01, whose every one-vertex extension is Hamiltonian. (3) Two distinct labels y,z in Y have second-type obstruction at the same gap of P, and {y,z} together with that displayed gap edge is Hamiltonian. (4) Two distinct labels y,z in Y are joined by a tight connector (y,p_{r+1},...,p_s,z) through an interval of P with s>=r+2. Thus, once neutral cyclic exchange is excluded, the 4|5|m potential-minimizing cover reduces to a four-vertex configuration or a direct connector between two vertices of the five-side through the long path.

## Body

Apply local45_exchange_or_triplelock01. If its neutral cyclic-exchange alternative occurs, we have (1). Otherwise choose three distinct labels y_1,y_2,y_3 in Y that are noninsertable into every position of P.

Apply the failed-insertion normal form insert01 separately to these three labels. If some label has alternative 1, 0425e03e2aa3 gives exactly outcome (2).

Assume all three have alternative 2, at gap indices i,j,k. Sort the indices. If two are equal, the same-gap case of 36fccff06d48 yields outcome (3). If they are pairwise distinct, the smallest and largest differ by at least two, and the separated-gap case of 36fccff06d48 yields outcome (4). These cases exhaust the three locked labels.

## Direct premises at migration

[]

## Direct consumers at migration

[]

## Supersession records at migration

[]

## Retained passed-version snapshot at migration

null
