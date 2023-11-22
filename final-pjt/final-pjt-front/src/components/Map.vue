<template>
  <div id="container" class="container">
    <h3>주변 은행 찾기</h3>
    <div id="map" class="mb-4"></div>
    <div class="button-group">
      <button @click="searchBanks" class="btn btn-primary">Search Banks</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

let map = null;
const markers = ref([]);
let infowindow = null

onMounted(() => {
  if (window.kakao && window.kakao.maps) {
    initMap();
  } else {
    const script = document.createElement('script');
    script.onload = () => kakao.maps.load(initMap);
    script.src =
    '//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=aebb8fdf97a41cbceffbd0cdd97ba9e1&libraries=services,clusterer,drawing';
    document.head.appendChild(script);
  }
});

function initMap() {
  const container = document.getElementById('map');
  let mapOption = {
    center: new kakao.maps.LatLng(37.566826, 126.9786567),
    level: 3
  };
  map = new kakao.maps.Map(container, mapOption);
  // let ps = new kakao.maps.services.Places(map);
  // ps.categorySearch('BK9', placesSearchCB, { useMapBounds: true });
}

function searchBanks() {
  let ps = new kakao.maps.services.Places(map);
  ps.categorySearch('BK9', placesSearchCB, { useMapBounds: true });
}


function placesSearchCB(data, status, pagination) {
  // console.log(data)
  if (status === kakao.maps.services.Status.OK) {
    const bounds = new kakao.maps.LatLngBounds();
    markers.value = []
    for (let i = 0; i < data.length; i++) {
      const marker = displayMarker(data[i]);
      markers.value.push(marker);
      // displayMarker(data[i]);
      bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
    }  
    map.setBounds(bounds);
      }
    }
    
    
    function displayMarker(place) {
      // if (!map) return;
      
      const marker = new kakao.maps.Marker({
        map: map,
        position: new kakao.maps.LatLng(place.y, place.x)
      });
      infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });
      // console.log(infowindow)
      kakao.maps.event.addListener(marker, 'click', function() {
        infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>');
        infowindow.open(map, marker);
  });
  return marker
}


</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#map {
  width: 400px;
  height: 400px;
}

.button-group {
  margin: 10px 0px;
}

button {
  margin: 0 3px;
}

#container {
  margin-top: 100px;
}
</style>
