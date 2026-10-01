# Every terminal-retained switcher yields a source-terminal lens or a two-terminal overlap

## Statement

Let e={x,v,u} be an ascending nonspecial edge with unique entrance x. Let P_v be a maximum endpoint path ending physically at v such that u lies on P_v and x does not. Let P_u and P_x be arbitrary maximum endpoint paths ending physically at u and x. Then P_v and P_u contain a balanced elementary endpoint lens attached at u. Moreover at least one of the following holds: (X) x lies on P_u, in which case P_u and P_x contain a balanced elementary endpoint lens attached at x; (V) v lies on P_u, in which case P_u and P_v contain a balanced elementary endpoint lens attached at v. Thus every terminal-retained switching state carries, in addition to its host attachment at u, either a source-terminal lens certificate or reciprocal terminal-terminal overlap through both terminal labels.

## Body

Because u is a vertex of the maximum path P_v distinct from its physical endpoint v, apply b35b0fd4e4cd with Q=P_v, y=u and P=P_u. It gives a clean balanced elementary endpoint lens between P_v and P_u attached at u. Next apply the reciprocal two-point transversal theorem 8f040f62964a to the ascending edge e at terminal u. Every maximum u-ending path contains x or v, so P_u contains at least one of these vertices. If x lies on P_u, apply b35b0fd4e4cd with Q=P_u, y=x and P=P_x to obtain a balanced elementary endpoint lens attached at x. If v lies on P_u, apply b35b0fd4e4cd with Q=P_u, y=v and P=P_v to obtain one attached at v. If both x and v lie on P_u, both conclusions hold. No gap-one, charging, source-clean, or terminal-single hypothesis is required beyond the terminal-retained condition u in V(P_v), x notin V(P_v).
