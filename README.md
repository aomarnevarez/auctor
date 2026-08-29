# Auctor

Estudio de escritura con **aprendizaje por refuerzo**. Tú das el concepto y el número de capítulos; Auctor propone voces literarias (Thompson sampling), tú calificas cada iteración (1–5), y la política aprende. El libro se escribe en **LaTeX** y vive en **GitHub**.

Repositorio del libro: este repo (`aomarnevarez/auctor`).

## Cómo se escribe

1. Concepto + número de capítulos.
2. Auctor genera un esquema. Lo calificas.
3. Capítulo a capítulo: genera, calificas, aceptas o reescribes.
4. Cada rating actualiza una posterior Beta de la voz usada (lírica, precisa, narrativa, ensayística, barroca, elíptica, cinematográfica, coral).
5. Al aceptar, se hace commit de `main.tex`, `chapters/*.tex`, el preámbulo, este README y `.auctor/project.json` (el estado RL).

## Compilar el PDF

```bash
pdflatex main.tex
pdflatex main.tex
```

O deja que GitHub Actions lo haga en cada push (workflow `build-pdf.yml`).

## Bot

Misma política, sin interfaz. Autenticación: token de GitHub.

```
POST /api/bot/start
POST /api/bot/generate
POST /api/bot/rate
GET  /api/bot/status
GET  /api/bot/latex
```

Ejemplo en `examples/auctor_bot.py`.
