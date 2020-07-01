import React from "react";
import { Router, Route, Switch } from "react-router-dom";
import RegisterUser from "./form/RegisterUser";
import LoginUser from "./form/LoginUser";
import DeleteUser from "./form/DeleteUser";
import EditUser from "./form/EditUser";
import Portfolio from "./portfolio/Portfolio";
import EditCurrency from "./portfolio/EditCurrency";
import RegisterCurrency from "./portfolio/RegisterCurrency";
import DeleteCurrency from "./portfolio/DeleteCurrency";
import UserAccount from "./portfolio/UserAccount";
import LogoutView from "./portfolio/LogoutView";
import ForgetPassword from "./form/ForgetPassword";
import ResetPassword from "./form/ResetPassword";
import history from "../history";

const App = () => {
  return (
    <div>
      <Router history={history}>
        <Switch>
          <Route path="/form/signup" exact component={RegisterUser} />
          <Route path="/form/login" exact component={LoginUser} />
          <Route path="/form/edit/:id" exact component={EditUser} />
          <Route path="/form/delete/:id" exact component={DeleteUser} />
          <Route path="/form/forgetPassword" exact component={ForgetPassword} />
          <Route
            path="/form/resetPassword/:token"
            exact
            component={ResetPassword}
          />
          <Route path="/portfolio/:id" exact component={Portfolio} />
          <Route
            path="/portfolio/registerCurrency/:id"
            exact
            component={RegisterCurrency}
          />
          <Route
            path="/portfolio/editCurrency/:id/:symbol"
            exact
            component={EditCurrency}
          />
          <Route
            path="/portfolio/deleteCurrency/:id/:symbol"
            exact
            component={DeleteCurrency}
          />
          <Route
            path="/portfolio/userAccount/:id"
            exact
            component={UserAccount}
          />
          <Route
            path="/portfolio/logputView/:id"
            exact
            component={LogoutView}
          />
        </Switch>
      </Router>
    </div>
  );
};

export default App;
