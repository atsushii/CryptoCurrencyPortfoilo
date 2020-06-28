import crypto from "../api/api";
import history from "../history";
import {
  SIGN_UP,
  LOGIN,
  LOGOUT,
  FETCH_USER,
  EDIT_USER,
  DELETE_USER,
  REFETCH_USER,
  FETCH_CURRENCY,
  EDIT_CURRENCY,
  DELETE_CURRENCY,
  REGISTER_CURRENCY,
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
  history.push(`/portfolio/${response.data.id}`);
};

export const fetchUser = (id) => async (dispatch) => {
  const response = await crypto.get(`/fetch/${id}`, {
    withCredentials: true,
  });
  dispatch({ type: FETCH_USER, payload: response.data });
};

export const editUser = (id, formValue) => async (dispatch) => {
  const response = await crypto.patch(`/edit/${id}`, formValue, {
    withCredentials: true,
  });

  dispatch({ type: EDIT_USER, payload: response.data });
  history.push(`/form/delete/${id}`);
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

export const fetchCurrency = () => async (dispatch) => {
  const response = await crypto.get("/fetch_currency", {
    withCredentials: true,
  });

  dispatch({ type: FETCH_CURRENCY, payload: response.data });
};

export const editCurrency = (id, formValue) => async (dispatch) => {
  const response = await crypto.patch(`/edit_currency/${id}`, formValue, {
    withCredentials: true,
  });
  dispatch({ type: EDIT_CURRENCY, payload: response.data });
  history.push(`/portfolio/${id}`);
};

export const deleteCurrency = (id, currency) => async (dispatch) => {
  await crypto.delete(`/delete_currency/${id}/${currency}`, {
    withCredentials: true,
  });
  dispatch({ type: DELETE_CURRENCY, payload: id });
  history.push(`/portfolio/${id}`);
};

export const registerCurrency = (id, formValues) => async (dispatch) => {
  const response = await crypto.post(`/register_currency/${id}`, formValues, {
    withCredentials: true,
  });

  dispatch({ type: REGISTER_CURRENCY, payload: response.data });
  history.push(`/portfolio/${id}`);
};
