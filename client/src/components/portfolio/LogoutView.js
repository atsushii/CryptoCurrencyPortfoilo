import React, { Fragment } from "react";
import { connect } from "react-redux";
import { fetchUser, logoutUser, reFetchUser } from "../../actions";
import Model from "../Model";
import { Link } from "react-router-dom";
import history from "../../history";

class LogoutView extends React.Component {
  // get user information
  componentDidMount() {
    this.props.fetchUser();
  }

  renderAction() {
    return (
      <Fragment>
        <button
          onClick={() => this.props.logoutUser(this.props.match.params.id)}
          className="btn btn-danger"
        >
          Logout
        </button>
        <Link to={`/portfolio/${this.props.match.params.id}`} className="col-2">
          Cancel
        </Link>
      </Fragment>
    );
  }

  renderUserInformation() {
    if (!this.props.user) {
      return "Do you want to logout?";
    }

    return `${this.props.user.username}: Do you want to logout?`;
  }

  render() {
    return (
      <Model
        title="Logout"
        content={this.renderUserInformation()}
        actions={this.renderAction()}
        onDismiss={() => history.push("form/login")}
      />
    );
  }
}

const mapStateToProps = (state, ownProps) => {
  return { user: state.user[ownProps.match.params.id] };
};

export default connect(mapStateToProps, { fetchUser, logoutUser, reFetchUser })(
  LogoutView
);
