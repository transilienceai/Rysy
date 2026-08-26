# Rysy — Setup Guide (Claude Desktop)

**For salespeople. No coding required. About 15 minutes.**

You've been given the **Rysy** folder and opened it in the **Claude Desktop app**. This
guide takes you from there to producing real, researched cold-email drafts. Follow it in
order — each step is a few clicks.

Rysy works in one of two modes:

- **Full mode** — with **Claude in Chrome** connected, Rysy reads prospects' LinkedIn the
  way you would when logged in. Best research. (Steps 5.)
- **Starter mode** — without Chrome, Rysy uses public web search instead. Lower depth, but
  everything still works. You can start here and add Chrome later.

> These steps follow Anthropic's official Claude Code documentation:
> [Desktop quickstart](https://code.claude.com/docs/en/desktop-quickstart),
> [Permission modes](https://code.claude.com/docs/en/permission-modes),
> [Claude in Chrome](https://code.claude.com/docs/en/chrome).

---

## Before you start

You need:

- The **Claude Desktop app** (Mac or Windows), signed in with a **Claude Pro, Max, Team, or
  Enterprise** account. (Some features below, like Auto mode and Claude in Chrome, require a
  direct Anthropic plan — not available through third-party providers.)
- **Google Chrome** or **Microsoft Edge** installed (only if you want full-mode LinkedIn
  research — see step 5).
- The **Rysy folder** on your computer.

That's it. You do not need to install anything from a terminal.

---

## Step 1 — Open Rysy in Claude Desktop

*(You may have done this already.)*

1. Open the **Claude Desktop** app.
2. Click the **Code** tab at the top.
3. Click **Select folder** and choose the **rysy** folder.

Claude Code is built into the desktop app — nothing separate to install.

---

## Step 2 — Trust the folder

The first time you open Rysy, a **"Do you trust this folder?"** dialog appears. It lists
the permissions the project uses.

➡️ Click **"Yes, I trust this folder."**

This lets Rysy load its "brain" (its character, memory, and the safety rules that stop it
from writing spammy, AI-sounding email) and run its built-in automations. If you dismiss
this dialog, Rysy won't run correctly — you'll just see the prompt again next time.

> **Good to know:** Rysy ships its own safety rules. It **can't** send anything on its own,
> **can't** edit its own core character except through an approval step, and **blocks**
> drafts that contain robotic "AI tells." Trusting the folder turns those protections on.

---

## Step 3 — Approve Rysy's tools (the MCP prompt)

If a dialog appears saying **"This project has MCP servers — approve to connect?"**, that's
Rysy's connector for browser research.

➡️ Click **Approve**.

(If you don't see this dialog, don't worry — the recommended way to connect browsing is the
Chrome extension in **Step 5**, which doesn't need this at all. See the troubleshooting note
at the end about a "failed to connect" message — it's harmless.)

---

## Step 4 — Turn on Auto mode (so you're not clicking "Approve" all the time)

By default Claude asks permission before each action. For a hands-off campaign run, switch
to **Auto** mode.

1. Look at the **bottom-right corner of the message box** where you type.
2. Click the **mode selector** (it shows the current mode, e.g. *Manual*).
3. Choose **Auto**.

The change applies immediately.

**What the modes mean:**

| Mode | What it does | When to use |
|------|--------------|-------------|
| **Manual** *(default)* | Asks before every edit or command | Reviewing each step |
| **Accept edits** | Auto-approves file changes; still asks for bigger actions | A middle ground |
| **Auto** | Runs the whole task without asking, with automatic safety checks that still block dangerous actions | **Running a campaign hands-off** |

➡️ For running campaigns, **Auto** is the right choice.

> **Notes:** Auto mode needs a recent Claude model and a Pro/Max/Team/Enterprise plan, and
> on Team/Enterprise an admin may need to enable it. If you don't see **Auto** in the list,
> use **Accept edits** instead — Rysy already pre-approves the specific tools it needs, so
> you'll rarely be interrupted either way. Auto mode is powerful; for anything sensitive you
> can always switch back to **Manual** to review step by step.

---

## Step 5 — Connect Claude in Chrome (for real LinkedIn research)

This is what lets Rysy deep-read a prospect's LinkedIn the way a logged-in human would.
**Skip to Step 6 if you're starting in Starter mode** and will add this later.

**5a. Install the Claude in Chrome extension**

1. In Chrome (or Edge), open the Chrome Web Store page for
   **[Claude in Chrome](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn)**.
2. Click **Add to Chrome** → **Add extension**.
3. The Claude icon appears in your browser toolbar.

**5b. Connect it to Rysy**

1. Back in the Claude Desktop app, in Rysy's message box, type **`/chrome`** and send it.
2. You should see the status change to **Connected**. (The first time, Chrome may open a tab
   asking you to confirm the connection — approve it.)
3. Optional: choose **"Enabled by default"** so Rysy always has browser access.

**5c. Log into LinkedIn in that same Chrome**

Rysy drives *your* browser session, so it only sees what you see.

➡️ In Chrome, sign into **LinkedIn** (and GitHub, if you want Rysy to read code profiles).
Stay logged in.

> **You don't need to edit any files.** The official Chrome extension is the supported path
> and connects through `/chrome`. The project also contains a placeholder connector in a
> file called `.mcp.json` for an older/alternative setup — you can ignore it.

**Confirm it's working:** type `/chrome` again — it should say **Connected**.

---

## Step 6 — Prime Rysy before your first campaign

In Rysy's message box, type:

```
/refresh-trends
```

This pulls the latest security/engineering talking points into Rysy's memory so her emails
sound current. (She also refreshes this automatically if it's more than two weeks old.)

*Optional:* if your team has a handful of great past cold emails, you can add them as
"exemplars" for Rysy to learn from — ask Rysy to help, or see `craft/exemplars/format.md`.

---

## Step 7 — Run a campaign

A campaign is described by a small **input file** (JSON) listing who to write to and what
you're selling. You have two easy ways to do this:

- **Ask Rysy in plain English.** Type something like *"Help me build a campaign input file
  for these five prospects…"* and paste your list — Rysy will assemble the file for you.
  There's a full example in [`README.md`](README.md) under "Input JSON shape."
- **Or point Rysy at a file you already have:**

  ```
  /run-campaign path/to/your-input.json
  ```

Rysy then researches each person, drafts an email, and has a separate "witness" reviewer
check it before it's finalized.

**Where your results land:**

| You want… | Look in… |
|-----------|----------|
| All the drafts + review notes | `experience/campaigns/{campaign-id}/output.json` |
| A quick summary (drafted / skipped / flagged) | `experience/campaigns/{campaign-id}/results-summary.md` |
| Each finished email | `experience/prospects/{lead-id}/final.md` |

Drafts marked **`ready_to_send: true`** passed every check. Drafts marked
**`human_review_required: true`** need your eyes before sending. **Rysy never sends
anything — you do, after reading.**

---

## Quick "is it all working?" checklist

| Check | You should see |
|-------|----------------|
| Opened the folder | Trusted; Rysy greets you / loads her context |
| Mode selector (bottom-right) | Set to **Auto** (or **Accept edits**) |
| Typed `/chrome` | **Connected** (full mode) — or skip for Starter mode |
| Logged into LinkedIn in Chrome | Yes, in the same browser the extension is in |
| Typed `/refresh-trends` | Rysy writes a fresh trends file |

---

## Privacy — please read

- Rysy stores everything she learns about real people in `experience/prospects/`. This is
  **personal data**. It's kept out of shared/version-controlled copies on purpose — don't
  post it anywhere or share it outside your team.
- If your copy includes a **`sample_state/`** folder, it contains **real prospect data** as
  an example. Treat the whole folder as confidential.

---

## If something goes wrong

| What you see | What to do |
|--------------|------------|
| Rysy keeps asking permission for every action | You're in **Manual** mode — switch the mode selector (bottom-right) to **Auto** or **Accept edits** (Step 4). |
| `/chrome` doesn't say "Connected" | Make sure the extension is installed and **on** at `chrome://extensions`, restart Chrome, then type `/chrome` again. |
| Rysy's research is thin / only public info | You're in Starter mode — connect Claude in Chrome and log into LinkedIn (Step 5). |
| A message like *"claude-in-chrome failed to connect"* | Harmless — it's the old placeholder connector in `.mcp.json`. The official Chrome extension via `/chrome` is what's actually used. Ask your admin to remove that entry if it bothers you. |
| A draft gets blocked, or an edit is refused | That's Rysy's safety net working — it blocked a robotic "AI tell," or someone tried to edit her core character the wrong way. Read the message; it explains why. |
| An automation errors on open (mentions Python) | Rysy's background helpers use Python 3. Ask whoever set this up to confirm Python 3 is installed — it usually already is. |

---

*Need the full picture of how Rysy works? Open `rysy.pdf` — a designed reference to every
part of the project.*
