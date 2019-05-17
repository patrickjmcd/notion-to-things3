# Notion to Things3 Integration

A (currently) one-directional syncing tool to copy and update tasks from Notion to Things3.

## Requirements

- Python3
- Things3
- Notion

## Installation

Clone this repository.

## Setup

Create a `.env` file or set environment variables:

- `NOTION_TOKEN`: the `token_v2` cookie value found by inspecting your browser cookies on a logged-in session on Notion.so
- `NOTION_TASK_LISTS`: a comma-separated list of Notion URLS for task databases (need fields `Name`, `Assign`, `Status`)
- `THINGS_DB`: The file path to your Things3 Database (try `~/Library/Containers/com.culturedcode.ThingsMac/Data/Library/Application\ Support/Cultured\ Code/Things/Things.sqlite3`)
- `THINGS_AUTH_TOKEN`: Authentication Token from Things > Preferences > Manage

## Running the Script

Run the script by executing:

```Shell
python3 sync.py
```

## Future Improvements

- [ ] Turn this into a package with an entry_point for use anywhere.
- [ ] Better Error-trapping for missing environment variables
