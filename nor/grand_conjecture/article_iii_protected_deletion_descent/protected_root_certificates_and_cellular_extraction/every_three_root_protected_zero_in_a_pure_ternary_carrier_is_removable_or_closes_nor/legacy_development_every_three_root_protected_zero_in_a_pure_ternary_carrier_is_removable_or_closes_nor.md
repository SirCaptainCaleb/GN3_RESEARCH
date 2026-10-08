# Every three-root protected zero in a pure ternary carrier is removable or closes NOR — preserved pre-item development

## Every three-root protected zero in a pure ternary carrier is removable or closes NOR

Continue from root §177 in the pure alternating ternary sector.

Let a support-minimal positive zero of actual window-slide roots in one ordered-partition carrier cell have exactly three roots. Then, after scaling,

rho_1=e_a-e_b,
rho_2=e_b-e_c,
rho_3=e_c-e_a.

Root §177 already shows that if a middle-swapped certificate chamber supplies any actual 10 root transverse to W_{abc}, the triangular zero is locally removable. Root §176 removes any opposite-root two-term subzero. Thus the only purported essential residue is:

- every inspected chamber root has endpoints in {a,b,c};
- no opposite triangle direction occurs;
- only the three forward directions rho_1,rho_2,rho_3 may survive.

We show that this residue produces a spanning one-change order.

### Step 1: a surviving triangle root after one middle swap was already present before the swap

Take a chamber pi carrying rho_1=e_a-e_b on the certified 10 packet

(a,u,v,b)

in four consecutive positions. Write pos(a)=r, so pos(b)=r+3.

Swap the two middle coordinates u,v, obtaining pi^*.

The packet (a,v,u,b) has colors 01 by alternation, so pi^* does not carry rho_1 as a 10 descent.

Counterexamplehood says pi^* still has some 10 descent. In the essential planar residue its root is rho_2 or rho_3.

If pi^* carries rho_2=e_b-e_c, then a ternary slide root forces

pos(c)=pos(b)+3=r+6.

Its unique certificate uses the four positions r+3,...,r+6. The swap u<->v occurred at positions r+1,r+2, so none of the two ternary windows of this b->c descent is affected. Therefore rho_2 was already a 10 descent in the original chamber pi.

If pi^* carries rho_3=e_c-e_a, then necessarily

pos(c)=pos(a)-3=r-3.

Again its unique four-position certificate lies entirely before the swapped middle pair, so rho_3 was already present in pi.

Hence every essential planar chamber carrying one cycle edge actually carries at least one adjacent cycle edge as well.

### Step 2: normalize to a two-edge directed path

By cyclic relabeling/reversal of the argument, assume pi carries

rho_1=e_a-e_b
and
rho_2=e_b-e_c.

Then the endpoint positions are forced to be

pos(a)=r,
pos(b)=r+3,
pos(c)=r+6.

Let the two certified four-packets be

(a,u,v,b)
and
(b,s,t,c).

Their middle pairs {u,v} and {s,t} are disjoint, occupying positions r+1,r+2 and r+4,r+5.

### Step 3: swap both middle pairs

Perform the two adjacent transpositions

u<->v,
s<->t.

They are disjoint and commute, and the resulting chamber pi^{**} still refines the same ordered-partition carrier cell.

By alternation,

(a,u,v,b): 10 -> (a,v,u,b): 01,

and independently

(b,s,t,c): 10 -> (b,t,s,c): 01.

Thus pi^{**} carries neither rho_1 nor rho_2 as a 10 root.

The endpoint positions a,b,c are unchanged. Therefore:

- rho_1 cannot occur elsewhere, because a,b are exactly three positions apart and their unique slide packet is the one just changed to 01;
- rho_2 cannot occur elsewhere for the same reason;
- rho_3=e_c-e_a is impossible in pi^{**}, because c occurs six positions AFTER a, whereas a ternary root e_c-e_a requires c exactly three positions BEFORE a.

So pi^{**} carries none of the three forward triangle roots.

### Step 4: counterexamplehood gives the contradiction

If pi^{**} had any actual 10 root sigma transverse to W_{abc}, then exactly the cone/blow-up argument of root §177 would remove the original triangular zero.

If it had an opposite triangle root, then together with the corresponding original rho_i it would give a two-root protected zero, removable by root §176.

Hence in an essential three-root residue pi^{**} can carry no actual 10 root at all.

But a binary word with no adjacent 10 pattern is monotone nondecreasing, hence has the form

0^* 1^*.

Therefore pi^{**} is a spanning one-change order, contradicting counterexamplehood.

### Theorem

Every support-minimal three-root positive zero of actual ternary window-slide roots in one ordered-partition carrier cell is either:

1. locally removable through a transverse actual root;
2. reducible to a removable two-root zero; or
3. directly converted by two commuting middle swaps into a spanning one-change order.

Consequently an essential protected-root zero in the pure alternating ternary sector has support size at least four.

This closes the planar A2 recycling residue left open in root §177.
