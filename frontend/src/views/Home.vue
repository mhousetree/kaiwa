<template>
  <div class="home">
    <ul id="category_list">
      <li>
        <router-link to="/greetings">基本表現</router-link>
      </li>
      <li>
        <router-link to="/airport">空港</router-link>
      </li>
      <li>
        <router-link to="/change">両替</router-link>
      </li>
      <li>
        <router-link to="/sightseeing">観光</router-link>
      </li>
      <li>
        <router-link to="/transportation">交通</router-link>
      </li>
      <li>
        <router-link to="/hotel">宿泊</router-link>
      </li>
      <li>
        <router-link to="/restaurant">食事</router-link>
      </li>
      <li>
        <router-link to="/shopping">買い物</router-link>
      </li>
      <li>
        <router-link to="/post_telephone">郵便・電話</router-link>
      </li>
      <li>
        <router-link to="/trouble">トラブル</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "Home",
};
</script>

<style lang="scss" scoped>
@import "../colors.scss";
#category_list {
  padding: 0;
  margin: 0 auto;
  list-style: none;
  display: grid;
  gap: .7rem;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));

  li {
    box-shadow: 0 2px 3px #cccc;
    border-radius: 0.3rem;

    a {
      border-radius: 0.3rem;
      display: block;
      padding: 1rem 1rem;
      text-decoration: none;
      color: $white;
      font-size: 1.2rem;
      font-weight: 400;

      // https://coolors.co/eef0f2-a4243b-c85f32-da7d2e-7e935b-0f8b8d-0d6195-0a369d-0f3670-143642

      &[href="/greetings"] {
        background-color: #eef0f2;
        color: $black;
      }
      &[href="/airport"] {
        background-color: #0a369d;
      }
      &[href="/change"] {
        background-color: #da7d2e;
      }
      &[href="/sightseeing"] {
        background-color: #7E935B;
      }
      &[href="/transportation"] {
        background-color: #0D6195;
      }
      &[href="/hotel"] {
        background-color: #0F3670;
      }
      &[href="/restaurant"] {
        background-color: #C85F32;
      }
      &[href="/shopping"] {
        background-color: #0F8B8D;
      }
      &[href="/post_telephone"] {
        background-color: #A4243B;
      }
      &[href="/trouble"] {
        background-color: #143642;
      }
    }

    &:hover {
      background-color: yellow;
    }
  }
}
</style>
