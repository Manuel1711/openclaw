# Overnight Maintenance Log — ERC8004 Empirics

## 2026-03-10 23:22 CET (22:22 UTC)

- Scope executed:
  1. Re-checked reproducibility/consistency across empirics scripts, tables, figures, and summary PDFs.
  2. Re-ran all empirics pipelines (`step01`..`step04`) and rebuilt LaTeX PDFs (`STEP_01`, `STEP_02`, `STEP_04`).
  3. Verified file completeness and non-empty outputs for all expected empirics figures/reports.
  4. Applied targeted maintenance fixes to Step04 method/report consistency.

- Commands/pipelines run:
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `pdflatex` (2 passes each) on:
    - `STEP_01_empirics_reliability.tex`
    - `STEP_02_client_agent_flow.tex`
    - `STEP_04_identity_transfer.tex`

- Fixes/regression hardening applied:
  - **Step04 script** (`working/analysis/empirics/empirics_step04_identity_transfer.py`)
    - Added explicit metric `transfer_events_burn` to `identity_transfer_key_metrics.csv`.
    - Added guardrail check to fail fast if secondary transfer partition becomes invalid (`n_secondary < 0`).
  - **Step04 PDF report** (`working/results/empirics/summaries/STEP_04_identity_transfer.tex`)
    - Added burn-event definition and consistency identity `N_tot = N_mint + N_burn + N_secondary`.
    - Added explicit burn count in key results.
    - Strengthened figure explanations (Fig10–Fig14) with concise reading guidance.

- Repro/consistency checks passed:
  - All expected empirics PDFs/figures present and non-zero size.
  - Transfer accounting identity holds (including burn term).
  - Concentration-share ordering checks passed (`top1 <= top5 <= top10 <= 1`).

- Key Step04 refreshed metrics snapshot:
  - `transfer_events_total=37334`, `mint=28418`, `burn=0`, `secondary=8916`
  - `tokens_total=28418`, `tokens_with_secondary_transfer=7942` (27.95%)
  - `final_owner_hhi=0.007954`, `final_owner_gini_tokens=0.707622`
  - `transfer_burst_disappear_addresses=111`

- Blockers / warnings:
  - **Warning (non-blocking):** matplotlib emits `Unable to import Axes3D` during runs.
  - **Mitigation:** current empirics pipeline is 2D-only and completed successfully; keep warning monitored and, if desired, normalize environment to a single matplotlib install before any future 3D analysis.

- Outcome:
  - Maintenance cycle completed successfully.
  - Outputs regenerated in place, with non-destructive internal edits only.

## 2026-03-11 00:24 CET (23:24 UTC)

- Scope executed:
  1. Re-ran full empirics pipeline (`step01`..`step04`) to verify reproducibility end-to-end.
  2. Recompiled all empirics summary PDFs with 2-pass `pdflatex` (now including `STEP_03_temporal_dynamics.pdf`).
  3. Re-validated output completeness and core consistency identities on refreshed tables.
  4. Applied internal maintenance fixes for path portability + methodological-note clarity.

- Maintenance fixes applied:
  - **Reproducibility hardening (all empirics scripts)**
    - Updated `empirics_step01_reliability.py`, `empirics_step02_client_agent_flow.py`, `empirics_step03_temporal_dynamics.py`, `empirics_step04_identity_transfer.py`.
    - Replaced host-specific absolute `ROOT` with script-relative resolution via `Path(__file__).resolve().parents[3]`.
    - Effect: same scripts now run reproducibly from any clone location, avoiding path-coupled regressions.
  - **Methodological-note improvement (Step03)**
    - Enhanced `step03_temporal_dynamics.md` generation with explicit methodological notes (delay definition, binning, burst criteria, visualization trimming).
    - Added figure reading guide for Fig07/Fig08/Fig09.
  - **PDF coverage improvement (Step03)**
    - Added `working/results/empirics/summaries/STEP_03_temporal_dynamics.tex`.
    - Compiled and produced `STEP_03_temporal_dynamics.pdf` to close the prior PDF gap for Step03.

- Consistency checks passed:
  - All expected empirics figures (`fig01`..`fig14`) and summary PDFs (`STEP_01`..`STEP_04`) exist and are non-empty.
  - Step04 transfer identity holds: `transfer_events_total = mint + burn + secondary`.
  - Owner concentration shares ordering holds: `top1 <= top5 <= top10 <= 1`.
  - Step03 sanity bounds hold: observed-delay agents `<=` registered agents; burst clients `<=` total clients.

- Blockers / warnings:
  - **Warning (non-blocking):** matplotlib still reports `Unable to import Axes3D` (multi-install warning).
  - **Mitigation:** pipeline remains 2D-only and completed successfully; keep warning tracked, normalize matplotlib environment before any future 3D workflow.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Outputs regenerated in place; edits remained internal and non-destructive.

## 2026-03-11 01:22 CET (00:22 UTC)

- Scope executed:
  1. Re-checked full reproducibility by re-running `step01`..`step04` empirics scripts.
  2. Recompiled all summary TeX reports (`STEP_01`..`STEP_04`) to refresh dependent PDF outputs.
  3. Ran consistency sanity checks on refreshed tables/figures (presence, partition identities, concentration ordering).
  4. Applied targeted internal code/documentation maintenance where weak.

- Fixes/regressions handled:
  - **Step01 methodological/report improvement** (`empirics_step01_reliability.py`)
    - Expanded generated markdown with explicit methodological notes and figure-reading guide.
  - **Step04 methodological/report improvement** (`empirics_step04_identity_transfer.py`)
    - Expanded generated markdown with transfer-ordering assumptions, partition logic, overlap/correlation caveat, and detailed figure-reading guide.
  - **Step03 cleanup** (`empirics_step03_temporal_dynamics.py`)
    - Removed dead helper function (`q`) to reduce maintenance ambiguity and future regression risk.

- Consistency/repro checks passed:
  - All 14 empirics figure PDFs present and non-empty.
  - Core Step02 concentration shares are ordered consistently (`top1 <= top5 <= top10 <= 1`).
  - Step04 transfer partition identity holds (`total = mint + burn + secondary`).
  - All regenerated CSV tables are non-empty.

- Blockers / warnings:
  - **Warning (non-blocking):** matplotlib emits `Unable to import Axes3D` in this environment.
  - **Mitigation:** empirics pipeline is strictly 2D; run completed successfully. Keep warning tracked and normalize matplotlib installs before any future 3D analysis.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Outputs regenerated in place with non-destructive, internal-only edits.

## 2026-03-11 02:23 CET (01:23 UTC)

- Scope executed:
  1. Re-ran full empirics pipeline (`step01`..`step04`) and recompiled summary PDFs (`STEP_01`..`STEP_04`, 2-pass `pdflatex`).
  2. Re-validated reproducibility/consistency across all tables, figures, and PDFs (existence, non-empty outputs, metric identities, sanity bounds).
  3. Applied targeted maintenance improvement where documentation was weaker (Step02 methodological/figure guidance).

- Fixes/regressions handled:
  - **Step02 robustness + notes improvement** (`working/analysis/empirics/empirics_step02_client_agent_flow.py`)
    - Added concentration-order guardrail (`top1 <= top5 <= top10`) with explicit failure if violated.
    - Expanded generated `step02_client_agent_flow.md` with methodological notes and figure-reading guide (Fig03–Fig06).

- Consistency/repro checks passed:
  - All expected outputs present and non-empty: 14 empirics figure PDFs, all empirics CSV tables, and `STEP_01`..`STEP_04` summary PDFs.
  - Step04 transfer partition identity holds: `transfer_events_total = mint + burn + secondary`.
  - Step02 concentration ordering verified: `top1_client_feedback_share <= top5_clients_feedback_share <= top10_clients_feedback_share <= 1`.
  - Step03 sanity bounds hold: observed delay agents `<=` registered agents; burst-and-disappear clients `<=` total clients.

- Blockers / warnings:
  - **Warning (non-blocking):** matplotlib environment warning `Unable to import Axes3D` persists.
  - **Mitigation:** current empirics workflow is 2D-only and completed successfully; keep warning tracked, normalize matplotlib installation before any future 3D workloads.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Outputs regenerated in place with internal, non-destructive edits only.

## 2026-03-11 03:24 CET (02:24 UTC)

- Scope executed:
  1. Re-ran full empirics pipeline (`step01`..`step04`) and rebuilt all summary PDFs (`STEP_01`..`STEP_04`).
  2. Performed reproducibility re-check (pre/post hash diff) and consistency sanity checks on regenerated outputs.
  3. Applied targeted bug/regression fix for reproducible summary timestamps + strengthened weak figure-reading notes.

- Fixes/regressions handled:
  - **Reproducibility fix (all empirics scripts)**
    - Updated:
      - `working/analysis/empirics/empirics_step01_reliability.py`
      - `working/analysis/empirics/empirics_step02_client_agent_flow.py`
      - `working/analysis/empirics/empirics_step03_temporal_dynamics.py`
      - `working/analysis/empirics/empirics_step04_identity_transfer.py`
    - Added `reproducible_timestamp(...)` helper to anchor generated markdown timestamps to input-data mtime (`SOURCE_DATE_EPOCH` fallback), removing run-to-run wall-clock drift in `step0x_*.md` summaries.
  - **Method/report quality improvements**
    - Strengthened figure-reading guidance where weak:
      - Step02 (`Fig03`–`Fig06`) now includes interpretation caveats on concentration steepness and low-sample over-reads.
      - Step03 (`Fig07`–`Fig09`) now clarifies p99 visual trim semantics and lifecycle interpretation.
      - Step04 (`Fig11`) now explicitly distinguishes rapid relays vs long-hold right-tail behavior.

- Consistency checks passed:
  - 14/14 empirics figure PDFs present and non-empty.
  - Step02 concentration ordering valid: `top1 <= top5 <= top10 <= 1`.
  - Step04 transfer partition identity valid: `total = mint + burn + secondary`.
  - Step03 sanity bounds valid: observed-delay agents `<=` registered agents; burst clients `<=` total clients.

- Blockers / warnings:
  - **Blocker (partial reproducibility):** bitwise hashes for generated PDFs (matplotlib figures + pdflatex reports) still change run-to-run even with fixed `SOURCE_DATE_EPOCH`.
  - **Mitigation applied:** preserved numeric/data reproducibility via stable CSV + markdown metrics; documented PDF hash instability as metadata/object-order noise.
  - **Next mitigation (if strict byte-repro is required):** add deterministic post-processing step (e.g., qpdf/ghostscript normalization) and compare semantic invariants rather than raw PDF bytes.
  - **Warning (non-blocking):** matplotlib `Unable to import Axes3D` persists.
  - **Mitigation:** pipeline is 2D-only and completed successfully; keep warning tracked until environment normalization.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Outputs regenerated in place with internal, non-destructive edits only.

## 2026-03-11 04:21 CET (03:21 UTC)

- Scope executed:
  1. Re-ran empirics reproducibility cycle on `step01`..`step04` and rebuilt summary PDFs (`STEP_01`..`STEP_04`).
  2. Re-checked consistency across refreshed tables/figures/PDFs (existence, non-empty outputs, concentration ordering, transfer identity, temporal sanity bounds).
  3. Detected and fixed a regression-risk in Step03 temporal key-metrics naming used by downstream maintenance checks.

- Fixes/regressions handled:
  - **Step03 backward-compat metric alias added** (`working/analysis/empirics/empirics_step03_temporal_dynamics.py`)
    - Added `n_unique_clients_feedback` alongside `n_clients_total` in `temporal_dynamics_key_metrics.csv`.
    - Rationale: prior maintenance checks referenced `n_unique_clients_feedback`; this avoids false negatives while keeping current naming.

- Outputs regenerated in place (affected):
  - `working/results/empirics/tables/temporal_dynamics_key_metrics.csv`
  - `working/results/empirics/summaries/step03_temporal_dynamics.md`
  - `working/results/empirics/figures/fig07_first_feedback_delay_hist.pdf`
  - `working/results/empirics/figures/fig08_mean_feedback_curve_by_bins.pdf`
  - `working/results/empirics/figures/fig09_client_burst_disappear_map.pdf`
  - `working/results/empirics/summaries/STEP_03_temporal_dynamics.pdf`

- Consistency checks passed:
  - 14/14 empirics figure PDFs present and non-empty.
  - All empirics table CSVs present and non-empty.
  - Summary PDFs `STEP_01`..`STEP_04` present and non-empty.
  - Step02 concentration ordering valid: `top1 <= top5 <= top10 <= 1`.
  - Step04 transfer partition identity valid: `total = mint + burn + secondary`.
  - Step03 sanity bounds valid, with alias-aware client-count checks passing.

- Blockers / warnings:
  - **Warning (non-blocking):** matplotlib still emits `Unable to import Axes3D`.
  - **Mitigation:** workflow is strictly 2D and completed successfully; keep warning tracked and normalize matplotlib environment before any future 3D workloads.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits were internal, non-destructive, and outputs were regenerated in place.

## 2026-03-11 05:21 CET (04:21 UTC)

- Scope executed:
  1. Re-ran full empirics pipeline (`step01`..`step04`) and rebuilt summary PDFs (`STEP_01`..`STEP_04`, 2-pass `pdflatex`).
  2. Re-checked consistency/reproducibility of generated tables, figures, and PDFs (presence/non-empty + metric sanity identities).
  3. Detected and fixed a backward-compatibility regression risk in Step03 temporal metrics consumed by maintenance checks.

- Fixes/regressions handled:
  - **Step03 key-metrics compatibility hardening** (`working/analysis/empirics/empirics_step03_temporal_dynamics.py`)
    - Added explicit legacy aliases in `temporal_dynamics_key_metrics.csv`:
      - `n_agents_registered` (alias of `n_registered_agents`)
      - `n_agents_with_observed_first_feedback_delay` (alias of `n_agents_with_feedback_delay_observed`)
      - `n_clients_burst_disappear` (alias of `n_clients_burst_and_disappear`)
    - Preserved existing alias `n_unique_clients_feedback`.
    - Rationale: avoids false regression flags from downstream checks still pinned to older metric labels.

- Outputs regenerated in place (affected):
  - `working/results/empirics/tables/temporal_dynamics_key_metrics.csv`
  - `working/results/empirics/tables/agent_first_feedback_delay.csv`
  - `working/results/empirics/tables/feedback_curve_by_block_bins.csv`
  - `working/results/empirics/tables/client_burst_disappear_summary.csv`
  - `working/results/empirics/figures/fig07_first_feedback_delay_hist.pdf`
  - `working/results/empirics/figures/fig08_mean_feedback_curve_by_bins.pdf`
  - `working/results/empirics/figures/fig09_client_burst_disappear_map.pdf`
  - `working/results/empirics/summaries/step03_temporal_dynamics.md`
  - `working/results/empirics/summaries/STEP_03_temporal_dynamics.pdf`

- Consistency/repro checks passed:
  - 14/14 empirics figure PDFs present and non-empty.
  - Summary PDFs `STEP_01`..`STEP_04` present and non-empty.
  - All empirics table CSVs present and non-empty.
  - Step02 concentration ordering valid: `top1 <= top5 <= top10 <= 1`.
  - Step04 transfer partition identity valid: `transfer_events_total = mint + burn + secondary`.
  - Step03 sanity bounds valid under both legacy and current metric labels.

- Refreshed Step04 snapshot (unchanged vs prior run):
  - `transfer_events_total=37334`, `mint=28418`, `burn=0`, `secondary=8916`
  - `tokens_total=28418`, `tokens_with_secondary_transfer=7942` (27.95%)
  - `final_owner_hhi=0.007954`, `final_owner_gini_tokens=0.707622`
  - `transfer_burst_disappear_addresses=111`

- Blockers / warnings:
  - **Warning (non-blocking):** matplotlib still emits `Unable to import Axes3D`.
  - **Mitigation:** workflow is 2D-only and completed successfully; keep warning tracked and normalize matplotlib installation before future 3D workloads.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal/non-destructive and affected outputs were regenerated in place.

## 2026-03-11 06:21 CET (05:21 UTC)

- Scope executed:
  1. Re-ran full empirics pipeline (`step01`..`step04`) and rebuilt summary PDFs (`STEP_01`..`STEP_04`, 2-pass `pdflatex`).
  2. Re-checked consistency/reproducibility across all produced tables, figures, and PDFs.
  3. Improved weak explanatory sections in Step01 report figures (operational reading guide + caveats), then regenerated affected PDF.

- Commands/pipelines run:
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `pdflatex` (2 passes each) on `STEP_01`..`STEP_04` TeX reports
  - Additional targeted `pdflatex` rebuild for updated `STEP_01_empirics_reliability.tex`

- Fixes/regressions handled today:
  - **Step01 figure-explanation strengthening** (`working/results/empirics/summaries/STEP_01_empirics_reliability.tex`)
    - F1 now includes explicit three-step reading protocol (density core, low-sample outliers, high-coverage robustness comparison) plus log-scale caveat.
    - F2 now includes direct decision-use interpretation (why unfiltered top-k is risky under Low-tier dominance and why to gate on reliability/shrunk score).

- Consistency/repro checks passed:
  - Figure completeness: `fig01`..`fig14` present and non-empty.
  - Summary PDFs: `STEP_01`..`STEP_04` present and non-empty.
  - Step02 concentration ordering valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 sanity bounds valid via compatibility labels: `n_agents_with_observed_first_feedback_delay <= n_agents_registered` and `n_clients_burst_disappear <= n_unique_clients_feedback`.
  - Step04 transfer partition identity valid: `transfer_events_total = transfer_events_mint + transfer_events_burn + transfer_events_secondary`.

- Blockers / warnings:
  - **Warning (non-blocking):** matplotlib still emits `Unable to import Axes3D` (multi-install environment issue).
  - **Mitigation:** empirics workflow is strictly 2D and completed successfully; warning kept tracked for environment normalization before any future 3D analysis.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Outputs regenerated in place with internal, non-destructive edits only.

## 2026-03-11 07:22 CET (06:22 UTC)

- Scope executed:
  1. Re-ran full empirics reproducibility cycle (`step01`..`step04`) and rebuilt all summary PDFs (`STEP_01`..`STEP_04`, 2-pass `pdflatex`).
  2. Re-checked consistency across scripts/tables/figures/PDFs with explicit sanity checks on concentration ordering, temporal bounds, and transfer partition identity.
  3. Improved weak methodological/figure explanations in Step03 technical note and regenerated affected PDF output in place.

- Fixes/regressions handled:
  - **Step03 figure-reading improvements** (`working/results/empirics/summaries/STEP_03_temporal_dynamics.tex`)
    - Strengthened interpretive guidance for Fig07/Fig08/Fig09 (p99 trim semantics, aggregate-curve caveat, and non-causal interpretation of burst-disappear candidates).
    - Rebuilt `STEP_03_temporal_dynamics.pdf` after edits.

- Consistency/repro checks passed:
  - All empirics scripts completed (`DONE` on `step01`..`step04`).
  - Figures `fig01`..`fig14` present and non-empty.
  - Summary PDFs `STEP_01`..`STEP_04` present and non-empty.
  - Step02 ordering valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 sanity bounds valid: observed-delay agents `<=` registered agents; burst clients `<=` total clients.
  - Step04 partition identity valid: `transfer_events_total = mint + burn + secondary`.

- Blockers / warnings:
  - **Warning (non-blocking):** matplotlib still emits `Unable to import Axes3D` due to multi-install environment.
  - **Mitigation:** current empirics pipeline is 2D-only and completed successfully; keep warning tracked until matplotlib environment normalization.

- Outcome:
  - Maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs regenerated in place.

## 2026-03-11 23:20 CET (22:20 UTC)

- Scope executed:
  1. Re-ran full empirics pipeline `step00`..`step05` to verify reproducibility on current raw snapshot.
  2. Recompiled all empirics summary PDFs `STEP_00`..`STEP_05` (2-pass `pdflatex`) and validated PDF readability (`pdfinfo`).
  3. Re-checked outputs for consistency/completeness across tables, figures, markdown summaries, and PDFs.
  4. Patched weak methodological documentation for Step05 and aligned script docs.

- Fixes/regressions handled:
  - **Step05 robustness + reporting hardening** (`working/analysis/empirics/empirics_step05_owner_behavior.py`)
    - Added safe percentage helper in markdown generation to avoid divide-by-zero crash on edge-case empty samples.
    - Expanded generated `step05_owner_behavior.md` with methodological notes, figure-reading notes, and explicit output inventory.
  - **Documentation consistency fix** (`working/analysis/empirics/README.md`)
    - Added missing section for `empirics_step05_owner_behavior.py` (scope, inputs, outputs) to match maintenance rule.

