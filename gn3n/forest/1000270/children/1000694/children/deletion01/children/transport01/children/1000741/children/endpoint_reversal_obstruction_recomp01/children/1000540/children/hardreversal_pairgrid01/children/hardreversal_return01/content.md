# The unresolved endpoint-reversal residue returns to the bounded four-vertex classification

## Statement

Continue the setting of hardreversal_pairgrid01. Then H contains one of the bounded four-vertex configurations from 2bbbc5a88109: a Hamiltonian four-set, the exceptional cyclic non-Hamiltonian four-set, or an edge-orderable non-Hamiltonian matching-block four-set with its forced complete reverse fan. Consequently the universal hard endpoint-reversal residue of adecd58bef3d cannot remain outside the bounded four-vertex frontier.

## Body

Choose distinct outside vertices y,z,w as in hardreversal_pairgrid01 with y->z and z->w in the tournament defined by a->b iff (a,p_m,b) is tight. Then a71e5571d6a2 supplies the tight Hamilton paths R=(y,p_m,z,p_0) and S=(z,p_m,w,p_0). The initial displayed edge of S is (z,p_m). The first consecutive triple of R is (y,p_m,z), which is tight and reverses that initial edge in exactly the orientation classified by 2bbbc5a88109: with S written as (s_0,s_1,s_2,s_3)=(z,p_m,w,p_0), the reversing triple is (y,s_1,s_0). Applying 2bbbc5a88109 to S and pivot y gives the four-set {y,z,p_m,w}, which is either Hamiltonian, exceptional cyclic non-Hamiltonian, or edge-orderable non-Hamiltonian matching-block with the corresponding complete reverse fan. Thus the supposedly unresolved endpoint-reversal branch returns after one transport step to the same bounded four-vertex classification. No path reversal or cyclic permutation is used.