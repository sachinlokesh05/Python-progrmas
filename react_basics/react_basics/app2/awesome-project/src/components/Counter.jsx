import React, { Component } from "react";
class Counter extends Component {
  product = 100;
  state = {
    count: 5,
    tags: ["sachin", "madhu", "sanju"]
  };

  styles = {
    fontWeight: "bold",
    fontSize: "30",
    padding: "10"
  };

  handleIncrement = product => {
    // console.log('increment happend',this)
    console.log();
    this.setState({ count: this.state.count + 1 });
  };

  handleDecrement = product => {
    this.setState({ count: this.state.count - 1 });
  };

  //   renderTags() {
  //     if (this.state.tags === 0) return <p>there are no tags</p>;

  //     return (
  //       <ul>
  //         {this.state.tags.map(tag => (
  //           <li key={tag}>{tag}</li>
  //         ))}{" "}
  //       </ul>
  //     );
  //   }

  render() {
    return (
      <React.Fragment>
        <span className={this.getbadgeClasses()}>{this.formatCount()} </span>
        <button
          onClick={this.handleIncrement}
          className="btn btn-secondary btn-sm"
        >
          Increament
        </button>{" "}
        <button
          onClick={this.handleDecrement}
          style={this.styles}
          className="btn btn-secondary btn-sm"
        >
          Decrement
        </button>{" "}
        {/* {/* <ul>
    //                     {this.state.tags.map(tag => <li key = {tag}>{tag}</li>)}
        //             </ul> */}
        {/* // {this.state.tags === 0 && 'please create new tags!'} */}
        {/* //             {this.renderTags()} */}
        {/* //{" "} */}
      </React.Fragment>
    );
  }

  formatCount() {
    const { count } = this.state;
    return count === 0 ? "Zero" : count;
  }

  getbadgeClasses() {
    let classes = "badge m-2 badge-";
    classes += this.state.count === 0 ? "warning" : "primary";
    return classes;
  }
}

export default Counter;
