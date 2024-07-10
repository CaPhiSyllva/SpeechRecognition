Claro! Aqui está o arquivo `README.md` revisado, sem as seções de Contributing e License:

```markdown
# Voice Command Recognition System

This project leverages speech recognition to execute specific system commands. It captures audio input from the microphone, transcribes the speech, and executes configured commands based on the recognized speech.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Tests](#tests)
- [Logging](#logging)

## Prerequisites

- Python 3.7 or higher
- `SpeechRecognition` library
- `PyAudio` library
- Windows Operating System (for the provided command examples)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/YourUsername/YourRepository.git
    cd YourRepository
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On macOS/Linux
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Install `PyAudio` if necessary:**

    ```bash
    pip install PyAudio
    ```

## Configuration

Create a `config.json` file at the root of the project with the commands you wish to execute:

```json
{
  "navegador": "start Chrome.exe",
  "Excel": "start Excel.exe",
  "PowerPoint": "start POWERPNT.exe",
  "Edge": "start msedge.exe",
  "Fechar": "Exit"
}
```

## Project Structure

```
.
├── src/
│   ├── microphone.py
│   ├── recognizer.py
│   ├── commands.py
│   └── settings/
│       └── db_connect_handler.py
├── tests/
│   ├── test_commands.py
│   ├── test_microphone.py
│   └── test_recognizer.py
├── config.json
├── app.log
├── main.py
├── requirements.txt
└── README.md
```

## Usage

Run the main script:

```bash
python main.py
```

The script will enter a loop, listening for commands from the microphone and executing actions as configured in `config.json`. To exit the loop, say "Fechar".

## Tests

The project includes unit tests for the main components. To run the tests, use:

```bash
python -m unittest discover tests
```
