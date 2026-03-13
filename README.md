# 🤖 Telegram Gay Counter Bot

Posts a message every time someone joins your channel/group:
> На каналі **{chat.title}** нарахували **{count}** геїв

## 📁 Files
```
bot.py               ← main bot code
requirements.txt     ← dependencies
.github/workflows/bot.yml  ← GitHub Actions runner
```

---

## 🚀 Setup (Free, No Server)

### Step 1 — Create your bot
1. Open Telegram → talk to [@BotFather](https://t.me/BotFather)
2. Send `/newbot`, follow the steps
3. Copy your **BOT_TOKEN**

### Step 2 — Add bot to your channel/group
1. Add the bot as **Admin** to your channel or group
2. Give it permission to **read messages** and **post messages**
3. ⚠️ For channels: go to channel settings → Administrators → Add bot

### Step 3 — Enable "Chat Member Updates" (important!)
In BotFather:
1. Send `/mybots` → select your bot
2. Go to **Bot Settings → Group Privacy → Turn OFF**
   (So the bot can see member join events)

### Step 4 — Push to GitHub
1. Create a new GitHub repository
2. Upload all files (`bot.py`, `requirements.txt`, `.github/workflows/bot.yml`)
3. Go to **Settings → Secrets → Actions**
4. Add a new secret:
   - Name: `BOT_TOKEN`
   - Value: your token from BotFather

### Step 5 — Run it
- Go to **Actions tab** in your GitHub repo
- Click **"Run Telegram Bot"** → **"Run workflow"**
- The bot will start and stay alive until GitHub kills it (~6 hours max per run)

### 🔁 To keep it running longer
Add this to `bot.yml` to auto-restart every 5 hours:
```yaml
on:
  schedule:
    - cron: '0 */5 * * *'  # every 5 hours
  workflow_dispatch:
  push:
    branches: [main]
```

---

## ⚠️ Limitations of free GitHub Actions hosting
| Limit | Value |
|-------|-------|
| Free minutes/month | 2,000 min |
| Max job duration | 6 hours |
| Restarts needed | Every ~5h via cron |

For a truly always-on free option, consider **Railway.app** or **Render.com** free tiers instead.
