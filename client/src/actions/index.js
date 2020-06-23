import crypto from "../api/api";
import history from "../history";
import {
  SIGN_UP,
  LOGIN,
  LOGOUT,
  FETCH_USER,
  DELETE_USER,
  REFETCH_USER,
} from "./types";

export const signUp = (formValues) => async (dispatch) => {
  const response = await crypto.post("/signup", formValues);

  dispatch({ type: SIGN_UP, payload: response.data });
  history.push("/form/login");
};

export const login = (formValues) => async (dispatch) => {
  const response = await crypto.post("/login", formValues, {
    withCredentials: true,
  });

  dispatch({ type: LOGIN, payload: response.data });
  history.push(`/form/delete/${response.data.id}`);
};

export const fetchUser = (id) => async (dispatch) => {
  const response = await crypto.get(`/fetch/${id}`, {
    withCredentials: true,
  });
  dispatch({ type: FETCH_USER, payload: response.data });
};

export const deleteUser = (id) => async (dispatch) => {
  await crypto.delete(`/delete/${id}`, {
    withCredentials: true,
  });
  dispatch({ type: DELETE_USER, payload: id });
  history.push("/form/signup");
};

export const reFetchUser = () => async (dispatch) => {
  const response = await crypto.get("/refetch", {
    withCredentials: true,
  });
  dispatch({ type: REFETCH_USER, payload: response.data });
};
