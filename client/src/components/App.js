import React from "react";
import { Router, Route, Switch } from "react-router-dom";
import RegisterUser from "./form/RegisterUser";
import LoginForm from "./form/LoginForm";
import history from "../history";

const App = () => {
  return (
    <div>
      <Router history={history}>
        <Switch>
          <Route path="/form/signup" exact component={RegisterUser} />
          <Route path="/form/login" exact component={LoginForm} />
        </Switch>
      </Router>
    </div>
  );
};

export default App;
