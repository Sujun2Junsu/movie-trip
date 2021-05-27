<template>
  <div class="container">
    <div class="row">
      <div @click="$router.go(-1)" class="text-light fas fa-arrow-left col-1 h1"></div>
      <div class="text-white h1 col-6 offset-2"><i class="fas fa-paper-plane"></i> 어디로 여행을 갈까요?</div>
      <!-- 아코디언 -->
      <div class="accordion col-3 d-none d-lg-block" id="accordionExample">
        <div class="accordion-item">
          <h2 class="accordion-header" id="headingOne">
            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
              사용방법
            </button>
          </h2>
          <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
            <div class="accordion-body">
              사용방법 : 지도 위의 확대버튼을 눌러 가고싶은 나라에 사람이 위치하게 한 후 '어디로 여행을 갈까요?' 버튼을 누르세요!
            </div>
          </div>
        </div>
      </div>
    <br>
    <br>
    <div id="parent">
      <div id="child"><i class="fas fa-running"></i></div>
      <vl-map :load-tiles-while-animating="true" :load-tiles-while-interacting="true" 
              data-projection="EPSG:4326" style="height: 400px">
        <vl-view :zoom.sync="zoom" :center.sync="center" :extent.sync="extent"></vl-view>
        <vl-layer-tile id="osm">
          <vl-source-osm></vl-source-osm>
        </vl-layer-tile>
      </vl-map>
      <div style="padding: 20px" class="text-light">
        현재 좌표 : {{ center }}<br><br>
      <button type="button" class="btn btn-primary" @click="getCountry">여기로 가요!</button>
      </div>
      <br>
      <h4 class="text-white" v-if="countryName">{{ countryName }}의 최신 추천 영화는?</h4>
    </div>
    <RecommendMovies
      :countryCode="countryCode"
    />
   </div>
  </div>
</template>

<script>
import Vue from 'vue'
import VueLayers from 'vuelayers'
import axios from 'axios'

import RecommendMovies from '@/components/Recommend/RecommendMovies'

Vue.use(VueLayers)

export default {
  name: 'Recommend',
  components: {
    RecommendMovies
  },
  data: function () {
    return { 
      zoom: 2,
      center: [0, 0],
      extent: [-180, -90, 180, 90],
      countryName: null,
      countryCode: null,
    }
  },
  methods: {
    getCountry: function () {
      axios({
        method: 'get',
        url: `https://api.bigdatacloud.net/data/reverse-geocode-client?latitude=${this.center[1]}&longitude=${this.center[0]}&localityLanguage=ko`
      })
        .then(res => {
          // console.log(res)
          this.countryName = res.data.localityInfo.administrative[0].isoName.split(' ')[0]
          this.getCountryCode()
        })
        .catch(err => {
          console.log(err)
        })
    },
    getCountryCode: function () {
      axios({
        method: 'get',
        url: 'http://kobis.or.kr/kobisopenapi/webservice/rest/code/searchCodeList.json?key=25082f603f83818090a9a2a338bc11da&comCode=2204'
      })
        .then(res => {
          // console.log(res)
          const countryList = res.data.codes
          for(var i in countryList) {
            if(countryList[i].engNm === this.countryName) {
              this.countryCode = parseInt(countryList[i].fullCd)
            } else if (this.countryName === 'Korea'){
              this.countryCode = 22041011
            } else if (this.countryName === 'United'){
              this.countryCode = 22042002
            } else if (this.countryName === 'Russian'){
              this.countryCode = 22044005
            }
          }
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style>
#parent {
  position: relative;
}
#child {
  position: absolute;
  top: 200px;
  left: 50%;
  z-index: 100;
}

.fa-running {
  font-size: 20px;
  color: rgb(214, 16, 214);
}

.fa-paper-plane {
  font-size: 40px;
  color: white;
}


</style>