- Outputs regenerated in place (affected):
  - Full regenerated artifacts from:
    - `working/analysis/empirics/empirics_step00_overview.py`
    - `working/analysis/empirics/empirics_step01_reliability.py`
    - `working/analysis/empirics/empirics_step02_client_agent_flow.py`
    - `working/analysis/empirics/empirics_step03_temporal_dynamics.py`
    - `working/analysis/empirics/empirics_step04_identity_transfer.py`
    - `working/analysis/empirics/empirics_step05_owner_behavior.py`
  - Rebuilt summary PDFs:
    - `working/results/empirics/summaries/STEP_00_empirics_overview.pdf`
    - `working/results/empirics/summaries/STEP_01_empirics_reliability.pdf`
    - `working/results/empirics/summaries/STEP_02_client_agent_flow.pdf`
    - `working/results/empirics/summaries/STEP_03_temporal_dynamics.pdf`
    - `working/results/empirics/summaries/STEP_04_identity_transfer.pdf`
    - `working/results/empirics/summaries/STEP_05_owner_behavior.pdf`

- Consistency/repro checks passed:
  - All empirics scripts executed successfully (`DONE`).
  - Figure PDFs and summary PDFs are present, non-empty, and readable.
  - No destructive operations performed; outputs regenerated in place only.

- Blockers / warnings:
  - **Warning (non-blocking):** matplotlib still emits `Unable to import Axes3D` (environment multi-install warning).
  - **Mitigation:** current empirics workflow is 2D-only and completed successfully; warning tracked for future environment normalization.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Internal non-destructive updates applied; Step05 methodology/report quality improved and all affected outputs regenerated.

## 2026-03-12 00:21 CET (23:21 UTC)

- Scope executed:
  1. Re-ran full empirics pipeline (`step00`..`step05`) to validate reproducibility on current raw snapshot.
  2. Recompiled all empirics summary PDFs (`STEP_00`..`STEP_05`, 2-pass `pdflatex`).
  3. Re-checked consistency/completeness across scripts, tables, figures, markdown summaries, and PDFs.
  4. Applied one internal documentation consistency fix where output inventory was stale.

- Commands/pipelines run:
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `pdflatex` (2 passes each) on `STEP_00`..`STEP_05` TeX reports

- Fixes/regressions handled:
  - **README consistency regression fix** (`working/analysis/empirics/README.md`)
    - Updated Step00 output inventory to include full generated artifacts (`fig00d`..`fig00f` and related tables), aligning docs with actual script outputs.

- Consistency/repro checks passed:
  - All empirics scripts completed successfully (`DONE`).
  - All expected empirics figures and all summary PDFs (`STEP_00`..`STEP_05`) exist and are non-empty.
  - All empirics CSV tables are non-empty.
  - Step02 ordering identity valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 sanity bounds valid: observed-delay agents `<=` registered agents; burst clients `<=` total clients.
  - Step04 transfer partition identity valid: `transfer_events_total = mint + burn + secondary`.

- Blockers / warnings:
  - **Warning (non-blocking):** matplotlib still emits `Unable to import Axes3D` (environment multi-install warning).
  - **Mitigation:** pipeline is strictly 2D and completed successfully; keep warning tracked and normalize matplotlib environment before any future 3D workflows.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits were internal and non-destructive; affected outputs regenerated in place.

## 2026-03-12 01:22 CET (00:22 UTC)

- Scope executed:
  1. Re-ran full empirics pipeline (`step00`..`step05`) to re-check reproducibility end-to-end.
  2. Recompiled all empirics summary PDFs (`STEP_00`..`STEP_05`, 2-pass `pdflatex`).
  3. Re-validated consistency across generated figures/tables/PDFs with explicit identity/sanity checks.
  4. Detected and fixed one Step05 regression-risk in key-metric naming compatibility used by maintenance checks.

- Commands/pipelines run:
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `pdflatex` (2 passes each) on `STEP_00`..`STEP_05` TeX reports

- Fixes/regressions handled:
  - **Step05 compatibility hardening** (`working/analysis/empirics/empirics_step05_owner_behavior.py`)
    - Added legacy alias metrics to `step05_owner_behavior_key_metrics.csv`:
      - `feedback_total`
      - `owner_to_own_count`
      - `owner_to_other_count`
      - `non_owner_count`
      - `owner_unknown_count`
    - Canonical `n_*` metrics were preserved.
    - Rationale: avoids false regression alarms in downstream checks expecting pre-standardized labels.

- Outputs regenerated in place (affected):
  - `working/results/empirics/tables/step05_owner_behavior_key_metrics.csv`
  - `working/results/empirics/tables/step05_owner_feedback_classification.csv`
  - `working/results/empirics/tables/step05_self_feedback_by_agent.csv`
  - `working/results/empirics/tables/step05_owner_behavior_by_address.csv`
  - `working/results/empirics/tables/step05_owner_feedback_time_bins_5000.csv`
  - `working/results/empirics/figures/fig05a_owner_feedback_composition.pdf`
  - `working/results/empirics/figures/fig05b_owner_feedback_temporal_composition.pdf`
  - `working/results/empirics/summaries/step05_owner_behavior.md`
  - `working/results/empirics/summaries/STEP_05_owner_behavior.pdf`

- Consistency/repro checks passed:
  - Figure PDFs: 26/26 present and non-empty.
  - Table CSVs: 36/36 present and non-empty.
  - Summary PDFs: 6/6 (`STEP_00`..`STEP_05`) present and non-empty.
  - Step02 ordering identity valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 sanity bounds valid: observed-delay agents `<=` registered agents; burst clients `<=` total clients.
  - Step04 transfer partition identity valid: `transfer_events_total = mint + burn + secondary`.
  - Step05 partition identity valid: total feedback equals sum of owner/non-owner classes.

- Refreshed Step05 snapshot:
  - `n_feedback_total=2782`
  - `n_owner_to_own_agent=0`
  - `n_owner_to_other_agent=79`
  - `n_nonowner_to_agent=2703`
  - `n_owner_unknown=0`

- Blockers / warnings:
  - **Blocker (resolved):** legacy Step05 checks expecting `feedback_total`/`owner_to_*_count` keys failed against canonical `n_*` keys.
  - **Mitigation applied:** added backward-compatible aliases while retaining canonical labels; compatibility checks now pass.
  - **Warning (non-blocking):** matplotlib still emits `Unable to import Axes3D` (multi-install warning).
  - **Mitigation:** empirics workflow is 2D-only and completed successfully; keep warning tracked until environment normalization.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs were regenerated in place.

## 2026-03-12 02:22 CET (01:22 UTC)

- Scope executed:
  1. Re-ran full empirics reproducibility cycle (`step00`..`step05`) and rebuilt summary PDFs (`STEP_00`..`STEP_05`, 2-pass `pdflatex`).
  2. Re-checked consistency/completeness across generated scripts outputs (tables, figures, markdown summaries, PDFs).
  3. Applied one internal maintenance improvement where methodological/figure guidance was still weaker (Step00 overview note quality).

- Commands/pipelines run:
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `pdflatex` (2 passes each) on `STEP_00`..`STEP_05` TeX reports

- Fixes/regressions handled:
  - **Step00 methodological + figure-explanation improvement** (`working/analysis/empirics/empirics_step00_overview.py`)
    - Expanded generated `step00_empirics_overview.md` with explicit **Methodological notes** (scaling, delay definition, concentration interpretation, log-scale caveat).
    - Added dedicated **Figure reading notes** for `Fig00a`..`Fig00f` to strengthen interpretation guidance.
    - Minor consistency correction: downstream reference updated from `Step01-04` to `Step01-05`.

- Outputs regenerated in place (affected):
  - Full refreshed artifacts from empirics scripts `step00`..`step05`.
  - Rebuilt summary PDFs `STEP_00`..`STEP_05`.
  - Directly updated summary artifact from fix:
    - `working/results/empirics/summaries/step00_empirics_overview.md`

- Consistency/repro checks passed:
  - Figure PDFs: `26/26` present and non-empty.
  - Table CSVs: `36/36` present and non-empty.
  - Summary PDFs: `6/6` (`STEP_00`..`STEP_05`) present and non-empty.
  - Step02 ordering identity valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 sanity bounds valid: observed-delay agents `<=` registered agents; burst clients `<=` total clients.
  - Step04 transfer partition identity valid: `transfer_events_total = mint + burn + secondary` (`37334 = 28418 + 0 + 8916`).
  - Step05 owner-class partition valid: `n_feedback_total = own + other + nonowner + unknown` (`2782 = 0 + 79 + 2703 + 0`).

- Blockers / warnings:
  - **Warning (non-blocking):** matplotlib still emits `Unable to import Axes3D` (multi-install environment warning).
  - **Mitigation:** workflow remains strictly 2D and completed successfully; warning tracked for environment normalization before any future 3D workloads.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs regenerated in place.

## 2026-03-12 03:20 CET (02:20 UTC)

- Scope executed:
  1. Re-ran full empirics reproducibility cycle (`step00`..`step05`) and refreshed summary PDFs (`STEP_00`..`STEP_05`, 2-pass `pdflatex`).
  2. Re-checked consistency/completeness across generated tables, figures, markdown summaries, and PDFs.
  3. Applied targeted internal maintenance improvement to Step05 figure-reading guidance where interpretation risk was weak.

- Commands/pipelines run:
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `pdflatex` (2 passes each) on `STEP_00`..`STEP_05` TeX reports
  - Targeted refresh: `python3 working/analysis/empirics/empirics_step05_owner_behavior.py` + `pdflatex` (2 passes) on `STEP_05_owner_behavior.tex`

- Fixes/regressions handled:
  - **Step05 methodological/figure-note hardening**
    - Updated `working/analysis/empirics/empirics_step05_owner_behavior.py` generated note for `fig05b` to explicitly state that peaks are on absolute counts and must be cross-checked against per-bin totals.
    - Updated `working/results/empirics/summaries/STEP_05_owner_behavior.tex` with the same caveat to reduce over-interpretation risk.
    - Minor cleanup: removed unused temporary variables in Step05 script (non-functional, maintenance hygiene).

- Consistency/repro checks passed:
  - Figure PDFs: `26/26` present and non-empty.
  - Table CSVs: `36/36` present and non-empty.
  - Summary PDFs: `6/6` (`STEP_00`..`STEP_05`) present and non-empty.
  - Step02 ordering identity valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 sanity bounds valid: observed-delay agents `<=` registered agents; burst clients `<=` total clients.
  - Step04 transfer partition identity valid: `transfer_events_total = mint + burn + secondary`.
  - Step05 partition identity valid: `n_feedback_total = own + other + nonowner + unknown`.

- Blockers / warnings:
  - **Warning (non-blocking):** matplotlib still emits `Unable to import Axes3D` (multi-install environment warning).
  - **Mitigation:** empirics workflow is 2D-only and completed successfully; keep warning tracked and normalize matplotlib environment before any future 3D workloads.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs regenerated in place.

## 2026-03-12 04:24 CET (03:24 UTC)

- Scope executed:
  1. Re-ran full empirics pipeline (`step00`..`step05`) to re-check reproducibility of scripts/tables/figures/summaries.
  2. Recompiled all summary TeX PDFs (`STEP_00`..`STEP_05`) and then recompiled `STEP_03` after targeted maintenance edits.
  3. Ran consistency checks on generated tables (non-empty files + key metric identities/sanity bounds).
  4. Applied one internal non-destructive maintenance fix to Step03 reporting consistency + strengthened weak figure/method notes.

- Fixes/regressions handled:
  - **Step03 temporal summary consistency fix** (`working/analysis/empirics/empirics_step03_temporal_dynamics.py`)
    - Split core metrics vs backward-compatible aliases.
    - Kept aliases in `temporal_dynamics_key_metrics.csv` for downstream compatibility, but removed duplicate alias lines from markdown summary to avoid ambiguity.
    - Added explicit reproducibility note (`SOURCE_DATE_EPOCH` behavior) and stronger Figure Reading Guide for Fig07/Fig08/Fig09.

- Outputs regenerated in place (affected):
  - `working/results/empirics/tables/temporal_dynamics_key_metrics.csv`
  - `working/results/empirics/tables/agent_first_feedback_delay.csv`
  - `working/results/empirics/tables/feedback_curve_by_block_bins.csv`
  - `working/results/empirics/tables/client_burst_disappear_summary.csv`
  - `working/results/empirics/tables/client_burst_disappear_red_table.csv`
  - `working/results/empirics/figures/fig07_first_feedback_delay_hist.pdf`
  - `working/results/empirics/figures/fig08_mean_feedback_curve_by_bins.pdf`
  - `working/results/empirics/figures/fig09_client_burst_disappear_map.pdf`
  - `working/results/empirics/summaries/step03_temporal_dynamics.md`
  - `working/results/empirics/summaries/STEP_03_temporal_dynamics.pdf`

- Consistency/repro checks passed:
  - All six empirics scripts executed successfully (`DONE`).
  - Summary PDFs `STEP_00`..`STEP_05` compile successfully.
  - `README.md` expected empirics output paths: all present (`57/57`).
  - Sanity identities/bounds verified:
    - Step02 concentration shares in `[0,1]`.
    - Step03 burst clients `<=` total clients.
    - Step04 transfer partition identity holds.
    - Step05 class shares sum to `1.0`.

- Blockers / warnings:
  - **Warning (non-blocking):** matplotlib still emits `Unable to import Axes3D` (multi-install environment warning).
  - **Mitigation:** empirics workflow remains strictly 2D and completed successfully; keep warning tracked and normalize matplotlib installation before future 3D workloads.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal, non-destructive, and outputs were regenerated in place.

## 2026-03-12 05:22 CET (04:22 UTC)

- Scope executed:
  1. Re-ran full empirics pipeline (`step00`..`step05`) to re-check script/table/figure reproducibility.
  2. Recompiled all summary PDFs (`STEP_00`..`STEP_05`, 2-pass `pdflatex`).
  3. Re-ran targeted Step01 regeneration after a methodological-note improvement.
  4. Re-validated completeness/consistency on expected outputs and key cross-step identities.

- Maintenance fix/improvement applied:
  - **Step01 methodological/figure-note strengthening** (`working/analysis/empirics/empirics_step01_reliability.py`)
    - Added explicit tier-share reporting (High/Medium/Low percentages) in generated `step01_empirics_reliability.md`.
    - Added comparison caveat: use tier shares (not only raw counts) when comparing datasets with different sample sizes.

- Outputs regenerated in place (affected):
  - Full refreshed artifacts from `step00`..`step05` scripts (tables, figures, markdown summaries).
  - Rebuilt summary PDFs: `STEP_00`..`STEP_05`.
  - Targeted refresh after Step01 note update:
    - `working/results/empirics/tables/agent_score_reliability.csv`
    - `working/results/empirics/figures/fig01_score_vs_coverage.pdf`
    - `working/results/empirics/figures/fig02_confidence_tiers_distribution.pdf`
    - `working/results/empirics/summaries/step01_empirics_reliability.md`
    - `working/results/empirics/summaries/STEP_01_empirics_reliability.pdf`

- Consistency/repro checks passed:
  - README-declared empirics outputs present/non-empty: `57/57`.
  - Step02 ordering identity valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 sanity bound valid: `n_clients_burst_and_disappear <= n_clients_total`.
  - Step04 transfer partition valid: `total = mint + burn + secondary`.
  - Step05 class partition valid: `n_feedback_total = own + other + nonowner + unknown`.

- Blockers / warnings:
  - **Warning (non-blocking):** matplotlib still emits `Unable to import Axes3D`.
  - **Mitigation:** current pipeline is strictly 2D and completed successfully; warning remains tracked for environment normalization before any future 3D workflows.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs regenerated in place.

### 2026-03-12 05:23 CET (04:23 UTC) — post-run patch

- Detected a minor formatting regression in `step01_empirics_reliability.md` (literal `\n` rendered in Tier-shares line).
- Fix applied in generator script (`empirics_step01_reliability.py`): corrected newline escaping.
- Regenerated affected outputs in place:
  - `tables/agent_score_reliability.csv`
  - `figures/fig01_score_vs_coverage.pdf`
  - `figures/fig02_confidence_tiers_distribution.pdf`
  - `summaries/step01_empirics_reliability.md`
  - `summaries/STEP_01_empirics_reliability.pdf`
- Outcome: regression resolved; no blocker.

## 2026-03-12 06:22 CET (05:22 UTC)

- Scope executed:
  1. Full reproducibility rerun of empirics generators (`step00`..`step05`).
  2. Full 2-pass TeX rebuild for `STEP_00`..`STEP_05` PDFs.
  3. Post-fix targeted refresh for Step04 (`empirics_step04_identity_transfer.py` + 2-pass `STEP_04_identity_transfer.tex`).
  4. Completeness and cross-step consistency checks on produced tables/figures/PDFs.

- Fixes/regressions handled:
  - **Step04 methodological-note hardening** (`working/analysis/empirics/empirics_step04_identity_transfer.py`)
    - Added explicit caveat in generated summary: burst-and-disappear labels are heuristic prioritization flags, not standalone causal evidence.
    - Strengthened Fig11 reading note: p99 trim is visualization-only; key percentile metrics are computed on full support.

- Outputs regenerated in place (affected):
  - `working/results/empirics/summaries/step04_identity_transfer.md`
  - `working/results/empirics/summaries/STEP_04_identity_transfer.pdf`
  - (Plus full rerun/rebuild artifacts from `step00`..`step05` and `STEP_00`..`STEP_05`.)

- Consistency/repro checks passed:
  - Figure PDFs present/non-empty: `26/26`.
  - Table CSVs present/non-empty: `36/36`.
  - Summary PDFs present/non-empty: `6/6`.
  - Step02 concentration ordering valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 sanity bound valid: `n_clients_burst_and_disappear <= n_clients_total`.
  - Step04 partition identity valid: `transfer_events_total = mint + burn + secondary`.
  - Step05 partition identity valid: `n_feedback_total = own + other + nonowner + unknown`.

- Blockers / warnings:
  - **Blocker (resolved during run):** initial maintenance validation assertions referenced legacy metric keys (`top1_share`, `n_feedback_owner_to_own`, etc.) not present in current outputs.
  - **Mitigation:** updated checks to use current metric names and alias-aware fallback, then re-ran validation successfully.
  - **Warning (non-blocking):** matplotlib `Unable to import Axes3D` persists.
  - **Mitigation:** workflow is strictly 2D; keep warning tracked for future environment normalization.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs were regenerated in place.

## 2026-03-12 07:20 CET (06:20 UTC)

- Scope executed:
  1. Re-ran full empirics reproducibility cycle (`step00`..`step05`) to re-check scripts/tables/figures/summaries coherence.
  2. Recompiled all summary PDFs (`STEP_00`..`STEP_05`, 2-pass `pdflatex`) and validated non-empty outputs.
  3. Re-checked cross-step consistency identities and sanity bounds on regenerated key tables.
  4. Detected and fixed one report-level inconsistency/regression in Step02 documentation scope.

- Commands/pipelines run:
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `pdflatex` (2 passes each) on `STEP_00`..`STEP_05` TeX reports
  - Targeted rebuild after fix: `pdflatex` (2 passes) on `STEP_02_client_agent_flow.tex`

- Fixes/regressions handled:
  - **Step02 summary/PDF scope consistency fix** (`working/results/empirics/summaries/STEP_02_client_agent_flow.tex`)
    - Previous `STEP_02` TeX content was temporally scoped (duplicating Step03 module) and inconsistent with current Step02 script outputs (`fig03`..`fig06`, concentration module).
    - Rewrote `STEP_02` report to align with actual Step02 methodology, metrics, figure references, and output inventory.
    - Strengthened methodological definitions and figure-reading caveats (especially top-client-share interpretation with low-sample caution).

- Outputs regenerated in place (affected):
  - Full refreshed artifacts from empirics scripts `step00`..`step05`.
  - Rebuilt summary PDFs `STEP_00`..`STEP_05`.
  - Directly updated and rebuilt:
    - `working/results/empirics/summaries/STEP_02_client_agent_flow.tex`
    - `working/results/empirics/summaries/STEP_02_client_agent_flow.pdf`

- Consistency/repro checks passed:
  - Figure PDFs present/non-empty: `26/26`.
  - Table CSVs present/non-empty: `36/36`.
  - Summary PDFs present/non-empty: `6/6`.
  - Step02 ordering identity valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 sanity bounds valid: observed-delay agents `<=` registered agents; burst clients `<=` total clients.
  - Step04 transfer partition valid: `transfer_events_total = mint + burn + secondary`.
  - Step05 owner-class partition valid: `n_feedback_total = own + other + nonowner + unknown`.

- Blockers / warnings:
  - **Blocker (resolved):** Step02 PDF scope regression (temporal module text instead of client-agent concentration module).
  - **Mitigation applied:** aligned Step02 TeX/PDF with canonical Step02 script outputs and rebuilt in place.
  - **Warning (non-blocking):** matplotlib still emits `Unable to import Axes3D` (multi-install environment warning).
  - **Mitigation:** current empirics workflow is 2D-only and completed successfully; warning remains tracked for future environment normalization.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs were regenerated in place.

## 2026-03-12 23:23 CET (22:23 UTC)

