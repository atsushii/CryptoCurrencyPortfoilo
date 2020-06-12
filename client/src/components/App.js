import React from "react";
import { Router, Route, Switch } from "react-router-dom";
import SignUpForm from "./form/SignupForm";
import history from "../history";

const App = () => {
  return (
    <div>
      <Router history={history}>
        <Switch>
          <Route path="/" exact component={SignUpForm} />
        </Switch>
      </Router>
    </div>
  );
};

export default App;
