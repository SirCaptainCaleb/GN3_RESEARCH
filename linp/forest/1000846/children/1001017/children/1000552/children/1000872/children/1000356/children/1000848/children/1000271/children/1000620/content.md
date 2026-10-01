# The clean-minus-double defect is bounded by the number of 0-1-1 ascending edges

## Statement

Choose maximum endpoint paths P_v and let C,D be the clean- and double-incidence counts of the contact-snake identity. Let N_011 be the number of ascending nonspecial edges e={x,u,v} whose contact signature on the three chosen endpoint paths is
   (mu_x(e),mu_u(e),mu_v(e))=(0,1,1),
where x is the unique entrance.

Then
   C-D <= N_011.

Consequently, if
   N_011 <= (3/4) sum_v phi(v),
then
   m <= (11/12) sum_v phi(v)-n/3,
and every P_ell-free linear triple system satisfies
   m <= ((11ell-15)/12)n.

## Body

By the clean-incidence characterization in 4e165e65be58, every incidence counted by C is the unique entrance incidence of an ascending nonspecial edge. Thus each clean incidence belongs to a unique source-clean ascending edge, and each such edge contributes exactly one unit to C.

For a source-clean ascending edge e={x,u,v}, its two terminal incidences cannot be clean entrance incidences. Their contact multiplicities are therefore 1 or 2. Let k(e) be the number of its two terminal incidences having multiplicity 2. The contribution of e to C-D, before counting any doubles belonging to non-source-clean edges, is
   1-k(e).
Hence:
- signature 0-1-1 contributes 1;
- signatures 0-1-2 or 0-2-1 contribute 0;
- signature 0-2-2 contributes -1.

Double incidences belonging to edges with nonclean source only subtract further from C-D. Summing gives
   C-D <= N_011.

Now combine this with
   3m-C+D <= 2S-n,
where S=sum_v phi(v). If N_011<=3S/4, then
   3m <= 2S-n +(C-D)
      <= 2S-n +N_011
      <= (11/4)S-n.
Thus
   m <= (11/12)S-n/3.
For P_ell-free H, S<=(ell-1)n, yielding
   m <= ((11ell-15)/12)n.