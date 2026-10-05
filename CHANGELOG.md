# Changelog

All notable changes to the skill-agent skill are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added
- GitHub Actions package validation for the skill frontmatter, all nine principles, references, manifests, versions, and guidance links.
- Codex user-level installation and verification guide.
- Lightweight evaluation scenarios and an evidence-based review rubric.

## [0.2.0] - 2026-10-06

### Added
- Two-tier structure: Tier 1 (Core, Karpathy's four) and Tier 2 (Advanced, five new principles). Tier 1 alone is a complete starting point.
- `references/cost-discipline.md` — when verification is worth its cost: the tradeoff matrix, the question budget, and over-application as a failure mode.
- `EXAMPLES.md`: new examples for Principle 1 (think before coding), Principle 4 (goal-driven execution), and Principle 10 (over-application). Added a provenance note distinguishing reported cases from illustrative ones.
- README: 30-second copy-paste quick start, and a "Limitations" section stating honestly what this guidance can and cannot do.

### Changed
- Softened unevidenced claims ("the most expensive failures are...") to experience-framed statements.
- README credits now attribute the adapted real-world examples.

## [0.1.0] - 2026-10-06

### Added
- Initial release: nine operating principles with falsifiable tests.
- `references/verification.md` — the evidence ladder (no check → exit code → output inspection → state check → independent corroboration).
- `references/failure-modes.md` — failed / blocked / unknown taxonomy and safe retry patterns.
- `references/security.md` — untrusted content, permission boundaries, secrets handling.
- `EXAMPLES.md` — seven concrete before/after pairs.
- Distribution: Claude Code plugin manifest, Cursor rule, `CLAUDE.md` / `AGENTS.md` pointers.
