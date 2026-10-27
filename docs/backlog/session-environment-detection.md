# Coexisting routers and headless sessions: detect and warn

## Observation

- **Coexistence.** The most likely adopter is a superpowers user. The
  README and `docs/codex.md` say never to run two routers in one session,
  but nothing detects it, and skill names collide across namespaces
  (brainstorming, writing-plans, …). A plugin cannot suppress another
  plugin's hook, but it can detect and warn: the router can say "if
  using-superpowers is also in context, stop and ask the user to disable
  one", or the SessionStart hook can read `enabledPlugins` from the user
  and project settings (fragile, since the hook is a bash script with no
  JSON parser; unverified). The maintainer: "maybe — we kind of can't
  suppress the superpowers router?"
- **Headless.** The hook fires on every startup, clear and compact and
  routes feature work into brainstorming and decision asks that a
  `claude -p`, CI or SDK session cannot answer; the router's
  `SUBAGENT-STOP` block covers only dispatched subagents. An SDK caller can
  avoid this by loading no plugins (`setting_sources=[]`). Partly
  addressable: a README note, plus, if the host exposes a non-interactive
  signal to SessionStart (unverified), a neutral injection. The maintainer: "legacy, I'd expect not addressable?"

## Follow-up

- A router line that detects a second router and stops.
- Probe what SessionStart input or environment distinguishes
  non-interactive sessions; otherwise document "disable crucible for
  headless use" in the README.
