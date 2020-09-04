<template>
  <!-- 得到用户信息数据以及一些公式 -->
  <div @click="clickHandle">
    <!-- 改成模板使用 -->
    <!--default模式-->
    <div class="regular-mode" :style="{'left': leftStart}">
      <!-- 设置区域 -->
      <div class="settings-area">
        <!-- 设置按钮 -->
        <img class="settings-img" src="/static/images/settings.png" mode="aspectFit" @click="openSettings"/>
      </div>
      <!-- 显示排名区域 -->
      <div class="ranking-area">
        <!-- 显示排名按钮 -->
        <img class="ranking-img" src="/static/images/leaderboard-80.png" mode="aspectFit" @click="openRanking"/>
      </div>
      <!-- 排名区 -->
      <div class="bulletin-area" @click="gotoBulletin">
        <img class="bulletin-img" src="/static/images/horn.png" mode="aspectFit" />
        <p class="today-news">今日公告:{{ news }}</p>
      </div>
      <!-- 显示学习时间 -->
      <div class="infomation-area">
        <p style="line-height: 3em; text-align: center;">已经学习</p>
        <div style="justify-content: center; display: flex;">
          <p v-if="notLoggedin" style="font-size: 0.8em; text-align: center; padding-top: 2em;">登陆以查看学习天数</p>
          <p v-else style="text-align: center;">
            <span style="font-size: 3em; color: red;">{{learningDays}}</span>
            <span style="font-size: 0.8em;">天</span>
          </p>
          <div class="calendar-div" style="width: 3em; right: 3em; height: 5em; position: absolute;" @click="checkLearned">
            <img style="width: 3em; height: 4em; position: absolute;" class="calendar-img" src="/static/images/calendar-80-1.png" mode="aspectFit"/>
            <p style="position: absolute; text-align: center; line-height: 4em; z-index: ; width: inherit;">{{dateToday}}</p>
            <p v-if="notLoggedin" class="notLogin" style="font-size: 0.5em; text-align: center; margin-top: 5.5em;">请先登录</p>
            <p v-else style="font-size: 0.5em; text-align: center; margin-top: 5.5em;"><span>点击</span><br/><span>学习/打卡</span></p>
          </div>
        </div>
      </div>
      <!-- 学前测试 -->
      <div class="test-area" @click="gotoExam">
        <img src="/static/images/th.jpg" />
          <p v-if="notLoggedin" style="position: absolute; color: white; padding: 1.2em;">请先登录再测试</p>
          <div v-else style="position: absolute; height: 4em; margin: 0.5em 0 0.5em 0; text-align: center; width: 100%;">
            <p class="text1" style="color: white;">对自己满怀信心？</p>
            <p class="text2" style="color: white;">何不来测试一下自己的水平？</p>
          </div>
      </div>
      <!-- 功能区 -->
      <div class="choose-area">
        <!-- 参加学习按钮 -->
        <div class="choice" @click="gotoStudy">
          <img src="/static/images/teacher.png" mode="aspectFit" />
          <p class="choice-text text1">学习</p>
        </div>
        <!-- 参加答题按钮 -->
        <div class="choice" @click="gotoExercise">
          <img src="/static/images/test.png" mode="aspectFit" />
          <p class="choice-text text2">答题</p>
        </div>
        <!-- 参加比赛按钮 -->
        <div class="choice" @click="gotoContest">
          <img src="/static/images/match.png" mode="aspectFit" />
          <p class="choice-text text3">比赛</p>
        </div>
      </div>
      <!-- 公式助记区域 -->
      <div class="memory-area">
        <div v-if="notLoggedin">
          <p style="text-indent: 1em;">公式助记</p>
          <p style="text-align: center; padding: 1em;">登录以进行公式记忆</p>
        </div>
        <div v-else class="formula">
          <p style="text-indent: 1em;">公式助记</p>
          <!-- <p style="text-align: center; padding:1em; font-size: 1.2em; ">{{ formula }}</p> -->
          <div style="display: flex; justify-content: center;">
            <img style="width: 10em; height: 4em;" :src="myUrl" alt="数学公式" />
          </div>
          <div class="button-area">
            <input class="memory-button" type="button" value="查看公式" />
            <input class="memory-button" type="button" value="换一个" style="background-color: #11dd00;" @click="changeFormula"/>
          </div>
        </div>
      </div>
    </div>
    <!-- 设置区域 -->
    <div class="settings-mode" v-show="settingsDisplay" style="width: 70%; position: absolute;">
      <!-- <img class="settings" src="" mode="aspectFit" /> -->
      <input style="height: 2em; line-height: 2em; font-weight: 200;" type="button" value="设置学习时间" />
    </div>
    <!-- <div class="ranking-mode" v-show="rankingShow">
    </div>-->
  </div>
