#!/usr/bin/env python3
"""
Manual update script for M3U content processing.
Can be run locally or used as a reference for manual operations.
"""

import argparse
import sys
from m3uparse import parse_m3u_and_split_by_group_title

def main():
    parser = argparse.ArgumentParser(description='Manually update M3U content')
    parser.add_argument('--url', 
                       default='https://xem.hoiquan.click',
                       help='M3U URL to process (default: https://xem.hoiquan.click)')
    parser.add_argument('--prefix', 
                       default='xem',
                       help='Output file prefix (default: xem)')
    parser.add_argument('--local-file',
                       help='Process local M3U file instead of URL')
    
    args = parser.parse_args()
    
    try:
        if args.local_file:
            print(f"Processing local file: {args.local_file}")
            parse_m3u_and_split_by_group_title(args.local_file, args.prefix)
        else:
            print(f"Processing URL: {args.url}")
            parse_m3u_and_split_by_group_title(args.url, args.prefix)
            
        print("✅ M3U processing completed successfully!")
        
    except Exception as e:
        print(f"❌ Error processing M3U: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
