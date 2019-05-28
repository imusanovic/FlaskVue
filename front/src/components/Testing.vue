<template>
  <div>
    <div class="container">
        <h1>{{ data.ime }} {{ data.prezime }}</h1>
        <h2>Adresa: {{ data.adresa.ulica }} {{ data.adresa.broj }}, {{ data.adresa.grad }}</h2>
        <h2>Mobitel: {{ data.mobitel }}</h2>
    </div>
  </div>
</template>

<style>
    #app{
        margin-top:60px;
    }
</style>

<script>
import axios from 'axios';

export default {
  name: 'Test',
  data() {
    return {
      data: '',
    };
  },
  methods: {
    testing() {
        const endpoint = '//localhost:5000/test'
        axios.get(endpoint).then((res) => {
            this.data = res.data;
        })
        .catch((error) => {
            console.error(error);
        })
    }
  },
  created(){
    this.testing();
  }
};
</script>
