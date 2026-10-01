# An anchor of compatibility degree k forces k-2 localized incompatibilities

## Statement

Let d have compatibility degree k>=2 and let F_d=P|Q. Then some neighbor a of d is incompatible with at least k-2 other neighbors b of d. For every such b, deleting d makes F_a and F_b compatible, so their entire incompatibility is localized at d. Moreover at least ceil((k-2)/2) of these partners can be chosen uniformly so that either all b lie in the other anchor path from a, giving support switches of d, or all b lie in the same anchor path as a, giving same-support relative-order relocations of d.

## Body

# Proof

By 47d4a615286a, the induced compatibility graph on N(d) is a linear forest. Every nonempty finite linear forest has a vertex of degree at most one. Choose a in N(d) with degree at most one inside G[N(d)].

There are k-1 other neighbors b of d. At most one is compatible with a, so a is incompatible with at least k-2 of them.

For every such b, the edges ad and bd are present while ab is absent. The anchored-localization lemma compatanchorlocal03 therefore applies: after deleting d, the restrictions of F_a and F_b are compatible, and every support or relative-order disagreement between the full common restrictions is carried by the single label d.

Now classify these at least k-2 labels b using the two displayed components P,Q of F_d. The fixed label a belongs to exactly one of P,Q. At least ceil((k-2)/2) of the incompatible partners b lie uniformly either in the same anchor component as a or in the other anchor component.

If b lies in the other component, compatanchorclass05 shows that F_a,F_b are support-incompatible solely because the restored label d switches between the two anchor support classes.

If b lies in the same component, the same lemma shows that F_a,F_b are support-compatible and their incompatibility is purely a relative-order relocation of d, with the two restored positions localized near a and b in the displayed anchor order.

Thus one anchor of degree k supplies a synchronized family of at least k-2 localized incompatibilities, with a uniform subfamily of size at least ceil((k-2)/2).
