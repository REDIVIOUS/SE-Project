<template>
  <div>
    <div class="search-area">
      <img class="search-img" src="/static/images/search.png" mode="aspectFit" />
    </div>
    <div class="search-mode">
      <input type="text" placeholder="输入你想查询的东西" />
      <div class="mostly-searched">
        <ul>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["text"]
};
</script>

<style>
.card {
  padding: 10px;
}
</style>
