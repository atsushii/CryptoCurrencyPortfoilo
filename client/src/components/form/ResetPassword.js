import React from "react";
import { resetPassword } from "../../actions";
import { connect } from "react-redux";
import ForgetPasswordForm from "./ForgetPasswordForm";

class ResetPassword extends React.Component {
  onSubmit = (formValue) => {
    this.props.resetPassword(formValue);
  };

  render() {
    return (
      <div>
        <ForgetPasswordForm onSubmit={this.onSubmit} />
      </div>
    );
  }
}

export default connect(null, { resetPassword })(ResetPassword);
