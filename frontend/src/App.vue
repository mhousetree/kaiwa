<template>
  <header>
    <button @click="toggle_mute">{{ is_muted ? "unmute" : "mute" }}</button>
    <button @click="swap_language">{{to_language}} ↔ {{from_language}}</button>
  </header>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav>
  <router-view />
</template>

<script>
export default {
  methods: {
    toggle_mute() {
      this.$store.commit("toggleMute")
    },
    swap_language() {
      this.$store.commit("swapLanguages")
    }
  },
  computed: {
    is_muted () {
      return this.$store.state.is_muted
    },
    from_language () {
      return this.$store.state.from_language
    },
    to_language () {
      return this.$store.state.to_language
    }
  },
  created(){
    this.$store.dispatch('init')
  }
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
