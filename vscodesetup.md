# Weekly Setup Guide — New Notebook/File in an Existing Course Repo

Use this every time you sit down to start a new week's work, assuming your computer was fully restarted and nothing is open.

---

## Step 1: Open VS Code into the right repo folder

- Launch VS Code
- File → Open Folder → select the specific course's repo folder (not a parent folder)
- Confirm bottom-left corner shows **WSL: Ubuntu** — this means you're in the Linux filesystem, not Windows

*Why:* VS Code needs to be opened at the repo root to correctly detect git and any project files.

---

## Step 2: Open a terminal and confirm you're in the right place

```bash
pwd
```
*Why:* Confirms your working directory matches the repo you intend to work in — especially important since you're juggling three separate repos.

---

## Step 3: Pull the latest changes

```bash
git status
```
*Why:* Shows whether you're behind the remote or have any leftover uncommitted changes from last time, before you touch anything.

```bash
git pull
```
*Why:* Downloads and merges any updates from GitHub — course materials, instructor files, or anything pushed from another machine — into your local copy.

---

## Step 4: Activate your virtual environment

```bash
source ~/.venv/bin/activate
```
*Why:* Switches your terminal into the isolated Python environment with your installed packages. Your prompt should now show `(.venv)`.

---

## Step 5: Create the new folder/notebook for this week

```bash
mkdir week3
cd week3
```
*Why:* Keeps each week's work organized in its own folder within the course repo.

- Create the new `.ipynb` file inside this folder (via VS Code's file explorer, or Command Palette → "Create: New Jupyter Notebook")

---

## Step 6: Select the correct kernel

- Open the new notebook
- Click the kernel picker (top-right)
- Choose the interpreter pointing to `/home/marty/.venv/bin/python`

*Why:* Ensures the notebook runs using your venv's packages, not a system Python.

*(Optional sanity check — run once in a cell):*
```python
import sys
print(sys.executable)
```

---

## Step 7: Pull in any relevant files (if applicable)

- If the instructor has posted new datasets, starter code, or assignment files to the repo, they should already be present after your `git pull` in Step 3
- If you're adding files manually (e.g., a dataset downloaded from a course portal), place them in the `week3` folder now

---

## Step 8: Stage and commit the new files early

```bash
git add .
git commit -m "Add week 3 folder and starter notebook"
git push
```
*Why:* Getting the new file structure onto GitHub early means you have a safe checkpoint even before you've done any actual work — useful in case anything goes wrong later in the session.

- `git add .` — stages all new/changed files, telling git "include these in the next commit"
- `git commit -m "..."` — saves a labeled snapshot of the staged changes to your local history
- `git push` — uploads your local commits to GitHub

---

## Step 9: Do the actual work

- Work through the assignment: notes, code, running cells
- **Save often** (Ctrl+S) — running a cell does *not* save the notebook file to disk; only Ctrl+S does

*(If you need a new package mid-session):*
```bash
pip install <package-name>
pip freeze > requirements.txt
```
*Why:* Installs the package into your active venv, then updates the requirements file so the repo reflects what your project actually depends on.

---

## Step 10: End-of-day commit and push

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
| `git status` | Shows what's changed and whether you're synced with GitHub |
| `git pull` | Downloads and merges the latest version from GitHub |
| `git add .` | Marks changed/new files to be included in the next commit |
| `git commit -m "..."` | Saves a labeled snapshot of staged changes locally |
| `git push` | Uploads local commits to GitHub |

---

## One habit to build in: repeat Steps 1–4 for *each* course repo separately

Since you have three separate repos, each one needs its own `cd`, `git pull`, and venv activation in its own terminal session (or one at a time in the same terminal, moving folder to folder) — git and your venv operate per-folder, not globally across all three courses at once.