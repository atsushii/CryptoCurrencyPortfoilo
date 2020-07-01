import React from "react";
import { resetPassword, isValidToken } from "../../actions";
import { connect } from "react-redux";
import ResetPasswordForm from "./ResetPasswordForm";

class ResetPassword extends React.Component {
  componentDidMount() {
    this.props.isValidToken(this.props.match.params.token);
  }
  onSubmit = (formValue, token) => {
    this.props.resetPassword(formValue, token);
  };

  render() {
    return (
      <div>
        <ResetPasswordForm
          onSubmit={this.onSubmit}
          token={this.props.match.params.token}
        />
      </div>
    );
  }
}

export default connect(null, { resetPassword, isValidToken })(ResetPassword);
