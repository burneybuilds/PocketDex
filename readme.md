<p align="center">
    <img src="images/logo.png" width="200" alt="Pocket-Dex Banner">
</p>

<h1 align="center">Pocket-Dex</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14-blue" alt="Python">
  <img src="https://img.shields.io/badge/Version-1.0-green" alt="Version">
  <img src="https://img.shields.io/badge/Status-Learning-orange" alt="Status">
  <img src="https://img.shields.io/badge/API-PokeAPI-red" alt="API">
  <img src="https://img.shields.io/badge/Interface-Terminal_UI-black" alt="Interface">
  <img src="https://github.com/burneybuilds/PocketDex/actions/workflows/python-tests.yml/badge.svg" alt="Tests">
</p>

---

# About the Project

Thank you for taking the time to check out Pocket-Dex.

This project answers three simple questions:

- Why did I build it?
- What does it do?
- What did I learn while building it?

## Why did I build this?

When I started learning Python, I didn't want my first project to be another to-do list or weather application. Those are great beginner projects, but I wanted something that would keep me motivated while teaching me real programming concepts.

Having grown up watching Pokémon and playing the games, building a Pokédex felt like the perfect first project.

Along the way, what started as a small CLI slowly evolved into a full terminal application.

---

## What is Pocket-Dex?

Pocket-Dex is a terminal-based Pokédex built with Python.

It communicates with the **PokeAPI**, retrieves live Pokémon data, processes only the information the application needs, and presents it through a clean Textual interface using Rich components.
---

## What did I learn?

Pocket-Dex became much more than an API project.

While building it I learned:

- Working with REST APIs using `requests`
- Parsing nested JSON responses
- Designing modular applications
- Separating networking, parsing, formatting, and UI
- Building terminal user interfaces with **Textual**
- Creating rich terminal layouts with **Rich**
- Managing project structure across multiple modules
- Writing unit tests with `pytest`
- Packaging Python applications
- Using Git and GitHub during development

---

# Tech Stack

- Python
- Textual
- Rich
- Requests
- Pytest
- PokeAPI

---

# Installation

See the documentation inside:

```
docs/setup.md
```

---

# Project Structure

```
Pocket-Dex/
│
├── pocket_dex/
│   ├── main.py
│   ├── cli_display.py
│   ├── command.py
│   ├── parser.py
│   ├── poke_api.py
│   ├── compare.py
│   ├── display_formatter.py
│   └── history_handler.py
│
├── docs/
│   ├── DATA_FLOW.md
│   ├── setup.md
│   └── build-your-own-cli.md
│
├── tests/
├── images/
├── requirements.txt
└── pyproject.toml
```

---

# Documentation

Want to understand how Pocket-Dex works internally?

Take a look at the documentation inside the `docs/` directory.

- **DATA_FLOW.md** — Explains how data moves through the application.
- **build-your-own-cli.md** — My development journey and lessons learned.
- **setup.md** — Local setup instructions.

---

# Contributing

Contributions are always welcome.

If you'd like to improve Pocket-Dex:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Open a Pull Request.

Bug reports, feature requests, and suggestions are also appreciated.

---

<h3 align="center">
Thanks for checking out Pocket-Dex!
</h3>
