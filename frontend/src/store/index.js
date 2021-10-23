import { createStore } from "vuex";

export default createStore({
  state: {
    from_language: null,
    to_language: null,
    is_muted: null,
  },
  mutations: {
    init(state) {
      state.from_language = "jp"
      state.to_language = "ru"
      state.is_muted = false
    },
    changeLanguage(state, payload) {
      if (payload.is_native) {
        state.from_language = payload.changed_language
      } else {
        state.to_language = payload.changed_language
      }
    },
    swapLanguages(state) {
      const tmp = state.from_language
      state.from_language = state.to_language
      state.to_language = tmp
    },
    toggleMute(state) {
      state.is_muted = !state.is_muted
    }
  },
  actions: {
    init(context) {
      context.commit('init')
    }
  },
  getters: {
    getIsMuted: state => state.is_muted,
    getToLanguage: state => state.to_language,
  },
  modules: {},
});
