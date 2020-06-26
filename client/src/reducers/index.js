import { combineReducers } from "redux";
import { reducer as formReducer } from "redux-form";
import userReducer from "./userReducer";
import portfolioReducer from "./portfolioReducer";
export default combineReducers({
  form: formReducer,
  user: userReducer,
  portfolio: portfolioReducer,
});
