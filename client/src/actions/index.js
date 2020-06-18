import crypto from "../api/api";
import history from "../history";
import { SIGN_UP, LOGIN, LOGOUT, FETCH_USER, DELETE_USER } from "./types";

export const signUp = (formValues) => async (dispatch) => {
  const response = await crypto.post("/signup", formValues);
  console.log(response);
  if (response.data) {
    dispatch({ type: SIGN_UP, payload: response.data });
    history.push("/form/login");
  } else {
    dispatch({ type: SIGN_UP, payload: response.data });
    history.push("/form/signup");
  }
};

export const login = (formValues) => async (dispatch) => {
  console.log(formValues);
  const response = await crypto.post("/login", formValues);

  if (response.data) {
    console.log("login!");
    dispatch({ type: LOGIN, payload: response.data });
    history.push("form/login");
  } else {
    console.log("failr");
    dispatch({ type: LOGIN, payload: response.data });
    history.push("/form/login");
  }
};

export const fetchUser = (id) => async (dispatch) => {
  const response = await crypto.get(`/fetch/${id}`);
  dispatch({ type: FETCH_USER, payload: response.data });
};

export const deleteUser = (id) => async (dispatch) => {
  await crypto.delete(`/delete/${id}`);
  dispatch({ type: DELETE_USER, payload: id });
};
