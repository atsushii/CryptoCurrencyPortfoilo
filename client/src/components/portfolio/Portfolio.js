import React from "react";
import Header from "./Header";
import Content from "./Content";
import Footer from "./Footer";
import { fetchUser, fetchCurrency } from "../../actions";
import { connect } from "react-redux";

class Portfolio extends React.Component {
  componentDidMount() {
    this.props.fetchUser();
    this.props.fetchCurrency();
  }

  render() {
    if (!this.props.user || !this.props.portfolio) {
      return <div>Loading Portfolio</div>;
    }
    return (
      <div>
        <Header
          username={this.props.user.username}
          userId={this.props.user.id}
        />
        <Content
          currencyList={this.props.portfolio.currency_list}
          totalValue={this.props.portfolio.total_value}
          userId={this.props.user.id}
        />
        <Footer />
      </div>
    );
  }
}

const mapStateToProps = (state, ownProps) => {
  return {
    user: state.user[ownProps.match.params.id],
    portfolio: state.portfolio[ownProps.match.params.id],
  };
};

export default connect(mapStateToProps, { fetchUser, fetchCurrency })(
  Portfolio
);
