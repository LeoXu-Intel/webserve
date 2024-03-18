import { createStore } from 'vuex'

export default createStore({
  state: {
  },
  getters: {
  },
  mutations: {
    setAuthentication(state, value) {
      state.isAuthenticated = value;
    },
  },
  actions: {
  },
  modules: {
  }
})
