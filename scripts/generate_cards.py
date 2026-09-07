#!/usr/bin/env python3
"""Render contribution + language cards for the profile README.

Writes light and dark SVGs to assets/. No third-party image services: the data
comes from the GitHub API and the SVG is drawn here, so the profile never shows
a broken card because someone else's Vercel quota ran out.
"""
import json, os, sys, urllib.request, datetime
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

USER = os.environ.get("CARD_USER", "petrasvestartas")
TOK = os.environ["GH_TOKEN"]
OUT = os.environ.get("CARD_OUT", "assets")
FONT = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"

THEMES = {
    "light": dict(bg="#ffffff", border="#d1d9e0", fg="#1f2328", muted="#59636e",
                  scale=["#ebedf0", "#aceebb", "#4ac26b", "#2da44e", "#116329"]),
    "dark":  dict(bg="#0d1117", border="#3d444d", fg="#f0f6fc", muted="#9198a1",
                  scale=["#151b23", "#033a16", "#196c2e", "#2ea043", "#56d364"]),
}
# linguist colours
LANG_COLOR = {"Rust": "#dea584", "C++": "#f34b7d", "C#": "#178600", "Python": "#3572A5",
              "WGSL": "#1a5799", "C": "#555555", "CMake": "#DA3434", "Vue": "#41b883",
              "JavaScript": "#f1e05a", "Shell": "#89e051", "HTML": "#e34c26", "CSS": "#663399"}
OTHER = "#8b949e"
CARD_W = 840


def api(url):
    r = urllib.request.Request(url, headers={"Authorization": f"Bearer {TOK}",
                                             "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(r, timeout=40) as x:
        return json.load(x)


def gql(query, variables):
    r = urllib.request.Request("https://api.github.com/graphql",
        data=json.dumps({"query": query, "variables": variables}).encode(),
        headers={"Authorization": f"Bearer {TOK}", "Content-Type": "application/json"})
    with urllib.request.urlopen(r, timeout=40) as x:
        body = json.load(x)
    if "errors" in body:
        sys.exit("GraphQL: " + json.dumps(body["errors"]))
    return body["data"]


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def fetch():
    q = """
    query($login:String!){
      user(login:$login){
        followers{totalCount}
        contributionsCollection{
          totalCommitContributions totalPullRequestContributions
          totalRepositoriesWithContributedCommits
          contributionCalendar{ totalContributions
            weeks{ firstDay contributionDays{ date contributionCount weekday } } }
        }
        repositories(first:100, ownerAffiliations:OWNER, isFork:false, privacy:PUBLIC){
          totalCount nodes{ nameWithOwner stargazerCount }
        }
      }
    }"""
    u = gql(q, {"login": USER})["user"]

    names = [r["nameWithOwner"] for r in u["repositories"]["nodes"]]
    def langs(full):
        try:
            return Counter(api(f"https://api.github.com/repos/{full}/languages"))
        except Exception:
            return Counter()
    with ThreadPoolExecutor(max_workers=12) as ex:
        totals = sum(ex.map(langs, names), Counter())

    return dict(
        weeks=u["contributionsCollection"]["contributionCalendar"]["weeks"],
        total=u["contributionsCollection"]["contributionCalendar"]["totalContributions"],
        commits=u["contributionsCollection"]["totalCommitContributions"],
        prs=u["contributionsCollection"]["totalPullRequestContributions"],
        active_repos=u["contributionsCollection"]["totalRepositoriesWithContributedCommits"],
        repos=u["repositories"]["totalCount"],
        stars=sum(r["stargazerCount"] for r in u["repositories"]["nodes"]),
        followers=u["followers"]["totalCount"],
        langs=totals,
    )


def frame(w, h, t, title, sub):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" role="img" aria-label="{esc(title)} — {esc(sub)}">'
            f'<g font-family="{FONT}">'
            f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="10" '
            f'fill="{t["bg"]}" stroke="{t["border"]}"/>'
            f'<text x="20" y="32" fill="{t["fg"]}" font-size="15" font-weight="600">{esc(title)}</text>'
            f'<text x="{w-20}" y="32" fill="{t["muted"]}" font-size="12.5" text-anchor="end">{esc(sub)}</text>')


def contributions_card(d, t):
    weeks, cell, gap, pad, top = d["weeks"], 11, 3, 20, 62
    step = cell + gap
    w = CARD_W
    grid = len(weeks) * step - gap
    left = (w - grid + 26) // 2          # centre the grid, leaving room for weekday labels
    h = top + 7 * step + 46

    # Quartiles of *active* days, not a linear split of the maximum: one 181-commit
    # day would otherwise flatten every other day into the same shade.
    active = sorted(x["contributionCount"] for wk in weeks
                    for x in wk["contributionDays"] if x["contributionCount"])
    qs = [active[min(len(active) - 1, int(len(active) * f))] for f in (0.25, 0.5, 0.75)] if active else [1, 1, 1]
    def bucket(n):
        if n == 0: return 0
        return 1 + sum(n > q for q in qs)

    s = [frame(w, h, t, "Contributions", f'{d["total"]:,} in the last year')]

    seen = set()
    for i, wk in enumerate(weeks):
        m = datetime.date.fromisoformat(wk["firstDay"])
        if m.day <= 7 and m.month not in seen:
            seen.add(m.month)
            s.append(f'<text x="{left + i*step}" y="{top - 6}" fill="{t["muted"]}" '
                     f'font-size="10.5">{m.strftime("%b")}</text>')
    for row, lab in ((1, "Mon"), (3, "Wed"), (5, "Fri")):
        s.append(f'<text x="{pad}" y="{top + row*step + 9}" fill="{t["muted"]}" font-size="10.5">{lab}</text>')

    for i, wk in enumerate(weeks):
        for day in wk["contributionDays"]:
            x, y = left + i * step, top + day["weekday"] * step
            s.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="2.5" '
                     f'fill="{t["scale"][bucket(day["contributionCount"])]}"/>')

    ly = top + 7 * step + 22
    s.append(f'<text x="{pad}" y="{ly+9}" fill="{t["muted"]}" font-size="11">'
             f'{d["commits"]:,} commits · {d["prs"]} pull requests · {d["active_repos"]} repositories</text>')
    lx = w - pad - (5 * step + 62)
    s.append(f'<text x="{lx}" y="{ly+9}" fill="{t["muted"]}" font-size="11">Less</text>')
    for i, c in enumerate(t["scale"]):
        s.append(f'<rect x="{lx + 32 + i*step}" y="{ly}" width="{cell}" height="{cell}" rx="2.5" fill="{c}"/>')
    s.append(f'<text x="{lx + 32 + 5*step + 4}" y="{ly+9}" fill="{t["muted"]}" font-size="11">More</text>')
    return "".join(s) + "</g></svg>"


