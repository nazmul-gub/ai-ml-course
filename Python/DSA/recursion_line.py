"""
Recursion visualization: "How many people are in front of me in the line?"

Run:   python recursion_line.py              -> opens an animation window
Save:  python recursion_line.py --save       -> saves recursion_line.gif
Extra: python recursion_line.py --people 6 --bangla

Needs: pip install matplotlib pillow
Controls: click the play/pause icon (bottom center) or press SPACE.
          LEFT / RIGHT arrow keys step backward / forward when paused.
Tip for reels: screen-record the window, or use --save and convert to mp4.
"""
import argparse
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle, Polygon, Rectangle
from matplotlib import font_manager

TEXT = {
    "en": {
        "ask": "How many people are in front of you?",
        "base": "Nobody in front of me! 0  (BASE CASE)",
        "ret": "{a} + 1 = {r}",
        "you": "YOU",
        "title_ask": "Step 1: Going down - passing the question forward",
        "title_base": "Step 2: Base case reached - the recursion stops",
        "title_ret": "Step 3: Coming back - each person adds 1",
        "final": "Answer: {n} people in front of you!",
    },
    "bn": {
        "ask": "আপনার সামনে কতজন?",
        "base": "আমার সামনে কেউ নেই! ০ (বেস কেস)",
        "ret": "{a} + ১ = {r}",
        "you": "আপনি",
        "title_ask": "ধাপ ১: প্রশ্ন সামনে পাঠানো হচ্ছে",
        "title_base": "ধাপ ২: বেস কেস, এখানে রিকার্শন থামল",
        "title_ret": "ধাপ ৩: উত্তর ফিরছে, প্রত্যেকে ১ যোগ করছে",
        "final": "উত্তর: আপনার সামনে {n} জন!",
    },
}

BN_DIGITS = str.maketrans("0123456789", "০১২৩৪৫৬৭৮৯")


def pick_bangla_font():
    wanted = ["Noto Sans Bengali", "Kalpurush", "SolaimanLipi", "Nirmala UI",
              "Vrinda", "Lohit Bengali", "Siyam Rupali"]
    installed = {f.name for f in font_manager.fontManager.ttflist}
    for name in wanted:
        if name in installed:
            return name
    return None


def build_steps(n, t, bangla):
    """Return a list of animation states. Person 0 = first in line, n-1 = YOU."""
    fmt = (lambda s: str(s).translate(BN_DIGITS)) if bangla else str
    steps = []
    # 1) the question travels from YOU toward the front of the line
    for i in range(n - 1, 0, -1):
        steps.append({"title": t["title_ask"], "active": i,
                      "bubbles": {i: (t["ask"], "#ffe08a")}, "arrow": (i, i - 1)})
    # 2) base case at the front
    steps.append({"title": t["title_base"], "active": 0,
                  "bubbles": {0: (t["base"], "#ff9aa2")}, "arrow": None})
    # 3) answers travel back
    answers = {0: (t["base"].split("(")[0].strip(), "#ff9aa2")}
    for i in range(1, n):
        r = i
        txt = t["ret"].format(a=fmt(r - 1), r=fmt(r))
        answers[i] = (txt, "#b5ead7")
        steps.append({"title": t["title_ret"], "active": i,
                      "bubbles": dict(answers), "arrow": (i - 1, i)})
    steps.append({"title": t["final"].format(n=fmt(n - 1)), "active": n - 1,
                  "bubbles": dict(answers), "arrow": None, "final": True})
    return steps


