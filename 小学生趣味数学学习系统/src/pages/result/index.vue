<template>
  <div style="margin: 1%;">
    <!-- 做题结果区域 -->
    <div style="margin: 0.5em 0 0.5em 0; background-color: #efefef;">
      <p style="font-size: 1.5em; text-align: center; padding-bottom: 0.3em;">本次做题结果</p>
      <ul style="margin: 0 4em 0 4em; text-align: center; font-size: 0.9em;">
        <!-- 展示本次做题数目、正确题目数目、错误题目数目以及正确率 -->
        <li class="res-li"><p>本次做题数:</p><p>{{totalNum}}</p></li>
        <li class="res-li"><p>正确数目:</p><p>{{correctNum}}</p></li>
        <li class="res-li"><p>错误数目:</p><p>{{wrongNum}}</p></li>
        <li class="res-li"><p>正确率:</p><p>{{correctRatio}}</p></li>
      </ul>
    </div>
    <div>
      <input style="width: 80%; height: 2em; line-height: 2em; border-radius: 0.2em; background-color: lightgreen;" type="button" value="下一单元" />
    </div>
    <!-- 做题反馈区域 -->
    <div style="margin: 0.5em 0 0.5em 0; background-color: #efefef;">
      <p style="font-size: 1.5em; text-align: center; padding-bottom: 0.3em;">本次做题反馈</p>
      <!-- 将所有的结果显示在界面上 -->
      <ul v-for="res in results">
        <li class="ans-li">
          <div class="ans-bar"></div>
          <!-- 分别显示题目、用户答案、正确答案、如果正确显示对勾，否则显示叉 -->
          <div class="ans-div">
            <p>{{res.data.formula}}</p>
            <p>你的答案：{{res.data.yourAnswer}}</p>
            <p>正确答案：{{res.data.correctAnswer}}</p>
            <p v-if="res.data.correct">✓</p>
            <p v-else>✗</p>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
.res-li {
  display: flex;
  justify-content: space-between;
  padding: 0.2em 0 0.2em 0;
}
.ans-bar {
  height: 1px;
  border-top: 1px gray dashed;
}
.ans-div{
  display: flex;
  justify-content: space-around;
  height: 2em;
  line-height: 2em;
  font-size: 0.8em;
}
</style>

<script>
export default {
  data () {
    return {
      totalNum: 0, // 总做题数目
      correctNum: 0, // 正确个数
      wrongNum: 0, // 错误个数
      correctRatio: '', // 正确率
      results: [] // 存放从后端返回的结果
    }
  },
  // 开始加载页面时把之前后端比改的结果反馈回来
  onLoad () {
    wx.cloud.callFunction({
      name: 'showResult',
      success: res => {
        this.totalNum = res.data.data.totalNum
        this.correctNum = res.data.data.correctNum
        this.wrongNum = res.data.data.wrongNum
        this.correctRatio = res.data.data.correctRatio
        this.results = res.data.data.results
      }
    })
  }
}
</script>