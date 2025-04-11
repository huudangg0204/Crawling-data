# YouTube Trending Videos API Crawler

This tool connects to the YouTube Data API v3 and retrieves trending videos for specified countries, extracting essential video details and saving them to CSV files.

## Features

- Retrieves trending videos from YouTube by country
- Extracts key video metrics (views, likes, comments, etc.)
- Saves data in structured CSV format
- Configurable parameters (region, max results, video category)
- Comprehensive error handling
- Detailed logging

## Prerequisites

- Python 3.7 or higher
- YouTube Data API v3 key (get one from [Google Developer Console](https://console.developers.google.com/))
- Required Python packages (see requirements.txt)

## Installation

1. Clone this repository or download the files
2. Install required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the script with the required API key:

```bash
python youtube_trending.py --api_key YOUR_API_KEY
```

### Command Line Arguments

- `--api_key` (required): Your YouTube Data API v3 key
- `--region` (optional): ISO 3166-1 alpha-2 country code (default: US)
- `--max_results` (optional): Maximum number of videos to retrieve (default: 50, max: 50)
- `--output_dir` (optional): Directory to save the CSV file (default: current directory)
- `--category` (optional): YouTube video category ID (default: 0 for all categories)

### Examples

Retrieve trending videos for Japan:
```bash
python youtube_trending.py --api_key YOUR_API_KEY --region JP
```

Retrieve 20 trending music videos for the UK:
```bash
python youtube_trending.py --api_key YOUR_API_KEY --region GB --max_results 20 --category 10
```

Save results to a specific directory:
```bash
python youtube_trending.py --api_key YOUR_API_KEY --output_dir ./data
```

## Common Video Category IDs

- 1: Film & Animation
- 2: Autos & Vehicles
- 10: Music
- 15: Pets & Animals
- 17: Sports
- 20: Gaming
- 22: People & Blogs
- 23: Comedy
- 24: Entertainment
- 25: News & Politics
- 26: Howto & Style
- 27: Education
- 28: Science & Technology

## Troubleshooting

- If you see a "quota exceeded" error, you've reached your daily API request limit
- Make sure your API key is correctly configured with YouTube Data API v3 access
- Check the youtube_api.log file for detailed error information

## License

This project is licensed under the MIT License - see the LICENSE file for details.