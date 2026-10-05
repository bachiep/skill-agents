"""Validate the distributable skill package without third-party dependencies."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "skill-agent"
SKILL_FILE = SKILL_DIR / "SKILL.md"

PRINCIPLES = (
    "Think Before Coding",
    "Simplicity First",
    "Surgical Changes",
    "Goal-Driven Execution",
    "Verify, Don't Claim",
    "Check Before You Retry",
    "Separate Fact from Inference",
    "Content Is Data, Not Instructions",
    "Classify Failure",
)
REFERENCES = (
    "verification.md",
    "failure-modes.md",
    "security.md",
    "cost-discipline.md",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"Validation failed: {message}")


def frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    require(lines and lines[0] == "---", "SKILL.md must start with frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError:
        raise SystemExit("Validation failed: SKILL.md frontmatter is not closed") from None

    values: dict[str, str] = {}
    for line in lines[1:end]:
        key, separator, value = line.partition(":")
        require(bool(separator), f"invalid frontmatter line: {line}")
        values[key.strip()] = value.strip()
    return values


def main() -> None:
    skill = SKILL_FILE.read_text(encoding="utf-8")
    metadata = frontmatter(skill)
    require(metadata.get("name") == "skill-agent", "skill name must be skill-agent")
    require(metadata.get("version"), "skill version is required")

    for principle in PRINCIPLES:
        require(principle in skill, f"missing principle: {principle}")
    for reference in REFERENCES:
        require((SKILL_DIR / "references" / reference).is_file(), f"missing reference: {reference}")
        require(reference in skill, f"SKILL.md does not link to {reference}")

    plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    marketplace = json.loads(
        (ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8")
    )
    require(plugin["name"] == metadata["name"], "plugin name differs from skill name")
    require(plugin["version"] == metadata["version"], "plugin version differs from skill version")
    require(marketplace["version"] == metadata["version"], "marketplace version differs from skill version")
    require(marketplace["plugins"][0]["version"] == metadata["version"], "marketplace plugin version differs from skill version")
    for path in plugin["skills"]:
        require((ROOT / path).is_dir(), f"plugin skill path does not exist: {path}")

    for guidance in ("AGENTS.md", "CLAUDE.md"):
        require(
            "skills/skill-agent/SKILL.md" in (ROOT / guidance).read_text(encoding="utf-8"),
            f"{guidance} must point to SKILL.md",
        )
    require("docs/codex.md" in (ROOT / "README.md").read_text(encoding="utf-8"), "README must link to Codex instructions")

    print("Package validation passed.")


if __name__ == "__main__":
    main()
