
READS

Use linp.read(ids,content) for small exact reads.

Before opening large modules:
  linp.read_preview(ids)
returns statement/body sizes, math_version/object_version, and Markdown headings.

For one exact Markdown section:
  linp.read_section(id,heading,occurrence)
returns the exact section text plus math_version and a watch_hint suitable for staged read guards.

For paged reads:
- content=statement or body with consistency=math watches math_version.
- content=math serializes stable mathematical fields and watches math_version.
- content=full watches the full object version.

Open with linp.open_read_ex(...), then use read_page(...) or read_more(...). Every page revalidates the entire manifest.

Completed exact math/full reads create only tiny bounded expiring receipts; historical body content is not cached.

For staged publication, explicitly watch the math_version actually read with watch_stage_reads_v2 when it is not already inferred from staged operations.

Ordinary active claims and the active special reasoning mode mathematical session are both valid principals for exact paged reads.
