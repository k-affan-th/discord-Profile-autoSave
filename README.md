# Discord Avatar Downloader

A Python script that automatically downloads Discord user avatars using their user IDs. The script uses Selenium with Microsoft Edge WebDriver to fetch avatar information and saves the images with proper organization and duplicate handling.

## Features

- 🤖 Automated Discord avatar downloading
- 🌐 Headless browser support with Microsoft Edge
- 🔄 Duplicate file detection and handling
- 📝 Comprehensive logging system
- 📁 Organized output directory structure
- 🎯 Batch processing of multiple Discord IDs

## Prerequisites

- Python 3.8 or higher
- Microsoft Edge Browser
- Microsoft Edge WebDriver

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/discord-Profile-autoSave.git
cd discord-Profile-autoSave
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/MacOS
python -m venv venv
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Project Structure

```
discord-avatar-downloader/
├── main.py                 # Main script
├── requirements.txt        # Python dependencies
├── data/
│   ├── IDs.txt            # List of Discord user IDs
│   ├── script/
│   │   ├── AvatarInfo.py  # Avatar information fetching script
│   │   └── download_img.py # Image downloading utilities
│   ├── output/            # Downloaded avatars storage
│   │   └── temp/          # Temporary storage for processing
│   └── log/               # Operation logs
└── README.md
```

## Usage

1. Add Discord user IDs to `data/IDs.txt`, one ID per line such as:
```
123456789012345678
234567890123456789
```

2. Run the script:
```bash
python main.py
```

3. Check the output in `data/output/` directory. Each user's avatars will be in their own folder.

## Output Structure

- Each user's avatars are stored in a dedicated folder named by their Discord ID
- Images are named in the format: `[Username] avatar_hash.jpeg`
- Duplicate images are automatically handled
- Logs are stored in `data/log/` with timestamps

## Logging

The script generates detailed logs including:
- Number of processed IDs
- Successfully downloaded avatars
- Any errors or issues encountered
- Duplicate file handling results

Logs are saved in the `data/log/` directory with timestamp-based filenames.

## Error Handling

The script includes error handling for:
- Network connection issues
- Invalid Discord IDs
- File system operations
- Duplicate file detection
- WebDriver issues

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Safety Note

Please use this tool responsibly and in accordance with Discord's terms of service and API guidelines. Avoid excessive requests that might be considered API abuse.

## Acknowledgments

- Uses [Selenium](https://www.selenium.dev/) for web automation
- Built with [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
