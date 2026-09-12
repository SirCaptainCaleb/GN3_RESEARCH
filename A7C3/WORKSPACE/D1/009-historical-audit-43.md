# Exact 43-configuration audit of the monotone minimum residue

**Workspace:** D1
**State:** example
**Key:** `historical-audit-43`

**Summary:** A retired but valid finite audit expands the six quotient shapes into 43 physical labelled forests, at most 172 ordered rail pairs, with every seam test localized to twelve coordinates.

R871/P947 is a valid abandoned audit, not a realizability theorem. In the monotone sigma=0 residue with c_X in {2,3}, assign the physical labels G_0,G_1,G_2 to the Q roles and G_3,G_4 to the X roles of the six R866 shapes. The complete labelled list is:

A (6): [G0 | G3-G1-G2-G4], [G0 | G4-G1-G2-G3], [G1 | G3-G0-G2-G4], [G1 | G4-G0-G2-G3], [G2 | G3-G0-G1-G4], [G2 | G4-G0-G1-G3].
B (4): [G0-G1-G3-G2 | G4], [G0-G1-G4-G2 | G3], [G0-G3-G1-G2 | G4], [G0-G4-G1-G2 | G3].
C (12): [G0-G1-G3 | G2-G4], [G0-G1-G4 | G2-G3], [G0-G2-G3 | G1-G4], [G0-G2-G4 | G1-G3], [G0-G3 | G1-G2-G4], [G0-G3 | G4-G1-G2], [G0-G4 | G1-G2-G3], [G0-G4 | G3-G1-G2], [G1-G3 | G4-G0-G2], [G1-G4 | G3-G0-G2], [G2-G3 | G4-G0-G1], [G2-G4 | G3-G0-G1].
D (3): [G0-G1 | G3-G2-G4], [G0-G2 | G3-G1-G4], [G1-G2 | G3-G0-G4].
E (12): [G0 | G1-G3-G2-G4], [G0 | G1-G4-G2-G3], [G0 | G3-G1-G4-G2], [G0 | G4-G1-G3-G2], [G0-G3-G1-G4 | G2], [G0-G3-G2-G4 | G1], [G0-G4-G1-G3 | G2], [G0-G4-G2-G3 | G1], [G1 | G3-G0-G4-G2], [G1 | G4-G0-G3-G2], [G2 | G3-G0-G4-G1], [G2 | G4-G0-G3-G1].
F (6): [G0-G3 | G1-G4-G2], [G0-G3-G1 | G2-G4], [G0-G3-G2 | G1-G4], [G0-G4 | G1-G3-G2], [G0-G4-G1 | G2-G3], [G0-G4-G2 | G1-G3].

Completeness is not a brute-force assertion. Shape A: choose the isolated Q in 3 ways and order the two X endpoints in 2, giving 6. B: choose the isolated X in 2 and the internal-X gap G0|G1 or G1|G2 in 2, giving 4. C: choose the Q on the two-block rail in 3, its X label in 2, and the endpoint side in 2, giving 12. D: choose the Q used in X-Q-X in 3; reversing that rail adds no unoriented configuration, giving 3. E: choose the isolated Q in 3, the internal X in 2, and the endpoint side in 2, giving 12. F: choose the internal X in 2 and the Q on the separate Q-X rail in 3, giving 6. Hence c_X=2 has 6+4+12+3=25 configurations and c_X=3 has 12+6=18, total 43.

R867 forces the internal order of every Q block. Only the two orientations of G_3 and the two of G_4 remain, so there are at most 43*4=172 ordered rail pairs. Every turn internal to a Q block is already a Q turn; only block-boundary seams need checking. These involve only q_0,q_1,q_3,q_4,q_{m-4},q_{m-3},q_{m-1},q_m,a,b,c,z. For m>=9 the twelve roles are distinct; m=6,7,8 only identify some of them. This proves the finite-locality certificate. It makes no claim that all 43 configurations occur.
