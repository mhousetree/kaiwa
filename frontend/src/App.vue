<template>
  <header>
    <router-link to="/">
      <img src="@/assets/img/icons/kaiwa_icon.svg" alt="kaiwa logo" />
    </router-link>
    <!-- <button @click="toggle_mute" class="button_no-bg">
      <span v-if="is_muted" class="material-icons"> volume_off </span>
      <span v-else class="material-icons"> volume_up </span>
    </button> -->
    <div id="languages">
      <button class="button_no-bg" @click="toggle_select_from_language">
        <span
          class="flag-icon"
          v-bind:class="'flag-icon-' + from_language"
        ></span>
        <div id="select_from_language">
          <span class="flag-icon flag-icon-jp"></span>
          <span class="flag-icon flag-icon-cn"></span>
          <span class="flag-icon flag-icon-kr"></span>
          <span class="flag-icon flag-icon-us"></span>
          <span class="flag-icon flag-icon-de"></span>
          <span class="flag-icon flag-icon-it"></span>
          <span class="flag-icon flag-icon-es"></span>
          <span class="flag-icon flag-icon-fr"></span>
          <span class="flag-icon flag-icon-ru"></span>
          <span class="flag-icon flag-icon-fi"></span>
        </div>
      </button>
      <button @click="swap_language" class="button_no-bg" id="swap">
        <span class="material-icons"> swap_horizontal_circle </span>
        <!-- {{ to_language }} ↔ {{ from_language }} -->
      </button>
      <button class="button_no-bg">
        <span
          class="flag-icon"
          v-bind:class="'flag-icon-' + to_language"
        ></span>
      </button>
    </div>
  </header>

  <router-view />

  <nav>
    <router-link to="/">
      <span v-if="$route.path === '/'" class="material-icons"> home </span>
      <span v-else class="material-icons-outlined"> home </span>
    </router-link>
    <router-link to="/playlist">
      <span v-if="$route.path === '/playlist'" class="material-icons">
        star
      </span>
      <span v-else class="material-icons"> star_outline </span>
    </router-link>
    <router-link to="/settings">
      <span v-if="$route.path === '/settings'" class="material-icons">
        settings
      </span>
      <span v-else class="material-icons-outlined"> settings </span>
    </router-link>
  </nav>

  <footer>
    <button @click="togglePlayer" class="button_no-bg">
      <span class="material-icons"> arrow_drop_down </span>
    </button>
    <audio src="" controls autoplay></audio>
  </footer>
</template>

<script>
export default {
  data() {
    return {
      is_player_open: true,
    };
  },
  methods: {
    toggle_mute() {
      this.$store.commit("toggleMute");
    },
    swap_language() {
      this.$store.commit("swapLanguages");
    },
    togglePlayer() {
      if (this.is_player_open) {
        document.querySelector("footer").classList.add("closed");
      } else {
        document.querySelector("footer").classList.remove("closed");
      }
      this.is_player_open = !this.is_player_open;
    },
    toggle_select_from_language() {
      const target = document.getElementById("select_from_language");
      if (target.style.display !== "grid") {
        target.style.display = "grid";
      } else {
        target.style.display = "none";
      }
    },
  },
  computed: {
    is_muted() {
      return this.$store.state.is_muted;
    },
    from_language() {
      return this.$store.state.from_language;
    },
    to_language() {
      return this.$store.state.to_language;
    },
  },
  mounted() {
    this.$store.watch(
      (state, getters) => getters.getIsMuted,
      (newValue) => {
        if (newValue) {
          Array.prototype.forEach.call(
            document.getElementsByTagName("audio"),
            (e) => {
              e.muted = true;
            }
          );
        } else {
          Array.prototype.forEach.call(
            document.getElementsByTagName("audio"),
            (e) => {
              e.muted = false;
            }
          );
        }
      }
    );
  },
  created() {
    this.$store.dispatch("init");
  },
};
</script>

<style lang="scss">
@import "./colors.scss";

:root {
  font-size: 16px;
  background-color: $white;
}

#app {
  padding: 5.3rem 1rem 11.5rem;
  font-family: kinto-sans, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: $black;
}

@media screen and (min-width: 470px) {
  #app {
    padding-top: 6rem;
  }
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

a {
  color: $blue;
}

header {
  position: fixed;
  width: 100%;
  top: 0;
  left: 0;
  padding: 1rem;
  background-color: rgba($white, 0.8);
  backdrop-filter: blur(5px);
  box-shadow: 0 2px 3px #0003;
  display: flex;
  justify-content: space-between;
  padding-bottom: 0.8rem;
  align-items: center;
  a {
    width: min(30%, 150px);
  }
}

#languages {
  display: flex;
  align-items: center;
  button {
    position: relative;

    #select_from_language {
      position: fixed;
      z-index: 3;
      padding: 1rem;
      grid-template-columns: repeat(5, 1fr);
      gap: 0.5rem;
      left: 0;
      width: 90%;
      bottom: -7.5rem;
      left: 5%;
      background-color: $white;
      filter: drop-shadow(0 2px 4px #0003);
      border-radius: 0.3rem;
      display: none;

      &::before {
        z-index: 2;
        position: fixed;
        top: -1.3rem;
        right: 31%;
        content: "";
        display: block;
        border-right: 1rem solid transparent;
        border-left: 1rem solid transparent;
        border-bottom: 1.3rem solid $white;
        filter: drop-shadow(0 -1px 1px #0003);
      }
    }
  }
  #swap {
    margin: 0.2rem 0.5rem 0;
    span {
      font-size: 1.6rem;
    }
  }
}

.button_no-bg {
  border: none;
  background-color: transparent;
  color: $grey;
}

.flag-icon {
  border: 1px solid #0002;
  box-shadow: 0 1px 3px #0002;
  font-size: 2rem;
}

nav {
  z-index: 2;
  position: fixed;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 2rem 0.5rem;
  width: 100%;
  height: 4rem;
  bottom: 0;
  left: 0;
  background-color: $white;
  border-top: 1px solid mix($grey, $white);

  .material-icons,
  .material-icons-outlined {
    font-size: 2rem;
  }

  a:not(.router-link-active) {
    opacity: 0.75;
  }
}

footer {
  position: fixed;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  left: 0;
  bottom: 4rem;
  box-shadow: 0 -2px 3px #0003;
  transition: 0.3s;
  background-color: $white;

  button {
    width: 100%;
    transition: 0.5s;
  }

  audio {
    margin: 0 0 1rem;
  }

  &.closed {
    bottom: calc(-70px + 4rem);
    button {
      transform: scaleY(-100%);
    }
  }
}
</style>
