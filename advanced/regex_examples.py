"""Regex examples."""

import re

EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")  # simple heuristic

def find_emails(text: str):
    return EMAIL_RE.findall(text)

if __name__ == "__main__":
    print(find_emails("Contact us at hello@example.com or admin@test.org"))
