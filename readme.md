# yt-dlp GUI Wrapper

A clean, user-friendly graphical interface for `yt-dlp` designed with accessibility in mind. This tool was specifically built to help users who prefer a visual workflow over command-line interfaces for downloading media for presentations.

## Key Features
- **Simplified Interface:** Large, high-contrast buttons and fields optimized for ease of use.
- **PowerPoint Ready:** One-click presets for H.264/MP4 compatibility.
- **Context-Aware:** Dropdowns that intelligently filter formats and codecs based on your selection (Audio vs. Video).
- **Cross-Platform:** Runs natively on Windows, macOS, and Linux.

## Built With
- **Python 3.11+**
- **PySide6** (Qt for Python)
- **yt-dlp**
- **FFmpeg** (for encoding and remuxing)

## Getting Started

### Prerequisites
- Python installed on your system.
- FFmpeg installed and added to your system PATH.

### Installation (Development)
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/sennematic/yt-dlp-wrapper.git](https://github.com/sennematic/yt-dlp-wrapper.git)
   cd yt-dlp-wrapper