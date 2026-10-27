# Visual companion: restore as an opt-in aid

## Observation

- Crucible dropped upstream's visual companion when it ported
  brainstorming, because the maintainer did not use it, and upstream's form
  is a Node server with a usage ping to strip.
- Upstream's brainstorming offers it just in time and opt-in ("If no
  visual question ever arises, never offer it"); its
  `superpowers/skills/brainstorming/visual-companion.md` handles Windows,
  and its scripts are a zero-dependency Node server.
- Upstream's companion loads its logo from Prime Radiant's site, carrying
  the superpowers version, as an opt-out usage ping (upstream's README
  § Visual companion telemetry;
  `superpowers/skills/brainstorming/scripts/server.cjs`; opt-out via
  `SUPERPOWERS_DISABLE_TELEMETRY`).
- For a general builder tool, UI and layout questions are central.

## Follow-up

- The proposed direction: offered just in time as upstream does, the agent
  writes a self-contained HTML mockup into the gitignored workspace and
  opens it; the user answers in the terminal; no server, no dependency, no
  ping.
- Consider host-native visual surfaces as an alternative (a
  runtime-adapter question).
