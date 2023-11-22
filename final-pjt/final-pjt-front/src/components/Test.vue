<template>
  <div id="container">
    <div>
      <select v-model="selectedProvince" @change="updateCityOptions">
        <option v-for="province in provinces" :value = "province" :key="province">{{ province }}</option>
      </select>
      <br>
      <!-- <div>{{  cities[selectedProvince] }}</div> -->
      <select v-model="selectedCity" @change="moveToCity">
          <option value="0">시/군/구</option>
        <option v-for="city in cities[selectedProvince]" :value = "city" :key="city">{{ city }}</option>
      </select>
    </div>
    <div id="map"></div>
    <div class="map_wrap">
      <div id="map" style="width:100%;height:100%;position:relative;overflow:hidden;"></div>
      <div id="menu_wrap" class="bg_white">
        <div class="option">
            <div class="button-group">
              <button @click="searchBanks">은행 찾기</button>
            </div>
        </div>
        <hr>
        <ul id="placesList"></ul>
        <div id="pagination"></div>
      </div>
    </div>

    <div id="pagination"></div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

let map = null;
const markers = ref([]);
let infowindow = ref(null)


const provinces = [
    '서울 특별시', '인천 광역시', '부산 광역시', '광주 광역시', '대구 광역시', '대전 광역시', '제주도', '경기도',
    '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상남도', '경상북도'
  ];
  let selectedProvince = ref(provinces[0]);
  
  const cities = {
      '서울 특별시': ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구', '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구'],
      '인천 광역시': ['강화군', '계양구', '남구', '남동구', '동구', '미추홀구', '부평구', '서구', '연수구', '중구'],
      '부산 광역시': ['강서구', '금정구', '남구', '동구', '동래구', '부산진구', '북구', '사상구', '사하구', '서구', '수영구', '연제구', '영도구', '중구', '해운대구', '기장군'],
      '광주 광역시': ['광산구', '서구', '남구', '동구', '북구'],
      '대구 광역시': ['달서구', '남구', '달성군', '동구', '북구', '서구', '수성구', '중구'],
      '대전 광역시': ['대덕구', '동구', '서구', '유성구', '중구'],
      '제주도': ['서귀포시', '제주시'],
      '경기도': ['가평군', '강화군', '고양시', '과천시', '광명시', '광주시', '구리시', '군포시', '김포시', '남양주시', '동두천시', '부천시', '성남시', '수원시', '시흥시', '안산시', '안성시', '안양시', '양주시', '양평군', '여주군', '여주시', '연천군', '오산시', '옹진군', '용인시', '의왕시', '의정부시', '이천시', '파주시', '평택시', '포천시', '하남시', '화성시', '인천시청'],
      '강원도': ['강릉시', '고성군', '동해시', '삼척시', '속초시', '양구군', '양양군', '영월군', '원주시', '인제군', '정선군', '철원군', '춘천시', '태백시', '평창군', '홍천군', '화천군', '횡성군'],
      '충청북도': ['청주시', '흥덕구', '충주시', '상당구', '청원구', '서원구', '제천시', '음성군', '진천군', '옥천군', '영동군', '증평군', '괴산군', '보은군', '단양군'],
      '충청남도': ['태안군', '서산시', '당진시', '아산시', '천안시', '예산군', '홍성군', '보령시', '청양군', '공주시', '부여군', '서천군', '계룡시', '논산시', '금산군'],
      '전라북도': ['군산시', '익산시', '전주시', '정읍시', '남원시', '김제시', '완주군', '진안군', '무주군', '장수군', '임실군', '순창군', '고창군', '부안군'],
      '전라남도': ['목포시', '여수시', '순천시', '나주시', '광양시', '담양군', '곡성군', '구례군', '고흥군', '보성군', '화순군', '장흥군', '강진군', '해남군', '영암군', '무안군', '함평군', '영광군', '장성군', '완도군', '진도군', '신안군'],
      '경상남도': ['거창군', '함양군', '산청군', '하동군', '합천군', '의령군', '진주시', '사천시', '남해군', '창녕군', '함안군', '고성군', '통영시', '밀양시', '창원시', '거제시', '김해시', '양산시'],
      '경상북도': ['포항시', '경주시', '김천시', '안동시', '구미시', '영주시', '영천시', '상주시', '문경시', '경산시', '군위군', '의성군', '청송군', '영양군', '영덕군', '청도군', '고령군', '성주군', '칠곡군', '예천군', '봉화군', '울진군', '울릉군'],
      // 각 지역의 시/군/구 목록을 추가
  };
  let selectedCity = ref(0);

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

const fixedLevel = 3;

function initMap() {
  const container = document.getElementById('map');
  const mapOption = {
    center: new kakao.maps.LatLng(37.566826, 126.9786567),
    level: fixedLevel
  };
  map = new kakao.maps.Map(container, mapOption);
}

