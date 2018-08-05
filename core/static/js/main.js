var mymap = L.map('map').setView([-8.051016, -34.957108], 13);
L.tileLayer("http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {}).addTo(mymap);


var polygon_point = {};
var submission = [];
var polygon_points = [];
var polygon;
var marker;

function onMapClick(e) {
    polygon_point["lat"] = e.latlng.lat;
    polygon_point["lng"] = e.latlng.lng;
    marker = L.marker([polygon_point["lat"], polygon_point["lng"]]).addTo(mymap);
    polygon_points.push({ lat: polygon_point["lat"], lng: polygon_point["lng"]});
    drawPolygon(polygon_points);
}

function drawPolygon(polygon_points) {
    console.log(polygon_points);
    if (polygon_points.length > 2) {
        if (polygon != null) {
            polygon.remove();
        }
        polygon = L.polygon(polygon_points).addTo(mymap);
    }
}

mymap.on('click', onMapClick);