</template>

<style scoped>
.settings-area .settings-img {
  width: 24px;
  height: 24px;
  left: 3%;
  position: absolute;
  z-index: 5;
}
.ranking-area .ranking-img {
  width: 24px;
  height: 24px;
  right: 3%;
  position: absolute;
  z-index: 5;
}
.regular-mode {
  width: 100%;
  position: absolute;
}
.bulletin-area {
  width: 70%;
  margin: 2% 15% 2% 15%;
  display: flex;
  justify-content: left;
}
.bulletin-area .bulletin-img {
  width: 16px;
  height: 16px;
}
.bulletin-area .today-news {
  color: red;
  font-size: 12px;
}
.infomation-area {
  width: 100%;
  height: 8em;
  border-top: 1px #dddddd dashed;
}
.test-area {
  display: flex;
  justify-content: center;
  width: 100%;
  height: 4em;
}
.test-area img {
  width: 100%;
  height: 4em;
  position: absolute;
}
.test-area .text2 {
  padding: 1%;
}
.choose-area {
  display: flex;
  justify-content: space-around;
  width: 100%;
  margin-top: 1em;
  margin-bottom: 1em;
  height: 5em;
}
.choose-area .choice {
  width: 64px;
  height: 80px;
}
.choose-area .choice img {
  width: 100%;
  height: 3.5em;
}
.choose-area .choice .choice-text {
  text-align: center;
  font-size: 1.2em;
}
.memory-area {
  width: 100%;
  border-top: 1px #cccccc dashed;
  height: 3em;
}
.memory-area .button-area {
  display: flex;
  justify-content: space-around;
}
.memory-area .button-area .memory-button {
  line-height: 1.5em;
  font-size: 0.8em;
  height: 1.5em;
}
</style>

<script>
export default {
  data () {
    return {
      notLoggedin: false, // 判断是否登录
      dateToday: (new Date()).getDate(), // 获取今天日期
      learningDays: 0, // 学习天数
      news: 'Hello miniprogram', // 消息显示
      settingsDisplay: false, // 是否显示设置区
      rankingDisplay: false, // 是否显示排名区域
      leftStart: '0', // 控制default界面位置
      openLeft: false, // 是否已经打开左侧设置区
      learned: false, // 是否进行学习
      haschecked: false, // 是否已经签到
      myUrl: '', // 公式图片URL
      number: 0, // 
      formulas: '' // 公式助记区的公式
    }
  },
  // 小程序创建时，初始化云端
  created () {
    wx.cloud.init()
  },
  // 页面加载时获取用户数据，公告标题，知识点公式
  onLoad () {
    wx.cloud.database().collection('Notice').get({
      success: res => {
        this.news = res.data[0].data.title
      }
    })
    wx.cloud.database().collection('UserInfo').get({
      success: res => {
        this.learningDays = res.data[0].data.SignDate
      }
    })
    wx.cloud.database().collection('Knowledge').get({
      success: res => {
        this.formulas = res.data
        this.myUrl = 'https://latex.codecogs.com/svg.latex?' + encodeURIComponent(res.data[this.number].data.know1)
      }
    })
  },
  methods: {
    // 打开设置区方法
    openSettings () {
      if (this.openLeft) {
        // 关闭设置区
        this.settingsDisplay = false
        this.leftStart = '0'
        this.openLeft = false
      } else {
        // 打开设置区，把default
        this.settingsDisplay = true
        this.leftStart = '70%'
        this.openLeft = true
      }
    },
    // 连接到学习界面
    gotoStudy () {
      if (!this.notLoggedin) {
        mpvue.navigateTo({url: '/pages/study/main'})
      }
    },
    // 检测是否已学习
    checkLearned () {
      if (!this.notLoggedin) {
        if (!this.haschecked) {
          this.haschecked = true
          if (this.learned) {
            this.learningDays += 1
          } else {
            this.gotoStudy()
          }
        }
      }
    },
    // 跳转到公告栏
    gotoBulletin () {
      mpvue.navigateTo({url: '/pages/bulletin/main'})
    },
    // 换一个公式
    changeFormula () {
      this.number += 1
      if (this.number >= 10) {
        this.number = 0
      }
      this.myUrl = 'https://latex.codecogs.com/svg.latex?' + encodeURIComponent(this.formulas[this.number].data.know1)
    }
  }
}
</script>