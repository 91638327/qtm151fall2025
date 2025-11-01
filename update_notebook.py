import json
from pathlib import Path

path = Path("Quiz_2.ipynb")
nb = json.loads(path.read_text(encoding="utf-8"))

nb["cells"][16]["source"] = [
    "# Write your own code\n",
    "tall_players = fifa_players.query(\"`Height(cm)` > 175\")\n",
    "num_tall = tall_players.shape[0]\n",
    "num_tall\n"
]

path.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
