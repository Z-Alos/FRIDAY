friday/
├── core/
│   ├── __init__.py          # Initialize core package
│   ├── engine.py            # TTS engine initialization
│   ├── listener.py          # Speech recognition logic
│   ├── command_handler.py   # Central command routing
│   ├── utilities.py         # Common utility functions
│   ├── config.py            # Global configurations
├── modules/
│   ├── accessibility/
│   │   ├── __init__.py      # Initialize system module
│   │   ├── keyboard.py      # Voice to text
│   ├── system/
│   │   ├── __init__.py      # Initialize system module
│   │   ├── volume.py        # Volume adjustment logic
│   │   ├── brightness.py    # Brightness adjustment logic
│   │   ├── power_manager.py # Power management logic
│   ├── internet/
│   │   ├── __init__.py      # Initialize internet module
│   │   ├── wikipedia.py     # Wikipedia search
│   │   ├── speed_test.py    # Internet speed testing
│   │   ├── open_website.py  # Open different websites
│   ├── media/
│   │   ├── __init__.py      # Initialize media module
│   │   ├── playback.py      # Play media on YouTube
│   │   ├── controls.py      # Media control (fullscreen, play/pause)
├── friday.py                # Entry point
├── requirements.txt         # Dependencies
├── README.md                # Documentation
├── .gitignore               # Gitignore
└── structure.md             # This file
