<template>
  <div class="com">
    <slot name="a"/>
    child compontes
    {{name}}  {{age}}

    <button type="button" @click="$emit('patch')"> 发送打</button>
    <slot name="b"/>
  </div>

</template>

<script>
  export default {
    props:['age'],
    data () {
      return{



    name: 'con['
       }
        }
  }
</script>

<style scoped>

</style>
