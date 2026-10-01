
SIMPLIFIED SUBTREE

simplified_subtree(root_id,max_depth=null)

Purpose
Show a compact indented view of a reasoning subtree using each node's id and simplified_statement instead of full statement/body text.

Parameters
- root_id: object at the root of the view.
- max_depth: maximum relative depth below root. Omit or pass NULL to use configuration key subtree.simplified_default_depth (currently 5). Values are capped by subtree.max_depth.

Output
- tree: newline-delimited indented text.
- max_depth: effective depth used.
- node_count: rendered real nodes.
- truncated: true iff at least one displayed branch continues below the depth limit.
- marker: present only when truncated, with legend "... = deeper descendants omitted".
- repository_revision: project revision observed.

Rendering
Each real node is shown as:
  • [object_id] simplified statement

If simplified_statement is blank, the title is shown in angle brackets as a fallback.

When a displayed node at max_depth has deeper children, one indented child line is added:
  …

That marker means only that deeper descendants exist but were omitted by the depth limit. It is not a real object and does not mean the branch terminates.

Examples
  simplified_subtree('1000270')
    Use the configured default depth.

  simplified_subtree('1000270',2)
    Show root plus descendants through relative depth 2.

  simplified_subtree('1000270',0)
    Show only the root; if it has children, an indented … marker shows that the branch continues.

Use this for quick structural orientation. Use subtree(...) or targeted read/context RPCs when full object metadata or mathematical text is needed.
