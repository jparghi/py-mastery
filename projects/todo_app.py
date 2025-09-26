"""Simple CLI Todo App (in-memory)."""

class TodoApp:
    def __init__(self):
        self.items = []

    def add(self, text: str):
        self.items.append({"text": text, "done": False})

    def list(self):
        return [f"[{i}] {'✔' if it['done'] else ' '} {it['text']}" for i,it in enumerate(self.items)]

    def done(self, idx: int):
        if 0 <= idx < len(self.items):
            self.items[idx]["done"] = True

def demo():
    app = TodoApp()
    app.add("Learn Python") 
    app.add("Build a Flask API") 
    app.done(0)
    for line in app.list():
        print(line)

if __name__ == "__main__":
    demo()
