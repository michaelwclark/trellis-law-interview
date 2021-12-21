<template>
  <div class="main">
    <input type="number" v-model="number" />
    <button @click="getNumberString">GET</button>
    <button @click="postNumberString" >POST</button>
    <div class="loading" v-if="loading">Loading...</div>
    <div class="result" v-if="result">{{numberString}}</div>
  </div>
</template>

<script>
import NumberService from '@/services/NumberService'
import {timeout} from '@/utils'
export default {
  name: 'HelloWorld',
  data() {
    return {
      numberInuput: '',
      numbserString: '',
      loading: false
    }
  },
  methods:{
    async getNumberString () {
      this.loading = true;
      const result = await NumberService.get({
        number: this.number
      })

      this.loading = false;
      this.numberString = result;
    },
    async postNumberString (){
      this.loading = true;
      const result = await NumberService.post({
        number: this.number
      })
      await timeout(5000);
      this.loading = false;
      this.numberString = result;
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
</style>
