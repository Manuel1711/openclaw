# RUNBOOK_DISCORD_STABILITY.md

## Objective
Keep Discord (`#general`) responsive and avoid silent message drops.

## Current stable baseline (2026-03-09)
- `channels.discord.groupPolicy = "open"`
- `channels.discord.guilds.1479524789327761582.requireMention = false`
- `channels.discord.guilds.1479524789327761582.channels.1479524789994524897`
  - `enabled = true`
  - `allow = true`
  - `requireMention = false`
  - `ignoreOtherMentions = false`

## Fast health check
1. `openclaw status`
2. `openclaw doctor --non-interactive`
3. `openclaw logs --limit 250 --plain | grep -Ei "discord|WebSocket connection closed|health-monitor|disconnected|no-mention"`

## If messages are dropped
- Confirm no `no-mention` drops in logs.
- Re-apply pinned channel policy above (config patch) if drifted.

## If Discord feels slow
Likely causes:
- Discord websocket reconnect events (transport-level).
- Oversized channel session context (high token load).

Action:
1. Backup `~/.openclaw/agents/main/sessions/sessions.json`
2. Remove bloated channel keys for `#general` from session store.
3. `gateway.restart`
4. Re-test in `#general` with a ping message.

## Residual risk
Intermittent websocket close code `1005` may still appear (network/transport path). Policy fixes prevent drops, but cannot guarantee zero disconnect events.
