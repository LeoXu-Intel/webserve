// store/index.js
import { createStore } from 'vuex';

export default createStore({
  state: {
    // 定义state
    selections: {
      selection1: '',
      selection2: '',
      selection3: '',
      selection4: [],
    },
    // ...其他state
  },
  mutations: {
    // 更新选择框的值
    updateSelections(state, payload) {
      state.selections.selection1 = payload.selection1;
      state.selections.selection2 = payload.selection2;
      state.selections.selection3 = payload.selection3;
      state.selections.selection4 = payload.selection4;
    },
  },
});
