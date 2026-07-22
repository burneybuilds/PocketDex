# How to Build Your Own CLI Application

By this point, you've probably looked through my code and found a few bugs, inefficient parts, or things that could have been written better. You may have even judged my coding style—and honestly, that's completely fair.

This was my very first Python project, and I was still figuring things out.

I won't pretend I built the entire project by myself. I did use AI, but not to write the main logic for me. I mainly used it to understand how certain features worked and how they could be implemented. As the project grew, I started relying on it less and less. Eventually, I was debugging problems on my own, reading documentation, and building new features without needing nearly as much help.

Hopefully, this guide helps you do the same.

---

# Step 1 — Brainstorming

Let's say you don't want to build a Pokédex like I did because you've got a better idea (which is totally possible).

So... where do you start?

The first step is simply deciding **what** you want to build.

Notice I said a **CLI application**, not just a **CLI tool**.

A CLI tool usually does one specific job.

Examples:

- `git`
- `ping`
- `curl`

A CLI application feels more like software that happens to live inside your terminal.

Examples:

- Password managers
- Terminal games
- Music players
- Package managers
- Pokédexes 🙂

Don't overthink your first idea.

It doesn't need to change the world.

It doesn't need AI.

It doesn't need blockchain.

(Please... it really doesn't.)

Your first project just needs to be something **you actually want to finish**.

---

# Step 2 — Tools You'll Need

Before writing any code, let's get your workspace ready.

- Install **Python**.
- Install **VS Code** (or any editor you like).
- Create a new project folder.
- Open the folder in your editor.
- Create a virtual environment (`venv`).
- Activate the virtual environment.
- Create a `requirements.txt` file.
- Create a `main.py` file.

That's it.

Nothing fancy.

### Bonus

If you're using VS Code, install the **Python** extension published by Microsoft.

It adds debugging, IntelliSense, formatting, and a lot of quality-of-life improvements.

Trust me—future you will thank you.

---

# Step 3 — Libraries You'll Need

We're not going to reinvent the wheel.

Python already has amazing libraries.

### requests

Probably one of the best libraries to start with.

It makes sending HTTP requests incredibly simple.

Without it, you'd have to deal with lower-level networking.

With it?

```python
requests.get(...)
```

Done.

Documentation:

https://requests.readthedocs.io/

---

### Rich

Think of Rich as **HTML + CSS for your terminal**.

Instead of boring text like this:

```
Name: Pikachu
HP: 35
Type: Electric
```

You can build colorful tables, panels, progress bars, columns, trees, markdown, and much more.

Documentation:

https://rich.readthedocs.io/

---

### Textual

If Rich makes your terminal look pretty...

Textual makes it interactive.

Think of it like building a desktop application—

except your "window" is the terminal.

If you've used React before, some concepts will feel surprisingly familiar.

Documentation:

https://textual.textualize.io/

---

### pytest

Eventually...

Something **will** break.

(Usually five minutes after you proudly tell yourself it finally works.)

That's where testing comes in.

`pytest` helps you make sure future changes don't accidentally break existing features.

If you're completely new to testing, I'd recommend watching this first:

https://www.youtube.com/watch?v=tIrcxwLqzjQ

---

## Installing Everything

Once your virtual environment is activated, install the libraries using `pip`.

Always make sure your virtual environment is active first.

Otherwise you'll end up installing packages globally...

...and then spend twenty minutes wondering why Python can't find them.

We've all been there.

---

# Step 4 — Writing Your First API Request

Time to write some actual code.

Earlier, we installed the **requests** library.

One of the most useful functions it provides is:

```python
requests.get()
```

Think of it like knocking on someone's front door.

You knock.

The server answers.

If everything goes well, it sends the information back.

```python
import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
```

Congratulations.

You just made your first HTTP request.

Now, the response you receive isn't magically a Python dictionary.

It's raw JSON data.

Luckily, `requests` gives us another helpful function:

```python
response.json()
```

That converts the JSON into a normal Python dictionary, making it much easier to work with.

We'll use that in the next section.