import _ from "lodash";
import React from "react";
import { connect } from "react-redux";
import { fetchUser, editUser } from "../../actions";
import UserForm from "./UserForm";

class EditUser extends React.Component {
  componentDidMount() {
    this.props.fetchUser();
  }

  onSubmit = (formValues) => {
    this.props.editUser(this.props.match.params.id, formValues);
  };

  render() {
    if (!this.props.user) {
      return <div>Loading User Information</div>;
    }
    return (
      <div>
        <UserForm
          initialValues={_.pick(this.props.user, "username", "email")}
          onSubmit={this.onSubmit}
          title="Edit a User"
          submitButton="Update"
        />
      </div>
    );
  }
}

const mapStateToProps = (state, ownProps) => {
  return { user: state.user[ownProps.match.params.id] };
};
export default connect(mapStateToProps, { fetchUser, editUser })(EditUser);