- Scope executed:
  1. Full reproducibility re-run of empirics pipeline (`step00`..`step06`).
  2. Consistency checks across regenerated tables/figures/summary PDFs (presence, non-empty, and key metric identities).
  3. Targeted maintenance updates on weak methodological/figure explanations.
  4. Regeneration of all impacted PDFs in place via 2-pass `pdflatex`.

- Commands run (core):
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex` (2 passes each) on `STEP_00`..`STEP_06` TeX summaries.

- Fixes / maintenance improvements applied:
  - **Documentation consistency fix:** added `empirics_step06_top_client_address.py` to `working/analysis/empirics/README.md` (scope/input/output now explicitly documented).
  - **Methodological-note strengthening (Step06 PDF):** improved figure-reading guidance in `STEP_06_top_client_address_profile.tex` for:
    - score-histogram interpretation jointly with `valueDecimals`;
    - temporal-bin interpretation caveat (5000-block aggregation vs point bursts).

- Repro/consistency checks passed:
  - All expected empirics figure PDFs present and non-empty (including Step06 figures).
  - All summary PDFs `STEP_00`..`STEP_06` present and non-empty after rebuild.
  - Step02 concentration ordering valid: `top1 <= top5 <= top10 <= 1`.
  - Step04 transfer identity valid: `transfer_events_total = mint + burn + secondary`.
  - Step03 sanity bounds valid: observed-delay agents `<=` registered agents; burst-disappear clients `<=` unique clients with feedback.

- Blockers / warnings:
  - **Warning (non-blocking):** matplotlib warning persists (`Unable to import Axes3D`).
  - **Mitigation:** pipeline is 2D-only and completed successfully; warning tracked in maintenance log, with environment normalization deferred to a dedicated dependency-cleanup pass.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs were regenerated in place.

## 2026-03-13 00:20 CET (23:20 UTC)

- Scope executed:
  1. Full reproducibility re-run of empirics pipeline (`step00`..`step06`) and full 2-pass rebuild of summary PDFs (`STEP_00`..`STEP_06`).
  2. Consistency checks across regenerated tables/figures/PDFs (presence, non-empty artifacts, and cross-step identities).
  3. Detection + fix of a Step06 reporting weakness (insufficient methodological/figure guidance in generated markdown summary).
  4. Regeneration in place of affected Step06 outputs after patch.

- Commands run (core):
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex` (2 passes each) on `STEP_00`..`STEP_06` TeX summaries.

- Fixes / maintenance improvements applied:
  - **Step06 methodological-note hardening** (`working/analysis/empirics/empirics_step06_top_client_address.py`)
    - Added reproducible UTC generation timestamp in `step06_top_client_address_profile.md` (anchored to input-data mtime / `SOURCE_DATE_EPOCH`).
    - Added explicit methodological notes (top-client definition, score scaling, out-of-range rule, 5000-block binning).
    - Added figure-reading guide for `Fig06a`..`Fig06d` with concentration and aggregation caveats.
    - Added robust percentage formatter to avoid divide-by-zero/NaN formatting regressions in edge-case runs.
    - Added explicit output inventory section for faster downstream audit.

- Outputs regenerated in place (affected):
  - `working/results/empirics/summaries/step06_top_client_address_profile.md`
  - `working/results/empirics/figures/fig06a_top_client_tag1_distribution.pdf`
  - `working/results/empirics/figures/fig06b_top_client_score_distribution.pdf`
  - `working/results/empirics/figures/fig06c_top_client_agent_concentration.pdf`
  - `working/results/empirics/figures/fig06d_top_client_timeline_bins5000.pdf`
  - `working/results/empirics/tables/step06_top_client_profile_metrics.csv`
  - `working/results/empirics/tables/step06_top_client_tag1_distribution.csv`
  - `working/results/empirics/tables/step06_top_client_tag2_distribution.csv`
  - `working/results/empirics/tables/step06_top_client_value_stats_by_tag1.csv`
  - `working/results/empirics/tables/step06_top_client_feedback_by_agent.csv`
  - `working/results/empirics/tables/step06_top_client_time_bins_5000.csv`
  - `working/results/empirics/tables/step06_top_client_score_out_of_range_rows.csv`
  - `working/results/empirics/summaries/STEP_06_top_client_address_profile.pdf`

- Repro/consistency checks passed:
  - Figure PDFs present/non-empty: `30/30`.
  - Table CSVs present/non-empty: `43/43`.
  - Summary PDFs present/non-empty: `7/7` (`STEP_00`..`STEP_06`).
  - Step02 concentration ordering valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 sanity bounds valid: observed-delay agents `<=` registered agents; burst clients `<=` unique clients with feedback.
  - Step04 transfer identity valid: `transfer_events_total = mint + burn + secondary`.
  - Step05 class partition valid: `n_feedback_total = own + other + nonowner + unknown`.

- Blockers / warnings:
  - **Warning (non-blocking):** matplotlib warning persists (`Unable to import Axes3D`).
  - **Mitigation:** workflow remains strictly 2D and completed successfully; warning tracked for later dependency-environment normalization.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs were regenerated in place.

## 2026-03-13 01:23 CET (00:23 UTC)

- Scope executed:
  1. Full reproducibility re-run of empirics scripts (`step00`..`step06`).
  2. Full summary PDF rebuild (`STEP_00`..`STEP_06`, 2-pass `pdflatex`).
  3. Consistency checks on regenerated artifacts (figures/tables/summary PDFs + cross-step identities).
  4. Regression detection/fix for Step04 key-metric naming compatibility.
  5. Regeneration in place of all affected outputs.

- Commands run (core):
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex` (2 passes each) on `STEP_00`..`STEP_06` from `working/results/empirics/summaries/`

- Fixes / maintenance improvements applied:
  - **Step04 backward-compat regression fix** (`working/analysis/empirics/empirics_step04_identity_transfer.py`)
    - Restored legacy alias metrics in `identity_transfer_key_metrics.csv` alongside canonical keys:
      - `n_mint_events`
      - `n_burn_events`
      - `n_secondary_transfer_events`
    - Purpose: preserve downstream checks that still reference legacy names while keeping canonical `transfer_events_*` metrics.

- Outputs regenerated in place (affected):
  - Full empirics artifacts refreshed via `step00`..`step06` scripts.
  - Summary PDFs refreshed: `STEP_00`..`STEP_06`.
  - Directly patched/regenerated Step04 artifacts:
    - `working/results/empirics/tables/identity_transfer_key_metrics.csv`
    - `working/results/empirics/tables/identity_transfer_token_lifecycle.csv`
    - `working/results/empirics/tables/identity_transfer_holding_deltas.csv`
    - `working/results/empirics/tables/identity_final_owner_distribution.csv`
    - `working/results/empirics/tables/identity_owner_feedback_link.csv`
    - `working/results/empirics/tables/identity_transfer_burst_disappear.csv`
    - `working/results/empirics/figures/fig10_token_secondary_transfer_hist.pdf`
    - `working/results/empirics/figures/fig11_transfer_holding_delta_hist.pdf`
    - `working/results/empirics/figures/fig12_final_owner_rank_size.pdf`
    - `working/results/empirics/figures/fig13_owner_feedback_link_scatter.pdf`
    - `working/results/empirics/figures/fig14_transfer_burst_disappear_map.pdf`
    - `working/results/empirics/summaries/step04_identity_transfer.md`
    - `working/results/empirics/summaries/STEP_04_identity_transfer.pdf`

- Repro/consistency checks passed:
  - Figure PDFs present/non-empty: `30/30`.
  - Table CSVs present/non-empty: `43/43`.
  - Summary PDFs present/non-empty: `7/7` (`STEP_00`..`STEP_06`).
  - Step02 concentration ordering valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 sanity bounds valid: observed-delay agents `<=` registered agents; burst clients `<=` clients with feedback.
  - Step04 transfer partition valid (including legacy aliases): `transfer_events_total = mint + burn + secondary`.
  - Step05 owner-class partition valid: `n_feedback_total = own + other + nonowner + unknown`.

- Blockers / warnings:
  - **Blocker (resolved):** initial PDF rebuild attempt from workspace root failed on relative figure paths (`../figures/...`) during `STEP_00` compile.
  - **Mitigation applied:** reran `pdflatex` from `working/results/empirics/summaries/` (where TeX relative paths are valid); full PDF rebuild completed.
  - **Warning (non-blocking):** matplotlib warning persists (`Unable to import Axes3D`).
  - **Mitigation:** empirics workflow remains 2D-only; warning tracked for later environment normalization.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs regenerated in place.

## 2026-03-13 02:22 CET (01:22 UTC)

- Scope executed:
  1. Re-ran full empirics pipeline (`step00`..`step06`) to re-check script/table/figure reproducibility.
  2. Rebuilt all summary PDFs (`STEP_00`..`STEP_06`, 2-pass `pdflatex`) and validated readability (`pdfinfo`).
  3. Re-ran consistency checks on regenerated outputs (presence/non-empty + cross-step identities/sanity bounds).
  4. Applied one internal maintenance fix to methodological framing consistency in Step00.

- Fixes/regressions handled:
  - **Step00 scope consistency fix** (`working/analysis/empirics/empirics_step00_overview.py`)
    - Updated downstream-reference text from `Step01-05` to `Step01-06` in generated overview note.
    - Regenerated affected artifacts in place:
      - `working/results/empirics/summaries/step00_empirics_overview.md`
      - `working/results/empirics/summaries/STEP_00_empirics_overview.pdf`

- Repro/consistency checks passed:
  - Figure PDFs present/non-empty: `30/30`.
  - Table CSVs present/non-empty: `43/43`.
  - Summary PDFs present/non-empty/readable: `7/7` (`STEP_00`..`STEP_06`).
  - Step02 concentration ordering valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 sanity bounds valid: observed-delay agents `<=` registered agents; burst clients `<=` total clients.
  - Step04 transfer identity valid: `transfer_events_total = mint + burn + secondary`.
  - Step05 owner-class partition valid: `n_feedback_total = own + other + nonowner + unknown`.

- Blockers / warnings:
  - **Warning (non-blocking):** matplotlib still emits `Unable to import Axes3D` across script runs.
  - **Mitigation:** pipeline is 2D-only and completed successfully; warning kept tracked for later environment normalization.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs were regenerated in place.

## 2026-03-13 03:23 CET (02:23 UTC)

- Scope executed:
  1. Full reproducibility re-run of empirics scripts (`step00`..`step06`).
  2. Full summary PDF rebuild (`STEP_00`..`STEP_06`, 2-pass `pdflatex`) + readability check (`pdfinfo`).
  3. Consistency validation across regenerated figures/tables/summaries and cross-step identities.
  4. Targeted methodological-note strengthening where weak in Step02, then in-place regeneration of affected outputs.

- Core commands run:
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex` (2 passes each) on `STEP_00`..`STEP_06` from `working/results/empirics/summaries/`
  - Targeted refresh after note update: `python3 .../empirics_step02_client_agent_flow.py` + 2-pass `STEP_02_client_agent_flow.tex`

- Fixes / maintenance improvements applied:
  - **Step02 methodological + figure-note hardening** (`working/analysis/empirics/empirics_step02_client_agent_flow.py`)
    - Added explicit caveat that `agent_rate_*` metrics are computed with uniform agent weighting and must be interpreted with volume columns.
    - Strengthened Fig06 reading note: in log-scale, small rank differences at the head can map to large absolute count gaps.

- Outputs regenerated in place (affected):
  - Full empirics outputs refreshed via `step00`..`step06`.
  - Summary PDFs refreshed: `STEP_00`..`STEP_06`.
  - Directly affected by targeted maintenance: `step02_client_agent_flow.md`, `STEP_02_client_agent_flow.pdf`, and Step02 tables/figures.

- Repro/consistency checks passed:
  - Figure PDFs present/non-empty: `30/30`.
  - Table CSVs present/non-empty: `43/43`.
  - Summary PDFs present/non-empty/readable: `7/7` (`STEP_00`..`STEP_06`).
  - Step02 concentration ordering valid: `top1_client_feedback_share <= top5_clients_feedback_share <= top10_clients_feedback_share <= 1`.
  - Step03 sanity bounds valid: observed-delay agents `<=` registered agents; burst clients `<=` unique clients with feedback.
  - Step04 transfer partition valid: `transfer_events_total = mint + burn + secondary`.
  - Step05 owner-class partition valid: `feedback_total = owner_to_own + owner_to_other + non_owner + owner_unknown`.
  - Step06 spot reproducibility check (hash-based) on key tables/summary: no diffs on immediate rerun.

- Blockers / warnings:
  - **Warning (non-blocking):** matplotlib warning persists (`Unable to import Axes3D`).
  - **Mitigation:** empirics pipeline remains 2D-only; outputs validated and run completed.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs regenerated in place.

## 2026-03-13 04:23 CET (03:23 UTC)

- Scope executed:
  1. Re-ran full empirics pipeline (`step00`..`step06`) for reproducibility/consistency re-check.
  2. Rebuilt all empirics summary PDFs (`STEP_00`..`STEP_06`, 2-pass `pdflatex`).
  3. Re-validated key artifact integrity (presence/non-empty + sanity checks on core metrics).
  4. Applied targeted internal maintenance improvement on Step06 methodological/figure guidance and deterministic ordering for tie cases.

- Fixes/regressions handled:
  - **Step06 deterministic tie-break + sorting stability fix** (`working/analysis/empirics/empirics_step06_top_client_address.py`)
    - Added deterministic tie-break for top-client selection (`n_feedback DESC`, `clientAddress ASC`).
    - Added deterministic secondary ordering for equal-count groupings (tag1/tag2/agent outputs).
    - Strengthened methodological note (explicit tie policy) and Fig06b reading guidance (histogram is in-range `[0,100]` only).

- Outputs regenerated in place:
  - Full `working/results/empirics/{tables,figures,summaries}` refresh via `step00`..`step06`.
  - Recompiled `STEP_00`..`STEP_06` PDFs.
  - Directly affected by targeted fix: `step06_top_client_address_profile.md`, Step06 tables/figures, `STEP_06_top_client_address_profile.pdf`.

- Blockers / warnings:
  - **Blocker (resolved):** initial combined rerun command failed during PDF phase due to relative log-path bug after `cd`.
  - **Mitigation:** reran PDF build with corrected pathing in `working/results/empirics/summaries/`; full build completed.
  - **Warning (non-blocking):** matplotlib `Axes3D` import warning persists.
  - **Mitigation:** pipeline uses only 2D plots; outputs validated and kept.

- Outcome:
  - Maintenance cycle completed successfully.
  - Edits remained internal/non-destructive; affected outputs regenerated in place.

## 2026-03-13 05:20 CET (04:20 UTC)

- Scope executed:
  1. Full reproducibility re-run of empirics scripts (`step00`..`step06`).
  2. Full summary PDF rebuild (`STEP_00`..`STEP_06`, 2-pass `pdflatex`) and readability check (`pdfinfo`).
  3. Consistency checks on regenerated tables/figures/PDFs (presence/non-empty + cross-step identities).
  4. Targeted methodological-note/figure-reading improvement on Step06 report, then in-place regeneration.

- Core commands run:
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex` (2 passes each) on `STEP_00`..`STEP_06` from `working/results/empirics/summaries/`
  - `pdfinfo` checks on all summary PDFs.

- Fixes / maintenance improvements applied:
  - **Regression fix (all empirics scripts):** hardened `reproducible_timestamp(...)` to handle malformed/empty `SOURCE_DATE_EPOCH` values safely.
    - Updated files:
      - `working/analysis/empirics/empirics_step00_overview.py`
      - `working/analysis/empirics/empirics_step01_reliability.py`
      - `working/analysis/empirics/empirics_step02_client_agent_flow.py`
      - `working/analysis/empirics/empirics_step03_temporal_dynamics.py`
      - `working/analysis/empirics/empirics_step04_identity_transfer.py`
      - `working/analysis/empirics/empirics_step05_owner_behavior.py`
      - `working/analysis/empirics/empirics_step06_top_client_address.py`
    - Effect: avoids `ValueError` crash when env var exists but is not a valid integer; falls back deterministically to input mtimes (or current UTC epoch if needed).
  - **Methodological/figure-note strengthening (Step06 PDF):**
    - Updated `working/results/empirics/summaries/STEP_06_top_client_address_profile.tex` with:
      - deterministic tie-break policy for top-client selection under equal counts;
      - explicit log-scale caveat for Fig06c (small visual gaps at head can map to large absolute-count gaps).

- Outputs regenerated in place:
  - Full refreshed artifacts from `step00`..`step06` (tables, figures, markdown summaries).
  - Rebuilt summary PDFs `STEP_00`..`STEP_06`.
  - Targeted rebuild after Step06 note update: `STEP_06_top_client_address_profile.pdf`.

- Repro/consistency checks passed:
  - Figure PDFs present/non-empty: `30/30`.
  - Table CSVs present/non-empty: `43/43`.
  - Summary PDFs present/non-empty/readable: `7/7` (`STEP_00`..`STEP_06`).
  - Step02 concentration ordering valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 sanity bounds valid: observed-delay agents `<=` registered agents; burst clients `<=` total clients.
  - Step04 transfer partition identity valid: `transfer_events_total = mint + burn + secondary`.
  - Step05 owner-class partition valid: `n_feedback_total = own + other + nonowner + unknown`.

- Blockers / warnings:
  - **Blocker (resolved):** first run failed in Step00 because `SOURCE_DATE_EPOCH` was present but empty, causing integer parse failure inside reproducible timestamp logic.
  - **Mitigation applied:** patched timestamp helper across all empirics scripts with robust parsing + deterministic fallback; rerun completed successfully.
  - **Warning (non-blocking):** matplotlib warning persists (`Unable to import Axes3D`).
  - **Mitigation:** pipeline remains 2D-only; outputs validated and accepted.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits were internal, non-destructive, and all affected outputs were regenerated in place.

## 2026-03-13 06:20 CET (05:20 UTC)

- Scope executed:
  1. Re-ran full empirics pipeline (`step00`..`step06`) to re-check reproducibility/consistency of scripts, tables, figures, and markdown outputs.
  2. Re-validated artifact integrity on all produced PDFs (figures + summary PDFs) via `pdfinfo`.
  3. Detected and fixed a reproducibility gap in figure-PDF byte stability.
  4. Strengthened methodological notes where weak and regenerated affected outputs in place.

- Fixes / maintenance improvements applied:
  - **Deterministic PDF export fix (all empirics scripts)**
    - Updated `empirics_step00_overview.py` .. `empirics_step06_top_client_address.py` to save figures with neutralized PDF metadata:
      - `metadata={'CreationDate': None, 'ModDate': None}`
    - Result: reruns on unchanged inputs now produce byte-identical figure PDFs (hash-stable).
  - **Methodological-note improvement (all steps)**
    - Added explicit reproducibility note in generated step summaries clarifying deterministic PDF-export policy.

- Repro/consistency checks passed:
  - Full script rerun completed successfully (`DONE` on `step00`..`step06`).
  - Determinism check: `changed_after_rerun = 0` across tracked empirics artifacts (`.csv`, `.md`, `.pdf`).
  - PDF integrity: `pdf_total=37`, `pdfinfo_failures=0`.

- Blockers / warnings:
  - **Warning (non-blocking):** matplotlib still emits `Unable to import Axes3D`.
  - **Mitigation:** pipeline is strictly 2D; outputs completed and validated successfully.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs were regenerated in place.

## 2026-03-13 07:21 CET (06:21 UTC)

- Scope executed:
  1. Re-ran full empirics reproducibility cycle (`step00`..`step06`) and rebuilt all summary PDFs (`STEP_00`..`STEP_06`, 2-pass `pdflatex`).
  2. Re-validated consistency/reproducibility across regenerated scripts/tables/figures/PDFs (presence, non-empty artifacts, and cross-step sanity identities).
  3. Detected and fixed a Step06 deterministic-ordering regression risk in one output table.
  4. Regenerated affected Step06 outputs in place after patch.

- Core commands run:
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex` (2 passes each) on `STEP_00`..`STEP_06` from `working/results/empirics/summaries/`
  - `pdfinfo` integrity check across all generated empirics PDFs.

- Fixes/regressions handled:
  - **Step06 deterministic ordering hardening** (`working/analysis/empirics/empirics_step06_top_client_address.py`)
    - In `step06_top_client_value_stats_by_tag1.csv`, changed sort from `n_feedback`-only to deterministic tie-break ordering:
      - `sort_values(['n_feedback', 'tag1_norm'], ascending=[False, True], kind='mergesort')`
    - Rationale: avoids tie-order drift in equal-frequency rows across reruns/platform differences.

