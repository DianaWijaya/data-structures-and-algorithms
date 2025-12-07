# Mountain Climber - Hash Table

A visual mountain trail management system built with Python and Arcade, featuring an interactive GUI for managing mountain trails, difficulties, and trail networks.

## Features

- **Interactive Trail Editor**: Add, remove, and edit mountains with visual feedback
- **Trail Branching**: Create complex trail networks with branches
- **Mountain Management**: Organize mountains by difficulty level
- **Graph Visualization**: View mountain difficulty distributions and positions
- **Persistent Storage**: Save and load trail configurations from JSON files

## Setup

Note: For all of these you may need to replace `python` with `py` or `python3` depending on your operating system and python version.

```bash
python -m pip install virtualenv
python -m venv venv
```

Next, activate your virtual environment (Must be done every time you open the terminal)

**Windows Bash**
```bash
source venv/Scripts/activate
```

**Windows CMD**
```cmd
venv/Scripts/activate
```

**Windows Powershell**
```powershell
venv/Scripts/activate.ps1
```

**Mac / Linux bash**
```bash
source venv/bin/activate
```

Then install the requirements!
```bash
python -m pip install -r requirements.txt
```

## Running the GUI

Run with default trail configuration:
```bash
python main.py
```

Run with a specific trail file:
```bash
python main.py <filename.json>
```

## Running the Tests

Run all tests:
```bash
python run_tests.py
```

## Running just some of the Tests

Run specific test groups:
```bash
python run_tests.py 1
```
This will run all tests marked with `@number("1.x")`.

### GUI Controls

The GUI provides several editing modes accessible via the sidebar buttons:

- **Add Mountain Mode**: Click on the trail to add a new mountain
- **Remove Mode**: Click on a mountain to remove it from the trail
- **Edit Mode**: Click on a mountain to edit its name, difficulty level, and length
- **Add Branch Mode**: Create branching paths in your trail network
- **Show Graph**: Visualize mountains organized by difficulty level
- **Save File**: Save your current trail configuration to a JSON file