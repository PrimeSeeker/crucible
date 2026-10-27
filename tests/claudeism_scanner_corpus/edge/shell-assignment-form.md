# Shell-only entrypoint, assignment form

The entrypoint bound to a variable instead of run inline. No plain
invocation appears in this file, so only the assignment form can match.

```
PACKAGE_CMD="bash <plugin-root>/skills/subagent-driven-development/scripts/review-package"
$PACKAGE_CMD <feature-slug> BASE HEAD
```
