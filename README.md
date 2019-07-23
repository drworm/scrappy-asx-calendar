# scrappy-asx-calendar

Quick and dirty ASX calendar events for the upcoming August 2019 reporting season.

![Example Calendar](/docs/example.png)

URL: https://investorwag.com/magic/scrappy-asx-calendar.ics

Essentially, it publishes an [iCal](https://icalendar.org/) file of calendar events you can subscribe to with you favourite calendar app. All the raw data is located under `data/events.yaml`.

Please raise PRs for any changes you'd like to make. There's currently no CI job hooked up, so the publishing process involves me manually running the script.

Nobody takes any responsibility for the accuracy of the information provided.

## Subscribe with Google Calendar

1. Settings > Add Calendar > From URL.
1. Enter the URL, give it a name, and tweak the settings to taste

Please note: Google seems to take a while to sync, so changes may not be immediate.

## Subscribe with iPhone/iPad Calendar

1. Open the Settings application.
1. Password and Accounts > Add Account > Other > Add Subscribed calendar
1. Enter the URL, and tweak the settings to taste

## Subscribe in MacOS Calendar

1. File > New Calendar Subscription
1. Enter the URL, and tweak the settings to taste
