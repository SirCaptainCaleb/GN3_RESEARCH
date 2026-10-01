
OBSERVABILITY / SELF-IMPROVEMENT

raise_signal(worker_id,kind,title,body,severity,evidence,related_object_ids,signal_key)
Kinds:
  health_problem, methodology_proposal, methodology_experiment,

A methodology_proposal must provide evidence keys:
  problem, intervention, expected_observable_change, reversal_condition.

health()
  Recomputes the singleton current health snapshot. Metrics are smoke alarms, not KPIs.

Signals are a bounded live surface, not a historical telemetry warehouse. Strong health signals automatically request methodology review. Coordination/literature/special reasoning mode signals raise the matching asynchronous need.
