# Dalil (دليل) 🧭

> **لكل رحلة دليل**
> From your first line of code to your first job.

Dalil is a Discord bot for a student community with three batches (C, Python, and a third track) plus graduates. Whether you're fighting a segfault, debugging Python, or job hunting after graduation, Dalil helps you get unstuck, stay motivated, and learn from people who've been there.

**Status:** early development. Built by a student, for students.

---

## Who it's for

| Group | What Dalil gives them |
| --- | --- |
| **C batch** | Error explanations, debugging help, daily challenges in C |
| **Python batch** | The same tools, in Python |
| **Third batch** | The same tools for their track |
| **Graduates** | A way to mentor, share their journey, and find resources for life after the program |

---

## Commands

### Available now

| Command | What it does |
| --- | --- |
| `/ping` | Checks that Dalil is awake and shows the response time |
| `/about` | Explains what Dalil is |

### Coming soon

See the [roadmap](#roadmap) below.

---

## Roadmap

### Phase 1: Foundation
- [x] Bot online in a private test server
- [x] `/ping` and `/about`
- [x] Public repo with MIT license
- [ ] `/tip`: a random study or coding tip
- [ ] `/duck`: rubber duck debugging; the bot asks guiding questions so you find the bug yourself
- [ ] `/help`: lists every command and what it does

### Phase 2: Batches and graduates
- [ ] `/batch`: pick your batch (C, Python, third track) or Graduate and get a role
- [ ] `/resources`: interview prep, CV tips, and job boards for graduates
- [ ] `/tip` upgrade: graduates submit tips with `/add-tip`, and a moderator approves them

### Phase 3: Getting unstuck (without giving answers)
- [ ] `/explain-error`: paste an error like `segmentation fault` or `IndentationError` and get a plain explanation of what it usually means
- [ ] `/git-oops`: fixes for common git mistakes, like committing to the wrong branch
- [ ] `/duck` upgrade: private thread, and you can type your problem into the command

### Phase 4: Community and fun
- [ ] `/challenge`: a daily mini puzzle in your track's language, with streaks
- [ ] `/duel @someone`: race a friend to solve the same small puzzle
- [ ] Batch vs batch: points from challenges and helping others go into a monthly leaderboard
- [ ] `/bug-of-the-week`: share your funniest or most painful bug, and the server votes
- [ ] `/focus 25`: a group study session that pings everyone when time is up

### Phase 5: Mentorship
- [ ] `/mentor`: matches a student with a graduate from their track who signed up to help
- [ ] `/journey`: graduates share how they got their first job; students browse by track

### Phase 6: Launch
- [ ] Test with a few classmates and collect feedback
- [ ] Host Dalil 24/7 on a small server, with auto-restart if it crashes
- [ ] Pitch to the server admins with a live demo
- [ ] Move from test-server commands to the real server

### Ideas for later
These might come back once the core is done:
- `/deadlines`: each batch's upcoming deadlines
- `/docs`: look up C man pages or Python docs
- `/ask` + `/next`: a peer-help queue

---

## Project rules

Dalil follows these rules so it's safe for any server to accept:

- **No project solutions.** Dalil never shares answers to program projects or tasks. It helps people learn, not copy.
- **Minimal permissions.** Dalil never asks for Administrator. It only requests what its commands need.
- **Slash commands only.** Dalil doesn't read people's messages.
- **No unnecessary data.** It stores only what a feature needs, like challenge streaks or points.
- **Secrets stay secret.** The bot token lives in `.env`, which is never committed.

---

## Running Dalil yourself

### Requirements
- Python 3.10 or newer
- A Discord account and a test server you own

### 1. Create the bot
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create a new application.
2. In the **Bot** tab, click **Reset Token** and copy it.
3. In **OAuth2 → URL Generator**, tick the `bot` and `applications.commands` scopes, plus the **Send Messages** and **Embed Links** permissions.
4. Open the generated URL and invite the bot to your test server.

### 2. Set up the project
```bash
git clone https://github.com/O1Wg/dalil.git
cd dalil
python -m venv venv
```

Activate the virtual environment:
- **Git Bash on Windows:** `source venv/Scripts/activate`
- **Windows Command Prompt:** `venv\Scripts\activate`
- **macOS or Linux:** `source venv/bin/activate`

Install the packages:
```bash
pip install -r requirements.txt
```

### 3. Add your secrets
Copy `.env.example` to `.env` and fill in your values:
```
DISCORD_TOKEN=your-token-here
GUILD_ID=your-server-id-here
```
To get the server ID, turn on **Developer Mode** in Discord (User Settings → Advanced), then right-click your server and choose **Copy Server ID**.

### 4. Run it
```bash
python bot.py
```
When you see `Logged in as ...`, type `/ping` in your server.

---

## Project structure

```
dalil/
├── bot.py             # The bot and its commands
├── requirements.txt   # Python packages
├── .env.example       # Template for your secrets
├── .gitignore         # Keeps .env and venv/ out of git
├── LICENSE            # MIT
└── README.md          # You are here
```

---

## Contributing

Ideas and help are welcome, especially from students and graduates in the community.

1. Open an issue describing the command or fix you have in mind.
2. Build and test it in your own test server.
3. Open a pull request with one feature at a time.

Please follow the [project rules](#project-rules), especially: no project solutions.

---

## License

[MIT](LICENSE)
Built by [@O1Wg](https://github.com/O1Wg), a student, for students.
