
window.onload = init;
function init(){

//Controls
const mousePositionControl = new ol.control.MousePosition();
const zoomSliderControl = new ol.control.ZoomSlider();
const zoomToExtentControl = new ol.control.ZoomToExtent();


  const map = new ol.Map({
    view: new ol.View({
      center: ol.proj.fromLonLat([17.193456, 44.776321]),
      zoom: 13,
      maxZoom: 20,
      minZoom: 3,
      rotation: 0

    }),
    layers: [
      new ol.layer.Tile({
        source: new ol.source.OSM({
          layer :"terrain"
        })
      })
    ],
    target: 'js-map',
    keyboardEventTarget: document,
    controls: ol.control.defaults().extend([
        mousePositionControl,
        zoomSliderControl,
        zoomToExtentControl
    ]),
  })

  //map.on("click", function (e) {
    //console.log(e.coordinate)
    //c1 = e.coordinate[0];
    //c2 = e.coordinate[1];
//});

}
