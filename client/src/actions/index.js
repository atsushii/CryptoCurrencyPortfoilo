import crypto from "../api/api";
import history from "../history";
import { SIGN_UP, LOGIN, LOGOUT } from "./types";

export const signUp = (formValues) => async (dispatch) => {
  const response = await crypto.post("/signup", formValues);
  console.log(response);
  dispatch({ type: SIGN_UP, payload: response.data });
  history.push("/form/login");
};
