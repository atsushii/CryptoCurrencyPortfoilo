import React from "react";
import { connect } from "react-redux";
import { fetchCurrency } from "../../actions";
import EditCurrencyForm from "./EditCurrencyForm";
import { editCurrency } from "../../actions";
import _ from "lodash";
import { compose } from "redux";

class EditCurrency extends React.Component {
  componentDidMount() {
    this.props.fetchCurrency();
  }

  onSubmit = (formValues) => {
    this.props.editCurrency(this.props.match.params.id, formValues);
  };

  renderCurrency() {
    const { currency_list } = this.props.portfolio;
    const { symble } = this.props.match.params;

    return currency_list.filter((currency) => currency.symbol === symble);
  }

  render() {
    if (!this.props.portfolio) {
      return <div>Loading Currency Data</div>;
    }

    const { symble } = this.props.match.params;
    const { symbol, num_hold } = this.renderCurrency()[0];

    const initialValues = { symbol: symbol, num_hold: num_hold };

    return (
      <div>
        <EditCurrencyForm
          onSubmit={this.onSubmit}
          title={symble}
          submitButton="Update"
          initialValues={initialValues}
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
