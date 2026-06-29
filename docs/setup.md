# Setting Up Pocket-Dex Locally

Follow these steps to run Pocket-Dex on your local machine.

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/pocket-dex.git
cd pocket-dex
```

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv env
env\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv env
source env/bin/activate
```

## 3. Install the Required Dependencies

```bash
pip install -r requirements.txt
```

## 4. Run the Application

```bash
python main.py
```

Pocket-Dex should now start in your terminal.

## Troubleshooting

### Virtual environment won't activate (Windows)

If PowerShell blocks script execution, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate the environment again:

```powershell
env\Scripts\Activate.ps1
```

### Module Not Found

If you receive a `ModuleNotFoundError`, make sure your virtual environment is activated and all dependencies are installed:

```bash
pip install -r requirements.txt
```

## Requirements

* Python 3.10 or newer
* Internet connection (Pocket-Dex fetches live data from PokeAPI)

Happy coding! 
