import React from "react";

class SearchBar extends React.Component {
  state = { term: "" };

  omFormSubmit = (e) => {
    e.preventDefault();
    this.props.onFormSubmit(this.state.term);
  };

  render() {
    return (
      <form
        className="d-none d-sm-inline-block form-inline mr-auto ml-md-3 my-2 my-md-0 mw-100 navbar-search"
        onSubmit={this.onFormSubmit}
      >
        <div className="input-group">
          <input
            type="text"
            className="form-control bg-light border-0 small"
            placeholder="Search for..."
            value={this.state.term}
            onChange={(e) => this.setState({ term: e.target.value })}
          />
          <div className="input-group-append">
            <button className="btn btn-primary" type="button">
              <i className="fas fa-search fa-sm"></i>
            </button>
          </div>
        </div>
      </form>
    );
  }
}

export default SearchBar;
