# Toolkit migration — Mutual deletion internality forces four endpoint windows or doubled reverse constraints

Preserved from the retired Toolkit Limbo object [[mutual_internal_endpoint_grid01]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 2,
    "created_at": "2026-10-01T01:39:56.928465+00:00",
    "updated_at": "2026-10-03T15:39:36.649056+00:00",
    "archived_at": "2026-10-03T15:39:36.649056+00:00",
    "original_id": "mutual_internal_endpoint_grid01",
    "audit_status": "unaudited",
    "math_version": 1,
    "toolkit_type": "other",
    "refutation_status": "unrefuted",
    "author_session_ids": [
    ],
    "audited_math_version": null
}

## Simplified statement

Two mutually internal deletion labels force, at every end of their common lower cover, either a Hamiltonian K4 or a doubled reverse constraint.

## Statement

Let H be a minimum counterexample and let d,t be distinct vertices such that d is internal in every two-cover of H-t and t is internal in every two-cover of H-d. Let H-{d,t}=P|Q be any displayed two-cover, with P=(p_0,...,p_m) and Q=(q_0,...,q_s). Then |P|,|Q|>=3. At each of the four displayed ends, one has a Hamiltonian four-window with non-Hamiltonian path-cover-two complement or a doubled reverse constraint. More precisely: at the initial end of P, either {p_1,p_0,d,t} is Hamiltonian, or both (t,d,p_0) and (d,t,p_0) are tight; at the terminal end of P, either {d,t,p_m,p_{m-1}} is Hamiltonian, or both (p_m,t,d) and (p_m,d,t) are tight. The analogous two alternatives hold at the initial and terminal ends of Q.

## Body

Apply square_permanent_internal_hooks01 first to G=H-t with universally internal vertex d and the lower two-cover G-d=H-{d,t}=P|Q. It gives |P|,|Q|>=3 and the endpoint hooks (p_1,p_0,d), (d,p_m,p_{m-1}), (q_1,q_0,d), and (d,q_s,q_{s-1}). Apply the same theorem to G'=H-d with universally internal vertex t and the same lower cover G'-t=P|Q. This gives the parallel hooks (p_1,p_0,t), (t,p_m,p_{m-1}), (q_1,q_0,t), and (t,q_s,q_{s-1}).

Consider the initial end of P. If (p_0,d,t) is tight, then (p_1,p_0,d,t) is a tight Hamiltonian four-path, using the hook (p_1,p_0,d). If (p_0,t,d) is tight, then (p_1,p_0,t,d) is a tight Hamiltonian four-path. If neither is tight, boundary antisymmetry forces both reversals (t,d,p_0) and (d,t,p_0) to be tight. This proves the initial-end dichotomy.

At the terminal end, if (d,t,p_m) is tight then (d,t,p_m,p_{m-1}) is a tight Hamiltonian four-path using (t,p_m,p_{m-1}); if (t,d,p_m) is tight then (t,d,p_m,p_{m-1}) is tight using (d,p_m,p_{m-1}). If neither is tight, boundary antisymmetry gives both (p_m,t,d) and (p_m,d,t). The two Q-end statements are identical.

Whenever one of these four-sets is Hamiltonian, it is proper. Its complement cannot be Hamiltonian, since complementary Hamilton paths would two-cover H; minimum-counterexample calculus therefore gives path-cover number two.

## Direct premises at migration

[]

## Direct consumers at migration

[]

## Supersession records at migration

[]

## Retained passed-version snapshot at migration

null
