import React from "react";

class Content extends React.Component {
  renderTableData() {
    return Array.from(this.props.currency_list).map((currency) => {
      const { symbol, num_hold, price, price_change_pct } = currency;
      return (
        <tr>
          <td>
            {symbol}
            <a
              className="small"
              href="{{ url_for('user_page.update_currency', currency_name=currency['symbol']) }}"
            >
              Add
            </a>
            <a
              className="small"
              href="{{ url_for('user_page.delete_currency', currency_name=currency['symbol']) }}"
            >
              Delete
            </a>
          </td>
          <td>{num_hold}</td>
          <td>${price}</td>
          <td>{price_change_pct}%</td>
        </tr>
      );
    });
  }

  render() {
    return (
      <div className="container-fluid">
        <h1 className="h3 mb-2 text-gray-800">
          Total Value: {this.props.total_value}$
        </h1>

        <div className="card shadow mb-4">
          <div className="card-header py-3">
            <h6 className="m-0 font-weight-bold text-primary">
              <a href="{{ url_for('user_page.register_currency') }}">
                Register Currency
              </a>
            </h6>
          </div>
          <div className="card-body">
            <div className="table-responsive">
              <table
                className="table table-bordered"
                id="dataTable"
                width="100%"
                cellSpacing="0"
              >
                <thead>
                  <tr>
                    <th>Currency</th>
                    <th>holdings</th>
                    <th>Price</th>
                    <th>Change</th>
                  </tr>
                </thead>
                <tfoot>
                  <tr>
                    <th>Currency</th>
                    <th>holdings</th>
                    <th>Price</th>
                    <th>Change</th>
                  </tr>
                </tfoot>
                <tbody>{this.renderTableData()}</tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Content;
