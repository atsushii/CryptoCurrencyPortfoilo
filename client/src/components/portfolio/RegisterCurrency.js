import React from "react";
import { connect } from "react-redux";
import { fetchCurrency } from "../../actions";
import CurrencyForm from "./CurrencyForm";
import { registerCurrency } from "../../actions";

class RegisterCurrency extends React.Component {
  componentDidMount() {
    this.props.fetchCurrency();
  }

  onSubmit = (formValues) => {
    this.props.registerCurrency(this.props.match.params.id, formValues);
  };

  render() {
    if (!this.props.portfolio) {
      return <div>Loading</div>;
    }

    return (
      <div>
        <CurrencyForm
          onSubmit={this.onSubmit}
          title="Register New Currency"
          submitButton="Register"
        />
      </div>
    );
  }
}

const mapStateToProps = (state, ownProps) => {
  return { portfolio: state.portfolio[ownProps.match.params.id] };
};

export default connect(mapStateToProps, { fetchCurrency, registerCurrency })(
  RegisterCurrency
);
