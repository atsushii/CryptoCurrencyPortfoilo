import React from "react";
import { Field, reduxForm } from "redux-form";

class SignupForm extends React.Component {
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
    return (
      <div className="card o-hidden border-0 shadow-lg my-5">
        <div className="card-body p-0">
          <div className="row">
            <div className="col-lg-5 d-none d-lg-block bg-register-image"></div>
            <div className="col-lg-7">
              <div className="p-5">
                <div className="text-center">
                  <h1 className="h4 text-gray-900 mb-4">Create an Account</h1>
                </div>
                <div className="form-group row">
                  <div className="col-sm-6 mb-3 mb-sm-0">
                    <label>{label}</label>
                    <input
                      className="form-control is-invalid"
                      {...input}
                      autoComplete="off"
                    />
                    {this.renderError(meta)}
                  </div>
                </div>
                <div className="text-center">
                  <a className="small" href="{{ url_for('user_page.login') }}">
                    Already have an account? Login!
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  };
  render() {
    return (
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
        <button className="btn btn-primary btn-user btn-block">Submit</button>
      </form>
    );
  }
}

const validate = (value) => {
  const errors = {};

  if (!value.userName) {
    errors.userName = "Required";
  } else if (value.userName.length < 10) {
    errors.userName = "input must be more than 10 character";
  }

  if (!value.email) {
    errors.email = "Required";
  } else if (!/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i.test(value.email)) {
    errors.email = "Invalid Email";
  }

  if (!value.password) {
    errors.password = "Required";
  }

  if (!value.confirmPassword) {
    errors.confirmPassword = "Required";
  } else if (value.password !== value.confirmPassword) {
    errors.confirmPassword = "Password mismatched";
  }

  return errors;
};

export default reduxForm({ form: "signupForm", validate })(SignupForm);
