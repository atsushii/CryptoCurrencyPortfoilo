import React, { Fragment } from "react";
import { connect } from "react-redux";
import { fetchCurrency, deleteCurrency } from "../../actions";
import Model from "../Model";
import { Link } from "react-router-dom";
import history from "../../history";

class DeleteCurrency extends React.Component {
  // get user information
  componentDidMount() {
    this.props.fetchCurrency();
  }

  renderAction() {
    const { symbol } = this.props.match.params;
    const { id } = this.props.match.params;

    return (
      <Fragment>
        <button
          onClick={() => this.props.deleteCurrency(id, symbol)}
          className="btn btn-danger"
        >
          Delete {symbol}
        </button>
        <Link to={`/portfolio/${id}`} className="col-2">
          Cancel
        </Link>
      </Fragment>
    );
  }

  renderUserInformation() {
    if (!this.props.portfolio) {
      return "Loading Currency Data";
    }

    return `Are you sure Do you want to Delete: ${this.props.match.params.symbol}?`;
  }

  render() {
    return (
      <Model
        title="Delete Currency"
        content={this.renderUserInformation()}
        actions={this.renderAction()}
        onDismiss={() => history.push(`/portfolio/${this.props.portfolio.id}`)}
      />
    );
  }
}

const mapStateToProps = (state, ownProps) => {
  return { portfolio: state.portfolio[ownProps.match.params.id] };
};

export default connect(mapStateToProps, {
  deleteCurrency,
  fetchCurrency,
})(DeleteCurrency);
