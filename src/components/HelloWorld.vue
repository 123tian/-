<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>哈哈</h2>
    <div v-html="msg" :id=" id "></div>
    <div >
      {{number + 1}}
    </div>
    <p v-if="seen">试试就试试</p>
    <p v-else>大哥你赢了！</p>
    <p v-show="isShow">大哥你赢了！</p>

    <div v-n="4"></div>
    <a href="http://www.baidu.com" @click.stop="test7">去百度 </a>
    <h2>3.按键修饰符</h2>
    <h2>田名振</h2>
    <input type="text" @keyup.13="test">
    <input type="text" @keyup.space="test">
    <input type="text" @keyup="test">
    <div :class="[a1,a2]">

      我借你{{money}},你还我{{h}},还剩{{s}}
    </div>
    <div :class="{'test-1':a3}">

      style object
    </div>

    <div :class="obj"></div>

    <ul>
      <li v-for="(item,idx) in list" :key="item">
        {{item}},{{idx}}
      </li>
    </ul>

    <ul>
      <template v-for="item in list">
        <li :key="item">hello</li>
        <li :key="item+1">{{item}}</li>
      </template>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: '<span style="color: #42b983">瞅你咋地</span>',
      id: 'txt',
      number: '1',
      seen: true,
      isShow: false,
      username: 100,
      h: 1,
      al: 'test-1',
      a2: 'test-2',
      a3: true,
      obj: {
        'test-1': false
      },
      list: ['a', 'b', 'c', 'd']
    }
  },
  methods: {
    test () {
      alert('aaa')
    }
  },
  computed: {
    s: function () {
      return this.money + this.h
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
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
