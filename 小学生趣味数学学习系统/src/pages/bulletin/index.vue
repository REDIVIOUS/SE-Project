<template>
  <!-- 从数据库中提取消息的数据，并展示在页面上 -->
  <div class="container">
    <div class="title-div">
      <!-- 公告标题 -->
      <p class="title-para">{{title}}</p>
      <!-- 公告发布时间 -->
      <p class="time-para">发布时间:{{time}}</p>
      <!-- 公告标题、内容分割线 -->
      <div class="sep-div"></div>
    </div>
    <!-- 公告内容 -->
    <div style="font-size: 0.9em; text-indent: 2em;" v-html="context"></div>
  </div>
</template>

<style scoped>
.container{
  margin: 1em;
  display: block;
  padding: 0;
}
.title-div{
  margin-bottom: 0.5em;
}
.title-para{
  line-height: 2em;
  font-size: 1.5em; 
  text-align: center;
}
.time-para{
  font-size: 0.5em; 
  text-align: right;
}
.sep-div{
  height: 1px; 
  border-bottom: 1px gray dashed;
}
</style>

<script>
export default {
  data () {
    return {
      title: '', // 公告标题
      time: '', // 公告时间
      context: '' // 公告内容
    }
  },
  // 页面加载时，从数据库中调取公告并将标题、时间、内容变量赋值
  onLoad () {
    wx.cloud.database().collection('Notice').get({
      success: res => {
        this.title = res.data[0].data.title
        this.time = JSON.stringify(res.data[0].data.date)
        this.context = res.data[0].data.context
      }
    })
  }
}
</script>