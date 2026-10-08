# Planar A2 recycling is impossible: middle swaps strictly eliminate 10 descents — preserved pre-item development

## Development

## Planar A2 recycling is impossible: middle swaps strictly eliminate 10 descents

Work in the pure alternating ternary sector and in one ordered-partition carrier cell.

Continue from the support-minimal three-root zero of §177. Thus the physical root support is the directed A2 triangle
rho_1=e_a-e_b,
rho_2=e_b-e_c,
rho_3=e_c-e_a,
and a three-root zero is already removable unless, after middle-swapping any certified 10 packet, every actual 10 descent available in the swapped chamber has physical root in the A2 subsystem on {a,b,c}.

We show that this planar recycling residue is impossible.

### One middle swap

Take a chamber whose certified 10 packet for rho=e_a-e_b occurs in the local coordinate sequence

..., t, r, a, u, v, b, s, z, ...

with
alpha(a,u,v)=1,
alpha(u,v,b)=0.

Swap the two middle coordinates u,v. The new local order is

..., t, r, a, v, u, b, s, z, ...

and alternation gives the two central colors

alpha(a,v,u)=0,
alpha(v,u,b)=1.

Write the affected/new neighboring status word as

A, B, 0, 1, C, D,

where
A=alpha(t,r,a),
B=alpha(r,a,v),
C=alpha(u,b,s),
D=alpha(b,s,z).

The statuses A,D are unchanged by the middle swap; B,C are the two outer changed windows.

### Planarity forces B=0

If B=1, then the adjacent pair B,0 is a new actual 10 descent supported by the ordered tetrahedron

(r,a,v,u).

Its physical root is
e_r-e_u.

The four packet coordinates a,u,v,b are distinct. If u is not c, then u is already outside {a,b,c}; if u=c, then r is outside {a,b,c}, because r is distinct from a,u,v,b and a,b,c are already represented by a,b,u. Hence in all cases e_r-e_u is transverse to the A2 subsystem on {a,b,c}.

By §177, such a transverse actual root removes the three-root zero.

Therefore a genuinely planar residue forces
B=0.

### Planarity forces C=1

If C=0, then the adjacent pair 1,C is an actual 10 descent on

(v,u,b,s)

with physical root
e_v-e_s.

Exactly the same distinctness argument shows that at least one of v,s lies outside {a,b,c}. Hence this root is transverse and removes the zero.

Therefore a planar residue forces
C=1.

### The next outer windows are forced as well

Suppose A=1. Since B=0, the pair A,B is a 10 descent on the ordered tetrahedron

(t,r,a,v)

with root
e_t-e_v.

If v is not c, this is immediately transverse. If v=c, then t is outside {a,b,c}, because a,b,c already occur among a,b,v and coordinates do not repeat. Thus e_t-e_v is transverse in every case.

Hence planarity forces
A=0.

Similarly, if D=0, then C,D is a 10 descent on

(u,b,s,z)

with root
e_u-e_z.

If u is not c it is transverse; if u=c then z is outside {a,b,c}. Therefore planarity forces
D=1.

Consequently every middle swap which remains inside the planar residue has the exact six-status neighborhood

0,0,0,1,1,1

across the affected region.

In particular:
- the original certified central 10 descent has disappeared;
- no new 10 descent is created at either changed outer window;
- no new 10 descent is created at either boundary between the changed packet and the unchanged word.

Every 10 descent outside this neighborhood is unchanged.

### Strict descent in the number of 10 transitions

Let N_10(pi) be the number of adjacent status pairs 1,0 in the full linear ternary word of a chamber pi.

Choose any actual 10 descent in a chamber belonging to the planar residue and perform its middle swap.

If a transverse root appears, §177 removes the carrier zero.

Otherwise the preceding argument applies, and
N_10(pi') < N_10(pi).
Indeed the chosen 10 descent is removed and no new 10 descent is created.

Thus planar recycling admits a strict nonnegative integer potential N_10.

Iterating cannot cycle. It terminates at a chamber with
N_10=0.

A binary linear word with no occurrence 10 is of the form
0^r 1^s
allowing either run to be empty. Hence the terminal chamber is a spanning order with at most one status change.

That is a NOR order, contradicting counterexamplehood.

### Theorem

A support-minimal positive three-root zero of actual protected ternary window-slide roots in one carrier cell is always locally removable.

More explicitly, for the directed A2 root triangle:
- if any middle-swapped certificate chamber exposes a transverse actual 10 root, cone through that root as in §177;
- otherwise every middle swap strictly decreases the number of 10 descents, and finite iteration reaches a spanning one-change chamber.

Therefore the planar A2 recycling residue of §177 does not exist.

### Topological consequence

After the two-root blow-up of §176 and the present theorem, an essential local zero of the pure ternary protected-root carrier must have support size at least four.

The first topologically nonremovable candidate is therefore a genuine four-or-more-root dependence. In type A this means the next obstruction cannot be an opposite pair or a directed root triangle; it must contain a larger physical circuit or a union of circuits.
