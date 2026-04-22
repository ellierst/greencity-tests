# README

## Description

This repository contains automated test cases for the “Events” page of the GreenCity web application, implemented both with and without the “Page Object Model” (POM) pattern.

## Page Under Test

https://www.greencity.cx.ua/#/greenCity/events

## How to Run Tests from folder tests

1. Install dependencies:
```bash
   pip install -r requirements.txt
```
2. Create a `.env` file in the root of the project

3. Run each test script individually:

```bash
cd tests
python TC_01_events_filter_by_type.py
python TC_02_events_view_toggle.py
python TC_03_events_no_results_message.py
python TC_04_events_bookmark.py
```

## How to Run Tests from folder tests+PO

1. Install dependencies:
```bash
   pip install -r requirements.txt
```
2. Create a `.env` file in the root of the project

3. Run each test script individually:

```bash
cd tests+PO
python tests/TC_01_events_filter_by_type.py
python tests/TC_02_events_view_toggle.py
python tests/TC_03_events_no_results_message.py
python tests/TC_04_events_bookmark.py
```

**PowerShell:** if you get `ModuleNotFoundError`, run first:
```powershell
$env:PYTHONPATH = "."
```
**bash/macOS/Linux:**
```bash
export PYTHONPATH=.
```

## Test Cases
 
| # | File | Description |
|---|------|-------------|
| 01 | TC_01_events_filter_by_type | Filter events by type (Social) |
| 02 | TC_02_events_view_toggle | Toggle between list and table view |
| 03 | TC_03_events_no_results_message | No results message for empty date range |
| 04 | TC_04_events_bookmark | Add and remove event bookmark (requires login) |

## Author
Oleksa Sofia