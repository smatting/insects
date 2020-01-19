import React from 'react';

import {graphql, QueryRenderer} from 'react-relay';
import { makeStyles, withStyles } from "@material-ui/core/styles";

import Environment from './GraphQLEnvironment'
import FrameGrid from './FrameGrid'
import DateRange from './DateRange'

import BrowserNav from './BrowserNav'


const useStyles = makeStyles({
    root: {
    }
});

class Browser extends React.Component {

    constructor(props) {
        super();

        // const classes = useStyles();

        this.state = {
            startDate: new Date('2019-10-01T00:00:00'),
            endDate: new Date('2019-12-31T00:00:00')
        };

        // const [startDate, setStartDate] = React.useState(new Date('2019-10-01T00:00:00'));
        // const [endDate, setEndDate] = React.useState(new Date('2019-12-31T00:00:00'));
    }

    setStartDate(startDate) {
        this.setState({startDate});
    }

    setEndDate(endDate) {
        this.setState({endDate});
    }

    query_render({error, props}) {

           if (error) {
             return <div>Error!</div>;
           }
           if (!props) {
             return <div>Loading...</div>;
           }
           console.log('Frames props', props)
           console.log('Frames state', this.state)

           return (
           <div>

               <DateRange
                   startDate={this.state.startDate}
                   setStartDate={this.setStartDate.bind(this)}
                   endDate={this.state.endDate}
                   setEndDate={this.setEndDate.bind(this)}
                   />

               <FrameGrid frames={props.frames} />

           </div>

           );
    }

    render() {
      const {startDate, endDate} = this.state;
      return (
        <QueryRenderer
          environment={Environment}
          query={graphql`
          query BrowserQuery($tbegin: DateTime!, $tend: DateTime!) {
              frames(tbegin: $tbegin,
                     tend: $tend,
                     nframes: 10) {
                  id
                  url
                  timestamp
                  thumbnail
              }
            }
          `}
          render={this.query_render.bind(this)}
          variables={{tbegin: startDate, tend: endDate}}
        />
      );
    }
}

export default Browser;
