<template>
  <div id="app">
    <img src="./assets/logo.png">
    <HelloWorld msg="<span>瞅你咋地!</span>"/>
  <ev/>
    <com :age="age" @patch="msg"/>
    <h1 slot="a">我要加东西</h1>
    <h1 slot="b">我要加东西</h1>
  </div>
</template>

<script>
  import HelloWorld from './components/HelloWorld'
  import ev from './components/Events'
  import com from './components/con['
  import './components/n'

export default {
  name: 'App',
  components: {
    HelloWorld,
    ev,
    com
  },
  data () {
    return{
      age: 18
    }
  },
  methods: {
    msg: function () {
      // console.log('msg')
      this.age++
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
