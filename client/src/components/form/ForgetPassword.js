import React from "react";
import { forgetPassword } from "../../actions";
import { connect } from "react-redux";
import ForgetPasswordForm from "./ForgetPasswordForm";

class forgetPassword extends React.Component {
  onSubmit = (formValue) => {
    this.props.forgetPassword(formValue);
  };

  render() {
    return (
      <div>
        <ForgetPasswordForm onSubmit={this.onSubmit} />
      </div>
    );
  }
}

export default connect(null, { forgetPassword })(forgetPassword);