def languages_card(d, t, top_n=6):
    pad, w = 20, CARD_W
    ranked = d["langs"].most_common()
    total = sum(d["langs"].values()) or 1
    head = ranked[:top_n]
    rest = sum(v for _, v in ranked[top_n:])
    rows = [(k, v, LANG_COLOR.get(k, OTHER)) for k, v in head]
    if rest:
        rows.append(("Other", rest, OTHER))

    cols, per = 3, (len(rows) + 2) // 3
    h = 62 + 14 + 26 + per * 22 + 12

    s = [frame(w, h, t, "Languages", f'across {d["repos"]} public repositories')]
    bw, x, y = w - 2 * pad, pad, 58
    s.append(f'<clipPath id="c"><rect x="{x}" y="{y}" width="{bw}" height="12" rx="6"/></clipPath>'
             f'<g clip-path="url(#c)">')
    cx = x
    for _, v, col in rows:
        seg = bw * v / total
        s.append(f'<rect x="{cx:.2f}" y="{y}" width="{seg:.2f}" height="12" fill="{col}"/>')
        cx += seg
    s.append(f'</g>')

    for i, (name, v, col) in enumerate(rows):
        col_i, row_i = i // per, i % per
        lx, ly = pad + col_i * (bw // cols), y + 38 + row_i * 22
        s.append(f'<circle cx="{lx+5}" cy="{ly-4}" r="5" fill="{col}"/>'
                 f'<text x="{lx+17}" y="{ly}" fill="{t["fg"]}" font-size="12">{esc(name)}</text>'
                 f'<text x="{lx+17+ (bw//cols) - 34}" y="{ly}" fill="{t["muted"]}" font-size="12" '
                 f'text-anchor="end">{100*v/total:.1f}%</text>')

    s.append(f'<text x="{pad}" y="{h-14}" fill="{t["muted"]}" font-size="11">'
             f'{d["repos"]} repositories · {d["stars"]} stars · {d["followers"]} followers</text>')
    return "".join(s) + "</g></svg>"


if __name__ == "__main__":
    data = fetch()
    os.makedirs(OUT, exist_ok=True)
    for name, theme in THEMES.items():
        for card, fn in (("contributions", contributions_card), ("languages", languages_card)):
            p = os.path.join(OUT, f"{card}-{name}.svg")
            open(p, "w").write(fn(data, theme))
            print(p, os.path.getsize(p), "bytes")
