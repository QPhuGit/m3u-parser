import re
from collections import defaultdict
import urllib.request
from urllib.parse import urlparse
from unidecode import unidecode
import os

def parse_m3u_and_split_by_group_title(input_path, output_prefix="xem"):
    group_pattern = re.compile(r'group-title="([^"]+)"')
    group_dict = defaultdict(list)
    current_entry = []

    # Check if input_path is a URL or local file
    parsed_url = urlparse(input_path)
    if parsed_url.scheme in ('http', 'https'):
        # Handle URL input
        with urllib.request.urlopen(input_path) as response:
            content = response.read().decode('utf-8')
            lines = content.splitlines(keepends=True)
    else:
        # Handle local file input
        with open(input_path, encoding='utf-8') as f:
            lines = f.readlines()

    for line in lines:
        if line.startswith("#EXTINF:"):
            current_entry = [line]
            match = group_pattern.search(line)
            group = match.group(1) if match else "Ungrouped"
        elif line.startswith("#"):
            continue  # skip non-entry metadata
        elif line.strip():
            current_entry.append(line)
            group_dict[group].append("".join(current_entry))
            current_entry = []

    # Create IPTV directory if it doesn't exist
    iptv_dir = "IPTV"
    os.makedirs(iptv_dir, exist_ok=True)

    for group, entries in group_dict.items():
        # Convert non-ASCII characters to ASCII equivalents using unidecode, then sanitize for filename
        safe_group = unidecode(group)
        safe_group = re.sub(r'[^\w\-_\. ]', '_', safe_group)
        out_file = os.path.join(iptv_dir, f"{output_prefix}_{safe_group}.m3u")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n")
            for entry in entries:
                f.write(entry)
        print(f"Wrote group '{group}' to {out_file}")

# Example usage:
# parse_m3u_and_split_by_group_title('playlist.m3u')  # Local file
# parse_m3u_and_split_by_group_title('https://xem.hoiquan.click')  # URL

if __name__ == "__main__":
    # Default execution when run directly
    parse_m3u_and_split_by_group_title('https://xem.hoiquan.click')
