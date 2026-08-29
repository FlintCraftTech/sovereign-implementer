# [HASH] — plan — the outbound register gets a deletion guard rather than being un-ignored, and the red flag clears by design

A consumer project reported that `INBOX/sent.md` — the permanent record of everything sent or posted — sits inside a gitignored folder, so it has no history and one deletion ends it. It arrived carrying an uncleared red flag, and was the session's first item on that ground.

**Reading the folder turned up what the report did not have, and it narrowed the fix.** The two files in there have opposite exposure profiles: the register holds no absolute paths at all and names only projects that are already public, while the address book beside it holds paths identifying the user and her machine, and one entry naming a real person alongside a sensitive matter. So the blanket ignore is wrong for one file and load-bearing for the other — which rules out any folder-level change.

**The severity was also lower than reported.** Most register lines point at LOG entries carrying the posted text verbatim, and `LOG/` is tracked, so what a post claimed survives in committed history. What would be lost is the index the repeal-grep runs over.

**The user declined publication**, asked directly, so the tracked-register route died there. What was kept instead is a guard in `pre_tool_use.py` refusing to delete or truncate the register, in the same shape as the existing guard against overwriting a session record.

**Red flag cleared by design, with the residual stated and accepted:** it stops a session or a script destroying the file, which is the failure reported. It does nothing about the folder being deleted by hand or a disk failing, because a hook only sees what goes through Claude's tools.

**Queue changes:** [sent-register-untracked] kept and cleared; its red flag moved to `State: cleared`.
**Work processed:** kept — [sent-register-untracked].
