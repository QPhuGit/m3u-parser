# M3U Parser and Group Splitter

A Python tool that parses M3U playlist files and splits them into separate files based on group titles. Supports both local files and URLs.

## Features

- Parse M3U files from local paths or URLs
- Split entries by `group-title` attribute
- Convert non-ASCII characters to ASCII equivalents for safe filenames
- Automatic file sanitization for cross-platform compatibility

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/m3u-parser.git
cd m3u-parser
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```python
from m3uparse import parse_m3u_and_split_by_group_title

# Parse local file
parse_m3u_and_split_by_group_title('playlist.m3u')

# Parse from URL
parse_m3u_and_split_by_group_title('https://example.com/playlist.m3u')

# Custom output prefix
parse_m3u_and_split_by_group_title('playlist.m3u', output_prefix='custom')
```

### Command Line Usage

```bash
python m3uparse.py
```

## Output

The script creates separate M3U files for each group found in the source playlist:
- `xem_Group1.m3u`
- `xem_Group2.m3u`
- `xem_Ungrouped.m3u` (for entries without group-title)

## Automated Updates

This repository supports automated updates through GitHub Actions:

### Scheduled Updates
- Automatically fetches and processes M3U content daily at 6 AM UTC
- Updates are committed back to the repository

### Manual Updates
- Trigger manual updates through GitHub Actions workflow dispatch
- Push code changes to automatically redeploy

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License
