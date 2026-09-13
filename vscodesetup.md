# Course Repo Workflow Guide

Covers everything from connecting to a brand-new course repo for the first time, through the recurring weekly routine, plus a troubleshooting appendix for issues you're likely to hit again.

---

## Part 1: One-Time Setup — Cloning a Course Repo for the First Time

Do this once per course, the very first time you touch that repo on this machine.

### Step 1: Navigate to where you want the repo to live

```bash
cd ~
```
*Why:* Keeps all course repos as siblings directly under your home folder, consistent with your existing setup.

### Step 2: Clone the repo

```bash
git clone <repo-url> <folder-name>
```
Example:
```bash
git clone git@github.com:iviartin/mba-f743-big-data-finance-26.git F743-BigData
```
*Why:* `git clone` downloads the entire repo and creates the local folder for you — this is the correct command for connecting to a repo for the first time. **Not** `git pull`, which only works on a repo you've already cloned.

Specifying `<folder-name>` explicitly (rather than leaving it blank) means the folder is named however you want — otherwise git defaults to naming it after the exact GitHub repo name, which can be long and inconsistent with your other course folders.

*Note:* If prompted for your SSH key passphrase during the clone, that's expected — not an error. Type it and press Enter.

### Step 3: Confirm the clone worked

```bash
cd <folder-name>
git status
```
*Why:* Should report you're on `main` and up to date with `origin` — confirms the repo is correctly connected before you build anything on top of it.

---

## Part 2: Weekly Workflow (Repeat Every Session)

Use this every time you sit down to start a new week's work in a course whose repo is already cloned, assuming your computer was fully restarted and nothing is open.

### Step 1: Open VS Code into the right repo folder

- Launch VS Code
- File → Open Folder → select the specific course's repo folder (not a parent folder)
- Confirm bottom-left corner shows **WSL: Ubuntu** — this means you're in the Linux filesystem, not Windows

*Why:* VS Code needs to be opened at the repo root to correctly detect git and any project files.

### Step 2: Open a terminal and confirm you're in the right place

```bash
pwd
```
*Why:* Confirms your working directory matches the repo you intend to work in — especially important since you're juggling three separate repos.

### Step 3: Pull the latest changes

```bash
git status
```
*Why:* Shows whether you're behind the remote or have any leftover uncommitted changes from last time, before you touch anything.

```bash
git pull
```
*Why:* Downloads and merges any updates from GitHub — course materials, instructor files, or anything pushed from another machine — into your local copy.

### Step 4: Activate your virtual environment

```bash
source ~/.venv/bin/activate
```
*Why:* Switches your terminal into the isolated Python environment with your installed packages. Your prompt should now show `(.venv)`.

### Step 5: Create the new folder/notebook for this week

```bash
mkdir week3
cd week3
```
*Why:* Keeps each week's work organized in its own folder within the course repo.

