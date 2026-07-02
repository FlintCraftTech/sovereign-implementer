---
hooks:
  - event: session.created
    actions:
      - bash:
          command: "node .opencode/plugin/si-plugin/src/session-start.js"
          timeout: 15000

  - event: tool.before.*
    conditions: [isMainSession]
    actions:
      - bash:
          command: "node .opencode/plugin/si-plugin/src/pre-tool-use.js"
          timeout: 10000

  - event: tool.after.write
    actions:
      - bash:
          command: "node .opencode/plugin/si-plugin/src/post-tool-use.js"
          timeout: 5000
---
