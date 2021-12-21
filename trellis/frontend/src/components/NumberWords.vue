<template>
  <div class="main">
    <input type="number" :disabled="loading" v-model="number" />
    <button @click="getNumberString" :disabled="loading">GET</button>
    <button @click="postNumberString" :disabled="loading" >POST</button>
    <Loader v-if="loading" />
    <div class="error" v-if="error">{{ errorString }}</div>
    <div class="result" v-if="numberString" >{{ numberString }}</div>
  </div>
</template>

<script>
import NumberService from '@/services/NumberService'
import Loader from '@/components/Loader'
import {timeout} from '@/utils'
export default {
  name: 'NumberWords',
  components:{
    Loader
  },
  data() {
    return {
      numberInuput: '',
      numberString: '',
      loading: false,
      number: null,
      error: false,
      errorString: '',
    }
  },
  methods:{
    defaultState() {
      this.loading = true;
      this.numberString = '';
      this.error = false;
      this.errorString = '';
    },
    hanldeResponse({ status, message, num_in_english}){
      this.error = status === 'error'
      this.errorString = message
      this.numberString = num_in_english
      this.loading = false;
    },
    async getNumberString () {
      this.defaultState()
      const response = await NumberService.get({
        number: this.number
      })
      this.hanldeResponse(response)
    },
    async postNumberString (){
      this.defaultState()
      const response = await NumberService.get({
        number: this.number
      })
      await timeout(5);
      this.hanldeResponse(response)
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.error {
  color: red;
}
</style>