- Create the new `.ipynb` file inside this folder (via VS Code's file explorer, or Command Palette → "Create: New Jupyter Notebook")

### Step 6: Select the correct kernel

- Open the new notebook
- Click the kernel picker (top-right)
- Choose the interpreter pointing to `/home/marty/.venv/bin/python`

*Why:* Ensures the notebook runs using your venv's packages, not a system Python.

*(Optional sanity check — run once in a cell):*
```python
import sys
print(sys.executable)
```

### Step 7: Pull in any relevant files (if applicable)

- If the instructor has posted new datasets, starter code, or assignment files to the repo, they should already be present after your `git pull` in Step 3
- If you're adding files manually (e.g., a dataset downloaded from a course portal), place them in the `week3` folder now

### Step 8: Stage and commit the new files early

```bash
git add .
git commit -m "Add week 3 folder and starter notebook"
git push
```
*Why:* Getting the new file structure onto GitHub early means you have a safe checkpoint even before you've done any actual work.

- `git add .` — stages all new/changed files, telling git "include these in the next commit"
- `git commit -m "..."` — saves a labeled snapshot of the staged changes to your local history
- `git push` — uploads your local commits to GitHub

### Step 9: Do the actual work

- Work through the assignment: notes, code, running cells
- **Save often** (Ctrl+S) — running a cell does *not* save the notebook file to disk; only Ctrl+S does

*(If you need a new package mid-session):*
```bash
pip install <package-name>
pip freeze > requirements.txt
```
*Why:* Installs the package into your active venv, then updates the requirements file so the repo reflects what your project actually depends on.

### Step 10: End-of-day commit and push

```bash
git status
```
*Why:* Shows exactly what's changed since your last commit — good habit before staging, so nothing gets committed by accident.

```bash
git add .
git commit -m "Week 3: completed [assignment name] notes and exercises"
git push
```
*Why:* Same three-step cycle as Step 8 — stage, snapshot, upload — this time capturing the actual work you did.

---

## Quick reference — what each git command does

| Command | What it does |
|---|---|
| `git clone <url> <folder>` | Downloads a repo for the first time and creates the local folder |
| `git status` | Shows what's changed and whether you're synced with GitHub |
| `git pull` | Downloads and merges the latest version from GitHub (repo must already be cloned) |
| `git add .` | Marks changed/new files to be included in the next commit |
| `git commit -m "..."` | Saves a labeled snapshot of staged changes locally |
| `git push` | Uploads local commits to GitHub |

---

## One habit to build in: repeat per repo

Since you have three separate repos, each one needs its own `cd`, `git pull`, and venv activation in its own terminal session (or one at a time in the same terminal, moving folder to folder) — git and your venv operate per-folder, not globally across all three courses at once.

---

## Appendix A: One-Time Machine Setup — Git Identity

If you ever see this error on a fresh machine or environment:
```
Author identity unknown
*** Please tell me who you are.
```

Set your identity once, globally — it then applies to every repo on the machine, not just the one you're in:
```bash
git config --global user.name "iviartin"
git config --global user.email "mramirez@laurentian.ca"
```

**Why this can seem to appear out of nowhere:** if you've previously only committed through VS Code's Source Control panel (rather than the raw terminal), VS Code can attach your identity from your signed-in GitHub account without ever writing it to any of the config files git normally checks (`~/.gitconfig`, `~/.config/git/config`, `/etc/gitconfig`). The identity is real and your commits are valid — it's just invisible outside VS Code. Running raw `git commit` from the terminal is what surfaces the gap, since the terminal has no such fallback.

---

## Appendix B: Fixing Folder/Rename Mistakes

**Rule of thumb:** rename or move repo folders using the terminal (`mv`), never Windows Explorer drag-and-drop.

*Why:* Explorer hides dotfiles/dotfolders (including `.git`) by default. Dragging visible contents into a new folder can leave `.git` behind, orphaned in the old location, or nested one level too deep — the repo silently stops being recognized as a repo.

**If `git status` suddenly returns `fatal: not a git repository`:**

1. Locate where `.git` actually is:
```bash
find ~ -maxdepth 3 -iname ".git" -type d
```

2. Depending on what turns up:

   - **`.git` orphaned alone in the old folder** — move it into the correct location:
     ```bash
     mv ~/old-folder-name/.git ~/correct-folder-name/.git
     rmdir ~/old-folder-name
     ```

   - **Repo nested one level too deep** (e.g., `~/CourseFolder/repo-name/.git` instead of `~/CourseFolder/.git`):
     ```bash
     mv ~/CourseFolder ~/CourseFolder-temp
     mv ~/CourseFolder-temp/repo-name ~/CourseFolder
     rmdir ~/CourseFolder-temp
     ```

   - **Genuinely gone** — simplest fix is re-cloning fresh (see Part 1), since nothing is lost as long as everything was already pushed.

3. Confirm the fix:
```bash
cd ~/correct-folder-name
git status
ls -la
```

---

## Appendix C: Terminal Troubleshooting Quick Reference

**Terminal stuck showing a `>` prompt and won't accept new commands**
Usually caused by an unmatched quote or backtick left open in a previous command.
- Press `Ctrl+C` to abandon the incomplete command and return to a clean prompt.

**Need to clear terminal clutter from a big paste**
- `Ctrl+U` — clears the current input line
- `Ctrl+L` or `clear` — clears the visible screen (scrollback history stays intact)

**A commit opens nano (or another unfamiliar text editor) instead of a message prompt you expect**
This happens when running `git commit` without `-m`, causing git to fall back to the system default editor.
- To exit nano without committing: `Ctrl+X`, then `N` if asked to save
- To make VS Code open instead of nano going forward:
  ```bash
  git config --global core.editor "code --wait"
  ```
- Simplest fix: just always include the message inline to skip the editor step entirely:
  ```bash
  git commit -m "your message here"
  ```