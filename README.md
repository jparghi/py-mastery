# py-mastery 🐍

A curated collection of **Python examples, algorithms, and projects** showcasing my Python skills.
This repo is structured to demonstrate **core programming, problem solving, advanced concepts, and small projects**.

## Structure
- `core_python/` → Basics, OOP, collections, exceptions
- `problem_solving/` → Sorting, searching, recursion, DP, stack/queue
- `advanced/` → File handling, decorators, generators, threading, multiprocessing, regex
- `projects/` → Mini projects (CLI apps + Flask API)
- `tests/` → Unit tests with `pytest`

## Quickstart
```bash
# (Optional) Create & activate a virtualenv
python3 -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install deps
pip install -r requirements.txt

# Run any script
python3 core_python/basics.py

# Run Flask API
export FLASK_APP=projects/flask_api/app.py  # Windows: set FLASK_APP=projects/flask_api/app.py
flask run

# Run tests
pytest -q
```

## Skills Demonstrated
- Core Python (OOP, data structures, exceptions)
- Algorithms & Problem Solving (Sorting, Searching, DP)
- Advanced Python (Decorators, Generators, Concurrency)
- Flask API Development
- Unit Testing with Pytest
