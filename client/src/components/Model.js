import React from "react";
import ReactDOM from "react-dom";

const Model = (props) => {
  return ReactDOM.createPortal(
    <div className="card o-hidden border-0 shadow-lg my-5">
      <div className="card-body p-0">
        <div className="row">
          <div className="col">
            <div className="p-5">
              <div className="text-center">
                <h1 className="h4 text-gray-900 mb-4">{props.title}</h1>
                <div onClick={props.onDismiss}>
                  <div onClick={(e) => e.stopPropagation()}>
                    <div style={{ "margin-top": 20 }}>{props.content}</div>
                    <div style={{ "margin-top": 20 }}>{props.actions}</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>,
    document.querySelector("#model")
  );
};

export default Model;
