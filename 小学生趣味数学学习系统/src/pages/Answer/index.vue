<template>
  <div class="container">
    <form style="width: 80%;">
      <!-- 填写回答问题编号区 -->
      <view class="fb-mobile">
        <view class="label">您回答的问题的编号是：</view>
        <view class="mobile-box">
          <input class="mobile" :value="inputTxt">
          <img class="clear-icon" src="/static/images/del.png">
          <button class='clear-btn' plain="true" hover-class="none" bindtap="clearblock">
          </button>
        </view>
      </view>
      <!-- 填写回答问题主题区域 -->
      <view class="fb-mobile">
        <view class="label">您回答的问题的主题是：</view>
        <view class="mobile-box">
          <input class="mobile" :value="inputTxt">
          <img class="clear-icon" src="/static/images/del.png">
          <button class='clear-btn' plain="true" hover-class="none" bindtap="clearblock">
          </button>
        </view>
      </view>
      <!-- 问题回答内容区域 -->
      <view class="label-content">回答提问</view>
      <view class="fb-body">
        <textarea class="content" placeholder="请在此输入你想回复的话" />
        <view class="text-count">最多输入500字</view>
      </view>
      <!-- 填写回答问题用户联系方式区域 -->
      <view class="fb-mobile">
        <view class="label">你的联系方式(选填，方便大家与你交流)</view>
        <view class="mobile-box">
          <input class="mobile" maxlength="20" placeholder="请输入您的QQ、微信或者手机号" :value="inputTxt" confirm-type ="send" />
          <img class="clear-icon" src="/static/images/del.png">
          <button class='clear-btn' plain="true" hover-class="none" bindtap="clearblock"></button>
        </view>
      </view>
    </form>
    <!-- 填写完毕提交按钮 -->
    <button class="fb-btn">提交</button>
  </div>
</template>

<style scoped>
page{
    background: #f4f4f4;
    min-height: 100%;
}
.container{
    background: #f4f4f4;
    min-height: 100%;
    padding-top: 30rpx;
}

.fb-type{
  height: 80rpx;
  width: 80%;
  background: #fff;
  margin-top: 50rpx;
  display: flex;
  flex-direction: row;
  align-items: center;
  padding-left: 30rpx;
  padding-right: 30rpx;
}

.fb-type .type-label{
  height: 36rpx;
  flex: 1;
  font-size: 28rpx;
  color: #7f7f7f;
}

.fb-type .type-icon{
  height: 36rpx;
  width: 36rpx;
}
.fb-body{
  /* width: 85%; */
  background: #fff;
  height: 374rpx;
  margin-top: 50rpx;
  padding: 18rpx 30rpx 64rpx 30rpx;
}
.fb-body .content{
  width: 85%;
  height: 100%;
  color: #333;
  line-height: 40rpx;
  font-size: 28rpx;
}
.fb-body .label{
  height: 58rpx;
  width: 85%;
  color: #7f7f7f;
  font-size: 24rpx;
  line-height: 33rpx;
}
.fb-body .text-count{
  padding-top: 17rpx;
  line-height: 30rpx;
  float: right;
  color: #666;
  font-size: 24rpx;
}
.fb-mobile{
  margin-top: 40rpx;
  height: 180rpx;
}
.fb-mobile .mobile-box{
  display: flex;
  flex-direction: row;
  align-items: center;
  height: 104rpx;
  color: #333;
  padding-left: 30rpx;
  padding-right: 30rpx;
  font-size: 24rpx;
  background: #fff;
  position: relative;
}
.fb-mobile .mobile{
  position: absolute;
  top: 27rpx;
  left: 30rpx;
  height: 50rpx;
  width: 80%;
  color: #333;
  line-height: 50rpx;
  font-size: 24rpx;
}
.fb-mobile .label{
  height: 58rpx;
  width: 85%;
  color: #7f7f7f;
  font-size: 24rpx;
  line-height: 30rpx;
}
.fb-mobile .clear-btn{
  position: absolute;
  right: 0rpx;
  width: 200rpx;
  height: 104rpx;
  border-radius: 0 0;
  border-color: white;
}
.clear-icon{
  position: absolute;
  top: 43rpx;
  right: 30rpx;
  width: 28rpx;
  height: 28rpx;
}
.fb-btn{
  width: 100%;
  height: 98rpx;
  line-height: 98rpx;
  background: #e64340;
  position: fixed;
  bottom: 0;
  left: 0;
  border-radius: 0;
  color: #fff;
  font-size: 28rpx;
  z-index: 5;
}
.label-content{
  height: 25rpx;
  width: 90%;
  color: #7f7f7f;
  font-size: 24rpx;
  line-height: 33rpx;
}
</style>

<script>
export default {
  data () {
    return {
      statusType: ['发言', '社区', '排名'], // 回答的问题类型
      tabClass: ['', '', ''], // 选择框显示的当前回答问题类型
      array: ['请选择交流分类', '简单', '中级', '高级', '竞赛'], // 回答类型
      index: 0, // 选择器状态值
      inputTxt: '', // 输入数据
      currentType: 0 // 向后台发送的当前问题类型选择状态
    }
  },
  // 将选择器与其索引值绑定
  bindPickerChange: function (e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.index = e.detail.value
  },
  // 用户目前回答的问题的信息
  statusTap: function (e) {
    const curType = e.currentTarget.dataset.index
    this.data.currentType = curType
    this.currentType = curType
    this.onShow()
  },
  // 点击清除输入框中内容
  clearblock: function () {
    this.inputTxt = '' // 更新页面input框显示
  }
}
</script>