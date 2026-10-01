# Uphill 0-1-1 edges are repeated-intersection or aligned X-X

## Statement

Let e={x,v,u} be an ascending nonspecial edge of rank q with unique entrance x and terminals v,u. Assume
  q<phi(v)=p<phi(u)=s.
Let P_v and P_u be chosen maximum endpoint paths ending at v and u, respectively, and assume e is terminal-single on both paths.

On P_v, exactly one of {x,u} occurs off v; call the lower-terminal contact type X if x occurs and U if u occurs.
On P_u, exactly one of {x,v} occurs off u; call the higher-terminal contact type X if x occurs and V if v occurs.

Then:

(1) If the type is U-X, U-V, or X-V, the two maximum paths P_v and P_u have at least two common vertices.

(2) The only type for which P_v and P_u can have a unique common vertex is X-X. In that case, if
  V(P_v) intersect V(P_u)={x},
then x is a joint on both paths at the same path index.

Thus every uphill strict-gap doubly-terminal-single edge either carries an explicit repeated-intersection certificate between its two terminal maximum paths, or is in the rigid X-X aligned-joint state.

## Body

Because q<p and q<s, the edge e cannot be the last edge of either chosen maximum terminal path. Hence terminal-singleness says exactly one of the two non-endpoint vertices of e occurs on the precursor, and linearity prevents the other from appearing only in the last path edge.

Suppose first that P_v has type U. Then u belongs to P_v, while u is the last vertex of P_u. Hence P_v and P_u share u. If u were their unique common vertex, the certified unique-intersection theorem 5854d853a44b would force u to be an internal joint of P_u, contradicting that u is its last vertex. Therefore P_v and P_u have at least two common vertices. This proves both U-X and U-V.

Now suppose P_u has type V. Then v belongs to P_u, while v is the last vertex of P_v. The same argument with v in place of u shows that P_v and P_u cannot intersect only at v. Hence they have at least two common vertices. This proves X-V as well.

The only remaining signature is X-X. Then both paths contain x. They may have additional common vertices, in which case the repeated-intersection conclusion already holds. If x is their unique common vertex, apply 5854d853a44b directly to the two maximum endpoint paths P_v and P_u. It gives an index t with
  x = g_t intersect g_{t+1} = h_t intersect h_{t+1},
where P_v=(g_1,...,g_p) and P_u=(h_1,...,h_s). Thus x is an aligned joint at the same index on both paths.

No selected-cell, common-anchor, source-clean, or near-extremal hypothesis is used.
