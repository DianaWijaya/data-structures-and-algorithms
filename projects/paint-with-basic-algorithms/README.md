# Paint - Fundamentals of Algorithms

A grid-based painting application built with Python and Arcade, featuring multiple drawing modes, layer management, undo/redo functionality, and action replay capabilities.

## Attribution

* Assignment Designed and Programmed by Jackson Goerner.
* Multiple points of valuable feedback and checking provided by Lifi Huang.
* Game Idea originated from [Chicory: A Colorful Tale](https://chicorygame.com/).

## Features

- **Multiple Drawing Modes**: 
  - **Set Mode**: Direct color placement on the grid
  - **Additive Mode**: Blend colors by adding RGB values
  - **Sequence Mode**: Apply colors in a sequential pattern
- **Layer System**: Work with multiple layers, each with unique visual effects
- **Brush Size Control**: Adjustable brush sizes for precise or broad strokes
- **Undo/Redo**: Full undo/redo support with keyboard shortcuts (Ctrl+Z / Ctrl+Y)
- **Action Replay**: Replay your entire drawing process step-by-step
- **Special Effects**: Apply special layer-specific effects to the entire canvas

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

## Running the Program

### Interactive Application

To run the interactive painting application:

```bash
python main.py
```

### Visual Tests

Run visual demonstrations:

```bash
python -m visuals.basic
python -m visuals.complex
python -m visuals.styles
```

### Unit Tests

Run the test suite:

```bash
python run_tests.py
```

## Drawing Modes

### Set Mode
Directly sets the color of grid squares to the selected layer's color. Painting over an existing color replaces it completely.

### Additive Mode
Adds the RGB values of the new layer to existing colors, creating blended color effects. Colors can become brighter as more layers are added.

### Sequence Mode
Applies colors in a specific sequence pattern. The behavior depends on the layer's sequence configuration, creating unique visual patterns.

## GUI Controls

**Sidebar Buttons:**
- **Layer Selection**: Click numbered buttons (0-9) to select different layers
- **Draw Mode Toggle**: Cycle through Set/Additive/Sequence modes
- **Replay Button**: Replay your drawing actions from the beginning
- **Brush Size Up**: Increase brush size
- **Brush Size Down**: Decrease brush size
- **Special Effect**: Apply special layer effects

**Keyboard Shortcuts:**
- `Ctrl + Z`: Undo last action
- `Ctrl + Y`: Redo undone action

**Mouse Controls:**
- Click and drag on the canvas to paint with the selected layer
- Painting creates a circular brush area based on the current brush size