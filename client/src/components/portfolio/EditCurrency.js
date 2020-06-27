import React from "react";
import { connect } from "react-redux";
import { fetchCurrency } from "../../actions";
import EditCurrencyForm from "./EditCurrencyForm";
import { editCurrency } from "../../actions";

class EditCurrency extends React.Component {
  componentDidMount() {
    this.props.fetchCurrency();
  }

  onSubmit = (formValues) => {
    this.props.editCurrency(this.props.match.params.id, formValues);
  };

  renderInitialValue() {
    const { currency_list } = this.props.portfolio;
    const { symbol } = this.props.match.params;

    const { num_hold } = currency_list.filter(
      (currency) => currency.symbol === symbol
    )[0];
    return { symbol: symbol, num_hold: num_hold };
  }

  render() {
    if (!this.props.portfolio) {
      return <div>Loading Currency Data</div>;
    }
    const { symbol } = this.props.match.params;

    return (
      <div>
        <EditCurrencyForm
          onSubmit={this.onSubmit}
          title={symbol}
          submitButton="Update"
          initialValues={this.renderInitialValue()}
        />
      </div>
    );
  }
}

const mapStateToProps = (state, ownProps) => {
  return { portfolio: state.portfolio[ownProps.match.params.id] };
};

export default connect(mapStateToProps, { fetchCurrency, editCurrency })(
  EditCurrency
);
