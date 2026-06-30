# Pocket-Desk Data Flow

This document explains how data moves through Pocket-Desk, from the moment a user enters a Pokémon name until the information is displayed in the terminal.

## Overview

<p align="center">
  <img src="../images/data_flow.png" alt="Pocket-Desk Data Flow" width="600">
</p>

# Step 1 — `main.py`

**Responsibility:** Entry point of the application.

The program starts here. It initializes the application and transfers control to the command handler.

**Input**

* None

**Output**

* Starts the command loop.

---

# Step 2 — `command.py`

**Responsibility:** Controls the application's workflow.

This module:

* Displays the menu
* Accepts user input
* Decides which feature to execute
* Calls the appropriate API and parser functions

It does **not** know how the API works or how the terminal UI is drawn.

---

# Step 3 — `poke_api.py`

**Responsibility:** Communicates with the PokéAPI.

This module sends HTTP requests to the API and retrieves the raw JSON response.

Example:

```text
User searches:
Pikachu

↓

GET https://pokeapi.co/api/v2/pokemon/pikachu

↓

Raw JSON Response
```

No formatting or display happens here.

---

# Step 4 — `parser.py`

**Responsibility:** Converts raw API data into clean Python data.

The PokéAPI returns hundreds of fields.

The parser extracts only the information Pocket-Desk needs, such as:

* Name
* ID
* Types
* Abilities
* Stats
* Height
* Weight
* Pokédex Description
* Legendary/Mythical Status

It also performs small transformations like:

* Joining multiple types
* Cleaning flavor text
* Determining Pokémon status

The output is a clean Python dictionary ready for display.

---

# Step 5 — `cli_display.py`

**Responsibility:** Displays information in the terminal.

This module never communicates with the API.

Instead, it receives already-parsed data and presents it using Rich components such as:

* Panels
* Tables
* Colors
* Rules
* Text formatting

Its only job is to make the information easy to read.

---

# Complete Data Flow

```text
User
 │
 │ Types "pikachu"
 ▼
command.py
 │
 │ Calls API
 ▼
poke_api.py
 │
 │ Returns raw JSON
 ▼
parser.py
 │
 │ Extracts useful data
 ▼
{
    "name": "Pikachu",
    "types": "Electric",
    "hp": 35,
    ...
}
 │
 ▼
cli_display.py
 │
 │ Creates Rich panels/tables
 ▼
Beautiful terminal output
```

---

# Design Philosophy

Each file has a single responsibility:

| File             | Responsibility                           |
| ---------------- | ---------------------------------------- |
| `main.py`        | Starts the application                   |
| `command.py`     | Handles program flow and user input      |
| `poke_api.py`    | Retrieves raw data from the PokéAPI      |
| `parser.py`      | Converts raw JSON into clean Python data |
| `cli_display.py` | Presents the data in the terminal        |

By separating these responsibilities, the code remains easier to understand, debug, and maintain as the project grows.
