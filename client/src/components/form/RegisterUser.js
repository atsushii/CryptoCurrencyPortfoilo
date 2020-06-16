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
        <h2>Signup</h2>
        <UserForm onSubmit={this.onSubmit} />
      </div>
    );
  }
}

export default connect(null, { signUp })(RegisterUser);
