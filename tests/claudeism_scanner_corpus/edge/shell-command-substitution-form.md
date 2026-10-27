# Shell-only entrypoint, command-substitution form

The same entrypoint inside a substitution. No plain invocation appears in
this file, so only the substitution forms can match.

```
PACKAGE=$(bash <plugin-root>/skills/subagent-driven-development/scripts/review-package <feature-slug> BASE HEAD)
BRIEF=`bash <plugin-root>/skills/subagent-driven-development/scripts/task-brief <feature-slug> PLAN_FILE N`
```
