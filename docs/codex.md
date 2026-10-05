# Install in Codex

This skill works with Codex's user-level skill discovery. A user-level install makes it available across projects.

## Install

Codex includes the `skill-installer` helper. Run it with the repository path and the actual skill directory:

```sh
python "$CODEX_HOME/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo bachiep/skill-agents \
  --path skills/skill-agent
```

The helper installs the package as `$CODEX_HOME/skills/skill-agent`. If `CODEX_HOME` is not set, Codex normally uses `~/.codex`.

## Verify

Confirm that the installed file has the expected frontmatter:

```sh
head -n 6 "$CODEX_HOME/skills/skill-agent/SKILL.md"
```

It should include `name: skill-agent`. Start a new Codex turn after installation so the skill catalog is refreshed.

## Add the short guidance

Copy the README's **Quick start (30 seconds)** block into your user-level `AGENTS.md` under `## Behavioral Guidelines`. Do this only when an equivalent section is not already present.

## Scope

The skill changes guidance, not the underlying model. Apply its checks in proportion to risk: use a light read-back for a trivial edit, and stronger evidence for irreversible or external actions.
