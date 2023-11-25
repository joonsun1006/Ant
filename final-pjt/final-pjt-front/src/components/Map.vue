<template>
  <div id="container">
  <div
    style="
      padding-top: 30px;
      justify-content: space-between;
      width: 1300px;
      margin: 0 auto;
    "
  >
    <span class="fs-2 fw-bold">은행 찾기</span>
    <hr style="margin: 0px; margin-bottom: 25px; border: 2px solid #001476" />
  </div>

  <div
    class="d-flex"
    style="justify-content: space-between; width: 1300px; margin: 0 auto"
  >
    <div class="search-box">
      <div class="input-group mb-5" style="width: 350px">
        <span class="input-group-text" id="basic-addon1">광역시 / 도</span>
        <select
          class="form-select"
          aria-label="Default select example"
          style="width: 100px"
          @change="updateCityOptions"
          v-model="selectedProvince"
        >
          <option v-for="state in localList.mapInfo">
            {{ state.name }}
          </option>
        </select>
      </div>

      <div class="input-group mb-5" style="width: 350px">
        <span class="input-group-text" id="basic-addon1">시 / 군 / 구</span>
        <select
          class="form-select"
          aria-label="Default select example"
          style="width: 100px"
          @change="moveToCity"
          v-model="selectedCity"
        >
          <template v-for="state in localList.mapInfo">
            <template v-if="state.name === selectedProvince">
              <option v-for="country in state.countries">
                {{ country }}
              </option>
            </template>
          </template>
        </select>
      </div>

      <button
        type="button"
        class="btn text-white fw-bold"
        @click="searchBanks"
        style="width: 350px; background-color: #001476; margin-bottom: 50px;"
      >
        찾기
      </button>

      <div class="map_wrap bank-list-box">
        <div id="menu_wrap" class="bg-white p-3">
          <ul id="placesList" class="list-group"></ul>
          <div id="pagination" class="mt-3"></div>
        </div>
      </div>

    </div>
    <div class="col-md-8 d-flex">
      <div id="map" class="mb-3 ms-auto"></div>
    </div>
  </div>
</div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import localdata from "@/assets/localdata.json";

const localList = localdata;

let map = null;
const markers = ref([]);
let infowindow = ref(null);

const selectedProvince = ref("");
const selectedCity = ref("");

onMounted(() => {
  if (window.kakao && window.kakao.maps) {
    initMap();
  } else {
    const script = document.createElement("script");
    script.onload = () => kakao.maps.load(initMap);
    script.src =
      "//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=aebb8fdf97a41cbceffbd0cdd97ba9e1&libraries=services,clusterer,drawing";
    document.head.appendChild(script);
  }
});

const fixedLevel = 3;

function initMap() {
  const container = document.getElementById("map");
  const mapOption = {
    center: new kakao.maps.LatLng(37.566826, 126.9786567),
    level: fixedLevel,
  };
  map = new kakao.maps.Map(container, mapOption);
}

function searchBanks() {
  if (!selectedCity) return;
  map.setLevel(3);
  markers.value.forEach((marker) => {
    marker.setMap(null);
  });
  markers.value = [];

  const ps = new kakao.maps.services.Places(map);
  ps.categorySearch("BK9", placesSearchCB, { useMapBounds: true });
}

function placesSearchCB(data, status) {
  if (status === kakao.maps.services.Status.OK) {
    displayPlaces(data);
  }
}

const callback = function (marker, title, itemEl) {
  kakao.maps.event.addListener(marker, "mouseover", function () {
    displayInfowindow(marker, title);
  });
  kakao.maps.event.addListener(marker, "mouseout", function () {
    infowindow.close();
  });
  itemEl.onmouseover = function () {
    displayInfowindow(marker, title);
  };
  itemEl.onmouseout = function () {
    infowindow.close();
  };
};
function displayPlaces(places) {
  const listEl = document.getElementById("placesList");
  const menuEl = document.getElementById("menu_wrap");
  const fragment = document.createDocumentFragment();
  const bounds = new kakao.maps.LatLngBounds();
  let listStr = "";

  removeAllChildNods(listEl);

  for (let i = 0; i < places.length; i++) {
    // const placePosition = new kakao.maps.LatLng(36, 127);
    const placePosition = new kakao.maps.LatLng(places[i].y, places[i].x);
    const marker = addMarker(placePosition, i);
    const itemEl = getListItem(i, places[i]);
    itemEl.classList.add("d-flex")
    itemEl.classList.add("mb-5")
    bounds.extend(new kakao.maps.LatLng(places[i].y, places[i].x));

    callback(marker, places[i].place_name, itemEl);

    fragment.appendChild(itemEl);
    console.log(itemEl)
  }
  map.setLevel(3);

  listEl.appendChild(fragment);
  map.setBounds(bounds);
}