- Outputs regenerated in place (affected by patch):
  - `working/results/empirics/tables/step06_top_client_value_stats_by_tag1.csv`
  - `working/results/empirics/tables/step06_top_client_profile_metrics.csv`
  - `working/results/empirics/tables/step06_top_client_tag1_distribution.csv`
  - `working/results/empirics/tables/step06_top_client_tag2_distribution.csv`
  - `working/results/empirics/tables/step06_top_client_feedback_by_agent.csv`
  - `working/results/empirics/tables/step06_top_client_time_bins_5000.csv`
  - `working/results/empirics/tables/step06_top_client_score_out_of_range_rows.csv`
  - `working/results/empirics/figures/fig06a_top_client_tag1_distribution.pdf`
  - `working/results/empirics/figures/fig06b_top_client_score_distribution.pdf`
  - `working/results/empirics/figures/fig06c_top_client_agent_concentration.pdf`
  - `working/results/empirics/figures/fig06d_top_client_timeline_bins5000.pdf`
  - `working/results/empirics/summaries/step06_top_client_address_profile.md`
  - `working/results/empirics/summaries/STEP_06_top_client_address_profile.pdf`

- Consistency/repro checks passed:
  - Figure PDFs present/non-empty: `30/30`.
  - Table CSVs present/non-empty: `43/43`.
  - Summary PDFs present/non-empty: `7/7` (`STEP_00`..`STEP_06`).
  - Step02 concentration ordering valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 sanity bounds valid: observed-delay agents `<=` registered agents; burst clients `<=` total clients.
  - Step04 transfer partition identity valid: `transfer_events_total = mint + burn + secondary`.
  - Step05 owner-class partition valid: `n_feedback_total = own + other + nonowner + unknown`.

- Blockers / warnings:
  - **Warning (non-blocking):** matplotlib still emits `Unable to import Axes3D`.
  - **Mitigation:** workflow is 2D-only and completed successfully; warning tracked for future environment normalization.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs were regenerated in place.

## 2026-03-13 23:23 CET (22:23 UTC)

- Scope executed:
  1. Full reproducibility re-run of empirics pipeline (`step00`..`step06`).
  2. Full 2-pass rebuild of summary PDFs (`STEP_00`..`STEP_06`).
  3. Consistency checks across regenerated scripts outputs (tables, figures, PDFs) and key cross-step identities.
  4. Targeted improvement on weak methodological guidance in Step00 summary report.

- Commands run (core):
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex` (2 passes each) on `STEP_00`..`STEP_06` TeX summaries.

- Fixes / maintenance improvements applied:
  - **Step00 methodological consistency fix** (`working/results/empirics/summaries/STEP_00_empirics_overview.tex`)
    - Updated section scope from `Step 01--04` to `Step 01--06`.
    - Added explicit methodological implications for Step05 (owner/client time-aware classification) and Step06 (top-client deep-dive interpretation limits).
    - Rebuilt `STEP_00_empirics_overview.pdf` in place (2-pass `pdflatex`).

- Repro/consistency checks passed:
  - Figures present and non-empty: `30/30`.
  - Tables present and non-empty: `43/43`.
  - Summary PDFs present and non-empty: `7/7` (`STEP_00`..`STEP_06`).
  - Step02 ordering identity valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 sanity bounds valid (agents with observed delay `<=` registered agents; burst clients `<=` total clients).
  - Step04 transfer partition identity valid: `transfer_events_total = mint + burn + secondary`.
  - Step05 owner-class partition valid: `n_feedback_total = own + other + nonowner + unknown`.

- Blockers / warnings:
  - **Warning (non-blocking):** matplotlib still emits `Unable to import Axes3D`.
  - **Mitigation:** pipeline is strictly 2D and completed successfully; warning tracked for future environment normalization.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits were internal, non-destructive, and affected outputs were regenerated in place.

## 2026-03-14 00:21 CET (23:21 UTC)

- Scope executed:
  1. Full overnight reproducibility sweep on empirics pipeline (`step00`..`step06`).
  2. Consistency re-check across produced scripts/tables/figures/markdown/PDF summaries.
  3. Regression scan on core cross-step identities and output completeness.
  4. In-place regeneration of all affected artifacts (non-destructive, internal only).

- Commands/pipelines run:
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex` (2 passes each) on `STEP_00`..`STEP_06` TeX summaries.

- Maintenance findings/fixes:
  - No new blocking bugs/regressions detected in this cycle.
  - Methodological/figure-explanation quality check performed on regenerated summaries; no weak sections requiring patch were found beyond current baseline.

- Consistency/repro checks passed:
  - README-declared empirics outputs: `69/69` present and non-empty.
  - Artifact counts (non-empty): `30` figure PDFs, `43` table CSVs, `7` summary PDFs.
  - Step02 concentration ordering valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 sanity bounds valid: observed-delay agents `<=` registered agents; burst clients `<=` total clients.
  - Step04 transfer partition identity valid: `transfer_events_total = mint + burn + secondary`.
  - Step05 owner-class partition valid: `n_feedback_total = own + other + nonowner + unknown`.

- Blockers / warnings:
  - **Warning (non-blocking):** matplotlib still emits `Unable to import Axes3D` (multi-install environment warning).
  - **Mitigation:** empirics workflow remains strictly 2D and completed successfully; keep warning tracked, normalize matplotlib environment before any future 3D workflows.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Outputs regenerated in place; edits remained internal and non-destructive.

## 2026-03-14 01:22 CET (00:22 UTC)

- Scope executed:
  1. Re-ran full empirics reproducibility pipeline (`step00`..`step06`).
  2. Recompiled summary PDFs (`STEP_00`..`STEP_06`, 2-pass `pdflatex`).
  3. Re-checked consistency across generated scripts/tables/figures/PDFs and key cross-step identities.
  4. Regenerated affected outputs in place (internal, non-destructive).

- Commands/pipelines run:
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex` (2 passes each) on `STEP_00`..`STEP_06` TeX summaries.

- Maintenance findings/fixes:
  - No new blocking bugs/regressions detected in this cycle.
  - No additional methodological-note/figure-explanation patch required after review of regenerated summaries.

- Consistency/repro checks passed:
  - Artifact counts (non-empty): `30` figure PDFs, `43` table CSVs, `7` summary PDFs.
  - Step02 concentration ordering valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 sanity bounds valid: observed-delay agents `<=` registered agents; burst clients `<=` total clients.
  - Step04 transfer partition identity valid: `transfer_events_total = mint + burn + secondary` (`37334 = 28418 + 0 + 8916`).
  - Step05 owner-class partition valid: `n_feedback_total = own + other + nonowner + unknown` (`2782 = 0 + 79 + 2703 + 0`).

- Blockers / warnings:
  - **Warning (non-blocking):** matplotlib warning persists (`Unable to import Axes3D`).
  - **Mitigation:** current empirics workflow is strictly 2D and completed successfully; keep warning tracked and normalize matplotlib environment before any future 3D workloads.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Outputs regenerated in place; edits remained internal and non-destructive.

## 2026-03-14 02:22 CET (01:22 UTC)

- Scope executed:
  1. Re-ran full empirics reproducibility pipeline (`step00`..`step06`).
  2. Rebuilt all empirics summary PDFs (`STEP_00`..`STEP_06`, 2-pass `pdflatex`).
  3. Re-checked consistency/completeness across scripts, tables, figures, markdown summaries, and PDFs.
  4. Re-ran cross-step regression identities; regenerated outputs in place (internal, non-destructive).

- Commands run (core):
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex` (2 passes each) on `STEP_00`..`STEP_06` TeX summaries.

- Maintenance findings/fixes:
  - No new bugs/regressions detected in empirics scripts or generated artifacts during this cycle.
  - Methodological notes + figure reading notes re-checked on regenerated summaries; no weak sections requiring patch in this pass.

- Consistency/repro checks passed:
  - README-declared empirics outputs present/non-empty: `69/69`.
  - Artifact counts (non-empty): `30/30` figure PDFs, `43/43` table CSVs, `7/7` summary PDFs.
  - Step02 concentration ordering valid: `top1 <= top5 <= top10 <= 1` (`0.436736 <= 0.697340 <= 0.717469`).
  - Step03 sanity bounds valid: observed-delay agents `<=` registered agents; burst clients `<=` clients with feedback (`1470 <= 28418`, `2 <= 571`).
  - Step04 transfer partition identity valid: `transfer_events_total = mint + burn + secondary` (`37334 = 28418 + 0 + 8916`).
  - Step05 owner-class partition valid: `n_feedback_total = own + other + nonowner + unknown` (`2782 = 0 + 79 + 2703 + 0`).

- Blockers / warnings:
  - **Warning (non-blocking):** matplotlib warning persists (`Unable to import Axes3D`).
  - **Mitigation:** pipeline is 2D-only and completed successfully; keep environment normalization task tracked before any future 3D analysis.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Outputs regenerated in place; edits remained internal and non-destructive.

## 2026-03-14 03:22 CET (02:22 UTC)

- Scope executed:
  1. Full reproducibility/consistency rerun on empirics pipeline (`step00`..`step06`).
  2. Full 2-pass LaTeX rebuild for summary PDFs (`STEP_00`..`STEP_06`).
  3. Determinism check with pre/post SHA256 comparison across generated tables/figures/markdown summaries.
  4. Output-integrity checks (non-empty artifacts + CSV parse sanity).

