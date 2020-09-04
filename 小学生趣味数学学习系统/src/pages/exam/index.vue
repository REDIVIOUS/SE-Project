<template>
  <view class="container">
    <!-- 所有题目展示区域 -->
    <view v-for="exam in exams" style="width: 100%">
      <view class="color-bar"></view>
      <view class="version">
        <!-- 问题题干 -->
        <p class="text-part">{{ exam }}</p>
        <!-- 问题输入 -->
        <input class="input-part" type="text" v-bind="inputs" />
      </view>
    </view>
    <view class="color-bar"></view>
    <!-- 对输入进行检测，如果有错误发出警告 -->
    <p style="color: red;">{{alert}}</p>
    <!-- 提交题目按钮 -->
    <button class="next-unit-button" @click="checkResults">提交题目</button>
  </view>
</template>

<style scoped>
.container {
  min-height: 100%;
  overflow: hidden;
  overflow-y: hidden;
  padding: 0;
}
.heading {
  height: 40rpx;
  width: 100%;
  font-size: 40rpx;
  font-weight: blod;
  text-align: center;
  padding: 20rpx;
}
.color-bar{
  height: 20rpx;
  background: #eee;
  width: 100%;
}
.version {
  width: 100%;
  height: 2em;
  padding: 1em;
  font-size: 24rpx;
  text-align: center;
  display: flex;
  justify-content: center;
}
.version .text-part{
  font-size: 1.2em;
  font-weight: 700;
  line-height: 2em;
}
.version .input-part{
  border: 1px #dddddd solid;
  width: 10%;
  margin-left: 1em;
}
.next-unit-button{
   width: 100%;
   background: #ff8800;
   border-radius: 1em;
}
</style>

<script>
export default {
  data () {
    return {
      exams: [], // 
      inputs: [],
      datas: [],
      alert: ''
    }
  },
  methods: {
    // 对输入进行检测，如果有未答完题目、输入中有非法字符、输入数值越界，则在页面显示警告
    getInput () {
      var i=0;
      var regex = '/^(-){0, 1}\\d+$/'
      for (i=0;i<inputs.length();i++){
        if (regex.strip().length() == 0){
          this.alert = '你有未答完的题目'
          break
        } else if (!regex.match(inputs[i])) {
          this.alert = '输入中含有非法字符'
          break
        } else if (inputs[i] < 0 || inputs[i] > 65536) {
          this.alert = '输入数值越界'
          break
        } else {
          data.append(inputs[i])
        }
      }
      if(i==10){
        this.markTest()
      }
    },
    // 将数据交到后端进行检查，如果后端接受跳转到结果页，否则根据后端返回的错误来显示警告
    markTest () {
      wx.cloud.callFunction({
        name: 'markTest',
        data: {
          data: this.datas
        },
        success: res => {
          if(res.data.data.accept){
            mpvue.navigateTo({url: '/pages/result/main'})
          } else {
            this.alert = res.data.data.alert
          }
        }
      })
    }
  }
}
</script>
