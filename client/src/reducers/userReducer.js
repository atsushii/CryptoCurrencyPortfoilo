import _ from "lodash";
import {
  SIGN_UP,
  LOGIN,
  LOGOUT,
  FETCH_USER,
  DELETE_USER,
  REFETCH_USER,
  EDIT_USER,
  FORGET_PASSWORD,
  RESET_PASSWORD,
} from "../actions/types";

export default (state = {}, action) => {
  switch (action.type) {
    case SIGN_UP:
      return state;

    case LOGIN:
      return {
        ...state,
        [action.payload.id]: action.payload,
      };

    case LOGOUT:
      return "";

    case FETCH_USER:
      return { ...state, [action.payload.id]: action.payload };

    case REFETCH_USER:
      return { ...state, [action.payload.id]: action.payload };

    case EDIT_USER:
      return { ...state, [action.payload.id]: action.payload };

    case DELETE_USER:
      return _.omit(state, action.payload);

    case FORGET_PASSWORD:
      return {
        ...state,
        [action.payload.id]: action.payload,
      };

    case RESET_PASSWORD:
      return {
        ...state,
        [action.payload.id]: action.payload,
      };

    default:
      return state;
  }
};
