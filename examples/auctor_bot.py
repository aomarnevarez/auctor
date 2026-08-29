#!/usr/bin/env python3
"""Bot mínimo para Auctor: esquema → generar → calificar → aceptar."""

from __future__ import annotations

import json
import os
import sys
import urllib.request

HOST = os.environ.get("AUCTOR_HOST", "http://127.0.0.1:8080")
TOKEN = os.environ["GITHUB_TOKEN"]
OWNER = os.environ.get("GITHUB_OWNER", "aomarnevarez")
REPO = os.environ.get("GITHUB_REPO", "auctor")


def call(method: str, path: str, body: dict | None = None) -> dict:
    url = f"{HOST}{path}"
    data = None if body is None else json.dumps(body).encode()
    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req) as res:
        if res.headers.get_content_type() == "application/json":
            return json.load(res)
        return {"text": res.read().decode()}


def main() -> None:
    start = call(
        "POST",
        "/api/bot/start",
        {
            "owner": OWNER,
            "repo": REPO,
            "title": "El cauce seco",
            "concept": sys.argv[1] if len(sys.argv) > 1 else "Un río que se retira y un mapa que miente.",
            "chapterCount": 6,
            "author": "Andrés",
            "language": "es",
            "genre": "novela",
            "createRepo": True,
        },
    )
    print(json.dumps(start.get("project", start), indent=2, ensure_ascii=False))

    rated = call(
        "POST",
        "/api/bot/rate",
        {
            "owner": OWNER,
            "repo": REPO,
            "rating": 4,
            "notes": "Buen arco. Conservar la agrimensora.",
            "accept": True,
        },
    )
    print("esquema aceptado", rated.get("project", {}).get("status"))

    generated = call(
        "POST",
        "/api/bot/generate",
        {"owner": OWNER, "repo": REPO},
    )
    title = (generated.get("project") or {}).get("latestDraft", {}) or {}
    print("borrador", title.get("title"), title.get("armName"))


if __name__ == "__main__":
    main()
