// Wait for the Google Maps API to load
 // Callback function to initialize the map and add markers
    function initMap() {

      // Get the map element
      const mapElement = document.getElementById('map');
      const map = mapElement.innerMap; // Access the underlying Map object

      // Define the addresses you want to mark
      const addresses = [
        "1600 Amphitheatre Parkway, Mountain View, CA",
        "1 Infinite Loop, Cupertino, CA",
        "350 5th Ave, New York, NY"
      ];

      // Geocoder to convert addresses to coordinates
      const geocoder = new google.maps.Geocoder();

      // Loop through the addresses and add markers
      addresses.forEach(address => {
        geocoder.geocode({ address: address }, (results, status) => {
          if (status === "OK") {
            const location = results[0].geometry.location;
            new google.maps.marker.AdvancedMarkerElement({
              map: map,
              position: location,
              title: address
            });
          } else {
            console.error("Geocode was not successful for the following reason: " + status);
          }
        });
      });
    }
