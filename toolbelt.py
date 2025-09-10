import subprocess, sys
from pathlib import Path

# ai_freedom root is one level up from this repo folder
ROOT = Path(__file__).resolve().parent.parent

TOOLS = {
    "1": ("Quick Notes", ROOT / "quick_notes_cli" / "main.py"),
    "2": ("Focus Timer", ROOT / "focus_timer_cli" / "main.py"),
    "3": ("Idea Box", ROOT / "idea_box_cli" / "main.py"),
}

def run_tool(key: str):
    name, path = TOOLS[key]
    if not path.exists():
        print(f"{name} not found at {path}")
        return
    # Prefer that project's venv python if it exists; else use current python
    venv_py = path.parent / ".venv" / "Scripts" / "python.exe"
    py = str(venv_py if venv_py.exists() else sys.executable)
    print(f"\n==> Launching {name}\n")
    # pass through args after the tool number
    extra = sys.argv[2:]
    subprocess.run([py, str(path), *extra], cwd=str(path.parent))

def main():
    if len(sys.argv) >= 2 and sys.argv[1] in TOOLS:
        return run_tool(sys.argv[1])
    print("\nCLI Toolbelt")
    for key, (name, _) in TOOLS.items():
        print(f" {key}) {name}")
    print("\nUsage examples:")
    print('  python toolbelt.py 1 add "Ship MVP"')
    print('  python toolbelt.py 2 start --minutes 25 --label work')
    print('  python toolbelt.py 3 add "AI SaaS" --tags ai,saas\n')

if __name__ == "__main__":
    main()