function searchBanks() {
  if (!selectedCity) return;
  map.setLevel(3)
  markers.value.forEach(marker => {
        marker.setMap(null);
    });
    markers.value = []

  const ps = new kakao.maps.services.Places(map);
  ps.categorySearch('BK9', placesSearchCB, { useMapBounds: true });
}

function placesSearchCB(data, status, pagination) {
  if (status === kakao.maps.services.Status.OK) {
    displayPlaces(data);
    displayPagination(pagination);

  }
}

const callback = function(marker, title, itemEl) {
  
    kakao.maps.event.addListener(marker, 'mouseover', function() {
      console.log(1)
      displayInfowindow(marker, title);
    });
    kakao.maps.event.addListener(marker, 'mouseout', function() {
            infowindow.close();
    })
    itemEl.onmouseover =  function () {
      displayInfowindow(marker, title);
    };
    itemEl.onmouseout =  function () {
        infowindow.close();
    };

  }
function displayPlaces(places) {
    const listEl = document.getElementById('placesList')
    const menuEl = document.getElementById('menu_wrap')
    const fragment = document.createDocumentFragment()
    const bounds = new kakao.maps.LatLngBounds()
    let listStr = ''

    removeAllChildNods(listEl);

    for (let i = 0; i < places.length; i++) {
      // const placePosition = new kakao.maps.LatLng(36, 127);
      const placePosition = new kakao.maps.LatLng(places[i].y, places[i].x);
      const marker = addMarker(placePosition, i);
      const itemEl = getListItem(i, places[i]);
      // console.log(placePosition)
      bounds.extend(new kakao.maps.LatLng(places[i].y, places[i].x))

      console.log(map.getLevel())

  

      callback(marker, places[i].place_name, itemEl)

      fragment.appendChild(itemEl);
    }
    map.setLevel(3)
    
    listEl.appendChild(fragment);
    menuEl.scrollTop = 0;
    map.setBounds(bounds);
}


function getListItem(index, places) {

  let el = document.createElement('li'),
  itemStr = '<span class="markerbg marker_' + (index+1) + '"></span>' +
              '<div class="info">' +
              '   <h5>' + places.place_name + '</h5>';

  if (places.road_address_name) {
      itemStr += '    <span>' + places.road_address_name + '</span>' +
                  '   <span class="jibun gray">' +  places.address_name  + '</span>';
  } else {
      itemStr += '    <span>' +  places.address_name  + '</span>'; 
  }
              
    itemStr += '  <span class="tel">' + places.phone  + '</span>' +
              '</div>';           

  el.innerHTML = itemStr;
  el.className = 'item';

  return el;
}


function addMarker(position, idx, title) {
    const imageSrc = 'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png', // 마커 이미지 url, 스프라이트 이미지를 씁니다
        imageSize = new kakao.maps.Size(36, 37),  // 마커 이미지의 크기
        imgOptions =  {
            spriteSize : new kakao.maps.Size(36, 691), // 스프라이트 이미지의 크기
            spriteOrigin : new kakao.maps.Point(0, (idx*46)+10), // 스프라이트 이미지 중 사용할 영역의 좌상단 좌표
            offset: new kakao.maps.Point(13, 37) // 마커 좌표에 일치시킬 이미지 내에서의 좌표
        },
        markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imgOptions),
            marker = new kakao.maps.Marker({
            position: position, // 마커의 위치
            image: markerImage 
        });

    marker.setMap(map); // 지도 위에 마커를 표출합니다
    markers.value.push(marker);  // 배열에 생성된 마커를 추가합니다

    return marker;
}


function updateCityOptions() {
  console.log(selectedProvince)
  selectedCity.value = 0;
}


function displayPagination(pagination) {
  const paginationEl = document.getElementById('pagination')
  const fragment = document.createDocumentFragment()
  
  // 기존에 추가된 페이지번호를 삭제합니다
  while (paginationEl.hasChildNodes()) {
      paginationEl.removeChild (paginationEl.lastChild);
  }

  for (let i=1; i<=pagination.last; i++) {
      const el = document.createElement('a');
      el.href = "#";
      el.innerHTML = i;

      if (i===pagination.current) {
        el.className = 'on';
      } else {
          el.onclick = (function(i) {
              return function() {
                  pagination.gotoPage(i);
              }
          })(i);
      }

      fragment.appendChild(el);
  }
  paginationEl.appendChild(fragment);
}

function displayInfowindow(marker, title) {
    const content = '<div style="padding:5px;z-index:1;">' + title + '</div>';
    infowindow = new kakao.maps.InfoWindow({ zIndex: 1 })
    infowindow.setContent(content);
    infowindow.open(map, marker);
}

function removeAllChildNods(el) {   
    while (el.hasChildNodes()) {
        el.removeChild (el.lastChild);
    }
}

function moveToCity() {
  if (!selectedCity) return;
  console.log(selectedCity.value, selectedProvince.value)
  const geocoder = new kakao.maps.services.Geocoder();
  const callback = function(result, status) {
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
  margin-top: 70px;
}
</style>