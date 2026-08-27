# [HASH] — The bot gets a house-style icon: white line art with cord striations on the Chagora badge, and sets it as its own avatar

The user confirmed `throughlinerprojectboticon.svg` as the intended line art, which turned the job from a redraw into a recolour-and-composite. Her addition at processing: the spinal cord at the bottom gains a couple of striations — **up-and-down lines running along the cord, not cross-lines**, her correction — to make it more recognisable for what it is meant to be.

The house style, read from Chagora's pair rather than described from memory: flat white stroke-only line art, no fill or shading, on a circular badge with a thin dark rim and a dark diagonal gradient running deep red at the left to desaturated teal-blue at the right, darkening toward the centre. The gradient stops were read out of Chagora's own SVG (`#ba1515` to `#0077a7`) rather than eyeballed from the PNG.

**A description mismatch, recorded rather than halted on.** The item calls this "the wrench-and-pencil figure". The file the user confirmed is a hard hat over a brain with a spinal cord hanging below. The build followed the file, because her striation instruction only makes sense against the art that actually has a cord, and because she had confirmed the file itself. The item's parenthetical is simply wrong about its own subject, and that is worth knowing if the description is ever used to identify the asset.

**A unit trap cost one render and is now on file.** Inkscape's `--query-all` and `--export-area` report and take **pixels**, while path data in this millimetre-based document is in millimetres — a factor of 3.7795. Coordinates read from the query and written into a `d` attribute land off-canvas silently, with no error. The first striation attempt did exactly that. Recorded in `TOOLS.md` so the next vector edit does not repeat it.

**The avatar was set only on an explicit yes**, being an outward-facing change, and confirmed by reading `/users/@me` back: a populated avatar hash where there had been none. The user raised the missing icon herself mid-run, which is how it came up when it did.

Converting the rendered mascot draft was refused at planning and stays refused: a filter cannot turn a shaded illustration into line art.

**Files:** `throughlinerprojectboticon.svg`, `throughliner-icon-badge.png` (created), `TOOLS.md`.

Rule gate: not needed — an artwork change; no rule is authored, amended or repealed.
