import {
  FETCH_CURRENCY,
  EDIT_CURRENCY,
  DELETE_CURRENCY,
  REGISTER_CURRENCY,
  LOGOUT,
} from "../actions/types";

export default (state = {}, action) => {
  switch (action.type) {
    case FETCH_CURRENCY:
      return { ...state, [action.payload.id]: action.payload };

    case EDIT_CURRENCY:
      return { ...state, [action.payload.id]: action.payload };

    case REGISTER_CURRENCY:
      return { ...state, [action.payload.id]: action.payload };

    case DELETE_CURRENCY:
      return "";

    case LOGOUT:
      return "";

    default:
      return state;
  }
};
