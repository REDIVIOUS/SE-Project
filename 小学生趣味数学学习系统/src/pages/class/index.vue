<template>
  <div>
    <!-- 知识点学习难度显示结构（表头） -->
    <div class="title">
      <p class="title-text">十以内加法-简单</p>
    </div>
    <!-- 学习公式数量提示结构 -->
    <div class="learning-info">
      <p class="info1">本次即将学习</p>
      <p class="info2">
        <span style="color: red; font-size: 2.0em;">{{number}}</span>
        <span style="font-size: 0.8em;">个公式</span>
      </p>
    </div>
    <!-- 公式显示结构 -->
    <div class="learning-content">
      <p v-for="formula in formulas" class="formula">{{formula}}</p>
    </div>
    <!-- 进行跳转按钮结构 -->
    <div class="start-learning" @click="startLearning">
      <div class="button">
        <p class="button-value">我学会了</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.title{
  margin: 1%;
  background-color: #dddddd;
}
.title .title-text{
  font-size: 1.2em;
}
.learning-info .info1{
  text-indent: 5em;
}
.learning-info .info2{
  text-align: center;
}
.learning-content{
  flex-direction: column;
  margin: 1%;
  background-color: #efefef;
}
.learning-content .formula{
  text-align: center;
  padding: 1%;
}
.start-learning{
  display: flex;
  justify-content: center;
  margin: 2%;
}
.start-learning .button{
  width: 40%;
  height: 2em;
  background-color: #ff8800;
  border-radius: 1em;
}
.start-learning .button .button-value{
  text-align: center;
  line-height: 2em;
}
</style>

<script>
export default {
  // 学习界面所需的数据列表
  data () {
    return {
      data: null, // 公式个数
      formulas: [], // 公式列表
      number: this.getJsonLength(this.formulas) // 获取公式长度
    }
  },
  // 页面加载时，从数据库中调取知识点公式
  onLoad () {
    wx.cloud.database().collection('Knowledge').get({
      success: res => {
        this.formulas = res.data.data.formulas
      }
    })
  },
  methods: {
    // 跳转到学习页面
    startLearning () {
      mpvue.navigateTo({url: '/pages/exam/main'})
    }
  }
}
</script>
