import React from "react";
import { connect } from "react-redux";
import { fetchUser } from "../../actions";
import { Link } from "react-router-dom";

class UserAccount extends React.Component {
  componentDidMount() {
    this.props.fetchUser();
  }

  renderPage() {
    return (
      <div className="row justify-content-center">
        <div className="col-xl-10 col-lg-12 col-md-9">
          <div className="card o-hidden border-0 shadow-lg my-5">
            <div className="card-body p-0">
              <div className="row">
                <div className="col">
                  <div className="p-5">
                    <div className="text-center">
                      <h1 className="h4 text-gray-900 mb-4">Account Page</h1>
                    </div>
                    <div className="text-center">
                      <p>User Name: {this.props.user.username}</p>
                    </div>
                    <div className="text-center">
                      <p>Email: {this.props.user.email}</p>
                    </div>
                    <div className="text-center">
                      <Link
                        className="small"
                        to={`/form/edit/${this.props.match.params.id}`}
                      >
                        Edit Account
                      </Link>
                    </div>
                    <div className="text-center">
                      <Link
                        className="small"
                        to={`/form/delete/${this.props.match.params.id}`}
                      >
                        Delete Account
                      </Link>
                    </div>
                    <div className="text-center">
                      <Link
                        className="small"
                        to={`/portfolio/${this.props.match.params.id}`}
                      >
                        Back To Portfolio
                      </Link>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }

  render() {
    if (!this.props.user) {
      return "Loading Account Information";
    }
    return <div className="container">{this.renderPage()}</div>;
  }
}

const mapStateToProps = (state, ownProps) => {
  return { user: state.user[ownProps.match.params.id] };
};

export default connect(mapStateToProps, { fetchUser })(UserAccount);
