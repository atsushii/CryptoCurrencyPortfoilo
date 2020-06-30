import React from "react";
import { connect } from "react-redux";
import { signUp } from "../../actions";
import UserForm from "./UserForm";

class RegisterUser extends React.Component {
  onSubmit = (formValues) => {
    this.props.signUp(formValues);
  };

  render() {
    return (
      <div>
        <UserForm
          onSubmit={this.onSubmit}
          title="Create Account"
          submitButton="SignUp"
          linkToSignupOrLogin="/form/login"
          linkDescriptionForSignupOrLogin="Already have an account? Login!"
          linkToForgetPassword=""
          linkDescriptionForForgetPassword=""
        />
      </div>
    );
  }
}

export default connect(null, { signUp })(RegisterUser);
