# Quick start

1. Install a complete skill directory using the README instructions. Standard skill metadata follows [Agent Skills](https://agentskills.io/specification). Codex local installs can use `.agents/skills/<name>/`; Claude Code project installs use `.claude/skills/<name>/`. Check your agent version's directory support. No global configuration change is required.
2. In a fresh chat invoke `$skill-name` in Codex or `/skill-name` in Claude Code, replacing the name with the installed skill. You can also describe the task naturally; explicit invocation is easiest to verify.
3. Paste your task and evidence. Define the offer, buyer, geography if known, and whether this is a main business or side hustle. State time/cash constraints that matter.
4. Review the result and its source limitations. If current sources are unavailable, keep the result provisional. Ask for a full analysis when the additional evidence could change the decision.

## Dependencies and isolation

No script runtime is needed. Browsing is needed only for claims requiring current verification. Spreadsheet output is optional.

Keep user records outside the installed skill and source repository. When testing an upgrade, copy into a disposable project and avoid overwriting an existing customized install. Examples are fictional, not client claims. See [validation](VALIDATION.md) for observed support rather than assuming every Agent Skills consumer was tested.
