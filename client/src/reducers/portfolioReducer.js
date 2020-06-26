import { FETCH_CURRENCY } from "../actions/types";

export default (state = {}, action) => {
  switch (action.type) {
    case FETCH_CURRENCY:
      return { ...state, [action.payload.id]: action.payload };

    default:
      return state;
  }
};
