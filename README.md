# Bright Minds Academy Equipment Booking System

## Description
This is a beginner-friendly Python console application for recording and searching equipment bookings in a college setting.

## How to Run
1. Make sure Python 3 is installed.
2. Open a terminal in this project folder.
3. Run:

```bash
python3 equipment_booking.py
```

## Features
- Menu-driven booking system
- Add new equipment
- Record bookings with date validation (`YYYY-MM-DD`)
- View booking records
- Search bookings by partial student name or equipment name (case-insensitive)
- Prevents double booking on the same date
- Includes default equipment:
  - Laptop 1
  - Laptop 2
  - Projector A
  - Tablet 1

## Quick Demo (for presentation)
Try this exact flow to show that booking and search work:

1. Choose `2` (Record a booking)
2. Enter student name: `Khadar Hassan`
3. Enter equipment name: `Laptop 1`
4. Enter date: `2026-03-19`
5. Choose `3` (View booking records) to show the saved booking
6. Choose `4` (Search bookings), type `khadar` to show case-insensitive search result
