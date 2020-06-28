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
        </Switch>
      </Router>
    </div>
  );
};

export default App;
