import React from "react";
import { Field, reduxForm } from "redux-form";
import { Link } from "react-router-dom";

class ForgetPasswordForm extends React.Component {
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

  onSubmit = (formValue) => {
    this.props.onSubmit(formValue);
  };

  render() {
    return (
      <div className="card o-hidden border-0 shadow-lg my-5">
        <div className="card-body p-0">
          <div className="row">
            <div className="col">
              <div className="p-5">
                <div className="text-center">
                  <h1 className="h4 text-gray-900 mb-4">Forget password</h1>
                  <p>
                    Please enter your email address and we will send a password
                    reset link to mail
                  </p>
                </div>

                <form
                  onSubmit={this.props.handleSubmit(this.onSubmit)}
                  className="user"
                >
                  <Field
                    name="email"
                    component={this.renderInput}
                    label="Enter Email"
                    type="email"
                  ></Field>
                  <button className="btn btn-primary btn-user btn-block">
                    Reset password
                  </button>
                </form>
                <div className="text-center">
                  <Link className="small" to="/form/login">
                    Back to login page
                  </Link>
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

  if (!value.email) {
    errors.email = "Required";
  } else if (!/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i.test(value.email)) {
    errors.email = "Invalid Email";
  }

  return errors;
};

export default reduxForm({ form: "userForm", validate })(ForgetPasswordForm);
