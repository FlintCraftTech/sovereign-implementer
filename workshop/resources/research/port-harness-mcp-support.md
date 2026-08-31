# MCP support in the port harnesses — OpenCode and Kilo Code both run local MCP servers natively

Searched 2026-08-31, prompted by the user's portability concern on [mcp-server-standing-intent]: would a Throughliner MCP server make the method less portable to the harnesses people are actually porting to? The two live ports in the Discord port-showcase (both by Egnatia-OC) target OpenCode and Kilo Code.

**OpenCode:** supports local (stdio) and remote (HTTP) MCP servers via its `opencode.json` — a local server is a command OpenCode starts itself, declared as `"type": "local"` with a command array, configurable globally or per project. Sources: [OpenCode MCP servers doc](https://opencode.ai/v2/docs/mcp-servers), [MCP.Directory client guide](https://mcp.directory/clients/opencode), [setup guide](https://ayodele.dev/blog/mcp-opencode-setup).

**Kilo Code:** the Kilo CLI supports local and remote MCP servers under the `mcp` key of `kilo.jsonc`, local via stdio, global or project-level, with a settings UI for managing them in the editor. Sources: [Using MCP in CLI](https://kilo.ai/docs/automate/mcp/using-in-cli), [Using MCP in Kilo Code](https://kilo.ai/docs/automate/mcp/using-in-kilo-code).

**What this settles:** a local, stdio Throughliner MCP server would be attachable to both known port harnesses through their own supported configuration — unlike the hooks, which each port must re-map by hand onto its harness's events. The portability cost of MCP therefore falls on harnesses without MCP support (none currently among the live ports) and on the added moving part a porter must understand, not on the two ports that exist.

**What this does not settle:** whether the ports' authors want the component; whether Kilo/OpenCode's tool-permission models match what the method's approval rules assume; version details of either harness's MCP implementation. Read from vendor docs, not tested against either harness.

**Frame validity (five criteria):**
- TIME RANGE: current vendor documentation, read 2026-08-31; the product decision it informs is near-term.
- PEOPLE: applies to porters running OpenCode/Kilo Code — the two known port authors' harnesses, confirmed from the port-showcase channel.
- FRESHNESS: harness config surfaces change often; re-verify at design time if months pass.
- RISK IF WRONG: a design premised on this would stumble at a port's integration step, visibly and cheaply — no exposure; re-check at build rather than a red flag.
- ALTERNATIVES: not applicable — the question was a capability fact, not an approach choice.
