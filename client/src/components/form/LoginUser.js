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
          link="/form/signup"
          link_description="Don't you have an account? Signup!"
        />
      </div>
    );
  }
}

export default connect(null, { login })(LoginUser);
