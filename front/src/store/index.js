// store.js
import { createStore } from 'vuex';

export default createStore({
  state: {
    selections: {
      selection1: '',
      selection2: '',
      selection3: '',
      selection4: [],
      id:[],
    },
  },
  mutations: {
    setSelection(state, { key, value }) {
      state.selections[key] = value;
    },
  },
});
