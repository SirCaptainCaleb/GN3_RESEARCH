# Both-prefix reciprocal terminals force a unique rail gate into the late half

## Statement

Let
  e_i={x_i,v,u_i}, e_j={x_j,v,u_j}
be distinct source-clean ascending nonspecial edges through the common terminal v, with canonical maximum source rails
  Q_i=(a_1,...,a_m), Q_j=(b_1,...,b_n)
ending at x_i,x_j, where m=phi(x_i)=phi(e_i)-1 and n=phi(x_j)=phi(e_j)-1.

Assume:
(1) V(Q_i)∩V(Q_j)={y}, and y is the aligned joint
    y=a_t∩a_{t+1}=b_t∩b_{t+1};
(2) the foreign-edge contacts are reciprocal-terminal:
    Q_i∩e_j={u_j}, Q_j∩e_i={u_i};
(3) both u_j on Q_i and u_i on Q_j occur strictly on the prefix side of y.

Then
  2t >= m+1
and
  2t >= n+1.
Equivalently
  t >= ceil((max{m,n}+1)/2).

Consequently, for a uniquely intersecting pair of source-clean U_11 edges in the consecutive-rank setting, if the aligned gate lies earlier than ceil((max{m,n}+1)/2), at least one of the two forced reciprocal terminal contacts must lie on the suffix side of the gate.

## Body

By the reciprocal-terminal hypotheses, e_j meets Q_i only at u_j and e_i meets Q_j only at u_i. Since both reciprocal terminals lie strictly before y, the suffixes
  Q_i[y,x_i] and Q_j[y,x_j]
avoid u_j and u_i respectively. The unique rail-intersection assumption says their interiors are disjoint and they meet only at y.

Therefore the cyclic sequence
  Q_i[y,x_i], e_i, e_j, reverse(Q_j[y,x_j])
is a linear cycle. Indeed Q_i attaches to e_i only at x_i; e_i and e_j meet only at v by linearity; e_j attaches to Q_j only at x_j; and the two rail suffixes close only at y. The potentially dangerous reciprocal contacts u_i,u_j lie in the omitted prefixes by assumption.

The two rail suffixes have lengths m-t and n-t. Hence the cycle has length
  c=(m-t)+1+1+(n-t)
   =m+n-2t+2.                                        (1)

Both e_i and e_j are nonspecial. By the cycle-rank theorem f2925a904b8e, every nonspecial edge on a linear c-cycle has rank at least c. Since
  phi(e_i)=m+1, phi(e_j)=n+1,
we obtain
  m+1 >= m+n-2t+2,
  n+1 >= m+n-2t+2.
Rearranging gives
  2t>=n+1
and
  2t>=m+1,
as claimed.

In the source-clean U_11 consecutive-rank setting, a uniquely intersecting source-rail pair has reciprocal-terminal contacts by 5570b54b0046, while the unique intersection is aligned by the maximum-path alignment lemmas. Thus the final consequence applies automatically.
