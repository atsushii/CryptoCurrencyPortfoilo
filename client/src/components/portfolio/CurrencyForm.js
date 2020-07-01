import React from "react";
import { Field, reduxForm } from "redux-form";
import { Link } from "react-router-dom";

class CurrencyForm extends React.Component {
  renderInput = ({ input, label }) => {
    return (
      <div className="form-group row">
        <div className="col-sm-6 mb-3 mb-sm-0">
          <label>{label}</label>
          <input {...input} autoComplete="off" />
        </div>
      </div>
    );
  };

  onSubmit = (formValues) => {
    this.props.onSubmit(formValues);
  };

  render() {
    console.log(this.props.initialValues);
    return (
      <div className="card o-hidden border-0 shadow-lg my-5">
        <div className="card-body p-0">
          <div className="row">
            <div className="col-lg-5 d-none d-lg-block bg-register-image"></div>
            <div className="col-lg-7">
              <div className="p-5">
                <div className="text-center">
                  <h1 className="h4 text-gray-900 mb-4">{this.props.title}</h1>
                </div>

                <form
                  onSubmit={this.props.handleSubmit(this.onSubmit)}
                  className="user"
                >
                  <Field
                    name="symbol"
                    component={this.renderInput}
                    label="Currency Name"
                    type="text"
                  ></Field>
                  <Field
                    name="num_hold"
                    component={this.renderInput}
                    label="Amount Of Currency"
                    type="number"
                  ></Field>
                  <button className="btn btn-primary btn-user btn-block">
                    {this.props.submitButton}
                  </button>
                </form>
                <div className="text-center">
                  <Link
                    className="small"
                    to={`/portfolio/${this.props.userId}`}
                  >
                    Back to Portfolio
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

export default reduxForm({ form: "currencyForm" })(CurrencyForm);
