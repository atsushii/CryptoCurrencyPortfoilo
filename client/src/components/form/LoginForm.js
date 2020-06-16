import React from "react";
import { Field, reduxForm } from "redux-form";

class LoginForm extends React.Component {
  renderError({ error, touched }) {
    if (touched && error) {
      return (
        <div className="text-danger">
          <div>{error}</div>
        </div>
      );
    }
  }

  renderInput = ({ input, label, meta }) => {
    const className = `form-control ${
      meta.error && meta.touched ? "is-invalid" : ""
    }`;
    return (
      <div className="form-group row">
        <div className="col-sm-6 mb-3 mb-sm-0">
          <label>{label}</label>
          <input className={className} {...input} autoComplete="off" />
          {this.renderError(meta)}
        </div>
      </div>
    );
  };
  render() {
    return (
      <div className="card o-hidden border-0 shadow-lg my-5">
        <div className="card-body p-0">
          <div className="row">
            <div className="col-lg-5 d-none d-lg-block bg-register-image"></div>
            <div className="col-lg-7">
              <div className="p-5">
                <div className="text-center">
                  <h1 className="h4 text-gray-900 mb-4">Login</h1>
                </div>
                <form className="user">
                  <Field
                    name="userName"
                    component={this.renderInput}
                    label="Enter User Name"
                    type="text"
                  ></Field>
                  <Field
                    name="email"
                    component={this.renderInput}
                    label="Enter Email"
                    type="email"
                  ></Field>
                  <Field
                    name="password"
                    component={this.renderInput}
                    label="Enter Password"
                    type="text"
                  ></Field>
                  <Field
                    name="confirmPassword"
                    component={this.renderInput}
                    label="Confirm Password"
                    type="text"
                  ></Field>
                  <button className="btn btn-primary btn-user btn-block">
                    Login
                  </button>
                </form>
                <div class="text-center">
                  <a
                    class="small"
                    href="{{ url_for('user_page.forgot_password') }}"
                  >
                    Forgot Password?
                  </a>
                </div>
                <div class="text-center">
                  <a class="small" href="{{ url_for('user_page.signup') }}">
                    Create an Account!
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

const validate = (value) => {
  const errors = {};

  if (!value.userName) {
    errors.userName = "Required";
  }

  if (!value.email) {
    errors.email = "Required";
  }

  if (!value.password) {
    errors.password = "Required";
  }

  if (!value.confirmPassword) {
    errors.confirmPassword = "Required";
  }

  return errors;
};

export default reduxForm({ form: "loginForm", validate })(LoginForm);
