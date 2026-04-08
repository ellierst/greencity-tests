# README

## Description

This repository contains manual test cases for the **Events page** of the GreenCity web application.
The goal is to verify the core functionality of the Events page.

## Page Under Test

https://www.greencity.cx.ua/#/greenCity/events

## How to Run Tests

1. Install dependencies:
```bash
   pip install -r requirements.txt
```
2. Create a `.env` file in the root of the project

3. Run each test script individually:

```bash
python tests/test_events_filter_by_type.py
python tests/test_events_view_toggle.py
python tests/test_events_no_results_message.py
python tests/test_events_bookmark.py
```

## Author
Oleksa Sofia