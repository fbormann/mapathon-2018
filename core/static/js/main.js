var mymap = L.map('map').setView([-8.051016, -34.957108], 13);
L.tileLayer("http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {}).addTo(mymap);


var polygon_point = {};
var submission = [];
var polygon_points = [];
var polygon;
var markers = [];

function onMapClick(e) {
    polygon_point["lat"] = e.latlng.lat;
    polygon_point["lng"] = e.latlng.lng;
    marker = L.marker([polygon_point["lat"], polygon_point["lng"]]).addTo(mymap);
    markers.push(marker);
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

function erasePolygon() {
    polygon.remove();
    polygon_points = [];
    for (let i = 0; i < markers.length; i++) {
        markers[i].remove();
    }
}

mymap.on('click', onMapClick);

/** form code */

var form = $('#competition-form');
var submission_values = {};

form.submit(function(e) {
    $(e).preventDefault();

    form_object = $(this)[0];
    submission_values["competition_name"] = form_object[0].value;
    submission_values["competition_goal"] = form_object[1].value;
    sendData();
});

function sendData() {

    submission_values["polygon_points"] = JSON.stringify(polygon_points);
    console.log(polygon_points)
    $.post("competitions/create", submission_values ,function( response ) {
        console.log(response);
    });
}