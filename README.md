# MBTA-Web-App-Project

# MBTA Web App

## 🚊 Project Overview

This is a simple web app I built using Flask that helps users find the nearest MBTA stop based on any place or address they enter. The app uses two APIs — Mapbox to turn the location into coordinates, and the MBTA API to find the closest station to those coordinates. It tells the user the name of the stop, if it’s wheelchair accessible, and links directly to Google Maps to view the stop.

I also focused on making the site look clean and easy to use. I added design elements like a gradient background, animations, a favicon, the MBTA logo, and a Google Font to make the experience feel more polished and professional.

---

## ✍️ Reflection

### Process

I started by working on the backend logic — getting the Mapbox and MBTA APIs to work together and making sure the app could handle different inputs (including places that aren’t in Boston). Once that was working, I moved on to the Flask web app and designed the front-end to keep it simple but engaging.

One issue I ran into was that some search results (like “Fenway Park”) were pulling up the wrong place, so I learned how to better format my queries and handle cases where no results were returned. Testing different inputs and using print statements really helped with troubleshooting.

### How I Worked

I worked on this project independently and broke it down into small steps. First, I made sure the backend logic worked correctly. Then I set up the web interface, added error handling, and finally focused on the design and user experience. Doing it this way helped me stay organized and catch errors early on.

### What I Learned

This project helped me understand how to work with APIs in Python, handle JSON data, and build a functional web app from scratch using Flask. I also learned how important user experience and design are — even small touches like fonts, colors, and spacing make a big difference.

I used AI tools throughout the project to help me debug, brainstorm design ideas, and figure out the best ways to structure my code. This made the process faster and helped me explore creative options I might not have thought of on my own.

![error screenshot](static/screenshot_error.png)

---

## 🛠️ Tools Used

- Python / Flask
- Mapbox API
- MBTA v3 API
- HTML / CSS
- Jinja templates
- Git / GitHub

