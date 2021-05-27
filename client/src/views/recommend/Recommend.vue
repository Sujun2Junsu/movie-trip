<template>
  <div class="container">
    <p class="text-white h1"><i class="fas fa-paper-plane"></i> 어디로 여행을 갈까요?</p>
    <div id="parent">
      <div id="child"><i class="fas fa-running"></i></div>
      <vl-map :load-tiles-while-animating="true" :load-tiles-while-interacting="true" 
              data-projection="EPSG:4326" style="height: 400px">
        <vl-view :zoom.sync="zoom" :center.sync="center" :extent.sync="extent"></vl-view>
        <vl-layer-tile id="osm">
          <vl-source-osm></vl-source-osm>
        </vl-layer-tile>
      </vl-map>
      <div style="padding: 20px" class="text-white">
        현재 좌표 : {{ center }}<br><br>
      <button type="button" class="btn btn-primary" @click="getCountry">여기로 가요!</button>
      </div>
      <h4 class="text-white" v-if="countryName">{{ countryName }}의 최신 추천 영화는?</h4>
    </div>
    <RecommendMovies
      :countryCode="countryCode"
    />
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