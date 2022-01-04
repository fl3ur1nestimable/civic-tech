mapboxgl.accessToken = 'pk.eyJ1IjoidGhpYmF1bHQtMjMiLCJhIjoiY2t4bG0xNHV1MWRobTJxcGVseWx1dGhoNSJ9.s7HzfDQrQPWrY8d5A4oivA';

const startString = document.getElementById('start').innerHTML;
const startCoordinate = startString.split(",").map(Number);

const endString = document.getElementById('end').innerHTML;
const endCoordinate = endString.split(",").map(Number);

const travelType = document.getElementById('travelType').innerHTML;
const emoji = document.getElementById('emoji').innerHTML;


const map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/streets-v11',
  center: startCoordinate, // starting position
  zoom: 13
});

// an arbitrary start will always be the same
// only the end or destination will change

// create a function to make a directions request
async function getRoute(start, end) {
    // make a directions request using cycling profile
    // an arbitrary start will always be the same
    // only the end or destination will change
    const query = await fetch(
      `https://api.mapbox.com/directions/v5/mapbox/${travelType}/${start[0]},${start[1]};${end[0]},${end[1]}?steps=true&geometries=geojson&access_token=${mapboxgl.accessToken}&language=fr`,
      { method: 'GET' }
    );
    const json = await query.json();
    const data = json.routes[0];
    const route = data.geometry.coordinates;
    const geojson = {
      type: 'Feature',
      properties: {},
      geometry: {
        type: 'LineString',
        coordinates: route
      }
    };
    // if the route already exists on the map, we'll reset it using setData
    if (map.getSource('route')) {
      map.getSource('route').setData(geojson);
    }
    // otherwise, we'll make a new request
    else {
      map.addLayer({
        id: 'route',
        type: 'line',
        source: {
          type: 'geojson',
          data: geojson
        },
        layout: {
          'line-join': 'round',
          'line-cap': 'round'
        },
        paint: {
          'line-color': '#3887be',
          'line-width': 5,
          'line-opacity': 0.75
        }
      });
    }

    // get the sidebar and add the instructions
    const instructions = document.getElementById('instructions');
    const steps = data.legs[0].steps;

    let tripInstructions = '';
    for (const step of steps) {
    tripInstructions += `<li>${step.maneuver.instruction}</li>`;
    }
    instructions.innerHTML = `<p><strong>Temps de trajet: ${Math.floor(
    data.duration / 60
    )} min ${emoji} </strong></p><ol>${tripInstructions}</ol>`;
}
  
map.on('load', () => {
    // Create the route between start and end point
    getRoute(startCoordinate, endCoordinate);


    // Add starting point to the map
    map.addLayer({
        'id': 'startPoint',
        'type': 'circle',
        'source': {
          'type': 'geojson',
          'data': {
            'type': 'FeatureCollection',
            'features': [
              {
                'type': 'Feature',
                'properties': {},
                'geometry': {
                  'type': 'Point',
                  'coordinates': startCoordinate
                }
              }
            ]
          }
        },
        'paint': {
          'circle-radius': 5,
          'circle-color': '#1D3FBF'
        }
      });

    // Add ending point to the map
    map.addLayer({
        'id': 'endPoint',
        'type': 'circle',
        'source': {
          'type': 'geojson',
          'data': {
            'type': 'FeatureCollection',
            'features': [
              {
                'type': 'Feature',
                'properties': {},
                'geometry': {
                  'type': 'Point',
                  'coordinates': endCoordinate
                }
              }
            ]
          }
        },
        'paint': {
          'circle-radius': 5,
          'circle-color': '#C73643'
        }
      });
});
