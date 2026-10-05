# The memory-lift graph Γ_n

## Metadata

- ID: lifted_geodesic_graph_and_one_change_orders_subsection_a
- Parent Section: lifted_geodesic_graph_and_one_change_orders
- Position: 1
- Row version: 4
- Development version: 4
- Composition version: 1
- Composition stale: False

## Cold composition

The staircase triangulation identifies spanning orders with cube geodesics, but the color at one step depends on three successive directions. Introduce a graph \(\Gamma_n\) that stores this two-step memory.

Its vertices are poles \(s,t\) and states
\[
(\sigma,S,u,v),
\]
where \(\sigma\in\{0,1\}\), \(u\ne v\), and \(S\subseteq V\setminus\{u,v\}\). Give the state rank \(|S|+1\), with \(r(s)=0\) and \(r(t)=n\). Join \(s\) to every \((\sigma,\varnothing,u,v)\); join
\[
(\sigma,S,u,v)\longrightarrow(\sigma,S\cup\{u\},v,w)
\]
whenever \(w\notin S\cup\{u,v\}\); and join every rank-\(n-1\) state to \(t\).

Color a source edge by \(\sigma\), an internal edge by \(h(u,v,w)\), and a terminal edge by \(1-\sigma\). The underlying graph depends only on \(n\).

## Development

The staircase triangulation identifies spanning orders with cube geodesics, but the color at one step depends on three successive directions. Introduce a graph \(\Gamma_n\) that stores this two-step memory.

Its vertices are poles \(s,t\) and states
\[
(\sigma,S,u,v),
\]
where \(\sigma\in\{0,1\}\), \(u\ne v\), and \(S\subseteq V\setminus\{u,v\}\). Give the state rank \(|S|+1\), with \(r(s)=0\) and \(r(t)=n\). Join \(s\) to every \((\sigma,\varnothing,u,v)\); join
\[
(\sigma,S,u,v)\longrightarrow(\sigma,S\cup\{u\},v,w)
\]
whenever \(w\notin S\cup\{u,v\}\); and join every rank-\(n-1\) state to \(t\).

Color a source edge by \(\sigma\), an internal edge by \(h(u,v,w)\), and a terminal edge by \(1-\sigma\). The underlying graph depends only on \(n\).
