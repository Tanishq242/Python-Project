# Algorithm Visualizer

A Python-based interactive algorithm visualization tool built with Pygame. Watch sorting algorithms, searching techniques, and process scheduling algorithms come to life with real-time visual representations.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)

## Features

### Sorting Algorithms
- Bubble Sort
- Selection Sort
- Insertion Sort

### Searching Algorithms
- Linear Search
- Binary Search

### Process Scheduling Algorithms
- First Come First Serve (FCFS)
- Shortest Job First (SJF)
- Round Robin
- Priority Scheduling

### Customization
- Adjustable visualization speed
- Customizable UI themes and colors
- Variable array sizes
- Step-by-step execution mode

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

## Usage

Run the main application:
```bash
python main.py
```

### Controls

- **Mouse Click**: Select algorithms and interact with UI elements
- **Space**: Start/Pause visualization
- **R**: Reset/Generate new data
- **Arrow Keys**: Adjust visualization speed
- **ESC**: Return to main menu

## Customizing the UI

### Changing Colors

Edit `ui/colors.py` to modify the color scheme:

```python
BACKGROUND = (20, 20, 30)
PRIMARY = (100, 200, 255)
SECONDARY = (255, 100, 150)
ACCENT = (50, 255, 150)
```

### Adjusting Window Size

Modify `utils/config.py`:

```python
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
```

### Creating Custom Themes

Add new themes in `ui/colors.py`:

```python
THEMES = {
    'dark': {...},
    'light': {...},
    'ocean': {...},
    'forest': {...}
}
```

## Screenshots

*Add screenshots of your visualizer here*

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Adding New Algorithms

To add a new algorithm:

1. Implement it in the appropriate file under `algorithms/`
2. Ensure it yields states for visualization
3. Add it to the menu system in `ui/menu.py`
4. Update this README

## Known Issues

- Performance may vary with very large datasets (>1000 elements)
- Some scheduling algorithms require specific input formats

## Future Enhancements

- [ ] Graph algorithms (BFS, DFS, Dijkstra's)
- [ ] Tree traversal visualizations
- [ ] Algorithm comparison mode
- [ ] Export visualization as video
- [ ] Sound effects for operations
- [ ] Mobile/web version

## Acknowledgments

- Inspired by VisualGo and Algorithm Visualizer
- Built with Pygame community support
- Algorithm implementations based on standard CS textbooks

## Contact

Developer Name - Tanishq
Email - kumar.tanishq081@gmail.com

---

⭐ Star this repository if you find it helpful!
