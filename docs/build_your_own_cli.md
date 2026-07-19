# How to make your very own cli applications ? 

By this point, you've probably looked through my code and found a few bugs, inefficient parts, or things that could have been written better. You may have even judged my coding style, and that's completely fair. But this was my very first project, and I was still learning. I won't say I wrote the entire project on my own—I did use AI, not to build the main logic, but to help me understand how certain features worked and how I could implement them. As time went on, I started understanding the code more deeply, debugging problems on my own, and writing features with much less assistance.

# Step 1 - BrainStorming.
Let's say you don't want to create a Pokédex like I did because you have a better idea. So where do you start?
First, decide what you want to build. In this case, we're building a CLI application, not a CLI tool. There is a difference, even though it's a small one. The first step is simply coming up with an idea. It doesn't have to be the biggest or most innovative idea ever, and your first project doesn't need to solve a real-world problem. It just needs to be your idea.

Once you have one, come back, and we'll start building it.

# Step 2 - Tools to get started.

- Install VS Code (or any code editor you prefer).
- Install Python and make sure it's added to your PATH.
- Create a project folder.
- Open the folder in VS Code (Your Text editor / IDE).
- Create and activate a virtual environment (venv).  Docs: https://docs.python.org/3/library/venv.html
- Create a `requirements.txt` file (even if it's empty for now).
- Create a `main.py` file (or any filename you prefer).

Extra - if you are using VS code there is this externtion called Python made by mincrosofte download it.

# Step 3 - Libraries You'll Need

- **requests** – One of the best libraries to start with. It's simple, reliable, and has very few dependencies.
  Docs: https://requests.readthedocs.io/en/latest/

- **rich** – Think of this as HTML and CSS for your terminal applications. It lets you create beautiful text, tables, progress bars, and more.
  Docs: https://rich.readthedocs.io/en/stable/

- **textual** – A framework for building interactive terminal applications. If you're familiar with React, you'll notice some similar ideas.
  Docs: https://textual.textualize.io/

- **pytest** – A testing framework for Python. If you're new to testing, I recommend watching this video first:
  https://www.youtube.com/watch?v=tIrcxwLqzjQ

## Note

You can install these libraries using `pip`. Make sure your virtual environment (`venv`) is activated before running any `pip install` commands. Otherwise, the packages may be installed globally instead of inside your project.

# Step 4 - How to write your first code using these lib ? 

if you have read the request docs you know it comes with a fucntion called ( get ) so we use that fucntion 

