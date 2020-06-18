import _ from "lodash";
import {
  SIGN_UP,
  LOGIN,
  LOGOUT,
  FETCH_USER,
  DELETE_USER,
} from "../actions/types";

const INITIAL_STATE = {
  isSignedIn: null,
  userId: null,
};

export default (state = INITIAL_STATE, action) => {
  switch (action.type) {
    case SIGN_UP:
      return { ...state, isSignedIn: null, userId: null };

    case LOGIN:
      return { ...state, isSignedIn: true, userId: action.payload };

    case FETCH_USER:
      return { ...state, [action.payload.id]: action.payload };

    case DELETE_USER:
      return _.omit(state, action.payload);

    default:
      return state;
  }
};
