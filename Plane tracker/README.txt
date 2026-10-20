# Aircraft Tracker — Python

A real-time aircraft tracking script built with Python that monitors aircraft within a user-defined geographic boundary and displays selected flight information in the terminal.

The project uses the OpenSky Network API for live aircraft state data and ADSBDB for aircraft identification and metadata.

## Features

- **Custom geofencing:** Define a geographic monitoring area using a base latitude, longitude, and directional distances.
- **Directional aircraft selection:** Select aircraft to the North, South, East, or West of the base location.
- **Live tracking:** Refresh aircraft data at regular intervals.
- **Flight information:** Display flight number, country of origin, aircraft type, registered owner, speed, and distance from the base.
- **Terminal interface:** Uses Rich to display information in a formatted, continuously updating panel.
- **Configurable monitoring:** Adjust the geofence and directional preference at runtime.

## Technologies Used

- Python
- Requests — HTTP requests to external APIs
- Rich — terminal formatting and live display
- OpenSky Network API — aircraft state vectors
- ADSBDB API — aircraft metadata

## How It Works

### 1. Define the monitoring area

The user enters a base latitude and longitude, followed by the distances to the North, South, East, and West boundaries.

The program converts these distances into approximate latitude and longitude offsets to construct a rectangular geofence.

### 2. Retrieve aircraft data

The script queries the OpenSky Network API for aircraft within the defined boundaries.

Aircraft state data includes position, flight identification, ground status, and velocity when available.

### 3. Filter aircraft by direction

The user selects a directional preference:

- **N:** North
- **S:** South
- **E:** East
- **W:** West

The program filters aircraft according to their position relative to the base location and excludes aircraft identified as being on the ground.

It then selects a candidate based on its position along the chosen direction.

### 4. Retrieve aircraft metadata

The selected aircraft's ICAO 24-bit address is used to query ADSBDB for available aircraft information, including aircraft type and registered owner.

Metadata may not be available for every aircraft.

### 5. Calculate distance and speed

The program estimates the aircraft's distance from the base using latitude and longitude offsets.

Aircraft velocity, when available, is converted from metres per second to knots.

### 6. Display live information

A Rich Live panel displays the selected aircraft's available information and API status. The program refreshes approximately every five seconds.

## Installation

### Requirements

- Python 3
- Internet connection
- Access to the OpenSky Network and ADSBDB APIs

### Install dependencies

```bash
pip install requests rich
```

Alternatively, install the dependencies from `requirements.txt` if provided.

### Run the tracker

Save the script as `tracker.py` and execute:

```bash
python tracker.py
```

Follow the prompts to enter the base coordinates, geofence dimensions, and directional preference.

## Example Configuration

A sample configuration might use a base location near an airport, with a larger boundary in the direction of the desired aircraft traffic.

The monitoring area is user-defined; the program does not require a fixed airport or set of coordinates.

## Limitations

- Aircraft positions and metadata depend on external data availability.
- Aircraft may be missing from the returned dataset or have incomplete state information.
- Directional selection is based on geographic position, not flight-plan intent or confirmed approach status.
- Distance is an approximation based on latitude and longitude offsets, rather than a geodesic calculation.
- The geofence conversion uses approximate distance-per-degree factors, so accuracy varies with location.
- Aircraft type and registered-owner information may be unavailable.
- API availability, rate limits, and access policies may affect operation.

This project is intended for educational and personal aircraft monitoring. It is not a certified aviation system and must not be used for air traffic control or flight-safety decisions.

## Future Improvements

Potential improvements include:

- More robust handling of API errors and missing data.
- Improved geographic distance calculations.
- Aircraft selection based on straight-line distance.
- A map-based display.
- Logging aircraft observations over time.

## Acknowledgements

- [OpenSky Network](https://opensky-network.org/) — aircraft state data.
- [ADSBDB](https://www.adsbdb.com/) — aircraft metadata.
- [Rich](https://github.com/Textualize/rich) — terminal interface.

## License

Choose a license before redistributing the project. If you intend to make it publicly reusable, consider the MIT License.
