
function initMap(){
    //Map options
    var options = {
        zoom: 8,
        center: {lat:44.3601, lng:17.0589}
    }
    //New map
    var map = new
    google.maps.Map(document.getElementById('map'), options);

    //Listen on click on map

    google.maps.event.addListener(map, 'click',
    function(event){
        addMarker({coords:event.latLng});
    })


    addMarker({
        coords:{lat:42.4668, lng:-70.9495},
        iconImage: "https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png",
        content:'<h1>Lynn MA</h1>'
    });
    addMarker({coords:{lat:42.8584, lng:-70.9300},
    content:'<h1>AmesburyYYY MA</h1>'
    });
    addMarker({coords:{lat:42.7762, lng:-71.0773}});


    //Add Marker function
    function addMarker(props){
        var marker = new google.maps.Marker({
        position:props.coords,
        map:map,
        //icon:props.iconImage
    });

        if(props.iconImage){
            marker.setIcon(props.iconImage)
        }

        if(props,content){
            var infoWindow = new google.maps.InfoWindow({
                content:props.content
            });
        
            marker.addListener('click', function(){
                infoWindow.open(map, marker);
            });
        }

    }
}