import { SIGN_UP, LOGIN, LOGOUT } from "../actions/types";

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

    default:
      return state;
  }
};
