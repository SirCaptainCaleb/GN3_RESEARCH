-- Reviewed NORI coordination retirement (October 2026).
-- All substantive mathematical findings have been summarized in nori.nodes('overview') v5;
-- original mathematical Items, Articles, compositions, dependencies, events and audit history remain intact.
-- The coordination tables contain no active task claims, no attempt reports, and one completed review.
-- This deliberately preserves research_core status, changes, session, version checks, staged-batch publication,
-- artifact latest revision and monotone artifact-publisher protections.
-- Prerequisite: restore nori.boot/status to research_core and remove mirror_context coordination caller.
BEGIN;
DROP FUNCTION IF EXISTS nori.coordination_checkpoint(p_session text, p_task_id bigint, p_checkpoint jsonb, p_lease_minutes integer);
DROP FUNCTION IF EXISTS nori.coordination_checkpoint_obligation(p_session text, p_task_id bigint, p_details jsonb, p_reviewed_update_ids bigint[], p_lease_minutes integer);
DROP FUNCTION IF EXISTS nori.coordination_claim(p_session text, p_objective_id text, p_target_key text, p_question text, p_method text, p_decision_enabled text, p_role text, p_selection jsonb, p_lease_minutes integer);
DROP FUNCTION IF EXISTS nori.coordination_claim_obligation(p_session text, p_obligation_id text, p_question text, p_method text, p_consequence text, p_role text, p_selection jsonb, p_lease_minutes integer);
DROP FUNCTION IF EXISTS nori.coordination_commit_batch_update(p_session text, p_batch_id text, p_overlap_checked boolean, p_kind text, p_objective_ids text[], p_item_versions jsonb, p_discovery text, p_implication text, p_priority_change text, p_evidence jsonb, p_reopening_condition text);
DROP FUNCTION IF EXISTS nori.coordination_decide_objective(p_session text, p_objective_id text, p_state text, p_truth_status text, p_reason text, p_reopening_condition text);
DROP FUNCTION IF EXISTS nori.coordination_decide_versioned(p_session text, p_objective_id text, p_expected_revision integer, p_state text, p_truth_status text, p_reason text, p_reopening_condition text);
DROP FUNCTION IF EXISTS nori.coordination_finish(p_session text, p_task_id bigint, p_outcome jsonb, p_decision text);
DROP FUNCTION IF EXISTS nori.coordination_finish_obligation(p_session text, p_task_id bigint, p_outcome jsonb, p_decision text);
DROP FUNCTION IF EXISTS nori.coordination_metrics();
DROP FUNCTION IF EXISTS nori.coordination_obligation_history(p_obligation text);
DROP FUNCTION IF EXISTS nori.coordination_prioritize(p_session text, p_objective_id text, p_expected_revision integer, p_priority_rank integer, p_assessment jsonb, p_selection_rationale text);
DROP FUNCTION IF EXISTS nori.coordination_propose_objective(p_session text, p_id text, p_payload jsonb);
DROP FUNCTION IF EXISTS nori.coordination_propose_obligation(p_session text, p_id text, p_payload jsonb);
DROP FUNCTION IF EXISTS nori.coordination_publish_update(p_session text, p_kind text, p_objectives text[], p_items jsonb, p_discovery text, p_implication text, p_priority_change text, p_evidence jsonb, p_reopening_condition text);
DROP FUNCTION IF EXISTS nori.coordination_record_baseline(p_session text, p_snapshot bigint);
DROP FUNCTION IF EXISTS nori.coordination_review_claim(p_session text);
DROP FUNCTION IF EXISTS nori.coordination_review_finish(p_session text, p_review_id bigint, p_report jsonb);
DROP FUNCTION IF EXISTS nori.coordination_review_state();
DROP FUNCTION IF EXISTS nori.coordination_strategy();
DROP TABLE IF EXISTS nori.coordination_attempts;
DROP TABLE IF EXISTS nori.coordination_reviews;
DROP TABLE IF EXISTS nori.coordination_review_config;
DROP TABLE IF EXISTS nori.coordination_tasks;
DROP TABLE IF EXISTS nori.coordination_obligations;
DROP TABLE IF EXISTS nori.coordination_baselines;
DROP TABLE IF EXISTS nori.coordination_relationships;
DROP TABLE IF EXISTS nori.coordination_landscape;
DROP TABLE IF EXISTS nori.coordination_updates;
DROP TABLE IF EXISTS nori.coordination_objectives;
DROP FUNCTION IF EXISTS nori.coordination_change_event();
COMMIT;
