# The surviving low C-terminal rotation forces the next joint to top potential

## Statement

In the surviving one-low odd-central 0-1-1 state, let p=phi(v)=2q-3 and let the unique rank-q edge be
  e={x,v,C},
where x is the unique entrance, x∉V(P_v), and
  C=g_{q-2}∩g_{q-1}
is the sole P_v-contact of e.

Then the charged endpoint rotation along P_v forces
  phi(E)>=p,
where
  E=g_{q-1}∩g_q.

Consequently, if E is occupied by one of the rank-(q+1) high single contacts, E cannot be that high edge's entrance (whose potential would be q); it must be its opposite terminal.

## Body

Apply the certified charged endpoint rotation 2e04b9ddaeaf to e at terminal v and the chosen maximum
  P_v=(g_1,...,g_p).
The opposite terminal C first occurs on g_{q-2}, so j=q-2. The rotated path is
  g_1,...,g_{q-2}, e, g_p,g_{p-1},...,g_q.
It has p edges. The rotation theorem identifies a last vertex
  w=g_{j+1}∩g_{j+2}=g_{q-1}∩g_q=E,
and therefore
  phi(E)>=p=2q-3.

If a rank-(q+1) high edge uses E as its sole P_v-contact and E were its unique entrance, ascendingness would give
  phi(E)=q.
For q>=4,
  q<2q-3,
contradicting the preceding lower bound. Hence any occupied E-slot is necessarily terminal-only in this surviving state.
