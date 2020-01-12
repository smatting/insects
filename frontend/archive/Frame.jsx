import React from "react";
import { withStyles } from "@material-ui/core/styles";

import {graphql, QueryRenderer} from 'react-relay';
import Environment from './GraphQLEnvironment'


const styles = theme => ({
  img: { width: "auto", height: 600 },
  placeholder: { width: 500, height: 400, backgroundColor: "grey" }
});


class Frame extends React.Component {
    query_render({error, props}) {
        console.log(props)
          if (error) {
            return <div>Error!</div>;
          }
          if (!props) {
            return <div>Loading...</div>;
          }
          return (
            <img className={this.props.classes.img} src={props.frame.url} />
          );
        }

    render() {
      return (
        <QueryRenderer
          environment={Environment}
          query={graphql`
          query FrameQuery {
            frame(id: "RnJhbWU6MjM1NjU5") {
              id
              url
            }
          }
          `}
          variables={{}}
          render={this.query_render.bind(this)}
        />
      );
    }
  }


  export default withStyles(styles)(Frame);
