# Setting Up Pocket-Dex Locally

Follow these steps to run Pocket-Dex from the source code.

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/PocketDex.git
cd PocketDex
```

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install the Dependencies

```bash
pip install -r requirements.txt
```

## 4. Install Pocket-Dex (Editable Mode)

```bash
pip install -e .
```

Installing in editable mode allows changes to the source code to be reflected immediately without reinstalling the package.

## 5. Run the Application

```bash
pocket-dex
```

or

```bash
python -m pocket_dex.main
```

## Requirements

- Python 3.10 or newer
- Internet connection (Pocket-Dex retrieves live data from the PokéAPI)