- Commands run (core):
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex` (2 passes each) on `STEP_00_empirics_overview.tex` .. `STEP_06_top_client_address_profile.tex`

- Fixes / regressions handled today:
  - No source-code regression detected in empirics scripts during this cycle.
  - Regenerated all affected outputs in place (internal, non-destructive).
  - Methodological/figure-note quality in generated summaries remains aligned with latest hardened versions (no additional patch required this run).

- Repro/consistency checks passed:
  - Full rerun completed successfully (`ALL_EMPIRICS_STEPS_OK`).
  - Summary PDF rebuild completed successfully (`ALL_SUMMARY_PDFS_OK`).
  - Determinism check passed (`REPRODUCIBLE_OK`) on:
    - `working/results/empirics/tables/*.csv`
    - `working/results/empirics/figures/*.pdf`
    - `working/results/empirics/summaries/step*.md`
  - Integrity checks passed:
    - zero-byte artifact check: `ZERO_FILE_CHECK_OK`
    - CSV parse check: `CSV_PARSE_CHECK_OK`
  - Current artifact counts:
    - figure PDFs: `30`
    - table CSVs: `43`
    - summary PDFs: `7` (`STEP_00`..`STEP_06`)
    - summary markdown files: `8`

- Blockers / warnings:
  - **Blocker (resolved during run):** first PDF rebuild attempt failed due to an incorrect relative log path after `cd`.
  - **Mitigation applied:** corrected log path to local `.overnight_pdflatex.log`, reran full PDF rebuild successfully.
  - **Warning (non-blocking):** matplotlib warning persists: `Unable to import Axes3D`.
  - **Mitigation:** current empirics workflow is 2D-only and completed successfully; keep environment warning tracked for future dependency cleanup.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal/non-destructive; outputs regenerated in place.

## 2026-03-14 04:23 CET (03:23 UTC)

- Scope executed:
  1. Re-ran full empirics reproducibility cycle (`step00`..`step06`) to re-check scripts/tables/figures/summaries end-to-end.
  2. Rebuilt all empirics summary PDFs (`STEP_00`..`STEP_06`, 2-pass `pdflatex`).
  3. Re-validated consistency/completeness on regenerated outputs (non-empty artifacts + cross-step identities/sanity bounds).
  4. Detected and fixed a recurring maintenance warning regression in empirics runtime logs.

- Commands/pipelines run:
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex` (2 passes each) on `STEP_00`..`STEP_06` TeX summaries.

- Fixes/regressions handled:
  - **Empirics warning-noise regression fix (all step00..step06 scripts)**
    - Updated:
      - `working/analysis/empirics/empirics_step00_overview.py`
      - `working/analysis/empirics/empirics_step01_reliability.py`
      - `working/analysis/empirics/empirics_step02_client_agent_flow.py`
      - `working/analysis/empirics/empirics_step03_temporal_dynamics.py`
      - `working/analysis/empirics/empirics_step04_identity_transfer.py`
      - `working/analysis/empirics/empirics_step05_owner_behavior.py`
      - `working/analysis/empirics/empirics_step06_top_client_address.py`
    - Added targeted `warnings.filterwarnings(...)` to suppress the known non-actionable matplotlib `Unable to import Axes3D` warning in this 2D-only pipeline.
    - Outcome: maintenance logs are now clean (no repeated Axes3D warning spam), while computational outputs remain unchanged in scope.

- Consistency/repro checks passed:
  - Figure PDFs: `30/30` present and non-empty.
  - Table CSVs: `43/43` present and non-empty.
  - Summary PDFs: `7/7` (`STEP_00`..`STEP_06`) present and non-empty.
  - Step02 concentration ordering valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 sanity bounds valid: observed-delay agents `<=` registered agents; burst-disappear clients `<=` total clients.
  - Step04 transfer partition identity valid: `transfer_events_total = mint + burn + secondary`.
  - Step05 owner-class partition valid: `n_feedback_total = own + other + nonowner + unknown`.

- Blockers / warnings:
  - No blocking issues encountered in this cycle.
  - Prior non-blocking Axes3D warning regression was mitigated in-script (see fixes above).

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs regenerated in place.

## 2026-03-14 05:23 CET (04:23 UTC)

- Scope executed:
  1. Re-ran full empirics pipeline (`step00`..`step06`) and rebuilt summary PDFs (`STEP_00`..`STEP_06`, 2-pass `pdflatex`).
  2. Re-checked reproducibility by hashing all generated CSV + `step*.md` summaries before/after a second full script rerun.
  3. Re-validated consistency across regenerated outputs (figures/tables/PDF presence + key cross-step identities).
  4. Improved weak Step06 figure explanation caveats in the report and regenerated the affected PDF in place.

- Commands/pipelines run (core):
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex` (2 passes each) on `STEP_00`..`STEP_06` TeX summaries.

- Fixes/improvements applied:
  - **Step06 report caveat strengthening** (`working/results/empirics/summaries/STEP_06_top_client_address_profile.tex`)
    - Added explicit caveat that Step06 tag-share percentages are conditional on top-client activity only (not global ERC8004 tag shares).
    - Added explicit Fig06a reading caveat to avoid global-overgeneralization.
  - Regenerated affected output:
    - `working/results/empirics/summaries/STEP_06_top_client_address_profile.pdf`

- Repro/consistency checks passed:
  - Reproducibility check (CSV + markdown summaries): **NO_DIFF** after second full rerun.
  - Figures present/non-empty: `30/30`.
  - Tables present/non-empty: `43/43`.
  - Summary PDFs present/non-empty: `7/7`.
  - Step02 ordering valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 sanity bounds valid.
  - Step04 transfer partition identity valid: `total = mint + burn + secondary`.
  - Step05 owner-class partition identity valid: `n_feedback_total = own + other + nonowner + unknown`.

- Blockers / warnings:
  - No blocking issues encountered in this cycle.
  - Mitigation note: PDF byte-level reproducibility was not used as a strict gate (semantic/data reproducibility validated on CSV + markdown invariants).

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs regenerated in place.

## 2026-03-14 06:21 CET (05:21 UTC)

- Scope executed:
  1. Re-ran full empirics reproducibility cycle (`step00`..`step06`) to refresh scripts/tables/figures/markdown outputs in place.
  2. Recompiled all summary PDFs (`STEP_00`..`STEP_06`, 2-pass `pdflatex`).
  3. Re-checked consistency identities and output completeness/non-empty status.
  4. Applied one internal methodological-note improvement where interpretation risk was still weak (Step06 concentration inference caveat), then regenerated affected PDF.

- Commands run (core):
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex` (2 passes each) on `STEP_00`..`STEP_06` TeX summaries

- Fixes/improvements applied:
  - **Step06 figure/method caveat strengthening** (`working/results/empirics/summaries/STEP_06_top_client_address_profile.tex`)
    - Added explicit inferential caveat to avoid over-reading broad agent dispersion as standalone evidence against coordinated behavior.
    - Regenerated `STEP_06_top_client_address_profile.pdf` in place.

- Consistency/repro checks passed:
  - Figure PDFs present/non-empty: `30/30`.
  - Table CSVs present/non-empty: `43/43`.
  - Summary PDFs present/non-empty: `7/7` (`STEP_00`..`STEP_06`).
  - Step02 ordering valid: `top1 <= top5 <= top10 <= 1` (`0.436736 <= 0.697340 <= 0.717469`).
  - Step03 bounds valid: observed-delay agents `<=` registered agents (`1470 <= 28418`), burst-disappear clients `<=` clients with feedback (`2 <= 571`).
  - Step04 partition identity valid: `transfer_events_total = mint + burn + secondary` (`37334 = 28418 + 0 + 8916`).
  - Step05 partition identity valid: `n_feedback_total = own + other + nonowner + unknown` (`2782 = 0 + 79 + 2703 + 0`).

- Refreshed Step06 snapshot:
  - `top_client_address=0xf653068677a9a26d5911da8abd1500d043ec807e`
  - `n_feedback_top_client=1215`

- Blockers / warnings:
  - None blocking in this run.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal, non-destructive, and affected outputs were regenerated in place.

## 2026-03-14 07:20 CET (06:20 UTC)

- Scope executed:
  1. Re-ran full empirics reproducibility cycle (`step00`..`step06`) to re-check scripts/tables/figures/summaries on current raw snapshot.
  2. Rebuilt all summary PDFs (`STEP_00`..`STEP_06`, 2-pass `pdflatex`) and recompiled `STEP_05` after a targeted report-level fix.
  3. Re-validated consistency/completeness across generated outputs (non-empty artifacts + cross-step sanity/identity checks).
  4. Applied one internal methodological/reporting hardening fix where class definitions were weaker.

- Commands/pipelines run:
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex` (2 passes each) on `STEP_00`..`STEP_06` TeX summaries
  - Determinism check: pre/post hash compare for all empirics CSV tables + step markdown summaries on an immediate rerun

- Fixes/regressions handled:
  - **Step05 methodological/report consistency hardening** (`working/results/empirics/summaries/STEP_05_owner_behavior.tex`)
    - Added explicit guard class `owner_unknown` to the mutually exclusive class definition block.
    - Added explicit `owner_unknown` result line in key metrics section.
    - Updated interpretation paragraph to state current run has zero `owner_unknown` cases.
    - Rebuilt `STEP_05_owner_behavior.pdf` after patch.

- Repro/consistency checks passed:
  - Full empirics scripts completed successfully (`DONE` on `step00`..`step06`).
  - Figure PDFs present/non-empty: `30/30`.
  - Table CSVs present/non-empty: `43/43`.
  - Summary PDFs present/non-empty: `7/7` (`STEP_00`..`STEP_06`).
  - Determinism on immediate rerun: CSV hash diff `0`, markdown hash diff `0` (stable on unchanged inputs).
  - Step02 ordering identity valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 sanity bounds valid: observed-delay agents `<=` registered agents; burst-disappear clients `<=` total clients.
  - Step04 transfer partition identity valid: `transfer_events_total = mint + burn + secondary` (`37334 = 28418 + 0 + 8916`).
  - Step05 class partition identity valid: `n_feedback_total = own + other + nonowner + unknown` (`2782 = 0 + 79 + 2703 + 0`).

- Blockers / warnings:
  - **Blocker (resolved during run):** first PDF rebuild attempt used an incorrect log path after changing directory, aborting before compilation.
  - **Mitigation:** corrected log path to local summary directory and re-ran full `STEP_00`..`STEP_06` 2-pass builds successfully.
  - No new pipeline runtime blockers detected after rerun.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs were regenerated in place.

## 2026-03-14 23:25 CET (22:25 UTC)

- Scope executed:
  1. Re-ran full empirics pipeline (`step00`..`step06`) to re-check script-level reproducibility and output consistency.
  2. Rebuilt all summary PDFs (`STEP_00`..`STEP_06`, 2-pass `pdflatex`) and validated output completeness/non-empty artifacts.
  3. Performed reproducibility hash checks (pre/post) and cross-step sanity identity checks on regenerated tables.
  4. Applied targeted internal improvements to Step06 methodological and figure-reading notes, then regenerated affected outputs in place.

- Commands/pipelines run (core):
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex` (2 passes each) on `STEP_00`..`STEP_06` TeX summaries.

- Fixes/regressions handled:
  - **Step06 methodological + figure-note strengthening**
    - Updated `working/analysis/empirics/empirics_step06_top_client_address.py` generated markdown notes:
      - explicit snapshot-conditioning caveat for top-client identity;
      - stronger Fig06c interpretation caveat for low per-agent max-count regimes.
    - Updated `working/results/empirics/summaries/STEP_06_top_client_address_profile.tex` with matching caveats.

- Outputs regenerated in place (affected):
  - `working/results/empirics/summaries/step06_top_client_address_profile.md`
  - `working/results/empirics/summaries/STEP_06_top_client_address_profile.pdf`
  - Rebuilt full summary set: `STEP_00`..`STEP_06` PDFs.

- Consistency/repro checks passed:
  - Figure PDFs present/non-empty: `30/30`.
  - Table CSVs present/non-empty: `43/43`.
  - Summary PDFs present/non-empty: `7/7`.
  - Step02 ordering valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 bounds valid: observed-delay agents `<=` registered agents; burst-disappear clients `<=` total clients.
  - Step04 transfer partition valid: `transfer_events_total = mint + burn + secondary`.
  - Step05 owner-class partition valid: `n_feedback_total = own + other + nonowner + unknown`.

- Blockers / warnings:
  - **Blocker (resolved):** initial reproducibility hash check failed because `pdflatex` was executed from the wrong working directory and later without deterministic TeX epoch anchoring (byte drift across PDFs).
  - **Mitigation applied:** corrected TeX build working directory and rebuilt with `SOURCE_DATE_EPOCH` anchored to the input snapshot mtime; subsequent PDF hash diff check is stable (`0` diff lines).
  - **Warning (non-blocking):** matplotlib `Unable to import Axes3D` warning persists.
  - **Mitigation:** empirics workflow is 2D-only and completed successfully; keep warning tracked for environment normalization before future 3D workloads.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs regenerated in place.

## 2026-03-15 00:22 CET (23:22 UTC)

- Scope executed:
  1. Re-ran full empirics reproducibility cycle (`step00`..`step06`) and refreshed all generated tables/figures/summaries.
  2. Recompiled all empirics summary PDFs (`STEP_00`..`STEP_06`, 2-pass `pdflatex`).
  3. Re-checked consistency identities/sanity bounds across Step02/03/04/05 key metrics.
  4. Applied one internal report-maintenance fix in Step06 where PDF typesetting quality was weak.

- Commands/pipelines run (core):
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex` (2 passes each) on `STEP_00`..`STEP_06` TeX summaries.

- Fixes/regressions handled:
  - **Step06 PDF typesetting regression fix** (`working/results/empirics/summaries/STEP_06_top_client_address_profile.tex`)
    - Replaced long unbreakable `\texttt{...}` address/path spans with `\path{...}` and loaded `url` package to avoid layout overflow.
    - Regenerated `STEP_06_top_client_address_profile.pdf` (2-pass `pdflatex`) after patch.

- Consistency/repro checks passed:
  - Generated artifacts present and non-empty: figures `30/30`, tables `43/43`, summary PDFs `7/7`.
  - Step02 ordering identity valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 sanity bounds valid: observed-delay agents `<=` registered agents; burst clients `<=` total clients.
  - Step04 transfer partition valid: `transfer_events_total = mint + burn + secondary`.
  - Step05 owner-class partition valid: `n_feedback_total = own + other + nonowner + unknown`.

- Blockers / warnings:
  - **Blocker (resolved during run):** initial attempt used `xurl` package not available in current TeX environment (`xurl.sty` missing).
  - **Mitigation applied:** switched to `url` package (available), kept line-break fix via `\path{...}`, recompiled successfully.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs were regenerated in place.

## 2026-03-15 01:23 CET (00:23 UTC)

- Scope executed:
  1. Re-ran full empirics maintenance cycle (`step00`..`step06`) and rebuilt all summary PDFs (`STEP_00`..`STEP_06`, 2-pass `pdflatex`).
  2. Re-checked consistency/reproducibility across scripts, tables, figures, and PDFs.
  3. Detected and fixed two backward-compatibility regressions in key-metric aliases used by legacy maintenance checks.
  4. Regenerated affected outputs in place and re-validated determinism on immediate rerun.

- Fixes/regressions handled:
  - **Step03 alias regression fix** (`working/analysis/empirics/empirics_step03_temporal_dynamics.py`)
    - Added legacy alias `n_agents_with_observed_delay` to `temporal_dynamics_key_metrics.csv` (mapped to `n_agents_with_feedback_delay_observed`).
  - **Step05 alias regression fix** (`working/analysis/empirics/empirics_step05_owner_behavior.py`)
    - Added legacy aliases `n_owner_own`, `n_owner_other`, `n_nonowner` to `step05_owner_behavior_key_metrics.csv`.

- Outputs regenerated in place (affected):
  - Full pipeline outputs refreshed (`step00`..`step06`).
  - Specifically regenerated after fixes:
    - `tables/temporal_dynamics_key_metrics.csv`
    - `tables/step05_owner_behavior_key_metrics.csv`
    - `summaries/step03_temporal_dynamics.md`
    - `summaries/step05_owner_behavior.md`
    - `figures/fig07_first_feedback_delay_hist.pdf`
    - `figures/fig08_mean_feedback_curve_by_bins.pdf`
    - `figures/fig09_client_burst_disappear_map.pdf`
    - `figures/fig05a_owner_feedback_composition.pdf`
    - `figures/fig05b_owner_feedback_temporal_composition.pdf`
    - `summaries/STEP_03_temporal_dynamics.pdf`
    - `summaries/STEP_05_owner_behavior.pdf`

- Consistency/repro checks passed:
  - Artifacts present/non-empty: figures `30/30`, tables `43/43`, summary PDFs `7/7`.
  - Step02 ordering valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 bounds valid and legacy alias restored.
  - Step04 transfer partition valid: `37334 = 28418 + 0 + 8916`.
  - Step05 class partition valid: `2782 = 0 + 79 + 2703 + 0` and legacy aliases restored.
  - Immediate rerun determinism check on CSV + step markdown summaries: diff lines `0`.

- Blockers / warnings:
  - **Blocker (resolved during run):** legacy maintenance checks failed on missing Step03/Step05 short alias names.
  - **Mitigation applied:** restored alias keys in scripts and regenerated affected outputs; checks now pass.
  - No remaining blocking issues.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal, non-destructive, and outputs were regenerated in place.

## 2026-03-15 02:26 CET (01:26 UTC)

- Scope executed:
  1. Full overnight maintenance rerun on empirics pipeline (`step00`..`step06`) with in-place regeneration of tables/figures/markdown summaries.
  2. Full summary PDF rebuild (`STEP_00`..`STEP_06`, 2-pass `pdflatex`) and reproducibility re-check on regenerated artifacts.
  3. Cross-step consistency checks re-validated on key identities/bounds (Step02/03/04/05).
  4. Targeted quality improvement on a weak interpretive note in Step03 figure explanation.

- Commands/pipelines run (core):
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex` (2 passes each) on `STEP_00`..`STEP_06` summaries.
  - Determinism rerun (scripts + PDFs) with fixed `SOURCE_DATE_EPOCH` anchored to raw snapshot mtime.

- Fixes/improvements applied:
  - **Step03 methodological/figure-note strengthening** (`working/results/empirics/summaries/STEP_03_temporal_dynamics.tex`)
    - Added explicit caveat in F9 (`fig09_client_burst_disappear_map.pdf`) that burst-and-disappear cases are sparse in current sample (`2/571`) and the figure is descriptive (not standalone causal evidence).
    - Regenerated affected output in place: `STEP_03_temporal_dynamics.pdf`.

- Consistency/repro checks passed:
  - Non-empty artifact counts: figures `30/30`, tables `43/43`, summary PDFs `7/7`.
  - Step02 ordering valid: `top1 <= top5 <= top10 <= 1` (`0.436736 <= 0.697340 <= 0.717469`).
  - Step03 bounds valid: observed-delay agents `<=` registered agents (`1470 <= 28418`), burst-disappear clients `<=` clients with feedback (`2 <= 571`).
  - Step04 transfer partition valid: `transfer_events_total = mint + burn + secondary` (`37334 = 28418 + 0 + 8916`).
  - Step05 owner-class partition valid: `n_feedback_total = own + other + nonowner + unknown` (`2782 = 0 + 79 + 2703 + 0`).
  - Determinism checks (second full rerun):
    - tables diff lines: `0`
    - markdown summaries diff lines: `0`
    - summary PDFs diff lines: `0`

- Blockers / warnings:
  - **Blocker (resolved during run):** initial reproducibility check showed markdown drift due mixed epoch context (scripts run once without fixed `SOURCE_DATE_EPOCH`, then rerun with inherited TeX epoch).
  - **Mitigation applied:** standardized full maintenance pass with fixed `SOURCE_DATE_EPOCH` for both script and PDF reruns; determinism now clean across tables/markdown/PDFs.
  - No remaining blocking issues.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs regenerated in place.

## 2026-03-15 03:23 CET (02:23 UTC)

- Scope executed:
  1. Re-check full empirics reproducibility/integrity state (tables, figures, summary PDFs).
  2. Re-run full pipeline `step00..step06` and rebuild `STEP_00..STEP_06` PDFs (2-pass `pdflatex` each).
  3. Run consistency guards for Step02/03/04/05 metric identities and partition constraints.
  4. Improve weak methodological wording in Step06 short summary (interpretive caveat aligned with PDF narrative).

- Commands/pipelines run (core):
  - `python3 working/analysis/empirics/empirics_step00_overview.py` ... `empirics_step06_top_client_address.py`
  - `pdflatex -interaction=nonstopmode -halt-on-error` (2 passes) on `STEP_00`..`STEP_06`
  - Hash-stability checks on full empirics outputs (`csv/md/pdf`) across immediate rerun with fixed `SOURCE_DATE_EPOCH`.

- Fixes/improvements applied:
  - **Step06 methodological note refinement** (`working/analysis/empirics/empirics_step06_top_client_address.py`)
    - Added explicit interpretive caution in generated markdown: broad target coverage + clean score ranges are descriptive diagnostics, not standalone causal evidence.
  - Regenerated affected outputs in place:
    - `working/results/empirics/summaries/step06_top_client_address_profile.md`
    - refreshed step06 tables/figures (same paths, in place).

- Consistency/repro checks passed:
  - Artifact counts/non-empty: figures `30`, tables `43`, summary PDFs `7`, missing/empty `0`.
  - Step02 ordering: `top1 <= top5 <= top10 <= 1` ✅
  - Step03 bounds: observed-delay agents `<=` registered agents; burst-disappear clients `<=` total clients ✅
  - Step04 transfer partition identity ✅
  - Step05 owner-class partition identity ✅
  - Full empirics hash stability on immediate rerun: `EMPIRICS_HASH_STABLE` ✅

- Bugs/regressions detected today:
  - No new computational regressions detected in this cycle.

- Blockers / mitigation:
  - No blockers encountered.

- Outcome:
  - Overnight maintenance cycle completed successfully, internal/non-destructive, with in-place regeneration and concise methodological quality lift.

## 2026-03-15 04:22 CET (03:22 UTC)

- Scope executed:
  1. Re-ran full empirics reproducibility cycle (`step00`..`step06`) to re-check scripts/tables/figures/summary outputs.
  2. Rebuilt all summary PDFs (`STEP_00`..`STEP_06`, 2-pass `pdflatex`).
  3. Re-ran consistency checks on regenerated outputs (presence/non-empty + cross-step metric identities/sanity bounds).
  4. Applied one internal report-quality maintenance patch where figure/method explanation was weak (Step06 timeline caveat) and regenerated affected PDF.

- Core commands run:
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex` (2 passes each) on `STEP_00`..`STEP_06`

- Fixes / maintenance improvements applied:
  - **Step06 methodological/figure-note strengthening** (`working/results/empirics/summaries/STEP_06_top_client_address_profile.tex`)
    - Added explicit caveat for Fig06d that 5000-block bins are not uniform wall-clock windows; calendar-time interpretation requires block timestamps.
    - Improved readability in executive summary by shortening in-text top-client address display while keeping full address available in Step06 tables.
    - Split long input-path listing into directory + filename entries to reduce report-layout fragility.

- Outputs regenerated in place (affected):
  - Full refreshed artifacts from `step00`..`step06` scripts.
  - Rebuilt summary PDFs `STEP_00`..`STEP_06`.
  - Targeted rebuild after Step06 report patch:
    - `working/results/empirics/summaries/STEP_06_top_client_address_profile.pdf`

- Consistency/repro checks passed:
  - Figure PDFs present/non-empty: `30/30`.
  - Table CSVs present/non-empty: `43/43`.
  - Summary PDFs present/non-empty: `7/7` (`STEP_00`..`STEP_06`).
  - Step02 concentration ordering valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 sanity bounds valid: observed-delay agents `<=` registered agents; burst clients `<=` total clients.
  - Step04 transfer partition valid: `transfer_events_total = mint + burn + secondary`.
  - Step05 owner-class partition valid: `n_feedback_total = own + other + nonowner + unknown`.

- Blockers / warnings:
  - **Blocker (resolved):** first maintenance runner failed at PDF phase due to relative log path after `cd` (`tee: .../.overnight_run_tmp.log: No such file or directory`).
  - **Mitigation applied:** switched runner logging to absolute path and resumed full PDF rebuild + validations successfully.
  - **Warning (non-blocking):** minor `Overfull \\hbox` warnings persist in `STEP_06` TeX layout.
  - **Mitigation:** reduced largest overflow materially by simplifying long inline address/path text; report compiles cleanly and remains readable.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs were regenerated in place.

## 2026-03-15 05:25 CET (04:25 UTC)

- Scope executed:
  1. Full overnight maintenance rerun on empirics pipeline (`step00`..`step06`) with in-place regeneration of tables/figures/markdown summaries.
  2. Full summary PDF rebuild (`STEP_00`..`STEP_06`, 2-pass `pdflatex` each).
  3. Reproducibility re-check via immediate rerun + hash diff over all empirics outputs (`csv`, `md`, figure `pdf`, summary `pdf`).
  4. Targeted methodology-note improvement where interpretation risk was weak (Step03 temporal bin semantics + burst/disappear small-sample caution).

- Core commands run:
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex -interaction=nonstopmode -halt-on-error` (2 passes each) on `STEP_00`..`STEP_06`
  - Hash manifests + `diff -u` reproducibility check (`.overnight_post.sha256` vs `.overnight_post2.sha256`).

- Fixes / maintenance improvements applied:
  - **Step03 methodological-note hardening** (`working/analysis/empirics/empirics_step03_temporal_dynamics.py`)
    - Added explicit caveat that 2000-block bins are chain-progress bins, not fixed wall-clock intervals.
    - Added explicit caution that burst/disappear flags are screening diagnostics and unstable as rates when flagged sample size is very small.
  - Regenerated affected outputs in place, including:
    - `working/results/empirics/summaries/step03_temporal_dynamics.md`
    - `working/results/empirics/summaries/STEP_03_temporal_dynamics.pdf`
    - plus full refreshed `step00`..`step06` tables/figures/summaries/PDFs.

- Consistency/repro checks passed:
  - Artifact presence/non-empty: figures `30/30`, tables `43/43`, summary PDFs `7/7`.
  - Step02 concentration ordering valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 sanity bounds valid: observed-delay agents `<=` registered agents; burst/disappear clients `<=` total clients.
  - Step04 transfer partition identity valid: `transfer_events_total = mint + burn + secondary`.
  - Step05 owner-class partition identity valid: total = own + other + nonowner + unknown.
  - Immediate rerun hash stability: `EMPIRICS_HASH_STABLE`.

- Blockers / mitigation:
  - **Blocker (resolved):** first maintenance-check pass failed due strict metric-key assumptions in local validator (`KeyError` on renamed metric labels across Step02/03/05 key-metrics files).
  - **Mitigation applied:** hardened validator to accept known legacy/current key aliases and reran full cycle successfully.
  - **Blocker (resolved):** initial artifact-count check used incorrectly quoted `find` paths in the runner, returning false zero counts.
  - **Mitigation applied:** fixed path quoting and reran full cycle; counts and downstream checks are valid.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs were regenerated in place.

## 2026-03-15 06:20 CET (05:20 UTC)

- Scope executed:
  1. Re-checked full ERC8004 empirics reproducibility and consistency across scripts/tables/figures/PDFs.
  2. Re-ran full empirics pipeline (`step00`..`step06`) and rebuilt summary PDFs (`STEP_00`..`STEP_06`, 2-pass `pdflatex`).
  3. Re-validated key cross-step identities/sanity bounds and output completeness.
  4. Applied targeted internal maintenance fixes where weak/inconsistent.

- Commands/pipelines run:
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex` (2 passes each) on `STEP_00`..`STEP_06` TeX summaries

- Fixes/regressions handled:
  - **Reproducibility regression mitigation (run-level):** detected that exporting a wall-clock `SOURCE_DATE_EPOCH` can force run-time dependent timestamps in generated markdown summaries, weakening reproducibility claims.
    - Mitigation applied: reran full `step00`..`step06` pipeline with `SOURCE_DATE_EPOCH` unset so generators fall back to input-anchored reproducible timestamps.
    - Affected outputs regenerated in place (tables/figures/markdown summaries from all steps).
  - **Step06 report consistency fix** (`working/results/empirics/summaries/STEP_06_top_client_address_profile.tex`):
    - Replaced stale hard-coded date (`2026-03-12`) with neutral rebuild-tracking label tied to this maintenance log.
    - Recompiled `STEP_06_top_client_address_profile.pdf` (2-pass `pdflatex`).

- Consistency/repro checks passed:
  - Figure PDFs present/non-empty: `30/30`.
  - Table CSVs present/non-empty: `43/43`.
  - Summary PDFs present/non-empty: `7/7` (`STEP_00`..`STEP_06`).
  - Step02 concentration ordering valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 sanity bounds valid: observed-delay agents `<=` registered agents; burst-disappear clients `<=` unique feedback clients.
  - Step04 transfer partition identity valid: `transfer_events_total = mint + burn + secondary`.
  - Step05 owner-class partition identity valid: `n_feedback_total = own + other + nonowner + unknown`.

- Blockers / warnings:
  - No hard blockers encountered in this cycle.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs were regenerated in place.

## 2026-03-15 07:21 CET (06:21 UTC)

- Scope executed:
  1. Re-checked reproducibility/consistency across full empirics stack (`step00`..`step06`) including scripts, tables, figures, markdown summaries, and summary PDFs.
  2. Re-ran all empirics generators and rebuilt `STEP_00`..`STEP_06` PDFs (2-pass `pdflatex` each).
  3. Re-validated cross-step sanity/identity checks and artifact completeness.
  4. Applied targeted internal documentation-quality improvements where figure-reading guidance was still weak.

- Core commands run:
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex -interaction=nonstopmode -halt-on-error` (2 passes each) on `STEP_00`..`STEP_06`

- Fixes / maintenance improvements applied:
  - **Step02 report hardening** (`working/results/empirics/summaries/STEP_02_client_agent_flow.tex`)
    - Replaced stale fixed date with maintenance-log tracked rebuild label (regression-risk reduction for timestamp drift in report front matter).
    - Strengthened figure-reading caveats for F3/F4/F6 (log-scale interpretation, snapshot-scope caveat for Lorenz, and coverage-vs-intensity distinction for multi-agent rank-size).
  - Regenerated affected output in place:
    - `working/results/empirics/summaries/STEP_02_client_agent_flow.pdf`

- Consistency/repro checks passed:
  - Full run completed (`DONE` on `step00`..`step06`).
  - Artifact completeness/non-empty: figures `30/30`, tables `43/43`, summary PDFs `7/7`.
  - Step02 concentration ordering valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 sanity bounds valid: observed-delay agents `<=` registered agents; burst/disappear clients `<=` total clients.
  - Step04 transfer partition valid: `transfer_events_total = mint + burn + secondary`.
  - Step05 owner-class partition valid: `n_feedback_total = own + other + nonowner + unknown`.
  - Immediate rerun reproducibility spot-check (`csv` + `md` hashes): `REPRO_OK`.

- Blockers / warnings:
  - No blockers encountered in this cycle.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs were regenerated in place.

## 2026-03-15 23:29 CET (22:29 UTC)

- Scope executed:
  1. Re-ran full empirics pipeline (`step00`..`step06`) to re-check reproducibility and refresh scripts/tables/figures.
  2. Rebuilt all empirics summary PDFs (`STEP_00`..`STEP_06`, 2-pass `pdflatex`) after regeneration.
  3. Re-validated consistency/completeness across declared outputs from `working/analysis/empirics/README.md`.
  4. Applied targeted maintenance improvement on methodological reproducibility notes where wording was too strong.
  5. Re-ran affected outputs in place and re-checked key cross-step identities.

- Maintenance fixes/improvements applied:
  - **Methodological-note clarification (Steps 00, 01, 03, 04, 05, 06)**
    - Updated generated markdown note in:
      - `working/analysis/empirics/empirics_step00_overview.py`
      - `working/analysis/empirics/empirics_step01_reliability.py`
      - `working/analysis/empirics/empirics_step03_temporal_dynamics.py`
      - `working/analysis/empirics/empirics_step04_identity_transfer.py`
      - `working/analysis/empirics/empirics_step05_owner_behavior.py`
      - `working/analysis/empirics/empirics_step06_top_client_address.py`
    - Change: replaced “byte-identical PDF across reruns” wording with stricter/correct statement: canonical reproducibility is checked on generated tables/metrics; PDF bytes may still vary by toolchain.

- Outputs regenerated in place:
  - Scripts re-executed: `step00`..`step06` (`DONE`).
  - Summary PDFs rebuilt: `STEP_00`..`STEP_06`.
  - Current artifact inventory (non-empty):
    - Figure PDFs: `30`
    - Table CSVs: `43`
    - Step markdown summaries: `8`
    - STEP PDFs: `7`

- Consistency/repro checks passed:
  - README-declared empirics outputs present/non-empty: `66/66`.
  - Step02 concentration ordering valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 sanity bounds valid: observed-delay agents `<=` registered agents; burst-disappear clients `<=` total clients.
  - Step04 partition identity valid: `transfer_events_total = mint + burn + secondary`.
  - Step05 partition identity valid: `n_feedback_total = own + other + nonowner + unknown`.
  - Step06 out-of-range score count valid/non-negative: `score_out_of_range_n = 0`.
  - Reproducibility re-check on regenerated tables/markdown (pre/post rerun hashes): no diffs (`0` lines for both tables + md diff logs).

- Blockers / warnings:
  - **Blocker (resolved during run):** initial PDF rebuild attempt failed because `pdflatex` was launched from project root, causing relative figure paths (e.g., `../figures/...`) to miss.
  - **Mitigation applied:** reran all `pdflatex` passes from `working/results/empirics/summaries/` (TeX-native working directory); full `STEP_00`..`STEP_06` rebuild completed successfully.
  - **Warning (non-blocking):** environment still emits matplotlib `Unable to import Axes3D` warning in some runs.
  - **Mitigation:** pipeline remains 2D-only and completed successfully; warning tracked for dedicated environment normalization.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal, non-destructive, and all affected outputs were regenerated in place.

## 2026-03-16 00:20 CET (23:20 UTC)

- Scope executed:
  1. Re-ran full empirics pipeline (`step00`..`step06`) to re-check reproducibility of scripts/tables/figures.
  2. Rebuilt all summary PDFs (`STEP_00`..`STEP_06`, 2-pass `pdflatex`) and revalidated PDF integrity (`%PDF-` header + non-empty files).
  3. Ran cross-step consistency checks on regenerated metrics (Step02 ordering, Step03 bounds, Step04 transfer identity, Step05 owner-class partition).
  4. Applied one internal documentation fix where methodological wording was overstated.

- Fixes/regressions handled:
  - **Step02 reproducibility-note correction** (`working/analysis/empirics/empirics_step02_client_agent_flow.py`)
    - Replaced “byte-identical PDF” claim with a stricter statement: metadata neutralization reduces drift, while canonical reproducibility should be validated on tables/metrics due to toolchain-dependent PDF bytes.
    - Regenerated affected outputs in place via `empirics_step02_client_agent_flow.py` and rebuilt `STEP_02_client_agent_flow.pdf`.

- Consistency/repro checks passed:
  - No missing/corrupted expected artifacts in empirics outputs.
  - Step02 ordering valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 bounds valid: observed-delay agents `<=` registered agents; burst-disappear clients `<=` total clients.
  - Step04 transfer partition valid: `transfer_events_total = mint + burn + secondary`.
  - Step05 owner-class partition valid: `n_feedback_total = own + other + nonowner + unknown`.

- Blockers / warnings:
  - **Warning (non-blocking):** matplotlib still emits `Unable to import Axes3D` in this environment.
  - **Mitigation:** pipeline remains strictly 2D and completed successfully; keep warning tracked and handle environment normalization in a dedicated dependency pass.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits were internal, non-destructive, and affected outputs were regenerated in place.

## 2026-03-16 01:24 CET (00:24 UTC)

- Scope executed:
  1. Re-checked full ERC8004 empirics reproducibility/consistency by re-running `step00`..`step06` generators and rebuilding all summary PDFs (`STEP_00`..`STEP_06`, 2-pass `pdflatex`).
  2. Re-validated artifact completeness/integrity across tables, figure PDFs, markdown summaries, and step PDFs.
  3. Ran cross-step sanity/identity checks (Step02 concentration ordering, Step03 bounds, Step04 transfer partition, Step05 owner partition, Step06 out-of-range metric bound).
  4. Improved one weak methodological/figure-interpretation area in Step06 and regenerated affected outputs in place.

- Maintenance fixes/improvements applied:
  - **Step06 methodological clarity hardening** (`working/analysis/empirics/empirics_step06_top_client_address.py`):
    - Updated markdown header from generic “Generated” wording to explicit input-anchored reproducible timestamp wording.
    - Strengthened Fig06d reading note to avoid over-interpreting single-bin spikes as abrupt regime changes without adjacent-bin confirmation.
  - Regenerated affected outputs:
    - `working/results/empirics/summaries/step06_top_client_address_profile.md`
    - `working/results/empirics/summaries/STEP_06_top_client_address_profile.pdf`

- Consistency/repro checks passed:
  - Artifact inventory (non-empty): figures `30/30`, tables `43/43`, step markdown summaries `8/8`, step PDFs `7/7`.
  - Summary PDF header validation passed (`%PDF-`): `7/7`.
  - Step02 ordering valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 bounds valid: observed-delay agents `<=` registered agents; burst-disappear clients `<=` total clients.
  - Step04 transfer partition valid: `transfer_events_total = mint + burn + secondary`.
  - Step05 owner-class partition valid: `n_feedback_total = own + other + nonowner + unknown`.
  - Step06 out-of-range metric valid/non-negative: `score_out_of_range_n = 0`.

- Blockers / warnings:
  - **Blocker (resolved during run):** initial Step06 metric bound check failed due mixed-type `value` column (`top_client_address` string + numeric metrics) when performing direct numeric comparison.
  - **Mitigation applied:** switched maintenance check to explicit numeric coercion on target metric (`score_out_of_range_n`) before bound assertion; validation then passed.
  - No hard pipeline blockers encountered.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs were regenerated in place.

## 2026-03-16 02:24 CET (01:24 UTC)

- Scope executed:
  1. Re-ran full empirics generation stack (`step00`..`step06`) to re-check script/table/figure reproducibility.
  2. Rebuilt all summary PDFs (`STEP_00`..`STEP_06`, 2-pass `pdflatex`) and re-ran post-build integrity/sanity checks.
  3. Re-validated cross-step metric identities/bounds (Step02 ordering, Step03 bounds, Step04 transfer partition, Step05 owner partition).
  4. Strengthened one weak figure-explanation segment in Step03 (burst-and-disappear interpretation) and regenerated the affected PDF in place.

- Maintenance fixes/improvements applied:
  - **Methodological/figure-note improvement (Step03)**
    - File updated: `working/results/empirics/summaries/STEP_03_temporal_dynamics.tex`.
    - Improvement: expanded F9 note with explicit threshold rule (`n_fb>=10`, `n_agent>=10`, `peak_window_share>=0.70`, final inactivity `>=5000` blocks) and clarified that highlighted points are audit candidates, not definitive classifications.
    - Regenerated output: `working/results/empirics/summaries/STEP_03_temporal_dynamics.pdf`.

- Consistency/repro checks passed:
  - Non-empty artifacts after rerun: figures `30`, tables `43`, step PDFs `7`.
  - Step02 ordering valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 bounds valid: observed-delay agents `<=` registered agents; burst-disappear clients `<=` total clients.
  - Step04 transfer partition valid: `transfer_events_total = mint + burn + secondary`.
  - Step05 owner partition valid: `n_feedback_total = own + other + nonowner + unknown`.
  - Final check status: `ALL_CHECKS_OK`.

- Blockers / warnings:
  - **Blocker (resolved during run):** first PDF rebuild attempt failed when `pdflatex` was launched from repo root; relative figure paths in TeX (`../figures/...`) were not resolvable in that working directory.
  - **Mitigation applied:** reran all TeX builds from `working/results/empirics/summaries/`; full rebuild completed successfully.
  - Non-blocking LaTeX overfull-box warnings persist (layout only, no build failure).

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Changes remained internal and non-destructive; affected outputs were regenerated in place.

## 2026-03-16 03:20 CET (02:20 UTC)

- Scope executed:
  1. Full overnight maintenance rerun for empirics pipeline (`step00..step06`) and summary PDFs (`STEP_00..STEP_06`).
  2. Consistency/reproducibility checks on regenerated artifacts (tables/figures/PDF presence + identity constraints).
  3. Targeted quality lift on weak methodological/figure interpretation wording in Step05 owner-behavior report.

- Core commands run:
  - `python3 working/analysis/empirics/empirics_step00_overview.py` ... `empirics_step06_top_client_address.py`
  - `pdflatex -interaction=nonstopmode -halt-on-error` (2 passes each) on `STEP_00`..`STEP_06`
  - Determinism pass: hash compare of generated `tables/*.csv`, `summaries/step*.md`, `summaries/STEP_*.pdf`

- Fixes / improvements applied:
  - **Step05 methodological note strengthening** (`working/results/empirics/summaries/STEP_05_owner_behavior.tex`)
    - Added explicit caveat that `owner_to_other_agent` reflects global owner-set overlap and is not standalone evidence of strategic coordination.
    - Strengthened Fig05b reading note: stacked counts are absolute volumes; for cross-period interpretation, normalize by class share per bin.
  - Regenerated affected output in place:
    - `working/results/empirics/summaries/STEP_05_owner_behavior.pdf` (2-pass rebuild; deterministic on immediate rerun).

- Consistency/repro checks passed:
  - Hash drift across full pass1/pass2 artifacts: `0` diff lines.
  - Figures non-empty: `30/30`.
  - Tables non-empty: `43/43`.
  - Summary PDFs non-empty: `7/7`.
  - Step02 ordering valid: `top1 <= top5 <= top10 <= 1` (`0.436736 <= 0.697340 <= 0.717469`).
  - Step03 bounds valid: observed-delay agents `<=` registered agents; burst-disappear clients `<=` total clients (`1470<=28418; 2<=571`).
  - Step04 transfer partition valid: `transfer_events_total = mint + burn + secondary` (`37334=28418+0+8916`).
  - Step05 owner-class partition valid: `n_feedback_total = owner_to_own + owner_to_other + nonowner + owner_unknown` (`2782=0+79+2703+0`).

- Blockers / mitigation:
  - **Blocker (resolved):** consistency checker initially failed with `KeyError` due metric-name drift in generated tables (`top1_share` vs `top1_client_feedback_share`; `n_feedback_owner_to_own` vs `n_owner_to_own_agent`).
  - **Mitigation applied:** updated checker key mapping to current schema and re-ran validations successfully.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs regenerated in place.

## 2026-03-16 04:20 CET (03:20 UTC)

- Scope executed:
  1. Re-ran full empirics maintenance cycle (`step00`..`step06`) and rebuilt summary PDFs (`STEP_00`..`STEP_06`, 2-pass `pdflatex`).
  2. Re-checked consistency/integrity across all produced tables, figures, markdown summaries, and PDFs.
  3. Re-validated cross-step sanity identities/bounds (Step02 ordering, Step03 bounds, Step04 transfer partition, Step05 owner partition, Step06 out-of-range metric).
  4. Improved one weak methodological section in Step00 figure interpretation and regenerated affected PDF in place.

- Fixes / quality improvements applied:
  - **Step00 methodological-note strengthening** (`working/results/empirics/summaries/STEP_00_empirics_overview.tex`):
    - Added explicit caveats in F00d/F00e that log-log power-law fits are local descriptive diagnostics (cutoff-sensitive), not formal structural tests.
    - Clarified client-vs-agent exponent comparison as descriptive slope comparison, not causal/structural inference.
  - Regenerated affected output:
    - `working/results/empirics/summaries/STEP_00_empirics_overview.pdf`

- Repro/consistency checks passed:
  - Artifact inventory (non-empty): figures `30/30`, tables `43/43`, markdown summaries `8/8`, step PDFs `7/7`.
  - Step02 ordering valid: `top1 <= top5 <= top10` (`0.436736 <= 0.697340 <= 0.717469`).
  - Step03 bounds valid: observed-delay agents `<=` registered agents; burst-disappear clients `<=` total clients (`1470<=28418; 2<=571`).
  - Step04 transfer identity valid: `transfer_events_total = mint + burn + secondary` (`37334=28418+0+8916`).
  - Step05 owner partition valid: `n_feedback_total = own + other + nonowner + unknown` (`2782=0+79+2703+0`).
  - Step06 bound valid: `score_out_of_range_n = 0` (non-negative).
  - Data-level reproducibility check (tables + markdown): stable (`hash diff lines = 0`) on immediate rerun.

- Blockers / mitigation:
  - **Blocker (known, non-fatal):** byte-level PDF hashes still drift on immediate rebuild despite unchanged data outputs.
  - **Mitigation:** treat CSV/metric invariants and markdown hashes as canonical reproducibility checks; keep PDF byte-hash comparison as informational only unless deterministic PDF normalization is introduced in a dedicated post-process pass.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits were internal, non-destructive, and affected outputs were regenerated in place.

## 2026-03-16 05:22 CET (04:22 UTC)

- Scope executed:
  1. Re-ran full empirics reproducibility cycle (`step00`..`step06`) from source scripts.
  2. Recompiled all empirics summary PDFs (`STEP_00`..`STEP_06`) with 2-pass `pdflatex`.
  3. Re-checked consistency/completeness across regenerated tables, figures, and PDFs (non-empty artifacts + cross-step sanity identities).
  4. Reviewed methodological/figure-explanation coverage in current summaries; no weak sections requiring patch were detected in active step outputs for this run.

- Commands/pipelines run:
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex` (2 passes each) on `STEP_00`..`STEP_06` TeX summaries.

- Consistency/repro checks passed:
  - Figure PDFs present/non-empty: `30/30`.
  - Table CSVs present/non-empty: `43/43`.
  - Summary PDFs present/non-empty: `7/7`.
  - Step02 concentration ordering valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 sanity bounds valid: observed-delay agents `<=` registered agents; burst-disappear clients `<=` total clients.
  - Step04 transfer partition identity valid: `transfer_events_total = mint + burn + secondary` (`37334 = 28418 + 0 + 8916`).
  - Step05 class partition identity valid: `n_feedback_total = own + other + nonowner + unknown`.

- Blockers / warnings:
  - **Warning (non-blocking):** matplotlib environment still emits `Unable to import Axes3D`.
  - **Mitigation:** empirics workflow remains strictly 2D; run completed successfully without impact. Warning kept tracked for future environment normalization.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Outputs were regenerated in place; edits remained internal and non-destructive.

## 2026-03-16 06:24 CET (05:24 UTC)

- Scope executed:
  1. Re-ran full empirics maintenance pipeline (`step00`..`step06`) and rebuilt all summary PDFs (`STEP_00`..`STEP_06`, 2-pass `pdflatex`).
  2. Re-checked consistency/reproducibility on generated scripts/tables/figures/PDFs (presence, non-empty outputs, metric identities, sanity bounds).
  3. Applied one regression-hardening code fix in Step03 and regenerated affected outputs in place.

- Commands/pipelines run:
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex` (2 passes each) on `STEP_00`..`STEP_06` under `working/results/empirics/summaries/`

- Fixes / methodological improvements:
  - **Step03 regression-hardening** (`working/analysis/empirics/empirics_step03_temporal_dynamics.py`): added backward-compatible metric alias `n_agents_with_observed_first_feedback` to `temporal_dynamics_key_metrics.csv` to prevent downstream maintenance-check key errors.
  - **Step03 note quality improvement**: strengthened methodological/figure guidance in generated summary by clarifying (i) delay quantiles are conditional on agents with observed feedback, and (ii) Fig07 uses p99 visual trim for readability.

- Regenerated affected outputs in place:
  - `working/results/empirics/tables/temporal_dynamics_key_metrics.csv`
  - `working/results/empirics/summaries/step03_temporal_dynamics.md`
  - `working/results/empirics/figures/fig07_first_feedback_delay_hist.pdf`
  - `working/results/empirics/figures/fig08_mean_feedback_curve_by_bins.pdf`
  - `working/results/empirics/figures/fig09_client_burst_disappear_map.pdf`
  - `working/results/empirics/summaries/STEP_03_temporal_dynamics.pdf`

- Consistency checks passed:
  - Output inventory non-empty: 30 figure PDFs, 43 CSV tables, 7 summary PDFs.
  - Step02 concentration ordering valid: `top1 <= top5 <= top10 <= 1`.
  - Step04 transfer identity valid: `transfer_events_total = mint + burn + secondary`.
  - Step03 sanity bounds valid: observed-delay agents `<=` registered agents; burst clients `<=` total clients.

- Blocker + mitigation:
  - **Blocker encountered:** initial integrity check failed with `KeyError: n_agents_with_observed_first_feedback` (naming mismatch in expected legacy key).
  - **Mitigation applied:** added legacy alias key in Step03 metrics export, reran Step03 + PDF build, and re-ran integrity checks (all passed).

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive.

## 2026-03-16 07:20 CET (06:20 UTC)

- Scope executed:
  1. Re-checked full ERC8004 empirics reproducibility/consistency on current snapshot by re-running all empirics scripts (`step00`..`step06`).
  2. Recompiled all summary PDFs (`STEP_00`..`STEP_06`, 2-pass `pdflatex`) and regenerated affected outputs in place.
  3. Ran post-run consistency validation on expected output inventory and cross-step metric identities.
  4. Reviewed methodological/figure-note quality in refreshed summaries (no new weak sections requiring patch in this cycle).

- Commands/pipelines run:
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex` (2 passes each) on `STEP_00`..`STEP_06` TeX summaries.

- Validation results:
  - README-declared expected outputs: `69/69` present, `0` missing, `0` empty.
  - Step02 concentration ordering: `0 <= top1 <= top5 <= top10 <= 1` passed (`0.436736 <= 0.697340 <= 0.717469`).
  - Step03 sanity bounds passed: agents `1470/28418`, burst clients `2/571`.
  - Step04 transfer partition identity passed: `37334 = 28418 + 0 + 8916`.
  - Step05 owner-class partition identity passed: `2782 = 0 + 79 + 2703 + 0`.

- Reproducibility artifacts written:
  - `working/results/empirics/summaries/.overnight_maintenance_20260316_0721.log`
  - `working/results/empirics/summaries/.overnight_checks_20260316_0721.log`
  - `working/results/empirics/summaries/.overnight_post_tables_20260316_0721.sha256`
  - `working/results/empirics/summaries/.overnight_post_figs_20260316_0721.sha256`
  - `working/results/empirics/summaries/.overnight_post_pdf_20260316_0721.sha256`

- Blockers / mitigation:
  - No hard blockers encountered in this cycle.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; outputs regenerated in place.

## 2026-03-16 23:22 CET (22:22 UTC)

- Scope executed:
  1. Re-checked full ERC8004 empirics reproducibility by re-running `step00`..`step06` scripts.
  2. Rebuilt all summary PDFs (`STEP_00`..`STEP_06`, 2-pass `pdflatex`).
  3. Re-validated consistency/completeness across produced tables, figures, markdown summaries, and PDFs.
  4. Applied targeted methodological/figure-explanation improvement where weakest (Step04 transfer report).
  5. Regenerated affected outputs in place and archived run artifacts/hashes.

- Commands/pipelines run (core):
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex` (2 passes each) on `STEP_00`..`STEP_06` TeX summaries.
  - Targeted refresh: `pdflatex` (2 passes) on updated `STEP_04_identity_transfer.tex`.

- Consistency/repro checks passed:
  - Script run status: all empirics steps completed (`DONE`).
  - Output inventory non-empty after refresh: `csv=43`, `figure_pdf=30`, `step_md=8`, `summary_pdf=7`.
  - Key identities/sanity checks all valid:
    - Step02: `top1 <= top5 <= top10 <= 1`.
    - Step03: observed-delay agents `<=` registered agents; burst clients `<=` unique clients.
    - Step04: `transfer_events_total = mint + burn + secondary`.
    - Step05: `n_feedback_total = own + other + nonowner + unknown`.
  - Hash-diff outcome:
    - Tables (`*.csv`): no diff.
    - Figures (`fig*.pdf`): no diff.
    - Summary reports (`STEP_*.pdf`): hash drift observed after recompilation.

- Fixes/improvements applied:
  - **Step04 methodological + figure-note hardening** (`working/results/empirics/summaries/STEP_04_identity_transfer.tex`)
    - Added explicit non-causal interpretation note for snapshot-based transfer metrics.
    - Strengthened figure caveats:
      - Fig11: visual-tail trimming caveat (read percentiles from tables, not visual bounds).
      - Fig12: log-rank visual compression caveat.
      - Fig13: overlap-subsample/outlier sensitivity caveat.
      - Fig14: burst/disappear flag interpreted as heuristic prioritization, not standalone manipulation proof.

- Blockers / mitigations:
  - **Blocker (none hard):** no execution blocker in this cycle.
  - **Non-blocking reproducibility caveat:** `STEP_*.pdf` hash drift on rebuild despite stable data outputs.
  - **Mitigation:** preserve reproducibility checks on CSV metrics/identities; keep pre/post hash artifacts (`.overnight_pre_*`, `.overnight_post_*`, `.overnight_repro_*_diff_*`) for audit trace.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs regenerated in place.

## 2026-03-18 00:20 CET (23:20 UTC, 2026-03-17)

- Scope executed:
  1. Re-ran full empirics pipeline (`step00`..`step06`) to re-check reproducibility of scripts/tables/figures.
  2. Rebuilt all summary PDFs (`STEP_00`..`STEP_06`, 2-pass `pdflatex`) under `working/results/empirics/summaries/`.
  3. Re-validated cross-step consistency/completeness: artifact inventory, metric identities/bounds (Step02–06).
  4. Identified weak Step01 methodological sections not yet patched in prior cycles; applied targeted improvements and regenerated affected PDF in place.

- Commands/pipelines run (core):
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex -interaction=nonstopmode -halt-on-error` (2 passes each) on `STEP_00`..`STEP_06`.
  - Targeted rebuild: `pdflatex` (2 passes) on updated `STEP_01_empirics_reliability.tex`.

- Fixes / methodological improvements applied:
  - **Step01 methodology hardening** (`working/results/empirics/summaries/STEP_01_empirics_reliability.tex`):
    - Added explicit caveat on shrinkage hyperparameter `k=10`: it is an operational constant, not statistically derived; ranking sensitivity to alternative values of `k` (e.g. 5, 10, 20) should be verified before applying fixed selection thresholds.
    - Added explicit caveat on tier thresholds (High/Medium/Low): thresholds are operational heuristics, not data-driven statistical cutoffs, and should be re-evaluated if dataset coverage structure changes significantly.
    - Strengthened F1 (Fig01 score vs coverage) reading note: clarified that the figure displays raw `mean_score`, not `shrunk_score`; outliers with high raw score and low coverage are already corrected toward the global mean in the actual ranking variable (`shrunk_score`), so visual instability in the scatter does not propagate to the operational ranking output.
  - Regenerated affected output in place:
    - `working/results/empirics/summaries/STEP_01_empirics_reliability.pdf`

- Consistency/repro checks passed:
  - All empirics scripts ran to completion (`DONE`): `step00`..`step06`.
  - Artifact inventory non-empty: figures `30/30`, tables `43/43`, summary PDFs `7/7` (valid `%PDF-` header: `7/7`).
  - Step02 concentration ordering valid: `0 <= top1 <= top5 <= top10 <= 1` (`0.436736 <= 0.697340 <= 0.717469`).
  - Step03 bounds valid: observed-delay agents `1470 <= 28418` registered agents; burst-disappear clients `2 <= 571` total clients with feedback.
  - Step04 transfer partition identity valid: `37334 = 28418 + 0 + 8916`.
  - Step05 owner-class partition identity valid: `2782 = 0 + 79 + 2703 + 0`.
  - Step06 out-of-range score rows: `0` (non-negative bound satisfied).

- Bugs/regressions detected:
  - **Maintenance check key-name drift (non-data, resolved inline):** inline consistency checker initially read `n_burst_and_disappear_clients` and `n_unique_clients_with_feedback` from Step03 metrics CSV, which mapped to empty strings (returning `0 <= 0`). Actual CSV keys are `n_clients_burst_disappear=2` and `n_clients_total=571`. No data regression — naming mismatch only in transient checker keys. Documented for future hardening of the maintenance-check key-alias table.
  - No computational regressions detected in step outputs.

- Blockers / warnings:
  - No hard blockers encountered in this cycle.
  - **Warning (tracked, non-blocking):** Step03 inline consistency checker key-name drift (see above). Mitigation: verified correct values directly from CSV; both bounds satisfied.
  - **Warning (tracked, non-blocking):** `STEP_*.pdf` byte-level hashes still drift on rebuild due to TeX toolchain metadata; CSV/metric invariants remain canonical reproducibility check.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs regenerated in place.

## 2026-03-18 01:20 CET (00:20 UTC)

- Scope executed:
  1. Re-ran full empirics pipeline (`step00`..`step06`) to re-check script-level reproducibility and refresh generated tables/figures/markdown summaries in place.
  2. Rebuilt all empirics summary PDFs (`STEP_00`..`STEP_06`, 2-pass `pdflatex`).
  3. Re-validated cross-step consistency/completeness: artifact inventory, metric identities/bounds (Step02–06).
  4. Hardened the overnight inline consistency checker to be robust to (a) deprecated `squeeze` argument in `pd.read_csv` (newer pandas) and (b) float-formatted integer values in metric CSVs (`int(float(v))` cast).
  5. Applied targeted methodological-note improvements to Step03 (two weak figure-reading sections); regenerated affected PDF in place.

- Commands/pipelines run (core):
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex -interaction=nonstopmode -halt-on-error` (2 passes each) on `STEP_00`..`STEP_06`.
  - Targeted rebuild: `pdflatex` (2 passes) on updated `STEP_03_temporal_dynamics.tex`.

- Fixes / methodological improvements applied:
  - **Inline consistency checker hardening (non-data fix):**
    - Removed use of deprecated `pd.read_csv(squeeze=True)` (removed in newer pandas versions).
    - Replaced direct `int(value)` conversion with `int(float(value))` to handle float-formatted integer values (e.g., `"1470.0"`) in metric CSVs.
    - Both issues caused false `CHECKS_FAILED` in previous inline runs but did not affect actual data or script outputs; now resolved in checker.
  - **Step03 F7 selection-conditioning caveat** (`working/results/empirics/summaries/STEP_03_temporal_dynamics.tex`):
    - Added explicit paragraph clarifying that the delay distribution is conditioned on agents with ≥1 feedback (1,470 / 28,418 = 5.17%); the remaining 26,948 agents are excluded by construction.
    - Corrects potential over-reading of F7 as representative of all registered agents.
  - **Step03 F8 right-truncation caveat** (`working/results/empirics/summaries/STEP_03_temporal_dynamics.tex`):
    - Added explicit paragraph warning that at large `bin_idx` values the number of active agents drops sharply (right-truncation from finite observation window); the mean at large bin indices is estimated on few agents and is less reliable.
    - Recommends reading F8 jointly with the secondary-axis agent-count bars.
  - Regenerated affected output in place:
    - `working/results/empirics/summaries/STEP_03_temporal_dynamics.pdf`

- Consistency/repro checks passed:
  - All empirics scripts ran to completion (`DONE`): `step00`..`step06`.
  - Artifact inventory non-empty: figures `30/30`, tables `43/43`, summary PDFs `7/7`, summary MDs `8/8`.
  - Summary PDFs with valid `%PDF-` header: `7/7`.
  - Step02 concentration ordering valid: `0 <= top1 <= top5 <= top10 <= 1` (`0.436736 <= 0.697340 <= 0.717469`).
  - Step03 bounds valid: observed-delay agents `1470 <= 28418`; burst-disappear clients `2 <= 571`.
  - Step04 transfer partition identity valid: `37334 = 28418 + 0 + 8916`.
  - Step05 owner-class partition identity valid: `2782 = 0 + 79 + 2703 + 0`.
  - Step06 out-of-range score rows: `0`.

- Bugs/regressions detected:
  - **Inline consistency checker bugs (resolved this cycle):**
    1. `pd.read_csv(squeeze=True)` — argument removed in pandas ≥2.0; caused `TypeError` and false `CHECKS_FAILED` in transient checker.
    2. `int("1470.0")` — float-formatted integer in CSV; caused `ValueError` on direct `int()` conversion.
    - Both bugs were in the transient maintenance checker only (not in any empirics script). Fixed inline; no data regressions.

- Blockers / warnings:
  - No hard blockers encountered in this cycle.
  - **Warning (tracked, non-blocking):** `STEP_*.pdf` byte-level hashes still drift on rebuild due to TeX toolchain metadata; CSV/metric invariants and markdown hashes remain the canonical reproducibility check.
  - **Warning (prior cycle, now mitigated):** Step03 inline consistency checker key-name drift (`n_burst_and_disappear_clients` vs `n_clients_burst_disappear`) noted in previous log entry. Mitigation applied this cycle: checker now tries multiple alias keys in fallback order; both canonical and legacy keys correctly resolve to `2` and `571` respectively.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs regenerated in place.

## 2026-03-18 02:20 CET (01:20 UTC)

- Scope executed:
  1. Re-ran full empirics pipeline (`step00`..`step06`) to re-check script-level reproducibility and refresh generated tables/figures/markdown summaries in place.
  2. Rebuilt all empirics summary PDFs (`STEP_00`..`STEP_06`, 2-pass `pdflatex`).
  3. Re-validated cross-step consistency/completeness: artifact inventory, metric identities/bounds (Step02–06).
  4. Applied targeted methodological-note improvements to Step04 (two weak sections); regenerated affected PDF in place.

- Commands/pipelines run (core):
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex -interaction=nonstopmode -halt-on-error` (2 passes each) on `STEP_00`..`STEP_06`.
  - Targeted rebuild: `pdflatex` (2 passes) on updated `STEP_04_identity_transfer.tex`.

- Fixes / methodological improvements applied:
  - **Step04 burn=0 supply-invariant interpretation note** (`working/results/empirics/summaries/STEP_04_identity_transfer.tex`):
    - Added explicit paragraph noting that burn events = 0 in the snapshot implies the entire circulating supply equals the minted supply (28,418 tokens). Flags that all downstream metrics (ownership concentration, holding deltas) are conditioned on the full minted universe — an empirically notable structural fact missing from prior report versions.
    - Added reference Gini for feedback-client side (~0.84 from Step02) to make the "less extreme than feedback side" ownership-concentration comparison quantitatively grounded.
  - **Step04 Fig14 heuristic-parameter sensitivity caveat** (`working/results/empirics/summaries/STEP_04_identity_transfer.tex`):
    - Expanded Fig14 reading note to explicitly state the three operative threshold parameters (≥20 transfers received; ≥70% in densest 1000-block window; ≥5000-block inactivity tail) and warn that the flagged count (111) is sensitive to those thresholds.
    - Mitigates over-reading of the flagged count as a robust or threshold-invariant finding.
  - Regenerated affected output in place:
    - `working/results/empirics/summaries/STEP_04_identity_transfer.pdf`

- Consistency/repro checks passed:
  - All empirics scripts ran to completion (`DONE`): `step00`..`step06`.
  - Artifact inventory non-empty: figures `30/30`, tables `43/43`, summary PDFs `7/7`, summary MDs `8/8`.
  - Summary PDFs with valid `%PDF-` header: `7/7`.
  - Step02 concentration ordering valid: `0 <= top1 <= top5 <= top10 <= 1` (`0.436736 <= 0.697340 <= 0.717469`).
  - Step03 bounds valid: observed-delay agents `1470 <= 28418`; burst-disappear clients `2 <= 571`.
  - Step04 transfer partition identity valid: `37334 = 28418 + 0 + 8916`.
  - Step05 owner-class partition identity valid: `2782 = 0 + 79 + 2703 + 0`.
  - Step06 out-of-range score rows: `0`.
  - Script hash stability on same-epoch immediate rerun: `SCRIPT_STABLE_ON_SAME_EPOCH` (CSV diff = 0, MD diff = 0 on second pass).
  - Initial MD hash drift (pre→post first pass): expected — session-epoch update in `generated_at` field; stable on same-epoch reruns.

- Bugs/regressions detected:
  - No computational regressions detected in step scripts or generated tables/figures.
  - MD hash drift (pre vs post snapshot): confirmed as expected `generated_at` timestamp update (epoch changed between prior session and current cycle); no data-level change.

- Blockers / warnings:
  - No hard blockers encountered in this cycle.
  - **Warning (tracked, non-blocking):** `STEP_*.pdf` byte-level hashes still drift on rebuild due to TeX toolchain metadata; CSV/metric invariants and markdown hashes remain canonical reproducibility check.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs regenerated in place.

## 2026-03-18 03:20 CET (02:20 UTC)

- Scope executed:
  1. Re-ran full empirics pipeline (`step00`..`step06`) to re-check script-level reproducibility and refresh generated tables/figures/markdown summaries in place.
  2. Rebuilt all empirics summary PDFs (`STEP_00`..`STEP_06`, 2-pass `pdflatex`).
  3. Re-validated cross-step consistency/completeness: artifact inventory, metric identities/bounds (Step02–06).
  4. Applied targeted methodological-note improvements to Step02 (three weak sections) and Step05 (two weak sections); fixed stale date fields in STEP_00 and STEP_05 TeX headers; regenerated affected PDFs in place.
  5. Documented ghost-artifact status of four legacy March-11 figures not generated by current step scripts.

- Commands/pipelines run (core):
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex -interaction=nonstopmode -halt-on-error` (2 passes each) on `STEP_00`..`STEP_06`.

- Fixes / methodological improvements applied:
  - **STEP_00 stale date fix** (`working/results/empirics/summaries/STEP_00_empirics_overview.tex`):
    - Replaced hardcoded `\date{2026-03-11}` with rebuild-timestamp tracking directive (consistent with all other STEP files).
  - **STEP_02 HHI interpretation note** (`working/results/empirics/summaries/STEP_02_client_agent_flow.tex`):
    - Added explicit methodological note on the HHI value (0.221): contextualized against antitrust thresholds (moderate-to-high concentration bracket), but reframed for on-chain reputational context — the operative risk is low effective independent rater count (1/HHI ≈ 4.53), not market power per se. Term "Nakamoto coefficient feedback" introduced to label this metric.
  - **STEP_02 τ_a instability caveat** (`working/results/empirics/summaries/STEP_02_client_agent_flow.tex`):
    - Added explicit warning that the 89.46% single-client-only statistic is mechanically inflated by agents with n_feedback=1 (where τ_a=1 by construction, not by preference). Recommended decomposition into coverage strata (n=1, n=2–4, n≥5) for robust inference on dependency structure.
  - **STEP_02 F6 effective-rater note** (`working/results/empirics/summaries/STEP_02_client_agent_flow.tex`):
    - Added network diversity note quantifying effective raters (1/HHI≈4.53) vs. formal count (571 clients), making the diversity analysis more actionable.
    - Added linear-scale gap annotation for F3 (top client 1215 feedback vs rank-2: gap invisible in log-log but large in absolute terms).
  - **STEP_05 stale date fix** (`working/results/empirics/summaries/STEP_05_owner_behavior.tex`):
    - Replaced hardcoded `\date{2026-03-11}` with rebuild-timestamp tracking directive.
  - **STEP_05 owner_unknown reconstruction quality note** (`working/results/empirics/summaries/STEP_05_owner_behavior.tex`):
    - Added explicit paragraph interpreting `owner_unknown=0` as a positive signal of full ownership reconstruction coverage for all 2782 feedback events (not merely "no guard class activated"). Described what a non-zero value would imply (agents with incomplete ownership history prior to first feedback).
  - **STEP_05 F05a reading guide** (`working/results/empirics/summaries/STEP_05_owner_behavior.tex`):
    - Replaced minimal one-line caption with structured reading guide: interpretation of dominant nonowner bar (97.16%), meaning of owner_to_other_agent bar (79 events, dual-role structure), and key caveat that address-level concentration of the 79 events must be verified from `step05_owner_behavior_by_address.csv` before over-interpreting the aggregate share.
  - Regenerated affected outputs in place:
    - `working/results/empirics/summaries/STEP_00_empirics_overview.pdf`
    - `working/results/empirics/summaries/STEP_02_client_agent_flow.pdf` (size: 217172 bytes)
    - `working/results/empirics/summaries/STEP_05_owner_behavior.pdf` (size: 143618 bytes)

- Consistency/repro checks passed:
  - All empirics scripts ran to completion (`DONE`): `step00`..`step06`.
  - Artifact inventory non-empty: figures `30/30`, tables `43/43`, summary PDFs `7/7` (valid `%PDF-` header: `7/7`), summary MDs `8/8`.
  - Step02 Top-k ordering valid: `0.436736 <= 0.697340 <= 0.717469` (all in [0,1]): ✓
  - Step02 Gini=0.7798 in [0,1]: ✓; HHI=0.220983 in [0,1]: ✓; effective raters=4.53.
  - Step03 bounds valid: observed-delay agents `1470 <= 28418`; burst-disappear clients `2 <= 571`.
  - Step04 transfer partition identity valid: `37334 = 28418 + 0 + 8916`.
  - Step05 owner-class partition identity valid: `2782 = 0 + 79 + 2703 + 0`; owner_unknown=0 (full reconstruction coverage).
  - Step06 out-of-range score rows: `0`.

- Bugs/regressions detected:
  - **Inline consistency checker key-name mismatches (non-data, documented):**
    - Step02 checker used keys `client_top1_share_pct`/`top1_share_pct` but actual CSV key is `top1_client_feedback_share` (fractional, not percent) with header row. Resolved: verified values directly from CSV with correct `pd.read_csv` call.
    - Step05 checker used key `n_owner_to_other` but actual CSV key is `n_owner_to_other_agent`; CSV uses header row. Resolved inline.
    - Step03 checker used key `n_agents_with_delay_data` but CSV key is `n_agents_with_feedback_delay_observed`. Resolved inline.
    - Root cause: inline checker key-alias table not updated to match CSV schema. No data regressions in any step script.
  - **Ghost artifacts (tracked, non-blocking):**
    - Four legacy figures dated 2026-03-11 persist in `working/results/empirics/figures/` but are NOT generated by any current step script (step00–step06):
      - `fig10_top_client_feedback_by_agent.pdf` (203 KB, 2026-03-11)
      - `fig11_top_client_feedback_timeline.pdf` (17 KB, 2026-03-11)
      - `fig12_top_agents_feedback_by_client.pdf` (68 KB, 2026-03-11)
      - `fig13_top_clients_feedback_timeline.pdf` (17 KB, 2026-03-11)
    - These originate from a superseded analysis version (pre-step06 refactor) and are no longer referenced in any active STEP_*.tex file. They do not cause script failures but inflate the figure count (30 vs 26 from current scripts).
    - **Mitigation/recommendation:** review with Manuel before removal (non-destructive policy; they could contain figures referenced in draft paper sections outside this pipeline). Flag for explicit cleanup decision.

- Blockers / warnings:
  - No hard blockers encountered in this cycle.
  - **Warning (tracked, non-blocking):** inline consistency checker key-name drift (see above). Mitigation: all values verified directly; all identities satisfied.
  - **Warning (tracked, non-blocking):** `STEP_*.pdf` byte-level hashes drift on rebuild due to TeX toolchain metadata; CSV/metric invariants remain canonical reproducibility check.
  - **Warning (new, non-blocking):** 4 ghost figures from 2026-03-11 in `figures/` directory — not regenerated by current scripts; see above for recommendation.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs regenerated in place.
  - Steps methodologically improved this cycle: STEP_02 (HHI note, τ_a instability caveat, effective-rater diversity note) and STEP_05 (owner_unknown reconstruction quality, F05a reading guide, date fix). STEP_00 date header fix applied.

## 2026-03-18 04:20 CET (03:20 UTC)

- Scope executed:
  1. Re-ran full empirics pipeline (`step00`..`step06`) to re-check script-level reproducibility and refresh generated tables/figures/markdown summaries in place.
  2. Rebuilt affected summary PDFs (`STEP_01`, `STEP_03`) following targeted methodological improvements; remaining 5 PDFs verified from prior cycle.
  3. Re-validated cross-step consistency/completeness: 8/8 invariant checks passed.
  4. Applied targeted methodological-note improvements to STEP_01 (stale date + obsolete next-step section) and STEP_03 (stale date + orphaned Add-on sections). Non-destructive: all deprecated content preserved as LaTeX comments.

- Commands/pipelines run (core):
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex -interaction=nonstopmode -halt-on-error` (2 passes each) on `STEP_01`, `STEP_03`.

- Fixes / methodological improvements applied:
  - **STEP_01 stale date fix** (`STEP_01_empirics_reliability.tex`):
    - Replaced hardcoded `\date{2026-03-10}` with rebuild-timestamp tracking directive (consistent with all other STEP files).
  - **STEP_01 obsolete "next step" section** (`STEP_01_empirics_reliability.tex`):
    - Section titled "Limitazioni e next step" referenced Step 02 as future work, but Step 02 (and Steps 03–06) are already complete. Replaced with accurate "Limitazioni e note per uso downstream" section describing integration points with the existing downstream steps, k-sensitivity reminder, and tier-threshold stability caveat.
  - **STEP_03 stale date fix** (`STEP_03_temporal_dynamics.tex`):
    - Replaced hardcoded `\date{2026-03-11}` with rebuild-timestamp tracking directive.
  - **STEP_03 orphaned Add-on sections deprecated** (`STEP_03_temporal_dynamics.tex`):
    - Two legacy "Add-on" sections (top-client concentration analysis and top-5 agents dual analysis, originally inline in step03) referenced figures F10–F13 and tables (top5_clients_specs.csv, top5_agents_specs.csv, etc.) that are NOT generated by the current `empirics_step03_temporal_dynamics.py` script. These sections were preserved as LaTeX block-comments (non-destructive policy) with an explicit maintenance header explaining supersession status and referencing STEP_06 as authoritative.
    - "Output prodotti" section updated to list only what the current step03 script generates (5 tables + 3 figures + 1 summary MD), removing the 8 legacy table/figure entries.
    - Added inline `\noindent` note listing the 4 ghost figure files still present in the filesystem (for audit traceability).
  - Regenerated affected outputs in place:
    - `working/results/empirics/summaries/STEP_01_empirics_reliability.pdf` (152,704 bytes)
    - `working/results/empirics/summaries/STEP_03_temporal_dynamics.pdf` (205,302 bytes)

- Consistency/repro checks passed (8/8):
  - All 7 empirics scripts ran to completion (`DONE`): `step00`..`step06`.
  - All 26 script-generated figures present (total 30 including 4 ghost legacy).
  - Summary PDFs valid %PDF-: 7/7.
  - Step02 top-k ordering: 0.4367 ≤ 0.6973 ≤ 0.7175 ∈ [0,1] ✓
  - Step02 Gini=0.7798 ∈ [0,1] ✓; HHI=0.2210 ∈ [0,1] ✓; effective raters=4.53.
  - Step03 bounds: delay_agents=1470 ≤ 28418; burst_clients=2 ≤ 571.
  - Step04 transfer partition: 37334=28418+0+8916 ✓
  - Step05 owner-class partition: 2782=0+79+2703+0; owner_unknown=0 (full reconstruction) ✓
  - Step06 out-of-range rows: 0.

- Bugs/regressions detected:
  - **Inline checker key-name mismatches (non-data, resolved in-session):**
    - Checker used wrong key `fig10_transfer_token_secondary_hist.pdf` (actual: `fig10_token_secondary_transfer_hist.pdf`). Corrected; no data issue.
    - Checker used wrong keys `gini_client_feedback`/`n_mint` etc. (actual: `client_feedback_gini`, `transfer_events_mint`). Corrected; all invariants confirmed satisfied.
    - Root cause: checker not updated when column names were changed in a prior step script refactoring. No data regressions.

- Blockers / warnings:
  - No hard blockers encountered in this cycle.
  - **Warning (tracked, non-blocking):** `STEP_*.pdf` byte-level hashes drift on rebuild due to TeX toolchain metadata; CSV/metric invariants remain canonical reproducibility check.
  - **Warning (tracked, pending decision):** 4 ghost figures (fig10–fig13, 2026-03-11) still present in `figures/` directory; not generated by current scripts; awaiting explicit cleanup decision from Manuel.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs regenerated in place.
  - Steps improved this cycle: STEP_01 (stale date, obsolete next-step section) and STEP_03 (stale date, orphaned Add-on deprecated, Output inventory corrected).

## 2026-03-18 23:22 CET (22:22 UTC)

- Scope executed:
  1. Re-ran full empirics pipeline (`step00`..`step06`) to re-check reproducibility across scripts/tables/figures/summaries.
  2. Recompiled all summary PDFs (`STEP_00`..`STEP_06`, 2-pass `pdflatex`).
  3. Re-ran consistency checks on regenerated outputs (presence/non-empty artifacts + cross-step metric identities).
  4. Applied one internal regression fix and regenerated affected Step02 outputs in place.

- Commands/pipelines run (core):
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex` (2 passes each) on `STEP_00`..`STEP_06`.

- Fixes/regressions handled today:
  - **Step02 backward-compat metric alias fix** (`working/analysis/empirics/empirics_step02_client_agent_flow.py`)
    - Added `top1_clients_feedback_share` alias (retaining canonical `top1_client_feedback_share`) in `client_agent_flow_key_metrics.csv` to avoid compatibility breaks in downstream maintenance checks.

- Outputs regenerated in place (affected):
  - Full refreshed artifacts from `step00`..`step06` scripts.
  - Rebuilt summary PDFs `STEP_00`..`STEP_06`.
  - Targeted refreshed Step02 artifacts after alias fix:
    - `working/results/empirics/tables/client_agent_flow_key_metrics.csv`
    - `working/results/empirics/tables/client_activity_summary.csv`
    - `working/results/empirics/tables/agent_incoming_client_mix.csv`
    - `working/results/empirics/tables/client_agent_edges.csv`
    - `working/results/empirics/figures/fig03_client_feedback_rank_size.pdf`
    - `working/results/empirics/figures/fig04_client_feedback_lorenz.pdf`
    - `working/results/empirics/figures/fig05_agent_top_client_share_hist.pdf`
    - `working/results/empirics/figures/fig06_client_multi_agent_rank_size.pdf`
    - `working/results/empirics/summaries/step02_client_agent_flow.md`
    - `working/results/empirics/summaries/STEP_02_client_agent_flow.pdf`

- Consistency/repro checks passed:
  - Non-empty figure PDFs: `30`.
  - Non-empty summary step PDFs: `7` (`STEP_00`..`STEP_06`).
  - Step02 ordering valid: `top1 <= top5 <= top10 <= 1` (`0.436736 <= 0.697340 <= 0.717469`).
  - Step03 sanity bound valid: burst/disappear clients `<=` total clients.
  - Step04 partition identity valid: `37334 = 28418 + 0 + 8916`.
  - Step05 partition identity valid: `2782 = 0 + 79 + 2703 + 0`.

- Blockers / warnings:
  - **Blocker (resolved):** downstream consistency check expected legacy `top1_clients_feedback_share` key and failed against canonical `top1_client_feedback_share` only.
  - **Mitigation applied:** added backward-compatible alias in Step02 key metrics export and regenerated affected outputs.
  - **Warning (non-blocking):** matplotlib still emits `Unable to import Axes3D` in this environment.
  - **Mitigation:** empirics workflow remains 2D-only; run completed successfully. Environment normalization deferred to dedicated dependency cleanup.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits were internal and non-destructive; affected outputs regenerated in place.

## 2026-03-19 00:22 CET (23:22 UTC)

- Scope executed:
  1. Re-ran full empirics pipeline (`step00`..`step06`) to re-check script-level reproducibility.
  2. Recompiled all summary PDFs (`STEP_00`..`STEP_06`, 2-pass `pdflatex`) and verified non-empty artifacts.
  3. Re-validated consistency across regenerated tables/figures/PDFs with key cross-step identity checks.
  4. Reviewed methodological/figure-note sections in refreshed outputs; no weak sections requiring patch in this cycle.

- Commands/pipelines run:
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex` (2 passes each) on `STEP_00`..`STEP_06` TeX summaries.

- Consistency/repro checks passed:
  - Figures present/non-empty: `30/30`.
  - Tables present/non-empty: `43/43`.
  - Summary PDFs present/non-empty: `7/7`.
  - Step02 ordering valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 sanity bounds valid: observed-delay agents `<=` registered agents; burst-disappear clients `<=` total clients.
  - Step04 transfer partition valid: `transfer_events_total = mint + burn + secondary`.
  - Step05 class partition valid: `n_feedback_total = own + other + nonowner + unknown`.

- Today regressions/bugs:
  - None detected in this run.

- Blockers / mitigations:
  - No blockers encountered.

- Run artifacts:
  - Detailed run log: `working/results/empirics/summaries/.overnight_maintenance_20260319_002112.log`

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - No destructive changes; outputs regenerated in place.

## 2026-03-19 01:20 CET (00:20 UTC)

- Scope executed:
  1. Full reproducibility re-run of empirics scripts `step00`..`step06`.
  2. Full rebuild of summary PDFs `STEP_00`..`STEP_06` (2-pass `pdflatex`).
  3. Consistency checks on regenerated tables/figures/PDFs (presence, non-empty artifacts, and cross-step identities).
  4. Targeted methodological improvement on Step06 figure/discussion interpretation, then in-place PDF regeneration.

- Commands run (core):
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex` (2 passes each) on `STEP_00`..`STEP_06` from `working/results/empirics/summaries/`.

- Fixes / improvements applied:
  - **Step06 methodological-note strengthening** (`working/results/empirics/summaries/STEP_06_top_client_address_profile.tex`)
    - Added explicit selection-bias caveat (top client is selected ex-post as sample argmax).
    - Added guidance to use benchmark distributions (top-k / quantiles / placebo-rank) for comparative/causal claims.
  - Regenerated affected output in place:
    - `working/results/empirics/summaries/STEP_06_top_client_address_profile.pdf`

- Consistency/repro checks passed:
  - Figure PDFs present/non-empty: `30/30`.
  - Table CSVs present/non-empty: `43/43`.
  - Summary PDFs present/non-empty: `7/7` (`STEP_00`..`STEP_06`).
  - Step02 ordering identity valid: `top1 <= top5 <= top10 <= 1`.
  - Step03 sanity bounds valid: observed-delay agents `<=` registered agents; burst clients `<=` total unique clients.
  - Step04 transfer partition valid: `transfer_events_total = mint + burn + secondary` (`37334 = 28418 + 0 + 8916`).
  - Step05 owner-class partition valid: `n_feedback_total = own + other + nonowner + unknown` (`2782 = 0 + 79 + 2703 + 0`).

- Blockers / warnings:
  - **Blocker (resolved during run):** initial `pdflatex` invocation from repo root could not resolve relative figure paths for TeX files.
  - **Mitigation applied:** compile TeX from `working/results/empirics/summaries/` (where relative `../figures/...` references resolve correctly); full PDF rebuild then completed.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs regenerated in place.

## 2026-03-19 02:20 CET (01:20 UTC)

- Scope executed:
  1. Re-ran full empirics pipeline (`step00`..`step06`) to re-check script/table/figure reproducibility end-to-end.
  2. Recompiled all summary PDFs (`STEP_00`..`STEP_06`, 2-pass `pdflatex`) and validated non-empty artifacts.
  3. Re-validated consistency across regenerated outputs (counts + cross-step identity checks).
  4. Applied one internal methodological-note improvement where interpretation risk remained weak (Step06 score-distribution caveat), then regenerated affected PDF in place.

- Commands/pipelines run:
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex` (2 passes each) on `STEP_00`..`STEP_06` TeX summaries.

- Fixes / improvements applied:
  - **Step06 figure-explanation strengthening** (`working/results/empirics/summaries/STEP_06_top_client_address_profile.tex`)
    - In Fig06b note, added explicit caveat that `0` out-of-range rows indicates mechanical range compliance only, not automatic score calibration validity; interpretation should include dispersion/tail shape and external benchmarks.
  - Regenerated affected output:
    - `working/results/empirics/summaries/STEP_06_top_client_address_profile.pdf`

- Consistency/repro checks passed:
  - Figures present/non-empty: `30/30`.
  - Tables present/non-empty: `43/43`.
  - Summary PDFs present/non-empty: `7/7`.
  - Step02 ordering valid: `top1 <= top5 <= top10 <= 1` (`0.436736 <= 0.697340 <= 0.717469`).
  - Step03 sanity bounds valid: observed-delay agents `<=` registered agents; burst clients `<=` total clients (`2 <= 571`).
  - Step04 transfer partition valid: `transfer_events_total = mint + burn + secondary` (`37334 = 28418 + 0 + 8916`).
  - Step05 owner-class partition valid: `n_feedback_total = own + other + nonowner + unknown` (`2782 = 0 + 79 + 2703 + 0`).

- Today regressions/bugs:
  - None detected in this cycle.

- Blockers / mitigations:
  - No blockers encountered.

- Run artifacts:
  - Detailed run log: `working/results/empirics/summaries/.overnight_maintenance_20260319_0220.log`

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs regenerated in place.

## 2026-03-19 03:20 CET (02:20 UTC)

- Scope executed:
  1. Full reproducibility re-run of empirics scripts `step00`..`step06`.
  2. Full rebuild of summary PDFs `STEP_00`..`STEP_06` (2-pass `pdflatex`).
  3. Consistency checks across generated tables/figures/PDFs and cross-step identity constraints.
  4. Methodological-note reinforcement for Step03 figure interpretation, then in-place PDF regeneration.

- Fixes / improvements applied:
  - **Regression fix (overnight checker compatibility):** added robust alias-aware checker script `working/analysis/empirics/overnight_consistency_check.py` to handle metric-key drift across Step03/Step04/Step05 key-metrics CSVs.
  - **Methodological note strengthened** (`working/results/empirics/summaries/STEP_03_temporal_dynamics.tex`):
    - In F8 note, added explicit caveat that 2000-block bins are block-time units (not civil-time bins), so block→hours/days conversion is approximate due to variable Ethereum block time.
  - Regenerated affected output in place:
    - `working/results/empirics/summaries/STEP_03_temporal_dynamics.pdf`

- Consistency/repro checks passed:
  - Figures present/non-empty: `30/30`.
  - Tables present/non-empty: `43/43`.
  - Summary PDFs present/non-empty: `7/7`.
  - Step02 ordering valid: `top1 <= top5 <= top10 <= 1` (`0.436736 <= 0.697340 <= 0.717469`).
  - Step03 sanity bounds valid: observed-delay agents `<=` registered agents; burst clients `<=` total clients (`1470 <= 28418`, `2 <= 571`).
  - Step04 transfer partition valid: `transfer_events_total = mint + burn + secondary` (`37334 = 28418 + 0 + 8916`).
  - Step05 owner-class partition valid: `n_feedback_total = own + other + nonowner + unknown` (`2782 = 0 + 79 + 2703 + 0`).

- Today regressions/bugs:
  - Detected during maintenance: overnight inline checker expected deprecated metric key `n_burst_clients_threshold10` and failed with `KeyError`.
  - Fixed by introducing alias-aware metric resolution in `overnight_consistency_check.py`; rerun completed cleanly.

- Blockers / mitigations:
  - **Blocker (resolved):** key-name drift in key-metrics CSVs broke the first consistency-check pass.
  - **Mitigation:** implemented resilient alias mapping for legacy/new metric names and reran the full check suite successfully.

- Run artifacts:
  - Detailed run log: `working/results/empirics/summaries/.overnight_maintenance_20260319_0320.log`

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Edits remained internal and non-destructive; affected outputs regenerated in place.

## 2026-03-19 04:24 CET (03:24 UTC)

- Scope executed:
  1. Re-ran full empirics maintenance pipeline (`step00`..`step06`) and regenerated tables/figures/markdown outputs in place.
  2. Recompiled all summary PDFs (`STEP_00`..`STEP_06`, 2-pass `pdflatex` each).
  3. Ran `overnight_consistency_check.py` after regeneration.
  4. Performed explicit reproducibility hash checks (pre/post snapshots over scripts, CSV tables, figure PDFs, summary MD/TEX/PDF).

- Consistency status (pass):
  - `figures_ok=30/30`
  - `tables_ok=43/43`
  - `reports_ok=7/7`
  - `step02_ordering` valid (`top1 <= top5 <= top10 <= 1`)
  - `step03_delay_bound` and `step03_burst_bound` valid
  - `step04_partition` valid (`total = mint + burn + secondary`)
  - `step05_partition` valid

- Regression/bug found and fixed:
  - **Issue:** summary report PDFs (`STEP_00`..`STEP_06`) were semantically stable but byte-unstable across repeated `pdflatex` runs (hash drift), weakening strict reproducibility checks.
  - **Fix applied:** added reproducible PDF metadata directives in all report TeX preambles:
    - `\pdfinfoomitdate=1`
    - `\pdftrailerid{}`
    - `\pdfsuppressptexinfo=15`
  - **Validation:** after patch, repeated recompile hash check reports `pdf_determinism=stable` across all `STEP_*.pdf`.

- Method/maintenance improvement:
  - Updated `working/analysis/empirics/overnight_consistency_check.py` to include TeX reproducibility preamble audit:
    - new check: `tex_repro_preamble_ok=7/7`.
  - This strengthens overnight guardrails by catching future regressions in report reproducibility settings.

- Blockers:
  - None blocking in current cycle.

- Outcome:
  - Overnight maintenance completed successfully.
  - Edits were internal and non-destructive; affected outputs regenerated in place.

## 2026-03-19 05:23 CET (04:23 UTC)

- Scope executed:
  1. Re-ran full ERC8004 empirics pipeline (`step00`..`step06`) to re-check reproducibility across scripts/tables/figures/summaries.
  2. Rebuilt all summary PDFs (`STEP_00`..`STEP_06`) with 2-pass `pdflatex` per report.
  3. Re-ran consistency checks (`overnight_consistency_check.py`) on refreshed artifacts.
  4. Re-checked table-level reproducibility with pre/post SHA256 snapshot diff.

- Commands/pipelines run:
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex` (2 passes each) on:
    - `STEP_00_empirics_overview.tex`
    - `STEP_01_empirics_reliability.tex`
    - `STEP_02_client_agent_flow.tex`
    - `STEP_03_temporal_dynamics.tex`
    - `STEP_04_identity_transfer.tex`
    - `STEP_05_owner_behavior.tex`
    - `STEP_06_top_client_address_profile.tex`
  - `python3 working/analysis/empirics/overnight_consistency_check.py`

- Maintenance findings/fixes:
  - No new script-level regressions detected in this cycle.
  - No destructive edits applied.

- Repro/consistency checks passed:
  - Figures: `30/30` non-empty PDFs.
  - Tables: `43/43` non-empty CSVs.
  - Reports: `7/7` non-empty summary PDFs.
  - TeX reproducibility preamble coverage: `7/7` (`\\pdfinfoomitdate`, `\\pdftrailerid{}`, `\\pdfsuppressptexinfo=15`).
  - Step02 ordering valid: `0.436736 <= 0.697340 <= 0.717469 <= 1`.
  - Step03 bounds valid: `1470 <= 28418` and `2 <= 571`.
  - Step04 partition valid: `37334 = 37334`.
  - Step05 partition valid: `2782 = 2782`.
  - Table-level reproducibility diff (pre/post SHA256): no differences.

- Blockers / mitigations:
  - **Blocker (resolved during run):** initial PDF rebuild attempt failed because TeX was executed from repository root, so relative figure paths (`../figures/...`) were unresolved.
  - **Mitigation applied:** reran `pdflatex` from `working/results/empirics/summaries/` (correct relative path context); full rebuild completed successfully.
  - **Warning (non-blocking):** matplotlib `Unable to import Axes3D` warning still appears in environment.
  - **Mitigation:** workflow remains 2D-only and completed successfully; warning tracked for future environment normalization.

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Outputs regenerated in place; edits remained internal and non-destructive.

## 2026-03-19 07:22 CET (06:22 UTC)

- Scope executed:
  1. Re-ran full ERC8004 empirics pipeline (`step00`..`step06`) to verify reproducibility across scripts/tables/figures/summaries.
  2. Rebuilt all summary PDFs (`STEP_00`..`STEP_06`, 2-pass `pdflatex` each).
  3. Ran `overnight_consistency_check.py` on regenerated outputs.
  4. Strengthened one weak figure-reading note in Step06 report and regenerated affected PDF in place.

- Commands/pipelines run:
  - `python3 working/analysis/empirics/empirics_step00_overview.py`
  - `python3 working/analysis/empirics/empirics_step01_reliability.py`
  - `python3 working/analysis/empirics/empirics_step02_client_agent_flow.py`
  - `python3 working/analysis/empirics/empirics_step03_temporal_dynamics.py`
  - `python3 working/analysis/empirics/empirics_step04_identity_transfer.py`
  - `python3 working/analysis/empirics/empirics_step05_owner_behavior.py`
  - `python3 working/analysis/empirics/empirics_step06_top_client_address.py`
  - `pdflatex` (2 passes each) on `STEP_00`..`STEP_06` TeX summaries
  - `python3 working/analysis/empirics/overnight_consistency_check.py`

- Maintenance improvements applied:
  - **Step06 figure explanation strengthened** (`working/results/empirics/summaries/STEP_06_top_client_address_profile.tex`)
    - Added explicit caveat in Fig06a note: with very low category cardinality, absolute counts must be reported alongside percentages to avoid over-interpretation.
  - Regenerated affected output:
    - `working/results/empirics/summaries/STEP_06_top_client_address_profile.pdf`

- Repro/consistency checks passed:
  - Figures: `30/30` non-empty PDFs.
  - Tables: `43/43` non-empty CSVs.
  - Reports: `7/7` non-empty summary PDFs.
  - TeX reproducibility preamble coverage: `7/7`.
  - Step02 ordering valid: `0.436736 <= 0.697340 <= 0.717469 <= 1`.
  - Step03 bounds valid: `1470 <= 28418` and `2 <= 571`.
  - Step04 partition valid: `37334 = 37334`.
  - Step05 partition valid: `2782 = 2782`.

- Blockers / mitigations:
  - **Blocker (resolved during run):** checker initially failed with missing files when launched from `working/` (wrong relative base path).
  - **Mitigation applied:** reran `overnight_consistency_check.py` from project root (`workspaces/erc8004-specialist`); all checks passed.
  - **Warning (non-blocking):** matplotlib `Unable to import Axes3D` warning still present.
  - **Mitigation:** workflow remains 2D-only and completed successfully; warning tracked for later environment normalization.

- Run artifacts:
  - Detailed run log: `working/results/empirics/summaries/.overnight_maintenance_20260319_0621.log`
  - Consistency check log: `working/results/empirics/summaries/.overnight_checks_20260319_0621.log`

- Outcome:
  - Overnight maintenance cycle completed successfully.
  - Outputs regenerated in place; edits remained internal and non-destructive.
