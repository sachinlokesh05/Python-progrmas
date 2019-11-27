import React, { Component } from "react";
class Counter extends Component {
  state = {
    count: 0
  };

  styles = {
    fontWeight: "bold",
    fontSize: "50",
    padding: "10"
  };

  handleIncrement() {
    this.setState({ count: this.state.count + 1 });
  }
  handleDecrement() {
    this.setState({ count: this.state.count - 1 });
  }

  render() {
    return (
      <div>
        <span style={this.styles} className={this.getbadgeClasses()}>
          {" "}
          {this.formatCount()}{" "}
        </span>
        <button
          onClick={() => this.handleIncrement()}
          className="btn btn-secondary btn-sm"
          style={this.styles}
        >
          {" "}
          Increment
        </button>
        <button
          onClick={() => this.handleDecrement()}
          className="btn btn-secondary btn-sm"
          style={this.styles}
        >
          {" "}
          Decrement
        </button>
      </div>
    );
  }

  getbadgeClasses() {
    let classes = "badge m-2 badge-";
    classes += this.state.count === 0 ? "warning" : "primary";
    return classes;
  }

  formatCount() {
    const { count } = this.state;
    return count === 0 ? "Zero" : count;
  }
}

export default Counter;
