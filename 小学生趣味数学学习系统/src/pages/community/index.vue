<template>
  <div>
    <div class="outer-div">
      <!-- 用户比赛排名展示区 -->
      <div class="ranking-div">
        <p class="ranking-title">比赛排名</p>
        <div class="table-div">
          <!-- 用户比赛排名展示表 -->
          <table class="ranking-table">
            <!-- 表头：包含用户排名，用户名，用户分数 -->
            <thead class="table-head">
              <tr class="table-row">
                <th class="table-cell">排名</th>
                <th class="table-cell-middle">用户名</th>
                <th class="table-cell">分数</th>
              </tr>
            </thead>
            <!-- 表格主体，显示不同用户比赛排名，一页五条数据 -->
            <tbody class="table-body">
              <tr class="table-row">
                <td class="table-body-cell">1</td>
                <td class="table-body-cell-middle">123</td>
                <td class="table-body-cell">8000</td>
              </tr>
              <tr class="table-row">
                <td class="table-body-cell">1</td>
                <td class="table-body-cell-middle">123</td>
                <td class="table-body-cell">8000</td>
              </tr>
              <tr class="table-row">
                <td class="table-body-cell">1</td>
                <td class="table-body-cell-middle">123</td>
                <td class="table-body-cell">8000</td>
              </tr>
              <tr class="table-row">
                <td class="table-body-cell">1</td>
                <td class="table-body-cell-middle">123</td>
                <td class="table-body-cell">8000</td>
              </tr>
              <tr class="table-row">
                <td class="table-body-cell">1</td>
                <td class="table-body-cell-middle">123</td>
                <td class="table-body-cell">8000</td>
              </tr>
            </tbody>
          </table>
        </div>
        <!-- 分页按钮 -->
        <div class="button-div">
          <!-- 回到首页按钮 -->
          <input class="page-button first-page-button" type="button" value="首页">
          <!-- 上一页按钮 -->
          <input class="page-button previous-page-button" type="button" value="上一页">
          <!-- 下一页按钮 -->
          <input class="page-button next-page-button" type="button" value="下一页">
          <!-- 末页按钮 -->
          <input class="page-button last-page-button" type="button" value="末页">
        </div>
      </div>
      <!-- 社区提问区域 -->
      <div class="question-div">
        <p class="question-title">社区提问</p>
        <div class="question-list-div">
          <ul class="question-list">
            <!-- 单条用户提问记录展示，点击该区域可以查看他人回答以及参与题目回答 -->
            <li class="question-unit" @click="gotoAnswer">
              <!-- 提问者用户名 -->
              <p class="question-user-name">456</p>
              <!-- 问题类型 -->
              <p class="question-type">简单</p>
              <!-- 问题类型 -->
              <p class="question-content">为什么1+1=2？</p>
            </li>
            <li class="question-unit">
              <p class="question-user-name">456</p>
              <p class="question-type">困难</p>
              <p class="question-content">为什么x^2-1=0的解是两个？</p>
            </li>
            <li class="question-unit">
              <p class="question-user-name">456</p>
              <p class="question-type">建议</p>
              <p class="question-content">建议加大题目难度。</p>
            </li>
          </ul>
        </div>
      </div>
    </div>
    <!-- 我要提问按钮，点击跳转到提问页面 -->
    <input class="ask-question-button" type="button" value="我要提问" @click="gotoAsking">
  </div>
</template>

<style scoped>
.outer-div{
  margin: 1em;
}
.ranking-div{
  padding-bottom: 1em;
  border-bottom: 1px black solid;
}
.ranking-title{
  font-size: 1.5em;
}
.table-div{
  margin: 1em 0 1em 0;
}
.ranking-table{
  border: 1.5px #efefef solid;
}
.table-head{
  background-color: #efefef;
}
.table-row{
  display: flex;
}
.table-cell{
  width: 20%;
  text-align: center;
  border: 1px solid #8f8f8f;
}
.table-cell-middle{
  width: 60%;
  text-align: center;
  border: 1px solid #8f8f8f;
}
.table-body-cell{
  height: 2em;
  line-height: 2em;
  width: 20%;
  text-align: center;
  border: 1px solid #8f8f8f;
}
.table-body-cell-middle{
  width: 60%;
  text-align: center;
  border: 1px solid #8f8f8f;
  height: 2em;
  line-height: 2em;
}
.button-div{
  display: flex;
  justify-content: center;
}
.page-button{
  font-size: 0.8em;
  line-height: inherit;
}
.question-div{
  padding-top: 1em;
  padding-bottom: 2em;
}
.question-title{
  font-size: 1.5em;
}
.question-list-div{
  margin: 1em 0 1em 0;
}
.question-unit{
  border: 1px #efefef solid;
  border-radius: 5px;
  padding: 0.5em;
  background-color: #efefef;
  margin: 0.5em 0 0.5em 0;
}
.question-user-name{
  font-size: 0.8em;
  text-indent: 0.8em;
}
.question-type{
  text-align: right;
  padding-right: 0.5em;
}
.question-content{
  width: 80%;
  border-top: 1px dashed #888;
  padding-left: 20%;
  /* text-indent: 5%; */
}
.ask-question-button{
  position: fixed;
  bottom: 0;
  width: 100%;
  border-radius: 0;
  background-color: #e64340;
  color: #ffffff;
}
</style>

<script>
export default {
  data () {
    return {

    }
  },
  methods: {
    // 跳转到回答界面
    gotoAnswer () {
      mpvue.navigateTo({url: '/pages/Answer/main'})
    },
    // 跳转到提问界面
    gotoAsking () {
      mpvue.navigateTo({url: '/pages/comment/main'})
    }
  }
}
</script>