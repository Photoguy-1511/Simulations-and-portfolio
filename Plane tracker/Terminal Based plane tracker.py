import requests
import time
import os
from rich import print
from rich.panel import Panel
from rich.live import Live

home_lat=float(input("Enter Base Latitude:"))
home_lon=float(input("Enter Base Longitude"))

print("Define geofence:")
n_km= float(input( "\t Enter distance from North boundary:"))
s_km= float(input( "\t Enter distance from South boundary:"))
e_km= float(input( "\t Enter distance from East boundary:"))
w_km= float(input( "\t Enter distance from West boundary:"))


pref=input("Direction Preference: (N/S/E/W)").upper()

print()
print()
print()
print()

n = n_km / 111    
s = s_km / 111    

w = w_km / 98      
e = e_km / 98     

latmin= home_lat - s
lonmin= home_lon - w        #setting parameters
latmax= home_lat + n
lonmax= home_lon + e

panel = Panel(
    "Searching...",
    title="[bold green]Tracker[/bold green]"
)

with Live(panel, refresh_per_second=1) as live:

    while True:
        response = requests.get(
        f"https://opensky-network.org/api/states/all?lamin={latmin}&lomin={lonmin}&lamax={latmax}&lomax={lonmax}"
        )
        #os.system('cls')
        if response.status_code==200:
            opensky_status = "Active"
        else:
            opensky_status = f"Error {response.status_code}"
            time.sleep(5)
            continue
            
        data=response.json()

        if data["states"] is None:
            time.sleep(5)
            continue   
            
        planes = data["states"]
        best_planes = []


        if pref=="N":
            for plane in planes:
                if plane[6] is None:      # n/a lat
                    continue
                if plane[8] == True:      # grounded
                    continue
                if home_lat <= plane[6] <= latmax:
                    best_planes.append(plane)           #  plane added to list

            pref_plane_no= f"Northward planes: {len(best_planes)}"

            if len(best_planes) > 0:
                best_plane = best_planes[0]
                for plane in best_planes:
                    if plane[6] < best_plane[6]:        # plane is best
                        best_plane = plane

                plane = best_plane
            else:

                plane = planes[0]
            
        elif pref=="S":
            for plane in planes:
                if plane[6] is None:      # n/a lat
                    continue
                if plane[8] == True:      # grounded
                    continue
                if latmin <= plane[6] <= home_lat:
                    best_planes.append(plane)           # plane added to list

            pref_plane_no= f"Southward planes: {len(best_planes)}"

            if len(best_planes) > 0:
                best_plane = best_planes[0]
                for plane in best_planes:

                    if plane[6] > best_plane[6]:        # plane is best
                        best_plane = plane
                plane = best_plane
            else:
                plane = planes[0]
            
        elif pref=="E":
            for plane in planes:
                if plane[5] is None:      # n/a lon
                    continue
                if plane[8] == True:      # grounded
                    continue
                if home_lon <= plane[5] <= lonmax:
                    best_planes.append(plane)           # plane added to list

            pref_plane_no= f"Eastward planes: {len(best_planes)}"

            if len(best_planes) > 0:
                best_plane = best_planes[0]
                for plane in best_planes:
                    if plane[5] > best_plane[5]:        # plane is best
                        best_plane = plane
                plane = best_plane

            else:
                plane = planes[0]

        elif pref=="W":
            for plane in planes:
                if plane[5] is None:      # n/a lon
                    continue
                if plane[8] == True:      # grounded
                    continue
                if lonmin <= plane[5] <= home_lon:
                    best_planes.append(plane)           # plane added to list

            pref_plane_no= f"Westward planes: {len(best_planes)}"

            if len(best_planes) > 0:
                best_plane = best_planes[0]
                for plane in best_planes:
                    if plane[5] > best_plane[5]:        # plane is best
                        best_plane = plane
                plane = best_plane

            else:
                plane = planes[0]

        plane_lon = plane[5]
        plane_lat = plane[6]

        d_lon = (plane_lon - home_lon)*98
        d_lat = (plane_lat - home_lat)*111

        dist = (d_lon**2 + d_lat**2)**0.5

        icao= plane[0]
        flight_no = plane[1].strip()
        country = plane[2]
        speed_knots = plane[9] * 1.94384

        adsbdb_data=requests.get(
            f"https://api.adsbdb.com/v0/aircraft/{icao}"
            )

        if adsbdb_data.status_code==200:
            adsbdb_status = "Found"
            planes_data = adsbdb_data.json()
            status= 1
        else:
            adsbdb_status = "Not Found"
            status= 0

        if status:
            plane_data = planes_data["response"]["aircraft"]
            airline = plane_data["registered_owner"]
            plane_type = plane_data["type"]
        else:
            airline = "N/A"
            plane_type = "N/A"
            
        panel = Panel(
            f"""

        [bold white]Opensky: [/bold white] [bold yellow] {opensky_status} [/bold yellow]
        
        [bold white]ADSBDB: [/bold white] [bold yellow] {adsbdb_status} [/bold yellow]

        [bold white]{pref_plane_no} [/bold white]

        [bold white]Flight:[/bold white] {flight_no}

        [bold white]Aircraft:[/bold white] {plane_type}

        [bold white]Airline:[/bold white] {airline}

        [bold white]Country:[/bold white] {country}

        [bold white]Speed:[/bold white] {int(speed_knots)} knots

        [bold white]Distance:[/bold white] {round(dist)} km

        [bold white]Aircraft in geofence:[/bold white] {len(data['states'])}

        [dim]Refreshing in a few seconds...[/dim]
        """,
            title="[bold green]Tracker[/bold green]",
            expand=False
        )

        live.update(panel)
        time.sleep(5)
