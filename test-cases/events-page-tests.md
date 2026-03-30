# Test Cases   Events Page

## Test Case ID
TC-01

**Title**
Verify that the events list can be filtered by event type

**Priority**
Medium

**Preconditions**

1. User is on the Events page
2. At least one event is present in the list
3. The application is running with Ukrainian language

**Environment**

- Browser: Chrome

**Test Steps**

| Steps | Test Step | Test Data | Expected Result |
|--------|-----------------|-----------|-----------------|
| 1 | Open the Events page | https://www.greencity.cx.ua/#/greenCity/events | The Events page is open; filter bar is visible with options: "Event time", "Location", "Status", "Type", "Date" |
| 2 | Click on the "Type" dropdown in the filter bar |   | A dropdown with available event types is displayed (e.g., СОЦІАЛЬНИЙ, ЕКОНОМІЧНИЙ) |
| 3 | Select one event type (e.g., "СОЦІАЛЬНИЙ") | Type: СОЦІАЛЬНИЙ | Selected value is displayed in filter field |
| 4 | Observe the event cards in the list |   | All displayed event cards contain the tag "СОЦІАЛЬНИЙ"; no event cards without the tag "СОЦІАЛЬНИЙ" are displayed; |
| 5 | Click the "x" icon to reset filter |   | Filter field is empty; the full list of events is displayed again |

**Postconditions**

1. The filter is cleared
2. The full events list is visible

**Date Created**
03-30-2026


## Test Case ID
TC-02
 
**Title**
Verify that the events list can be switched between grid and list view
 
**Priority**
Low
 
**Preconditions**
 
1. User is on the Events page
2. At least one event is present in the list
 
**Environment**
 
- Browser: Chrome
 
**Test Steps**
 
| Steps | Test Step | Test Data | Expected Result |
|--------|-----------------|-----------|-----------------|
| 1 | Open the Events page | https://www.greencity.cx.ua/#/greenCity/events | The Events page is open; event cards are displayed in grid view by default; grid/list toggle icons are visible in the top-right of the list |
| 2 | Click the list view icon (≡) in the top-right corner of the events section |   | The layout switches to list view; each event is displayed as a horizontal row |
| 3 | Observe the event information in list view |   | Each event row displays |
| 4 | Click the grid view icon (⊞) |   | The layout switches back to grid view; event cards are displayed in columns |
 
**Postconditions**
 
1. The selected view mode is applied
2. All event data remains unchanged after switching views
3. Grid view is active after the test
 
**Date Created**
03-30-2026


## Test Case ID
TC-03
 
**Title**
Verify that the "We did not find any results matching to this search" message is displayed when no events match the applied filters
 
**Priority**
Medium
 
**Preconditions**
 
1. User is on the Events page
2. At least one event is present in the list
3. The application is running with Ukrainian language
 
**Environment**
 
- Browser: Chrome
 
**Test Steps**
 
| Steps | Test Step | Test Data | Expected Result |
|--------|-----------------|-----------|-----------------|
| 1 | Open the Events page | https://www.greencity.cx.ua/#/greenCity/events | The Events page is open; event cards are visible |
| 2 | Click on the "Date" dropdown in the filter bar |   | A date picker or date range input is displayed |
| 3 | Set a date range with no events (e.g., a past date range with no events) | Date: 23.10.2020 – 29.10.2020 | The selected date range is applied to the filter |
| 4 | Observe the events list area |   | No event cards are displayed; the message "We did not find any results matching to this search" is shown on the page |
| 5 | Click the "x" icon to reset filter |   | Filter field is empty; the full list of events is displayed again |
 
**Postconditions**
 
1. The filter is cleared
2. The full events list is visible
 
**Date Created**
03-30-2026

## Test Case ID
TC-04
 
**Title**
Verify that an authorized user can save an event to bookmarks
 
**Priority**
Medium
 
**Preconditions**
 
1. User is logged in as a registered user
2. User is on the Events page
3. At least one event is present in the list
 
**Environment**
 
- Browser: Chrome
 
**Test Steps**
 
| Steps | Test Step | Test Data | Expected Result |
|--------|-----------------|-----------|-----------------|
| 1 | Open the Events page | https://www.greencity.cx.ua/#/greenCity/events | The Events page is open; event cards are visible; each card has a bookmark icon in the top-right corner |
| 2 | Click the bookmark icon on any event card |   | The bookmark icon becomes active (filled/colored); event is added to bookmarks |
| 3 | Open the Bookmarks page | https://www.greencity.cx.ua/#/greenCity/events?isBookmark=true&section=events | Bookmarks page is opened |
| 4 | Verify the saved event is present in bookmarks list |   | Previously bookmarked event is displayed in the list |
| 5 | Return to Events page and click the same bookmark icon again |   | Bookmark icon returns to inactive state; event is removed from bookmarks |
| 6 | Open Bookmarks section again |   | The event is no longer present in the bookmarks list |
 
**Postconditions**
 
1. Bookmark state is updated correctly
2. The events list remains unchanged
 
**Date Created**
03-30-2026
