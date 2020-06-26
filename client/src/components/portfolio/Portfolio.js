import React from "react";
import Header from "./Header";
import Content from "./Content";
import Footer from "./Footer";
import { fetchUser, fetch_currency } from "../../actions";
import { connect } from "react-redux";

class Portfolio extends React.Component {
  componentDidMount() {
    this.props.fetchUser(this.props.match.params.id);
    this.props.fetch_currency(this.props.match.params.id);
  }

  render() {
    if (!this.props.user || !this.props.portfolio) {
      return <div>Loading Portfolio</div>;
    }
    return (
      <div>
        <Header username={this.props.user.username} />
        <Content
          currency_list={this.props.portfolio.currency_list}
          total_value={this.props.portfolio.total_value}
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

export default connect(mapStateToProps, { fetchUser, fetch_currency })(
  Portfolio
);