def draw_person(ax, x, color, label=None):
    ax.add_patch(Circle((x, 1.6), 0.22, fc=color, ec="black", lw=2, zorder=3))
    ax.plot([x, x], [1.38, 0.7], color="black", lw=3, zorder=2)          # body
    ax.plot([x - 0.3, x + 0.3], [1.15, 1.15], color="black", lw=3)       # arms
    ax.plot([x, x - 0.25], [0.7, 0.2], color="black", lw=3)              # legs
    ax.plot([x, x + 0.25], [0.7, 0.2], color="black", lw=3)
    if label:
        ax.text(x, -0.1, label, ha="center", va="top", fontsize=13,
                fontweight="bold")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--people", type=int, default=5, help="people in the line (incl. you)")
    ap.add_argument("--bangla", action="store_true", help="use Bangla text")
    ap.add_argument("--save", action="store_true", help="save as recursion_line.gif")
    ap.add_argument("--speed", type=int, default=1400, help="ms per step")
    args = ap.parse_args()

    n = max(2, args.people)
    lang = "bn" if args.bangla else "en"
    t = TEXT[lang]
    if args.bangla:
        font = pick_bangla_font()
        if font:
            plt.rcParams["font.family"] = font
        else:
            print("Bangla font not found; install 'Noto Sans Bengali' for proper text.")

    steps = build_steps(n, t, args.bangla)
    fig, ax = plt.subplots(figsize=(10, 6.6))
    fig.subplots_adjust(bottom=0.16)
    gap = 1.8
    state = {"playing": True, "frame": 0}

    def render(k):
        state["frame"] = k
        ax.clear()
        s = steps[k]
        ax.set_xlim(-1, (n - 1) * gap + 1)
        ax.set_ylim(-0.8, 4.6)
        ax.axis("off")
        ax.set_title(s["title"], fontsize=15, fontweight="bold", pad=12)
        ax.plot([-0.8, (n - 1) * gap + 0.8], [0.15, 0.15], color="#888", lw=2)

        for i in range(n):
            x = i * gap
            color = "#ffd166" if i == s["active"] else "#cfd8dc"
            if i == n - 1:
                color = "#74c0fc" if i != s["active"] else "#ffd166"
            label = t["you"] if i == n - 1 else f"#{i + 1}"
            draw_person(ax, x, color, label)

            if i in s["bubbles"]:
                text, bg = s["bubbles"][i]
                ax.text(x, 2.5 + (0.0 if i % 2 == 0 else 0.7), text, ha="center",
                        va="bottom", fontsize=10, wrap=True,
                        bbox=dict(boxstyle="round,pad=0.4", fc=bg, ec="black"),
                        zorder=5)

        if s["arrow"]:
            a, b = s["arrow"]
            ax.annotate("", xy=(b * gap, 2.1), xytext=(a * gap, 2.1),
                        arrowprops=dict(arrowstyle="-|>", lw=3, color="#d62828"))

        if s.get("final"):
            pass

    anim = FuncAnimation(fig, render, frames=len(steps), interval=args.speed,
                         repeat=True, repeat_delay=2000)

    if not args.save:
        # ---- play / pause icon (drawn with shapes, so no font issues) ----
        btn_ax = fig.add_axes([0.46, 0.03, 0.08, 0.09])
        btn_ax.set_xlim(0, 1)
        btn_ax.set_ylim(0, 1)
        btn_ax.set_aspect("equal")
        btn_ax.axis("off")

        def draw_icon():
            btn_ax.clear()
            btn_ax.set_xlim(0, 1)
            btn_ax.set_ylim(0, 1)
            btn_ax.axis("off")
            btn_ax.add_patch(Circle((0.5, 0.5), 0.48, fc="#222", ec="none"))
            if state["playing"]:   # show PAUSE icon while playing
                btn_ax.add_patch(Rectangle((0.32, 0.28), 0.12, 0.44, fc="white"))
                btn_ax.add_patch(Rectangle((0.56, 0.28), 0.12, 0.44, fc="white"))
            else:                  # show PLAY icon while paused
                btn_ax.add_patch(Polygon([(0.38, 0.27), (0.38, 0.73), (0.74, 0.5)],
                                         closed=True, fc="white"))
            fig.canvas.draw_idle()

        def toggle(_event=None):
            state["playing"] = not state["playing"]
            if state["playing"]:
                anim.event_source.start()
            else:
                anim.event_source.stop()
            draw_icon()

        def step(delta):
            k = (state["frame"] + delta) % len(steps)
            render(k)
            fig.canvas.draw_idle()

        def on_click(event):
            if event.inaxes is btn_ax:
                toggle()

        def on_key(event):
            if event.key == " ":
                toggle()
            elif event.key == "right" and not state["playing"]:
                step(1)
            elif event.key == "left" and not state["playing"]:
                step(-1)

        fig.canvas.mpl_connect("button_press_event", on_click)
        fig.canvas.mpl_connect("key_press_event", on_key)
        draw_icon()

    if args.save:
        anim.save("recursion_line.gif", writer="pillow", fps=max(1, 1000 // args.speed))
        print("Saved recursion_line.gif")
    else:
        plt.show()


if __name__ == "__main__":
    main()