import React, { Fragment } from "react";
import { connect } from "react-redux";
import { fetchUser, deleteUser, reFetchUser } from "../../actions";
import Model from "../Model";
import { Link } from "react-router-dom";
import history from "../../history";

class DeleteUser extends React.Component {
  // get user information
  componentDidMount() {
    this.props.fetchUser();
  }

  renderAction() {
    return (
      <Fragment>
        <button
          onClick={() => this.props.deleteUser(this.props.match.params.id)}
          className="btn btn-danger"
        >
          Delete Account
        </button>
        <Link
          to={`/portfolio/userAccount/${this.props.match.params.id}`}
          className="col-2"
        >
          Cancel
        </Link>
      </Fragment>
    );
  }

  renderUserInformation() {
    if (!this.props.user) {
      return "Are you sure Do you want to delete your account?";
    }

    return `${this.props.user.username}: Are you sure Do you want to Delete?`;
  }

  render() {
    return (
      <Model
        title="Delete User"
        content={this.renderUserInformation()}
        actions={this.renderAction()}
        onDismiss={() => history.push("form/signup")}
      />
    );
  }
}

const mapStateToProps = (state, ownProps) => {
  return { user: state.user[ownProps.match.params.id] };
};

export default connect(mapStateToProps, { fetchUser, deleteUser, reFetchUser })(
  DeleteUser
);
