import React from "react";
import { connect } from "react-redux";
import { login } from "../../actions";
import UserForm from "./UserForm";

class LoginUser extends React.Component {
  onSubmit = (formValues) => {
    this.props.login(formValues);
  };

  render() {
    return (
      <div>
        <UserForm
          onSubmit={this.onSubmit}
          title="Login"
          submitButton="Login"
          linkToSignupOrLogin="/form/signup"
          linkDescriptionForSignupOrLogin="Don't you have an account? Signup!"
          linkToForgetPassword="/form/forgetPassword"
          linkDescriptionForForgetPassword="Forget password?"
        />
      </div>
    );
  }
}

export default connect(null, { login })(LoginUser);