function getListItem(index, places) {
  let el = document.createElement("li"),
    itemStr =
      '<div class="markerbg marker_' +
      (index + 1) +
      '"></div>' +
      '<div class="info d-flex flex-column">' +
      '   <div class="fs-4 fw-bold">' +
      (index+1)+'.'+places.place_name +
      "</div>";

  if (places.road_address_name) {
    itemStr +=
      '<span class="fw-medium" style="color: gray"><span class="fs-5 fw-bold" >도로명: </span>' +
      places.road_address_name +
      "</span>" +
      '   <span class="jibun gray fw-medium" style="color: gray"><span class="fs-5 fw-bold">지번: </span>' +
      places.address_name +
      "</span>";
  } else {
    itemStr += "    <span>" + places.address_name + "</span>";
  }

  itemStr += '  <span class="tel fw-medium" style="color: gray"><span class="fs-5 fw-bold">Tel. </span> ' + places.phone + '</span>' + "</div>";
  el.innerHTML = itemStr;
  el.className = "item";

  return el;
}

function addMarker(position, idx, title) {
  const imageSrc =
      "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png", // 마커 이미지 url, 스프라이트 이미지를 씁니다
    imageSize = new kakao.maps.Size(36, 37), // 마커 이미지의 크기
    imgOptions = {
      spriteSize: new kakao.maps.Size(36, 691), // 스프라이트 이미지의 크기
      spriteOrigin: new kakao.maps.Point(0, idx * 46 + 10), // 스프라이트 이미지 중 사용할 영역의 좌상단 좌표
      offset: new kakao.maps.Point(13, 37), // 마커 좌표에 일치시킬 이미지 내에서의 좌표
    },
    markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imgOptions),
    marker = new kakao.maps.Marker({
      position: position, // 마커의 위치
      image: markerImage,
    });

  marker.setMap(map); // 지도 위에 마커를 표출합니다
  markers.value.push(marker); // 배열에 생성된 마커를 추가합니다

  return marker;
}

function updateCityOptions() {
  selectedCity.value = 0;
}



function displayInfowindow(marker, title) {
  const content =
    '<div style="padding:5px;z-index:1;height:60px; width:100px; font-size:12px;">' +
    title +
    "</div>";
  infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });
  infowindow.setContent(content);
  infowindow.open(map, marker);
}

function removeAllChildNods(el) {
  while (el.hasChildNodes()) {
    el.removeChild(el.lastChild);
  }
}

function moveToCity() {
  if (!selectedCity) return;

  const geocoder = new kakao.maps.services.Geocoder();
  const callback = function (result, status) {
    if (status === kakao.maps.services.Status.OK) {
      const position = new kakao.maps.LatLng(result[0].y, result[0].x);
      map.panTo(position);
    }
  };

  geocoder.addressSearch(selectedProvince.value + selectedCity.value, callback);
}
</script>

<style scoped>
#map {
  width: 900px;
  height: 700px;
  position: relative;
  overflow: hidden;
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

.list-group-item {
  cursor: pointer;
}

.list-group-item:hover {
  background-color: #f8f9fa;
}

.bank-list-box {
  border: 1px solid lightgray;
  border-radius: 20px;
  width: 350px;
  padding: 15px;
  height: auto;
}
.search-box {
  border: 1px solid white;
  border-radius: 10px;
  width: 300px;
  height: 800px;
}

#menu_wrap {
  overflow-y: auto;
  max-height: 400px;
}

#container {
  margin-top: 40px;
}

</style>